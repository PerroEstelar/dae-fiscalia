# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Terminaciones anticipadas» (17 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver «Unidades» en `base_ta_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el
mismo compuesto.

**Fuente.** `ta_u4_inicio_fuente.mp4` (Drive del curso → VIDEOS › VIDEOS UNIDADES,
«Terminaciones Anticipadas Inicio U4 Juan Peña.mp4», `1vgGm-htgbmrtefXO99s5UPNPeS8dMQwe`, del 17 nov): 1920×1080, 30 fps
parejos, 14.300 cuadros (476,7 s). STT (Scribe, WAV a 16 kHz): 1.098 palabras, de 4,46 a 471,14 s, leído
de corrido, **con una repetición** que la primera entrega dejó adentro (ver «Versión 2»).

Entra del cuadro 119 (medio segundo antes de la primera palabra) al 14158 (0,8 s después de la
última). Los tiempos están en segundos de la fuente.

**Versión 2 (18 nov 2026): la repetición, cortada.** Al leer la transcripción para los subtítulos apareció
el párrafo que empieza en «Conviene comenzar por una distinción» y termina en «volver a hacer ese párrafo»
(55,1 a 88,2 s de la v1); queda la segunda lectura, con un corte directo en 0:55. La `-v2` se hizo sobre el
MP4 de la `-v1`, sin reprocesar: `recortar_entrega.py plan_tau4i 1 2 1321 2115` quita los cuadros 1321–2115
de la línea (794 cuadros, 33,1 s; de 12037 a 11243 cuadros). Las constantes de abajo siguen siendo las de la
v1 (el compuesto y la línea de Resolve conservan la toma completa): para una versión con gráficos, o se
corta con la misma herramienta la entrega nueva, o se rearma con dos tramos de fuente, `TRAMOS = [(119 / 30,
1260 / 30, None), (2253 / 30, 14158 / 30, None)]`.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ta_profe import *  # noqa: E402,F401,F403
from base_ta_profe import armar_unidad, PROFE, XY_UNIDADES, VENTANA_UNIDADES  # noqa: E402

XY, VENTANA = XY_UNIDADES, VENTANA_UNIDADES
MATRIZ_FUENTE = 'bt709'
PRESET_ENTREGA = 'medium'     # entrega provisional: x264 CRF 18 con preset medium (ver mp4_entrega); la v2 con gráficos vuelve a slow
globals().update(armar_unidad(4, 'INICIO', 119, 14158))

CORTE_V2 = (1321, 2115)      # cuadros de la línea de la v1 que la v2 no tiene (ver «Versión 2»)

ITEMS = [
    ('lt01', 'lt', 5.5, 13.5, PROFE),
]
