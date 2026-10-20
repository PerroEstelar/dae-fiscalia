#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los cartones `ae` del Caso 2, teñidos sobre cama.

DE CATORCE LOSAS BLANCAS A ONCE CARTONES Y DOS GRÁFICAS
    Este caso tenía la mitad de sus ranuras en blanco —catorce de veintiocho—,
    con tramos de dos y tres seguidas. Se reparten así:

        dos pasan a GRÁFICA DE MOTION      `graficas_p3c2.py`
            ae02, la fila de seis que se abre en 2 y 4
            ae13, las cinco decisiones renglón a renglón
        uno pasa a LOWER THIRD             `lowerthirds_p3c2.py`
            ae09, que es Elisa y su edad: un nombre con un dato corto
        once quedan como CARTÓN TEÑIDO sobre una cama que corre en V1

LAS CUATRO PROPUESTAS, Y POR QUÉ CAMBIAN DE FONDO
    `ae05`, `ae07`, `ae08` y `ae11` son las propuestas equivocadas que el caso
    cita literales. La regla original era que no cayeran nunca sobre una cara,
    para no atribuirle a la persona en cuadro lo que propone otro, y por eso
    estaban en blanco.

    Siguen sin caer sobre una cara. Ahora van teñidas sobre camas del mundo
    INSTITUCIONAL —la mesa del equipo en cenital, el informe y el esfero, el
    pasillo, la sala de entrevista— y eso cumple la regla igual y además hace
    un motivo: cada vez que aparece una mala propuesta, la pieza se va a la
    oficina y no al taller. El blanco aislaba; la cama sitúa.
"""
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_p3c2"
os.makedirs(OUT, exist_ok=True)

#  ✦ = propuesta equivocada: cama institucional, nunca una cara
TENIDOS = [
    ("ae01_primer_contacto", "r01", 165, {
        "suelta": "La información es la del primer contacto. No se tiene por "
                  "demostrada la responsabilidad de nadie"}),
    ("ae03_pasaporte", "r07", 180, {
        "ante": "Mara",
        "titulo": "Afirma que Saúl conserva su pasaporte",
        "cuerpo": "Y que divulgará imágenes privadas si se va"}),
    ("ae04_pide", "r10", 185, {
        "ante": "Mara pide",
        "titulo": "Alojamiento y atención médica",
        "cuerpo": "No quiere denunciar mientras su hermana siga recibiendo llamadas"}),
    ("ae05_la_propuesta", "r11", 213, {                      # ✦
        "ante": "Un funcionario propone",
        "titulo": "No activar la asistencia hasta que firme una denuncia",
        "cuerpo": "Y utilizar el nombre registral en todo contacto"}),
    ("ae06_lo_que_vio", "r13", 167, {
        "ante": "Samuel",
        "titulo": "Observó varias entregas de documentos a Saúl",
        "cuerpo": "Y conoce cómo se manejan las cuentas"}),
    ("ae07_suplir", "r16", 127, {                            # ✦
        "suelta": "Suplir su versión con el informe de Darío, porque es más rápido"}),
    ("ae08_descartarse", "r17", 212, {                       # ✦
        "ante": "Y otro funcionario",
        "titulo": "«como Samuel no puede comunicarse, no es un testigo útil»",
        "cuerpo": "y debe descartarse"}),
    ("ae10_ya_escuchada", "r20", 157, {
        "suelta": "Ya fue escuchada, con personal capacitado y registro "
                  "audiovisual íntegro"}),
    ("ae11_repetir", "r21", 224, {                           # ✦
        "ante": "Otro funcionario solicita",
        "titulo": "Repetir todo el relato",
        "cuerpo": "porque la adolescente «se mostró tranquila» y omitió "
                  "precisar una fecha"}),
    ("ae12_no_verificado", "r25", 198, {
        "ante": "Se conocen los mensajes",
        "titulo": "No se ha verificado la amenaza",
        "cuerpo": "Ni lo que Patricia sabía de las condiciones"}),
    ("ae14_hipotesis", "r28", 227, {
        "ante": "Por ahora",
        "titulo": "Que el inmueble sea lugar de trata es una hipótesis",
        "cuerpo": "No una conclusión sobre todas las personas que trabajan allí"}),
]

if __name__ == "__main__":
    for nom, r, fr, spec in TENIDOS:
        C.render_carton(spec, fr, None, True,
                        "%s/P3C2_%s.mov" % (OUT, nom), con_tinte=True)
        print("%-22s %-5s %4d cuadros" % (nom, r, fr))
