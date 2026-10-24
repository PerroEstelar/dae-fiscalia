#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los dos cartones de apertura pasan a verbatim, y se sincronizan.

POR QUÉ ERAN CONFUSOS, QUE ES LO QUE SEBASTIÁN DIJO
    No era el estilo: era que NO DECÍAN LO QUE SE ESTABA OYENDO.

    b01 son tres frases con una pausa de 0,9 s entre cada una. Medidas sobre
    el máster, con un pasabanda de voz para que la cama de música no tape
    los silencios:

        frase 1   12,59 → 18,88 s     las dos audiencias
        frase 2   20,09 → 25,65 s     el medio ofrecido / lo admitido
        frase 3   26,81 → 31,21 s     el alcance del ejercicio

    Y las ranuras:

        r01   12,55 → 19,52 s        (167 cuadros)
        r02   19,52 → 32,03 s        (300 cuadros)

    O sea: sobre r01 se oye la frase 1, y el cartón de r01 parafraseaba la
    frase 2. Sobre r02 se oyen las frases 2 y 3, y el cartón de r02
    parafraseaba solo la 3. Ninguno de los dos decía lo que sonaba debajo.

LO QUE SE HACE
    Cada cartón lleva LITERAL lo que se dice encima de él. El de r01, la
    frase 1. El de r02, las frases 2 y 3 —caben las dos porque la ranura
    dura 12,5 s— y cada renglón ENTRA CUANDO SE DICE: los de la frase 3 a
    los 175 cuadros del cartón, que son los 26,81 s de la pieza.

    Forma: sin antetítulo, un solo bloque, filete amarillo de una pieza que
    crece con el bloque, y el tinte azul de la serie. Es la forma del
    verbatim, que es lo que estas dos frases son.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

AZUL_FGN = (0, 72, 144)          # #004890, el del intro oficial
C.TINTE = AZUL_FGN
AMARILLO = C.BAR_C[:3]
BLANCO = (255, 255, 255)
OUT = "/home/claude/p3c5/cartones/rev25"
os.makedirs(OUT, exist_ok=True)


def _escritor(salida):
    return subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo",
         "-pix_fmt", "argb", "-s", "%dx%d" % (C.W, C.H), "-r", C.FPS,
         "-i", "-", "-c:v", "qtrle", "-pix_fmt", "argb", salida],
        stdin=subprocess.PIPE)


def _t(f, a, b):
    if f <= a:
        return 0.0
    if f >= b:
        return 1.0
    x = (f - a) / float(b - a)
    return x * x * (3 - 2 * x)


def _tinte(f, n):
    if f < C.TINTE_IN:
        ta = C.TINTE_A * C.ease_out(f / float(C.TINTE_IN))
    elif f >= n - C.TINTE_OUT:
        ta = C.TINTE_A * (1 - (f - (n - C.TINTE_OUT)) / float(C.TINTE_OUT))
    else:
        ta = C.TINTE_A
    return Image.new("RGBA", (C.W, C.H), C.TINTE + (int(ta),))


def _escribir(p, im):
    """ARGB, y en ESE orden."""
    r, g, b, al = im.split()
    p.stdin.write(Image.merge("RGBA", (al, r, g, b)).tobytes())


def partir(texto, font, draw, maxw=C.MAXW):
    """Reparte en renglones que caben, sin dejar una palabra sola al final."""
    palabras = texto.split()
    lineas, act = [], ""
    for w in palabras:
        probe = (act + " " + w).strip()
        if draw.textlength(probe, font=font) <= maxw or not act:
            act = probe
        else:
            lineas.append(act)
            act = w
    if act:
        lineas.append(act)
    if len(lineas) > 1 and len(lineas[-1].split()) == 1:
        # una palabra huérfana se lleva otra del renglón anterior
        ant = lineas[-2].split()
        lineas[-1] = ant[-1] + " " + lineas[-1]
        lineas[-2] = " ".join(ant[:-1])
    return lineas


def verbatim(frases, n, salida, y0=400, cuerpo=50, salto=68):
    """Un bloque verbatim con filete, y cada frase entra cuando se dice.

    `frases` es una lista de (texto, cuadro_en_que_empieza_a_decirse).
    El filete va de una sola pieza desde el primer renglón hasta el
    último que ya está puesto: crece con el bloque, no por renglón.
    """
    f_c = C.fuente(C.F_BOLD, cuerpo)
    base = Image.new("RGBA", (10, 10))
    dm = ImageDraw.Draw(base)

    #  UN RESPIRO ENTRE FRASES, O SE LEEN COMO UNA SOLA
    #      Sin el hueco, «...se admite y se practica. Las decisiones
    #      evaluadas...» corre seguido y parece un parrafo de cinco
    #      renglones en vez de dos frases. El hueco es la mitad de un salto.
    renglones = []          # (texto, cuadro_de_entrada, y_relativa)
    y = 0
    for j, (texto, f0) in enumerate(frases):
        if j:
            y += salto // 2
        for i, ln in enumerate(partir(texto, f_c, dm)):
            renglones.append((ln, f0 + i * 9, y))
            y += salto

    p = _escritor(salida)
    for f in range(n):
        im = _tinte(f, n)
        d = ImageDraw.Draw(im)

        # el filete: alto hasta el ultimo renglon que ya esta entrando
        alto = 0.0
        for ln, f0, yr in renglones:
            t = _t(f, f0, f0 + 22)
            if t > 0.004:
                alto = max(alto, (yr + cuerpo + 8) * min(1.0, t * 1.6))
        if alto > 1:
            d.rectangle([C.BAR_X, y0 - 8, C.BAR_X + 10, y0 - 8 + int(alto)],
                        fill=AMARILLO + (255,))

        for ln, f0, yr in renglones:
            t = _t(f, f0, f0 + 26)
            if t <= 0.004:
                continue
            d.text((C.TEXT_X, y0 + yr + int(12 * (1 - t))), ln,
                   font=f_c, fill=BLANCO + (int(248 * t),))
        _escribir(p, im)
    p.stdin.close()
    p.wait()
    print("%-34s %4d f  %d renglones" % (os.path.basename(salida), n,
                                         len(renglones)))


if __name__ == "__main__":
    # r01 · 167 cuadros · la voz dice la frase 1 desde el cuadro 1
    verbatim([("Las escenas que siguen pertenecen a dos momentos de la misma "
               "actuación: la audiencia preparatoria y el juicio.", 2)],
             167, "%s/P3C5_ae00_medio_ofrecido.mov" % OUT,
             y0=430, cuerpo=52, salto=70)

    # r02 · 300 cuadros · frase 2 desde el cuadro 14 (20,09 s) y frase 3
    # desde el 175 (26,81 s)
    verbatim([("En cada una hay que diferenciar el medio que se ofrece de la "
               "información que finalmente se admite y se practica.", 14),
              ("Las decisiones evaluadas se limitan a los hechos y condiciones "
               "expresamente suministrados.", 175)],
             300, "%s/P3C5_ae07_alcance.mov" % OUT,
             y0=396, cuerpo=48, salto=66)
