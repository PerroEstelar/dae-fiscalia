# -*- coding: utf-8 -*-
r"""Simulación de un plan de profe sobre su compuesto, antes de armar la línea (17 nov 2026).

Es `dh_sim*.py` de Derechos humanos para cualquier plan. Hojas de 24 cuadros (640×360), una
fila de cuatro, en `<P.TMP>/sim/`:
- cada cartón y el lower third rendidos, encima del cuadro del compuesto en su tiempo (el lower
  third, en cuatro momentos: el profe se mueve);
- cada lista con la caja dibujada (x 86 → 170 + MAXW, y 250–690) en su último segundo, que es
  cuando están todas las filas;
- tiras a 4 cuadros por segundo de los tramos pedidos (planos cerrados, cortes), y tiras cuadro
  a cuadro alrededor de un punto (congelados, cambios de ventana).

    python profe_sim.py plan_sr1c [nombre=a-b ...] [nombre@t ...]

`nombre=a-b` es una tira de a a b segundos de la fuente (no puede cruzar un corte);
`nombre@t` son 24 cuadros seguidos del compuesto alrededor del segundo t de la fuente.
Al final compara los cuadros del compuesto con los esperados por `TRAMOS`.
"""
import glob
import importlib
import os
import subprocess
import sys

from PIL import Image, ImageDraw

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
AQUI = os.path.dirname(os.path.abspath(__file__))
plan = sys.argv[1]
for _r, _d, _f in os.walk(os.path.join(AQUI, '..', '..', 'cursos')):
    if plan + '.py' in _f:
        sys.path.insert(0, _r)
        break
P = importlib.import_module(plan)
T = P.TMP + '/sim/'
os.makedirs(T, exist_ok=True)
log = open(T + 'sim.log', 'w', encoding='utf-8')
MAXW = getattr(P, 'MAXW', 615)


def ct(t):
    """Segundo de la fuente -> segundo del compuesto, exacto: se suman los tramos anteriores. Antes
    pasaba por `P.cuadro` (la rejilla de 23,976 de la línea) y el cuadro podía ser el de al lado."""
    acum = 0.0
    for a, b, _w in getattr(P, 'TRAMOS', None) or [(P.T0, P.T1, None)]:
        if a - 1e-6 <= t and (b is None or t <= b + 1e-6):
            return acum + t - a
        acum += b - a
    raise ValueError('%.2f cae en un corte' % t)


def cuadro_comp(t, out):
    """El cuadro del compuesto que está en pantalla en el segundo t. Se busca 4 ms antes: con el
    tiempo redondeado a milésimas, un cuadro en 687,66667 se pedía como 687,667 y salía el siguiente
    (desarrollo de la U4 de SRPA: las tiras cuadro a cuadro de los cortes salían corridas un cuadro)."""
    if os.path.exists(out):
        os.remove(out)
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', '%.4f' % max(0.0, t - 0.004), '-i', P.COMPUESTO,
                    '-frames:v', '1', out])
    return Image.open(out).convert('RGBA')


def cuadro_mov(f, k, out):
    if os.path.exists(out):
        os.remove(out)
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', f, '-vf', 'select=eq(n\\,%d)' % k,
                    '-frames:v', '1', out])
    return Image.open(out).convert('RGBA')


def hoja(tiles, nombre, cols=4, w=640, h=360):
    for n in range(0, len(tiles), 24):
        lote = tiles[n:n + 24]
        H = Image.new('RGB', (w * cols, h * ((len(lote) + cols - 1) // cols)), (20, 20, 20))
        for k, im in enumerate(lote):
            H.paste(im, ((k % cols) * w, (k // cols) * h))
        H.save(T + '%s_%d.jpg' % (nombre, n // 24), quality=82)
        print(nombre, n // 24, len(lote), file=log, flush=True)


tiles = []
for clave, tipo, t0, t1, d in P.ITEMS:
    if tipo == 'lt':
        ts = [t0 + 0.8, t0 + 3, t0 + 5.5, t1 - 0.6]
    elif tipo == 'carton':
        ts = [(t0 + t1) / 2]
    else:
        ts = [t1 - 1.0]
    for t in ts:
        im = cuadro_comp(ct(t), T + 'c.png')
        if tipo in ('carton', 'lt'):
            _v = getattr(P, 'VERSIONES', {}).get(clave)
            f = '%s/02 CARTONES/%s_%s%s.mov' % (P.R, P.PREFIJO, clave, ' v%d' % _v if _v else '')
            ov = cuadro_mov(f, int(round((t - t0) * P.FPS)), T + 'o.png')
            im = Image.alpha_composite(im, ov)
        else:
            ImageDraw.Draw(im).rectangle([86, 250, 86 + 84 + MAXW, 690], outline=(0, 255, 255), width=4)
        im = im.convert('RGB').resize((640, 360))
        ImageDraw.Draw(im).text((6, 4), '%s %.1f' % (clave, t), fill=(255, 255, 0))
        tiles.append(im)
hoja(tiles, 'sim_' + P.PREFIJO)
for arg in sys.argv[2:]:
    ts = []
    if '=' in arg:
        nombre, r = arg.split('=')
        a, b = (float(x) for x in r.split('-'))
        t = a
        while t < b - 0.05:
            ts.append((ct(t), '%.2f' % t))
            t += 0.25
    else:
        nombre, t = arg.split('@')
        fc = str(getattr(P, 'FPS_COMPUESTO', 30)).split('/')
        fc = float(fc[0]) / float(fc[1]) if len(fc) > 1 else float(fc[0])
        k0 = int(round(ct(float(t)) * fc))        # el cuadro del compuesto que empieza en t
        ts = [((k0 + k - 12) / fc, '%+d' % (k - 12)) for k in range(24)]
    tl = []
    for tc, rot in ts:
        im = cuadro_comp(tc, T + 'c.png').convert('RGB').resize((480, 270))
        ImageDraw.Draw(im).text((6, 4), rot, fill=(255, 255, 0))
        tl.append(im)
    hoja(tl, 'tira_' + nombre, cols=6, w=480, h=270)
r = subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-count_packets', '-show_entries',
                    'stream=codec_type,nb_read_packets,duration', '-of', 'csv=p=0', P.COMPUESTO],
                   capture_output=True, text=True)
esp = sum(b - a for a, b, _w in P.TRAMOS)
print('compuesto', r.stdout.replace(chr(10), ' | '), 'esperado %.3f s = %d cuadros a 30' % (esp, round(esp * 30)),
      file=log, flush=True)
print('LISTO', file=log, flush=True)
