# -*- coding: utf-8 -*-
r"""Cadena de un plan de profe (`ic_pieza`), para cualquier curso (17 nov 2026).

Es `dh_cadena.py` de Derechos humanos sin el curso fijo: el plan se busca en `cursos/` por su
nombre, y el disco que se mide es el de la carpeta de la pieza (`P.R`).

    python profe_cadena.py plan_tai                 todos los pasos
    python profe_cadena.py plan_tai cartones mg     solo esos (componer, titulo, cartones, mg)

1. `componer`, `titulo` y `cartones`; si uno falla, corta con «LOTE FALLO».
2. `mg_armar` con la máquina libre (un reintento si aftr corta a los 30 s) y `mg_render`.
   After Effects tiene que tener abierto el proyecto del plan (`P.AEP`).

Log: `<P.TMP>/cadena.log`, que termina en «LOTE LISTO», «MG FALLO» o «LOTE FALLO».
Se lanza con Popen (el puente corta a los 60 s) y se sondea el log.
"""
import importlib
import os
import shutil
import subprocess
import sys
import time

PY = sys.executable
AQUI = os.path.dirname(os.path.abspath(__file__))
IC = os.path.join(AQUI, 'ic_pieza.py')
plan = sys.argv[1]
pasos = sys.argv[2:] or ['componer', 'titulo', 'cartones', 'mg']
for _r, _d, _f in os.walk(os.path.join(AQUI, '..', '..', 'cursos')):
    if plan + '.py' in _f:
        sys.path.insert(0, _r)
        break
P = importlib.import_module(plan)
os.makedirs(P.TMP, exist_ok=True)
log = open(P.TMP + '/cadena.log', 'w', encoding='utf-8')


def w(*a):
    print(*a, file=log, flush=True)


while not os.path.exists(P.ORIGINAL):
    time.sleep(10)
env = dict(os.environ, DAE_PLAN=plan, PYTHONUTF8='1')


def paso(p):
    t = time.time()
    r = subprocess.run([PY, IC, p], capture_output=True, text=True, env=env, errors='replace')
    w('== %s  rc %d  %.0f s' % (p, r.returncode, time.time() - t))
    w(r.stdout[-6000:])
    if r.returncode:
        w('ERR', r.stderr[-1500:])
    return r.returncode, r.stdout


disco = os.path.splitdrive(P.R)[0] + '/'
libre = shutil.disk_usage(disco).free / 1e9
minutos = (P.T1 - P.T0) / 60.0
hace_falta = max(3.0, 0.35 * minutos)     # compuesto, cartones y listas en ProRes 4444
w('%s libre %.1f GB (hacen falta %.1f para %.1f min)' % (disco, libre, hace_falta, minutos))
if libre < hace_falta:
    w('SIN ESPACIO EN ' + disco)
    w('LOTE FALLO')
    sys.exit(1)
for p in ('componer', 'titulo', 'cartones'):
    if p in pasos and paso(p)[0]:
        w('LOTE FALLO en %s' % p)
        sys.exit(1)
if 'mg' in pasos:
    time.sleep(15)
    rc, out = paso('mg_armar')
    if 'ARMADO' not in out:
        w('mg_armar no terminó: reintento en 30 s')
        time.sleep(30)
        rc, out = paso('mg_armar')
    if 'ARMADO' not in out:
        w('MG FALLO')
        sys.exit(1)
    rc, out = paso('mg_render')
    if 'FALLA' in out or 'RENDER LISTO' not in out:
        w('MG FALLO')
        sys.exit(1)
w('LOTE LISTO')
