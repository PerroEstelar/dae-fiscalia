# -*- coding: utf-8 -*-
r"""Retroalimentación de evaluaciones de la unidad 4 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de retroalimentación de evaluaciones» de la unidad 4: las tres retroalimentaciones que grabó
el profe, una tras otra (actividad 1, actividad 2 y cuestionario sumativo). Entre una y otra se saca lo que dice
para marcar el video («Finaliza ese video y comienza el video de retroalimentación de la actividad dos»); los cortes
llevan seis cuadros de mezcla (`SUAVE`).

**Tramos de la fuente** (6:45.2 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 1:16:15.6 a 1:18:28.8 (133.2 s). Empieza «En este ejercicio de encontrar abordamos un…» (4576.08 s;
  4.74 s de silencio antes) y termina «…Seguimos adelante con rigor y sensibilidad humana.» (4708.32 s; 1.00 s
  después).
- Tramo 2: 1:18:39.8 a 1:20:53.5 (133.7 s). Empieza «En este ejercicio abordamos una de las…» (4720.24 s; 4.46 s
  de silencio antes) y termina «…justicia y la dignidad de las víctimas.» (4852.80 s; 1.38 s después).
- Tramo 3: 1:21:06.6 a 1:23:24.9 (138.3 s). Empieza «En este video revisaremos los reactivos fundamentales…»
  (4867.02 s; 4.00 s de silencio antes) y termina «…todos y bienvenidos a la unidad cinco.» (5004.22 s; 1.34 s
  después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(4, 'RETROALIMENTACION', [(4575.63, 4708.82), (4719.79, 4853.49), (4866.57, 5004.89)]))
SUAVE = 6

ITEMS = rotulo(T0)  # noqa: F821
