# -*- coding: utf-8 -*-
r"""Inicio de la unidad 1 de «Justicia restaurativa en la práctica del fiscal» (18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u1_inicio_fuente.mp4` (Drive del curso → VIDEOS, `1dqkWwz5aokHQV2ECPAvmvXv8aYCI9FFI`, 151 MB):
1920×1080, 30 fps parejos, 36.117 cuadros (20:03,9), BT.601, pico de −0,9 dBFS. **Solo los primeros 8 minutos tienen
contenido**: intro pegada (cuadros 0–277), la conversación (278–14418), dos cuadros blancos (14419 y 14420), el outro,
y después negro hasta el final del archivo. Entra del cuadro 280 al 14419 (la última palabra termina en 479,74 s;
0,9 s después empieza el blanco).

**Qué es.** Tres personas en tres mosaicos de videollamada sobre blanco: arriba a la izquierda Martín Posada Martínez
(x 38–940, y 22–528), arriba a la derecha un tercer profesor (x 979–1881, y 22–528) y abajo al centro Víctor Hugo
Ospina Vargas (x 509–1410, y 551–1057). Víctor presenta la unidad y pregunta (0:09,5 a 1:02); responde el tercer
profesor (1:02,5 a 4:32,6), después Martín (4:34,9 a 6:03,4) y cierra Víctor (6:05,9 a 8:00). STT (Scribe): 1.025
palabras. Sin reinicios ni pausas de más de 2,8 s: no se corta nada.

**Nombre de la unidad.** Del PDF del curso del 10 de noviembre (`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`, 3.1): «Bases
conceptuales y marco jurídico de la justicia restaurativa».

**Lower thirds.** En tinta azul sobre el blanco, como en el cierre, pero aquí el blanco libre está abajo a los lados:
el de Martín va bajo su mosaico (abajo a la izquierda, arriba), el del tercer profesor bajo el suyo (abajo a la
derecha) y el de Víctor a la izquierda de su mosaico (abajo a la izquierda, más abajo). Cada uno sale cuando esa
persona empieza a hablar. **El tercer profesor:** Víctor lo presenta como «el profesor Jhonatan Sandoval» (así lo
oye Scribe); no está en la ficha del curso, así que la grafía y el cargo se le preguntaron a Sebastián (`TERCERO`).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar, VICTOR, MARTIN, TINTA_LT  # noqa: E402

globals().update(armar('jr_u1_inicio_fuente.mp4', 'UNIDAD 1/INICIO',
                       'Unidad 1. Bases conceptuales y marco jurídico de la justicia restaurativa',
                       'JR - U1 - INICIO', 'justiciarestaurativa - U1 - INICIO', 'JRU1I', 280, 14419))

_LTU = dict(ancho=430, tinta=TINTA_LT)
VICTOR_U = (VICTOR[0], VICTOR[1], dict(_LTU, x=40, top=820))
MARTIN_U = (MARTIN[0], MARTIN[1], dict(_LTU, x=40, top=575))
TERCERO = None      # (nombre, cargo): pendiente de Sebastián

ITEMS = [
    ('lt01', 'lt', 11.0, 18.5, VICTOR_U),
    ('lt03', 'lt', 275.9, 283.4, MARTIN_U),
]
if TERCERO:
    ITEMS.insert(1, ('lt02', 'lt', 63.3, 70.8, (TERCERO[0], TERCERO[1], dict(_LTU, x=1440, top=575))))
