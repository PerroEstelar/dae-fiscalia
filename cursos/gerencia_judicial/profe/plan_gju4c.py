# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4, «Articulación interinstitucional y territorial», de «Gerencia judicial» (27 nov 2026). **Entrega provisional** (ver `base_gj_profe`).

**Fuente.** `01 VIDEO/gj_u4c_fuente.mp4`, sacada de `00 FUENTES/VIDEO 3 … apertura y cierre.mp4` (cuadros 36153 a 40722 de esa
grabación; los tramos de abajo ya están en cuadros del _fuente). Entra medio segundo antes de «Cerramos» y sale 0,8 s después de «gracias.».

**2 cortes**:
- 21:04.6 de la grabación, «…inmediata" a otra dirección [con la que solo hay coordinación,] con la que solo…»: salen los cuadros 1785 a 1875 de la fuente (3.03 s); energía en los bordes 42 y 44 dB bajo la voz; diferencia de imagen 18.5 (plano cerrado después).
- 21:56.5 de la grabación, «…declare por su cuenta. [Diagnóstico de entrada versus respuesta final.] Vuelva ahora a sus…»: salen los cuadros 3343 a 3496 de la fuente (5.13 s); energía en los bordes 95 y 41 dB bajo la voz; diferencia de imagen 7.8 (plano cerrado después).

Termina en «Muchas gracias.»; después dice «Aquí terminamos», fuera de la pieza.

El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(4, 'CIERRE', [(45, 1785), (1876, 1983, CERRADO), (1983, 3343), (3497, 3620, CERRADO), (3620, 4517)]))

SUAVE = 3            # cuadros de mezcla en un corte sin cambio de plano

ITEMS = [
    ('lt01', 'lt', 3.21, 11.21, PROFE),
]
