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

# Cartones sobre la narración. Eran tres —los de `cartones_narracion.py`— y la
# pieza se sentía hueca. Ahora son seis, calzados al tramo de voz medido con
# `silencedetect` sobre TA08_NARRADOR.wav: cada uno empieza en el cuadro en que
# empieza su frase y dura exactamente lo que dura. Texto literal del guion.
NARRACION = [
    ("n1_lesiones", 63, {
        "titulo": "Una indagación por lesiones personales fue archivada"}),
    ("n2_no_permitian", 118, {
        "titulo": "Las grabaciones disponibles no permitían establecer quién había agredido a la víctima"}),
    ("n3_seis_meses", 50, {"suelta": "Seis meses después"}),
    ("n4_otro_video", 72, {
        "titulo": "La víctima encuentra un video tomado desde otro establecimiento comercial"}),
    ("n5_el_rostro", 142, {
        "titulo": "Se observa con mayor claridad el rostro de uno de los hombres que participó en los hechos"}),
    ("n6_el_abogado", 129, {
        "titulo": "El abogado informa del video a la Fiscalía y solicita que se continúe con la actuación"}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"

    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA08_{nombre}.mov", con_tinte=True)

    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, f"{OUT}/TA08_{nombre}.mov", con_tinte=True)

    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“El video que aparece seis meses después”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA08_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Cuál fue la razón concreta del archivo?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA08_carton_cierre.mov", con_marca=True)
