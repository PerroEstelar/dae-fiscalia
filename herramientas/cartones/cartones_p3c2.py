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
    print("%-24s %-5s %6s %6s %7s" % ("carton", "ranura", "cartón", "ranura", "margen"))
    apretados = []
    for fam, lista, alfa, tinte in (("gráfico", GRAFICOS, False, False),
                                    ("narración", NARRACION, True, True)):
        print("--- %s" % fam)
        for n, r, fr, spec in lista:
            necesita = cuadros(spec)
            f = fr if not alfa else necesita
            m = fr - necesita
            if m < 0:
                apretados.append((n, m))
            C.render_carton(spec, f, C.BLANCO_FONDO if not alfa else None, alfa,
                            "%s/P3C2_%s.mov" % (OUT, n), con_tinte=tinte)
            print("%-24s %-5s %6d %6d %+7d" % (n, r, f, fr, m))
    print("\nAPRETADOS:", apretados or "ninguno")
