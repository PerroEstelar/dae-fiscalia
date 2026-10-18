#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de pausa del C5U3: el lecho de votacion y la tarea del foro.

Misma regla de 168 ppm con holgura. El eje del caso es que los cinco bienes
salen de la misma diligencia y ninguno llega en la misma condicion, asi que la
premisa tiene que enumerarlos: sin la lista la pregunta no se entiende.

Regla de la casa: las opciones son posiciones, no respuestas. Ninguna afirma
contenido juridico que el texto del profesor no enuncie.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C
from cartones_c5u3 import cuadros, FPS

OUT = "/mnt/user-data/outputs/cartones_c5u3"
os.makedirs(OUT, exist_ok=True)

PREGUNTA = "¿Procede la misma medida sobre los cinco bienes?"

PAUSA = [
    # la premisa: los cinco bienes y la circunstancia de cada uno
    ("p1a_votacion", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "Ocho vehículos aprehendidos como presuntos instrumentos. Una "
                  "bodega con un tercero arrendatario adentro. Quince servidores "
                  "que se deprecian mes a mes. Quinientos millones en efectivo, "
                  "junto a la prueba contable. Y dos apartamentos sin ocupar."}),
    # las tres opciones, con la pregunta todavia a la vista
    ("p1b_opciones", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "a)  Sí: lo recaudado en una misma diligencia sigue una misma "
                  "suerte.\n"
                  "b)  No: la condición de cada bien —instrumento, producto, "
                  "prueba o bien sujeto a registro— define la medida.\n"
                  "c)  Depende de si el bien se aprehende materialmente o basta "
                  "afectarlo jurídicamente."}),
    ("p2_foro", {
        "ante": "Tarea del foro",
        "titulo": "Escoja dos de los cinco bienes y diga qué medida procede sobre "
                  "cada uno",
        "cuerpo": "y qué hace con el tercero arrendatario y con los equipos que "
                  "se deprecian mientras el proceso avanza."}),
]

if __name__ == "__main__":
    tot = 0
    for n, spec in PAUSA:
        f = cuadros(spec)
        tot += f
        C.render_carton(spec, f, None, True, "%s/C5U3_%s.mov" % (OUT, n),
                        con_tinte=True)
        print("%-16s %4d cuadros  %5.1f s" % (n, f, f / FPS))
    print("lecho de pausas: %d cuadros, %.1f s" % (tot, tot / FPS))
