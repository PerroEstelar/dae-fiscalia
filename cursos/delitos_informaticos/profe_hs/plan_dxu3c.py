# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Cierre Unidad 3.mov`.

Entera: de «Terminamos la tercera unidad…» a «…Nos vemos».

**Sin rótulo (24 nov 2026):** el nombre del profe no está confirmado (ver `base_hs_profe`). La v2 va sin rótulo y
con «24NOV» en el nombre del archivo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu3c', 3, 'CIERRE', 'Cierre Unidad 3.mov',
                              [(1.65, 175.64)]))

VERSION = 2
NOMBRE_LINEA = 'DI HS - U3 - CIERRE v2'
ITEMS = rotulo(T0 + 1.5)  # noqa: F821   # vacío: sin rótulo
