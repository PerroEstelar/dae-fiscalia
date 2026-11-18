# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2 de «Terminaciones anticipadas» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver «Unidades» en `base_ta_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el
mismo compuesto.

**Fuente.** `ta_u2_inicio_fuente.mp4` (Drive del curso → VIDEOS › VIDEOS UNIDADES,
«Terminaciones Anticipadas Inicio U2 Juan-peña.mp4», `1NrX0ctZWC0yBQuDBCO6cXmqEQ9ZcobA7`, del 17 nov): 1920×1080, 30 fps
parejos, 13.821 cuadros (460,7 s). STT (Scribe, WAV a 16 kHz): 1.077 palabras, de 2,66 a 453,14 s, leído
de corrido, **con una repetición** que la primera entrega dejó adentro (ver «Versión 2»).

Entra del cuadro 65 (medio segundo antes de la primera palabra) al 13618 (0,8 s después de la
última). Los tiempos están en segundos de la fuente.

**Versión 2 (18 nov 2026): la repetición, cortada.** Al leer la transcripción para los subtítulos apareció
la primera toma, que se corta en «la convicci--, ah, voy a volver a empezar» (17,6 a 45,7 s de la v1); el
video arranca en la segunda. La `-v2` se hizo sobre el MP4 de la `-v1`, sin reprocesar: `recortar_entrega.py
plan_tau2i 1 2 409 1129 lt=lt01` quita los cuadros 409–1129 de la línea (720 cuadros, 30,0 s; de 11649 a
10929 cuadros). Las constantes de abajo siguen siendo las de la v1 (el compuesto y la línea de Resolve
conservan la toma completa): para una versión con gráficos, o se corta con la misma herramienta la entrega
nueva, o se rearma con `armar_unidad(…, 965, 13618)` (la fuente entra desde el cuadro 965) y el lower third
30,0 s más tarde en tiempo de fuente.
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

CORTE_V2 = (409, 1129)      # cuadros de la línea de la v1 que la v2 no tiene (ver «Versión 2»)

ITEMS = [
    ('lt01', 'lt', 3.7, 11.7, PROFE),
]
