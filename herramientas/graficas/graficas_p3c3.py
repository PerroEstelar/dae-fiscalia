#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las tres graficas de motion del Caso 3 «Ruta del Golfo».

POR QUE TRES Y NO DOS
    Los dos casos anteriores llevaron dos. Aqui hay tres que se ganan el
    lugar, y ninguna cuesta creditos porque se renderizan en local.

    `g1 la ruta`      orienta en siete segundos lo que la locucion tardaria
                      cuarenta en situar, y el caso se llama asi.
    `g2 antes y despues`  ES el caso. Si una sola cosa de esta pieza se queda
                      en la cabeza, es esta.
    `g3 los recursos` es lo que hace que el ejercicio muerda: sin la escasez,
                      «revisar el programa» no cuesta nada.

LA SEGUNDA ES LA QUE HAY QUE MIRAR CON CUIDADO
    `g2` pone en dos columnas lo que el informe inicial atribuia a cada
    proveedor y lo que la reunion de evaluacion mostro. La tentacion es
    dibujar cuatro tachones: cuatro atribuciones, cuatro desmentidos, caso
    cerrado. Seria falso.

    El caso desmiente TRES y deja UNA en pie: la contabilidad de Teresa sigue
    registrando deuda sin cierre y cargos que no disminuyen pese al trabajo.
    Por eso su fila NO se tacha, y lleva en la columna derecha el unico texto
    que no empieza por una negacion.

    Esa asimetria es el contenido de la grafica. Dibujarla simetrica seria
    hacer con la imagen lo que el caso enseña a no hacer con el expediente:
    conservar por inercia una lectura pareja para todos.

LOS NOMBRES VAN, Y LOS ACENTOS TAMBIEN
    Es la unica grafica de la serie donde aparecen los cuatro nombres juntos.
    Cada uno lleva el filete de su acento -azul Teresa, amarillo los otros
    tres-, que es la misma gramatica de las placas y no una decoracion.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

W, H = 1920, 1080
FPS = "24000/1001"
OUT = "/mnt/user-data/outputs/graficas_p3c3"

FONDO = C.AZUL_NOCHE
AMARILLO = (252, 197, 14)
AZUL = (8, 83, 159)
BLANCO = (255, 255, 255)
GRIS = (150, 156, 166)


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


def _cabecera(d, lineas, ys, bt, bb, f):
    """Sin filete amarillo: el titulo entra solo.

    Sebastian, 21 oct: el filete grande junto al titulo no dice nada y
    ensucia. Los filetes pequenos de cada nombre si se quedan, porque esos
    son la gramatica de acento de la serie y no decoracion.
    """
    _texto(d, lineas, C.TEXT_X, ys, f, 2, 1)


# ------------------------------------------------------------------ r03
def la_ruta(n=168, salida=None):
    """Medellin, la carretera, Necoclí. Y a donde sigue."""
    salida = salida or "%s/P3C3_r03_graf_la_ruta_v168.mov" % OUT
    lineas, ys, (bt, bb) = _bloque({"titulo": "La ruta"}, 220, 1250)
    f_ciu = C.fuente(C.F_BOLD, 54)
    f_pie = C.fuente(C.F_MED, 32)
    Y = 640
    X0, X1 = 330, 1590
    PUNTOS = [(X0, "Medellín", "origen"),
              (X1, "Necoclí", "último punto conocido")]

    p = _escritor(salida, n)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")
        _cabecera(d, lineas, ys, bt, bb, f)

        # la linea, que se dibuja de izquierda a derecha
        k = _t(f, 18, 70)
        if k > 0.004:
            d.line([(X0, Y), (X0 + int((X1 - X0) * k), Y)],
                   fill=GRIS + (235,), width=4)
        # la continuacion, punteada: el viaje sigue y el caso no lo cubre
        k2 = _t(f, 78, 108)
        if k2 > 0.004:
            x = X1
            while x < X1 + int(230 * k2):
                d.line([(x, Y), (min(x + 16, X1 + int(230 * k2)), Y)],
                       fill=GRIS + (150,), width=4)
                x += 30

        for i, (x, ciudad, pie) in enumerate(PUNTOS):
            t = _t(f, 24 + i * 26, 24 + i * 26 + 14)
            if t <= 0.004:
                continue
            rr = int(13 * t)
            d.ellipse([x - rr, Y - rr, x + rr, Y + rr], fill=AMARILLO + (int(255 * t),))
            an = d.textlength(ciudad, font=f_ciu)
            d.text((x - an / 2, Y - 110 + int(14 * (1 - t))), ciudad,
                   font=f_ciu, fill=BLANCO + (int(255 * t),))
            ap = d.textlength(pie, font=f_pie)
            d.text((x - ap / 2, Y + 44 + int(10 * (1 - t))), pie,
                   font=f_pie, fill=GRIS + (int(235 * t),))

        t = _t(f, 112, 134)
        if t > 0.004:
            txt = "Abril de 2026"
            an = d.textlength(txt, font=f_pie)
            d.text(((W - an) / 2, Y + 210 + int(10 * (1 - t))), txt,
                   font=f_pie, fill=BLANCO + (int(220 * t),))

        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(os.path.basename(salida), n, "f", os.path.getsize(salida) // 1024, "KB")


# ------------------------------------------------------------------ r22
def antes_y_despues(n=358, salida=None):
    """Cuatro proveedores, dos columnas. Tres se desarman y una queda."""
    salida = salida or "%s/P3C3_r22_graf_antes_y_despues_v358.mov" % OUT
    lineas, ys, (bt, bb) = _bloque(
        {"ante": "En la reunión de evaluación",
         "titulo": "Lo que el informe atribuía · lo que los resultados mostraron"},
        205, 1420)
    f_nom = C.fuente(C.F_BOLD, 40)
    f_col = C.fuente(C.F_MED, 30)
    XN, XA, XD = 190, 470, 1120
    Y0, DY = 460, 142
    #  (nombre, acento, antes, despues, se_desarma)
    FILAS = [
        ("Luis", AMARILLO, "Usuario de la cuenta",
         "No se ha establecido si la controlaba\ntodo el período", True),
        ("Marta", AMARILLO, "Cinco giros a su nombre",
         "Tres son remesas familiares\ny el resto, gastos del grupo", True),
        ("Omar", AMARILLO, "Conduce el vehículo",
         "Orden de servicio anterior,\ncon tarifa ordinaria", True),
        ("Teresa", AZUL, "Administra el alojamiento",
         "Su contabilidad registra deuda\nsin cierre", False),
    ]

    p = _escritor(salida, n)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")
        _cabecera(d, lineas, ys, bt, bb, f)

        for i, (nom, ac, antes, desp, tacha) in enumerate(FILAS):
            y = Y0 + i * DY
            t = _t(f, 30 + i * 18, 30 + i * 18 + 14)
            if t <= 0.004:
                continue
            dy = int(14 * (1 - t))
            d.rectangle([C.BAR_X, y + dy, C.BAR_X + 8, y + 62 + dy],
                        fill=ac + (int(255 * t),))
            d.text((XN, y + 8 + dy), nom, font=f_nom, fill=BLANCO + (int(255 * t),))
            for j, ren in enumerate(antes.split("\n")):
                d.text((XA, y + 12 + j * 38 + dy), ren, font=f_col,
                       fill=GRIS + (int(235 * t),))

            # la columna derecha entra despues, fila por fila
            t2 = _t(f, 120 + i * 30, 120 + i * 30 + 16)
            if t2 <= 0.004:
                continue
            for j, ren in enumerate(desp.split("\n")):
                d.text((XD, y + 12 + j * 38 + int(10 * (1 - t2))), ren,
                       font=f_col, fill=BLANCO + (int(250 * t2),))
            # y solo entonces se tacha lo que se desarmo
            if tacha:
                t3 = _t(f, 136 + i * 30, 136 + i * 30 + 14)
                if t3 > 0.004:
                    an = max(d.textlength(r, font=f_col) for r in antes.split("\n"))
                    yy = y + 12 + 19 + (19 if "\n" in antes else 0)
                    d.line([(XA, yy), (XA + int(an * t3), yy)],
                           fill=GRIS + (int(220 * t3),), width=3)

        # la linea de cierre al pie salio apretada y se quito (21 oct).
        # La asimetria ya la dice la fila de Teresa, que es la unica sin
        # tachar: no hace falta subrayarla con texto.

        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(os.path.basename(salida), n, "f", os.path.getsize(salida) // 1024, "KB")


# ------------------------------------------------------------------ r29
def los_recursos(n=176, salida=None):
    """Con que cuenta el equipo, y que esta a punto de perder."""
    salida = salida or "%s/P3C3_r29_graf_los_recursos_v176.mov" % OUT
    lineas, ys, (bt, bb) = _bloque({"ante": "El equipo cuenta con",
                                    "titulo": "Un plazo interno limitado"}, 215, 1250)
    f_it = C.fuente(C.F_BOLD, 48)
    f_pi = C.fuente(C.F_MED, 30)
    TIENE = ["Un analista digital", "Un investigador de campo",
             "Un analista financiero"]
    Y0, DY = 470, 104

    p = _escritor(salida, n)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")
        _cabecera(d, lineas, ys, bt, bb, f)

        for i, it in enumerate(TIENE):
            t = _t(f, 26 + i * 16, 26 + i * 16 + 14)
            if t <= 0.004:
                continue
            y = Y0 + i * DY + int(14 * (1 - t))
            d.rectangle([C.BAR_X, y + 6, C.BAR_X + 10, y + 52],
                        fill=AMARILLO + (int(255 * t),))
            d.text((C.TEXT_X, y), it, font=f_it, fill=BLANCO + (int(255 * t),))

        # y lo que se va
        t = _t(f, 92, 118)
        if t > 0.004:
            y = Y0 + 3 * DY + 44
            d.line([(C.BAR_X, y), (C.BAR_X + 1250, y)],
                   fill=GRIS + (int(120 * t),), width=2)
            txt = "Y dos de sus fuentes continúan el viaje"
            d.text((C.TEXT_X, y + 36 + int(12 * (1 - t))), txt, font=f_it,
                   fill=GRIS + (int(245 * t),))
            t2 = _t(f, 112, 138)
            if t2 > 0.004:
                d.text((C.TEXT_X, y + 104 + int(10 * (1 - t2))),
                       "Solo podrán mantener contacto por una aplicación",
                       font=f_pi, fill=GRIS + (int(225 * t2),))

        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(os.path.basename(salida), n, "f", os.path.getsize(salida) // 1024, "KB")


if __name__ == "__main__":
    la_ruta()
    antes_y_despues()
    los_recursos()
