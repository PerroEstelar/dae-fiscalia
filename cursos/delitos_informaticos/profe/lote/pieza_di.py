# -*- coding: utf-8 -*-
"""Delitos informáticos (22 nov 2026): una pieza de punta a punta hasta el compuesto. Crea las carpetas, saca la
placa del logo de la fuente del profe (`limpia_logo_di.py`, si la fuente limpia no existe todavía) y corre
`profe_cadena.py <plan> componer titulo cartones`. La lanza `cadena_di.py`.

    python pieza_di.py plan_diu3i
"""
import importlib
import os
import subprocess
import sys

PY = sys.executable
AQUI = 'D:/DAE/_repo/cursos/delitos_informaticos/profe'
sys.path.insert(0, AQUI)
p = sys.argv[1]
P = importlib.import_module(p)
for s in ('01 VIDEO', '02 CARTONES', '05 EXPORTS', '10 TIMELINE SEBASTIAN'):
    os.makedirs(P.R + '/' + s, exist_ok=True)
os.makedirs(P.TMP, exist_ok=True)
log = open(P.TMP + '/pieza.log', 'a', encoding='utf-8')
if not os.path.exists(P.ORIGINAL):
    r = subprocess.run([PY, AQUI + '/limpia_logo_di.py', P.FUENTE_PROFE, P.ORIGINAL, P.TMP + '/placa.json'],
                       stdout=log, stderr=subprocess.STDOUT)
    if r.returncode or not os.path.exists(P.ORIGINAL):
        print('LIMPIA FALLO', file=log, flush=True)
        sys.exit(1)
r = subprocess.run([PY, 'D:/DAE/_repo/herramientas/montaje/profe_cadena.py', p, 'componer', 'titulo', 'cartones'],
                   stdout=log, stderr=subprocess.STDOUT)
sys.exit(r.returncode)
