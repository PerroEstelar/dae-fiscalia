# -*- coding: utf-8 -*-
r"""Inicio del curso de «Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado» (19 nov 2026).
**Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de INTRODUCCIÓN 1826-18/11/2026,
18:00.mp4» (`1x6FgzAQThWgv8RBt75PvEP-xUEcMnN0m`, 211.817.617 bytes): 1920×1080, 30 fps parejos, 12.814 cuadros
(7:07,2), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe): 892 palabras; la voz va de 11,77 a 424,81 s (medida en el audio).

Entra del cuadro 338 (11,27 s: medio segundo antes de la primera palabra) al 12769 (425,63 s: 0,8 s después de la
última).

**Qué se deja.** «…contribuirán a, a una justicia penal más pronta» (6:58): la «a» repetida va pegada a
«contribuirán» y a «una», sin un valle donde cortar. En 0:38,6 dice su nombre y su formación: de ahí sale el
cargo del lower third (ver la base).

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_curso, PROFE  # noqa: E402

globals().update(armar_curso('INICIO', [(338, 12769)]))

ITEMS = [
    ('lt01', 'lt', 13.0, 21.0, PROFE),
]
