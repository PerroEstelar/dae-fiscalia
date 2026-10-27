# -*- coding: utf-8 -*-
r"""Baja los crudos de video (Kling) de las situaciones.

    python bajar_crudos_sit.py crudos.json

crudos.json = {"D:\\DAE\\_tmp\\sit\\mov\\crudos\\SIT_A_r03_el_camino.mp4": "url", ...}
No pisa: si ya existe un crudo con ese nombre, el nuevo entra como _2, _3...
(un reintento de Kling nunca borra el anterior).
"""
import json
import os
import sys
import time
import urllib.request


def libre(p):
    if not os.path.exists(p):
        return p
    b, e = os.path.splitext(p)
    k = 2
    while os.path.exists('%s_%d%s' % (b, k, e)):
        k += 1
    return '%s_%d%s' % (b, k, e)


for p, u in sorted(json.load(open(sys.argv[1], encoding='utf-8')).items()):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if os.path.exists(p) and '--nuevo' not in sys.argv:
        print('ya', p, flush=True)
        continue
    d = libre(p)
    for i in range(4):
        try:
            with urllib.request.urlopen(u, timeout=120) as r:
                data = r.read()
            open(d + '.part', 'wb').write(data)
            os.replace(d + '.part', d)
            print('ok', d, len(data), flush=True)
            break
        except Exception as e:                            # noqa: BLE001
            print('reintento', i, e, flush=True)
            time.sleep(3)
print('LISTO')
