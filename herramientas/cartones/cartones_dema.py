#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Cartones y lower thirds del conversatorio «Articulación DEMA y DECOC» (Unidad 1).

Los cartones son los de caja de cartones_v3/cartones_ma: el mismo dibujo, la misma
sombra y la misma animación, pero puestos en la banda de abajo de la composición
(y 680–1080), debajo de quien habla, anclados arriba en y=725 y con 720 de ancho.

Los lower thirds copian el de la U1 («Diana Carolina Florez Vallona»):
- Barra amarilla (227, 214, 49) de 17 px y nombre en Montserrat Bold blanco.
- La U1 lo revela con un barrido de izquierda a derecha y lo saca con otro
  barrido en el mismo sentido.
- Acá el nombre va a 48 para que quepa en media pantalla, y debajo va la
  dirección en Medium 27.

    python cartones_dema.py            todo
    python cartones_dema.py c05 lt01   solo esas claves
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente')
sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\conversatorio_dema')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ma as C  # noqa: E402
import plan_dema as P  # noqa: E402

DEST = ('E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/UNIDAD 1/'
        'CONVERSATORIO - Articulacion DEMA y DECOC/02 CARTONES')

LT_BAR_C = (227, 214, 49, 255)
LT_BAR_W = 17
LT_GAP = 27                  # de la barra al texto, como en la U1
LT_TOP = 760
LT_NOMBRE, LT_CARGO = 48, 27
LT_ANCHO = 760
LT_IN, LT_OUT = 12, 12


def frames(t0, t1):
    return int(round((t1 - t0) * P.FPS))


def carton(clave, lado, t0, t1, lineas):
    C.BAR_X = P.LADO[lado]['bar_x']
    C.TEXT_X = P.LADO[lado]['text_x']
    C.MAXW = P.MAXW
    C.BASE_Y = C.H - 20                       # medida provisoria, dentro del cuadro
    _capas, _barra, total, _off = C.componer(lineas)
    C.BASE_Y = P.BANDA_TOP + total            # anclado arriba: crece hacia abajo
    out = '%s/DEMA_%s.mov' % (DEST, clave)
    n = frames(t0, t1)
    C.render(lineas, n, out)
    fondo = P.BANDA_TOP + total + C.BAR_PAD
    return n, total, fondo


def lower_third(clave, lado, t0, t1, datos):
    nombre, cargo = datos
    bx = P.LADO[lado]['bar_x']
    tx = bx + LT_BAR_W + LT_GAP
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
    d.rectangle([bx, bb[1] - 10, bx + LT_BAR_W - 1, bb[3] + 10], fill=LT_BAR_C)
    plano = C.sombra(plano)
    x0, x1 = bx - 4, max(bb[2], tx) + 30
    n = frames(t0, t1)
    out = '%s/DEMA_%s.mov' % (DEST, clave)
    p = subprocess.Popen([C.FFMPEG, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba',
                          '-s', '%dx%d' % (C.W, C.H), '-r', '24000/1001', '-i', '-',
                          '-c:v', 'qtrle', '-pix_fmt', 'argb', '-r', '24000/1001', out],
                         stdin=subprocess.PIPE)
    vacio = Image.new('RGBA', (C.W, C.H), (0, 0, 0, 0))
    for f in range(n):
        if f < LT_IN:                      # barrido de entrada: se descubre de izquierda a derecha
            a, b = x0 - 80, x0 + (x1 - x0 + 80) * C.ease_out((f + 1) / LT_IN)
        elif f >= n - LT_OUT:              # barrido de salida: se borra de izquierda a derecha
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
    return n, y - LT_TOP, bb[3] + 10


if __name__ == '__main__':
    os.makedirs(DEST, exist_ok=True)
    solo = sys.argv[1:]
    for clave, tipo, lado, t0, t1, cont in P.ITEMS:
        if solo and not any(clave.startswith(s) for s in solo):
            continue
        if tipo == 'carton':
            n, alto, fondo = carton(clave, lado, t0, t1, cont)
        elif tipo == 'lt':
            n, alto, fondo = lower_third(clave, lado, t0, t1, cont)
        else:
            continue
        aviso = '  <-- SE SALE DE LA BANDA' if fondo > 1050 else ''
        print('%-18s %s %5d f  alto %3d  fondo %4d%s' % (clave, lado, n, alto, fondo, aviso), flush=True)
    print('LISTO', flush=True)
