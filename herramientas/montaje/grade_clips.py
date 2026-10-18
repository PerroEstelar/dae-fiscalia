#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade y recorte de los clips de Kling, a la misma curva que las placas.

POR QUE LOS CLIPS LLEVAN SU PROPIO GRADE
    El clip se genera sobre la placa SIN graduar, a proposito: graduar antes y
    otra vez despues comprime dos veces y aplana los medios. Asi que el clip
    sale con la luma de la placa cruda, y hay que llevarlo al mismo 23/84/205
    que el resto del set. La curva se calcula sobre un cuadro del clip, no
    sobre la placa: Kling vuelve a renderizar y mueve el histograma.

LA SATURACION SE CALCULA, NO SE ADIVINA
    El C5U3 uso un hue=s=0,72 fijo para los cuatro clips. Aqui se mide: se
    aplica la curva a un cuadro con la misma LUT, se mide el croma que queda y
    el factor sale de dividir. Un solo paso de ffmpeg con las dos cosas.

EL RECORTE
    El clip rinde mas cuadros que la ranura por diseno -se pidieron los
    segundos justos para que sobre-. Se recorta con -frames:v al numero EXACTO
    que pide la rejilla, y se reencoda a 24000/1001, que es el reloj de la
    serie; Kling entrega 24/1 exacto.
"""
import json
import os
import subprocess
import sys

from PIL import Image, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grade_placas import CROMA_OBJETIVO, OBJETIVO, croma, curva, perfiles

FPS = '24000/1001'


def _cuadro(ffmpeg, clip, n, destino):
    subprocess.run([ffmpeg, '-v', 'error', '-y', '-i', clip,
                    '-vf', "select='eq(n\\,%d)'" % n, '-fps_mode', 'passthrough',
                    '-frames:v', '1', destino], check=True)


def graduar(ffmpeg, clip, cuadros, salida, tmp):
    """Devuelve el informe; escribe la ranura ya graduada y recortada."""
    _cuadro(ffmpeg, clip, 1, tmp)
    im = Image.open(tmp).convert('RGB')
    p2, p50, p98, d0 = perfiles(im)
    lut = curva(p2, p50, p98)

    # la misma LUT sobre el cuadro, para saber que croma queda DESPUES
    prueba = im.point(lut * 3)
    cr, _ = croma(prueba)
    s = min(1.0, CROMA_OBJETIVO / cr) if cr > CROMA_OBJETIVO else 1.0

    pts = ' '.join('%.6f/%.6f' % (x / 255.0, lut[x] / 255.0)
                   for x in (0, p2, p50, p98, 255))
    vf = "curves=all='%s',hue=s=%.4f" % (pts, s)
    subprocess.run([ffmpeg, '-v', 'error', '-y', '-i', clip, '-vf', vf,
                    '-frames:v', str(cuadros), '-an', '-c:v', 'libx264',
                    '-preset', 'slow', '-crf', '14', '-pix_fmt', 'yuv420p',
                    '-g', '600', '-keyint_min', '600', '-sc_threshold', '0',
                    '-r', FPS, salida], check=True)
    os.remove(tmp)
    return dict(clip=os.path.basename(clip), antes=(p2, p50, p98),
                croma_curva=cr, saturacion=s, cuadros=cuadros)


if __name__ == '__main__':
    ffmpeg = os.environ['FFMPEG']
    trabajos = json.load(open(sys.argv[1], encoding='utf-8'))
    print('%-24s %14s %8s %7s %7s' % ('clip', 'antes', 'croma', 'satur', 'cuadr'))
    for t in trabajos:
        r = graduar(ffmpeg, t['clip'], t['cuadros'], t['salida'],
                    t['salida'] + '.tmp.png')
        print('%-24s %14s %8.2f %7.3f %7d' % (
            r['clip'][:24], '%d/%d/%d' % r['antes'], r['croma_curva'],
            r['saturacion'], r['cuadros']))
