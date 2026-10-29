# -*- coding: utf-8 -*-
r"""Hoja de la LINEA sin render: compone, desde la media en disco, el cuadro
que la linea muestra en cada marca (mitad de cada ranura de V1, de cada
movimiento V2, de cada detalle V3, de cada carton V4 y el rotulo V8).

    python hoja_linea_gj.py T1 [T3 T4]

Es la hoja de `gj_pieza.revisar` cuando Resolve no puede rendir (29 oct: el
render de revision se colgo en 0 %). Usa el mismo `plan` y las mismas `capas`
que el montaje, asi que lo que sale es lo que la linea tiene: V1 abajo, V2
encima (tapa la ranura entera; el fundido de entrada no se simula), V3, los
cartones V4 y la marca V6 con su alfa, el rotulo V8 con su alfa.
Salida: D:\DAE\_tmp\gj\linea_<T>.jpg
"""
import os
import subprocess
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

from PIL import Image, ImageDraw                          # noqa: E402

import gj_pieza as SP                                     # noqa: E402

FPS = 24000 / 1001.0
W, Hh = 960, 540


def cuadro(p, i, alfa=False):
    fmt, n = ('rgba', 4) if alfa else ('rgb24', 3)
    r = subprocess.run(['ffmpeg', '-v', 'error', '-ss', '%.4f' % ((i + 0.25) / FPS), '-i', p,
                        '-frames:v', '1', '-vf', 'scale=%d:%d' % (W, Hh),
                        '-f', 'rawvideo', '-pix_fmt', fmt, '-'], capture_output=True)
    if len(r.stdout) < W * Hh * n:
        return None
    return Image.frombytes('RGBA' if alfa else 'RGB', (W, Hh), r.stdout[:W * Hh * n])


def en(lista, q):
    for pos, largo, p in lista:
        if pos <= q < pos + largo:
            return pos, p
    return None


def compone(L, q, v1, v2, v3, v4, v6, v8):
    capa = []
    b = en(v1, q)
    im = cuadro(b[1], q - b[0]) if b else None
    im = im or Image.new('RGB', (W, Hh), (0, 0, 0))
    for lista, alfa, k in ((v2, False, 'V2'), (v3, False, 'V3')):
        c = en(lista, q)
        if c:
            f = cuadro(c[1], q - c[0])
            if f:
                im = f
                capa.append(k)
    im = im.convert('RGBA')
    for lista, k in ((v4, 'V4'), (v6, 'V6'), (v8, 'V8')):
        c = en(lista, q)
        if c:
            f = cuadro(c[1], q - c[0], alfa=True)
            if f:
                im = Image.alpha_composite(im, f)
                capa.append(k)
    return im.convert('RGB'), capa


def hoja(L):
    v1, v4, v6, voz, mus, ini, dur, tot = SP.plan(L)
    v2, v3, v8, faltan = SP.capas(L)
    marcas = [('V1', pos + largo // 2) for pos, largo, _ in v1]
    marcas += [('V2', pos + largo // 2) for pos, largo, _ in v2]
    marcas += [('V3', pos + largo // 2) for pos, largo, _ in v3]
    marcas += [('V4', pos + largo // 2) for pos, largo, _ in v4]
    marcas += [('V8', pos + 60) for pos, largo, _ in v8]
    marcas = sorted(set(marcas), key=lambda x: x[1])
    tw, th = 480, 270
    cols = 4
    out = Image.new('RGB', (cols * tw, ((len(marcas) + cols - 1) // cols) * th), (20, 20, 20))
    d = ImageDraw.Draw(out)
    for i, (k, q) in enumerate(marcas):
        im, capa = compone(L, q, v1, v2, v3, v4, v6, v8)
        x, y = (i % cols) * tw, (i // cols) * th
        out.paste(im.resize((tw, th)), (x, y))
        s = q / FPS
        d.rectangle([x, y, x + tw, y + 16], fill=(0, 0, 0))
        d.text((x + 4, y + 2), '%s  %d  %d:%05.2f  %s' % (k, q, int(s // 60), s % 60,
                                                        '+'.join(capa) or 'V1'),
               fill=(255, 255, 0))
    p = os.path.join(SP.TMP, 'linea_%s.jpg' % L)
    out.save(p, quality=84)
    print(L, 'marcas', len(marcas), 'V2', len(v2), 'V3', len(v3), 'V4', len(v4), 'V8', len(v8),
          'faltan', faltan or 'nada', p, flush=True)


if __name__ == '__main__':
    for L in [a.upper() for a in sys.argv[1:]]:
        hoja(L)
