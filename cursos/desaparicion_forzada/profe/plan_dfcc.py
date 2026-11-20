# -*- coding: utf-8 -*-
r"""Cierre del curso de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de cierre del curso» (la «finalización y síntesis general del curso»). Dura más que los 5 a 8
minutos que da la ficha: es lo que el profe grabó y no se recorta contenido. **Un corte de 6,1 s:** «Toda noticia de
desaparición activa de inmediato. Toda denuncia, perdónenme, eh, eh, de desaparición, activa de inmediato el formato
FUPD…» queda «Toda noticia de desaparición, | activa de inmediato el formato FUPD…»: sale de 6879,76 (en el silencio
de 0,1 s entre «desaparición» y «activa», medido en RMS de 10 ms: −88 dB) a 6885,84 (silencio de 0,2 s antes del
segundo «activa», −89 dB). Tres cuadros de mezcla (`SUAVE`).

**Tramos de la fuente** (15:15.1 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 1:41:34.9 a 1:54:39.8 (784.9 s). Empieza «Apreciadas y apreciados estudiantes, en nombre de…» (6095.32
  s; 4.28 s de silencio antes) y termina «…Toda noticia de desaparición activa de inmediato.» (6881.13 s; 1.24 s
  después).
- Tramo 2: 1:54:45.8 a 1:56:56.0 (130.2 s). Empieza «el formato FUPD, el Registro Nacional de…» (6887.13 s; 0.04 s
  de silencio antes) y termina «…su compromiso y hasta una próxima oportunidad.» (7015.33 s; 2.22 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar('CURSO/CIERRE', 'Cierre del curso', 'DF - CURSO - CIERRE', 'desaparicionforzada - CURSO - CIERRE', 'DFCC',
                       [(6094.87, 6879.76), (6885.84, 7016.03)]))
SUAVE = 3

ITEMS = rotulo(T0)  # noqa: F821
