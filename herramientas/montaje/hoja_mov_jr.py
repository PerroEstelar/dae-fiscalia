# -*- coding: utf-8 -*-
r"""Hoja para mirar la capa de movimiento / detalle de Justicia restaurativa.

    python hoja_mov_jr.py salida.jpg clip1.mp4 [clip2.mp4 ...]

Por clip una fila: cuadro 0 | cuadro 12 | medio | ultimo. Si el clip es de
MOVIMIENTO, se le antepone el cuadro 0 de su RANURA (para ver el empalme).
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

W, H = 480, 270


def cuadros(p):
    o = subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0',
                        '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', p],
                       capture_output=True, text=True).stdout.strip()
    return int(o or 0)


def cuadro(p, i):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf',
                        'select=eq(n\\,%d),scale=%d:%d' % (i, W, H), '-frames:v', '1',
                        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True)
    if len(r.stdout) < W * H * 3:
        return Image.new('RGB', (W, H), (60, 0, 0))
    return Image.frombytes('RGB', (W, H), r.stdout[:W * H * 3])


sal, clips = sys.argv[1], sys.argv[2:]
hoja = Image.new('RGB', (W * 5 + 60, (H + 26) * len(clips) + 10), (30, 30, 30))
d = ImageDraw.Draw(hoja)
for k, c in enumerate(clips):
    y = 10 + k * (H + 26)
    n = cuadros(c)
    d.text((10, y), '%s  (%d cuadros)' % (os.path.basename(c), n), fill=(230, 230, 230))
    fila = []
    if os.sep + 'MOVIMIENTO' + os.sep in c:
        base = os.path.basename(c).replace('_mov_v', '_v')
        rr = os.path.join(os.path.dirname(os.path.dirname(c)), 'RANURAS', base)
        fila.append(('ranura 0', cuadro(rr, 0)))
    for etq, i in (('0', 0), ('12', 12), ('medio', n // 2), ('ultimo', max(0, n - 1))):
        fila.append((etq, cuadro(c, i)))
    for j, (etq, im) in enumerate(fila):
        x = 10 + j * (W + 10)
        hoja.paste(im, (x, y + 18))
        d.text((x + 4, y + 20), etq, fill=(255, 255, 0))
hoja.save(sal, quality=84)
print('ok', sal)
