# -*- coding: utf-8 -*-
r"""Presentación del curso de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Bienvenida al Curso.mov`.

De «Bienvenido al curso de profundización en delitos informáticos…» a «…bienvenido y comencemos».

**Un corte:** sale «su--» en «vuelve su-- sobre su decisión» (165,08–165,44; los bordes en el bache entre
«vuelve» y el titubeo, −44 dB, y en el silencio antes de «sobre», −51 dB).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_curso('dxci', 'INICIO', 'Inicio del curso', 'Bienvenida al Curso.mov',
                             [(1.81, 165.08), (165.44, 215.08)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
