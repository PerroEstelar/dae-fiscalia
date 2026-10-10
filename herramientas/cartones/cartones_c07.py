#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 07 · ¿incumplimiento contractual o delito?

Unidad 1 · Lección 1.1. Las seis preguntas son literales del guion del profesor,
con sus paréntesis y sus comillas tal como él las escribió. Las duraciones salen
de `silencedetect` sobre la pista de voz real, no de la fórmula.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c07"
os.makedirs(OUT, exist_ok=True)

PREGUNTAS = [
    ("p0_el_fiscal_podria", 218, {
        "titulo": "El fiscal podría preguntarse",
        "cuerpo": "para reconocer la existencia de una presunta conducta típica e identificar la procedencia o no de la orden de archivo."}),
    ("p1_tipos_penales", 123, {
        "titulo": "¿Cuál o cuáles (concurso de delitos) son los tipos penales que encajarían en los hechos analizados?"}),
    ("p2_elementos_objetivos", 95, {
        "titulo": "¿Qué elementos objetivos de ese(os) tipo(s) penal(es) deben verificarse?"}),
    ("p3_conducta_tipica", 110, {
        "titulo": "¿La información disponible permite reconocer una conducta objetivamente típica?"}),
    ("p4_ausencia_de_elementos", 128, {
        "titulo": "¿La ausencia de elementos para establecer “X” puede ser resuelta mediante una orden de archivo?"}),
    ("p5_actos_de_investigacion", 101, {
        "titulo": "¿Es necesario realizar actos de investigación?, ¿cuáles?"}),
    ("p6_por_que_archivo", 181, {
        "titulo": "¿Estoy archivando porque objetivamente no existe delito o porque todavía no he podido establecer cómo actuó una persona determinada?"}),
]

# Cartones sobre la narración. Eran tres y la primera mitad se sentía hueca.
# Ahora son ocho, calzados al tramo de voz medido con `silencedetect` sobre
# TA07_NARRADOR.wav: cada cartón empieza en el cuadro en que empieza su frase y
# dura exactamente lo que dura. Todo el texto es literal del guion del profesor.
#
# El hueco entre el cuadro 469 y el 625 de la narración queda LIBRE a propósito:
# ahí va el lower third que Sebastian armó a mano en Fusion —«No podía continuar
# con la obra, debido a dificultades económicas»— y no se le pone nada encima.
NARRACION = [
    ("n1_la_denuncia", 96, {
        "titulo": "María formula una denuncia contra Carlos por el delito de abuso de confianza"}),
    ("n2_ocho_millones", 91, {"suelta": "$8.000.000"}),
    ("n3_materiales", 86, {
        "titulo": "Para que comprara materiales destinados a la remodelación de su vivienda"}),
    ("n4_se_robo", 85, {
        "titulo": "María sostiene que Carlos se robó su dinero y solicita que sea procesado penalmente"}),
    ("n5_el_contrato", 140, {
        "titulo": "Se recauda el contrato celebrado entre las partes y los comprobantes de pago"}),
    ("n6_reconoce", 173, {
        "titulo": "Carlos reconoce haber recibido el dinero y explica las dificultades que tuvo para terminar la obra"}),
    ("n7_incumplimiento", 166, {
        "titulo": "Se produjo un incumplimiento de las obligaciones contractuales"}),
    ("n8_apropiarselo", 159, {
        "titulo": "No encuentra elementos que permitan afirmar que Carlos recibió el dinero con la finalidad de apropiárselo"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA07_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, f"{OUT}/TA07_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“¿Incumplimiento contractual o delito?”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA07_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Objetivamente no existe delito, o todavía no se ha establecido?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA07_carton_cierre.mov", con_marca=True)
