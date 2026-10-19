#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El lecho de votacion y la tarea del foro del PRIORIDAD 03 · Caso 1.

LA PREGUNTA ES LA DEL CASO, NO UNA MIA
    El documento trae las tres tesis del equipo y esas son las opciones,
    literales. Ninguna se presenta como la correcta y el carton no insinua
    cual lo es: si el video contesta, el taller sobra.

POR QUE LA PREMISA VA EN SU PROPIO CARTON
    La votacion se decide comparando personas, y para eso hay que tener a la
    vista que son nueve y que ninguna esta en la misma posicion. Ese recuerdo
    va primero, solo, y despues entran las tres opciones con la pregunta
    todavia arriba.
"""
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C
from cartones_p3c1 import cuadros, FPS

OUT = "/mnt/user-data/outputs/cartones_p3c1"
os.makedirs(OUT, exist_ok=True)

PREGUNTA = "¿Responden todos por trata?"

PAUSA = [
    ("p1a_votacion", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "Nueve personas en el mismo hospedaje. Una llegó por su cuenta "
                  "y se fue cuando quiso. Otra podía salir a la tienda y tenía "
                  "que volver. Otra nunca alcanzó a generar ingresos."}),
    ("p1b_opciones", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "a)  Sí: todos los que contribuyeron al funcionamiento del "
                  "hospedaje.\n"
                  "b)  No: quienes llegaron voluntariamente o podían salir a la "
                  "calle quedan fuera.\n"
                  "c)  Frente a Juliana solo cabría tentativa, porque nunca fue "
                  "explotada."}),
    ("p2_foro", {
        "ante": "Tarea del foro",
        "titulo": "Escoja dos de las nueve personas y explique qué las separa",
        "cuerpo": "Y diga qué significa, en cada una, haber podido salir a la calle."}),
]

if __name__ == "__main__":
    tot = 0
    for n, spec in PAUSA:
        f = cuadros(spec)
        tot += f
        C.render_carton(spec, f, None, True, "%s/P3C1_%s.mov" % (OUT, n), con_tinte=True)
        print("%-16s %4d cuadros  %5.1f s" % (n, f, f / FPS))
    print("lecho de pausas: %d cuadros, %.1f s" % (tot, tot / FPS))
