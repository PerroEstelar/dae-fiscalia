# -*- coding: utf-8 -*-
r"""Cartón de título de las introducciones MA con el nombre correcto del curso.

Sebastián (10 nov 2026): el curso se llama «Investigación y judicialización de
delitos contra el medio ambiente y los recursos naturales» —en minúscula salvo la
primera palabra— en el cartón de entrada y en el de salida de los cinco videos.
El subtítulo «Introducción Unidad n» se queda como está.

El cartón original (`carton titulo ambientales u1v2.mp4`, 1920×1080, 30 fps, 270
cuadros, sin proyecto fuente en disco) se rehace sobre sus propios cuadros:
de cada `carton titulo ambientales unv2.mp4` se conservan el fondo, la barra, la
marca APRENDE CON LA DAE y el subtítulo con su dígito. Solo se borra la zona del
título (x 280–1600, y 440–706) y se vuelve a escribir palabra por palabra con la
animación medida en el original:

- Montserrat Bold 68, color (11, 54, 78). Líneas base 528, 607 y 686, con el texto
  desde x≈295 y los mismos cortes de línea.
- Cada línea tiene su máscara: 444–545, 549–624 y 629–703.
- Entrada: la palabra k sube desde abajo de su máscara. Empieza en 6 + 4,5·k, con
  la curva medida (41, 25, 16, 10, 6, 4, 2, 1, 1 px por cuadro y su media fase).
- Salida: sube y sale por arriba. Empieza en 253,18 + k/3, con dy = −200·t².

    python titulo_ma_v3.py medir      posiciones del original contra el modelo
    python titulo_ma_v3.py 1 2 3 4 5  rinde `carton titulo ambientales unv3.mp4`
"""
import glob
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

FD = os.path.expanduser('~') + '/AppData/Local/Microsoft/Windows/Fonts/'
FUENTE = ImageFont.truetype(FD + 'Montserrat-Bold.ttf', 68)
COLOR = (11, 54, 78)
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
W, H, N = 1920, 1080, 270

LINEAS = ['Investigación y judicialización de',
          'delitos contra el medio ambiente y',
          'los recursos naturales']
BASE = [528, 607, 686]
MASCARA = [(444, 545), (549, 624), (629, 703)]
TINTA_X = 295                       # borde izquierdo de la tinta de cada línea
ZONA = (280, 440, 1600, 706)        # x0, y0, x1, y1 que se borra

# curva de entrada en medios cuadros desde la primera aparición (medida)
ENTRADA = {-0.5: 51, 0: 41, 0.5: 32, 1: 25, 1.5: 20, 2: 16, 2.5: 13, 3: 10, 3.5: 8,
           4: 6, 4.5: 5, 5: 4, 5.5: 3, 6: 2, 6.5: 2, 7: 1, 7.5: 1, 8: 1, 8.5: 1}


def palabras():
    """[(k, línea, palabra, x de origen)] con el espaciado de Montserrat."""
    out, k = [], 0
    for li, linea in enumerate(LINEAS):
        x0 = TINTA_X - FUENTE.getbbox(linea, anchor='ls')[0]
        pos = 0
        for pal in linea.split(' '):
            i = linea.index(pal, pos)
            out.append((k, li, pal, x0 + FUENTE.getlength(linea[:i])))
            pos = i + len(pal)
            k += 1
    return out


def dy(k, n):
    """Desplazamiento vertical de la palabra k en el cuadro n (None = no se ve)."""
    t = n - (6 + 4.5 * k)
    if t < -0.5:
        return None
    if t < 9:
        return ENTRADA[round(t * 2) / 2.0]
    s = n - (253.18 + k / 3.0)
    if s <= 0:
        return 0
    return -200.0 * s * s


def capa_linea(li, pals, n):
    """La línea li en el cuadro n como RGBA del tamaño del cuadro, recortada a su máscara."""
    im = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(im)
    for k, l, pal, x in pals:
        if l != li:
            continue
        v = dy(k, n)
        if v is None:
            continue
        d.text((x, BASE[li] + v), pal, font=FUENTE, fill=255, anchor='ls')
    a = np.array(im)
    m0, m1 = MASCARA[li]
    a[:m0] = 0
    a[m1 + 1:] = 0
    return a


def cuadros(src):
    p = subprocess.Popen([FB + '/ffmpeg.exe', '-v', 'error', '-i', src, '-f', 'rawvideo',
                          '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
    p.wait()


def rendir(u):
    src = '%s/UNIDAD %d/02 CARTONES/carton titulo ambientales u%dv2.mp4' % (CURSO, u, u)
    dst = '%s/UNIDAD %d/02 CARTONES/carton titulo ambientales u%dv3.mp4' % (CURSO, u, u)
    pals = palabras()
    enc = subprocess.Popen([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                            '-s', '%dx%d' % (W, H), '-r', '30', '-i', '-',
                            '-vf', 'scale=out_color_matrix=bt709:out_range=tv',
                            '-c:v', 'libx264', '-crf', '12', '-preset', 'slow', '-pix_fmt', 'yuv420p',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                            '-movflags', '+faststart', dst], stdin=subprocess.PIPE)
    col = np.array(COLOR, np.float32)
    n = 0
    for f in cuadros(src):
        g = f.astype(np.float32)
        x0, y0, x1, y1 = ZONA
        g[y0:y1, x0:x1] = 255.0
        for li in range(len(LINEAS)):
            a = capa_linea(li, pals, n)[..., None].astype(np.float32) / 255.0
            if a.any():
                g = g * (1 - a) + col * a
        enc.stdin.write(np.clip(g + 0.5, 0, 255).astype(np.uint8).tobytes())
        n += 1
    enc.stdin.close()
    enc.wait()
    print('U%d %d cuadros -> %s' % (u, n, os.path.basename(dst)), flush=True)


def medir():
    """Las palabras del original (u1v2, cuadro 150) contra las del modelo con el texto viejo."""
    viejo = ['Investigación y Judicialización de', 'Delitos Contra el Medio Ambiente y',
             'los Recursos Naturales']
    for li, linea in enumerate(viejo):
        x0 = TINTA_X - FUENTE.getbbox(linea, anchor='ls')[0]
        pos = 0
        for pal in linea.split(' '):
            i = linea.index(pal, pos)
            x = x0 + FUENTE.getlength(linea[:i])
            b = FUENTE.getbbox(pal, anchor='ls')
            print('%d %-16s tinta x %4d-%4d  y %d-%d' % (li, pal, x + b[0], x + b[2],
                                                       BASE[li] + b[1], BASE[li] + b[3]))
            pos = i + len(pal)
    for k, li, pal, x in palabras():
        b = FUENTE.getbbox(pal, anchor='ls')
        print('nuevo %2d %-16s %4d-%4d' % (k, pal, x + b[0], x + b[2]))


if __name__ == '__main__':
    if sys.argv[1] == 'medir':
        medir()
    else:
        for u in [int(x) for x in sys.argv[1:]]:
            rendir(u)
