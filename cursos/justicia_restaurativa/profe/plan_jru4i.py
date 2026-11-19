# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Justicia restaurativa en la práctica del fiscal» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u4_inicio_fuente.mp4` (Drive del curso → VIDEOS, «Justica restuaraativa-  Unidad 4 inicio.mp4»,
`1q_czi8j8AMRGgv9CZThThXnz67JBiBiE`, 163 MB, del 19 nov): 1920×1080, 30 fps parejos, 16.330 cuadros (9:04,4),
etiquetada `smpte170m` (BT.601: no lleva `MATRIZ_FUENTE`), pico de −0,7 dBFS. Trae pegados la intro (cuadros 0–277)
y el outro (desde el 16054; el 16052 y el 16053 son blancos). El primer enlace que llegó fue el audio suelto de la
misma grabación (`.m4a`, `1Tu-qHnIQVyrinWiVNygBTzlKz4FZwrlL`): dura lo mismo y dice lo mismo.

- **Una raya negra en el borde de arriba**, como en las otras fuentes del curso: fila 0 en negro y fila 1 en gris
  (127) sobre el lienzo blanco (252), medida en tres cuadros. `PREFILTRO` pinta esas dos filas del blanco del lienzo.
- **Un empalme del editor de la grabación en 111,97 s** (cuadros 3359 a 3363): una disolvencia de cinco cuadros en
  los tres mosaicos a la vez (la diferencia entre cuadros sube de 0,1 a 47 y baja en cinco cuadros; Jhonatan cambia
  de postura). Cae en silencio digital, entre la pregunta de Víctor (termina en 111,52 s) y la respuesta de Jhonatan
  (113,32 s). Viene así y se deja: con tres mosaicos no hay plano cerrado que lo disimule, y ya es suave.
- **La grabación termina a media frase.** Víctor cierra con «…afronten de la mejor manera esta última unidad.» y
  arranca otra frase que queda cortada («Es un—», 532,20 a 532,98 s; después, silencio hasta el outro). **Ese
  arranque no entra**: el tramo termina en el cuadro 15964 (532,13 s), en el silencio medido entre «unidad.» (acaba
  en 531,88 s) y «Es» (RMS de 20 ms).

Entra del cuadro 300 (10,0 s; la primera palabra empieza en 11,44 s y antes hay silencio digital) al 15964.

**Qué es.** Los tres mosaicos de la unidad 1, con los mismos bordes medidos (ver `plan_jru1i`): Martín Posada
Martínez arriba a la izquierda, Jhonatan Sandoval arriba a la derecha y Víctor Hugo Ospina Vargas abajo al centro.
Víctor presenta la unidad y pregunta (0:11,4 a 1:51,5); responde Jhonatan (1:53,3 a 5:07,5), después Martín, con el
ejemplo del almuerzo (5:10,7 a 7:15,5; Jhonatan le contesta «A mí me gustó»), y cierra Víctor (7:18,7 a 8:51,9).
STT (Scribe): 1.130 palabras. Sin reinicios ni pedidos de corte; las pausas de más de 2 s (cuatro) son un cambio
de quien habla y tres de Martín mientras arma el ejemplo.

**Nombre de la unidad.** «Plan de justicia restaurativa» (PDF del curso del 10 de noviembre,
`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`, 2.4).

**Lower thirds.** Los de tres mosaicos de `plan_jru1i` (dos renglones, en el blanco libre de abajo), cada uno cuando
esa persona empieza a hablar. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar  # noqa: E402
from plan_jru1i import VICTOR_U, MARTIN_U, TERCERO, _LTU  # noqa: E402  (los rótulos de tres mosaicos)

globals().update(armar('jr_u4_inicio_fuente.mp4', 'UNIDAD 4/INICIO',
                       'Unidad 4. Plan de justicia restaurativa',
                       'JR - U4 - INICIO', 'justiciarestaurativa - U4 - INICIO', 'JRU4I', 300, 15964))

PREFILTRO = 'drawbox=x=0:y=0:w=iw:h=2:color=0xFCFCFC:t=fill'

ITEMS = [
    ('lt01', 'lt', 12.9, 20.4, VICTOR_U),
    ('lt02', 'lt', 114.1, 121.6, (TERCERO[0], TERCERO[1], dict(_LTU, x=1440, top=575))),
    ('lt03', 'lt', 311.6, 319.1, MARTIN_U),
]
