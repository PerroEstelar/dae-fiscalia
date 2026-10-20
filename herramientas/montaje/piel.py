#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lleva la piel de una placa al gris calido desaturado de la serie.

POR QUE HACE FALTA
    La direccion de arte de la serie dice que la piel va en un "gris calido
    desaturado, apenas tenido". El modelo no entrega eso de forma estable: en
    el Caso 3 salio sistematicamente mas saturada y mas roja que en los dos
    casos que Sebastian ya aprobo.

    Medido el 20 oct 2026 sobre las placas de los tres casos, en la poblacion
    de pixeles calidos de saturacion media -que en este sistema es la piel,
    porque todo lo demas es gris o es el acento-:

        Caso 1, aprobado     tono 19 a 37    satur 0,18 a 0,23
        Caso 2, aprobado     tono 12 a 34    satur 0,16 a 0,28
        Caso 3               tono  0 a 26    satur 0,29 a 0,33

    Un tono cerca de 0 grados con saturacion 0,3 se lee como marron rojizo.
    Los mismos rasgos en tono 26 con saturacion 0,19 se leen como gris
    calido. La diferencia no es de luz ni de grado: es de cuanto color.

QUE TOCA Y QUE NO
    Solo la poblacion de piel: calida, y con la saturacion entre SAT_MIN y
    SAT_MAX. SAT_MAX esta por DEBAJO del piso de `acentos.py` (0,45), asi que
    un acento institucional nunca entra aqui, ni siquiera en el borde donde
    la prenda se funde con la mano.

    El VALOR no se toca. La piel del Caso 3 es mas oscura que la del Caso 2,
    pero eso es la luz de cada plano y corregirlo aplanaria el grado. Lo que
    se corrige es el color, que es lo que se ve como marron.

LA MISMA CORRECCION VA AL CLIP
    La capa de movimiento se genera a partir de la placa, asi que si la placa
    cambia el clip deja de calzar. `cube()` escribe la correccion como LUT 3D
    y ffmpeg la aplica al clip con lut3d: misma funcion, mismo resultado, sin
    volver a generar nada.
"""
import colorsys
import math
import os
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

TONO_PIEL = 26.0          # el centro de los dos casos aprobados
SATUR_PIEL = 0.19

SAT_MIN, SAT_MAX = 0.10, 0.42     # 0,42 queda bajo el piso del acento (0,45)
RAMPA = 0.06                      # suavizado en los dos extremos de la banda
VENTANA = 45.0                    # grados alrededor de la piel MEDIDA


def _hsv(r, g, b):
    return colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)


def _dist(a, b):
    return abs(((a - b + 180) % 360) - 180)


def medir(im, centro=None):
    """Tono, saturacion y valor medios de la piel, y cuanta hay."""
    ch = im.resize((640, 360)) if im.width > 640 else im
    px = list(ch.getdata())
    hs, ss, vs = [], [], []
    for r, g, b in px:
        mx = max(r, g, b)
        if mx < 30:
            continue
        s = (mx - min(r, g, b)) / float(mx)
        if not (SAT_MIN <= s <= SAT_MAX):
            continue
        h, _, v = _hsv(r, g, b)
        h *= 360
        if centro is None:
            if not (h <= 70 or h >= 350):
                continue
        elif _dist(h, centro) > VENTANA:
            continue
        hs.append(h)
        ss.append(s)
        vs.append(v)
    if len(hs) < 120:
        return None
    sx = sum(math.cos(math.radians(h)) for h in hs)
    sy = sum(math.sin(math.radians(h)) for h in hs)
    return dict(tono=math.degrees(math.atan2(sy, sx)) % 360,
                satur=sum(ss) / len(ss), valor=sum(vs) / len(vs),
                porcentaje=100.0 * len(hs) / len(px))


def _peso(s):
    """1 en el centro de la banda, 0 fuera, con rampa en los dos extremos."""
    if s <= SAT_MIN or s >= SAT_MAX:
        return 0.0
    return min(1.0, (s - SAT_MIN) / RAMPA, (SAT_MAX - s) / RAMPA)


def _corrector(antes):
    """La funcion que lleva un pixel de piel al objetivo. Pura, sin estado."""
    centro = antes["tono"]
    giro = (((TONO_PIEL - centro) + 180) % 360 - 180)
    escala = SATUR_PIEL / max(antes["satur"], 0.01)

    def f(r, g, b):
        mx = max(r, g, b)
        if mx < 30:
            return None
        s = (mx - min(r, g, b)) / float(mx)
        k = _peso(s)
        if k <= 0.0:
            return None
        h, sa, v = _hsv(r, g, b)
        if _dist(h * 360, centro) > VENTANA:
            return None
        h2 = ((h * 360 + giro * k) % 360) / 360.0
        s2 = sa * (1.0 + (escala - 1.0) * k)
        nr, ng, nb = colorsys.hsv_to_rgb(h2, min(1.0, s2), v)
        return (int(round(nr * 255)), int(round(ng * 255)), int(round(nb * 255)))
    return f, giro, escala


def fijar(origen, destino, cube=None, tam=33):
    im = Image.open(origen).convert("RGB")
    antes = medir(im)
    if antes is None:
        im.save(destino)
        return dict(placa=os.path.basename(origen), aviso="no encuentro piel")
    f, giro, escala = _corrector(antes)

    px = im.load()
    an, al = im.size
    for y in range(al):
        for x in range(an):
            n = f(*px[x, y])
            if n is not None:
                px[x, y] = n
    im.save(destino)
    if cube:
        escribir_cube(cube, f, tam)
    return dict(placa=os.path.basename(origen), antes=antes,
                despues=medir(im, antes["tono"] + giro),
                giro=giro, escala=escala)


def escribir_cube(ruta, f, tam=33):
    """La misma correccion, como LUT 3D, para aplicarla al clip con ffmpeg."""
    with open(ruta, "w", encoding="ascii") as fh:
        fh.write("TITLE \"piel DAE\"\nLUT_3D_SIZE %d\n" % tam)
        d = 255.0 / (tam - 1)
        for b in range(tam):
            for g in range(tam):
                for r in range(tam):
                    R, G, B = int(round(r * d)), int(round(g * d)), int(round(b * d))
                    n = f(R, G, B) or (R, G, B)
                    fh.write("%.6f %.6f %.6f\n"
                             % (n[0] / 255.0, n[1] / 255.0, n[2] / 255.0))


if __name__ == '__main__':
    # piel.py <entrada> <salida> [salida.cube]
    r = fijar(sys.argv[1], sys.argv[2],
              sys.argv[3] if len(sys.argv) > 3 else None)
    print('%-42s' % r['placa'][:42])
    if 'aviso' in r:
        print('   %s' % r['aviso'])
    else:
        a, d = r['antes'], r['despues']
        print('   antes    tono %5.1f  satur %4.2f  valor %4.2f  (%.1f%% del cuadro)'
              % (a['tono'], a['satur'], a['valor'], a['porcentaje']))
        print('   despues  tono %5.1f  satur %4.2f  valor %4.2f'
              % (d['tono'], d['satur'], d['valor']) if d else '   despues  -')
        print('   objetivo tono %5.1f  satur %4.2f   giro %+.1f  escala x%.2f'
              % (TONO_PIEL, SATUR_PIEL, r['giro'], r['escala']))
