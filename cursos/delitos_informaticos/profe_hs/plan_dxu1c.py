# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Cierre Unidad 1.mov`.

De «Llegamos al cierre de la primera unidad…» a «…Nos vemos allá».

**Un corte:** sale «a--» en «pasamos a-- de comprender a tipificar» (152,60–153,22, los dos bordes en silencio,
−47 y −49 dB).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu1c', 1, 'CIERRE', 'Cierre Unidad 1.mov',
                              [(2.29, 152.6), (153.22, 157.04)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
