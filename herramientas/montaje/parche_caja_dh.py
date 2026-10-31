# -*- coding: utf-8 -*-
r"""Borra lo que Kling escribio dentro de una caja de luz LISA (Derechos humanos, 31 oct).

U1 r13: la placa tiene la caja de luz sobre la puerta de la emisora en
blanco, como pide la biblia (nada legible). Kling le dibujo encima dos
renglones que se leen como letrero («COMMUNITY RADIO»). Esto no regenera
nada: busca cuadro a cuadro el rectangulo claro dentro de una zona y lo
rellena con el fondo del letrero (perfiles de fila y columna al percentil
85, sin los trazos), que conserva el degradado de la luz. El archivo
anterior va a _descartes.

    python parche_caja_dh.py <mp4> x0 x1 y0 y1   (fracciones del cuadro: busca la
                                                  caja; pixeles: rectangulo fijo)
"""
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import dh_pieza as SP                                   # noqa: E402

W, H = 1920, 1080


def limpia_caja(fr, zona):
    if min(zona) > 1:
        # rectangulo FIJO en pixeles (el letrero no se mueve: camara quieta).
        # La deteccion por claridad fallaba: los renglones escritos bajan el
        # conteo de claros por fila y solo encontraba un pedazo.
        c, d, a, b = [int(x) for x in zona]
        return rellena(fr, a, b, c, d), (c, a, d, b)
    x0, x1, y0, y1 = [int(round(f * d)) for f, d in zip(zona, (W, W, H, H))]
    sub = fr[y0:y1, x0:x1]
    claro = sub.max(axis=2) > 190
    filas = np.where(claro.sum(1) > 80)[0]
    if len(filas) < 8:
        return fr, None
    r0, r1 = filas.min(), filas.max()
    cols = np.where(claro[r0:r1 + 1].sum(0) > (r1 - r0) * 0.5)[0]
    if len(cols) < 20:
        return fr, None
    c0, c1 = cols.min(), cols.max()
    a, b = y0 + r0 + 3, y0 + r1 - 2
    c, d = x0 + c0 + 3, x0 + c1 - 2
    if b - a < 6 or d - c < 12:
        return fr, None
    return rellena(fr, a, b, c, d), (c, a, d, b)


def rellena(fr, a, b, c, d):
    out = fr.copy()
    caja = out[a:b, c:d].astype(np.float32)
    # el fondo del letrero, sin los trazos: perfil por fila y por columna con
    # el percentil 85 (los trazos son oscuros y ocupan pocas filas/columnas),
    # suavizados; la caja se rellena con su producto (conserva el degradado
    # de la luz, centro mas claro)
    fila = np.percentile(caja, 85, axis=1)                    # (h, 3)
    col = np.percentile(caja.mean(axis=2), 85, axis=0)        # (w,)
    k = np.ones(9) / 9.0
    fila = np.stack([np.convolve(np.pad(fila[:, i], 4, mode='edge'), k, 'valid')
                     for i in range(3)], axis=1)
    col = np.convolve(np.pad(col, 4, mode='edge'), k, 'valid')
    col = col / max(col.mean(), 1.0)
    lleno = fila[:, None, :] * col[None, :, None]
    img = Image.fromarray(np.clip(lleno, 0, 255).astype(np.uint8))
    out[a:b, c:d] = np.asarray(img.filter(ImageFilter.GaussianBlur(1.5)))
    return out


def parchar(mp4, zona):
    n = SP.cuadros(mp4)
    tmp = mp4 + '.parche.mp4'
    lee = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', mp4, '-f', 'rawvideo',
                            '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    esc = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo',
                            '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W, H), '-r', '24000/1001',
                            '-i', '-', '-c:v', 'libx264', '-crf', '14', '-preset', 'slow',
                            '-pix_fmt', 'yuv420p', '-an', tmp], stdin=subprocess.PIPE)
    cajas = []
    for _ in range(n):
        buf = lee.stdout.read(W * H * 3)
        if len(buf) < W * H * 3:
            break
        fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        o, bb = limpia_caja(fr, zona)
        cajas.append(bb)
        esc.stdin.write(o.tobytes())
    esc.stdin.close()
    esc.wait()
    lee.wait()
    n2 = SP.cuadros(tmp)
    hechas = [b for b in cajas if b]
    SP.w('%s  %d/%d cuadros  caja encontrada en %d  primera %s  ultima %s'
         % (os.path.basename(mp4), n2, n, len(hechas), hechas[:1], hechas[-1:]))
    assert n2 == n, (n2, n)
    SP.aparta(mp4, 'letrero_de_kling')
    os.replace(tmp, mp4)


if __name__ == '__main__':
    parchar(sys.argv[1], [float(x) for x in sys.argv[2:6]])
    SP.w('LISTO')
