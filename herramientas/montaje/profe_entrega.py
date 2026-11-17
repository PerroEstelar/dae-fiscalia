# -*- coding: utf-8 -*-
r"""Línea de Resolve, entrega MP4 y hoja de revisión de un plan de profe (17 nov 2026).

Es `dh_entrega.py` de Derechos humanos para cualquier curso. Si el plan trae `MASTER_DIR`, el
máster de 32 Mb/s va ahí (la pieza vive en un disco sin espacio para guardarlo).

    python profe_entrega.py <log de la cadena | -> plan_tai

Espera «LOTE LISTO» en el log de la cadena (o no espera, con «-»). No sigue si la línea no
quedó bien. Log: `<P.TMP>/entrega.log`, que termina en «ENTREGA LISTA».
"""
import importlib
import os
import subprocess
import sys
import time

PY = sys.executable
M = os.path.dirname(os.path.abspath(__file__)) + os.sep
espera, plan = sys.argv[1], sys.argv[2]
for _r, _d, _f in os.walk(os.path.join(M, '..', '..', 'cursos')):
    if plan + '.py' in _f:
        sys.path.insert(0, _r)
        break
P = importlib.import_module(plan)
os.makedirs(P.TMP, exist_ok=True)
log = open(P.TMP + '/entrega.log', 'w', encoding='utf-8')


def w(*a):
    print(*a, file=log, flush=True)


if espera != '-':
    while True:
        try:
            s = open(espera, encoding='utf-8').read()
            if 'LOTE LISTO' in s:
                break
            if 'LOTE FALLO' in s or 'MG FALLO' in s:
                w('LA CADENA FALLÓ: no sigo')
                sys.exit(1)
        except OSError:
            pass
        time.sleep(15)


def corre(args, env):
    t = time.time()
    r = subprocess.run(args, capture_output=True, text=True, env=env, errors='replace')
    out = r.stdout + ('\nERR ' + r.stderr[-2000:] if r.returncode else '')
    w('-- %s  rc %d  %.0f s' % (os.path.basename(args[1]), r.returncode, time.time() - t))
    w(out[-3000:])
    return r.returncode, out


env = dict(os.environ, DAE_PLAN=plan, PYTHONUTF8='1')
v = getattr(P, 'VERSION', 1)
w('==', plan, P.NOMBRE_LINEA)
rc, out = corre([PY, M + 'ic_linea_externa.py'], env)
if 'LINEA LISTA' not in out or 'problemas ninguno' not in out:
    w('LA LINEA NO QUEDO BIEN: no sigo')
    sys.exit(1)
args = [PY, M + 'mp4_entrega.py', P.NOMBRE_LINEA, P.R, P.EXPORT % v]
if getattr(P, 'MASTER_DIR', None):
    os.makedirs(P.MASTER_DIR, exist_ok=True)
    args.append(P.MASTER_DIR)
rc, out = corre(args, env)
corre([PY, M + 'ic_revision.py', str(v)], env)
w('ENTREGA LISTA')
