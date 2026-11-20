# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de presentación de la unidad 2». Empieza en la bienvenida a la unidad y termina en la
despedida; lo que dice antes y después para marcar los videos («Finaliza ese video y comienza…») no entra. **Un
corte de 13,2 s:** al terminar la lección cuatro dice «Hasta ahí ese video. Viene el video… perdón, continúa este
video, continúa este video con el video anterior» y sigue con el capítulo dos del caso integrador; sale de 1911,19 a
1924,40. Seis cuadros de mezcla (`SUAVE`).

**Tramos de la fuente** (6:50.5 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:27:55.8 a 0:31:51.2 (235.4 s). Empieza «Reciban una cordial bienvenida a la unidad…» (1676.24 s; 5.64
  s de silencio antes) y termina «…de la Fiscalía General de la Nación.» (1910.49 s; 2.10 s después).
- Tramo 2: 0:32:04.4 a 0:34:59.5 (175.1 s). Empieza «En esta unidad aplicaremos los conocimientos al…» (1924.85 s;
  1.32 s de silencio antes) y termina «…esta unidad dos. Muchos éxitos y adelante.» (2099.05 s; 0.94 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(2, 'INICIO', [(1675.79, 1911.19), (1924.40, 2099.52)]))
SUAVE = 6

ITEMS = rotulo(T0)  # noqa: F821
