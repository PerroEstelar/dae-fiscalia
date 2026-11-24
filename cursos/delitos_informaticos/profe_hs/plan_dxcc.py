# -*- coding: utf-8 -*-
r"""Cierre del curso de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Cierre del Curso.mov`.

Entera: de «Hemos llegado al final del curso…» a «…Hasta luego».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_curso('dxcc', 'CIERRE', 'Cierre del curso', 'Cierre del Curso.mov',
                             [(1.51, 161.1)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
