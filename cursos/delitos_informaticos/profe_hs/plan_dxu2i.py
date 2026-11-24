# -*- coding: utf-8 -*-
r"""Introducción de la unidad 2 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Introducción Unidad 2.mov`.

De «Bienvenido a la segunda unidad: el marco jurídico…» a «…Son muchas cosas, pero comencemos». Sale el «Listo.»
del principio (0,82 s), que es para el técnico.

**Sin rótulo (24 nov 2026):** el nombre del profe no está confirmado (ver `base_hs_profe`). La v2 va sin rótulo y
con «24NOV» en el nombre del archivo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu2i', 2, 'INICIO', 'Introducción Unidad 2.mov',
                              [(2.81, 163.26)]))

VERSION = 2
NOMBRE_LINEA = 'DI HS - U2 - INICIO v2'
ITEMS = rotulo(T0 + 1.5)  # noqa: F821   # vacío: sin rótulo
