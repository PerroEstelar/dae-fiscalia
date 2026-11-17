# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3 de «Terminaciones anticipadas» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver «Unidades» en `base_ta_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el
mismo compuesto.

**Fuente.** `ta_u3_cierre_fuente.mp4` (Drive del curso → VIDEOS › VIDEOS UNIDADES,
«Terminaciones Anticipadas Cierre U3 Juan-Peña.mp4», `1fvV_FmNhgKNSlVSMwrgw1KIUdpdDs4g3`, del 17 nov): 1920×1080, 30 fps
parejos, 11.223 cuadros (374,1 s). STT (Scribe, WAV a 16 kHz): 874 palabras, de 3,26 a 367,12 s, leído
de corrido y en una sola toma.

Entra del cuadro 83 (medio segundo antes de la primera palabra) al 11038 (0,8 s después de la
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
globals().update(armar_unidad(3, 'CIERRE', 83, 11038))

ITEMS = [
    ('lt01', 'lt', 4.3, 12.3, PROFE),
]
