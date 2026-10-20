#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del PRIORIDAD 03 · Caso 2 «El taller del segundo piso».

LAS CUATRO PROPUESTAS EQUIVOCADAS VAN A CARTON, Y VAN LITERALES
    Es el material didactico del caso. Un carton las pone a la vista sin que
    nadie las diga en pantalla, que es exactamente lo que hay que lograr: el
    participante tiene que reconocerlas como propuestas de su propio equipo,
    no como errores de un personaje.

    Por eso ninguna propuesta va encima de una cara. Van en ranura propia, con
    fondo blanco. Poner «no es un testigo util» sobre el primer plano de
    Samuel convertiria la frase en algo que a el le pasa, cuando es algo que
    el equipo dice.

EL VERBATIM
    Dos frases se citan entre comillas porque son del documento y porque son
    lo que hay que reconocer:

        «como Samuel no puede comunicarse, no es un testigo util»
        «se mostro tranquila»

LO QUE NINGUN CARTON HACE
    Ninguno corrige. El video no dice cual es el error: lo pone donde se vea.

LA FAMILIA `GRAFICOS` DE ESTE ARCHIVO YA NO SE USA. QUEDA COMO REGISTRO.
    La mitad de la pieza era losa blanca -catorce de veintiocho ranuras- y en
    la revision de Sebastian eso se acabo. Se repartieron asi:

        once a CARTON TENIDO sobre cama      `ae_tenidos_p3c2.py`
        dos a GRAFICA DE MOTION              `../graficas/graficas_p3c2.py`
            ae02, la fila de seis que se abre en 2 y 4
            ae13, las cinco decisiones renglon a renglon
        uno a LOWER THIRD                    `lowerthirds_p3c2.py`
            ae09, que era Elisa y su edad

    Y de NARRACION se fueron cuatro: `n01` la fecha, `n04` Mara y `n07` Dario
    son lower thirds -un nombre con un dato corto-, y `n02` desaparecio porque
    decia lo mismo que la grafica de r03, que va justo antes.

    `n05` y `n10` se volvieron a renderizar con los numeros en digitos, en
    `digitos_p3c2.py`.

    Correr este archivo vuelve a escribir las losas blancas encima de los
    cartones tenidos. Por eso su `__main__` ya no renderiza nada: esta aqui
    para leer, no para correr.
"""
import math
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_p3c2"
os.makedirs(OUT, exist_ok=True)

FPS = 23.976023976
PPM = 168.0


def cuadros(spec, holgura=1.15, minimo=96):
    txt = " ".join(spec.get(k, "") for k in ("ante", "titulo", "cuerpo", "suelta"))
    n = len([w for w in txt.split() if any(ch.isalnum() for ch in w)])
    return max(minimo, int(math.ceil(n / PPM * 60 * FPS * holgura)))


# ---------------------------------------------------------------- graficos
GRAFICOS = [
    ("ae01_primer_contacto", "r01", 165, {
        "suelta": "La información es la del primer contacto. No se tiene por "
                  "demostrada la responsabilidad de nadie"}),
    ("ae02_seis_personas", "r03", 217, {
        "ante": "Seis personas",
        "titulo": "Dos conservan documentos, cobran por prenda y pueden irse",
        "cuerpo": "Las otras cuatro: catorce horas y una deuda sin explicar"}),
    ("ae03_pasaporte", "r07", 180, {
        "ante": "Mara",
        "titulo": "Afirma que Saúl conserva su pasaporte",
        "cuerpo": "Y que divulgará imágenes privadas si se va"}),
    ("ae04_pide", "r10", 185, {
        "ante": "Mara pide",
        "titulo": "Alojamiento y atención médica",
        "cuerpo": "No quiere denunciar mientras su hermana siga recibiendo llamadas"}),
    ("ae05_la_propuesta", "r11", 213, {
        "ante": "Un funcionario propone",
        "titulo": "No activar la asistencia hasta que firme una denuncia",
        "cuerpo": "Y utilizar el nombre registral en todo contacto"}),
    ("ae06_lo_que_vio", "r13", 167, {
        "ante": "Samuel",
        "titulo": "Observó varias entregas de documentos a Saúl",
        "cuerpo": "Y conoce cómo se manejan las cuentas"}),
    ("ae07_suplir", "r16", 127, {
        "suelta": "Suplir su versión con el informe de Darío, porque es más rápido"}),
    ("ae08_descartarse", "r17", 212, {
        "ante": "Y otro funcionario",
        "titulo": "«como Samuel no puede comunicarse, no es un testigo útil»",
        "cuerpo": "y debe descartarse"}),
    ("ae09_por_la_tia", "r19", 157, {
        "ante": "Elisa, diecisiete años",
        "titulo": "Llegó por una tía que recibe parte de su remuneración"}),
    ("ae10_ya_escuchada", "r20", 157, {
        "suelta": "Ya fue escuchada, con personal capacitado y registro "
                  "audiovisual íntegro"}),
    ("ae11_repetir", "r21", 224, {
        "ante": "Otro funcionario solicita",
        "titulo": "Repetir todo el relato",
        "cuerpo": "porque la adolescente «se mostró tranquila» y omitió "
                  "precisar una fecha"}),
    ("ae12_no_verificado", "r25", 198, {
        "ante": "Se conocen los mensajes",
        "titulo": "No se ha verificado la amenaza",
        "cuerpo": "Ni lo que Patricia sabía de las condiciones"}),
    ("ae13_cinco_decisiones", "r26", 215, {
        "ante": "El equipo debe decidir",
        "titulo": "Asistencia · canales · entrevista · participación · investigación"}),
    ("ae14_hipotesis", "r28", 227, {
        "ante": "Por ahora",
        "titulo": "Que el inmueble sea lugar de trata es una hipótesis",
        "cuerpo": "No una conclusión sobre todas las personas que trabajan allí"}),
]

# --------------------------------------------------------------- narracion
NARRACION = [
    ("n01_cucuta", "r02", 263, {"suelta": "Cúcuta, dieciocho de marzo"}),
    ("n02_seis", "r04", 238, {"suelta": "Seis personas trabajan y duermen allí"}),
    ("n03_candados", "r05", 154, {"suelta": "No hay candados"}),
    ("n04_mara", "r06", 140, {"suelta": "Mara, veintiséis años"}),
    ("n05_domingos", "r09", 203, {"suelta": "Ha salido dos domingos, y ha regresado"}),
    ("n06_senas", "r12", 287, {
        "ante": "Samuel",
        "titulo": "Usa señas de su entorno familiar",
        "cuerpo": "No domina la lengua de señas colombiana"}),
    ("n07_dario", "r14", 138, {"suelta": "Darío trabaja para Saúl"}),
    ("n08_por_separado", "r15", 267, {
        "ante": "Preguntado por separado",
        "titulo": "el equipo no logra comprender sus respuestas"}),
    ("n09_delante", "r22", 163, {"suelta": "Elisa pide no hablar delante de la tía"}),
    ("n10_amenaza", "r24", 255, {
        "ante": "Patricia sostiene",
        "titulo": "que lo hizo tras una amenaza de expulsión",
        "cuerpo": "junto con su hija de cuatro años"}),
    ("n11_sin_riesgos", "r27", 138, {"suelta": "Sin evaluación de riesgos"}),
]

if __name__ == "__main__":
    print(__doc__)
