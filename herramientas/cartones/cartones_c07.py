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

NARRACION = [
    ("n1_ocho_millones", 91, {"suelta": "$8.000.000"}),
    ("n2_reconoce", 111, {
        "titulo": "Carlos reconoce haber recibido el dinero y explica las dificultades que tuvo"}),
    ("n3_incumplimiento", 111, {
        "titulo": "Un incumplimiento de las obligaciones contractuales"}),
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
