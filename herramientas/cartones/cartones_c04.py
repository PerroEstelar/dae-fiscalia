#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 04 · la marginalidad alegada sin sustento.

Unidad 4 · Lección 4.1. Las seis preguntas son literales del guion del profesor.
Misma retícula y misma animación que `cartones_ta.py`; aquí solo va el contenido.

Las duraciones salen de medir los silencios de las dos pistas de voz reales, no
de la fórmula. Los cartones de narración son siete, repartidos por toda la
primera mitad: un video con la narración desnuda se siente hueco.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c04"
os.makedirs(OUT, exist_ok=True)

# cuadros medidos sobre TA04_PREGUNTAS.wav: 195 · 197 · 97 · 88 · 96 · 214 · 204
PREGUNTAS = [
    ("p0_el_fiscal_determina", 195, {
        "titulo": "El fiscal debe contestar las siguientes preguntas",
        "cuerpo": "para determinar si, en estas condiciones, puede celebrar el preacuerdo."}),
    ("p1_reconocer_marginalidad", 197, {
        "titulo": "¿Puede el fiscal reconocer en el preacuerdo la circunstancia de marginalidad solicitada por la defensa, a fin de favorecer la negociación?"}),
    ("p2_fundamento_factico", 97, {
        "titulo": "¿Existe un fundamento fáctico para la circunstancia alegada?"}),
    ("p3_elementos_probatorios", 88, {
        "titulo": "¿Existen elementos probatorios que permitan sostenerla?"}),
    ("p4_relacion_con_la_conducta", 96, {
        "titulo": "¿La circunstancia tiene relación con la ejecución de la conducta?"}),
    ("p5_creando_o_reconociendo", 214, {
        "titulo": "¿El fiscal está simplemente «creando» una circunstancia para disminuir la pena, o está reconociendo una situación que encuentra respaldo en la actuación?"}),
    ("p6_moneda_de_cambio", 204, {
        "titulo": "¿Qué diferencia existe entre reconocer una circunstancia que tiene sustento en los hechos y utilizarla artificialmente como «moneda de cambio»?"}),
]

NARRACION = [
    ("n1_el_hurto", 111, {
        "titulo": "El hurto de varios equipos electrónicos de un establecimiento comercial"}),
    ("n2_dieciocho_millones", 91, {
        "suelta": "$18 millones"}),
    ("n3_tecnico_de_sistemas", 142, {
        "titulo": "Miguel había trabajado anteriormente como técnico de sistemas",
        "cuerpo": "y tenía ingresos provenientes de esa actividad"}),
    ("n4_no_existen_elementos", 142, {
        "titulo": "No existen elementos probatorios que indiquen que se encontrara en una situación de pobreza extrema, marginalidad o ignorancia"}),
    ("n5_la_defensa_propone", 111, {
        "ante": "La defensa propone",
        "titulo": "Reconocer la circunstancia del artículo 56 del Código Penal"}),
    ("n6_dificultades", 91, {
        "suelta": "“Dificultades económicas”"}),
    ("n7_la_rebaja", 142, {
        "titulo": "Miguel asume la responsabilidad penal y solicita una reducción significativa de la pena"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA04_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, f"{OUT}/TA04_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“La marginalidad alegada sin sustento”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA04_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Existe un fundamento fáctico para la circunstancia alegada?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA04_carton_cierre.mov", con_marca=True)
