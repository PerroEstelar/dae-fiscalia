# -*- coding: utf-8 -*-
r"""Retroalimentación de evaluaciones de la unidad 5 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de retroalimentación de evaluaciones» de la unidad 5: las tres retroalimentaciones que grabó
el profe, una tras otra (actividad 1, actividad 2 y cuestionario sumativo). Entre una y otra se saca lo que dice
para marcar el video («Finaliza ese video y comienza el video de retroalimentación de la actividad dos»); los cortes
llevan seis cuadros de mezcla (`SUAVE`). Termina en «Felicitaciones a todas y todos por este gran logro profesional
e institucional».

**Tramos de la fuente** (6:39.8 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 1:34:03.7 a 1:36:24.9 (141.2 s). Empieza «En este primer taller de la unidad…» (5644.14 s; 3.32 s de
  silencio antes) y termina «…Sigamos adelante con la máxima precisión científica.» (5784.24 s; 1.40 s después).
- Tramo 2: 1:36:35.2 a 1:38:34.4 (119.3 s). Empieza «En esta actividad práctica consolidamos la hoja…» (5795.62 s;
  4.28 s de silencio antes) y termina «…Adelante hacia el cierre de nuestro curso.» (5913.74 s; 1.72 s después).
- Tramo 3: 1:38:44.3 a 1:41:03.6 (139.2 s). Empieza «En este video revisaremos los reactivos finales…» (5924.76 s;
  3.64 s de silencio antes) y termina «…por este gran logro profesional e institucional» (6062.86 s; 1.64 s
  después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(5, 'RETROALIMENTACION', [(5643.69, 5784.94), (5795.17, 5914.44), (5924.31, 6063.56)]))
SUAVE = 6

ITEMS = rotulo(T0)  # noqa: F821
