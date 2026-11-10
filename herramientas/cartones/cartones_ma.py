#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de caja de las introducciones U2-U5 de Medio Ambiente (10 nov 2026).

Mismo dibujo y misma animacion que `cartones_v3.py` (los de la U1 que Sebastian
aprobo): rejilla B, caja x 60-790 / y 250-720, bloque anclado abajo en y=690,
sombra de tres capas, sin tinte. Corre en la maquina de Sebastian (fuentes
Montserrat del usuario) y toma los textos y los cuadros de
`cursos/medio-ambiente/plan_intros.py`; solo los items de tipo `carton`.

    python cartones_ma.py            U2-U5
    python cartones_ma.py 3          una unidad
    python cartones_ma.py 3 c07      un carton
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, os, sys, glob

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente')
import plan_intros as P

FPS = 24000 / 1001
FD = os.path.expanduser('~') + '/AppData/Local/Microsoft/Windows/Fonts/'
BOLD, MED = FD + 'Montserrat-Bold.ttf', FD + 'Montserrat-Medium.ttf'
FFMPEG = glob.glob('C:/Users/call_/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin/ffmpeg.exe')[0]

W, H = 1920, 1080
ZONA = (60, 250, 790, 720)
BAR_X, BAR_W, BAR_C = 86, 14, (254, 185, 0, 255)
TEXT_X = 170
MAXW = ZONA[2] - TEXT_X - 5        # 615
BASE_Y = 690
BAR_PAD = 28
ALTO_MAX = BASE_Y - ZONA[1] - BAR_PAD   # 412
WHITE = (255, 255, 255, 255)
SANGRIA = 46
INTERLINEA = 1.30

CAPAS_SOMBRA = [
    (3,  0.85, (0, 0)),
    (22, 0.70, (0, 0)),
    (7,  0.70, (0, 4)),
]
MARGEN = 80

BARRA_IN, BARRA_OUT = 10, 10
TXT_IN, TXT_OUT = 14, 10
RETARDO_IN, RETARDO_OUT = 3, 2
SUBE_IN, SUBE_OUT = 14, 8
ARRANQUE_TXT = 6

B = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/UNIDAD %d/02 CARTONES/v3'


def ease_out(t):
    return 1 - (1 - t) ** 3


def ease_in(t):
    return t ** 3


def wrap(d, text, font, maxw):
    out, line = [], ""
    for w in text.split():
        probe = (line + " " + w).strip()
        if d.textlength(probe, font=font) <= maxw or not line:
            line = probe
        else:
            out.append(line)
            line = w
    if line:
        out.append(line)
    return out


def sombra(capa):
    a = capa.split()[3]
    fondo = Image.new("RGBA", capa.size, (0, 0, 0, 0))
    for blur, alfa, (ox, oy) in CAPAS_SOMBRA:
        m = a.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * alfa))
        s = Image.new("RGBA", capa.size, (0, 0, 0, 0))
        s.putalpha(m)
        if (ox, oy) == (0, 0):
            fondo.alpha_composite(s)
        else:
            desp = Image.new("RGBA", capa.size, (0, 0, 0, 0))
            desp.paste(s, (ox, oy))
            fondo.alpha_composite(desp)
    fondo.alpha_composite(capa)
    return fondo


def componer(lineas):
    probe = Image.new("RGBA", (10, 10))
    d0 = ImageDraw.Draw(probe)
    laid, y = [], 0
    for text, weight, px, gap in lineas:
        ft = ImageFont.truetype(BOLD if weight == "bold" else MED, px)
        y += gap
        sangra = text[:1] in "123456789" and text[1:2] == "."
        for i, ln in enumerate(wrap(d0, text, ft, MAXW - (SANGRIA if sangra else 0))):
            laid.append((ln, ft, y, SANGRIA if (sangra and i) else 0))
            y += int(px * INTERLINEA)
    total = y - int(lineas[-1][2] * (INTERLINEA - 1.0))
    off = BASE_Y - total                      # anclado abajo

    capas = []
    for ln, ft, yy, dx in laid:
        plano = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(plano).text((TEXT_X + dx, off + yy), ln, font=ft, fill=WHITE)
        bb = plano.getbbox()
        caja = (max(0, bb[0] - MARGEN), max(0, bb[1] - MARGEN),
                min(W, bb[2] + MARGEN), min(H, bb[3] + MARGEN))
        capas.append({"img": sombra(plano.crop(caja)), "pos": (caja[0], caja[1])})

    barra = (BAR_X, off - BAR_PAD, BAR_X + BAR_W, off + total + BAR_PAD)
    return capas, barra, total, off


def capa_barra(barra, alto):
    x0, y0, x1, _ = barra
    plano = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(plano).rectangle([x0, y0, x1, y0 + alto], fill=BAR_C)
    caja = (max(0, x0 - MARGEN), max(0, y0 - MARGEN),
            min(W, x1 + MARGEN), min(H, y0 + alto + MARGEN))
    return sombra(plano.crop(caja)), (caja[0], caja[1])


def alfa_capa(img, k):
    if k >= 0.999:
        return img
    c = img.copy()
    c.putalpha(c.split()[3].point(lambda v: int(v * k)))
    return c


def render(lineas, n, salida):
    capas, barra, total, off = componer(lineas)
    alto_barra = barra[3] - barra[1]
    cache = {}
    p = subprocess.Popen(
        [FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
         "-s", "%dx%d" % (W, H), "-r", "24000/1001", "-i", "-",
         "-c:v", "qtrle", "-pix_fmt", "argb", "-r", "24000/1001", salida],
        stdin=subprocess.PIPE)

    for f in range(n):
        cuadro = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        if f < BARRA_IN:
            k = ease_out((f + 1) / BARRA_IN)
        elif f >= n - BARRA_OUT:
            k = 1 - ease_in((f - (n - BARRA_OUT) + 1) / BARRA_OUT)
        else:
            k = 1.0
        hb = int(round(alto_barra * k))
        if hb > 0:
            if hb not in cache:
                cache[hb] = capa_barra(barra, hb)
            img, pos = cache[hb]
            cuadro.alpha_composite(img, pos)

        for i, c in enumerate(capas):
            e0 = ARRANQUE_TXT + i * RETARDO_IN
            s0 = n - TXT_OUT - (len(capas) - 1) * RETARDO_OUT + i * RETARDO_OUT
            if f < e0:
                continue
            if f < e0 + TXT_IN:
                t = ease_out((f - e0 + 1) / TXT_IN)
                a, dy = t, int(round(SUBE_IN * (1 - t)))
            elif f >= s0:
                t = min(1.0, (f - s0 + 1) / TXT_OUT)
                a, dy = 1 - t, -int(round(SUBE_OUT * ease_in(t)))
            else:
                a, dy = 1.0, 0
            if a <= 0.002:
                continue
            cuadro.alpha_composite(alfa_capa(c["img"], a), (c["pos"][0], c["pos"][1] + dy))

        p.stdin.write(cuadro.tobytes())
    p.stdin.close()
    p.wait()
    return total, off


# ---------------------------------------------------------------------------
# (nombre, frame DEL CLIP, duración, líneas).  Línea de tiempo = frame + 409.

if __name__ == "__main__":
    unidades = [int(sys.argv[1])] if len(sys.argv) > 1 else [2, 3, 4, 5]
    solo = sys.argv[2:] or None
    for u in unidades:
        os.makedirs(B % u, exist_ok=True)
        for clave, tipo, ini, dur, lineas in P.UNIDADES[u]['items']:
            if tipo != 'carton':
                continue
            if solo and not any(clave.startswith(s) for s in solo):
                continue
            out = '%s/MA_U%d_%s.mov' % (B % u, u, clave)
            total, off = render(lineas, dur, out)
            aviso = ''
            if total > ALTO_MAX:
                aviso = '  <-- MUY ALTO'
            if off - BAR_PAD < ZONA[1]:
                aviso += '  <-- SE SUBE DE LA ZONA'
            print('U%d %-22s %5d %4d alto %3d cima %3d%s' % (u, clave, ini, dur, total, off - BAR_PAD, aviso), flush=True)
    print('LISTO', flush=True)
