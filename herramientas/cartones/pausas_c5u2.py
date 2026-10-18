#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de pausa del C5U2: el lecho de votacion y la tarea del foro.

Misma regla de duracion que los de narracion: 168 palabras por minuto, con
holgura. La leccion del C5U1 fue que un carton de 80 palabras en 8 segundos va
a 600 ppm y no se lee; aqui el texto manda sobre el reloj.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C
from cartones_c5u2 import cuadros, FPS

OUT = "/mnt/user-data/outputs/cartones_c5u2"
os.makedirs(OUT, exist_ok=True)

PREGUNTA = "¿Procede la misma medida sobre todo el patrimonio?"

PAUSA = [
    # la premisa y la pregunta
    ("p1a_votacion", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "Un patrimonio de origen lícito: una casa habitada, una "
                  "camioneta de uso personal y el cuarenta por ciento de una "
                  "sociedad que no está imputada. La pretensión es de tres mil "
                  "quinientos millones."}),
    # las tres opciones, con la pregunta todavia a la vista
    ("p1b_opciones", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "a)  Sí: el patrimonio responde como un todo.\n"
                  "b)  No: la casa habitada y los bienes de un tercero no "
                  "imputado tienen régimen propio.\n"
                  "c)  Depende de si el bien está sujeto a registro y de quién "
                  "es su titular."}),
    ("p2_foro", {
        "ante": "Tarea del foro",
        "titulo": "Escoja dos bienes del inventario y diga qué medida procede "
                  "sobre cada uno",
        "cuerpo": "y en qué momento procesal, contando el término de seis meses "
                  "y la caución."}),
]

if __name__ == "__main__":
    tot = 0
    for n, spec in PAUSA:
        f = cuadros(spec)
        tot += f
        C.render_carton(spec, f, None, True, "%s/C5U2_%s.mov" % (OUT, n),
                        con_tinte=True)
        print("%-16s %4d cuadros  %5.1f s" % (n, f, f / FPS))
    print("lecho de pausas: %d cuadros, %.1f s" % (tot, tot / FPS))
