# -*- coding: utf-8 -*-
r"""Graficos de la V2 de los casos del profe Carlos Humberto, en el estilo de
la V1 (medido sobre sus cuadros, 28 oct):

  carton    velo azul de cuadro completo + barra amarilla (253,182,0) de 28 px en
            x 176 + texto blanco Montserrat Bold, 2 o 3 renglones, interlinea 90,
            bloque centrado en y 583 (V1 caso 2, «Familia garante...»).
  etiqueta  barra amarilla (226,213,49) de 16 px en x 188 + texto blanco con
            sombra suave, abajo a la izquierda (V1 caso 3, «José»).
  titulo    el rotulo blanco del caso con otro nombre: se toma el rotulo de la
            V1 cuadro a cuadro, se borra la palabra y se escribe la nueva con
            la misma opacidad que tenia la vieja en ese cuadro.

Todo sale en .mov QuickTime Animation (qtrle, argb), como los lower thirds
de la serie: Resolve respeta el alfa.
"""
import os
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
BOLD = r'C:\Windows\Fonts\Montserrat-Bold.ttf'
SEMI = r'C:\Windows\Fonts\Montserrat-SemiBold.ttf'
TINTE = ((22, 64, 140), 0.52)          # se recalibra con la V1 limpia
AMARILLO_C = (253, 182, 0)
AMARILLO_E = (226, 213, 49)
TITULO_TXT = (16, 55, 78)


def _salida(out, n):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    return subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo',
                             '-pix_fmt', 'rgba', '-s', '%dx%d' % (W, H), '-r', '24000/1001',
                             '-i', '-', '-c:v', 'qtrle', '-pix_fmt', 'argb', out],
                            stdin=subprocess.PIPE)


def _ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def _fuente(texto_ref, ancho_ref, ruta=BOLD):
    """Tamano tal que texto_ref mida ancho_ref (como en la V1)."""
    for s in range(40, 120):
        f = ImageFont.truetype(ruta, s)
        if f.getlength(texto_ref) >= ancho_ref:
            return ImageFont.truetype(ruta, s)
    return ImageFont.truetype(ruta, 74)


F_CARTON = None
F_ETIQ = None


def fuentes():
    global F_CARTON, F_ETIQ
    if F_CARTON is None:
        F_CARTON = _fuente('de derechos y corresponsable', 1354 - 240)
        F_ETIQ = _fuente('José', 412 - 245)
    return F_CARTON, F_ETIQ


def carton(lineas, n, out, entra=10, sale=6, tinte=None, y_centro=583):
    fc, _ = fuentes()
    color, alfa = tinte or TINTE
    inter = 90
    alto = inter * len(lineas)
    y0 = y_centro - alto // 2
    texto = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(texto)
    for i, l in enumerate(lineas):
        d.text((240, y0 + i * inter), l, font=fc, fill=(255, 255, 255, 255))
    bb = texto.getbbox()
    barra = (176, bb[1] - 16, 204, bb[3] + 17)
    p = _salida(out, n)
    for f in range(n):
        k = min(_ease(f / float(entra)), _ease((n - 1 - f) / float(sale)))
        im = Image.new('RGBA', (W, H), color + (int(round(255 * alfa * k)),))
        dx = int(round((1 - k) * 28))
        t = texto.copy()
        if k < 1:
            a = t.getchannel('A').point(lambda v: int(v * k))
            t.putalpha(a)
        im.alpha_composite(t, (-dx, 0))
        db = ImageDraw.Draw(im)
        h = int((barra[3] - barra[1]) * k)
        cy = (barra[1] + barra[3]) // 2
        if h > 0:
            db.rectangle((barra[0], cy - h // 2, barra[2], cy + h // 2), fill=AMARILLO_C + (255,))
        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    return out


def etiqueta(lineas, n, out, entra=10, sale=6, x=245, y_base=853, tam=None, barra=True):
    _, fe = fuentes()
    if tam:
        fe = ImageFont.truetype(BOLD, tam)
    asc = fe.getbbox('Ay')[1]
    inter = int(fe.size * 1.22)
    capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    y_top = y_base - (len(lineas) - 1) * inter - (fe.getbbox('A')[3])
    for i, l in enumerate(lineas):
        d.text((x, y_top + i * inter), l, font=fe, fill=(255, 255, 255, 255))
    bb = capa.getbbox()
    sombra = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sombra.putalpha(capa.getchannel('A').point(lambda v: int(v * 0.45)))
    sombra = sombra.filter(ImageFilter.GaussianBlur(6))
    base = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    base.alpha_composite(sombra, (3, 4))
    base.alpha_composite(capa)
    if barra:
        ImageDraw.Draw(base).rectangle((x - 57, bb[1] - 13, x - 42, bb[3] + 28),
                                       fill=AMARILLO_E + (255,))
    p = _salida(out, n)
    for f in range(n):
        k = min(_ease(f / float(entra)), _ease((n - 1 - f) / float(sale)))
        im = base.copy()
        im.putalpha(base.getchannel('A').point(lambda v: int(v * k)))
        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    return out


def titulo(src, viejo_bbox, nuevo, out):
    """viejo_bbox = (x0, y0, x1, y1) de la palabra a cambiar en el rotulo
    blanco de la V1 (1920x1080). Se lee el rotulo cuadro a cuadro: la
    opacidad de la palabra vieja en cada cuadro decide la de la nueva."""
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_frames',
                        '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', src],
                       capture_output=True, text=True).stdout.strip()
    n = int(r)
    rd = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', src, '-vf',
                           'scale=%d:%d,fps=24000/1001' % (W, H), '-f', 'rawvideo',
                           '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    frames = []
    while True:
        b = rd.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            break
        frames.append(np.frombuffer(b, np.uint8).reshape(H, W, 3).copy())
    rd.wait()
    x0, y0, x1, y1 = viejo_bbox
    ref = frames[len(frames) // 2][y0:y1, x0:x1].astype(np.float32)
    tinta_ref = (253.0 - ref.mean(2)).clip(0).sum()
    f_t = ImageFont.truetype(BOLD, 10)
    for s in range(20, 90):
        f_t = ImageFont.truetype(BOLD, s)
        if f_t.getbbox('C')[3] - f_t.getbbox('C')[1] >= (563 - 515) * 0.98:
            break
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt',
                          'rgb24', '-s', '%dx%d' % (W, H), '-r', '24000/1001', '-i', '-',
                          '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', out],
                         stdin=subprocess.PIPE)
    for fr in frames:
        reg = fr[y0:y1, x0:x1].astype(np.float32)
        k = min(1.0, (253.0 - reg.mean(2)).clip(0).sum() / max(tinta_ref, 1.0))
        im = Image.fromarray(fr)
        d = ImageDraw.Draw(im)
        d.rectangle((x0, y0 - 6, x1 + 40, y1 + 14), fill=(253, 253, 253))
        if k > 0.02:
            capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(capa).text((x0, y1), nuevo, font=f_t, anchor='ls',
                                      fill=TITULO_TXT + (int(255 * k),))
            im = im.convert('RGBA')
            im.alpha_composite(capa)
            im = im.convert('RGB')
        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    return out, len(frames)
