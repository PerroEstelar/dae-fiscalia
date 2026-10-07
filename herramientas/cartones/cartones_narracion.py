#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de narración · la primera mitad de los tres videos.

Son los mismos cartones de tinte azul translúcido del bloque de preguntas, pero
pocos y cortos: tres por pieza, puestos donde la narración dice el dato. Todo lo
que llevan es literal del guion del profesor — nombres, cifras y frases suyas —
porque un cartón que inventa una síntesis ya no es el texto del profesor.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_narracion"
os.makedirs(OUT, exist_ok=True)

# caso -> [(nombre, frames, spec)]
NARRACION = {
    "02": [
        ("n1_los_dos", 111, {
            "titulo": "Carlos, funcionario de una entidad pública",
            "cuerpo": "Andrés, representante de una empresa contratista"}),
        ("n2_120_millones", 91, {
            "suelta": "$120 millones"}),
        ("n3_la_defensa", 111, {
            "titulo": "La defensa de Andrés manifiesta su interés en celebrar un preacuerdo"}),
    ],
    "06": [
        ("n1_el_hurto", 111, {
            "titulo": "Un hurto calificado con circunstancias de agravación",
            "cuerpo": "durante la madrugada."}),
        ("n2_varios_meses", 111, {
            "titulo": "Después de varios meses no existe ninguna persona individualizada"}),
        ("n3_las_camaras", 142, {
            "titulo": "No se han solicitado las grabaciones de cámaras ubicadas en las calles cercanas"}),
    ],
    "08": [
        ("n1_fue_archivada", 111, {
            "titulo": "Una indagación por lesiones personales fue archivada"}),
        ("n2_seis_meses", 111, {
            "suelta": "Seis meses después"}),
        ("n3_el_rostro", 91, {
            "titulo": "El rostro de uno de los hombres que participó en los hechos"}),
    ],
}

if __name__ == "__main__":
    casos = sys.argv[1:] or sorted(NARRACION)
    for caso in casos:
        for nombre, n, spec in NARRACION[caso]:
            C.render_carton(spec, n, None, True,
                            f"{OUT}/TA{caso}_{nombre}.mov", con_tinte=True)
