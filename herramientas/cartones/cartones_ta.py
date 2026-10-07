#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cartones de la serie DAE · rejilla A (escala profe Edwin / Terminaciones Anticipadas)

Mide lo que hay, no inventa: la retícula sale de medir A_carton_pausa1.mov y
A_carton_cierre.mov del Caso A, y el cartón de entrada de
'U1-PROFE EDWIN - CASO A - carton de caso.mp4'.

    barra   #FCB500, 28 px de ancho, borde izquierdo en x=176
    texto   Montserrat, x=249, ancho máximo 1250
    centro  óptico del bloque en y=583
    tinte   #03398B al 46 % (alpha 117)
    blanco  fondo #FCFCFC, texto azul noche #07224B
    marca   APRENDE CON LA DAE, 408 px de ancho, en (1351, 131), al 12,5 %

Animación (la misma de la v3 de medio ambiente, que ya pasó revisión):
    la barra crece desde arriba en 10 f con easeOutCubic
    el texto entra desde el frame 6, línea por línea, subiendo 14 px en 14 f,
        escalonado 3 f
    salida: 10 f, bajando 8 px, escalonada 2 f; la barra se retrae en los
        últimos 10 f
    el tinte entra en 12 f y sale en 10 f
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
FPS = "24000/1001"

BAR_X, BAR_W = 176, 28
BAR_C = (252, 181, 0, 255)
TEXT_X = 249
MAXW = 1250
CENTRO_Y = 583
BAR_PAD = 30

TINTE = (3, 57, 139)
TINTE_A = 117            # 46 %
BLANCO_FONDO = (252, 252, 252)
AZUL_NOCHE = (7, 34, 75)

TIT, CUE, SUELTA, ANTE = 54, 44, 72, 30
INTERLINEA = 1.34
GAP_TIT, GAP_CUE, GAP_ANTE = 26, 12, 18

BARRA_IN, BARRA_OUT = 10, 10
TXT_IN, TXT_OUT = 14, 10
RETARDO_IN, RETARDO_OUT = 3, 2
SUBE_IN, SUBE_OUT = 14, 8
ARRANQUE_TXT = 6
TINTE_IN, TINTE_OUT = 12, 10

FDIR = "/usr/share/fonts/truetype/montserrat/"
F_BOLD = FDIR + "Montserrat-Bold.ttf"
F_MED = FDIR + "Montserrat-Medium.ttf"
F_SEMI = FDIR + "Montserrat-SemiBold.ttf"

MARCA = "/mnt/user-data/uploads/DAE/_ref/APRENDE_CON_LA_DAE_alfa.png"
MARCA_BOX = (1351, 131, 408, 278)
MARCA_OP = 0.10


def fuente(path, size):
    return ImageFont.truetype(path, size)


def partir(texto, font, maxw, draw):
    palabras, lineas, cur = texto.split(), [], ""
    for p in palabras:
        t = (cur + " " + p).strip()
        if draw.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lineas.append(cur)
            cur = p
    if cur:
        lineas.append(cur)
    return lineas


def armar_lineas(spec, draw):
    """spec: {'ante':str?, 'titulo':str?, 'cuerpo':str?, 'suelta':str?} -> [(txt, font, size, gap_antes)]"""
    out = []
    if spec.get("suelta"):
        f = fuente(F_BOLD, SUELTA)
        for i, l in enumerate(partir(spec["suelta"], f, MAXW, draw)):
            out.append((l, f, SUELTA, 0 if i == 0 else 0))
        return out
    if spec.get("ante"):
        # NUNCA en versalitas: la identidad de la entidad no usa may\u00fasculas sostenidas.
        # La \u00fanica excepci\u00f3n es la marca de agua, que es un logotipo, no texto.
        f = fuente(F_SEMI, ANTE)
        for i, l in enumerate(partir(spec["ante"], f, MAXW, draw)):
            out.append((l, f, ANTE, 0))
    if spec.get("titulo"):
        f = fuente(F_BOLD, TIT)
        for i, l in enumerate(partir(spec["titulo"], f, MAXW, draw)):
            out.append((l, f, TIT, GAP_ANTE if (i == 0 and out) else 0))
    if spec.get("cuerpo"):
        f = fuente(F_MED, CUE)
        for i, l in enumerate(partir(spec["cuerpo"], f, MAXW, draw)):
            out.append((l, f, CUE, GAP_TIT if (i == 0 and out) else GAP_CUE if i else 0))
    return out


def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


def ease_out(t):
    return 1 - (1 - t) ** 2


def render_carton(spec, nframes, fondo, alfa, salida, con_marca=False, con_tinte=False):
    """fondo: None (transparente) | (r,g,b) | PIL.Image ya a 1920x1080"""
    probe = Image.new("RGBA", (10, 10))
    pd = ImageDraw.Draw(probe)
    lineas = armar_lineas(spec, pd)

    alturas = [int(sz * INTERLINEA) for (_, _, sz, _) in lineas]
    gaps = [g for (_, _, _, g) in lineas]
    total = sum(alturas) + sum(gaps)
    top = CENTRO_Y - total // 2

    ys, y = [], top
    for h, g in zip(alturas, gaps):
        y += g
        ys.append(y)
        y += h
    bar_top = top - BAR_PAD
    bar_bot = y + BAR_PAD - int(alturas[-1] * 0.22)
    bar_h = bar_bot - bar_top

    color_txt = (255, 255, 255) if (alfa or con_tinte) else AZUL_NOCHE

    marca = None
    if con_marca and os.path.exists(MARCA):
        m = Image.open(MARCA).convert("RGBA").resize((MARCA_BOX[2], MARCA_BOX[3]), Image.LANCZOS)
        a = m.getchannel("A").point(lambda v: int(v * MARCA_OP))
        m.putalpha(a)
        marca = m

    pix = "argb" if alfa else "rgb24"
    cmd = ["ffmpeg", "-loglevel", "error", "-y",
           "-f", "rawvideo", "-pix_fmt", pix, "-s", f"{W}x{H}", "-r", FPS, "-i", "-"]
    if alfa:
        cmd += ["-c:v", "qtrle", "-pix_fmt", "argb"]
    else:
        cmd += ["-c:v", "libx264", "-preset", "slow", "-crf", "12", "-pix_fmt", "yuv420p",
                "-g", "400", "-keyint_min", "400", "-sc_threshold", "0"]
    cmd += [salida]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    for f in range(nframes):
        if alfa or fondo is None:
            base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        elif isinstance(fondo, Image.Image):
            base = fondo.copy().convert("RGBA")
        else:
            base = Image.new("RGBA", (W, H), fondo + (255,))

        if con_tinte:
            if f < TINTE_IN:
                ta = TINTE_A * ease_out(f / TINTE_IN)
            elif f >= nframes - TINTE_OUT:
                ta = TINTE_A * (1 - (f - (nframes - TINTE_OUT)) / TINTE_OUT)
            else:
                ta = TINTE_A
            capa = Image.new("RGBA", (W, H), TINTE + (int(ta),))
            base = Image.alpha_composite(base, capa)

        if marca is not None:
            base.alpha_composite(marca, (MARCA_BOX[0], MARCA_BOX[1]))

        cap = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(cap)

        # barra
        if f < BARRA_IN:
            k = ease_out_cubic(f / BARRA_IN)
        elif f >= nframes - BARRA_OUT:
            k = 1 - ease_out_cubic((f - (nframes - BARRA_OUT)) / BARRA_OUT)
        else:
            k = 1.0
        if k > 0:
            d.rectangle([BAR_X, bar_top, BAR_X + BAR_W - 1, bar_top + int(bar_h * k)], fill=BAR_C)

        # texto
        for i, ((txt, font, sz, _), ly) in enumerate(zip(lineas, ys)):
            fi = f - ARRANQUE_TXT - i * RETARDO_IN
            if fi < 0:
                continue
            if fi < TXT_IN:
                t = ease_out_cubic(fi / TXT_IN)
                a, dy = t, int(SUBE_IN * (1 - t))
            else:
                a, dy = 1.0, 0
            fo = f - (nframes - TXT_OUT - (len(lineas) - 1 - i) * RETARDO_OUT)
            if fo >= 0:
                t = min(1.0, fo / TXT_OUT)
                a = min(a, 1 - t)
                dy = int(SUBE_OUT * t)
            if a <= 0.004:
                continue
            d.text((TEXT_X, ly + dy), txt, font=font, fill=color_txt + (int(255 * a),))

        out = Image.alpha_composite(base, cap)
        if alfa:
            r, g, b, al = out.split()
            pr.stdin.write(Image.merge("RGBA", (al, r, g, b)).tobytes())
        else:
            pr.stdin.write(out.convert("RGB").tobytes())

    pr.stdin.close()
    pr.wait()
    print(os.path.basename(salida), nframes, "f", os.path.getsize(salida) // 1024, "KB")


# ─────────────────────────────────────────────────────────────── el contenido

OUT = "/mnt/user-data/outputs/cartones"
os.makedirs(OUT, exist_ok=True)

ALFA = [
    ("a01_120_millones", 132, {"titulo": "Ciento veinte millones",
                               "cuerpo": "Lo que Andrés le entregó a Carlos a cambio de la intervención."}),
    ("a02_400_millones", 160, {"titulo": "Cuatrocientos millones",
                               "cuerpo": "El incremento patrimonial ilícito que obtuvo la empresa contratista."}),
    ("a03_la_propuesta", 151, {"titulo": "La propuesta de la defensa",
                               "cuerpo": "Cien millones ahora. Los trescientos restantes, en un plazo de cinco años."}),
    ("a04_no_es_tramite", 300, {"titulo": "No es un requisito de trámite",
                                "cuerpo": "Impide que la justicia premial beneficie a quien no hizo esfuerzos "
                                          "suficientes para restablecer el patrimonio afectado."}),
    ("a05_antes_no_durante", 114, {"suelta": "Antes, no durante."}),
    ("a06_moneda_de_cambio", 152, {"titulo": "No es moneda de cambio",
                                   "cuerpo": "El reintegro patrimonial es una condición que no puede "
                                             "convertirse en moneda de cambio."}),
]

if __name__ == "__main__":
    solo = sys.argv[1] if len(sys.argv) > 1 else "todo"

    if solo in ("todo", "alfa"):
        for nombre, n, spec in ALFA:
            render_carton(spec, n, None, True, f"{OUT}/TA02_{nombre}.mov", con_tinte=True)

    if solo in ("todo", "blancos"):
        render_carton({"ante": "Caso 02", "titulo": "El doble beneficio y el reintegro"},
                      119, BLANCO_FONDO, False, f"{OUT}/TA02_carton_entrada.mov", con_marca=True)
        render_carton({"suelta": "¿Hasta dónde puede negociar el fiscal?"},
                      119, BLANCO_FONDO, False, f"{OUT}/TA02_carton_cierre.mov", con_marca=True)

    if solo in ("todo", "pausa"):
        kf09 = "/mnt/user-data/uploads/DAE/_probe/KF09_carpeta_cerrada_vA.png"
        fondo = Image.open(kf09).convert("RGB").resize((W, H), Image.LANCZOS)
        render_carton({"suelta": "El reintegro no se negocia. Se verifica."},
                      144, fondo, False, f"{OUT}/TA02_carton_pausa.mov", con_tinte=True)


# ────────────────────────────────────── KF 06 · la aritmética del artículo 349

def render_grafico_349(nframes, salida):
    """Placa limpia, misma familia que los cartones blancos.

    Los tiempos están medidos contra TA02_NARRADOR_B2: el bloque entra en el
    frame 1594 de la línea y la voz arranca 18 f después.
    La marca del 50 % entra DESPUÉS de que la voz dice la cifra, no mientras
    la dice: ese desfase es lo que la hace leerse como conclusión.
    """
    X0, X1 = 249, 1670
    BY, BH = 596, 92
    ANCHO = X1 - X0
    OFRECIDO = ANCHO // 4
    MITAD = ANCHO // 2
    GRIS = (226, 229, 233)
    NAVY = AZUL_NOCHE

    f_ante, f_barra = 6, 18          # antetítulo y barra vacía
    f_ofrecido = 40                  # «cien millones, de cuatrocientos»
    f_lab_izq = 60
    f_lab_der = 410                  # «la garantía del recaudo del remanente»
    f_marca = 548                    # medio segundo después de «cincuenta por ciento»

    f_ante_b = fuente(F_SEMI, ANTE)
    f_tit_b = fuente(F_BOLD, 46)
    f_cif_b = fuente(F_BOLD, 40)
    f_pie_b = fuente(F_MED, 32)
    f_mar_b = fuente(F_BOLD, 34)

    cmd = ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", FPS, "-i", "-", "-c:v", "libx264", "-preset", "slow",
           "-crf", "12", "-pix_fmt", "yuv420p", "-g", "400", "-keyint_min", "400",
           "-sc_threshold", "0", salida]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    def ap(f, inicio, dur=12):
        if f < inicio:
            return 0.0
        return min(1.0, ease_out_cubic((f - inicio) / dur))

    for f in range(nframes):
        im = Image.new("RGB", (W, H), BLANCO_FONDO)
        d = ImageDraw.Draw(im, "RGBA")

        salida_g = max(0.0, 1 - (f - (nframes - 14)) / 14) if f > nframes - 14 else 1.0

        def c(rgb, a):
            return rgb + (int(255 * max(0.0, min(1.0, a * salida_g))),)

        # barra amarilla del titular
        k = ease_out_cubic(min(1.0, max(0.0, (f - 2) / 10)))
        if k > 0:
            d.rectangle([BAR_X, 330, BAR_X + BAR_W - 1, 330 + int(150 * k)], fill=c(BAR_C[:3], 1))

        a = ap(f, f_ante)
        if a > 0:
            d.text((X0, 334), "Artículo 349 · Código de Procedimiento Penal",
                   font=f_ante_b, fill=c(NAVY, a * 0.75))
            d.text((X0, 386), "El reintegro mínimo para poder preacordar",
                   font=f_tit_b, fill=c(NAVY, a))

        # la barra entera — el incremento patrimonial
        a = ap(f, f_barra, 14)
        if a > 0:
            w = int(ANCHO * a)
            d.rectangle([X0, BY, X0 + w, BY + BH], fill=c(GRIS, 1))
            d.text((X0, BY - 112), "Incremento patrimonial · cuatrocientos millones",
                   font=f_pie_b, fill=c(NAVY, a * 0.8))

        # la porción ofrecida
        a = ap(f, f_ofrecido, 16)
        if a > 0:
            d.rectangle([X0, BY, X0 + int(OFRECIDO * a), BY + BH], fill=c(NAVY, 1))

        a = ap(f, f_lab_izq)
        if a > 0:
            d.text((X0, BY + BH + 26), "Cien millones", font=f_cif_b, fill=c(NAVY, a))
            d.text((X0, BY + BH + 76), "ahora", font=f_pie_b, fill=c(NAVY, a * 0.75))

        a = ap(f, f_lab_der)
        if a > 0:
            d.text((X0 + OFRECIDO + 40, BY + BH + 26), "Trescientos millones",
                   font=f_cif_b, fill=c(NAVY, a))
            d.text((X0 + OFRECIDO + 40, BY + BH + 76), "en un plazo de cinco años",
                   font=f_pie_b, fill=c(NAVY, a * 0.75))

        # la marca del cincuenta por ciento
        a = ap(f, f_marca, 16)
        if a > 0:
            x = X0 + MITAD
            alto = int((BH + 70) * a)
            d.rectangle([x - 3, BY - 54, x + 3, BY - 54 + alto], fill=c(BAR_C[:3], 1))
            d.text((x + 22, BY - 58), "mínimo legal", font=f_pie_b, fill=c(NAVY, a * 0.8))
            d.text((x + 22, BY - 22), "cincuenta por ciento", font=f_mar_b, fill=c(NAVY, a))

        pr.stdin.write(im.tobytes())

    pr.stdin.close()
    pr.wait()
    print(os.path.basename(salida), nframes, "f", os.path.getsize(salida) // 1024, "KB")


if len(sys.argv) > 1 and sys.argv[1] in ("grafico", "todo"):
    render_grafico_349(656, f"{OUT}/TA02_KF06_grafico_349.mov")
