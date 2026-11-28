# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2, «Liderazgo y gestión del talento humano», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).

**Fuente.** `01 VIDEO/gj_u2c_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros 15196 a 19674 de esa
grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «La» y sale 0,8 s después de «mejorar.».

**2 cortes**:
- 8:47.2 de la grabación, «…continuidad de los servicios. [Tratar a todos igual no siempre garantiza la igualdad.] La idea más importante…»: salen los cuadros 619 a 769 de la fuente (5.03 s); energía en los bordes 42 y 46 dB bajo la voz; diferencia de imagen 4.1 (SUAVE).
- 9:32.6 de la grabación, «…su lector de pantalla, [la re--] la primera respuesta no…»: salen los cuadros 1981 a 2014 de la fuente (1.13 s); energía en los bordes 44 y 35 dB bajo la voz; diferencia de imagen 8.0 (plano cerrado después).



El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(2, 'CIERRE', [(45, 619), (770, 1981), (2015, 2111, CERRADO), (2111, 4427)]))

SUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano

ITEMS = [
    ('lt01', 'lt', 3.21, 11.21, PROFE),
]
