# -*- coding: utf-8 -*-
r"""Tira de cuadros de un clip, para mirar un problema de cerca.

    python tira_gj.py clip.mp4 salida.jpg [cada=12] [ancho=640] [x0 y0 x1 y1 en 1920x1080]
"""
import subprocess
import sys

from PIL import Image, ImageDraw

clip, sal = sys.argv[1], sys.argv[2]
cada = int(sys.argv[3]) if len(sys.argv) > 3 else 12
W = int(sys.argv[4]) if len(sys.argv) > 4 else 640
caja = [int(x) for x in sys.argv[5:9]] if len(sys.argv) > 8 else None
r = subprocess.run(['ffmpeg', '-v', 'error', '-i', clip, '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                    '-s', '1920x1080', '-'], capture_output=True)
fb = 1920 * 1080 * 3
n = len(r.stdout) // fb
idx = list(range(0, n, cada))
if idx[-1] != n - 1:
    idx.append(n - 1)
ims = []
for i in idx:
    im = Image.frombytes('RGB', (1920, 1080), r.stdout[i * fb:(i + 1) * fb])
    if caja:
        im = im.crop(caja)
    im = im.resize((W, int(im.height * W / im.width)))
    ims.append((i, im))
h = ims[0][1].height
cols = 4
filas = (len(ims) + cols - 1) // cols
hoja = Image.new('RGB', (cols * (W + 6) + 6, filas * (h + 6) + 6), (30, 30, 30))
d = ImageDraw.Draw(hoja)
for k, (i, im) in enumerate(ims):
    x, y = 6 + (k % cols) * (W + 6), 6 + (k // cols) * (h + 6)
    hoja.paste(im, (x, y))
    d.text((x + 4, y + 4), str(i), fill=(255, 255, 0))
hoja.save(sal, quality=85)
print('ok', n, 'cuadros', sal)
