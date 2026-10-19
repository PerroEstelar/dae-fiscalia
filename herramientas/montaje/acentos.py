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

    La correccion entra con una rampa sobre el croma (RAMPA_BAJA a RAMPA_ALTA)
    para que no quede un borde duro entre la prenda y la piel.
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


def _croma(p):
    return max(p) - min(p)


def medir(im, umbral=45):
    """Tono, saturacion y valor medios de los pixeles con color, y cuantos son."""
    ch = im.resize((640, 360)) if im.width > 640 else im
    px = list(ch.getdata())
    sel = [p for p in px if _croma(p) > umbral]
    if not sel:
        return None
    m = tuple(sum(c[i] for c in sel) / float(len(sel)) for i in range(3))
    h, s, v = colorsys.rgb_to_hsv(m[0] / 255.0, m[1] / 255.0, m[2] / 255.0)
    return dict(rgb=tuple(int(round(c)) for c in m), tono=h * 360, satur=s,
                valor=v, porcentaje=100.0 * len(sel) / len(px))


def fijar(origen, destino, color):
    """Lleva el acento de la placa al hexadecimal institucional."""
    obj = INSTITUCIONAL[color]
    ho, so, _vo = colorsys.rgb_to_hsv(obj[0] / 255.0, obj[1] / 255.0, obj[2] / 255.0)

    im = Image.open(origen).convert('RGB')
    antes = medir(im)
    if antes is None:
        im.save(destino)
        return dict(placa=os.path.basename(origen), aviso='sin pixeles de color')

    giro = ho - antes['tono'] / 360.0
    escala = so / max(antes['satur'], 0.01)

    px = im.load()
    an, al = im.size
    for y in range(al):
        for x in range(an):
            r, g, b = px[x, y]
            c = max(r, g, b) - min(r, g, b)
            if c <= RAMPA_BAJA:
                continue
            k = min(1.0, (c - RAMPA_BAJA) / float(RAMPA_ALTA - RAMPA_BAJA))
            h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            h2 = (h + giro * k) % 1.0
            s2 = min(1.0, s * (1.0 + (escala - 1.0) * k))
            nr, ng, nb = colorsys.hsv_to_rgb(h2, s2, v)
            px[x, y] = (int(round(nr * 255)), int(round(ng * 255)), int(round(nb * 255)))

    im.save(destino)
    despues = medir(im)
    return dict(placa=os.path.basename(origen), color=color,
                antes=antes, despues=despues, giro=giro * 360, escala=escala)


if __name__ == '__main__':
    # acentos.py <entrada> <salida> <azul|amarillo|rojo|neon>
    r = fijar(sys.argv[1], sys.argv[2], sys.argv[3])
    if 'aviso' in r:
        print('%-42s %s' % (r['placa'][:42], r['aviso']))
    else:
        a, d = r['antes'], r['despues']
        o = INSTITUCIONAL[r['color']]
        print('%-42s %s' % (r['placa'][:42], r['color']))
        print('   antes    #%02X%02X%02X  tono %5.1f  satur %4.2f  (%.1f%% del cuadro)'
              % (a['rgb'] + (a['tono'], a['satur'], a['porcentaje'])))
        print('   despues  #%02X%02X%02X  tono %5.1f  satur %4.2f'
              % (d['rgb'] + (d['tono'], d['satur'])))
        print('   objetivo #%02X%02X%02X  giro %+.1f grados  escala de satur x%.2f'
              % (o + (r['giro'], r['escala'])))
