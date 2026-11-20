# -*- coding: utf-8 -*-
r"""Inicio de la unidad 5 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de presentación de la unidad 5». Empieza en la bienvenida a la unidad y termina en la
despedida; lo que dice antes y después para marcar los videos («Finaliza ese video y comienza…») no entra. **Un
corte de 3,6 s:** «le sugerimos revisar la atención— con mucha atención, excúsenme, la guía de análisis de
contexto…» queda «le sugerimos revisar | la guía de análisis de contexto…». Sale de 5359,16 (silencio de 20 ms entre
«revisar» y «la», −69 dB en RMS de 10 ms) a 5362,80 (silencio antes de «la guía», −90 dB). Tres cuadros de mezcla
(`SUAVE`). Dice «cinco lecciones»; la ficha de la unidad 5 trae siete: es lo que grabó el profe.

**Tramos de la fuente** (6:28.7 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 1:23:36.8 a 1:29:19.2 (342.4 s). Empieza «Reciban una cordial bienvenida a la quinta…» (5017.22 s; 5.58
  s de silencio antes) y termina «…recomendación final de estudio, le sugerimos revisar» (5358.93 s; 0.06 s
  después).
- Tramo 2: 1:29:22.8 a 1:30:09.1 (46.3 s). Empieza «la guía de análisis de contexto de…» (5363.09 s; 0.58 s de
  silencio antes) y termina «…felicitaciones por culminar este proceso de formación.» (5408.55 s; 1.16 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(5, 'INICIO', [(5016.77, 5359.16), (5362.80, 5409.13)]))
SUAVE = 3

ITEMS = rotulo(T0)  # noqa: F821
