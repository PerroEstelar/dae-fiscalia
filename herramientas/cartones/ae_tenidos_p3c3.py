#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los cartones del Caso 3 «Ruta del Golfo», teñidos sobre cama.

HISTORICO: SUPERSEDIDO POR cartones_p3c3.py (21 de octubre de 2026).
    El pigmento de estos cartones es el de la plantilla, no el azul
    institucional medido del intro oficial. Correr este archivo vuelve a
    escribir los .mov con el azul viejo. Queda como registro.

TRES FAMILIAS EN UN SOLO ARCHIVO
    `ae`     nueve cartones de enunciado, uno por bisagra del caso
    `prop`   las tres propuestas equivocadas, LITERALES
    `cap`    las dos citas de las capturas

LAS TRES PROPUESTAS NO CAEN SOBRE UNA CARA
    Misma regla que el Caso 2, y por la misma razón: poner «cada giro
    constituye una operación independiente» encima del primer plano de Marta
    convierte en algo que a ella le pasa lo que en realidad el equipo propone.

    Van teñidas sobre camas del mundo institucional —la mesa del equipo en
    cenital, el informe y el esfero, la sala de reunión—, que es el motivo que
    el Caso 2 dejó construido: cada vez que aparece una mala propuesta, la
    pieza se va a la oficina y no a la ruta.

LAS DOS CITAS NO VAN DONDE SE CITAN
    El guion las tenía en el bloque de las capturas y ahí no caben: esa ranura
    mide 178 cuadros y ya lleva `ae02`. Sebastián decidió llevarlas al final,
    a la ranura de la conversación íntegra —205 cuadros, sin nada encima—,
    que es el momento en que la pieza las vuelve a mirar.

    Queda mejor que en su sitio original: se leen cuando se están
    reexaminando, no cuando todavía se daban por buenas.

NINGUNO CORRIGE
    El video no dice cuál es el error. Lo pone donde se vea.
"""
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_p3c3"
os.makedirs(OUT, exist_ok=True)

#  ✦ = propuesta equivocada: cama institucional, nunca una cara
#  (archivo, ranura, cuadros, spec)
TENIDOS = [
    ("ae01_progresiva", "r01", 202, {
        "suelta": "Información progresiva: la carpeta reúne fuentes de "
                  "distinto alcance, no un conjunto de hechos demostrados"}),

    ("ae02_no_identificada", "r07", 178, {
        "ante": "Todavía no",
        "titulo": "Se ha identificado qué disposición migratoria le era "
                  "aplicable a cada pasajero",
        "cuerpo": "en la fecha investigada"}),

    ("prop1_tres_peticiones", "r08", 237, {                      # ✦
        "ante": "El investigador propone",
        "cuerpo": "Interceptar todos los números asociados al alojamiento.\n"
                  "Solicitar la totalidad de la información bancaria de los "
                  "familiares de Marta durante 5 años.\n"
                  "Afirmar que cada giro constituye una operación "
                  "independiente."}),

    ("ae03_podian_salir", "r11", 257, {
        "ante": "Y a la vez",
        "titulo": "Todos podían salir a comprar",
        "cuerpo": "No están esclarecidos la duración del acuerdo, el abono "
                  "real del trabajo, ni la intervención de Luis en esas "
                  "condiciones"}),

    ("prop2_agregar_trata", "r12", 169, {                        # ✦
        "ante": "Un fiscal auxiliar propone",
        "titulo": "Agregar trata a todas las personas ya investigadas por "
                  "tráfico"}),

    ("ae04_materialmente", "r14", 228, {
        "ante": "El visado",
        "titulo": "Es materialmente auténtico",
        "cuerpo": "Luis sostiene que solo ayudaba a llenar formularios y que "
                  "el pago era una tarifa ordinaria"}),

    ("ae05_sin_relacion", "r17", 101, {
        "suelta": "La relación entre los dos episodios no está establecida"}),

    ("prop3_ignorar", "r21", 173, {                              # ✦
        "ante": "Un funcionario propone",
        "titulo": "Ignorar el documento de ingreso",
        "cuerpo": "porque la certificación inicial es oficial"}),

    ("ae06_no_atribuido", "r25", 174, {
        "ante": "Un mensaje posterior",
        "titulo": "Podría mostrar una instrucción de entrega a un guía",
        "cuerpo": "Todavía no se ha atribuido a su teléfono"}),

    ("cap01_viernes", "r26", 102, {
        "ante": "Dos de los fragmentos",
        "titulo": "«se entregan el viernes»"}),

    ("cap02_saldo", "r26", 103, {
        "titulo": "«el saldo queda allá»"}),

    ("ae07_si_describen", "r27", 184, {
        "ante": "La conversación íntegra",
        "titulo": "Un fragmento se refería a entrega de equipaje",
        "cuerpo": "Otros mensajes sí describen la coordinación de una ruta "
                  "sin controles"}),

    ("ae08_sin_cierre", "r28", 201, {
        "ante": "La contabilidad de Teresa",
        "titulo": "Registra deuda sin cierre y cargos que no disminuyen pese "
                  "al trabajo",
        "cuerpo": "Ese dato todavía debe contrastarse con las personas "
                  "alojadas"}),

    ("ae09_sin_inercia", "r31", 153, {
        "ante": "Revisar el programa",
        "titulo": "Sin perder esas fuentes y sin extender autorizaciones por "
                  "comodidad",
        "cuerpo": "Y sin conservar, por inercia, la atribución inicial a "
                  "todos los proveedores"}),
]

if __name__ == "__main__":
    for nom, r, fr, spec in TENIDOS:
        C.render_carton(spec, fr, None, True,
                        "%s/P3C3_%s.mov" % (OUT, nom), con_tinte=True)
        print("%-24s %-5s %4d cuadros" % (nom, r, fr))
