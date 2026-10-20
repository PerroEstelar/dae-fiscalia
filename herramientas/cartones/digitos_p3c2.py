#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los dos cartones de narración del Caso 2 que llevaban números en letras.

    n05  «Ha salido dos domingos»      ->  «Ha salido 2 domingos»
    n10  «su hija de cuatro años»      ->  «su hija de 4 años»

Los demás cartones de narración no tienen números. Los que sí los tenían y
además eran un nombre con un dato corto —`n01` la fecha, `n04` Mara y su edad,
`n07` Darío— dejaron de ser cartones y son lower thirds.

El conteo de cuadros no cambia al pasar a dígitos: las dos frases siguen
teniendo las mismas palabras contables y el piso de 96 manda igual.
"""
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_p3c2"

DOS = [
    ("n05_domingos", 96, {"suelta": "Ha salido 2 domingos, y ha regresado"}),
    ("n10_amenaza", 168, {
        "ante": "Patricia sostiene",
        "titulo": "que lo hizo tras una amenaza de expulsión",
        "cuerpo": "junto con su hija de 4 años"}),
]

if __name__ == "__main__":
    for nom, fr, spec in DOS:
        C.render_carton(spec, fr, None, True,
                        "%s/P3C2_%s.mov" % (OUT, nom), con_tinte=True)
        print(nom, fr)
