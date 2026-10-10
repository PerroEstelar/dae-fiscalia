#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 03 · coautoría, complicidad y subrogados.

Unidad 4 · Lección 4.3. Las cuatro preguntas son literales del guion del
profesor. Misma retícula y misma animación que `cartones_ta.py`.

Las duraciones salen de repartir las frases del texto sobre los tramos de voz
medidos con `silencedetect` (ver `rejilla/calzar.py`), no de la fórmula.

La narración dura 4.811 cuadros —tres minutos y veinte— así que los cartones no
pueden cubrirla entera: trece cartones sobre los trece momentos que el profesor
subraya, cubriendo el 60 % del tiempo y dejando respirar la imagen en el resto.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c03"
os.makedirs(OUT, exist_ok=True)

PREGUNTAS = [
    ("p0_con_base", 96, {
        "titulo": "El fiscal podría preguntarse",
        "cuerpo": "con base en el anterior contexto."}),
    ("p1_por_que_no_puede", 219, {
        "titulo": "¿Por qué la Fiscalía no puede aceptar que Julián sea condenado como cómplice, si los hechos y las pruebas demuestran que actuó como coautor?"}),
    ("p2_la_diferencia", 274, {
        "titulo": "¿Cuál es la diferencia entre modificar artificialmente la responsabilidad y utilizar una calificación jurídica diferente exclusivamente para efectos punitivos?"}),
    ("p3_sin_respaldo", 284, {
        "titulo": "Si no existe ningún respaldo fáctico o probatorio de una situación de ira o intenso dolor, ¿puede incorporarse esa circunstancia al preacuerdo simplemente para reducir la pena?"}),
    ("p4_los_subrogados", 327, {
        "titulo": "Si la calificación más favorable se utiliza únicamente para determinar la pena, ¿significa que automáticamente deben concederse los subrogados o sustitutos penales correspondientes a esa calificación?"}),
]

NARRACION = [
    ("n1_ambos_participan", 228, {
        "titulo": "Andrés y Julián participan directamente en la ejecución del hurto"}),
    ("n2_el_arma", 184, {
        "titulo": "Andrés amenaza al propietario con un arma mientras Julián recoge las joyas"}),
    ("n3_como_autor", 250, {
        "titulo": "Los elementos materiales probatorios permiten sostener que Julián actuó como autor, y no como simple cómplice"}),
    ("n4_la_defensa_propone", 216, {
        "ante": "La defensa propone",
        "titulo": "Que Julián sea condenado como cómplice, porque su participación fue secundaria"}),
    ("n5_no_seria_admisible", 244, {
        "titulo": "No sería admisible presentar el preacuerdo afirmando que Julián fue cómplice cuando la evidencia muestra que actuó como coautor"}),
    ("n6_calificacion_que_no_corresponde", 246, {
        "titulo": "La negociación no puede asignar a los hechos una calificación jurídica que no corresponde"}),
    ("n7_segunda_propuesta", 250, {
        "ante": "Segunda propuesta",
        "titulo": "Julián sigue siendo responsable como coautor; la referencia a la complicidad opera solo para determinar la pena"}),
    ("n8_solo_la_sancion", 196, {
        "titulo": "La referencia al cómplice opera únicamente para determinar la sanción negociada"}),
    ("n9_ira_e_intenso_dolor", 202, {
        "suelta": "“Ira e intenso dolor”"}),
    ("n10_no_existe_informacion", 250, {
        "titulo": "En la actuación no existe información que permita sostener esas circunstancias"}),
    ("n11_el_juez_distingue", 160, {
        "titulo": "El juez deberá distinguir entre la declaración de responsabilidad y la pena negociada"}),
    ("n12_domiciliaria", 213, {
        "titulo": "La defensa solicita prisión domiciliaria o suspensión de la ejecución de la pena"}),
    ("n13_los_subrogados", 250, {
        "titulo": "Los subrogados y sustitutos se analizan conforme a sus propios requisitos legales, no como consecuencia automática de la ficción"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA03_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, f"{OUT}/TA03_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“Coautoría, complicidad y subrogados”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA03_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Para qué puede usarse una calificación jurídica en un preacuerdo?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA03_carton_cierre.mov", con_marca=True)
