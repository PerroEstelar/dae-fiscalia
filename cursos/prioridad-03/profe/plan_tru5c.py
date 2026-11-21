# -*- coding: utf-8 -*-
r"""Cierre de la unidad 5, «Tráfico de migrantes y trata de personas» (21 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `E:\DAE MASTER\CURSO INVESTIGACION Y JUDCIALIZACION\UNIDAD 5\Cierre de la Unidad 5.webm` (del zip de la carpeta VIDEOS de Drive):
1280×720, H.264 en WebM con cadencia variable, Opus mono; 464,6 s. STT (Scribe, WAV a 16 kHz): 977 palabras, de 3,62 a 461,84 s.

Sin tomas repetidas ni tropiezos. La presentadora es la de los cierres de las unidades 1 a 3, y termina la frase
(«…compatibles con el material probado»).

Entra de 3,12 a 462,64 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, PROFE_CIERRES  # noqa: E402,F401

globals().update(armar_unidad(5, 'CIERRE', '.webm', 3.12, 462.64))
XY, VENTANA = (0, 40), (1143, 643)
POR_TIEMPO = True       # cadencia variable: el video se corta por tiempo
FPS_FUENTE = 30

# El lower third espera el nombre de la presentadora (PROFE_CIERRES en la base).
ITEMS = [('lt01', 'lt', 4.6, 12.6, PROFE_CIERRES)] if PROFE_CIERRES else []
