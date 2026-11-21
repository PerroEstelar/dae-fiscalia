# -*- coding: utf-8 -*-
"""Derecho de petición, videos de profe (20 nov 2026; es `cadena_df.py` con las rutas de este curso): compuesto, cartón de título y lower third de cada plan
(`profe_cadena.py <plan> componer titulo cartones`), tres a la vez y con prioridad baja, en el orden de `PLANES`
(el cierre de la U1 primero: es el más largo). `entrega_gpu.py` espera el «LOTE LISTO» de cada uno.
Log: D:/DAE/_tmp/dp_p/cadena_dp.log"""
import importlib
import os
import subprocess
import sys
import time

PY = sys.executable
CAD = 'D:/DAE/_repo/herramientas/montaje/profe_cadena.py'
PLANES = ['plan_dpu1c', 'plan_dpci', 'plan_dpu1i', 'plan_dpu2i', 'plan_dpu3i', 'plan_dpu4i']
A_LA_VEZ = 3
log = open('D:/DAE/_tmp/dp_p/cadena_dp.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


# ic_pieza no crea las carpetas de la pieza: ffmpeg falla al escribir el compuesto (código 4294967294, ENOENT) después
# de la medida de loudnorm. Se crean acá.
sys.path.insert(0, 'D:/DAE/_repo/cursos/derecho_peticion/profe')
for _p in PLANES:
    _P = importlib.import_module(_p)
    for _s in ('01 VIDEO', '02 CARTONES', '05 EXPORTS', '10 TIMELINE SEBASTIAN'):
        os.makedirs(_P.R + '/' + _s, exist_ok=True)
    os.makedirs(_P.TMP, exist_ok=True)
pend, vivos = list(sys.argv[1:] or PLANES), {}
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
