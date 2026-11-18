# -*- coding: utf-8 -*-
"""El lower third (un .mov ya rendido) sobre dos cuadros de cada una de las ocho fuentes: 16 mosaicos en una hoja.
    python sim_todos.py <lt.mov> <salida.jpg>"""
import importlib, os, subprocess, glob, sys
from PIL import Image, ImageDraw
FF = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0] + '/ffmpeg.exe'
T = 'D:/DAE/_tmp/bi_u/'
sys.path.insert(0, 'D:/DAE/_repo/cursos/bienes-proceso-penal/unidades')
lt, sal = sys.argv[1], sys.argv[2]
subprocess.run([FF, '-y', '-v', 'error', '-i', lt, '-vf', "select='eq(n,96)'", '-frames:v', '1', '-pix_fmt', 'rgba', T + 'simt_o.png'])
o = Image.open(T + 'simt_o.png').convert('RGBA')
h = Image.new('RGB', (1920, 1080), (0, 0, 0))
i = 0
for k in ('4i', '3i', '1i', '2i', '3c', '4c', '2c', '1c'):
    P = importlib.import_module('plan_biu' + k)
    t0 = P.ITEMS[0][2]
    for dt in (2.5, 7.0):
        subprocess.run([FF, '-y', '-v', 'error', '-ss', '%.2f' % (t0 + dt), '-i', P.ORIGINAL, '-frames:v', '1', T + 'simt_f.png'])
        a = Image.alpha_composite(Image.open(T + 'simt_f.png').convert('RGBA'), o).convert('RGB').resize((480, 270))
        ImageDraw.Draw(a).text((6, 4), 'u' + k, fill=(255, 255, 0))
        h.paste(a, ((i % 4) * 480, (i // 4) * 270)); i += 1
h.save(sal, quality=85)
print('LISTO')
