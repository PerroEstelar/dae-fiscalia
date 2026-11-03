# -*- coding: utf-8 -*-
r"""(Derechos humanos; es `subir_sit`.) Sube placas graduadas a Magnific (PUT a la URL prefirmada) para usarlas
como referencia de imagen o como cuadro inicial de Kling.

    python subir_lp.py subidas.json

subidas.json = [{"archivo": ruta png, "url": proxyUploadUrl, "path": ...}, ...]
o, sin "archivo", con "nombre" y "tipo" y la ruta se resuelve en el arbol:
    tipo "madre"  01 PLANOS/_grade/<nombre>.png
    tipo "det"    01 PLANOS/DETALLE/_grade/<nombre>.png
31 oct: toda REFERENCIA sube con `piel_ref` (piel gris calido a s <= 0,15;
el archivo de la pieza no se toca). Un cuadro inicial de Kling va con
"tipo": "kling" o "piel": false y sube tal cual.
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
    import rutas_lp as R
    L = s['nombre'].split('_')[1]
    pl = R.sub(L, '01 PLANOS')
    if s.get('tipo') == 'det':
        return os.path.join(pl, 'DETALLE', '_grade', s['nombre'] + '.png')
    return os.path.join(pl, '_grade', s['nombre'] + '.png')


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from piel_ref import piel_ref, medir                       # noqa: E402

for s in json.load(open(sys.argv[1], encoding='utf-8')):
    p = resuelve(s)
    im = Image.open(p).convert('RGB')
    # 31 oct: toda referencia sube con la piel de la serie (ver `piel_ref`);
    # "piel": false -o "tipo": "kling"- la sube tal cual: un cuadro inicial
    # de Kling ya viene graduado y no debe diferir de la placa de la linea
    if s.get('piel', s.get('tipo') != 'kling'):
        a = medir(im)
        im = piel_ref(im)
        b = medir(im)
        print('   piel %s p50 %.3f -> %.3f  rosado %.2f -> %.2f'
              % (os.path.basename(p), a['p50'], b['p50'], a['rosado'], b['rosado']),
              flush=True)
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
