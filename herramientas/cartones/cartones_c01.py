#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 01 · los tres escenarios probatorios.

Unidad 4 · Lección 4.2. Las cuatro preguntas son literales del guion del
profesor. Misma retícula y misma animación que `cartones_ta.py`; este archivo
solo trae el contenido.

Las duraciones de las preguntas NO salen de la fórmula: salen de medir los
silencios de la pista de voz real con `silencedetect`. Cada cartón dura
exactamente lo que dura su pregunta en boca de la narradora.

Los tres cartones de narración son las etiquetas de escenario. La etiqueta va
en el antetítulo y el cuerpo del cartón es una frase literal del guion: el
rótulo ordena, el profesor habla.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c01"
os.makedirs(OUT, exist_ok=True)

# cuadros medidos sobre TA01_PREGUNTAS.wav: 137 · 157 · 237 · 385 · 303
PREGUNTAS = [
    ("p0_el_fiscal_responde", 137, {
        "titulo": "El fiscal debe responder las siguientes preguntas",
        "cuerpo": "para analizar la viabilidad del preacuerdo."}),
    ("p1_de_la_misma_manera", 157, {
        "titulo": "¿Responde la Fiscalía a la propuesta de la defensa de la misma manera en los tres escenarios? ¿Por qué?"}),
    ("p2_la_contraprestacion", 237, {
        "titulo": "¿Cómo debería valorar el fiscal la contraprestación que está recibiendo a cambio de la concesión, teniendo en cuenta la fortaleza o debilidad de su teoría del caso?"}),
    ("p3_en_cual_de_los_escenarios", 385, {
        "titulo": "En cuál de los escenarios la negociación puede servir para obtener una contraprestación procesal frente a una alta probabilidad de éxito en juicio, y en cuál para reducir la incertidumbre propia de un caso con riesgos probatorios"}),
    ("p4_debe_negociar_necesariamente", 303, {
        "titulo": "En el tercer escenario, ¿la debilidad probatoria significa que la Fiscalía debe negociar necesariamente, o debe valorar primero si el preacuerdo constituye realmente una alternativa adecuada?"}),
]

# Cartones sobre la narración. La primera mitad iba vacía —cincuenta segundos
# sin un solo cartón— y la pieza se sentía hueca. Ahora el hecho se va fijando
# en pantalla a medida que se cuenta, y los tres rótulos de escenario ordenan la
# segunda mitad. Todo el texto es literal del guion del profesor.
NARRACION = [
    ("n1_alejandro", 111, {
        "titulo": "Alejandro, empleado de una empresa de transporte"}),
    ("n2_ochenta_millones", 91, {
        "suelta": "$80 millones"}),
    ("n3_la_madrugada", 111, {
        "titulo": "Retirar el dinero durante la madrugada"}),
    ("n4_el_abogado", 142, {
        "titulo": "El abogado manifiesta que su defendido está dispuesto a aceptar responsabilidad mediante un preacuerdo"}),
    ("n5_valorar", 91, {
        "titulo": "El fiscal debe valorar integralmente los medios probatorios"}),
    ("n6_escenario_1", 111, {
        "ante": "Escenario 1",
        "titulo": "Se identifica claramente a Alejandro retirando el dinero"}),
    ("n7_escenario_2", 111, {
        "ante": "Escenario 2",
        "titulo": "No permiten identificarlo plenamente"}),
    ("n8_escenario_3", 111, {
        "ante": "Escenario 3",
        "titulo": "Las cámaras no permiten identificar al autor"}),
    ("n9_la_misma_propuesta", 142, {
        "titulo": "En los tres escenarios, la propuesta de la defensa es exactamente la misma"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"

    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA01_{nombre}.mov", con_tinte=True)

    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, f"{OUT}/TA01_{nombre}.mov", con_tinte=True)

    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“Los tres escenarios probatorios”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA01_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Responde la Fiscalía de la misma manera en los tres escenarios?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA01_carton_cierre.mov", con_marca=True)
