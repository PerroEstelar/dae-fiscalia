# -*- coding: utf-8 -*-
"""Audiencias preliminares, videos de profe (20 nov 2026; copia del de Desaparición forzada): compuesto, cartón de título y lower third de cada plan
(`profe_cadena.py <plan> componer titulo cartones`), tres a la vez y con prioridad baja, en el orden de `PLANES`
(los cierres primero: son los más largos). `entrega_gpu.py` espera el «LOTE LISTO» de cada uno.
Log: D:/DAE/_tmp/ap_p/cadena_ap.log"""
import importlib
import os
import subprocess
import sys
import time

PY = sys.executable
CAD = 'D:/DAE/_repo/herramientas/montaje/profe_cadena.py'
PLANES = ['plan_apu3c', 'plan_apu4c', 'plan_apu2c', 'plan_apu1c', 'plan_apu3i', 'plan_apu1i', 'plan_apu4i', 'plan_apu2i']
A_LA_VEZ = 3
log = open('D:/DAE/_tmp/ap_p/cadena_ap.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


# ic_pieza no crea las carpetas de la pieza: ffmpeg falla al escribir el compuesto (código 4294967294, ENOENT) después
# de la medida de loudnorm. Se crean acá.
sys.path.insert(0, 'D:/DAE/_repo/cursos/audiencias_preliminares/profe')
ELEGIDOS = sys.argv[1:] or PLANES   # 23 nov: se pasan los planes nuevos (inicio y cierre del curso)
for _p in ELEGIDOS:
    _P = importlib.import_module(_p)
    for _s in ('01 VIDEO', '02 CARTONES', '05 EXPORTS', '10 TIMELINE SEBASTIAN'):
        os.makedirs(_P.R + '/' + _s, exist_ok=True)
    os.makedirs(_P.TMP, exist_ok=True)
pend, vivos = list(ELEGIDOS), {}
w('arranca', len(pend))
while pend or vivos:
    for p, (pr, t) in list(vivos.items()):
        if pr.poll() is not None:
            w(p, 'rc', pr.returncode, '%.0f s' % (time.time() - t))
            del vivos[p]
    while pend and len(vivos) < A_LA_VEZ:
        p = pend.pop(0)
        vivos[p] = (subprocess.Popen([PY, CAD, p, 'componer', 'titulo', 'cartones'],
                                     creationflags=0x00000208 | 0x00004000), time.time())
        w(p, 'lanzado')
    time.sleep(5)
w('CADENA LISTA')
