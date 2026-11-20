# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de cierre de la unidad 2» (lo que el profe llama «finalización y síntesis»). Va antes que las
retroalimentaciones en la grabación; en el aula va al final de la unidad.

**Tramos de la fuente** (3:39.3 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:35:09.7 a 0:38:49.0 (219.3 s). Empieza «Felicitaciones por haber concluido los contenidos de…»
  (2110.19 s; 4.78 s de silencio antes) y termina «…para fortalecer el trabajo en equipo interdisciplinario.»
  (2328.32 s; 1.56 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(2, 'CIERRE', [(2109.74, 2329.02)]))

ITEMS = rotulo(T0)  # noqa: F821
