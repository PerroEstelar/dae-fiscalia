#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones para los videos de introducción — versión 3.

Qué cambia frente a la v2:

  · TAMAÑO. Sebastián escaló los doce a zoom 1.160 en la línea de tiempo.
    Esa escala queda horneada en el archivo: título Bold 46, cuerpo Medium 37,
    frase suelta Bold 54, barra de 14 px. Los items van a zoom 1.0 / pan 0.

  · UBICACIÓN. Medida contra la locutora, no a ojo. En el cuadro limpio ella
    ocupa de x≈790 hacia la derecha entre y 240 y 720, y por debajo de y 720 el
    hombro se le abre hacia la izquierda (a y=840 ya llega a x≈540). El logo
    DAE/Fiscalía ocupa arriba hasta y≈215.
    Queda libre un rectángulo de x 60–790, y 250–720. El bloque se ancla
    ABAJO, en y=690, y crece hacia arriba: así los cartones cortos quedan bien
    bajos — lejos de su cara — y los largos suben por la columna libre en vez
    de invadirla.

  · SOMBRA. Tres capas en vez de dos, más densas: núcleo pegado a la letra,
    ambiental ancha y contacto desplazada. Sigue sin contorno duro.

  · MÁS CARTONES, sobre todo en el último tercio: las actividades pasan de
    tres cartones apretados a siete, uno por actividad, y se agregan dos en la
    zona de las lecciones que estaba floja.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import subprocess, os, json

FPS = 24000 / 1001
FT = "/usr/share/fonts/truetype/montserrat/Montserrat-%s.ttf"
BOLD, MED = FT % "Bold", FT % "Medium"

W, H = 1920, 1080

# --- zona libre medida contra la locutora ---------------------------------
ZONA = (60, 250, 790, 720)
BAR_X, BAR_W, BAR_C = 86, 14, (254, 185, 0, 255)
TEXT_X = 170
MAXW = ZONA[2] - TEXT_X - 5        # 615
BASE_Y = 690                       # el bloque se apoya acá y crece hacia arriba
BAR_PAD = 28
ALTO_MAX = BASE_Y - ZONA[1] - BAR_PAD   # 412
WHITE = (255, 255, 255, 255)
SANGRIA = 46

TIT, CUE, SUELTA = 46, 37, 54      # 1,16 × los cuerpos de la v2
ANTE = 29                          # antetítulo ("Lección 3", "Actividad 2")
INTERLINEA = 1.30
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

# --- sombra: núcleo + ambiental + contacto ---------------------------------
CAPAS_SOMBRA = [
    (3,  0.85, (0, 0)),    # núcleo: pegado a la letra, es lo que da el filo
    (22, 0.70, (0, 0)),    # ambiental: oscurece el fondo alrededor
    (7,  0.70, (0, 4)),    # contacto: peso y dirección
]
MARGEN = 80

# --- animación -------------------------------------------------------------
BARRA_IN, BARRA_OUT = 10, 10
TXT_IN, TXT_OUT = 14, 10
RETARDO_IN, RETARDO_OUT = 3, 2
SUBE_IN, SUBE_OUT = 14, 8
ARRANQUE_TXT = 6

OUT = "/home/claude/ma/out3"
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
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba",
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
OFFSET = 409

CARTONES = [
 ("c01_unidad", 975, 265, [
    ("Unidad 1", "med", ANTE, 0),
    ("Desafíos del Derecho Penal Ambiental y la Constitución Ecológica",
     "bold", TIT, GAP_ANTE)]),

 ("c02_al_finalizar", 1470, 300, [
    ("Al finalizar esta unidad", "bold", TIT, 0),
    ("Aplicar el marco normativo, institucional y dogmático de protección de "
     "los recursos naturales.", "med", CUE, GAP_TIT)]),

 ("c03_sina", 1860, 290, [
    ("Evaluar la intervención", "bold", TIT, 0),
    ("Del derecho penal y del Sistema Nacional Ambiental — SINA — frente a los "
     "daños ecológicos y la explotación ilícita.", "med", CUE, GAP_TIT)]),

 ("c04_cinco_lecciones", 2330, 195, [
    ("Cinco lecciones", "bold", SUELTA, 0)]),

 ("c05_leccion1", 2650, 310, [
    ("Lección 1", "med", ANTE, 0),
    ("Problemáticas del daño al medio ambiente", "bold", TIT, GAP_ANTE),
    ("Deforestación · Explotación ilícita · Grupos armados", "med", CUE, GAP_CUE + 8)]),

 ("c06_leccion2", 3320, 300, [
    ("Lección 2", "med", ANTE, 0),
    ("La Constitución Ecológica", "bold", TIT, GAP_ANTE),
    ("Base del derecho penal ambiental y referente de la actuación del Estado.",
     "med", CUE, GAP_CUE + 8)]),

 ("c07_leccion3", 3880, 310, [
    ("Lección 3", "med", ANTE, 0),
    ("El Sistema Nacional Ambiental", "bold", TIT, GAP_ANTE),
    ("Entidades, institutos, órganos y competencias.", "med", CUE, GAP_CUE + 8)]),

 ("c08_articulacion", 4300, 260, [
    ("Articulación institucional", "bold", TIT, 0),
    ("Qué entidades integran el SINA y qué competencias desarrollan.",
     "med", CUE, GAP_TIT)]),

 ("c09_leccion4", 4680, 265, [
    ("Lección 4", "med", ANTE, 0),
    ("Los ecosistemas", "bold", TIT, GAP_ANTE),
    ("Sujetos de protección especial.", "med", CUE, GAP_CUE + 8)]),

 ("c10_leccion5", 5100, 300, [
    ("Lección 5", "med", ANTE, 0),
    ("Daño ambiental y daño ecológico", "bold", TIT, GAP_ANTE),
    ("La distinción entre las formas de afectación y sus efectos.",
     "med", CUE, GAP_CUE + 8)]),

 ("c11_actividades", 5620, 200, [
    ("Actividades y recursos", "bold", SUELTA, 0)]),

 ("c12_video_intro", 5950, 290, [
    ("Actividad 1", "med", ANTE, 0),
    ("Video introductorio", "bold", TIT, GAP_ANTE),
    ("Problemáticas ambientales y criminalidad.", "med", CUE, GAP_CUE + 8)]),

 ("c13_casos", 6330, 310, [
    ("Actividad 2", "med", ANTE, 0),
    ("Análisis de casos", "bold", TIT, GAP_ANTE),
    ("Problemas prácticos sobre economías ilícitas y minería ilegal.",
     "med", CUE, GAP_CUE + 8)]),

 ("c14_material", 6820, 320, [
    ("Actividad 3", "med", ANTE, 0),
    ("Material virtual", "bold", TIT, GAP_ANTE),
    ("Fundamentación conceptual y jurídica del derecho penal ambiental.",
     "med", CUE, GAP_CUE + 8)]),

 ("c15_dema", 7310, 330, [
    ("Actividad 4", "med", ANTE, 0),
    ("Conversatorio institucional", "bold", TIT, GAP_ANTE),
    ("Con la DEMA, Dirección Especializada en Materia de Derechos del Medio "
     "Ambiente.", "med", CUE, GAP_CUE + 8)]),

 ("c16_al_cerrar", 7780, 330, [
    ("Al cerrar la unidad", "bold", TIT, 0),
    ("Video integrador de repaso y actividad evaluativa de consolidación.",
     "med", CUE, GAP_TIT)]),

 ("c17_proposito", 8600, 330, [
    ("El propósito", "bold", TIT, 0),
    ("Fortalecer las herramientas para investigar y judicializar las conductas "
     "que afectan el medio ambiente.", "med", CUE, GAP_TIT)]),
]

if __name__ == "__main__":
    import sys
    solo = sys.argv[1:] or None
    plan, prev, cubierto = [], None, 0
    print(f"{'cartón':22} {'clip':>6} {'tl':>6} {'dura':>5} {'seg':>6} "
          f"{'hueco':>6} {'alto':>5} {'cima':>5}")
    for nom, a, n, lineas in CARTONES:
        plan.append([nom, a, n])
        cubierto += n
        if solo and nom not in solo:
            prev = a + n
            continue
        total, off = render(lineas, n, f"{OUT}/MA_U1_{nom}.mov")
        hueco = "" if prev is None else "%6.1f" % ((a - prev) / FPS)
        aviso = ""
        if total > ALTO_MAX:
            aviso = "   <-- MUY ALTO (max %d)" % ALTO_MAX
        if off - BAR_PAD < ZONA[1]:
            aviso += "   <-- SE SUBE DE LA ZONA"
        print(f"{nom:22} {a:6d} {a+OFFSET:6d} {n:5d} {n/FPS:6.1f} {hueco:>6} "
              f"{total:5d} {off-BAR_PAD:5d}{aviso}")
        prev = a + n
    print(f"\n{len(CARTONES)} cartones · {cubierto} f en pantalla de 9220 "
          f"({100*cubierto/9220:.0f} %)")
    json.dump({"offset": OFFSET, "zona": ZONA, "cartones": plan},
              open('/home/claude/ma/plan_u1_v3.json', 'w'), ensure_ascii=False)
