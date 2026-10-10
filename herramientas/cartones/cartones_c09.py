#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 09 · el conductor y la maniobra.

Unidad 1 · Lección 1.2 —diferencias entre archivo, inadmisión y preclusión—,
que era la única lección del curso sin caso en video. Las cuatro preguntas son
literales del guion del profesor.

El caso cabe en un párrafo, así que el peso lo lleva el bloque de preguntas: la
narración son 561 cuadros y las preguntas 781. Los cartones van densos sobre la
narración (83 % del tiempo) porque es corta y porque cada frase trae un hecho.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c09"
os.makedirs(OUT, exist_ok=True)

PREGUNTAS = [
    ("p0_reflexionar", 152, {
        "titulo": "El fiscal tendría que reflexionar sobre",
        "cuerpo": "para establecer la procedencia de la orden de archivo o de la preclusión."}),
    ("p1_conducta_tipica", 64, {
        "titulo": "¿Existe objetivamente una conducta típica?"}),
    ("p2_circunstancia", 163, {
        "titulo": "¿Existe una conducta que puede ser típica, pero concurre una circunstancia que podría excluir la responsabilidad?"}),
    ("p3_mediante_archivo", 146, {
        "titulo": "¿La existencia de una posible causal de ausencia de responsabilidad puede ser decidida mediante archivo?"}),
    ("p4_el_mecanismo", 164, {
        "titulo": "¿Cómo identificar la naturaleza jurídica de la causal y aplicar el mecanismo procesal compatible con el ordenamiento?"}),
]

NARRACION = [
    ("n1_lesiones", 107, {
        "titulo": "Un conductor causa lesiones a una mujer en un accidente de tránsito"}),
    ("n2_maniobra_brusca", 110, {
        "ante": "La investigación establece",
        "titulo": "El conductor realizó una maniobra brusca"}),
    ("n3_el_nino", 83, {
        "titulo": "Un niño ingresó repentinamente a la vía"}),
    ("n4_el_fiscal_propone", 165, {
        "titulo": "El fiscal considera que obró cobijado por una causal que excluye su responsabilidad, y pretende ordenar el archivo"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"
    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA09_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, f"{OUT}/TA09_{nombre}.mov", con_tinte=True)
    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“El conductor y la maniobra”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA09_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Una causal de ausencia de responsabilidad se decide archivando?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA09_carton_cierre.mov", con_marca=True)
