# -*- coding: utf-8 -*-
r"""Retroalimentación de evaluaciones de la unidad 1 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de retroalimentación de evaluaciones» de la unidad 1: las tres retroalimentaciones que grabó
el profe, una tras otra (actividad 1, actividad 2 y cuestionario sumativo). Entre una y otra se saca lo que dice
para marcar el video («Finaliza ese video y comienza el video de retroalimentación de la actividad dos»); los cortes
llevan seis cuadros de mezcla (`SUAVE`). En la actividad 2 el profe lee primero el rótulo del guion («Introducción
al taller.»): no entra.

**Tramos de la fuente** (8:14.4 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:18:55.9 a 0:21:50.0 (174.1 s). Empieza «Apreciadas y apreciados estudiantes, tras revisar sus…»
  (1136.35 s; 5.02 s de silencio antes) y termina «…adelante con excelencia en la investigación judicial.» (1309.27
  s; 2.46 s después).
- Tramo 2: 0:22:09.5 a 0:24:46.6 (157.0 s). Empieza «En esta actividad abordamos el desafío metodológico…»
  (1329.95 s; 0.86 s de silencio antes) y termina «…con rigor y compromiso por la verdad.» (1486.00 s; 1.14 s
  después).
- Tramo 3: 0:25:02.4 a 0:27:45.7 (163.3 s). Empieza «Apreciados participantes, felicitaciones por culminar la
  evaluación…» (1502.86 s; 4.28 s de silencio antes) y termina «…todos y bienvenidos a la unidad dos.» (1665.20 s;
  0.94 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(1, 'RETROALIMENTACION', [(1135.90, 1309.97), (1329.52, 1486.57), (1502.41, 1665.67)]))
SUAVE = 6

ITEMS = rotulo(T0)  # noqa: F821
