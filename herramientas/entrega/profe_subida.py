# -*- coding: utf-8 -*-
r"""Copia la entrega MP4 de un plan de profe a la carpeta de paso de Drive (17 nov 2026).

Es `dh_subida2.py` de Derechos humanos para cualquier plan, con la copia exclusiva de
`subir_exclusivo.py` (Drive para escritorio no puede leer el archivo hasta que está entero).

    python profe_subida.py plan_tai [esperar]

Con «esperar», espera «ENTREGA LISTA» en `<P.TMP>/entrega.log`. Log: `<P.TMP>/subida.log`,
con los bytes y el md5 de lo copiado, y «LISTO» al final.
"""
import importlib
import os
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from subir_exclusivo import copiar_exclusivo  # noqa: E402

plan = sys.argv[1]
for _r, _d, _f in os.walk(os.path.join(AQUI, '..', '..', 'cursos')):
    if plan + '.py' in _f:
        sys.path.insert(0, _r)
        break
P = importlib.import_module(plan)
if len(sys.argv) > 2:
    while True:
        try:
            if 'ENTREGA LISTA' in open(P.TMP + '/entrega.log', encoding='utf-8').read():
                break
        except OSError:
            pass
        time.sleep(15)
nm = P.EXPORT % getattr(P, 'VERSION', 1) + '.mp4'
src = P.R + '/05 EXPORTS/' + nm
dst = 'G:/My Drive/_MA subidas/' + nm
log = open(P.TMP + '/subida.log', 'w', encoding='utf-8')
if os.path.exists(src):
    n, md5 = copiar_exclusivo(src, dst)
    print('copiado', nm, os.path.getsize(src), n, os.path.getsize(dst), md5, file=log, flush=True)
else:
    print('NO EXISTE LA ENTREGA', src, file=log, flush=True)
print('LISTO', file=log, flush=True)
