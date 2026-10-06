#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones para los videos de introducción — versión 2.

Cambios frente a la v1:
  · El texto vive dentro de la caja que marcó la DAE: x 62–730, y 278–650.
  · Sin tinte azul. Alfa limpia: se ve el plano entero detrás.
  · Legibilidad por sombra, no por fondo: una sombra ambiental ancha y suave
    que oscurece el fondo alrededor de las letras, más una sombra de contacto
    corta y desplazada que les da peso. Nada de contorno ni de caja.
  · Entradas y salidas animadas: la barra amarilla crece desde arriba, el
    texto sube y aparece línea por línea, y al salir se va en el mismo orden.

Retícula de la caja (misma proporción que la rejilla JEP, a escala):
  barra  #FEB900, 12 px, borde izquierdo x=72
  texto  Montserrat blanco, borde izquierdo x=140   (68 px de separación)
  ancho máximo 582 · centro óptico y=464 · aire de barra 24
  título Bold 40 · cuerpo Medium 32 · frase suelta Bold 46
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, os, json, math

FPS = 24000 / 1001
FT = "/usr/share/fonts/truetype/montserrat/Montserrat-%s.ttf"
BOLD, MED = FT % "Bold", FT % "Medium"

W, H = 1920, 1080

# --- la caja marcada por la DAE -------------------------------------------
BOX = (62, 278, 730, 650)
BAR_X, BAR_W, BAR_C = 72, 12, (254, 185, 0, 255)
TEXT_X = 140
MAXW = BOX[2] - TEXT_X - 8                 # 582
CENTER_Y = (BOX[1] + BOX[3]) // 2          # 464
BAR_PAD = 24
ALTO_MAX = (BOX[3] - BOX[1]) - 2 * BAR_PAD  # 324
WHITE = (255, 255, 255, 255)
SANGRIA = 40

# --- sombra ----------------------------------------------------------------
AMB_BLUR, AMB_A, AMB_OFF = 18, 0.52, (0, 0)    # ambiental: despega del fondo
CON_BLUR, CON_A, CON_OFF = 5, 0.62, (0, 3)     # contacto: le da peso
MARGEN = 60                                     # aire para recortar las capas

# --- animación -------------------------------------------------------------
BARRA_IN, BARRA_OUT = 10, 10
TXT_IN, TXT_OUT = 14, 10
RETARDO_IN, RETARDO_OUT = 3, 2                 # escalonado entre líneas
SUBE_IN, SUBE_OUT = 14, 8                      # px que recorre cada línea
ARRANQUE_TXT = 6                               # el texto entra tras la barra

OUT = "/home/claude/ma/out2"
os.makedirs(OUT, exist_ok=True)


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
    """Devuelve la capa con su sombra debajo, ya compuesta."""
    a = capa.split()[3]
    fondo = Image.new("RGBA", capa.size, (0, 0, 0, 0))
    for blur, alfa, (ox, oy) in ((AMB_BLUR, AMB_A, AMB_OFF), (CON_BLUR, CON_A, CON_OFF)):
        m = a.filter(ImageFilter.GaussianBlur(blur))
        m = m.point(lambda v: int(v * alfa))
        s = Image.new("RGBA", capa.size, (0, 0, 0, 0))
        s.putalpha(m)
        fondo.alpha_composite(s, (0, 0)) if (ox, oy) == (0, 0) else None
        if (ox, oy) != (0, 0):
            desp = Image.new("RGBA", capa.size, (0, 0, 0, 0))
            desp.paste(s, (ox, oy))
            fondo.alpha_composite(desp)
    fondo.alpha_composite(capa)
    return fondo


def componer(lineas):
    """Mide y arma: devuelve las capas de cada línea (recortadas) y la barra."""
    probe = Image.new("RGBA", (10, 10))
    d0 = ImageDraw.Draw(probe)
    laid, y = [], 0
    for text, weight, px, gap in lineas:
        ft = ImageFont.truetype(BOLD if weight == "bold" else MED, px)
        y += gap
        sangra = text[:1] in "123456789" and text[1:2] == "."
        for i, ln in enumerate(wrap(d0, text, ft, MAXW - (SANGRIA if sangra else 0))):
            laid.append((ln, ft, y, SANGRIA if (sangra and i) else 0, px))
            y += int(px * 1.30)
    total = y - int(lineas[-1][2] * 0.30)
    off = CENTER_Y - total // 2

    capas = []
    for ln, ft, yy, dx, px in laid:
        plano = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(plano).text((TEXT_X + dx, off + yy), ln, font=ft, fill=WHITE)
        bb = plano.getbbox()
        caja = (max(0, bb[0] - MARGEN), max(0, bb[1] - MARGEN),
                min(W, bb[2] + MARGEN), min(H, bb[3] + MARGEN))
        capas.append({"img": sombra(plano.crop(caja)), "pos": (caja[0], caja[1])})

    barra = (BAR_X, off - BAR_PAD, BAR_X + BAR_W, off + total + BAR_PAD)
    return capas, barra, total, off


def capa_barra(barra, alto):
    """La barra recortada a `alto` px desde arriba, con su sombra."""
    x0, y0, x1, y1 = barra
    if alto <= 0:
        return None
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
    cache_barra = {}

    p = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
         "-s", "%dx%d" % (W, H), "-r", "24000/1001", "-i", "-",
         "-c:v", "qtrle", "-pix_fmt", "argb", "-r", "24000/1001", salida],
        stdin=subprocess.PIPE)

    for f in range(n):
        cuadro = Image.new("RGBA", (W, H), (0, 0, 0, 0))

        # barra
        if f < BARRA_IN:
            k = ease_out((f + 1) / BARRA_IN)
        elif f >= n - BARRA_OUT:
            k = 1 - ease_in((f - (n - BARRA_OUT) + 1) / BARRA_OUT)
        else:
            k = 1.0
        hb = int(round(alto_barra * k))
        if hb > 0:
            if hb not in cache_barra:
                cache_barra[hb] = capa_barra(barra, hb)
            img, pos = cache_barra[hb]
            cuadro.alpha_composite(img, pos)

        # líneas
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
# (nombre, frame DEL CLIP donde entra, duración, líneas)
# En la línea de tiempo hay que sumar 409: ahí arranca el clip de la unidad.
OFFSET = 409

CARTONES = [
 ("c01_unidad", 975, 265, [
    ("Unidad 1", "bold", 40, 0),
    ("Desafíos del Derecho Penal Ambiental y la Constitución Ecológica",
     "med", 32, 24)]),

 ("c02_al_finalizar", 1470, 300, [
    ("Al finalizar esta unidad", "bold", 40, 0),
    ("Aplicar el marco normativo, institucional y dogmático de protección de "
     "los recursos naturales.", "med", 32, 24)]),

 ("c03_sina", 1860, 290, [
    ("Evaluar la intervención", "bold", 40, 0),
    ("Del derecho penal y del Sistema Nacional Ambiental — SINA — frente a los "
     "daños ecológicos y la explotación ilícita.", "med", 32, 24)]),

 ("c04_cinco_lecciones", 2330, 195, [
    ("Cinco lecciones", "bold", 46, 0)]),

 ("c05_leccion1", 2650, 310, [
    ("Lección 1 · Problemáticas del daño al medio ambiente", "bold", 40, 0),
    ("Deforestación · Explotación ilícita · Vinculación de grupos armados",
     "med", 32, 24)]),

 ("c06_leccion2", 3320, 300, [
    ("Lección 2 · La Constitución Ecológica", "bold", 40, 0),
    ("Base fundamental del derecho penal ambiental y referente de la actuación "
     "del Estado.", "med", 32, 24)]),

 ("c07_leccion3", 3880, 290, [
    ("Lección 3 · El Sistema Nacional Ambiental", "bold", 40, 0),
    ("Entidades, institutos, órganos y competencias.", "med", 32, 24)]),

 ("c08_leccion4", 4660, 265, [
    ("Lección 4 · Los ecosistemas", "bold", 40, 0),
    ("Sujetos de protección especial.", "med", 32, 24)]),

 ("c09_leccion5", 5100, 300, [
    ("Lección 5 · Daño ambiental y daño ecológico", "bold", 40, 0),
    ("La distinción que permite comprender las formas de afectación y sus "
     "efectos.", "med", 32, 24)]),

 ("c10_actividades", 5950, 340, [
    ("Las actividades", "bold", 40, 0),
    ("1. Video introductorio sobre problemáticas ambientales y criminalidad",
     "med", 32, 24),
    ("2. Análisis de casos: economías ilícitas y minería ilegal", "med", 32, 10)]),

 ("c11_material_dema", 6870, 330, [
    ("También encontrarán", "bold", 40, 0),
    ("3. Material virtual de fundamentación conceptual y jurídica", "med", 32, 24),
    ("4. Conversatorio institucional con la DEMA", "med", 32, 10)]),

 ("c12_cierre", 7790, 330, [
    ("Al cerrar la unidad", "bold", 40, 0),
    ("5. Video integrador de repaso", "med", 32, 24),
    ("6. Actividad evaluativa de consolidación de conceptos", "med", 32, 10)]),
]


if __name__ == "__main__":
    import sys
    solo = sys.argv[1:] or None
    plan = []
    print(f"{'cartón':22} {'clip':>6} {'tl':>6} {'dura':>5} {'seg':>6} {'alto':>5}")
    for nom, a, n, lineas in CARTONES:
        if solo and nom not in solo:
            plan.append([nom, a, n])
            continue
        total, off = render(lineas, n, f"{OUT}/MA_U1_{nom}.mov")
        aviso = ""
        if total > ALTO_MAX:
            aviso = "   <-- SE SALE DE LA CAJA (max %d)" % ALTO_MAX
        print(f"{nom:22} {a:6d} {a+OFFSET:6d} {n:5d} {n/FPS:6.1f} {total:5d}{aviso}")
        plan.append([nom, a, n])
    json.dump({"offset": OFFSET, "caja": BOX, "cartones": plan},
              open('/home/claude/ma/plan_u1_v2.json', 'w'), ensure_ascii=False)
