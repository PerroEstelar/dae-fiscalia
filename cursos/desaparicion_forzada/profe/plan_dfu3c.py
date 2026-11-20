# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de cierre de la unidad 3» (lo que el profe llama «finalización y síntesis»). Va antes que las
retroalimentaciones en la grabación; en el aula va al final de la unidad.

**Tramos de la fuente** (3:39.8 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:53:51.7 a 0:57:31.5 (219.8 s). Empieza «Felicitaciones por haber completado con éxito la…» (3232.11
  s; 3.52 s de silencio antes) y termina «…seguir fortaleciendo nuestra labor humana y judicial.» (3450.82 s; 1.28 s
  después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(3, 'CIERRE', [(3231.66, 3451.46)]))

ITEMS = rotulo(T0)  # noqa: F821
