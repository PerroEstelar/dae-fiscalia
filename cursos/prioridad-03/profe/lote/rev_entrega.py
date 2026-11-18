# -*- coding: utf-8 -*-
"""Despues de cada entrega de Trata: compara la copia de servidor (carpeta de verificacion) con la local y arma una
hoja de seis cuadros de la entrega. Uso: rev_entrega.py <prefijo del plan, p. ej. tru1r>   Imprime el resultado."""
import glob, importlib, os, subprocess, sys, time
sys.path.insert(0, 'D:/DAE/_repo/cursos/prioridad-03/profe')
sys.path.insert(0, 'D:/DAE/_repo/herramientas/montaje')
PY = sys.executable
T = 'D:/DAE/_tmp/tr_p/'
V = 'G:/My Drive/_MA subidas/_verif trata 18nov/'
FF = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
k = sys.argv[1]
P = importlib.import_module('plan_' + k)
nb = (P.EXPORT % getattr(P, 'VERSION', 1)) + '.mp4'
f = '%s/05 EXPORTS/%s' % (P.R, nb)
for _ in range(15):
    if os.path.exists(V + nb):
        break
    time.sleep(2)
if os.path.exists(V + nb):
    subprocess.run([PY, T + 'verif_tr.py', 'copia=' + V, nb])
    print([l for l in open(T + 'verif.log', encoding='utf-8').read().splitlines() if nb in l][-1])
else:
    print('LA COPIA NO APARECE EN G:')
d = float(subprocess.run([FF + '/ffprobe.exe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)
ts = [19.5] + [d * x for x in (0.2, 0.4, 0.6, 0.8)] + [d - 22]
for i, t in enumerate(ts):
    subprocess.run([FF + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', '%.2f' % t, '-i', f, '-frames:v', '1', '-vf', 'scale=960:540', '%s%s/q%d.png' % (T, k, i)])
subprocess.run([FF + '/ffmpeg.exe', '-y', '-v', 'error'] + sum([['-i', '%s%s/q%d.png' % (T, k, i)] for i in range(6)], []) + ['-filter_complex', 'xstack=inputs=6:layout=0_0|960_0|1920_0|0_540|960_540|1920_540', '-frames:v', '1', '-update', '1', '-q:v', '3', '%s%s/entrega_6.jpg' % (T, k)])
print('dura %.1f s' % d, 'hoja', os.path.getsize('%s%s/entrega_6.jpg' % (T, k)))
