# -*- coding: utf-8 -*-
r"""Compara la revision de Resolve con la de ffmpeg, cuadro a cuadro (cada 12).

    python comparar_revisiones_gj.py T1 [T3 T4]

Si las dos coinciden, la linea de Resolve es la que se penso (y el armado de
ffmpeg sirve de respaldo). Imprime la diferencia media, las peores marcas y
guarda una hoja con los 4 peores pares (Resolve | ffmpeg).
"""
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw

T = r'D:\DAE\_tmp\gj'
W, H = 480, 270


def cuadros(p, cada):
    r = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf',
                          "select='not(mod(n\\,%d))',scale=%d:%d" % (cada, W, H), '-fps_mode', 'passthrough',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    while True:
        b = r.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
    r.wait()


for L in [a.upper() for a in sys.argv[1:]]:
    a = os.path.join(T, 'revision', 'GJ_%s_v1_REVISION_INTERNA.mp4' % L)
    b = os.path.join(T, 'revision', 'GJ_%s_REVISION_FFMPEG.mp4' % L)
    difs, pares = [], []
    for k, (x, y) in enumerate(zip(cuadros(a, 12), cuadros(b, 12))):
        d = float(np.abs(x.astype(np.int16) - y.astype(np.int16)).mean())
        difs.append((d, k * 12))
        pares.append((x, y))
    v = np.array([d for d, _ in difs])
    peores = sorted(difs, reverse=True)[:4]
    print('%s  %d marcas  media %.2f  mediana %.2f  p95 %.2f  max %.2f  peores %s'
          % (L, len(v), v.mean(), np.median(v), np.percentile(v, 95), v.max(),
             [(n, round(d, 1)) for d, n in peores]), flush=True)
    hoja = Image.new('RGB', (2 * W + 10, 4 * (H + 18)), (20, 20, 20))
    dr = ImageDraw.Draw(hoja)
    for i, (d, n) in enumerate(peores):
        x, y = pares[n // 12]
        hoja.paste(Image.fromarray(x), (0, i * (H + 18) + 18))
        hoja.paste(Image.fromarray(y), (W + 10, i * (H + 18) + 18))
        dr.text((4, i * (H + 18) + 3), '%s cuadro %d  dif %.1f   Resolve | ffmpeg' % (L, n, d),
                fill=(255, 255, 0))
    hoja.save(os.path.join(T, 'comparar_%s.jpg' % L), quality=84)
print('LISTO')
