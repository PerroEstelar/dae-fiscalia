# -*- coding: utf-8 -*-
"""C5U3 «Eslabón Financiero»: el cartón de pausa p2 sin el antetítulo «Tarea del foro» (23 nov 2026).
Sebastián: «esto no es un foro, así que quitar toda la línea que dice tarea del foro».

1. Rinde el cartón viejo con el código de hoy y lo compara con el archivo de octubre (si el código no cambió, sale
   idéntico cuadro a cuadro): así el nuevo se ve igual que los otros dos de la pausa.
2. Rinde el nuevo, mismo largo (345 cuadros), con el título y el cuerpo de siempre: `C5U3_p2_foro v2.mov`.
Log: D:/DAE/_tmp/c5u3/foro.log"""
import glob, hashlib, os, subprocess, sys, time
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
os.environ['PATH'] = FB + os.pathsep + os.environ['PATH']
sys.path.insert(0, r'D:\DAE\_repo\herramientas\cartones')
import cartones_ta as C

K = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/UNIDAD 3/CASO 03 - eslabon financiero/02 CARTONES/'
T = 'D:/DAE/_tmp/c5u3/'
LOG = T + 'foro.log'
N = 345
VIEJO = {"ante": "Tarea del foro",
         "titulo": "Escoja dos de los cinco bienes y diga qué medida procede sobre cada uno",
         "cuerpo": "y qué hace con el tercero arrendatario y con los equipos que se deprecian mientras el proceso avanza."}
NUEVO = {k: v for k, v in VIEJO.items() if k != 'ante'}


def w(*a):
    with open(LOG, 'a', encoding='utf-8') as f:
        print(time.strftime('%H:%M:%S'), *a, file=f, flush=True)


def md5s(p):
    r = subprocess.run([FB + '/ffmpeg.exe', '-v', 'error', '-i', p, '-map', '0:v', '-f', 'framemd5', '-'],
                       capture_output=True, text=True)
    return [l.split(',')[-1].strip() for l in r.stdout.splitlines() if l and not l.startswith('#')]


os.makedirs(T, exist_ok=True)
w('== cartón p2 sin «Tarea del foro»')
C.render_carton(VIEJO, N, None, True, T + 'check_p2_foro.mov', con_tinte=True)
a, b = md5s(K + 'C5U3_p2_foro.mov'), md5s(T + 'check_p2_foro.mov')
dif = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
w('control: octubre %d cuadros, hoy %d, distintos %d' % (len(a), len(b), dif))
dst = K + 'C5U3_p2_foro v2.mov'
if os.path.exists(dst):
    w('ya existe', dst)
    sys.exit(1)
C.render_carton(NUEVO, N, None, True, T + 'p2_foro_v2.mov', con_tinte=True)
n = len(md5s(T + 'p2_foro_v2.mov'))
w('nuevo: %d cuadros' % n)
if n == N:
    import shutil
    shutil.copy2(T + 'p2_foro_v2.mov', dst)
    w('copiado a', dst)
subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', '7', '-i', K + 'C5U3_p2_foro.mov', '-ss', '7', '-i', dst,
                '-filter_complex', '[0:v]scale=960:540[a];[1:v]scale=960:540[b];[a][b]hstack', '-frames:v', '1',
                T + 'p2_antes_despues.png'])
w('FORO LISTO')
