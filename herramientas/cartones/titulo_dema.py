# -*- coding: utf-8 -*-
r"""Cartón de título del conversatorio «Articulación DEMA y DECOC».

Es el mismo cartón de las introducciones (`titulo_ma_v3`): el nombre del curso
en minúscula, con la animación palabra por palabra medida en el original. Lo
único que cambia es el subtítulo: en vez de «Introducción Unidad n» dice
«Conversatorio: articulación DEMA y DECOC». El subtítulo se borra del cuadro
base (u1v2) y se vuelve a escribir con su propia máscara y la misma curva.
Del original se miden el tamaño (Montserrat Regular 54,5), la línea base (775)
y la entrada (palabra j en 123 + 4,5·j).

    python titulo_dema.py
"""
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import titulo_ma_v3 as T  # noqa: E402

SUB = 'Conversatorio: articulación DEMA y DECOC'
F_SUB = ImageFont.truetype(T.FD + 'Montserrat-Regular.ttf', 54.5)
COLOR_SUB = (22, 58, 79)
BASE_SUB = 775
MASCARA_SUB = (722, 789)
ZONA = (280, 440, 1600, 800)
SRC = T.CURSO + '/UNIDAD 1/02 CARTONES/carton titulo ambientales u1v2.mp4'
DST = (T.CURSO + '/UNIDAD 1/CONVERSATORIO - Articulacion DEMA y DECOC/02 CARTONES/'
       'carton titulo conversatorio DEMA y DECOC.mp4')


def palabras_sub():
    x0 = T.TINTA_X - F_SUB.getbbox(SUB, anchor='ls')[0]
    out, pos = [], 0
    for j, pal in enumerate(SUB.split(' ')):
        i = SUB.index(pal, pos)
        out.append((j, pal, x0 + F_SUB.getlength(SUB[:i])))
        pos = i + len(pal)
    return out


def dy_sub(j, n):
    t = n - (123 + 4.5 * j)
    if t < -0.5:
        return None
    if t < 9:
        return T.ENTRADA[round(t * 2) / 2.0]
    s = n - (253.8 + 0.7 * j)
    if s <= 0:
        return 0
    return -200.0 * s * s


def capa_sub(pals, n):
    im = Image.new('L', (T.W, T.H), 0)
    d = ImageDraw.Draw(im)
    for j, pal, x in pals:
        v = dy_sub(j, n)
        if v is not None:
            d.text((x, BASE_SUB + v), pal, font=F_SUB, fill=255, anchor='ls')
    a = np.array(im)
    a[:MASCARA_SUB[0]] = 0
    a[MASCARA_SUB[1] + 1:] = 0
    return a


def rendir():
    pals, subs = T.palabras(), palabras_sub()
    enc = subprocess.Popen([T.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                            '-s', '%dx%d' % (T.W, T.H), '-r', '30', '-i', '-',
                            '-vf', 'scale=out_color_matrix=bt709:out_range=tv',
                            '-c:v', 'libx264', '-crf', '12', '-preset', 'slow', '-pix_fmt', 'yuv420p',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                            '-movflags', '+faststart', DST], stdin=subprocess.PIPE)
    col = np.array(T.COLOR, np.float32)
    col_s = np.array(COLOR_SUB, np.float32)
    n = 0
    for f in T.cuadros(SRC):
        g = f.astype(np.float32)
        x0, y0, x1, y1 = ZONA
        g[y0:y1, x0:x1] = 255.0
        for li in range(len(T.LINEAS)):
            a = T.capa_linea(li, pals, n)[..., None].astype(np.float32) / 255.0
            if a.any():
                g = g * (1 - a) + col * a
        a = capa_sub(subs, n)[..., None].astype(np.float32) / 255.0
        if a.any():
            g = g * (1 - a) + col_s * a
        enc.stdin.write(np.clip(g + 0.5, 0, 255).astype(np.uint8).tobytes())
        n += 1
    enc.stdin.close()
    enc.wait()
    print('%d cuadros -> %s' % (n, os.path.basename(DST)), flush=True)


if __name__ == '__main__':
    rendir()
