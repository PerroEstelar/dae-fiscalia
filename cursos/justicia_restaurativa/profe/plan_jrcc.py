# -*- coding: utf-8 -*-
r"""Cierre del curso «Justicia restaurativa en la práctica del fiscal» (18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, tres lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_cierre_curso_fuente.mp4` (Drive del curso → VIDEOS, «Justica restuaraativa-  Cierre curso.mp4»,
`1dGNePRbK98Td0Q45F07m7tKQzZkp1IRv`, del 18 nov): 1920×1080, 30 fps parejos, 80.225 cuadros (44:34,2), pico de
−1,3 dBFS. Los cuadros 0–277 son una intro de la FGN pegada y desde el 79949 hay un outro (79947 y 79948 son
blancos): no entran.

**Qué es.** Una conversación de cierre entre los dos coautores, sin guion leído. Habla Víctor Hugo Ospina Vargas
(mosaico izquierdo) de 0:09,6 a 5:35; Martín Posada Martínez (mosaico derecho) de 5:37,7 a 23:09, con un «Adelante,
profesor» de Víctor en 21:04; y cierra Víctor de 23:11 a 44:24. STT (Scribe): 4.518 palabras.

**Sin cortes.** Se leyó la transcripción entera buscando reinicios («repito», «volver a empezar», «perdón», «corte»,
frases repetidas, pausas): no hay ninguno. Hay tropiezos de quien habla sin leer («llegamos al-- llegaron al
final», «La grav-- bueno, ahí no se ve muy bien») y diez pausas de 2,5 a 3,7 s, que se dejan.

Entra del cuadro 280 (el profe empieza en el 278; primera palabra en 9,62 s) al 79947 (0,8 s después de la última
palabra, que termina en 2664,10 s, y justo antes del blanco). Los tiempos están en segundos de la fuente.

**Lower thirds.** Uno por persona al principio, uno tras otro (están los dos en pantalla desde el primer cuadro), y
el de Martín otra vez cuando toma la palabra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar, VICTOR, MARTIN  # noqa: E402

globals().update(armar('jr_cierre_curso_fuente.mp4', 'CIERRE DEL CURSO', 'Cierre del curso', 'JR - CURSO - CIERRE',
                       'justiciarestaurativa - CURSO - CIERRE', 'JRCC', 280, 79947))

ITEMS = [
    ('lt01', 'lt', 11.0, 18.5, VICTOR),
    ('lt02', 'lt', 19.2, 26.7, MARTIN),
    ('lt03', 'lt', 338.6, 346.6, MARTIN),
]
