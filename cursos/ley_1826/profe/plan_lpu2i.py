# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2, «Procedimiento: investigación, traslado, audiencia concentrada y juicio», de «Ley 1826 de
2017: procedimiento penal especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de bienvenida unidad
2-18/11/2026, 19:34.mp4» (`1kRltFKTglwIYHt6nnuaChBr6DY00CnU2`, 138.098.812 bytes): 1920×1080, 30 fps parejos, 9.574
cuadros (5:19,1), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la
base): la `ORIGINAL` del plan es el recortado. STT (Scribe): 724 palabras; la voz va de 8,00 a 317,40 s (medida en
el audio).

Entra del cuadro 225 (7,50 s: medio segundo antes de la primera palabra) al 9546 (318,20 s: 0,8 s después de la
última).

**Dos cortes**, los dos con `SUAVE = 3` (tres cuadros de mezcla; ver la base):
- «Examinaremos las vara— las variaciones en casos de captura en flagrancia» (1:58): salen los cuadros 3552 a
  3564 (118,40 a 118,83 s), «vara— las». Los dos puntos caen en el mismo sitio de la palabra, el valle entre
  «las» y «va…» (19,5 y 20,3 dB en la misma escala): queda «Examinaremos las variaciones». Diferencia de imagen
  en el corte: 3,0.
- «…participar en los foros de consulta y ava— avanzar con rigor» (5:11): salen los cuadros 9337 a 9346 (311,23
  a 311,57 s). La «y» va pegada a «ava—» (un solo golpe de voz de 311,18 a 311,45 s): por bandas, la «i» dura
  hasta 311,22 y la «a» empieza en 311,23; el corte sale ahí y entra en el arranque de «avanzar» (311,57).
  Diferencia de imagen: 2,1.

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE  # noqa: E402

globals().update(armar_unidad(2, 'INICIO', [(225, 3552), (3565, 9337), (9347, 9546)]))

SUAVE = 3            # cuadros de mezcla en cada corte (la ventana no cambia)

ITEMS = [
    ('lt01', 'lt', 9.2, 17.2, PROFE),
]
