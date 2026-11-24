# -*- coding: utf-8 -*-
r"""Introducción de la unidad 4 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Introduccion Unidad 4.mov`.

Entera: de «Bienvenido a la cuarta y última unidad…» a «…Ahora sí, comencemos».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu4i', 4, 'INICIO', 'Introduccion Unidad 4.mov',
                              [(4.13, 175.96)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
