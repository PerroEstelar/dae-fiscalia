# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2 de «Terminaciones anticipadas» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver «Unidades» en `base_ta_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el
mismo compuesto.

**Fuente.** `ta_u2_inicio_fuente.mp4` (Drive del curso → VIDEOS › VIDEOS UNIDADES,
«Terminaciones Anticipadas Inicio U2 Juan-peña.mp4», `1NrX0ctZWC0yBQuDBCO6cXmqEQ9ZcobA7`, del 17 nov): 1920×1080, 30 fps
parejos, 13.821 cuadros (460,7 s). STT (Scribe, WAV a 16 kHz): 1.077 palabras, de 2,66 a 453,14 s, leído
de corrido y en una sola toma.

Entra del cuadro 65 (medio segundo antes de la primera palabra) al 13618 (0,8 s después de la
última). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ta_profe import *  # noqa: E402,F401,F403
from base_ta_profe import armar_unidad, PROFE, XY_UNIDADES, VENTANA_UNIDADES  # noqa: E402

XY, VENTANA = XY_UNIDADES, VENTANA_UNIDADES
MATRIZ_FUENTE = 'bt709'
PRESET_ENTREGA = 'medium'     # entrega provisional: x264 CRF 18 con preset medium (ver mp4_entrega); la v2 con gráficos vuelve a slow
globals().update(armar_unidad(2, 'INICIO', 65, 13618))

ITEMS = [
    ('lt01', 'lt', 3.7, 11.7, PROFE),
]
