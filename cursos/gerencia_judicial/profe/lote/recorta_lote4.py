# -*- coding: utf-8 -*-
"""Gerencia judicial (27 nov 2026): el inicio de la U4 lo recorta este proceso apenas termina el lote 3, en vez de
esperar al final de la cola del lote 2. Para que el lote 2 lo salte, antes se deja un archivo vacio con el nombre del
recortado (el lote 2 solo mira si existe); recorta_cuadro.py lo reemplaza al terminar."""
import os, subprocess, sys, time
T = 'D:/DAE/_tmp/gj_p/'
R = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE/'
REC = 'D:/DAE/_repo/herramientas/video/recorta_cuadro.py'
FU = R + 'UNIDAD 4/INICIO/01 VIDEO/gj_u4i_fuente.mp4'
SA = R + 'UNIDAD 4/INICIO/01 VIDEO/gj_u4i_recortado.mp4'
if not os.path.exists(SA):
    open(SA, 'wb').close()
log = open(T + 'recorta_lote.log', 'a', encoding='utf-8')
while 'LOTE DE RECORTES 3 LISTO' not in open(T + 'recorta_lote.log', encoding='utf-8').read():
    time.sleep(20)
if os.path.getsize(SA) == 0:
    print(time.strftime('%H:%M:%S'), 'lote 4: empieza u4i', file=log, flush=True)
    os.makedirs(T + 'u4i', exist_ok=True)
    env = {k: v for k, v in os.environ.items() if not k.startswith('PYTHON')}
    t = time.time()
    with open(T + 'u4i/recorta.out', 'w', encoding='utf-8') as out:
        rc = subprocess.run([sys.executable, '-X', 'utf8', REC, FU, R + '00 FONDOS/FONDO 4 V2.png', SA, '--escala', '0.85', '--cx', '1220'],
                            stdout=out, stderr=subprocess.STDOUT, env=env).returncode
    s = open(T + 'u4i/recorta.out', encoding='utf-8', errors='replace').read()
    print(time.strftime('%H:%M:%S'), 'RECORTE u4i', 'OK' if rc == 0 and 'LISTO' in s else 'FALLA', '%.0f min' % ((time.time() - t) / 60), ' '.join(s.split())[-80:], file=log, flush=True)
