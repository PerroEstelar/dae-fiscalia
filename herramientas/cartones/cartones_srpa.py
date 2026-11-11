#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Cartones de caja y lower thirds de los videos de profes del curso SRPA y
justicia restaurativa.

- Cartones: los de las introducciones de Delitos ambientales (`cartones_ma`, que
  es el dibujo y la animación de cartones_v3): caja x 62–790 / y 250–720, bloque
  anclado abajo en y=690, ancho 615, sombra de tres capas, sin tinte.
- Lower third: el de la U1 de Delitos ambientales («Diana Carolina Florez
  Vallona»), con el dibujo de `cartones_dema`: barra (227, 214, 49) de 17 px,
  nombre en Montserrat Bold 48 y debajo el cargo en Medium 27, barrido de
  izquierda a derecha a la entrada y a la salida. Abajo a la izquierda, como el de
  la U1 (bloque desde y=870, barra en x=86).

Lee `cursos/srpa-justicia-restaurativa/plan_srpa.py` y escribe
`<video>/02 CARTONES/SRPA_<video>_<clave>.mov` (qtrle con alfa, 23,976).

    python cartones_srpa.py curso            todo un video
    python cartones_srpa.py curso c04 lt     solo esas claves (prefijo)
    python cartones_srpa.py medir curso      alto y cima de cada cartón, sin rendir
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ma as C  # noqa: E402
import plan_srpa as P  # noqa: E402
import srpa as S  # noqa: E402

LT_BAR_C = (227, 214, 49, 255)
LT_BAR_W = 17
LT_GAP = 27
LT_X = 86
LT_TOP = 870
LT_NOMBRE, LT_CARGO = 48, 27
LT_ANCHO = 900
LT_IN, LT_OUT = 12, 12


def frames(t0, t1):
    return int(round((t1 - t0) * P.FPS))


def destino(video, clave):
    return '%s/02 CARTONES/SRPA_%s_%s.mov' % (S.carpeta(video), video, clave)


def lower_third(out, n, datos):
    nombre, cargo = datos
    tx = LT_X + LT_BAR_W + LT_GAP
    fn = ImageFont.truetype(C.BOLD, LT_NOMBRE)
    fc = ImageFont.truetype(C.MED, LT_CARGO)
    d0 = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    lineas = C.wrap(d0, cargo, fc, LT_ANCHO)
    plano = Image.new('RGBA', (C.W, C.H), (0, 0, 0, 0))
    d = ImageDraw.Draw(plano)
    y = LT_TOP
    d.text((tx, y), nombre, font=fn, fill=(255, 255, 255, 255))
    y += int(LT_NOMBRE * 1.22) + 8
    for ln in lineas:
        d.text((tx, y), ln, font=fc, fill=(255, 255, 255, 235))
        y += int(LT_CARGO * 1.38)
    bb = plano.getbbox()
    d.rectangle([LT_X, bb[1] - 10, LT_X + LT_BAR_W - 1, bb[3] + 10], fill=LT_BAR_C)
    plano = C.sombra(plano)
    x0, x1 = LT_X - 4, max(bb[2], tx) + 30
    p = subprocess.Popen([C.FFMPEG, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba',
                          '-s', '%dx%d' % (C.W, C.H), '-r', '24000/1001', '-i', '-',
                          '-c:v', 'qtrle', '-pix_fmt', 'argb', '-r', '24000/1001', out],
                         stdin=subprocess.PIPE)
    vacio = Image.new('RGBA', (C.W, C.H), (0, 0, 0, 0))
    for f in range(n):
        if f < LT_IN:
            a, b = x0 - 80, x0 + (x1 - x0 + 80) * C.ease_out((f + 1) / LT_IN)
        elif f >= n - LT_OUT:
            a, b = x0 + (x1 - x0 + 80) * C.ease_in((f - (n - LT_OUT) + 1) / LT_OUT) - 80, x1 + 80
        else:
            a, b = 0, C.W
        if b <= a:
            p.stdin.write(vacio.tobytes())
            continue
        mascara = Image.new('L', (C.W, C.H), 0)
        ImageDraw.Draw(mascara).rectangle([int(a), 0, int(b), C.H], fill=255)
        cuadro = Image.new('RGBA', (C.W, C.H), (0, 0, 0, 0))
        cuadro.paste(plano, (0, 0), mascara)
        p.stdin.write(cuadro.tobytes())
    p.stdin.close()
    p.wait()
    return bb[3] + 10


def medir(video):
    for clave, tipo, t0, t1, cont in P.ITEMS[video]:
        if tipo != 'carton':
            continue
        _c, _b, total, off = C.componer(cont)
        aviso = '  <-- SE SUBE DE LA ZONA' if off - C.BAR_PAD < C.ZONA[1] else ''
        largo = sum(len(x[0]) for x in cont)
        print('%-24s %5.1f s  %3d car  %4.1f car/s  alto %3d cima %3d%s' % (
            clave, t1 - t0, largo, largo / (t1 - t0), total, off - C.BAR_PAD, aviso), flush=True)


def rendir(video, solo):
    os.makedirs(os.path.dirname(destino(video, 'x')), exist_ok=True)
    for clave, tipo, t0, t1, cont in P.ITEMS[video]:
        if tipo not in ('carton', 'lt'):
            continue
        if solo and not any(clave.startswith(s) for s in solo):
            continue
        n = frames(t0, t1)
        out = destino(video, clave)
        if tipo == 'carton':
            total, off = C.render(cont, n, out)
            aviso = '  <-- SE SUBE DE LA ZONA' if off - C.BAR_PAD < C.ZONA[1] else ''
            print('%s %-24s %4d f  alto %3d cima %3d%s' % (video, clave, n, total, off - C.BAR_PAD, aviso),
                  flush=True)
        else:
            fondo = lower_third(out, n, cont)
            print('%s %-24s %4d f  lower third, fondo %d' % (video, clave, n, fondo), flush=True)
    print('LISTO', flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'medir':
        for v in sys.argv[2:]:
            medir(v)
    else:
        rendir(sys.argv[1], sys.argv[2:])
