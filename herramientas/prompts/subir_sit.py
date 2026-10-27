# -*- coding: utf-8 -*-
r"""Sube placas graduadas a Magnific (PUT a la URL prefirmada) para usarlas
como referencia de imagen o como cuadro inicial de Kling.

    python subir_sit.py subidas.json

subidas.json = [{"archivo": ruta png, "url": proxyUploadUrl, "path": ...}, ...]
o, sin "archivo", con "nombre" y "tipo" y la ruta se resuelve en el arbol:
    tipo "madre"  01 PLANOS/_grade/<nombre>.png
    tipo "det"    01 PLANOS/DETALLE/_grade/<nombre>.png
Se manda JPEG 2560 de ancho calidad 93: pesa un quinto del PNG de 16 bits y
la referencia no necesita mas.
"""
import io
import json
import os
import sys
import urllib.request

from PIL import Image

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')


def resuelve(s):
    if s.get('archivo'):
        return s['archivo']
    import rutas_sit as R
    L = s['nombre'].split('_')[1]
    pl = R.sub(L, '01 PLANOS')
    if s.get('tipo') == 'det':
        return os.path.join(pl, 'DETALLE', '_grade', s['nombre'] + '.png')
    return os.path.join(pl, '_grade', s['nombre'] + '.png')


for s in json.load(open(sys.argv[1], encoding='utf-8')):
    p = resuelve(s)
    im = Image.open(p).convert('RGB')
    if im.width > 2560:
        im = im.resize((2560, int(im.height * 2560 / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=93)
    req = urllib.request.Request(s['url'], data=b.getvalue(), method='PUT',
                                 headers={'Content-Type': 'image/jpeg'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            print(r.status, s['path'], os.path.basename(p), len(b.getvalue()), flush=True)
    except Exception as e:                                # noqa: BLE001
        print('FALLA', s['path'], e, flush=True)
print('LISTO')
