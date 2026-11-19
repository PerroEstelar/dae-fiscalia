# -*- coding: utf-8 -*-
"""Ley 1826, videos de profe (19 nov 2026): recorta al profe de las diez grabaciones y lo pone sobre el fondo de
la Fiscalia (`herramientas/video/recorta_cuadro.py`: el cuadro entero al 90 %, centro en x=1250, apoyado abajo).
Dos a la vez por la placa (4,4 c/s cada uno en la GTX 970: 104.600 cuadros en unas 3,3 h), los cortos primero.
Despues de cada uno cuenta los cuadros del recortado contra los de la fuente. Lo que ya existe no se rehace.
La pluma de los bordes (96 px a la izquierda, 48 arriba) es la que trae recorta_cuadro.py por omision; los cuatro
primeros recortes se hicieron antes de que existiera y se emplumaron con emplumar.py.
Log: recorta_lote.log; la salida de cada recorte, en <clave>/recorta.out"""
import os
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from glob import glob

PY = sys.executable
FB = glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
REC = 'D:/DAE/_repo/herramientas/video/recorta_cuadro.py'
T = 'D:/DAE/_tmp/lp_p/'
R = 'E:/DAE MASTER/PRIORIDAD 1/CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO/VIDEOS PROFE/'
FONDO = R + '00 FONDOS/FONDO 4 V2.png'
LOTE = [('lpci', 'CURSO/INICIO', 'lp_curso_inicio'), ('lpu1i', 'UNIDAD 1/INICIO', 'lp_u1_inicio'),
        ('lpu1c', 'UNIDAD 1/CIERRE', 'lp_u1_cierre'), ('lpu2i', 'UNIDAD 2/INICIO', 'lp_u2_inicio'),
        ('lpu2c', 'UNIDAD 2/CIERRE', 'lp_u2_cierre'), ('lpu3i', 'UNIDAD 3/INICIO', 'lp_u3_inicio'),
        ('lpu3c', 'UNIDAD 3/CIERRE', 'lp_u3_cierre'), ('lpu4i', 'UNIDAD 4/INICIO', 'lp_u4_inicio'),
        ('lpu4c', 'UNIDAD 4/CIERRE', 'lp_u4_cierre'), ('lpcc', 'CURSO/CIERRE', 'lp_curso_cierre')]
log = open(T + 'recorta_lote.log', 'a', encoding='utf-8')
lock = threading.Lock()


def w(*a):
    with lock:
        print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def cuadros(p):
    r = subprocess.run([FB + '/ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries',
                        'stream=nb_read_packets', '-of', 'csv=p=0', p], capture_output=True, text=True)
    return int(r.stdout.strip().split(',')[0] or 0)


def uno(x):
    clave, carpeta, base = x
    fu = R + carpeta + '/01 VIDEO/' + base + '_fuente.mp4'
    sa = R + carpeta + '/01 VIDEO/' + base + '_recortado.mp4'
    if os.path.exists(sa):
        w('ya estaba', clave)
        return
    t = time.time()
    w('empieza', clave)
    os.makedirs(T + clave, exist_ok=True)
    with open(T + clave + '/recorta.out', 'w', encoding='utf-8') as out:
        rc = subprocess.run([PY, REC, fu, FONDO, sa, '--escala', '0.9', '--cx', '1250'], stdout=out,
                            stderr=subprocess.STDOUT).returncode
    s = open(T + clave + '/recorta.out', encoding='utf-8', errors='replace').read()
    ok = rc == 0 and 'LISTO' in s and os.path.exists(sa)
    a = cuadros(fu)
    b = cuadros(sa) if ok else 0
    w('RECORTE', clave, 'OK' if ok and a == b else 'FALLA', 'cuadros', a, b, '%.0f min' % ((time.time() - t) / 60),
      ' '.join(s.split())[-120:])


w('lote: arranca')
with ThreadPoolExecutor(2) as ex:
    list(ex.map(uno, LOTE))
w('LOTE DE RECORTES LISTO')
