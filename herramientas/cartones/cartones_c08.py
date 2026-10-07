#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 08 · el video que aparece seis meses después.

Unidad 1 · Lección 1.3 · desarchivo. Las cuatro preguntas son literales del
guion del profesor. Misma retícula y misma animación que `cartones_ta.py`;
este archivo solo trae el contenido.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c08"
os.makedirs(OUT, exist_ok=True)

# (nombre, frames, spec)
PREGUNTAS = [
    ("p0_el_fiscal_deberia", 194, {
        "titulo": "El fiscal debería preguntarse",
        "cuerpo": "para identificar la procedencia o no de una orden de desarchivo."}),
    ("p1_razon_del_archivo", 111, {
        "titulo": "¿Cuál fue la razón concreta del archivo?"}),
    ("p2_que_nueva_evidencia", 142, {
        "titulo": "¿Qué nueva evidencia física o información legalmente obtenida se conoció?"}),
    ("p3_capacidad_de_modificar", 194, {
        "titulo": "¿Este nuevo elemento probatorio tiene capacidad para modificar los fundamentos que justificaron la decisión inicial?"}),
    ("p4_que_actuaciones", 152, {
        "titulo": "¿Qué actuaciones investigativas podrían adelantarse a partir de ese elemento conocido?"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"

    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA08_{nombre}.mov", con_tinte=True)

    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“El video que aparece seis meses después”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA08_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Cuál fue la razón concreta del archivo?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA08_carton_cierre.mov", con_marca=True)
