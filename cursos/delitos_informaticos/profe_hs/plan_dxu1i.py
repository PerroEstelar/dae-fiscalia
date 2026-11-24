# -*- coding: utf-8 -*-
r"""Introducción de la unidad 1 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Introducción Unidad 1.mov`.

Entera: de «Bienvenido a la primera unidad del curso…» a «…Empecemos».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu1i', 1, 'INICIO', 'Introducción Unidad 1.mov',
                              [(3.97, 179.26)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
