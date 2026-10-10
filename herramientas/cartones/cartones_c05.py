#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 05 · la negociación paso a paso.

Unidad 4 · Lección 4.2. Las tres preguntas son literales del guion del profesor.

Es el único caso de la serie que enseña el método completo, así que los
cartones tienen una función que no tienen en los otros: los antetítulos
«Apertura», «Intercambio» y «Cierre» son la columna de la pieza. El resto de
los cartones cuelga de esos tres.

Las duraciones salen de repartir las frases sobre los tramos de voz medidos
(ver `rejilla/calzar.py`), no de la fórmula.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c05"
os.makedirs(OUT, exist_ok=True)

PREGUNTAS = [
    ("p0_en_el_marco", 80, {
        "titulo": "El fiscal debería preguntarse",
        "cuerpo": "en el marco del anterior proceso."}),
    ("p1_la_apertura", 241, {
        "titulo": "En la etapa de apertura, ¿qué aspectos debe identificar el fiscal antes de comenzar a formular o recibir propuestas? ¿Y cuáles deben permanecer fuera de la negociación?"}),
    ("p2_el_intercambio", 134, {
        "titulo": "Durante el intercambio, ¿qué debe preguntarse el fiscal frente a cada concesión que realiza?"}),
    ("p3_el_cierre", 254, {
        "titulo": "¿Por qué no es suficiente que las partes hayan llegado a un consenso para formalizar el preacuerdo? ¿Qué debe verificar el fiscal durante el cierre?"}),
]

NARRACION = [
    ("n1_laura", 207, {
        "titulo": "Laura, administradora de una empresa que habría presentado información falsa para obtener tres contratos con una entidad pública"}),
    ("n2_coordino", 160, {
        "titulo": "Laura coordinó la elaboración y la presentación de los documentos"}),
    ("n3_doscientos_cincuenta", 137, {"suelta": "$250 millones"}),
    ("n4_se_recaudaron", 250, {
        "titulo": "Correos electrónicos, documentos contractuales, declaraciones de empleados y registros contables"}),
    ("n5_base_probatoria", 250, {
        "titulo": "Existe una base probatoria suficiente para sostener la teoría del caso"}),
    ("n6_la_defensa", 250, {
        "ante": "La defensa",
        "titulo": "Laura está dispuesta a aceptar responsabilidad y terminar anticipadamente el proceso"}),
    ("n7_apertura", 250, {
        "ante": "Apertura",
        "titulo": "Qué consecuencias jurídicas pueden acordarse como contraprestación por la aceptación de responsabilidad"}),
    ("n8_lo_que_no", 250, {
        "titulo": "El fiscal identifica también aquello que no puede ser objeto de negociación"}),
    ("n9_precisa_los_hechos", 220, {
        "titulo": "Precisa los hechos que considera establecidos y aquellos que podrían ser materia de discusión"}),
    ("n10_intercambio", 265, {
        "ante": "Intercambio",
        "titulo": "La defensa propone que Laura acepte los cargos a cambio de una reducción significativa de la pena"}),
    ("n11_sin_respaldo", 250, {
        "titulo": "La circunstancia solicitada no tiene suficiente respaldo: no puede utilizarse como concesión"}),
    ("n12_nueva_propuesta", 250, {
        "titulo": "Laura acepta integralmente los hechos, renuncia al juicio y entrega información sobre otros involucrados"}),
    ("n13_que_recibe", 246, {
        "titulo": "Qué concede la Fiscalía, por qué puede concederlo, y qué recibe a cambio"}),
    ("n14_cierre", 250, {
        "ante": "Cierre",
        "titulo": "Antes de formalizar el preacuerdo, el fiscal realiza una revisión integral"}),
    ("n15_el_beneficio", 250, {
        "titulo": "El tratamiento del beneficio patrimonial, su reintegro y la situación de la entidad afectada"}),
    ("n16_la_victima", 278, {
        "titulo": "Los derechos de la víctima, y poder explicar ante el juez por qué cada concesión encuentra fundamento jurídico"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA05_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, f"{OUT}/TA05_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“La negociación paso a paso”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA05_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Qué concede la Fiscalía, y qué recibe a cambio?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA05_carton_cierre.mov", con_marca=True)
