#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de entrada y de cierre del C5U2: fondo blanco, con marca de agua."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c5u2"
os.makedirs(OUT, exist_ok=True)

TITULO = {"ante": "Caso", "titulo": "«El siniestro vial»"}

if __name__ == "__main__":
    for n in ("carton_entrada", "carton_cierre"):
        C.render_carton(TITULO, 119, C.BLANCO_FONDO, False,
                        "%s/C5U2_%s.mov" % (OUT, n), con_marca=True)
