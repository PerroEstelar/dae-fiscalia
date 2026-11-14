# -*- coding: utf-8 -*-
r"""Arma la línea de `ic_linea` desde fuera de `run_inline` (14 nov 2026).

`run_inline` corta a los 58 s. Con el cierre de Bienes (117 ítems) la importación al
pool y los `AppendToTimeline` tardan más: la primera línea de la introducción (33
ítems) ya se había cortado a mitad de la importación.

Este script se conecta a Resolve con `DaVinciResolveScript`, deja `resolve`, `project`
y `mp` como los deja `run_inline`, y ejecuta `ic_linea.py` tal cual.

    set DAE_PLAN=plan_bc
    python ic_linea_externa.py        (con Popen, sin límite de tiempo)

Resolve tiene que estar abierto con el proyecto y sin un render en curso.
"""
import os
import sys
import time

import DaVinciResolveScript as dvr

resolve = dvr.scriptapp('Resolve')
project = resolve.GetProjectManager().GetCurrentProject()
mp = project.GetMediaPool()
t0 = time.time()
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ic_linea.py'), encoding='utf-8').read())
construir()   # noqa: F821
drt()         # noqa: F821
print('LINEA LISTA %.0f s' % (time.time() - t0), flush=True)
