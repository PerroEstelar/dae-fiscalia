#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 06 · el hurto de madrugada.

Usa la misma retícula y la misma animación que `cartones_ta.py` — este archivo
solo trae el contenido. Las preguntas son literales del guion del profesor.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c06"
os.makedirs(OUT, exist_ok=True)

# (nombre, frames, spec)
PREGUNTAS = [
    ("p0_el_fiscal_deberia", 194, {
        "titulo": "El fiscal debería preguntarse",
        "cuerpo": "para delimitar al sujeto activo y verificar la procedencia o no de la orden de archivo."}),
    ("p1_archivar_por_imposibilidad", 163, {
        "titulo": "¿Puede el fiscal archivar las diligencias por la imposibilidad de establecer al sujeto activo?"}),
    ("p2_causal_suficiente", 204, {
        "titulo": "¿La falta de identificación o individualización inicial del autor constituye, por sí sola, una causal suficiente para archivar?"}),
    ("p3_hasta_que_punto", 92, {
        "titulo": "¿Hasta qué punto se ha impulsado activamente la indagación?"}),
    ("p4_actividades_exigibles", 153, {
        "titulo": "¿Qué actividades investigativas resultan razonablemente exigibles en este momento de la investigación?"}),
    ("p5_preservacion_temprana", 174, {
        "titulo": "¿Se han seguido los pasos de la intervención y preservación temprana de fuentes de información?"}),
    ("p6_asociacion", 92, {
        "titulo": "¿Podría existir asociación o relación con otras investigaciones?"}),
    ("p7_que_se_hizo", 255, {
        "titulo": "¿Qué se hizo para identificar al sujeto?",
        "cuerpo": "¿Qué resultados se obtuvieron? ¿Por qué, a pesar de las actividades realizadas, persiste la imposibilidad?"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"

    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA06_{nombre}.mov", con_tinte=True)

    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso 06", "titulo": "El hurto de madrugada"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA06_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Hasta qué punto se ha impulsado activamente la indagación?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA06_carton_cierre.mov", con_marca=True)
