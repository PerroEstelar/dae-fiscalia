# -*- coding: utf-8 -*-
"""Hoja de contactos solo con las diapositivas marcadas (no las de Bien así ni las repetidas de portada/pies)."""
import glob, importlib.util, os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '/home/claude/marcas')
import aplicar
cur, lecs, salida = sys.argv[1], sys.argv[2].split(','), sys.argv[3]
S = aplicar.specs(cur)
omit = set(sys.argv[4].split(',')) if len(sys.argv) > 4 else set()
fs = []
for lec in lecs:
    for n, (c, mk) in sorted(S[lec].items()):
        if mk and c.split(':')[0] not in omit:
            fs.append('/home/claude/marcas/marcados/%s/%s/%s - %02d.png' % (cur, lec, lec, n))
C, TW, TH = 3, 520, 292
F = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', 22)
filas = (len(fs) + C - 1) // C
im = Image.new('RGB', (C * (TW + 10) + 10, filas * (TH + 40) + 10), 'white'); d = ImageDraw.Draw(im)
for i, f in enumerate(fs):
    x, y = 10 + (i % C) * (TW + 10), 10 + (i // C) * (TH + 40)
    d.text((x, y), os.path.basename(f)[:-4], font=F, fill=(200, 0, 0))
    im.paste(Image.open(f).convert('RGB').resize((TW, TH), Image.LANCZOS), (x, y + 30))
im.save(salida); print(len(fs))
