# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2 de «Justicia restaurativa en la práctica del fiscal» (18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u2_inicio_fuente.mp4` (Drive del curso → VIDEOS, «Justica restaurativa-  Unidad 2 inicio.mp4»,
`15uZ6c_QyxX5PCDsW2ekmAdh75fs9z-Rz`, 228 MB): 1920×1080, 30 fps parejos, 36.408 cuadros (20:13,6), BT.601, pico de
−1,2 dBFS. Trae pegados la intro (cuadros 0–277) y el outro (desde el 36132; el 36130 y el 36131 son blancos); brillo
medido en los 36.408 cuadros: parejo en 188 del 278 al 36129. Entra del cuadro 280 al 36130.

**Qué es.** Dos mosaicos sobre blanco, como el inicio y el cierre del curso: Víctor Hugo Ospina Vargas a la izquierda
(x 38–940) y Jhonatan Sandoval, el profesor invitado, a la derecha (x 980–1880), los dos en y 286–794. Víctor
presenta la unidad (0:14,5 a 3:27,9), Jhonatan explica el enfoque restaurativo (3:29,0 a 11:21,9) y Víctor recorre
las lecciones de la unidad y cierra (11:24,0 a 20:02,1). STT (Scribe): 2.277 palabras. Sin reinicios ni pausas de
más de 2,5 s: **no se corta nada**.

**Nombre de la unidad.** Del PDF del curso del 10 de noviembre (`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`): «Aplicación
jurídica de la justicia restaurativa en el proceso penal».

**Lower thirds.** Los de dos mosaicos de la base (debajo de cada mosaico, en tinta azul). El de Víctor al empezar;
el de Jhonatan cuando Víctor lo presenta («nuestro invitado, el profesor Jhonatan Sandoval») y otra vez cuando toma
la palabra. Jhonatan no está en la ficha del curso: va el nombre solo, con la grafía que indicó Sebastián para el
inicio de la unidad 1 («Jhonatan Sandoval, sin cargo»). Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar, VICTOR, _LT  # noqa: E402

globals().update(armar('jr_u2_inicio_fuente.mp4', 'UNIDAD 2/INICIO',
                       'Unidad 2. Aplicación jurídica de la justicia restaurativa en el proceso penal',
                       'JR - U2 - INICIO', 'justiciarestaurativa - U2 - INICIO', 'JRU2I', 280, 36130))

JHONATAN = ('Jhonatan Sandoval', '', dict(_LT, x=1015))     # Sebastián, 18 nov: «Jhonatan Sandoval, sin cargo»

ITEMS = [
    ('lt01', 'lt', 15.5, 23.0, VICTOR),
    ('lt02', 'lt', 31.5, 39.0, JHONATAN),
    ('lt03', 'lt', 210.0, 217.5, JHONATAN),
]
