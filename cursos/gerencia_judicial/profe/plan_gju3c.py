# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3, «Gestión de servicios, planeación y seguimiento», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).

**Fuente.** `01 VIDEO/gj_u3c_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros 25787 a 30375 de esa
grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «Cerramos» y sale 0,8 s después de «resultados.».

**3 cortes**:
- 14:40.5 de la grabación, «…decisión me permite tomar? [La vel--] la evaluación del desempeño…»: salen los cuadros 628 a 654 de la fuente (0.90 s); energía en los bordes 44 y 46 dB bajo la voz; diferencia de imagen 12.5 (plano cerrado después).
- 15:24.9 de la grabación, «…complejos". Precisa qué, cuándo, [en qué,] en qué plazo y…»: salen los cuadros 1959 a 1991 de la fuente (1.10 s); energía en los bordes 47 y 45 dB bajo la voz; diferencia de imagen 7.7 (plano cerrado después).
- 16:14.0 de la grabación, «…por su cuenta propia. [Tres indicadores para mi tablero.] Si en la evaluación…»: salen los cuadros 3432 a 3500 de la fuente (2.30 s); energía en los bordes 46 y 44 dB bajo la voz; diferencia de imagen 6.7 (plano cerrado después).

**Para revisar:** «Un buen objetivo en clave de Drucker nos dice: "Mejoraremos la investigación de delitos complejos"» queda como se oye.

El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(3, 'CIERRE', [(46, 628), (655, 797, CERRADO), (797, 1959), (1992, 2073, CERRADO), (2073, 3432), (3501, 3631, CERRADO), (3631, 4537)]))

SUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano

ITEMS = [
    ('lt01', 'lt', 3.23, 11.23, PROFE),
]
