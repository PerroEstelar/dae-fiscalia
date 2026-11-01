# -*- coding: utf-8 -*-
r"""Los cartones de una pieza APRETADA (`voz/apretar_dh.py`), quemados al largo
nuevo con su entrada y su salida completas.

    python cartones_apretados_dh.py U3 <cartones_apretados.json>

El json lo arma el plan: por carton, `ini` (cuadro de la linea, ya pasado por
el mapa de tiempo) y `cuadros`. El largo es el del mapa, y si con eso el
carton queda mas denso de lo que estaba, se le devuelve su largo de antes
(el de la linea de Sebastian: respeta sus recortes) mientras no pase el
inicio del siguiente menos 24 cuadros ni el final de la voz.

Recortar el clip en la linea le cortaba la salida al carton; por eso se
vuelve a quemar. El archivo nuevo lleva el largo en el nombre
(`..._carton_ap<cuadros>.mov`): otro nombre, la cache de Resolve no lo pisa.
"""
import json
import os
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('cartones', 'montaje', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_dh as R                                    # noqa: E402
import cartones_dh as CS                                # noqa: E402


def quemar(L, d):
    import cartones_ta as C
    C.TINTE = (0, 72, 144)
    import apertura_verbatim_p3c5 as V
    dest = os.path.join(R.sub(L, '02 CARTONES'), d['nuevo'])
    if os.path.exists(dest):
        return dest, 'ya estaba'
    n = d['renglones']
    y0 = int(540 - (n * CS.SALTO) / 2.0) + 20
    V.verbatim([(d['frase'], 0)], d['cuadros'], dest, y0=y0, cuerpo=CS.CUERPO,
               salto=CS.SALTO)
    return dest, 'quemado'


if __name__ == '__main__':
    L = sys.argv[1].upper()
    for d in json.load(open(sys.argv[2], encoding='utf-8')):
        p, que = quemar(L, d)
        CS.w('%s %s  %d cuadros  ini %d' % (os.path.basename(p), que, d['cuadros'], d['ini']))
    CS.w('LISTO')
