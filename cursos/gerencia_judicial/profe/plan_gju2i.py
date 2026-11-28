# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2, «Liderazgo y gestión del talento humano», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).

**Fuente.** `01 VIDEO/gj_u2i_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros 10384 a 14841 de esa
grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «Bienvenidos» y sale 0,8 s después de «segunda.».

**1 cortes**:
- 6:57.2 de la grabación, «…a los objetivos institucionales. [Las cinco lecciones.] Recordemos cinco lecciones. La…»: salen los cuadros 2131 a 2182 de la fuente (1.73 s); energía en los bordes 45 y 42 dB bajo la voz; diferencia de imagen 14.1 (plano cerrado después).

Se deja «a las disposiciones— a la disposición» (el borde de salida queda en la «s» de «adaptarlos»).

El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(2, 'INICIO', [(45, 2131), (2183, 2272, CERRADO), (2272, 4406)]))

SUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano

ITEMS = [
    ('lt01', 'lt', 3.21, 11.21, PROFE),
]
