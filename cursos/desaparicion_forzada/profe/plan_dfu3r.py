# -*- coding: utf-8 -*-
r"""Retroalimentación de evaluaciones de la unidad 3 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de retroalimentación de evaluaciones» de la unidad 3: las tres retroalimentaciones que grabó
el profe, una tras otra (actividad 1, actividad 2 y cuestionario sumativo). Entre una y otra se saca lo que dice
para marcar el video («Finaliza ese video y comienza el video de retroalimentación de la actividad dos»); los cortes
llevan seis cuadros de mezcla (`SUAVE`).

**Tramos de la fuente** (7:10.8 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:57:44.6 a 1:00:09.5 (144.9 s). Empieza «En este ejercicio realizamos el mapeo interactivo…» (3465.02
  s; 6.54 s de silencio antes) y termina «…la actividad dos. Seguimos adelante con excelencia.» (3608.90 s; 1.22 s
  después).
- Tramo 2: 1:00:21.4 a 1:02:38.3 (136.9 s). Empieza «En esta actividad abordamos un problema recurrente…» (3621.82
  s; 5.94 s de silencio antes) y termina «…tres. Sigamos adelante con rigor y responsabilidad.» (3757.59 s; 1.62 s
  después).
- Tramo 3: 1:02:51.9 a 1:05:20.8 (148.9 s). Empieza «En este video revisaremos las preguntas fundamentales…»
  (3772.33 s; 4.48 s de silencio antes) y termina «…todas. Bienvenidos ahora a la unidad cuatro.» (3920.11 s; 1.60 s
  después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(3, 'RETROALIMENTACION', [(3464.57, 3609.51), (3621.37, 3758.29), (3771.88, 3920.81)]))
SUAVE = 6

ITEMS = rotulo(T0)  # noqa: F821
