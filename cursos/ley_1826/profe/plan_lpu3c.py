# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3, «Acusador privado, conversión y reversión», de «Ley 1826 de 2017: procedimiento penal
especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de cierre unidad 3-18/11/2026,
20:38.mp4» (`1A2AEYpWLHGfvkj38EOur6mnpDdpYXFHI`, 146.037.160 bytes): 1920×1080, 30 fps parejos, 8.994 cuadros
(4:59,8), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe): 653 palabras; la voz va de 5,61 a 298,57 s (medida en el audio).

Entra del cuadro 153 (5,10 s: medio segundo antes de la primera palabra) al 8982 (299,40 s: 0,8 s después de la
última).

**Un corte**, con `SUAVE = 3` (ver la base): «…cuando existe imp— inimputabilidad» (2:01). Salen los cuadros
3632 a 3641 (121,07 a 121,40 s): del silencio que sigue a «existe» (−7 dB en 121,06, en la escala en que la voz
da 28) al silencio que precede a «inimputabilidad» (arranca en 121,43). Diferencia de imagen: 3,1.

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(3, 'CIERRE', [(153, 3632), (3642, 8982)]))

SUAVE = 3            # cuadros de mezcla en cada corte (la ventana no cambia)

ITEMS = [
    ('lt01', 'lt', 6.8, 14.8, PROFE),
]
