# -*- coding: utf-8 -*-
r"""Cartones de título del curso «Sistema de responsabilidad penal para
adolescentes y justicia restaurativa» (entrada y salida de los videos de profes).

Es el cartón de las introducciones de Delitos ambientales (`titulo_ma_v3`), con
su fondo, su barra y su marca APRENDE CON LA DAE tomados de los cuadros de
`carton titulo ambientales u1v2.mp4`, y la misma animación palabra por palabra:
- El nombre del curso en dos líneas, Montserrat Bold 68, color (11, 54, 78).
- Debajo, el subtítulo en Montserrat Regular 44, color (22, 58, 79): «Presentación
  del curso» o «Unidad n. <nombre de la unidad>», partido a 1.330 px.
- El bloque entero se centra en la barra (y 466–780). Cada renglón tiene su
  máscara (de la línea base −84 a +17 en el título, como el original, y −64/+14
  en el subtítulo) y las palabras suben desde abajo de ella con la curva medida.
- Título: palabra k entra en 6 + 4,5·k y sale en 253,18 + k/3 (como el original).
  Subtítulo: palabra j entra en 64 + 3·j y sale en 253,5 + 0,35·j.

    python titulo_srpa.py medir         alto del bloque y renglones de cada cartón
    python titulo_srpa.py               los cinco: curso, U1, U3, U4, U5
    python titulo_srpa.py 0 3           solo esos (0 = curso)
"""
import os
import subprocess
import sys

import numpy as np
from PIL import ImageDraw, Image, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
import titulo_ma_v3 as T  # noqa: E402
import srpa as S  # noqa: E402

F_TIT = T.FUENTE                       # Montserrat Bold 68
F_SUB = ImageFont.truetype(T.FD + 'Montserrat-Regular.ttf', 44)
COLOR_SUB = (22, 58, 79)
LEAD_TIT, LEAD_SUB, GAP_SUB = 79, 56, 74   # de línea base a línea base
SUB_MAXW = 1330
BARRA = (466, 780)
ZONA = (280, 430, 1760, 830)
SRC = T.CURSO + '/UNIDAD 1/02 CARTONES/carton titulo ambientales u1v2.mp4'

_d = ImageDraw.Draw(Image.new('L', (10, 10)))


def partir(texto, font, maxw):
    """Los renglones que haría el corte voraz, pero equilibrados: entre todos los
    cortes con ese número de renglones, el que deja el renglón más ancho más corto."""
    pals = texto.split()
    out, ln = [], ''
    for w in pals:
        p = (ln + ' ' + w).strip()
        if _d.textlength(p, font=font) <= maxw or not ln:
            ln = p
        else:
            out.append(ln)
            ln = w
    n = len(out) + 1
    if n == 1:
        return [ln]
    import itertools
    mejor = None
    for cortes in itertools.combinations(range(1, len(pals)), n - 1):
        lim = (0,) + cortes + (len(pals),)
        rs = [' '.join(pals[a:b]) for a, b in zip(lim, lim[1:])]
        ancho = max(_d.textlength(r, font=font) for r in rs)
        if ancho <= maxw and (mejor is None or ancho < mejor[0]):
            mejor = (ancho, rs)
    return mejor[1]


def maqueta(u):
    """Renglones [(texto, fuente, color, base, mascara, tipo)] centrados en la barra."""
    sub = 'Presentación del curso' if u == 0 else 'Unidad %d. %s' % (u, S.UNIDADES[u])
    subs = partir(sub, F_SUB, SUB_MAXW)
    asc_t = -F_TIT.getbbox('Ád', anchor='ls')[1]      # alto sobre la base (con tilde)
    desc_s = F_SUB.getbbox('gjpq', anchor='ls')[3]
    alto = asc_t + LEAD_TIT * (len(S.CURSO_LINEAS) - 1) + GAP_SUB + LEAD_SUB * (len(subs) - 1) + desc_s
    b0 = (BARRA[0] + BARRA[1]) / 2.0 - alto / 2.0 + asc_t
    out, abajo = [], -999
    # las máscaras no se pisan: cada una empieza 4 px debajo de la anterior,
    # como en el original (444–545 y 549–624)
    for i, ln in enumerate(S.CURSO_LINEAS):
        b = round(b0 + i * LEAD_TIT)
        m = (max(b - 84, abajo + 4), b + 17)
        out.append((ln, F_TIT, T.COLOR, b, m, 'tit'))
        abajo = m[1]
    bs = b0 + LEAD_TIT * (len(S.CURSO_LINEAS) - 1) + GAP_SUB
    for i, ln in enumerate(subs):
        b = round(bs + i * LEAD_SUB)
        m = (max(b - 64, abajo + 4), b + 14)
        out.append((ln, F_SUB, COLOR_SUB, b, m, 'sub'))
        abajo = m[1]
    return out


def palabras(renglones):
    """[(renglón, palabra, x, índice dentro de su tipo)]"""
    out, k = [], {'tit': 0, 'sub': 0}
    for r, (ln, ft, _c, _b, _m, tipo) in enumerate(renglones):
        x0 = T.TINTA_X - ft.getbbox(ln, anchor='ls')[0]
        pos = 0
        for pal in ln.split(' '):
            i = ln.index(pal, pos)
            out.append((r, pal, x0 + ft.getlength(ln[:i]), k[tipo]))
            pos = i + len(pal)
            k[tipo] += 1
    return out


def dy(tipo, k, n):
    if tipo == 'tit':
        t, s = n - (6 + 4.5 * k), n - (253.18 + k / 3.0)
    else:
        t, s = n - (64 + 3.0 * k), n - (253.5 + 0.35 * k)
    if t < -0.5:
        return None
    if t < 9:
        return T.ENTRADA[round(t * 2) / 2.0]
    if s <= 0:
        return 0
    return -200.0 * s * s


def capa(renglones, pals, r, n):
    ln, ft, _c, b, (m0, m1), tipo = renglones[r]
    im = Image.new('L', (T.W, T.H), 0)
    d = ImageDraw.Draw(im)
    for rr, pal, x, k in pals:
        if rr != r:
            continue
        v = dy(tipo, k, n)
        if v is not None:
            d.text((x, b + v), pal, font=ft, fill=255, anchor='ls')
    a = np.array(im)
    a[:m0] = 0
    a[m1 + 1:] = 0
    return a


def destino(u):
    if u == 0:
        return '%s/PRESENTACION DEL CURSO/02 CARTONES/carton titulo srpa curso.mp4' % S.RAIZ
    return '%s/UNIDAD %d/02 CARTONES/carton titulo srpa u%d.mp4' % (S.RAIZ, u, u)


def rendir(u):
    ren = maqueta(u)
    pals = palabras(ren)
    dst = destino(u)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    enc = subprocess.Popen([T.FB + '/ffmpeg.exe', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                            '-s', '%dx%d' % (T.W, T.H), '-r', '30', '-i', '-',
                            '-vf', 'scale=out_color_matrix=bt709:out_range=tv',
                            '-c:v', 'libx264', '-crf', '12', '-preset', 'slow', '-pix_fmt', 'yuv420p',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                            '-movflags', '+faststart', dst], stdin=subprocess.PIPE)
    n = 0
    for f in T.cuadros(SRC):
        g = f.astype(np.float32)
        x0, y0, x1, y1 = ZONA
        g[y0:y1, x0:x1] = 255.0
        for r, (_l, _f, col, _b, _m, _t) in enumerate(ren):
            a = capa(ren, pals, r, n)[..., None].astype(np.float32) / 255.0
            if a.any():
                g = g * (1 - a) + np.array(col, np.float32) * a
        enc.stdin.write(np.clip(g + 0.5, 0, 255).astype(np.uint8).tobytes())
        n += 1
    enc.stdin.close()
    enc.wait()
    print('%s %d cuadros' % (os.path.basename(dst), n), flush=True)


def medir():
    for u in (0, 1, 3, 4, 5):
        ren = maqueta(u)
        for ln, ft, _c, b, m, tipo in ren:
            bb = ft.getbbox(ln, anchor='ls')
            print('%d %s base %d tinta x %d-%d y %d-%d  %s' % (u, tipo, b, T.TINTA_X, T.TINTA_X + bb[2] - bb[0],
                                                             b + bb[1], b + bb[3], ln))
        print()


if __name__ == '__main__':
    if sys.argv[1:2] == ['medir']:
        medir()
    else:
        for u in [int(x) for x in sys.argv[1:]] or [0, 1, 3, 4, 5]:
            rendir(u)
