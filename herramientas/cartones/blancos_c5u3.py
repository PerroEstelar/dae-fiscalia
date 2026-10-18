#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de entrada y de cierre del C5U3: fondo blanco, con marca de agua."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c5u3"
os.makedirs(OUT, exist_ok=True)

TITULO = {"ante": "Caso", "titulo": "«Eslabón Financiero»"}

if __name__ == "__main__":
    for n in ("carton_entrada", "carton_cierre"):
        C.render_carton(TITULO, 119, C.BLANCO_FONDO, False,
                        "%s/C5U3_%s.mov" % (OUT, n), con_marca=True)
        print(n, "119 cuadros")
