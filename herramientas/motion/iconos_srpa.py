# -*- coding: utf-8 -*-
r"""Íconos de los motion graphics del curso SRPA y justicia restaurativa.

Tres hojas de 3×3 de Magnific (nano-banana-2-flash, 2k, el mismo prompt de las
hojas A–D de Delitos ambientales: líneas blancas redondeadas sobre negro, estilo
Lucide, sin texto). Se bajan en la máquina de Sebastián (el contenedor no llega a
pikaso.cdnpk.net), se guardan en `00 MOTION GRAPHICS/iconos/hojas` y cada celda
de 682 px se vuelve un PNG de 512 px blanco con el alfa sacado de la luminancia,
igual que los de Delitos ambientales.

    python iconos_srpa.py
"""
import io
import os
import sys
import urllib.request

import numpy as np
from PIL import Image

sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
import srpa as S  # noqa: E402

DEST = S.RAIZ + '/00 MOTION GRAPHICS/iconos'

HOJAS = {
    'E': ('https://pikaso.cdnpk.net/private/production/6008068564/render.png?token=exp=1794700800~hmac='
          '2623360066d3504bae9b2d748648c10092055770534a66d4d5e407d0def4dd77',
          ['bombilla', 'reloj', 'birrete', 'edificio', 'balanza', 'persona', 'engranaje', 'ojo', 'doc_check']),
    'F': ('https://pikaso.cdnpk.net/private/production/6008069928/render.png?token=exp=1794700800~hmac='
          '02e63bac3b57a78f84df2e51f54515b8236a1117d2d610e082bcf054f8d7ad64',
          ['calendario', 'puerta_salida', 'mano_corazon', 'familia', 'mazo', 'carpeta', 'bifurcacion',
           'mundo', 'candado']),
    'G': ('https://pikaso.cdnpk.net/private/production/6008070518/render.png?token=exp=1794700800~hmac='
          '45a07f9a05c24a5e3f834df378eccd2e9642af8634dadde8726087dfc2cd387b',
          ['reloj_arena', 'cerebro', 'libreta', 'escritorio', 'circulo', 'libros', 'torta', 'ciclo',
           'lupa_persona']),
}


def cortar(hoja, nombres):
    g = np.asarray(hoja.convert('L')).astype(np.float32)
    n = g.shape[0] / 3.0
    for i, nm in enumerate(nombres):
        r, c = divmod(i, 3)
        celda = g[int(r * n):int((r + 1) * n), int(c * n):int((c + 1) * n)]
        a = Image.fromarray(np.clip(celda, 0, 255).astype(np.uint8)).resize((512, 512), Image.LANCZOS)
        out = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
        out.putalpha(a)
        out.save('%s/%s.png' % (DEST, nm))


if __name__ == '__main__':
    os.makedirs(DEST + '/hojas', exist_ok=True)
    for k, (url, nombres) in HOJAS.items():
        b = urllib.request.urlopen(url, timeout=120).read()
        hoja = Image.open(io.BytesIO(b))
        hoja.save('%s/hojas/hoja_%s.png' % (DEST, k))
        cortar(hoja, nombres)
        print(k, hoja.size, ', '.join(nombres), flush=True)
    print('LISTO')
