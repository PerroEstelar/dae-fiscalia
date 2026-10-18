#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de pausa del C5U4: el lecho de votacion y la tarea del foro.

La pregunta de la votacion es la del Activo A, que es el eje mas fino del
caso: el comprador hizo las cuatro diligencias que se le pueden pedir y aun
asi compro a un testaferro.

Regla de la casa: las opciones son posiciones, no respuestas. Ninguna afirma
contenido juridico que el texto del profesor no enuncie.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C
from cartones_c5u4 import cuadros, FPS

OUT = "/mnt/user-data/outputs/cartones_c5u4"
os.makedirs(OUT, exist_ok=True)

PREGUNTA = "¿Qué ocurre con la adquisición del comprador del hotel?"

PAUSA = [
    # la premisa: las cuatro diligencias, y el hecho que lo complica
    ("p1a_votacion", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "Revisó el certificado de tradición, que no tenía gravámenes. "
                  "Otorgó promesa de compraventa. Pagó el valor comercial por el "
                  "banco. Inscribió el título. Y le compró a un testaferro de la "
                  "organización."}),
    # las tres opciones, con la pregunta todavia a la vista
    ("p1b_opciones", {
        "ante": "Votación",
        "titulo": PREGUNTA,
        "cuerpo": "a)  Se mantiene: acreditó buena fe exenta de culpa.\n"
                  "b)  Se extingue: el bien tiene origen ilícito, sin importar "
                  "quién lo tenga hoy.\n"
                  "c)  Depende de si las diligencias que hizo bastaban según el "
                  "valor y la naturaleza del bien."}),
    ("p2_foro", {
        "ante": "Tarea del foro",
        "titulo": "Proponga cómo afectar la cadena de estaciones de servicio",
        "cuerpo": "protegiendo a los dos socios minoritarios y los ochenta "
                  "empleos, e indique qué medida concreta usaría."}),
]

if __name__ == "__main__":
    tot = 0
    for n, spec in PAUSA:
        f = cuadros(spec)
        tot += f
        C.render_carton(spec, f, None, True, "%s/C5U4_%s.mov" % (OUT, n),
                        con_tinte=True)
        print("%-16s %4d cuadros  %5.1f s" % (n, f, f / FPS))
    print("lecho de pausas: %d cuadros, %.1f s" % (tot, tot / FPS))
