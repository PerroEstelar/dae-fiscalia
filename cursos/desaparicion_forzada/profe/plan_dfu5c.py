# -*- coding: utf-8 -*-
r"""Cierre de la unidad 5 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de cierre de la unidad 5» (lo que el profe llama «finalización y síntesis»). Va antes que las
retroalimentaciones en la grabación; en el aula va al final de la unidad.

**Tramos de la fuente** (3:28.0 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 1:30:24.7 a 1:33:52.7 (208.0 s). Empieza «Felicitaciones por haber completado la quinta unidad…»
  (5425.17 s; 7.74 s de silencio antes) y termina «…funciones misionales y hasta una próxima oportunidad.» (5632.04
  s; 1.46 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(5, 'CIERRE', [(5424.72, 5632.74)]))

ITEMS = rotulo(T0)  # noqa: F821
