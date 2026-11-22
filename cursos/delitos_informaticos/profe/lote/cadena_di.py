# -*- coding: utf-8 -*-
"""Delitos informáticos, videos de profe (22 nov 2026; es `cadena_dp.py` con un paso más): de cada plan, la fuente sin
la placa del logo y después compuesto, cartón de título y cartones (`pieza_di.py`), tres a la vez y con prioridad baja.
`entrega_gpu.py` espera el «LOTE LISTO» del `cadena.log` de cada pieza. Log: D:/DAE/_tmp/di_p/cadena_di.log"""
import subprocess
import sys
import time

PY = sys.executable
PIEZA = 'D:/DAE/_repo/cursos/delitos_informaticos/profe/lote/pieza_di.py'
PLANES = ['plan_diu4m', 'plan_diu3i', 'plan_diu4i', 'plan_diu4c', 'plan_diu3m']
A_LA_VEZ = 3
log = open('D:/DAE/_tmp/di_p/cadena_di.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


pend, vivos = list(sys.argv[1:] or PLANES), {}
w('arranca', len(pend))
while pend or vivos:
    for p, (pr, t) in list(vivos.items()):
        if pr.poll() is not None:
            w(p, 'rc', pr.returncode, '%.0f s' % (time.time() - t))
            del vivos[p]
    while pend and len(vivos) < A_LA_VEZ:
        p = pend.pop(0)
        vivos[p] = (subprocess.Popen([PY, PIEZA, p], creationflags=0x00000208 | 0x00004000), time.time())
        w(p, 'lanzado')
    time.sleep(5)
w('CADENA LISTA')
