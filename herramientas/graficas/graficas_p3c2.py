#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las dos gráficas de motion del Caso 2 «El taller del segundo piso».

POR QUÉ ESTAS DOS Y NO OTRAS
    De los catorce cartones `ae` del caso, dos no son texto que se pueda poner
    encima de una imagen: son el texto Y su forma al mismo tiempo.

    `ae02` dice que de seis personas, dos conservan sus documentos y pueden
    irse, y las otras cuatro no. Esa partición ES la tesis del caso —el
    inmueble no es una cosa sola— y escrita en dos renglones se lee como un
    dato más. Dibujada, la fila de seis que se abre en 2 y 4 dice en dos
    segundos lo que el cartón tarda nueve en decir.

    `ae13` enumera las cinco decisiones que el equipo tiene pendientes. Una
    lista que aparece renglón a renglón es una lista; escrita de corrido con
    puntos medios es un párrafo.

LOS NÚMEROS SON EL DIBUJO
    Sebastián pidió dígitos en pantalla. Aquí el dígito no es tipografía: el
    2 y el 4 van grandes, en amarillo, encima de su grupo, y la fila de
    figuras los verifica. Es la única forma de la serie en que el número se
    puede contar con el ojo.

LAS FIGURAS NO SON PERSONAJES
    Seis siluetas idénticas, sin rostro y sin acento de color. Si se
    distinguieran entre sí el participante empezaría a adivinar quién es
    quién, y la gracia del plano es exactamente que todavía no se sabe.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

W, H = 1920, 1080
FPS = "24000/1001"
OUT = "/mnt/user-data/outputs/ranuras_p3c2"

FONDO = C.AZUL_NOCHE
FIGURA = (206, 209, 214)
AMARILLO = (252, 181, 0)
CANAL_NUM = 16          # aire entre el numero y el texto del item
BLANCO = (255, 255, 255)


def _escritor(salida, n):
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    return subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", "%dx%d" % (W, H), "-r", FPS, "-i", "-", "-an", "-c:v", "libx264",
         "-preset", "slow", "-crf", "12", "-pix_fmt", "yuv420p", "-g", "600",
         "-keyint_min", "600", "-sc_threshold", "0", salida], stdin=subprocess.PIPE)


def _t(f, a, b):
    if f <= a:
        return 0.0
    if f >= b:
        return 1.0
    return C.ease_out_cubic((f - a) / float(b - a))


def _figura(d, cx, base, alto, color):
    """Una silueta sencilla: cabeza y torso. Sin rostro, sin acento."""
    rc = alto * 0.15
    d.ellipse([cx - rc, base - alto, cx + rc, base - alto + 2 * rc], fill=color)
    hombro = cx - alto * 0.22
    d.polygon([(hombro, base), (hombro + alto * 0.05, base - alto * 0.60),
               (cx - rc * 0.9, base - alto * 0.68), (cx + rc * 0.9, base - alto * 0.68),
               (cx + alto * 0.22 - alto * 0.05, base - alto * 0.60),
               (cx + alto * 0.22, base)], fill=color)


def _bloque(spec, centro_y, maxw):
    probe = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    viejo, C.MAXW = C.MAXW, maxw
    lineas = C.armar_lineas(spec, probe)
    C.MAXW = viejo
    alturas = [int(sz * C.INTERLINEA) for (_, _, sz, _, _) in lineas]
    gaps = [g for (_, _, _, g, _) in lineas]
    top = centro_y - (sum(alturas) + sum(gaps)) // 2
    ys, y = [], top
    for h, g in zip(alturas, gaps):
        y += g
        ys.append(y)
        y += h
    return lineas, ys, (top - C.BAR_PAD, y + C.BAR_PAD - int(alturas[-1] * 0.22))


def _texto(d, lineas, x, ys, f, desde, paso):
    for i, ((txt, font, sz, _, sg), y) in enumerate(zip(lineas, ys)):
        t = _t(f, desde + i * paso, desde + i * paso + 10)
        if t <= 0.004:
            continue
        d.text((x + sg, y + int(12 * (1 - t))), txt, font=font,
               fill=BLANCO + (int(255 * t),))


# ------------------------------------------------------------------ r03
def seis_personas(n=217, salida=None):
    """Seis siluetas que se abren en 2 y 4, con su número encima."""
    salida = salida or "%s/P3C2_r03_graf_seis_personas_v217.mov" % OUT
    # El encabezado es solo el número. La primera version decia ademas
    # «Trabajan y duermen en el taller», que es LITERALMENTE lo que dice el
    # carton n02 en la ranura siguiente: el espectador lo leia dos veces
    # seguidas. Lo que esta grafica tiene que decir lo dicen los dos grupos.
    lineas, ys, (bt, bb) = _bloque({"titulo": "6 personas"}, 240, 1250)
    BASE, ALTO, PASO = 700, 220, 150
    CENTRO = W // 2
    SEP = 150                       # cuánto se abre el hueco entre los grupos
    f_num = C.fuente(C.F_BOLD, 96)
    f_lab = C.fuente(C.F_MED, 32)
    LAB = ["Conservan sus documentos,\ncobran por prenda y pueden irse",
           "14 horas, descuentos por alojamiento\ny una deuda sin explicar"]

    p = _escritor(salida, n)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")

        d.rectangle([C.BAR_X, bt, C.BAR_X + C.BAR_W - 1,
                     bt + int((bb - bt) * _t(f, 0, 10))], fill=AMARILLO)
        _texto(d, lineas, C.TEXT_X, ys, f, 2, 1)

        ap = _t(f, 46, 88)          # la apertura
        for i in range(6):
            ent = _t(f, 16 + i * 5, 16 + i * 5 + 12)
            if ent <= 0.004:
                continue
            x = CENTRO + (i - 2.5) * PASO
            x += (-SEP if i < 2 else SEP) * ap
            col = FIGURA + (int(255 * ent),)
            _figura(d, x, BASE, int(ALTO * (0.88 + 0.12 * ent)), col)

        # el número de cada grupo, y su rótulo
        for g, (cuantos, idx) in enumerate(((2, (0, 1)), (4, (2, 3, 4, 5)))):
            tn = _t(f, 92, 108)
            if tn <= 0.004:
                continue
            xs = [CENTRO + (i - 2.5) * PASO + (-SEP if i < 2 else SEP) * ap
                  for i in idx]
            cx = sum(xs) / float(len(xs))
            txt = str(cuantos)
            an = d.textlength(txt, font=f_num)
            d.text((cx - an / 2, BASE - ALTO - 150 + int(14 * (1 - tn))), txt,
                   font=f_num, fill=AMARILLO + (int(255 * tn),))
            tl = _t(f, 104 + g * 8, 120 + g * 8)
            if tl <= 0.004:
                continue
            d.line([(cx - 150, BASE + 46), (cx + 150, BASE + 46)],
                   fill=AMARILLO + (int(230 * tl),), width=3)
            for j, ren in enumerate(LAB[g].split("\n")):
                aw = d.textlength(ren, font=f_lab)
                d.text((cx - aw / 2, BASE + 74 + j * 44 + int(10 * (1 - tl))),
                       ren, font=f_lab, fill=BLANCO + (int(235 * tl),))

        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(os.path.basename(salida), n, "f", os.path.getsize(salida) // 1024, "KB")


# ------------------------------------------------------------------ r26
def cinco_decisiones(n=215, salida=None):
    """Las cinco decisiones pendientes, renglón a renglón."""
    salida = salida or "%s/P3C2_r26_graf_cinco_decisiones_v215.mov" % OUT
    lineas, ys, (bt, bb) = _bloque({"ante": "El equipo debe decidir"}, 230, 1250)
    ITEMS = ["Asistencia", "Canales de comunicación",
             "Condiciones de entrevista", "Participación",
             "Líneas de investigación"]
    f_it = C.fuente(C.F_BOLD, 54)
    f_no = C.fuente(C.F_SEMI, 30)
    Y0, DY = 430, 112

    p = _escritor(salida, n)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")

        d.rectangle([C.BAR_X, bt, C.BAR_X + C.BAR_W - 1,
                     bt + int((bb - bt) * _t(f, 0, 10))], fill=AMARILLO)
        _texto(d, lineas, C.TEXT_X, ys, f, 2, 1)

        for i, it in enumerate(ITEMS):
            t = _t(f, 24 + i * 16, 24 + i * 16 + 14)
            if t <= 0.004:
                continue
            y = Y0 + i * DY + int(16 * (1 - t))
            d.rectangle([C.BAR_X, y + 6, C.BAR_X + 10, y + 56],
                        fill=AMARILLO + (int(255 * t),))
            # El numero va en la canal entre el filete y el texto, alineado a
            # la derecha. En la primera version se dibujaba en TEXT_X - 64 =
            # 185, y el filete llega hasta 186: el filete se comia el trazo
            # izquierdo del digito, y siendo los dos amarillos el numero se
            # leia pegado al filete. Alinear a la derecha ademas pone los
            # cinco digitos en columna, que es lo correcto en una lista.
            num = str(i + 1)
            an = d.textlength(num, font=f_no)
            d.text((C.TEXT_X - CANAL_NUM - an, y + 11), num, font=f_no,
                   fill=AMARILLO + (int(220 * t),))
            d.text((C.TEXT_X, y), it, font=f_it, fill=BLANCO + (int(255 * t),))

        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(os.path.basename(salida), n, "f", os.path.getsize(salida) // 1024, "KB")


if __name__ == "__main__":
    seis_personas()
    cinco_decisiones()
