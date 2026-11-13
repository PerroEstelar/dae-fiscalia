# -*- coding: utf-8 -*-
r"""Revisión de los exports de los videos de profes del curso SRPA y justicia restaurativa.

Para cada export de `05 EXPORTS`:
- Comprueba con ffprobe el códec (h264 High), el tamaño, la cadencia, la pista de
  audio y el número de cuadros contra la línea (intro + título + clip + cierre +
  outro), y mide la sonoridad con ebur128.
- Arma una hoja de contacto con un cuadro a mitad de cada gráfico del plan, más el
  intro, el título, un cuadro del clip sin gráfico, el cierre y el outro, en
  `D:/DAE/_tmp/srpa/rev/<video>.jpg`.

    python srpa_revision.py u3b u1b
"""
import glob
import json
import os
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
import plan_srpa as P  # noqa: E402
import srpa as S  # noqa: E402

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
REV = 'D:/DAE/_tmp/srpa/rev'
FPS = P.FPS


def export(clave):
    """El export de versión más alta que haya en 05 EXPORTS. La entrega es MP4
    (receta del 23 oct); si una versión solo existe en .mov, se toma el .mov."""
    def ruta(n):
        base = '%s/05 EXPORTS/%s' % (S.carpeta(clave), S.nombre_export(clave, n))
        return base + '.mp4' if os.path.exists(base + '.mp4') else base + '.mov'
    n = 1
    while os.path.exists(ruta(n + 1)):
        n += 1
    return ruta(n)


def sonda(f):
    j = json.loads(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-show_streams', '-show_format', '-count_packets',
                                   '-of', 'json', f], capture_output=True, text=True).stdout)
    v = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
    a = [s for s in j['streams'] if s['codec_type'] == 'audio']
    return v, a, float(j['format']['duration'])


def sonoridad(f):
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', f, '-vn', '-af', 'ebur128=peak=true',
                        '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
    s = r[r.rfind('Summary'):]
    i = re.search(r'I:\s+(-?[\d.]+) LUFS', s)
    p = re.search(r'Peak:\s+(-?[\d.]+) dBFS', s)
    return (float(i.group(1)) if i else None, float(p.group(1)) if p else None)


def cuadro(f, seg, out):
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', '%.3f' % seg, '-i', f, '-frames:v', '1',
                    '-vf', 'scale=480:270', out], check=True)


def largo_clip(clave):
    return float(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-show_entries', 'format=duration', '-of',
                                 'csv=p=0', S.compuesto_final(clave)], capture_output=True, text=True).stdout)


def hoja(clave):
    f = export(clave)
    clip = largo_clip(clave)
    fin_clip = P.CLIP0 + int(round(clip * FPS))
    marcas = [('intro', 100), ('titulo', 300)]
    for item, tipo, t0, t1, _c in P.ITEMS[clave]:
        a, b = P.cuadro(clave, t0), P.cuadro(clave, t1)
        marcas.append((item, (a + b) // 2))
    marcas += [('cierre', fin_clip + 30), ('cierre', fin_clip + 120), ('cierre', fin_clip + 200),
               ('outro', fin_clip + 215 + 60), ('outro', fin_clip + 215 + 150), ('outro', fin_clip + 215 + 190)]
    os.makedirs(REV + '/tmp', exist_ok=True)
    col = 6
    filas = (len(marcas) + col - 1) // col
    out = Image.new('RGB', (480 * col, 300 * filas), 'black')
    d = ImageDraw.Draw(out)
    fn = ImageFont.truetype(os.path.expanduser('~') + '/AppData/Local/Microsoft/Windows/Fonts/Montserrat-Medium.ttf', 18)
    for i, (nm, fr) in enumerate(marcas):
        p = '%s/tmp/%s_%03d.png' % (REV, clave, i)
        cuadro(f, fr / FPS, p)
        x, y = (i % col) * 480, (i // col) * 300
        out.paste(Image.open(p), (x, y))
        d.text((x + 6, y + 274), '%s  %d' % (nm, fr), font=fn, fill='white')
    dst = '%s/%s.jpg' % (REV, clave)
    out.save(dst, quality=82)
    return dst


def revisar(clave):
    f = export(clave)
    v, a, dur = sonda(f)
    clip = largo_clip(clave)
    esperado = P.CLIP0 + int(round(clip * FPS)) + 215 + 194
    n = int(v.get('nb_read_packets') or 0)
    I, pk = sonoridad(f)
    print('%s %s %s %dx%d %s cuadros %d (línea ~%d) audio %s  I %s LUFS pico %s  %.0f MB' % (
        clave, v['codec_name'], v.get('profile'), v['width'], v['height'], v['r_frame_rate'], n, esperado,
        'OK' if a else 'FALTA', I, pk, os.path.getsize(f) / 1e6), flush=True)
    print('  hoja', hoja(clave), flush=True)


if __name__ == '__main__':
    for k in sys.argv[1:]:
        revisar(k)
