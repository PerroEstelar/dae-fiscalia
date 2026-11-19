# -*- coding: utf-8 -*-
"""Ley 1826, videos de profe (19 nov 2026): le pone la pluma de los bordes a un recortado que se hizo sin ella.

Los cuatro primeros recortes (inicio del curso, inicio y cierre de la U1, inicio de la U2) salieron antes de que
`recorta_cuadro.py` tuviera `--pluma-x/--pluma-y`: una mano que tocaba el borde izquierdo de la fuente, o la cabeza
el de arriba, quedaba cortada por una linea recta en medio del fondo. No hace falta volver a pasar el modelo (37 a
52 min por video): el recortado es fgr*a + fondo*(1-a), y mezclarlo con el fondo con el peso w de la rampa da
fgr*a*w + fondo*(1-a*w), que es lo mismo que haber multiplicado el alfa por la rampa. Se hace con un PNG del fondo
(el mismo que usa `recorta_cuadro.py`: PIL, LANCZOS a 1920x1080) con alfa 1-w, puesto encima con ffmpeg.

Uso: emplumar.py <clave> [<clave> ...]      (lpci, lpu1i, lpu1c, lpu2i)
El recortado sin pluma queda en `01 VIDEO/_descartes/<nombre>_recortado_sin_pluma.mp4`; el mate no cambia (es el
alfa del modelo, sin pluma). Cuenta los cuadros antes de cambiar nada. Log: emplumar.log"""
import os
import shutil
import subprocess
import sys
import time
from glob import glob

import numpy as np
from PIL import Image

FB = glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
T = 'D:/DAE/_tmp/lp_p/'
R = 'E:/DAE MASTER/PRIORIDAD 1/CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO/VIDEOS PROFE/'
FONDO = R + '00 FONDOS/FONDO 4 V2.png'
PIEZAS = {'lpci': ('CURSO/INICIO', 'lp_curso_inicio'), 'lpu1i': ('UNIDAD 1/INICIO', 'lp_u1_inicio'),
          'lpu1c': ('UNIDAD 1/CIERRE', 'lp_u1_cierre'), 'lpu2i': ('UNIDAD 2/INICIO', 'lp_u2_inicio')}
CW, CH = 1920, 1080
W, H, X0, Y0 = 1728, 972, 386, 108          # el rectangulo de la fuente al 90 %, centro en x=1250, apoyado abajo
PLUMA_X, PLUMA_Y = 96, 48                   # las de recorta_cuadro.py
log = open(T + 'emplumar.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def rampa(n, p, ini, fin):
    r = np.ones(n, np.float32)
    if p > 0:
        t = (np.arange(p, dtype=np.float32) + 0.5) / p
        s = t * t * (3.0 - 2.0 * t)
        if ini:
            r[:p] = s
        if fin:
            r[n - p:] = s[::-1]
    return r


def sobre():
    """El fondo con alfa 1-w: opaco donde la pluma apaga a la persona, transparente en el resto."""
    out = T + 'pluma/sobre_fondo.png'
    os.makedirs(T + 'pluma', exist_ok=True)
    pl = rampa(H, PLUMA_Y, Y0 > 0, Y0 + H < CH)[:, None] * rampa(W, PLUMA_X, X0 > 0, X0 + W < CW)[None, :]
    peso = np.ones((CH, CW), np.float32)
    peso[Y0:Y0 + H, X0:CW] = pl[:CH - Y0, :CW - X0]
    f = np.asarray(Image.open(FONDO).convert('RGB').resize((CW, CH), Image.LANCZOS), dtype=np.uint8)
    a = np.clip((1.0 - peso) * 255.0 + 0.5, 0, 255).astype(np.uint8)
    Image.fromarray(np.dstack([f, a]), 'RGBA').save(out)
    return out


def cuadros(p):
    r = subprocess.run([FB + '/ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries',
                        'stream=nb_read_packets', '-of', 'csv=p=0', p], capture_output=True, text=True)
    return int(r.stdout.strip().split(',')[0] or 0)


S = sobre()
for clave in sys.argv[1:]:
    carpeta, base = PIEZAS[clave]
    d = R + carpeta + '/01 VIDEO/'
    rec, viejo, nuevo = d + base + '_recortado.mp4', d + '_descartes/' + base + '_recortado_sin_pluma.mp4', \
        d + base + '_recortado_con_pluma.parcial.mp4'
    if os.path.exists(viejo):
        w('ya estaba', clave)
        continue
    t = time.time()
    r = subprocess.run([FB + '/ffmpeg', '-y', '-v', 'error', '-i', rec, '-framerate', '30', '-loop', '1', '-i', S,
                        '-filter_complex', '[1:v]scale=out_color_matrix=bt709:out_range=tv,format=yuva420p[s];'
                        '[0:v][s]overlay=shortest=1:format=yuv420[v]', '-map', '[v]', '-map', '0:a?',
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
                        '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'copy',
                        '-movflags', '+faststart', '-f', 'mp4', nuevo], capture_output=True, text=True, errors='replace')
    a, b = cuadros(rec), cuadros(nuevo) if os.path.exists(nuevo) else 0
    if r.returncode or a != b:
        w('EMPLUMAR FALLA', clave, r.returncode, a, b, r.stderr[-300:])
        continue
    os.makedirs(d + '_descartes', exist_ok=True)
    shutil.move(rec, viejo)
    os.replace(nuevo, rec)
    w('EMPLUMADO', clave, 'cuadros', a, b, '%.0f s' % (time.time() - t), os.path.getsize(rec) >> 20, 'MB')
w('LISTO')
