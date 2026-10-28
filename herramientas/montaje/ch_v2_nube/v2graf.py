# -*- coding: utf-8 -*-
"""Graficos de la V2 en el estilo medido de la V1 (cuadros de la propia linea)."""
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
FONTS = '/mnt/user-data/uploads/DAE/_tmp/ch/fonts/'
BOLD = FONTS + 'Montserrat-Bold.ttf'
TINTE = ((6, 71, 148), 0.45)            # medido: V1 caso 6 full vs limpio, error < 1 nivel
AMARILLO_ETQ = (227, 214, 49)
AMARILLO_CART = (253, 182, 0)


def leer(p, n=None, desde=0):
    """Lee cuadros [desde, desde+n) sin cargar el resto (memoria)."""
    vf = 'select=gte(n\\,%d)' % desde if desde else 'null'
    cmd = ['ffmpeg', '-v', 'error', '-i', p, '-vf', vf, '-fps_mode', 'passthrough']
    if n:
        cmd += ['-frames:v', str(n)]
    r = subprocess.run(cmd + ['-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(r, np.uint8).reshape(-1, H, W, 3)


def mp4(frames, out, crf=8):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W, H),
                          '-r', '24000/1001', '-i', '-', '-c:v', 'libx264', '-crf', str(crf), '-preset', 'slow',
                          '-tune', 'animation', '-pix_fmt', 'yuv420p', '-color_primaries', 'bt709',
                          '-color_trc', 'bt709', '-colorspace', 'bt709', out], stdin=subprocess.PIPE)
    for f in frames:
        p.stdin.write(np.ascontiguousarray(f, np.uint8).tobytes())
    p.stdin.close()
    p.wait()


def qtrle(rgba_frames, out):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', '%dx%d' % (W, H),
                          '-r', '24000/1001', '-i', '-', '-c:v', 'qtrle', '-pix_fmt', 'argb', out],
                         stdin=subprocess.PIPE)
    for f in rgba_frames:
        p.stdin.write(np.ascontiguousarray(f, np.uint8).tobytes())
    p.stdin.close()
    p.wait()


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def fuente(sz):
    return ImageFont.truetype(BOLD, sz)


def sobre(base, capa):
    """base uint8 HxWx3, capa RGBA float/uint8 -> uint8"""
    a = capa[..., 3:4].astype(np.float32) / 255
    return (base.astype(np.float32) * (1 - a) + capa[..., :3].astype(np.float32) * a + 0.5).astype(np.uint8)


# ---------------------------------------------------------------- etiqueta
def etiqueta_capa(lineas, sz, x, base_ult, inter, sombra=(4, 5, 8, 0.38), alto_barra=94, sep_barra=54):
    f = fuente(sz)
    capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    n = len(lineas)
    for i, l in enumerate(lineas):
        d.text((x, base_ult - (n - 1 - i) * inter), l, font=f, anchor='ls', fill=(255, 255, 255, 255))
    bb = capa.getbbox()
    dx, dy, bl, op = sombra
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sh.putalpha(capa.getchannel('A').point(lambda v: int(v * op)))
    sh = sh.filter(ImageFilter.GaussianBlur(bl))
    texto = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    texto.alpha_composite(sh, (dx, dy))
    texto.alpha_composite(capa)
    cy = (bb[1] + bb[3]) // 2
    barra = (x - sep_barra, cy - alto_barra // 2, x - sep_barra + 17, cy + alto_barra // 2)
    return np.asarray(texto).copy(), barra


def etiqueta_cuadro(texto, barra, k_in, k_out_wipe, entra_px=420):
    """k_in 0..1 (deslizamiento desde la izquierda); k_out_wipe 0..1 (barrido
    de izquierda a derecha al salir, como la V1)."""
    out = np.zeros((H, W, 4), np.uint8)
    dx = int(round(-(1 - ease(k_in)) * entra_px))
    src = texto
    if dx < 0:
        out[:, :W + dx] = src[:, -dx:]
    else:
        out[:] = src
    x0, y0, x1, y1 = barra
    bx0, bx1 = x0 + dx, x1 + dx
    if bx1 > 0:
        out[y0:y1, max(0, bx0):bx1] = AMARILLO_ETQ + (255,)
    if k_out_wipe > 0:
        bb = np.where(texto[..., 3].any(0))[0]
        xa, xb = min(bb.min(), x0), bb.max()
        cut = int(xa + ease(k_out_wipe) * (xb - xa + 1))
        out[:, :cut] = 0
    return out


# ---------------------------------------------------------------- titulo
def titulo_cambiar(frames, nuevo, x0=479, base=563, cols=(470, 700), mascara=(495, 583),
                   color=(14, 54, 77), sz=None, fondo=253):
    """Cambia la palabra de la derecha del rotulo blanco ('Juan') por `nuevo`
    siguiendo su animacion: sube desde abajo recortada por una mascara al entrar
    y sigue subiendo al salir. Solo toca cuadros de fondo blanco."""
    if sz is None:
        for sz in range(50, 90):
            bb = fuente(sz).getbbox('J', anchor='ls')
            if -bb[1] >= base - 516:
                break
    f = fuente(sz)
    capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(capa).text((x0, base), nuevo, font=f, anchor='ls', fill=color + (255,))
    capa = np.asarray(capa)
    out = []
    log = []
    c0, c1 = cols
    for i, fr in enumerate(frames):
        reg = fr[440:660, c0:c1].astype(np.float32).mean(2)
        blanco = (fr[440:660, c1:c1 + 200].mean() > 250) and (fr[300:420, 250:1100].mean() > 250)
        if not blanco:
            out.append(fr)
            log.append((i, '-'))
            continue
        ink = (fondo - reg).clip(0)
        rows = np.where(ink.sum(1) > 300)[0] + 440
        if len(rows) == 0:
            out.append(fr)
            log.append((i, 'vacio'))
            continue
        g = fr.copy()
        g[mascara[0] - 25:mascara[1] + 25, c0:c1 + 40] = fondo
        top, bot = rows.min(), rows.max()
        if bot >= 560 and top >= 516:          # entrando o quieta: manda el borde de arriba
            dy = top - 516
        else:                                   # saliendo: manda el borde de abajo
            dy = bot - 563
        c = np.zeros_like(capa)
        if dy >= 0:
            c[dy:] = capa[:H - dy]
        else:
            c[:H + dy] = capa[-dy:]
        c[:mascara[0]] = 0
        c[mascara[1]:] = 0
        out.append(sobre(g, c))
        log.append((i, int(dy)))
    return out, log, sz


# ---------------------------------------------------------------- carton
# Medido en la V1 (casos 2, 3 y 6): Montserrat Bold 71, renglones cada 86 px,
# texto en x 236 con el bloque de tinta centrado en y 583; barra amarilla
# (254,183,0) fija en x 176-203, y 491-677; velo (6,71,148) al 45 %.
# Animacion: el velo entra y sale en 24 cuadros; el texto entra deslizandose
# desde la izquierda en 11 cuadros y sale barrido de izquierda a derecha.
CARTON = dict(sz=71, paso=86, x=236, centro=583, barra=(176, 491, 204, 678),
              amarillo=(254, 183, 0), tinte=TINTE)


def carton_texto(lineas, est=CARTON):
    f = fuente(est['sz'])
    capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    for i, l in enumerate(lineas):
        d.text((est['x'], 300 + i * est['paso']), l, font=f, anchor='ls', fill=(253, 253, 253, 255))
    bb = capa.getbbox()
    dy = est['centro'] - (bb[1] + bb[3]) // 2
    a = np.asarray(capa)
    out = np.zeros_like(a)
    if dy < 0:
        out[:H + dy] = a[-dy:]
    else:
        out[dy:] = a[:H - dy]
    return out


def carton_cuadros(base, lineas, est=CARTON, velo_in=24, velo_out=24, txt_in=11, txt_out=11,
                   txt_desde=8, txt_hasta=None, velo_desde=0, velo_hasta=None, con_velo=True):
    """base: lista de cuadros (HxWx3). Devuelve los cuadros con el carton.
    Indices relativos a base: el velo dura [velo_desde, velo_hasta), el texto
    [txt_desde, txt_hasta)."""
    n = len(base)
    vh = n if velo_hasta is None else velo_hasta
    th = (vh - 10) if txt_hasta is None else txt_hasta
    texto = carton_texto(lineas, est)
    col, alfa = est['tinte']
    bx0, by0, bx1, by1 = est['barra']
    bb = np.where(texto[..., 3].any(0))[0]
    xa, xb = bx0, bb.max()
    for i, fr in enumerate(base):
        img = fr.astype(np.float32)
        if con_velo and velo_desde <= i < vh:
            k = min(ease((i - velo_desde + 1) / velo_in), ease((vh - i) / velo_out))
            a = alfa * k
            img = img * (1 - a) + np.array(col, np.float32) * a
        if txt_desde <= i < th:
            kin = ease((i - txt_desde + 1) / txt_in)
            kout = ease((i - (th - txt_out)) / txt_out) if i >= th - txt_out else 0
            capa = np.zeros((H, W, 4), np.uint8)
            dx = int(round(-(1 - kin) * (xb + 40)))
            if dx < 0:
                capa[:, :W + dx] = texto[:, -dx:]
            else:
                capa[:] = texto
            if bx1 + dx > 0:
                capa[by0:by1, max(0, bx0 + dx):bx1 + dx] = est['amarillo'] + (255,)
            if kout > 0:
                capa[:, :int(xa + kout * (xb - xa + 1))] = 0
            img = sobre(np.clip(img, 0, 255).astype(np.uint8), capa).astype(np.float32)
        yield np.clip(img + 0.5, 0, 255).astype(np.uint8)


MARCA = None


def con_marca(fr):
    """Marca «APRENDE CON LA DAE» de la V1 (V4, 52 %), sacada de un cuadro negro de la propia V1."""
    global MARCA
    if MARCA is None:
        MARCA = np.load('/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/marca.npy')
    return sobre(fr, MARCA)
