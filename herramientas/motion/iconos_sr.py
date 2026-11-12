# -*- coding: utf-8 -*-
r"""Íconos de las listas animadas de los CASOS del curso SRPA (`mg_sr`).

Dos hojas de 3×3 de Magnific (nano-banana-2-flash, 2k): líneas blancas
redondeadas sobre negro, estilo Lucide, sin texto, como las de `iconos_srpa`.
Se bajan en la máquina de Sebastián, se guardan en
`00 MOTION GRAPHICS/iconos/hojas` y cada celda se vuelve un PNG de 512 px
blanco con el alfa sacado de la luminancia.

A diferencia de las hojas E-G, estas dos trajeron la RETÍCULA dibujada
(líneas finas entre celdas): cada celda se recorta un 6 % por lado antes de
escalar, y lo que quede pegado al borde se apaga con un marco de 8 px.

    python iconos_sr.py
"""
import io
import os
import sys
import urllib.request

import numpy as np
from PIL import Image

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))
import rutas_sr as R  # noqa: E402

DEST = os.path.join(R.MOTION, 'iconos')
RECORTE = 0.06

HOJAS = {
    'H': ('https://pikaso.cdnpk.net/private/production/6019122536/render.png?token=exp=1794700800~hmac='
          '980e503dfabd87bf3dc02669da3d762f3a1a9319ffeb856f8fa45aa618c74c82',
          ['tamal', 'sopa', 'taza', 'billete', 'video', 'grupo', 'curita', 'plato', 'cama']),
    'I': ('https://pikaso.cdnpk.net/private/production/6019122383/render.png?token=exp=1794700800~hmac='
          '3b12a987206cbaa70fdee38962b296ee4157e4138c0e0182a7e4fed9cea3ea29',
          ['cruz_medica', 'escudo', 'lupa_doc', 'estetoscopio', 'pie', 'zapato_olor', 'peine',
           'bascula', 'doc_sello']),
}


def cortar(hoja, nombres):
    g = np.asarray(hoja.convert('L')).astype(np.float32)
    n = g.shape[0] / 3.0
    m = int(n * RECORTE)
    for i, nm in enumerate(nombres):
        r, c = divmod(i, 3)
        celda = g[int(r * n) + m:int((r + 1) * n) - m, int(c * n) + m:int((c + 1) * n) - m]
        a = Image.fromarray(np.clip(celda, 0, 255).astype(np.uint8)).resize((512, 512), Image.LANCZOS)
        a = np.asarray(a).copy()
        a[:8, :] = 0
        a[-8:, :] = 0
        a[:, :8] = 0
        a[:, -8:] = 0
        out = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
        out.putalpha(Image.fromarray(a))
        out.save(os.path.join(DEST, nm + '.png'))


if __name__ == '__main__':
    os.makedirs(os.path.join(DEST, 'hojas'), exist_ok=True)
    for k, (url, nombres) in HOJAS.items():
        b = urllib.request.urlopen(url, timeout=120).read()
        hoja = Image.open(io.BytesIO(b))
        hoja.save(os.path.join(DEST, 'hojas', 'hoja_sr_%s.png' % k))
        cortar(hoja, nombres)
        print(k, hoja.size, ', '.join(nombres), flush=True)
    print('LISTO')
