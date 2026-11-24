# -*- coding: utf-8 -*-
"""Hoja de contactos de una lección capturada (o marcada): 3 columnas, número de página encima."""
import glob, os, sys
from PIL import Image, ImageDraw, ImageFont
src, salida = sys.argv[1], sys.argv[2]
desde = int(sys.argv[3]) if len(sys.argv) > 3 else 1
hasta = int(sys.argv[4]) if len(sys.argv) > 4 else 99
fs = [f for f in sorted(glob.glob(os.path.join(src, '*.png'))) if desde <= int(f[-6:-4]) <= hasta]
C, TW, TH = 3, 520, 292
F = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', 22)
filas = (len(fs) + C - 1) // C
im = Image.new('RGB', (C * (TW + 10) + 10, filas * (TH + 40) + 10), 'white')
d = ImageDraw.Draw(im)
for i, f in enumerate(fs):
    x, y = 10 + (i % C) * (TW + 10), 10 + (i // C) * (TH + 40)
    d.text((x, y), os.path.basename(f)[:-4], font=F, fill=(200, 0, 0))
    im.paste(Image.open(f).convert('RGB').resize((TW, TH), Image.LANCZOS), (x, y + 30))
im.save(salida)
print(len(fs), im.size)
