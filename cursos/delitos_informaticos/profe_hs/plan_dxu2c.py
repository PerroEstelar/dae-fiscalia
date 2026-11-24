# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Cierre Unidad 2.mov`.

De «Cerramos la segunda unidad dedicada al marco jurídico…» a «…Lo espero».

**Dos cortes** (bordes en silencio, −49 a −50 dB):
- 63,64–64,44: «castiga la instrusión-- la intrusión» queda «castiga la intrusión».
- 113,32–113,82: «obstaculización ileti-- ilegítima» queda «obstaculización ilegítima».

**Sin rótulo (24 nov 2026):** el nombre del profe no está confirmado (ver `base_hs_profe`). La v2 va sin rótulo y
con «24NOV» en el nombre del archivo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu2c', 2, 'CIERRE', 'Cierre Unidad 2.mov',
                              [(2.11, 63.64), (64.44, 113.32), (113.82, 172.1)]))

VERSION = 2
NOMBRE_LINEA = 'DI HS - U2 - CIERRE v2'
ITEMS = rotulo(T0 + 1.5)  # noqa: F821   # vacío: sin rótulo
