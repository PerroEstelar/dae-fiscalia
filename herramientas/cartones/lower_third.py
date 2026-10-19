#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El lower third de la serie DAE: barra amarilla, sin tinte, sin caja.

QUE ES Y QUE NO ES
    Es el cuarto tipo de carton de la serie, y el que faltaba. Los otros tres:
    el BLANCO -solo el titulo general de la pieza-, el TEÑIDO -texto blanco
    sobre la toma con 46 % de azul encima, que es el caballo de batalla- y la
    GRAFICA de After Effects.

    Este no tapa nada. Va sobre la toma limpia, en el tercio inferior, y lleva
    un dato corto: una fecha, el nombre de alguien que acaba de entrar al
    relato. Nunca una frase larga: para eso esta el teñido.

LA LEGIBILIDAD LA HACE UNA SOMBRA, NO UNA CAJA
    Son dos sombras superpuestas bajo el texto y bajo la barra:

        ambiental   negro, difuminado 27 px, 68 %, sin desplazamiento
        contacto    negro, difuminado 5 px, 3 px hacia abajo, 62 %

    LA AMBIENTAL SUBIO DE 18/52 A 27/68, Y ESTA MEDIDO POR QUE
    La cifra del Medio Ambiente v2 se saco sobre fondos de medio a oscuro.
    En el Caso 1 hay dos anfitriones claros: la fachada de r02 mide p50 161
    con el 78 % de la banda por encima de 150, y la camisa blanca de Diana
    en r25 mide p50 193. Ahi el halo de 18 px es demasiado estrecho y el
    renglon de dato pierde el borde.

    Se compararon tres a tamano real sobre esos dos anfitriones:

        18 px / 52 %   el dato se lee flojo sobre la camisa
        27 px / 68 %   separa bien y sigue leyendose como sombra  <- esta
        36 px / 80 %   separa mas, pero ya se lee como una mancha oscura
                       alrededor del texto, que es justo lo que no queremos

    Sobre un anfitrion oscuro la diferencia no se ve: oscurecer lo oscuro no
    cambia nada. Por eso la cifra es una sola para toda la serie y no una por
    carton.

    La ambiental oscurece el fondo alrededor de las letras sin leerse como
    sombra; la de contacto les da peso y direccion. Sin contorno y sin borde
    duro: asi se sostiene lo mismo sobre un muro claro que sobre una sombra.

    Hace falta aunque las placas de esta serie sean gris medio-oscuro: una
    ventana o un cielo en el tercio inferior basta para perder la linea.

LA POSICION
    Centro optico en y=880. El carton teñido de la serie vive en y=583, que es
    la zona de lectura central; el lower third tiene que quedar claramente
    debajo para que se lean como dos cosas distintas y puedan coexistir.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

W, H = 1920, 1080
FPS = "24000/1001"

BAR_X, BAR_W = 176, 20
BAR_C = (252, 181, 0, 255)
TEXT_X = 249
CENTRO_Y = 880
BAR_PAD = 22

NOMBRE, DATO = 46, 34
INTERLINEA = 1.30
GAP_DATO = 8

BARRA_IN, BARRA_OUT = 10, 8
TXT_IN, TXT_OUT = 10, 8
RETARDO = 3
SUBE_IN, SUBE_OUT = 14, 8
ARRANQUE_TXT = 3

SOMBRA_AMB = dict(blur=27, alpha=0.68, dx=0, dy=0)
SOMBRA_CON = dict(blur=5, alpha=0.62, dx=0, dy=3)


def _lineas(spec):
    out = []
    if spec.get("nombre"):
        out.append((spec["nombre"], C.fuente(C.F_BOLD, NOMBRE), NOMBRE, 0))
    if spec.get("dato"):
        out.append((spec["dato"], C.fuente(C.F_MED, DATO), DATO, GAP_DATO))
    return out


def render(spec, nframes, salida):
    lineas = _lineas(spec)
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

    os.makedirs(os.path.dirname(salida), exist_ok=True)
    pr = subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "argb",
         "-s", "%dx%d" % (W, H), "-r", FPS, "-i", "-",
         "-c:v", "qtrle", "-pix_fmt", "argb", salida], stdin=subprocess.PIPE)

    for f in range(nframes):
        tinta = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(tinta)

        if f < BARRA_IN:
            k = C.ease_out_cubic(f / BARRA_IN)
        elif f >= nframes - BARRA_OUT:
            k = 1 - C.ease_out_cubic((f - (nframes - BARRA_OUT)) / BARRA_OUT)
        else:
            k = 1.0
        if k > 0:
            d.rectangle([BAR_X, bar_top, BAR_X + BAR_W - 1, bar_top + int(bar_h * k)],
                        fill=BAR_C)

        for i, ((txt, font, sz, _), ly) in enumerate(zip(lineas, ys)):
            fi = f - ARRANQUE_TXT - i * RETARDO
            if fi < 0:
                continue
            if fi < TXT_IN:
                t = C.ease_out_cubic(fi / TXT_IN)
                a, dy = t, int(SUBE_IN * (1 - t))
            else:
                a, dy = 1.0, 0
            fo = f - (nframes - TXT_OUT - (len(lineas) - 1 - i) * RETARDO)
            if fo >= 0:
                t = min(1.0, fo / TXT_OUT)
                a = min(a, 1 - t)
                dy = int(SUBE_OUT * t)
            if a <= 0.004:
                continue
            d.text((TEXT_X, ly + dy), txt, font=font, fill=(255, 255, 255, int(255 * a)))

        # las dos sombras salen de la MISMA tinta, asi la barra tambien las lleva
        base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        for s in (SOMBRA_AMB, SOMBRA_CON):
            sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            alfa = tinta.getchannel("A").filter(ImageFilter.GaussianBlur(s["blur"]))
            alfa = alfa.point(lambda v, a=s["alpha"]: int(v * a))
            sombra.putalpha(alfa)
            base = Image.alpha_composite(base, sombra.transform(
                (W, H), Image.AFFINE, (1, 0, -s["dx"], 0, 1, -s["dy"])))
        out = Image.alpha_composite(base, tinta)

        r, g, b, al = out.split()
        pr.stdin.write(Image.merge("RGBA", (al, r, g, b)).tobytes())

    pr.stdin.close()
    pr.wait()
    print(os.path.basename(salida), nframes, "f", os.path.getsize(salida) // 1024, "KB")
