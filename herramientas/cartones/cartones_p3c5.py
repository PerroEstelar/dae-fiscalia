#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los cartones del PRIORIDAD 03 · Caso 5 «Voces, registros y cuentas».

DIECISIETE, Y NINGUNO SOBRE UNA CARA
    Once de afirmacion y seis de narracion, mas la cita del cuaderno. Las
    placas con rostro son r03, r05, r21, r23, r27, r28 y r32, y ninguna lleva
    carton: poner «Tomas debe explicar el dinero para evitar la condena»
    encima del primer plano de Tomas convierte en algo que a el le pasa lo que
    en realidad el fiscal dice.

LAS AFIRMACIONES VAN LITERALES, Y DOS DE ELLAS LAS HACE LA DEFENSA
    r31 -«quien regresa voluntariamente a un alojamiento nunca puede estar
    sometido»- y r41 -«la ausencia de encierro y el pago parcial excluyen
    cualquier trata»-. Van en la misma retorica neutra que las de la
    Fiscalia: el caso no es un reparto de buenos y malos.

DOS AFIRMACIONES COMPARTEN RANURA
    «Cuatro informes equivalen a cuatro corroboraciones» y «Tomas debe
    explicar el dinero» caen las dos dentro de b18 y sobre la misma ranura
    medida. Van juntas en un carton de dos vinetas, que es lo que el Caso 4
    hizo con la propuesta de las cuentas. Separarlas obligaria a partir una
    ranura que la voz no parte.

EL CARTON DE r07 ES EL QUE SOSTIENE EL FINAL
    «No se acusa a Oscar por captar a una tercera mujer» se lee en el minuto
    uno y se cobra en el minuto seis, cuando el alegato pide condenar por ese
    episodio. Sin ese carton al principio, el error del final no se ve: se
    oye una frase mas.

LA CITA DEL CUADERNO
    Tres palabras: abono, multa por salir, falta. Son lo unico concreto que el
    documento da de su contenido, y la discusion de pertinencia es sobre ellas.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

AZUL_FGN = (0, 72, 144)          # #004890, medido del intro oficial
C.TINTE = AZUL_FGN

# EL AMARILLO ES EL DE LA SERIE, NO UNO PARECIDO
#     Estaba en (252, 197, 14) y la barra de `render_carton` -C.BAR_C-
#     esta en (252, 181, 0). Son dos amarillos distintos dentro de la
#     misma pieza: en r39 la vineta quedaba 16 niveles mas verde que el
#     filete del carton anterior. Se toma del modulo para que no vuelva
#     a separarse.
AMARILLO = C.BAR_C[:3]
BLANCO = (255, 255, 255)
GRIS = (168, 174, 184)

OUT = "/home/claude/p3c5/cartones/out"
os.makedirs(OUT, exist_ok=True)


def _escritor(salida):
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    return subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "argb",
         "-s", "%dx%d" % (C.W, C.H), "-r", C.FPS, "-i", "-",
         "-c:v", "qtrle", "-pix_fmt", "argb", salida], stdin=subprocess.PIPE)


def _t(f, a, b):
    if f <= a:
        return 0.0
    if f >= b:
        return 1.0
    x = (f - a) / float(b - a)
    return x * x * (3 - 2 * x)


def _tinte(f, n):
    """La misma rampa de azul que `render_carton(con_tinte=True)`."""
    if f < C.TINTE_IN:
        ta = C.TINTE_A * C.ease_out(f / float(C.TINTE_IN))
    elif f >= n - C.TINTE_OUT:
        ta = C.TINTE_A * (1 - (f - (n - C.TINTE_OUT)) / float(C.TINTE_OUT))
    else:
        ta = C.TINTE_A
    return Image.new("RGBA", (C.W, C.H), C.TINTE + (int(ta),))


def _escribir(p, im):
    """ARGB, y en ESE orden.

    EL ERROR QUE ESTO ARREGLA
        `im.tobytes()` de una RGBA entrega R,G,B,A. El flujo esta declarado
        `-pix_fmt argb`, que espera A,R,G,B. Cada pixel sale corrido un
        canal: el blanco (255,255,255,245) sobrevive casi intacto y por eso
        el texto parecia bien, pero el filete amarillo (252,197,14,255) se
        leia como (197,14,255) -magenta-. `render_carton` ya hacia la
        permutacion; estas dos funciones, escritas aparte, no.
    """
    r, g, b, al = im.split()
    p.stdin.write(Image.merge("RGBA", (al, r, g, b)).tobytes())


def lista_vinetas(ante, puntos, n, salida, y0=420, dy=170):
    """Dos o tres afirmaciones en una sola ranura, cada una con su filete."""
    f_ante = C.fuente(C.F_SEMI, 30)
    f_pt = C.fuente(C.F_MED, 44)
    p = _escritor(salida)
    for f in range(n):
        im = _tinte(f, n)
        d = ImageDraw.Draw(im)
        t = _t(f, 0, 14)
        if t > 0.004:
            d.text((C.TEXT_X, 330), ante, font=f_ante,
                   fill=BLANCO + (int(235 * t),))
        for i, txt in enumerate(puntos):
            t2 = _t(f, 18 + i * 16, 42 + i * 16)
            if t2 <= 0.004:
                continue
            y = y0 + i * dy
            d.rectangle([C.BAR_X, y + 6, C.BAR_X + 10, y + 56],
                        fill=AMARILLO + (int(255 * t2),))
            for k, linea in enumerate(txt.split("\n")):
                d.text((C.TEXT_X, y + k * 58 + int(10 * (1 - t2))), linea,
                       font=f_pt, fill=BLANCO + (int(245 * t2),))
        _escribir(p, im)
    p.stdin.close()
    p.wait()
    print("%-28s %4d f" % (os.path.basename(salida), n))


def cita(texto, n, salida, y0=430):
    """Un verbatim: sin antetitulo, sin filete, entre comillas angulares."""
    f_c = C.fuente(C.F_BOLD, 54)
    p = _escritor(salida)
    lineas = texto.split("\n")
    for f in range(n):
        im = _tinte(f, n)
        d = ImageDraw.Draw(im)
        for i, linea in enumerate(lineas):
            t = _t(f, 8 + i * 10, 34 + i * 10)
            if t <= 0.004:
                continue
            d.text((C.TEXT_X, y0 + i * 72 + int(12 * (1 - t))), linea,
                   font=f_c, fill=BLANCO + (int(248 * t),))
        _escribir(p, im)
    p.stdin.close()
    p.wait()
    print("%-28s %4d f" % (os.path.basename(salida), n))


#  (archivo, ranura, cuadros, spec)   — el largo es el de la ranura medida
TENIDOS = [
    # LOS DOS DE APERTURA. Anadidos el 23 oct 2026: la pieza corria 57,6 s
    # sin un solo carton, contra los 12,6 a 14,2 s de las otras cuatro. Los
    # textos son la primera y la tercera frase del encabezado del documento
    # del profesor, que ningun carton decia. Cada uno sobre su imagen: la
    # tesis sobre las dos bandejas vacias de r01, el alcance sobre la sala
    # vacia de r02. El de r01 va corto -dos lineas y el separador de ae02 y
    # ae03- porque 167 cuadros son 7,0 s y en tres lineas no se lee.
    ("ae00_medio_ofrecido", "r01", 167, {
        "ante": "El punto de partida",
        "titulo": "El medio ofrecido · la información admitida y practicada"}),

    ("ae07_alcance", "r02", 300, {
        "ante": "El alcance del ejercicio",
        "titulo": "Las decisiones evaluadas se limitan a los hechos y "
                  "condiciones expresamente suministrados"}),

    ("ae01_individualizan", "r06", 117, {
        "ante": "La acusación",
        "titulo": "Individualiza episodios, sujetos y elementos"}),

    ("ae02_no_se_acusa", "r07", 189, {
        "ante": "Y queda fuera de la acusación",
        "titulo": "Captar a una tercera mujer · pertenecer a una organización",
        "cuerpo": "Ni a Óscar lo uno, ni a Tomás lo otro"}),

    ("prop1_informe", "r11", 159, {
        "ante": "La Fiscalía pide",
        "titulo": "El informe con todos sus anexos, como una sola petición",
        "cuerpo": "Sin funciones diferenciadas"}),

    ("ae03_andres", "r13", 197, {
        "ante": "El informe mezcla",
        "titulo": "Lo que Andrés percibió · lo que recibió de otra funcionaria",
        "cuerpo": "La habitación la vio él. El teléfono se lo entregaron"}),

    ("prop3_estipulacion", "r19", 198, {
        "ante": "La Fiscalía pretende añadir",
        "titulo": "Que todos los movimientos de la cuenta corresponden a "
                  "comisiones de tráfico",
        "cuerpo": "La estipulación comprendió la titularidad"}),

    ("prop4_interceptaciones", "r20", 167, {
        "ante": "La Fiscalía pide",
        "titulo": "Todas las interceptaciones de una línea durante seis meses",
        "cuerpo": "Sin precisar sesiones ni contenido"}),

    ("ae04_voz_sin_dueno", "r22", 131, {
        "ante": "La otra voz",
        "titulo": "Aún no se ha establecido quién es ni a qué se refiere"}),

    ("prop5_renata", "r24", 203, {
        "ante": "La Fiscalía sostiene",
        "titulo": "Que la migración vuelve imposible su comparecencia",
        "cuerpo": "Renata mantiene contacto y acepta declarar"}),

    ("prop6_credibilidad", "r25", 293, {
        "ante": "La psicóloga ofrece declarar",
        "titulo": "Que ambas mujeres son creíbles porque sus relatos coinciden "
                  "con un perfil de víctima de trata",
        "cuerpo": "Además de explicar las afectaciones que observó"}),

    ("ae05_grafica", "r26", 296, {
        "ante": "El análisis financiero",
        "titulo": "No separa remesas, gastos y comisiones",
        "cuerpo": "Los extractos sí se descubrieron a tiempo"}),

    ("prop7_regresa", "r31", 181, {
        "ante": "Una pregunta de la defensa afirma",
        "titulo": "Que quien regresa voluntariamente a un alojamiento nunca "
                  "puede estar sometido"}),

    ("ae06_acta", "r34", 152, {
        "ante": "El acta firmada",
        "titulo": "No se utiliza como confesión"}),

    ("prop10_tercera", "r40", 214, {
        "ante": "La Fiscalía pide condenar además",
        "titulo": "Por un episodio mencionado por primera vez en el juicio",
        "cuerpo": "Y que la acusación dejó fuera"}),

    ("prop11_sin_encierro", "r41", 195, {
        "ante": "La defensa sostiene",
        "titulo": "Que la ausencia de encierro y el pago parcial excluyen "
                  "cualquier trata"}),
]

if __name__ == "__main__":
    for nom, r, fr, spec in TENIDOS:
        C.render_carton(spec, fr, None, True, "%s/P3C5_%s.mov" % (OUT, nom),
                        con_tinte=True)
        print("%-28s %-5s %4d f" % (nom, r, fr))

    # las dos afirmaciones del alegato que comparten ranura
    lista_vinetas(
        "En el alegato, la Fiscalía sostiene",
        ["Que cuatro informes que reproducen las entrevistas\nequivalen a cuatro corroboraciones independientes.",
         "Que Tomás debe explicar el dinero para evitar\nla condena."],
        253, "%s/P3C5_prop8y9_alegato.mov" % OUT, y0=400, dy=180)        # r39

    # la sustentacion de la pertinencia: el verbatim central
    cita("«Es pertinente porque fue hallado en el\n"
         "inmueble donde ocurrieron los hechos\n"
         "y se refiere a las víctimas»",
         228, "%s/P3C5_cita01_pertinencia.mov" % OUT)                    # r17

    # las tres anotaciones del cuaderno
    cita("«abono»   ·   «multa por salir»   ·   «falta»",
         113, "%s/P3C5_cita02_cuaderno.mov" % OUT, y0=500)               # r15
