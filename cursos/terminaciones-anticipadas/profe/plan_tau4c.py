# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4 de «Terminaciones anticipadas» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver «Unidades» en `base_ta_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el
mismo compuesto.

**Fuente.** `ta_u4_cierre_fuente.mp4` (Drive del curso → VIDEOS › VIDEOS UNIDADES,
«Terminaciones Anticipadas Cierre U4 Juan-Peña.mp4», `19-UrsK30dpMXe_kvyUrnlcXAdGMfNPcB`, del 17 nov): 1920×1080, 30 fps
parejos, 12.897 cuadros (429,9 s). STT (Scribe, WAV a 16 kHz): 1.005 palabras, de 2,62 a 423,74 s, leído
de corrido, **con una repetición** que la primera entrega dejó adentro (ver «Versión 2»).

Entra del cuadro 64 (medio segundo antes de la primera palabra) al 12736 (0,8 s después de la
última). Los tiempos están en segundos de la fuente.

**Versión 2 (18 nov 2026): la repetición, cortada.** Al leer la transcripción para los subtítulos apareció
el arranque en falso «…pero también plantarles--» (17,1 a 26,2 s de la v1); el video arranca en el segundo
«Llegamos al cierre». La `-v2` se hizo sobre el MP4 de la `-v1`, sin reprocesar: `recortar_entrega.py
plan_tau4c 1 2 409 628 lt=lt01 limpios=8` quita los cuadros 409–628 de la línea (219 cuadros, 9,1 s; de
10945 a 10726 cuadros). Las constantes de abajo siguen siendo las de la v1 (el compuesto y la línea de
Resolve conservan la toma completa): para una versión con gráficos, o se corta con la misma herramienta la
entrega nueva, o se rearma con `armar_unidad(…, 338, 12736)` (la fuente entra desde el cuadro 338) y el
lower third 9,1 s más tarde en tiempo de fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ta_profe import *  # noqa: E402,F401,F403
from base_ta_profe import armar_unidad, PROFE, XY_UNIDADES, VENTANA_UNIDADES  # noqa: E402

XY, VENTANA = XY_UNIDADES, VENTANA_UNIDADES
MATRIZ_FUENTE = 'bt709'
PRESET_ENTREGA = 'medium'     # entrega provisional: x264 CRF 18 con preset medium (ver mp4_entrega); la v2 con gráficos vuelve a slow
globals().update(armar_unidad(4, 'CIERRE', 64, 12736))

CORTE_V2 = (409, 628)      # cuadros de la línea de la v1 que la v2 no tiene (ver «Versión 2»)

ITEMS = [
    ('lt01', 'lt', 3.6, 11.6, PROFE),
]
