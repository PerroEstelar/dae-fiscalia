# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4, «Tráfico de migrantes y trata de personas» (21 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(ver `base_tr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `E:\DAE MASTER\CURSO INVESTIGACION Y JUDCIALIZACION\UNIDAD 4\Cierre de la Unidad 4.webm` (del zip de la carpeta VIDEOS de Drive):
1280×720, H.264 en WebM con cadencia variable, Opus mono; 463,7 s. STT (Scribe, WAV a 16 kHz): 956 palabras, de 2,54 a 460,92 s.

Sin tomas repetidas ni tropiezos (la pausa más larga, 1,6 s en 321,4 s, va entre dos frases). La presentadora es la
de los cierres de las unidades 1 a 3, y termina la frase («…carece de vía de incorporación»).

Entra de 2,04 a 461,72 s: medio segundo antes de la primera palabra y hasta 0,8 s después de la última
(o hasta el final del archivo). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_tr_profe import *  # noqa: E402,F401,F403
from base_tr_profe import armar_curso, armar_unidad, PROFE_CIERRES  # noqa: E402,F401

globals().update(armar_unidad(4, 'CIERRE', '.webm', 2.04, 461.72))
XY, VENTANA = (0, 40), (1143, 643)
POR_TIEMPO = True       # cadencia variable: el video se corta por tiempo
FPS_FUENTE = 30

# v2 (21 nov 2026): con el rótulo de la presentadora, que Sebastián confirmó (PROFE_CIERRES en la base). La v1 iba
# sin rótulo; mismo compuesto.
VERSION = 2
ITEMS = [('lt01', 'lt', 3.5, 11.5, PROFE_CIERRES)] if PROFE_CIERRES else []
