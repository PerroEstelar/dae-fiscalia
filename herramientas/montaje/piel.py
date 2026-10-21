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

    Se corrigen las tres: tono, saturacion y valor. El tono y la saturacion
    son lo que se ve como marron; el valor es lo que se ve como oscuro. El
    valor sube como ganancia y con tope, por las razones escritas junto a
    VALOR_PIEL.

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

# El VALOR tambien, desde el 20 oct 2026.
#
#   La primera version de esta herramienta no tocaba el valor, con el
#   argumento de que la piel del Caso 3 es mas oscura porque la luz de cada
#   plano lo es, y que subirla aplanaria el grado. Sebastian vio las placas
#   ya corregidas de color y pidio la piel MAS CLARA igual.
#
#   Tenia razon y los casos aprobados lo respaldan. Valor medio de la piel:
#
#       Caso 2, aprobado     0,40 a 0,71   (Mara 0,40 · Elisa 0,47 ·
#                                            Dario 0,44 · Patricia 0,64)
#       Caso 3, corregido     0,18 a 0,38
#
#   El Caso 3 estaba por debajo de TODO el rango aprobado.
#
# La subida va como GANANCIA sobre el valor de cada pixel, no como
# desplazamiento: asi el modelado propio de la cara -la mejilla iluminada y
# la que no- se mantiene en proporcion en vez de aplastarse contra el techo.
#
# Y va con tope. Sin tope, un plano de verdad oscuro -Marta de lejos, en 0,18-
# pedia x2,5 y la cara terminaba brillando sobre una habitacion en penumbra,
# que es exactamente el aspecto de recorte pegado que esta serie no tiene.
VALOR_PIEL = 0.45
GANANCIA_MAX = 1.5

# EL TOPE NO PUEDE SER UNO SOLO PARA TODAS LAS PLACAS, 21 OCT 2026
#     El tope de 1,5 se puso contra un plano en penumbra -Marta de lejos, en
#     0,18- donde una ganancia de 2,5 dejaba la cara brillando sobre una
#     habitacion oscura. Esa razon sigue siendo buena ahi y mala en otro
#     sitio: en el Caso 4 hay siete planos de una MANO SOBRE UN ESCRITORIO
#     CLARO, y ahi el tope deja la piel cuatro veces mas oscura que la mesa
#     que la sostiene. Medido en el set ya graduado, piel contra el p75 del
#     cuadro:
#
#         en banda      r13 1,17 · r22 1,07 · r25 0,93
#         fuera         r01 0,23 · r15 0,24 · r37 0,31 · r07 0,31
#
#     O sea: donde la piel quedo bien, esta a la altura del cuarto mas claro
#     del cuadro; donde quedo mal, esta muy por debajo. Eso es lo que hay que
#     medir, no un numero fijo.
#
#     El tope pasa a ser relativo al propio cuadro: la piel puede subir hasta
#     el p75 de la imagen y nunca mas de TECHO_ABSOLUTO. En un plano en
#     penumbra el p75 es bajo y el tope vuelve a ser el de antes; en una mano
#     sobre papel blanco deja subir lo que hace falta. El motivo original del
#     tope -que la cara no brille sobre su entorno- queda intacto, porque el
#     techo ES el entorno.
TECHO_ABSOLUTO = 2.5

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


def _corrector(antes, techo=GANANCIA_MAX):
    """La funcion que lleva un pixel de piel al objetivo. Pura, sin estado."""
    centro = antes["tono"]
    giro = (((TONO_PIEL - centro) + 180) % 360 - 180)
    escala = SATUR_PIEL / max(antes["satur"], 0.01)
    ganancia = min(techo, VALOR_PIEL / max(antes["valor"], 0.01))

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
        v2 = v * (1.0 + (ganancia - 1.0) * k)
        nr, ng, nb = colorsys.hsv_to_rgb(h2, min(1.0, s2), min(1.0, v2))
        return (int(round(nr * 255)), int(round(ng * 255)), int(round(nb * 255)))
    return f, giro, escala, ganancia


def techo_de(im, antes):
    """Hasta donde puede subir la piel EN ESTA placa: su propio p75."""
    ch = im.convert("L").resize((640, 360))
    px = sorted(ch.getdata())
    p75 = px[int(len(px) * 0.75)] / 255.0
    return max(GANANCIA_MAX, min(TECHO_ABSOLUTO, p75 / max(antes["valor"], 0.01)))


def fijar(origen, destino, cube=None, tam=33):
    im = Image.open(origen).convert("RGB")
    antes = medir(im)
    if antes is None:
        im.save(destino)
        return dict(placa=os.path.basename(origen), aviso="no encuentro piel")
    f, giro, escala, ganancia = _corrector(antes, techo_de(im, antes))

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
                giro=giro, escala=escala, ganancia=ganancia)


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
        print('   objetivo tono %5.1f  satur %4.2f  valor %4.2f'
              % (TONO_PIEL, SATUR_PIEL, VALOR_PIEL))
        print('   giro %+.1f  escala de satur x%.2f  ganancia de valor x%.2f'
              % (r['giro'], r['escala'], r['ganancia']))
