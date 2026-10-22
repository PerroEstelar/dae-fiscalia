#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de entrada y de cierre del PRIORIDAD 03 · Caso 4."""
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

OUT = "/home/claude/p3c4/cartones/out"
os.makedirs(OUT, exist_ok=True)

TITULO = {"ante": "Caso", "titulo": "«Puerto de salida»"}

if __name__ == "__main__":
    for n in ("carton_entrada", "carton_cierre"):
        C.render_carton(TITULO, 119, C.BLANCO_FONDO, False,
                        "%s/P3C4_%s.mov" % (OUT, n), con_marca=True)
        print(n, "119 cuadros")
