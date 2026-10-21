#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del PRIORIDAD 03 · Caso 3 «Ruta del Golfo».

EL PIGMENTO SALE DEL INTRO OFICIAL, NO DE LA PLANTILLA
    En la revision del 21 de octubre Sebastian marco que el fondo de los
    cartones *"no es el azul institucional y tiene un ligero gradiente"*.
    Tenia razon en las dos cosas, y son dos cosas distintas:

    EL PIGMENTO.  Medido sobre `FGN_intro_version7.mp4`, que es el intro
        oficial y por tanto la referencia de marca que la pieza ya lleva
        dentro, la Fiscalia usa #004890 como azul institucional y #002048
        como azul noche. La plantilla de la casa (`cartones_ta.TINTE`) trae
        #03398B, heredado del Caso A: esta cerca, pero no es. Aqui se
        sobreescribe en tiempo de render -`AZUL_FGN`- y SOLO para este caso,
        para no mover la plantilla que usan los demas cursos.

    EL GRADIENTE.  No lo dibuja el carton: es la placa transparentandose. Con
        la tinta al 46 % el cuadro compuesto va de (94,119,158) arriba a
        (18,43,81) abajo, 76 niveles medidos. Subir la tinta al 88 % lo
        bajaria a 17, pero rompe el emparejado con los Casos 1 y 2 ya
        aprobados. Se deja en 46 % a proposito y queda anotado por si algun
        dia se actualizan los tres a la vez.

DOS FORMAS QUE LA PLANTILLA NO SABE DIBUJAR
    `lista_acentos`  filas de nombre + dato, cada una con el filete de SU
                     acento. Es la gramatica de color de la serie aplicada a
                     un carton: amarillo lo que el enunciado da por
                     establecido de Luis, Marta y Omar; azul lo de Teresa.
    `lista_vinetas`  un filete amarillo por item. Sebastian lo pidio para las
                     tres peticiones de la propuesta 1: eran tres frases en un
                     bloque corrido y se leian como una sola.

EL CARTON DE LOS CUATRO EXISTE PORQUE LA LOCUCION LOS NOMBRA SEGUIDOS
    En doce segundos suenan Luis, Marta, Omar y Teresa, uno detras de otro.
    Sin nada en pantalla el espectador no alcanza a separarlos y la pieza
    arranca confusa -Sebastian lo marco como *"un poco engañoso"* en el minuto
    0:38-. El carton va TEÑIDO Y TRANSPARENTE sobre el plano de los cuatro de
    espaldas, que es el plano que les corresponde.

    Resuelve ademas lo de Marta: es la unica de los cinco sin primer plano
    propio, porque el guion no le da una frase sola donde quepa. Aqui su
    nombre y su dato aparecen igual que los de los otros tres.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

AZUL_FGN = (0, 72, 144)          # #004890, medido del intro oficial
AZUL_NOCHE_FGN = (0, 32, 72)     # #002048, por si hace falta el fondo cerrado
C.TINTE = AZUL_FGN

AMARILLO = (252, 197, 14)
AZUL = (8, 83, 159)
BLANCO = (255, 255, 255)
GRIS = (168, 174, 184)

OUT = "/mnt/user-data/outputs/cartones_p3c3"
os.makedirs(OUT, exist_ok=True)


def _escritor(salida, n):
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
    p = _escritor(salida, n)
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
    print("%-34s %4d f  %5d KB" % (os.path.basename(salida), n,
                                   os.path.getsize(salida) // 1024))


def lista_acentos(titulo, filas, n, salida, y0=350, dy=140):
    """filas: [(nombre, acento, dato)]"""
    f_tit = C.fuente(C.F_SEMI, 34)
    f_nom = C.fuente(C.F_BOLD, 46)
    f_dat = C.fuente(C.F_MED, 30)

    def pintar(d, f, n):
        t = _t(f, 2, 12)
        if t > 0.004:
            d.text((C.TEXT_X, y0 - 86 + int(12 * (1 - t))), titulo, font=f_tit,
                   fill=GRIS + (int(240 * t),))
        for i, (nom, ac, dato) in enumerate(filas):
            a = _t(f, 14 + i * 14, 14 + i * 14 + 12)
            o = _t(f, n - C.TXT_OUT, n)
            a = min(a, 1 - o)
            if a <= 0.004:
                continue
            y = y0 + i * dy + int(12 * (1 - a))
            d.rectangle([C.BAR_X, y + 4, C.BAR_X + 10, y + 56],
                        fill=ac + (int(255 * a),))
            d.text((C.TEXT_X, y), nom, font=f_nom, fill=BLANCO + (int(255 * a),))
            d.text((C.TEXT_X, y + 60), dato, font=f_dat,
                   fill=GRIS + (int(238 * a),))
    _render(n, salida, pintar)


def lista_vinetas(ante, items, n, salida, y0=380, dy=132):
    f_ant = C.fuente(C.F_SEMI, 34)
    f_it = C.fuente(C.F_MED, 36)

    def pintar(d, f, n):
        t = _t(f, 2, 12)
        if t > 0.004:
            d.text((C.TEXT_X, y0 - 86 + int(12 * (1 - t))), ante, font=f_ant,
                   fill=GRIS + (int(240 * t),))
        for i, it in enumerate(items):
            a = _t(f, 14 + i * 16, 14 + i * 16 + 12)
            o = _t(f, n - C.TXT_OUT, n)
            a = min(a, 1 - o)
            if a <= 0.004:
                continue
            y = y0 + i * dy + int(12 * (1 - a))
            d.rectangle([C.BAR_X, y + 6, C.BAR_X + 10, y + 50],
                        fill=AMARILLO + (int(255 * a),))
            for j, ren in enumerate(it.split("\n")):
                d.text((C.TEXT_X, y + j * 42), ren, font=f_it,
                       fill=BLANCO + (int(255 * a),))
    _render(n, salida, pintar)


TENIDOS = [
 ("ae01_progresiva", 202, {
  "suelta": "Información progresiva: la carpeta reúne fuentes de distinto "
            "alcance, no un conjunto de hechos demostrados"}),
 ("ae02_no_identificada", 178, {
  "ante": "Todavía no",
  "titulo": "Se ha identificado qué disposición migratoria le era aplicable a cada pasajero",
  "cuerpo": "en la fecha investigada"}),
 ("ae03_podian_salir", 257, {
  "ante": "Y a la vez",
  "titulo": "Todos podían salir a comprar",
  "cuerpo": "No están esclarecidos la duración del acuerdo, el abono real del "
            "trabajo, ni la intervención de Luis en esas condiciones"}),
 ("prop2_agregar_trata", 169, {
  "ante": "Un fiscal auxiliar propone",
  "titulo": "Agregar trata a todas las personas ya investigadas por tráfico"}),
 ("ae04_materialmente", 228, {
  "ante": "El visado",
  "titulo": "Es materialmente auténtico",
  "cuerpo": "Luis sostiene que solo ayudaba a llenar formularios y que el pago "
            "era una tarifa ordinaria"}),
 ("ae05_sin_relacion", 101, {
  "suelta": "La relación entre los dos episodios no está establecida"}),
 ("ae10_un_puesto", 170, {
  "ante": "La primera respuesta migratoria",
  "titulo": "Consultó únicamente un puesto de control, y un intervalo de quince días"}),
 ("ae11_dos_meses", 197, {
  "ante": "El informe la presenta",
  "titulo": "Como prueba de que las cuatro personas ingresaron clandestinamente",
  "cuerpo": "durante los dos meses anteriores"}),
 ("prop3_ignorar", 173, {
  "ante": "Un funcionario propone",
  "titulo": "Ignorar el documento de ingreso",
  "cuerpo": "porque la certificación inicial es oficial"}),
 ("ae06_no_atribuido", 174, {
  "ante": "Un mensaje posterior",
  "titulo": "Podría mostrar una instrucción de entrega a un guía",
  "cuerpo": "Todavía no se ha atribuido a su teléfono"}),
 ("cap01_viernes", 87, {
  "ante": "Dos de los fragmentos",
  "titulo": "«se entregan el viernes»"}),
 ("ae07_si_describen", 122, {
  "ante": "Otros mensajes",
  "titulo": "Sí describen la coordinación de una ruta sin controles"}),
 ("ae08_sin_cierre", 201, {
  "ante": "La contabilidad de Teresa",
  "titulo": "Registra deuda sin cierre y cargos que no disminuyen pese al trabajo",
  "cuerpo": "Ese dato todavía debe contrastarse con las personas alojadas"}),
 ("ae09_sin_inercia", 153, {
  "ante": "Revisar el programa",
  "titulo": "Sin perder esas fuentes y sin extender autorizaciones por comodidad",
  "cuerpo": "Y sin conservar, por inercia, la atribución inicial a todos los proveedores"}),
]

if __name__ == "__main__":
    for nom, fr, spec in TENIDOS:
        C.render_carton(spec, fr, None, True, "%s/P3C3_%s.mov" % (OUT, nom),
                        con_tinte=True)
        print("%-30s %4d f" % (nom, fr))
    lista_acentos(
        "Cuatro proveedores",
        [("Luis",   AMARILLO, "Aparece como usuario de la cuenta Enlace Norte"),
         ("Marta",  AMARILLO, "Recibe 5 giros en una cuenta bancaria a su nombre"),
         ("Omar",   AMARILLO, "Conduce el vehículo que lleva al grupo"),
         ("Teresa", AZUL, "Administra el alojamiento donde se quedan")],
        303, "%s/P3C3_ae00_los_cuatro.mov" % OUT, y0=320, dy=152)
    lista_vinetas(
        "El investigador propone",
        ["Interceptar todos los números asociados al alojamiento.",
         "Solicitar la totalidad de la información bancaria\nde los familiares de Marta durante 5 años.",
         "Afirmar que cada giro constituye una operación independiente."],
        237, "%s/P3C3_prop1_tres_peticiones.mov" % OUT, y0=360, dy=140)
