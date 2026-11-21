# -*- coding: utf-8 -*-
r"""Retroalimentación de la evaluación de la unidad 5, «Tráfico de migrantes y trata de personas» (21 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `E:\DAE MASTER\CURSO INVESTIGACION Y JUDCIALIZACION\UNIDAD 5\Retroalimentación unidad 5..mp4` (del zip de la carpeta VIDEOS de Drive):
1080×1920 a 25 fps (avatar vertical); 390,4 s. El avatar se recorta y va sobre el fondo de la DAE (`recorta_persona.py`, ver la base): la
`ORIGINAL` del plan es el recortado. STT (Scribe, WAV a 16 kHz): 1005 palabras, de 0,86 a 389,56 s.

Retroalimentación: el avatar dice «de al unidad cinco» al empezar (el subtítulo dice «la»).

Entra de 0,36 a 390,36 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, PROFE  # noqa: E402,F401

globals().update(armar_unidad(5, 'RETROALIMENTACION', '.mp4', 0.36, 390.36, recortado=True))
RECORTE = dict(y=215, x=0, lado=1080)      # el cuadrado de la fuente que se recorta (del pelo al pecho)
FPS_FUENTE = 25
FPS_COMPUESTO = '25'

ITEMS = [
    ('lt01', 'lt', 1.9, 9.9, PROFE),
]
