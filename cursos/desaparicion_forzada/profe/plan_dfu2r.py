# -*- coding: utf-8 -*-
r"""Retroalimentación de evaluaciones de la unidad 2 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de retroalimentación de evaluaciones» de la unidad 2: las tres retroalimentaciones que grabó
el profe, una tras otra (actividad 1, actividad 2 y cuestionario sumativo). Entre una y otra se saca lo que dice
para marcar el video («Finaliza ese video y comienza el video de retroalimentación de la actividad dos»); los cortes
llevan seis cuadros de mezcla (`SUAVE`).

**Tramos de la fuente** (7:24.1 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:39:00.3 a 0:41:16.9 (136.6 s). Empieza «En este ejercicio encontramos un momento crítico…» (2340.78
  s; 5.86 s de silencio antes) y termina «…mecanismos de búsqueda en la actividad dos.» (2476.20 s; 3.40 s después).
- Tramo 2: 0:41:33.6 a 0:44:04.9 (151.3 s). Empieza «En este taller nos enfrentamos al desafío…» (2494.00 s; 6.26
  s de silencio antes) y termina «…de la unidad dos. Adelante con excelencia.» (2644.29 s; 1.20 s después).
- Tramo 3: 0:44:18.6 a 0:46:54.8 (156.2 s). Empieza «Apreciadas y apreciados participantes, felicitaciones por
  culminar…» (2659.09 s; 3.26 s de silencio antes) y termina «…y bienvenidos ahora a la unidad tres.» (2814.27 s;
  1.04 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(2, 'RETROALIMENTACION', [(2340.33, 2476.90), (2493.55, 2644.89), (2658.64, 2814.79)]))
SUAVE = 6

ITEMS = rotulo(T0)  # noqa: F821
