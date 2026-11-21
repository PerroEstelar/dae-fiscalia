# -*- coding: utf-8 -*-
r"""Introducción de la unidad 4, «Tráfico de migrantes y trata de personas» (21 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `E:\DAE MASTER\CURSO INVESTIGACION Y JUDCIALIZACION\UNIDAD 4\Introducción a la Unidad 4.mp4` (del zip de la carpeta VIDEOS de Drive):
1080×1920 a 25 fps (avatar vertical); 395,6 s. El avatar se recorta y va sobre el fondo de la DAE (`recorta_persona.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe, WAV a 16 kHz): 1009 palabras, de 0,88 a 394,78 s.

Entra de 0,38 a 395,58 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, PROFE  # noqa: E402,F401

globals().update(armar_unidad(4, 'INICIO', '.mp4', 0.38, 395.58, recortado=True))
RECORTE = dict(y=230, x=0, lado=1080)      # el cuadrado de la fuente que se recorta (del pelo al pecho)
FPS_FUENTE = 25
FPS_COMPUESTO = '25'

ITEMS = [
    ('lt01', 'lt', 1.9, 9.9, PROFE),
]
