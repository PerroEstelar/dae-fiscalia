#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del PRIORIDAD 03 · Caso 4 «Puerto de salida».

EL PIGMENTO, COMO EN EL CASO 3
    `AZUL_FGN` = #004890, medido sobre `FGN_intro_version7.mp4`, que es el
    intro oficial y por tanto la referencia de marca que la pieza ya lleva
    dentro. La plantilla de la casa trae #03398B, heredado del Caso A: esta
    cerca, pero no es. Se sobreescribe en tiempo de render y solo para este
    caso.

SIETE PROPUESTAS, Y NINGUNA CAE SOBRE UNA CARA
    Es la regla de la serie, y aqui pesa mas que nunca: seis de las siete
    decisiones que la pieza expone son equivocadas y LA CUARTA LA TOMA UNA
    JUEZA. Las siete van sobre arquitectura, mobiliario y manos -el estrado
    vacio, el microfono apartado, la silla de la defensa, la mesa en cenital-
    y nunca sobre uno de los seis planos que si llevan rostro.

    Comprobado contra `escenas.py`: ninguna de las ranuras con carton de
    propuesta -r08, r10, r15, r20, r24, r29- esta en la lista de las seis con
    rostro -r02, r05, r13, r19, r22, r25-.

LA SEPTIMA NO LLEVA CARTON, Y ES A PROPOSITO
    «El equipo trata las tres modificaciones como simples precisiones» se oye
    en r35 y r36, y r36 YA ES la grafica que desarma esa frase: tres filas,
    tres etiquetas, una sola precision. Poner ademas el carton seria decir dos
    veces lo mismo y tapar la grafica justo cuando entra. El carton de r37
    recoge en cambio lo que la grafica no dice: el rotulo de la carpeta.

EL VERBATIM VA ENTERO Y SIN TOCAR
    La imputacion de Lina es el unico texto literal de la pieza, y va en
    carton ademas de en voz. Parafrasearla contestaria la pregunta antes de
    hacerla: lo que se discute es justamente si esa frase individualiza algo.
    Por eso r26 lleva la frase sola, con comillas angulares, y r27 lleva lo
    que le falta.

LAS DOS FORMAS HEREDADAS DEL CASO 3
    `lista_vinetas` -un filete amarillo por item- para la propuesta de las
    cuentas, que son dos peticiones en una sola frase y se leian como una.
    `cita` -la frase sola, grande, sin ante ni cuerpo- para el verbatim y
    para el rotulo de la carpeta.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

AZUL_FGN = (0, 72, 144)          # #004890, medido del intro oficial
C.TINTE = AZUL_FGN

AMARILLO = (252, 197, 14)
AZUL = (8, 83, 159)
BLANCO = (255, 255, 255)
GRIS = (168, 174, 184)

OUT = "/home/claude/p3c4/cartones/out"
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
    return C.ease_out_cubic((f - a) / float(b - a))


def _tinte(n, f):
    if f < C.TINTE_IN:
        return C.TINTE_A * C.ease_out(f / C.TINTE_IN)
    if f >= n - C.TINTE_OUT:
        return C.TINTE_A * (1 - (f - (n - C.TINTE_OUT)) / C.TINTE_OUT)
    return C.TINTE_A


def _render(n, salida, pintar):
    p = _escritor(salida)
    for f in range(n):
        base = Image.new("RGBA", (C.W, C.H), (0, 0, 0, 0))
        base = Image.alpha_composite(
            base, Image.new("RGBA", (C.W, C.H), C.TINTE + (int(_tinte(n, f)),)))
        cap = Image.new("RGBA", (C.W, C.H), (0, 0, 0, 0))
        pintar(ImageDraw.Draw(cap), f, n)
        out = Image.alpha_composite(base, cap).convert("RGBA")
        a = out.getchannel("A")
        p.stdin.write(Image.merge("RGBA", (a,) + out.convert("RGB").split()).tobytes())
    p.stdin.close()
    p.wait()
    print("%-38s %4d f  %5d KB" % (os.path.basename(salida), n,
                                   os.path.getsize(salida) // 1024))


def lista_vinetas(ante, items, n, salida, y0=380, dy=132):
    f_ant = C.fuente(C.F_SEMI, 34)
    f_it = C.fuente(C.F_MED, 36)

    def pintar(d, f, n):
        t = _t(f, 2, 12)
        if t > 0.004:
            d.text((C.TEXT_X, y0 - 86 + int(12 * (1 - t))), ante, font=f_ant,
                   fill=GRIS + (int(240 * t),))
        for i, it in enumerate(items):
            a = min(_t(f, 14 + i * 16, 14 + i * 16 + 12), 1 - _t(f, n - C.TXT_OUT, n))
            if a <= 0.004:
                continue
            y = y0 + i * dy + int(12 * (1 - a))
            d.rectangle([C.BAR_X, y + 6, C.BAR_X + 10, y + 50],
                        fill=AMARILLO + (int(255 * a),))
            for j, ren in enumerate(it.split("\n")):
                d.text((C.TEXT_X, y + j * 42), ren, font=f_it,
                       fill=BLANCO + (int(255 * a),))
    _render(n, salida, pintar)


def cita(frase, n, salida, pie=None, cuerpo=52, y0=420):
    """La frase sola, sin ante. Para el verbatim y para el rotulo."""
    f_fr = C.fuente(C.F_BOLD, cuerpo)
    f_pi = C.fuente(C.F_MED, 30)

    def pintar(d, f, n):
        o = 1 - _t(f, n - C.TXT_OUT, n)
        renglones = frase.split("\n")
        for j, ren in enumerate(renglones):
            a = min(_t(f, 6 + j * 9, 6 + j * 9 + 14), o)
            if a <= 0.004:
                continue
            y = y0 + j * int(cuerpo * 1.42) + int(12 * (1 - a))
            d.text((C.TEXT_X, y), ren, font=f_fr, fill=BLANCO + (int(255 * a),))
        if pie:
            a = min(_t(f, 20 + len(renglones) * 9, 20 + len(renglones) * 9 + 16), o)
            if a > 0.004:
                y = y0 + len(renglones) * int(cuerpo * 1.42) + 34
                d.text((C.TEXT_X, y + int(10 * (1 - a))), pie, font=f_pi,
                       fill=GRIS + (int(238 * a),))
    _render(n, salida, pintar)


#  (nombre, ranura, cuadros de la ranura, spec)
#  ✦ = propuesta o decision equivocada: nunca sobre una cara
TENIDOS = [
    ("ae01_preliminares", "r01", 240, {
        "suelta": "Las calificaciones preliminares no convierten en demostrados "
                  "los hechos que se debaten"}),
    ("ae02_seis_meses", "r07", 285, {
        "ante": "Primera actuación",
        "titulo": "Una cuenta vinculada con cobros de la ruta",
        "cuerpo": "El fiscal propone pedir autorización por seis meses"}),
    ("prop2_registro", "r10", 234, {                                    # ✦
        "ante": "El fiscal pretende",
        "titulo": "Ordenar el registro de ese segundo inmueble invocando la "
                  "gravedad de la trata",
        "cuerpo": "Sin otra información que lo conecte con el delito"}),
    ("ae03_sin_actos", "r14", 167, {
        "ante": "Del recepcionista",
        "titulo": "No se describen actos delictivos que estuviera realizando",
        "cuerpo": "Ni una hipótesis concreta de participación"}),
    ("prop3_permanente", "r15", 167, {                                  # ✦
        "ante": "El investigador propone",
        "titulo": "Fundar la legalización únicamente en que la trata puede ser "
                  "permanente"}),
    ("ae04_no_demostrada", "r18", 102, {
        "suelta": "Reconoce que no ha demostrado fuga ni obstrucción"}),
    ("prop4_jueza", "r20", 237, {                                       # ✦
        "ante": "La jueza",
        "titulo": "Impone detención intramural por la alarma social que genera "
                  "el delito",
        "cuerpo": "Y estima que la domiciliaria solo puede existir como sustituto"}),
    ("ae05_sin_anuncio", "r21", 131, {
        "suelta": "No anuncia previamente un posible apartamiento, ni permite "
                  "discutirlo"}),
    ("ae06_mensajes_nuevos", "r23", 300, {
        "ante": "La representante aporta",
        "titulo": "Mensajes nuevos, atribuidos a Iván, con amenazas posteriores "
                  "a la denuncia",
        "cuerpo": "Y solicita una cautela privativa por protección"}),
    ("prop5_no_se_oye", "r24", 294, {                                   # ✦
        "ante": "El fiscal sostiene",
        "titulo": "Que esa petición no puede oírse, porque él ya presentó la suya",
        "cuerpo": "La defensa pide conocer los mensajes antes de la decisión"}),
    ("ae07_no_individualiza", "r27", 289, {
        "ante": "Se cita el artículo 188 A",
        "titulo": "Pero no se individualizan víctimas, episodios, actos ni finalidad",
        "cuerpo": "Ni el aprovechamiento que la norma exige"}),
    ("prop6_silencio", "r29", 118, {                                    # ✦
        "ante": "Otra fiscal considera",
        "titulo": "Que el silencio previo de la defensa sana el defecto"}),
    ("ae08_individualizadas", "r31", 113, {
        "suelta": "Con conducta, irregularidad y finalidad individualizadas"}),
]

if __name__ == "__main__":
    for nom, r, fr, spec in TENIDOS:
        C.render_carton(spec, fr, None, True, "%s/P3C4_%s.mov" % (OUT, nom),
                        con_tinte=True)
        print("%-24s %-5s %4d f" % (nom, r, fr))

    # la propuesta 1: dos peticiones en una sola frase, separadas
    lista_vinetas(
        "El investigador sugiere",
        ["Incluir todas las cuentas de los familiares de Iván\ndurante cinco años.",
         "Porque, dice, las redes suelen usar terceros."],
        260, "%s/P3C4_prop1_cuentas.mov" % OUT, y0=400, dy=150)          # r08 ✦

    # el verbatim, entero y sin tocar
    cita("«Durante 2024 y 2025 usted captó, trasladó\n"
         "y acogió a varias mujeres con fines de\n"
         "explotación sexual en esta ciudad»",
         232, "%s/P3C4_cita01_imputacion_lina.mov" % OUT,
         pie="La imputación, completa", cuerpo=50, y0=380)               # r26

    # el rotulo de la carpeta
    cita("«Informe de policía judicial y anexos»",
         145, "%s/P3C4_cita02_informe_anexos.mov" % OUT,
         pie="Sin índice, y sin separación de entrevistas, registros y extracciones",
         cuerpo=54, y0=460)                                              # r37
