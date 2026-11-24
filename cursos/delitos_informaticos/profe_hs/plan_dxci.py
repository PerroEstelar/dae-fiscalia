# -*- coding: utf-8 -*-
r"""Presentación del curso de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Bienvenida al Curso.mov`.

De «Bienvenido al curso de profundización en delitos informáticos…» a «…bienvenido y comencemos».

**Dos cortes:**
- 93,07–93,78: «el Convenio de Buda- de Budapest» queda «el Convenio de Budapest» (sale «de Buda-» y la pausa; bordes
  en el bache entre «Convenio» y «de», −48 dB, y en el silencio antes del segundo «de», −50 dB).
- 165,08–165,44: sale «su--» en «vuelve su-- sobre su decisión» (los bordes en el bache entre «vuelve» y el titubeo,
  −44 dB, y en el silencio antes de «sobre», −51 dB).

**v2 (24 nov 2026):** la v1 tenía solo el segundo corte; «Buda-» se oyó al revisar los subtítulos.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_curso('dxci', 'INICIO', 'Inicio del curso', 'Bienvenida al Curso.mov',
                             [(1.81, 93.07), (93.78, 165.08), (165.44, 215.08)]))

VERSION = 2
COMPUESTO = R + '/01 VIDEO/DXCI_compuesto_v2.mp4'  # noqa: F821
NOMBRE_LINEA = 'DI HS - CURSO - INICIO v2'

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
