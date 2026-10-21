#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las tres graficas de motion del Caso 4 «Puerto de salida».

DONDE VAN, Y CONTRA QUE FRASE
    Las tres se disenan contra la frase MEDIDA que se oye encima, igual que
    las placas. Leido de `cruce_p3c4.json`:

      r06 · 209 cuadros · Pilar
        «La identidad de los pasajeros, y la regulación migratoria aplicable
         a ese episodio, ya fueron individualizadas en la carpeta.»
      r36 · 205 cuadros · Carlos
        «El equipo trata las tres modificaciones como simples precisiones...»
      r38 · 292 cuadros · Pilar
        «El equipo debe revisar, una por una, las seis actuaciones. Qué se
         pidió, con qué sustento y con qué alcance...»

UN CAMBIO RESPECTO A LA PREPRODUCCION, Y LA RAZON
    El plan decia que la de r06 fuera la cadena de las seis actuaciones. Al
    correr el cruce se ve que r06 CIERRA el bloque de las dos lineas y que
    «Primera actuación» no empieza hasta r07: una tabla de contenidos ahi
    ilustraria lo que todavia no se ha dicho, y dejaria sin imagen lo que si
    se acaba de decir.

    Ademas la cadena de las seis ya esta en el cierre: r38 las nombra una por
    una y dura 292 cuadros, que es la ranura mas larga de la pieza. Ponerla
    dos veces seria repetir la unica grafica que de verdad es el caso.

    Asi que r06 es `las_dos_lineas` -lo que la carpeta tiene de cada quien- y
    el recuento de las seis se queda donde la locucion lo pide.

LA SEGUNDA ES LA QUE HAY QUE MIRAR CON CUIDADO
    `lo_expuesto_y_lo_invocado` pone las seis actuaciones en dos columnas. La
    tentacion es llenar las doce casillas. Seria falso: en la cuarta y en la
    quinta NO HAY nada en la columna de la izquierda, porque sobre la medida
    de Ivan la Fiscalia no expuso y sobre la imputacion de Lina no describio.

    El hueco es el contenido. Un guion corto en esa casilla dice mas que
    cualquier frase, y es la misma asimetria que en el Caso 3 sostenia la
    fila de Teresa sin tachar.

Y LA TERCERA
    `las_tres_modificaciones` marca cual de las tres SI es una precision. Dos
    agregan hechos o imputacion nueva; una sola corrige una direccion sin
    cambiar el sitio ni la conducta. Tratarlas igual es el error, y la
    grafica lo dice separando la que si lo es.

NINGUNA CUESTA CREDITOS
    Se renderizan en local con PIL y ffmpeg, como las de los tres casos
    anteriores.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

W, H = 1920, 1080
FPS = "24000/1001"
OUT = "/home/claude/p3c4/graficas/out"

FONDO = C.AZUL_NOCHE
AMARILLO = (252, 197, 14)
AZUL = (8, 83, 159)
BLANCO = (255, 255, 255)
GRIS = (150, 156, 166)


def _escritor(salida):
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
    return lineas, ys


def _cabecera(d, lineas, ys, f):
    """Sin filete grande junto al titulo: Sebastian lo quito el 21 de oct."""
    for i, ((txt, font, sz, _, sg), y) in enumerate(zip(lineas, ys)):
        t = _t(f, 2 + i, 12 + i)
        if t <= 0.004:
            continue
        d.text((C.TEXT_X + sg, y + int(12 * (1 - t))), txt, font=font,
               fill=BLANCO + (int(255 * t),))


def _cerrar(p, salida, n):
    p.stdin.close()
    p.wait()
    print("%-46s %3d f  %5d KB" % (os.path.basename(salida), n,
                                   os.path.getsize(salida) // 1024))


# ------------------------------------------------------------------ r06
def las_dos_lineas(n=209, salida=None):
    """Lo que la carpeta tiene de cada quien, antes de la primera actuación."""
    salida = salida or "%s/P3C4_r06_graf_las_dos_lineas_v%d.mov" % (OUT, n)
    lineas, ys = _bloque({"ante": "La carpeta, antes de la primera actuación",
                          "titulo": "Dos líneas"}, 215, 1420)
    f_nom = C.fuente(C.F_BOLD, 46)
    f_it = C.fuente(C.F_MED, 31)
    XN, XI = 190, 470
    Y0, DY = 450, 230
    #  (nombre, acento, lo que la carpeta registra)
    FILAS = [
        ("Nora", AMARILLO, ["Captación de Inés y Alba mediante ofertas de trabajo",
                            "Recepción en un alojamiento",
                            "Entrevistas · conversaciones atribuidas · registros de viaje"]),
        ("Iván", AMARILLO, ["Coordinación de transporte interno al punto de salida",
                            "Instrucciones para evitar controles · cobro de comisiones",
                            "Pasajeros y regulación migratoria, ya individualizados"]),
    ]

    p = _escritor(salida)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")
        _cabecera(d, lineas, ys, f)

        for i, (nom, ac, items) in enumerate(FILAS):
            y = Y0 + i * DY
            t = _t(f, 26 + i * 34, 26 + i * 34 + 15)
            if t <= 0.004:
                continue
            dy = int(14 * (1 - t))
            d.rectangle([C.BAR_X, y + dy, C.BAR_X + 9, y + 60 + dy],
                        fill=ac + (int(255 * t),))
            d.text((XN, y + 6 + dy), nom, font=f_nom, fill=BLANCO + (int(255 * t),))
            for j, it in enumerate(items):
                tj = _t(f, 40 + i * 34 + j * 13, 40 + i * 34 + j * 13 + 14)
                if tj <= 0.004:
                    continue
                d.text((XI, y + 6 + j * 48 + int(10 * (1 - tj))), it, font=f_it,
                       fill=(BLANCO if j < 2 else GRIS) + (int(245 * tj),))

        # la sola frase que las junta, y que es lo que se oye encima
        t = _t(f, 150, 176)
        if t > 0.004:
            y = Y0 + 2 * DY - 10
            d.line([(C.BAR_X, y), (C.BAR_X + 1450, y)],
                   fill=GRIS + (int(110 * t),), width=2)
            d.text((C.TEXT_X - 73, y + 34 + int(12 * (1 - t))),
                   "Las dos están en la misma carpeta",
                   font=C.fuente(C.F_BOLD, 38), fill=GRIS + (int(240 * t),))

        p.stdin.write(im.tobytes())
    _cerrar(p, salida, n)


# ------------------------------------------------------------------ r36
def las_tres_modificaciones(n=205, salida=None):
    """Tres cambios al proyecto de acusación. Una sola es una precisión."""
    salida = salida or "%s/P3C4_r36_graf_tres_modificaciones_v%d.mov" % (OUT, n)
    lineas, ys = _bloque({"ante": "El proyecto de acusación de Iván",
                          "titulo": "Tres modificaciones"}, 215, 1420)
    f_it = C.fuente(C.F_BOLD, 38)
    f_pi = C.fuente(C.F_MED, 29)
    f_et = C.fuente(C.F_BOLD, 27)
    Y0, DY = 440, 180
    XE = 1760          # borde DERECHO de las etiquetas: las tres alineadas
    #  (que cambia, el detalle, etiqueta, es_precision)
    FILAS = [
        ("Dos viajes de junio", "Respecto de personas distintas",
         "Hecho nuevo", False),
        ("La dirección de la entrega", "Mismo sitio material, misma conducta",
         "Precisión", True),
        ("La agravación del numeral diez", "Coordinación por aplicación de mensajería",
         "Imputación nueva", False),
    ]

    p = _escritor(salida)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")
        _cabecera(d, lineas, ys, f)

        for i, (que, det, et, prec) in enumerate(FILAS):
            y = Y0 + i * DY
            t = _t(f, 24 + i * 20, 24 + i * 20 + 15)
            if t <= 0.004:
                continue
            dy = int(14 * (1 - t))
            d.rectangle([C.BAR_X, y + dy, C.BAR_X + 9, y + 78 + dy],
                        fill=(GRIS if prec else AMARILLO) + (int(255 * t),))
            d.text((C.TEXT_X, y + dy), que, font=f_it, fill=BLANCO + (int(255 * t),))
            d.text((C.TEXT_X, y + 50 + dy), det, font=f_pi,
                   fill=GRIS + (int(235 * t),))

            # la etiqueta entra DESPUES: primero las tres parecen iguales
            t2 = _t(f, 108 + i * 18, 108 + i * 18 + 16)
            if t2 <= 0.004:
                continue
            col = GRIS if prec else AMARILLO
            an = d.textlength(et, font=f_et)
            x = XE - an
            d.rectangle([x - 18, y + 4, x + an + 18, y + 44],
                        outline=col + (int(230 * t2),), width=2)
            d.text((x, y + 12 + int(8 * (1 - t2))), et, font=f_et,
                   fill=col + (int(255 * t2),))

        # y entonces se ve que solo una lo es
        t = _t(f, 168, 196)
        if t > 0.004:
            d.text((C.TEXT_X, Y0 + 3 * DY - 24 + int(12 * (1 - t))),
                   "Una sola de las tres es una precisión",
                   font=C.fuente(C.F_BOLD, 38), fill=BLANCO + (int(250 * t),))

        p.stdin.write(im.tobytes())
    _cerrar(p, salida, n)


# ------------------------------------------------------------------ r38
def lo_expuesto_y_lo_invocado(n=292, salida=None):
    """Las seis actuaciones, en dos columnas. Dos casillas quedan vacías."""
    salida = salida or "%s/P3C4_r38_graf_expuesto_invocado_v%d.mov" % (OUT, n)
    lineas, ys = _bloque({"ante": "Las seis actuaciones, una por una",
                          "titulo": "Lo que se sustentó · lo que se invocó"},
                         205, 1500)
    f_num = C.fuente(C.F_BOLD, 29)
    f_col = C.fuente(C.F_MED, 26)
    # La primera version puso el nombre de la actuacion en 182 y la columna
    # de sustento en 300: se pisaban. El nombre mas largo -«6 · Acusación de
    # Iván»- mide 330 a este cuerpo, asi que la columna empieza en 560.
    XN, XA, XD = 176, 556, 1210
    Y0, DY = 396, 90
    #  (nº y actuación, lo sustentado, lo invocado)
    FILAS = [
        ("1 · Solicitudes", "Una cuenta vinculada a cobros, seis meses",
         "Todas las cuentas familiares, cinco años"),
        ("2 · Capturas", "Orden vigente, hora real, derechos informados",
         "«Su nombre aparece en un informe»"),
        ("3 · Medida sobre Nora", "Inferencia desarrollada; fuga no demostrada",
         "La alarma social"),
        ("4 · Medida sobre Iván", None,
         "«Yo ya presenté la mía»"),
        ("5 · Imputación de Lina", None,
         "Una sola frase, sin episodios ni actos"),
        ("6 · Acusación de Iván", "El episodio de febrero, individualizado",
         "«Simples precisiones» · todo en una carpeta"),
    ]

    p = _escritor(salida)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")
        _cabecera(d, lineas, ys, f)

        # los dos encabezados de columna
        t = _t(f, 18, 38)
        if t > 0.004:
            fh = C.fuente(C.F_BOLD, 25)
            d.text((XA, Y0 - 54 + int(8 * (1 - t))), "CON QUÉ SUSTENTO",
                   font=fh, fill=GRIS + (int(210 * t),))
            d.text((XD, Y0 - 54 + int(8 * (1 - t))), "CON QUÉ SE INVOCÓ",
                   font=fh, fill=AMARILLO + (int(210 * t),))
            d.line([(XN, Y0 - 20), (1744, Y0 - 20)],
                   fill=GRIS + (int(90 * t),), width=2)

        for i, (nom, sus, inv) in enumerate(FILAS):
            y = Y0 + i * DY
            t = _t(f, 42 + i * 22, 42 + i * 22 + 15)
            if t <= 0.004:
                continue
            dy = int(12 * (1 - t))
            d.text((XN, y + dy), nom, font=f_num, fill=BLANCO + (int(250 * t),))
            if sus:
                d.text((XA, y + 1 + dy), sus, font=f_col,
                       fill=BLANCO + (int(235 * t),))
            else:
                # el hueco es el contenido: no se expuso nada
                d.line([(XA, y + 17 + dy), (XA + 34, y + 17 + dy)],
                       fill=GRIS + (int(170 * t),), width=3)

            t2 = _t(f, 60 + i * 22, 60 + i * 22 + 16)
            if t2 > 0.004:
                d.text((XD, y + 1 + int(10 * (1 - t2))), inv, font=f_col,
                       fill=AMARILLO + (int(245 * t2),))

        t = _t(f, 232, 266)
        if t > 0.004:
            y = Y0 + 6 * DY + 14
            d.line([(XN, y), (1744, y)], fill=GRIS + (int(90 * t),), width=2)
            d.text((XN, y + 28 + int(12 * (1 - t))),
                   "En dos de las seis, la columna de la izquierda está vacía",
                   font=C.fuente(C.F_BOLD, 33), fill=BLANCO + (int(250 * t),))

        p.stdin.write(im.tobytes())
    _cerrar(p, salida, n)


if __name__ == "__main__":
    las_dos_lineas()
    las_tres_modificaciones()
    lo_expuesto_y_lo_invocado()
