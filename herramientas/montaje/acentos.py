#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fija los acentos institucionales de una placa, sin tocar los grises.

POR QUE HACE FALTA
    El Manual de Identidad fija los colores institucionales por hexadecimal y
    eso es regla dura. Pero el modelo no los entrega: acierta el TONO y falla
    la SATURACION, sistematicamente y por la mitad.

    Medido el 19 oct 2026 en las dos primeras hojas de personaje del
    PRIORIDAD 03:

        azul      tono 211,1 vs 210,2   satur 0,49 vs 0,95   valor 0,64 vs 0,62
        amarillo  tono  37,4 vs  46,1   satur 0,49 vs 0,94   valor 0,92 vs 0,99

    El azul es el azul correcto, lavado. El amarillo ademas se corre nueve
    grados hacia el naranja. Regenerar no lo arregla -es como pinta el modelo-
    y cuesta creditos; corregirlo cuesta cero y es exacto.

QUE HACE, Y QUE NO
    Solo toca los pixeles que YA llevan color. El sistema de la casa tiene el
    entorno enteramente en grises, asi que los pixeles de croma bajo son el
    noventa y pico por ciento del cuadro y deben quedar intactos: cualquier
    operacion global los tenirian.

    Sobre los pixeles de color:
      - el TONO se rota hasta el del objetivo
      - la SATURACION se escala para que la MEDIA caiga en la del objetivo,
        no se aplana a un valor fijo: aplanarla mata el modelado suave de la
        prenda, que es justo lo que sostiene el volumen sin contorno
      - el VALOR no se toca, y por eso el dibujo no cambia de forma

    La correccion entra con DOS rampas, y pesa la menor de las dos: una sobre
    el croma (RAMPA_BAJA a RAMPA_ALTA) para que no quede borde duro entre la
    prenda y el fondo, y otra sobre la saturacion (SAT_BAJA a SAT_ALTA), que
    es la que de verdad deja la piel fuera. El tono no sirve para eso: en las
    placas del Caso 3 el panuelo de Marta y su propia piel estan a doce grados
    uno de otra.
"""
import colorsys
import os
import sys

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

INSTITUCIONAL = {
    'azul': (0x08, 0x53, 0x9F),
    'amarillo': (0xFC, 0xC5, 0x0E),
    'rojo': (0xE4, 0x1E, 0x29),
    'neon': (0xE9, 0xDF, 0x00),
}

RAMPA_BAJA, RAMPA_ALTA = 25, 55      # croma donde la correccion entra y satura

# Rampa de SATURACION. Es lo que de verdad separa el acento de la piel.
#
# MEDIDO EL 20 OCT 2026 EN LAS PLACAS DEL CASO 3
#   El panuelo de Marta salio en tono 25,7 y su piel en tono 13,2: el tono NO
#   los separa, y en kf13 estan todavia mas cerca. Lo que si los separa, y por
#   mucho, es la saturacion:
#
#       acento    satur 0,80 a 1,00   (panuelo, banda, delantal)
#       piel      satur 0,30 a 0,40
#
#   Entre 0,45 y 0,62 no hay nada en ninguna de las placas del caso, asi que
#   la rampa cabe entera en tierra de nadie. Va como rampa y no como umbral
#   duro porque la sombra propia de la prenda baja hasta 0,50 -el delantal de
#   Teresa vive entre 0,50 y 0,90- y un umbral dejaria una costura visible en
#   el pliegue.
SAT_BAJA, SAT_ALTA = 0.45, 0.62

# Cuanto se busca el acento alrededor del hexadecimal objetivo. Es ancho a
# proposito: sirve para ENCONTRARLO, no para decidir que se toca.
BUSQUEDA = 90.0

# Ventana de TONO, en grados, alrededor del acento MEDIDO -no del objetivo-.
# Fuera de ella no se toca nada.
#
# EL ERROR QUE ESTO CORRIGE, 20 OCT 2026
#   La version anterior centraba la ventana en el HEXADECIMAL OBJETIVO. Un
#   acento que se hubiera ido mas grados que la ventana quedaba invisible
#   para la herramienta: `medir` no encontraba un solo pixel y la placa salia
#   intacta, sin aviso util. Paso con los tres amarillos del Caso 3, que
#   cayeron entre 17 y 30 grados con una ventana de 14 alrededor de 46.
#
#   Ahora el acento se LOCALIZA primero por saturacion -que es lo que lo
#   distingue de la piel- y la ventana se centra donde esta de verdad. La
#   ventana sigue haciendo falta para separar dos acentos distintos en la
#   misma placa.
#
# POR QUE HACE FALTA, MEDIDO EL 19 OCT 2026
#   Corriendo acentos DESPUES del grade, la camisa azul de Victor pedia un giro
#   de -26,6 grados. Sin ventana ese giro se aplicaba a TODO pixel con croma
#   sobre 25, y despues del grade la piel y el pelo ya pasaban ese umbral: la
#   piel, que esta en tono ~30, salia rotada a ~3 y la placa quedo con la cara
#   magenta y el pelo rojo. El umbral de croma solo no basta.
#
#   Ya no hace falta que la ventana del amarillo sea estrecha para dejar
#   fuera la piel: de eso se encarga la rampa de saturacion. Lo que la
#   ventana mide ahora es cuanto se abre el acento sobre si mismo -luz y
#   sombra de la misma prenda-, y 25 grados sobran para eso.
VENTANA = {
    'azul': 45.0,
    'amarillo': 25.0,
    'rojo': 25.0,
    'neon': 25.0,
}


def _croma(p):
    return max(p) - min(p)


def _satur(p):
    mx = max(p)
    return 0.0 if mx == 0 else (mx - min(p)) / float(mx)


def _tono(p):
    return colorsys.rgb_to_hsv(p[0] / 255.0, p[1] / 255.0, p[2] / 255.0)[0] * 360


def _dist(a, b):
    return abs(((a - b + 180) % 360) - 180)


def _media_circular(hs):
    import math
    sx = sum(math.cos(math.radians(h)) for h in hs)
    sy = sum(math.sin(math.radians(h)) for h in hs)
    return math.degrees(math.atan2(sy, sx)) % 360


def localizar(im, color):
    """Donde esta el acento DE VERDAD en esta placa, no donde deberia estar.

    Se queda con los pixeles saturados -lo unico que distingue el acento de
    la piel-, busca el racimo de tono mas poblado dentro de BUSQUEDA grados
    del objetivo, y devuelve su centro. Si la placa trae dos acentos, cada
    uno es su propio racimo y el objetivo decide cual.
    """
    obj = INSTITUCIONAL[color]
    ho = _tono(obj)
    ch = im.resize((640, 360)) if im.width > 640 else im
    px = list(ch.getdata())
    sel = [p for p in px
           if _croma(p) > RAMPA_BAJA and _satur(p) >= SAT_ALTA
           and _dist(_tono(p), ho) <= BUSQUEDA]
    if not sel:
        return None
    cubos = {}
    for p in sel:
        cubos.setdefault(int(_tono(p) // 5) * 5, []).append(p)
    pico = max(cubos, key=lambda k: len(cubos[k]))
    cerca = [p for p in sel if _dist(_tono(p), pico + 2.5) <= VENTANA[color]]
    return dict(centro=_media_circular([_tono(p) for p in cerca]),
                satur=sum(_satur(p) for p in cerca) / float(len(cerca)),
                porcentaje=100.0 * len(cerca) / len(px),
                rgb=tuple(int(round(sum(c[i] for c in cerca) / float(len(cerca))))
                          for i in range(3)))


def medir(im, color):
    """Lo que hay hoy en la placa, para informar antes y despues."""
    return localizar(im, color)


def fijar(origen, destino, color):
    """Lleva el acento de la placa al hexadecimal institucional.

    Un pixel se corrige en la medida en que cumple las TRES condiciones:
    croma sobre RAMPA_BAJA, saturacion sobre la rampa SAT_BAJA..SAT_ALTA, y
    tono dentro de VENTANA[color] del acento medido. El peso es el menor de
    las dos rampas, para que ni el borde de la prenda ni su sombra propia
    queden con costura.
    """
    obj = INSTITUCIONAL[color]
    ho, so, _vo = colorsys.rgb_to_hsv(obj[0] / 255.0, obj[1] / 255.0, obj[2] / 255.0)
    vent = VENTANA[color]

    im = Image.open(origen).convert("RGB")
    antes = localizar(im, color)
    if antes is None:
        im.save(destino)
        return dict(placa=os.path.basename(origen), color=color,
                    aviso="no encuentro acento saturado cerca de %s" % color)

    centro = antes["centro"]
    giro = (((ho * 360 - centro) + 180) % 360 - 180) / 360.0
    escala = so / max(antes["satur"], 0.01)

    px = im.load()
    an, al = im.size
    for y in range(al):
        for x in range(an):
            r, g, b = px[x, y]
            c = max(r, g, b) - min(r, g, b)
            if c <= RAMPA_BAJA:
                continue
            h, sa, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            if sa <= SAT_BAJA:
                continue
            if _dist(h * 360, centro) > vent:
                continue
            k = min((c - RAMPA_BAJA) / float(RAMPA_ALTA - RAMPA_BAJA),
                    (sa - SAT_BAJA) / float(SAT_ALTA - SAT_BAJA), 1.0)
            h2 = (h + giro * k) % 1.0
            s2 = min(1.0, sa * (1.0 + (escala - 1.0) * k))
            nr, ng, nb = colorsys.hsv_to_rgb(h2, s2, v)
            px[x, y] = (int(round(nr * 255)), int(round(ng * 255)), int(round(nb * 255)))

    im.save(destino)
    return dict(placa=os.path.basename(origen), color=color,
                antes=antes, despues=localizar(im, color),
                giro=giro * 360, escala=escala)


if __name__ == '__main__':
    # acentos.py <entrada> <salida> <azul|amarillo|rojo|neon>
    r = fijar(sys.argv[1], sys.argv[2], sys.argv[3])
    print('%-42s %s' % (r['placa'][:42], r['color']))
    if 'aviso' in r:
        print('   %s' % r['aviso'])
    else:
        a, d = r['antes'], r['despues']
        o = INSTITUCIONAL[r['color']]
        print('   antes    #%02X%02X%02X  tono %5.1f  satur %4.2f  (%.2f%% del cuadro)'
              % (a['rgb'] + (a['centro'], a['satur'], a['porcentaje'])))
        print('   despues  #%02X%02X%02X  tono %5.1f  satur %4.2f'
              % (d['rgb'] + (d['centro'], d['satur'])))
        print('   objetivo #%02X%02X%02X  giro %+.1f grados  escala de satur x%.2f'
              % (o + (r['giro'], r['escala'])))
