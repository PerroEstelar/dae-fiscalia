#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El lecho de votacion y la tarea del foro del PRIORIDAD 03 · Caso 2.

POR QUE SE VOTA PATRICIA Y NO OTRA COSA
    El documento trae cuatro propuestas equivocadas, pero solo UNA discusion
    con dos posiciones expresas enfrentadas entre integrantes del equipo: un
    integrante propone tratar a Patricia como coautora de inmediato, otro
    sostiene que ser tambien victima excluye cualquier examen.

    Las otras tres propuestas no se votan porque no hay dos posiciones: hay
    una propuesta y un error. Votarlas seria fingir un debate que el caso no
    tiene, y ademas le daria rango de opinion a algo que no lo es. Van en el
    cuerpo de la pieza, a la vista, y vuelven en la tarea del foro.
"""
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C
from cartones_p3c2 import cuadros, FPS

OUT = "/mnt/user-data/outputs/cartones_p3c2"
os.makedirs(OUT, exist_ok=True)

PREGUNTA = "¿Cómo se trata la intervención de Patricia?"

PAUSA = [
    ("p1a_votacion", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "Sus mensajes invitando a Mara existen. Sostiene que los "
                  "escribió después de que Saúl amenazara con expulsarla junto "
                  "con su hija de cuatro años. No se ha verificado el contexto."}),
    ("p1b_opciones", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "a)  Es coautora de trata desde ya: los mensajes están.\n"
                  "b)  Ser también víctima excluye cualquier examen de su "
                  "intervención.\n"
                  "c)  No se califica todavía: falta verificar la amenaza y "
                  "qué sabía."}),
    ("p2_foro", {
        "ante": "Tarea del foro",
        "titulo": "Escoja una de las cuatro personas y diga qué hace el equipo "
                  "primero con ella",
        "cuerpo": "Y diga qué haría falta saber antes de calificar el inmueble."}),
]

if __name__ == "__main__":
    tot = 0
    for n, spec in PAUSA:
        f = cuadros(spec)
        tot += f
        C.render_carton(spec, f, None, True, "%s/P3C2_%s.mov" % (OUT, n), con_tinte=True)
        print("%-16s %4d cuadros  %5.1f s" % (n, f, f / FPS))
    print("lecho de pausas: %d cuadros, %.1f s" % (tot, tot / FPS))
