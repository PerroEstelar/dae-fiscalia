# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de presentación de la unidad 4». Empieza en la bienvenida a la unidad y termina en la
despedida; lo que dice antes y después para marcar los videos («Finaliza ese video y comienza…») no entra.

**Tramos de la fuente** (6:35.0 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 1:05:30.4 a 1:12:05.5 (395.0 s). Empieza «Reciban una cordial bienvenida a la unidad…» (3930.87 s; 3.64
  s de silencio antes) y termina «…la función pública. Muchos éxitos y adelante.» (4324.76 s; 2.18 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(4, 'INICIO', [(3930.42, 4325.46)]))

ITEMS = rotulo(T0)  # noqa: F821
