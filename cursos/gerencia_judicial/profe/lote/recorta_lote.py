# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026): recorta al profe (Robust Video Matting, resnet50, por la placa)
y lo pone sobre FONDO 4 V2 (herramientas/video/recorta_cuadro.py): el cuadro entero de la fuente al 85 %, centro en
x=1220, apoyado abajo, con la pluma de los bordes de siempre. Es un plano de camara web (cabeza y hombros): al 85 %
la cabeza queda del tamano de los videos de Justicia restaurativa y el hombro derecho entra entero.
Dos a la vez: la bienvenida al curso (44.876 cuadros) en uno y las ocho piezas de unidad, en orden, en el otro;
cada pieza espera a que su _fuente.mp4 exista (gj_extraer.py). Lo que ya existe no se rehace.
Log: recorta_lote.log; la salida de cada recorte, en <clave>/recorta.out"""
import os, subprocess, sys, threading, time
from glob import glob
PY = sys.executable
FB = glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
REC = 'D:/DAE/_repo/herramientas/video/recorta_cuadro.py'
T = 'D:/DAE/_tmp/gj_p/'
R = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE/'
FONDO = R + '00 FONDOS/FONDO 4 V2.png'
CI = [('gjci', R + 'CURSO/INICIO/01 VIDEO/VIDEO 1 GERENCIA JUDICIAL TOMA1.mp4', R + 'CURSO/INICIO/01 VIDEO/gj_curso_inicio_recortado.mp4')]
U = [(k, R + c + '/01 VIDEO/gj_%s_fuente.mp4' % k, R + c + '/01 VIDEO/gj_%s_recortado.mp4' % k) for k, c in
     [('u1c', 'UNIDAD 1/CIERRE'), ('u2i', 'UNIDAD 2/INICIO'), ('u2c', 'UNIDAD 2/CIERRE'),
      ('u3i', 'UNIDAD 3/INICIO'), ('u3c', 'UNIDAD 3/CIERRE'), ('u4i', 'UNIDAD 4/INICIO'), ('u4c', 'UNIDAD 4/CIERRE'), ('u1i', 'UNIDAD 1/INICIO')]]
log = open(T + 'recorta_lote.log', 'a', encoding='utf-8')
lock = threading.Lock()
env = {k: v for k, v in os.environ.items() if not k.startswith('PYTHON')}


def w(*a):
    with lock:
        print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def cuadros(p):
    r = subprocess.run([FB + '/ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries',
                        'stream=nb_read_packets', '-of', 'csv=p=0', p], capture_output=True, text=True)
    return int(r.stdout.strip().split(',')[0] or 0)


def uno(clave, fu, sa):
    if os.path.exists(sa):
        w('ya estaba', clave); return
    while not os.path.exists(fu):
        time.sleep(15)
    t = time.time(); w('empieza', clave)
    os.makedirs(T + clave, exist_ok=True)
    with open(T + clave + '/recorta.out', 'w', encoding='utf-8') as out:
        rc = subprocess.run([PY, '-X', 'utf8', REC, fu, FONDO, sa, '--escala', '0.85', '--cx', '1220'], stdout=out,
                            stderr=subprocess.STDOUT, env=env).returncode
    s = open(T + clave + '/recorta.out', encoding='utf-8', errors='replace').read()
    ok = rc == 0 and 'LISTO' in s and os.path.exists(sa)
    a = cuadros(fu); b = cuadros(sa) if ok else 0
    w('RECORTE', clave, 'OK' if ok and a == b else 'FALLA', 'cuadros', a, b, '%.0f min' % ((time.time() - t) / 60), ' '.join(s.split())[-120:])


def fila(lista):
    for x in lista:
        uno(*x)


w('lote: arranca')
h = [threading.Thread(target=fila, args=(CI,)), threading.Thread(target=fila, args=(U,))]
for x in h: x.start()
for x in h: x.join()
w('LOTE DE RECORTES LISTO')
