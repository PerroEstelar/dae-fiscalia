# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4 de «Justicia restaurativa en la práctica del fiscal» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u4_cierre_fuente.mp4` (Drive del curso → VIDEOS, «Justica restuaraativa-  Unidad 4 cierre.mp4»,
`1G4PPvI-l50lDGY0ffUOr0Rushskq8MSt`, 191 MB, del 19 nov; se miró el `mimeType`: es video): 1920×1080, 30 fps
parejos, 20.144 cuadros (11:11,5), etiquetada `smpte170m` (BT.601: no lleva `MATRIZ_FUENTE`), pico de −0,9 dBFS.
Trae la intro pegada (cuadros 0–277) y **no trae outro**: la conversación llega al último cuadro (brillo medido
en los 20.144 cuadros: parejo en 152–156 desde el 278). Entra del cuadro 280 al 20144.

- **Una raya negra en el borde de arriba**, de lado a lado, como en las otras fuentes del curso: la fila 0 en
  negro y la fila 1 en gris (126) sobre el lienzo blanco (252), medida en tres cuadros (0:20, 5:00 y 11:00).
  `PREFILTRO` pinta esas dos filas del blanco del lienzo. Los otros tres bordes están limpios.
- **Termina sin despedida.** Las últimas palabras de Víctor son «…que se encuentren a punto de efectivamente,
  eh, culminar este curso» (terminan en 671,01 s, 0,46 s antes del final del archivo). Así llegó la grabación.

**Qué es.** Los tres mosaicos de la unidad 1, con los mismos bordes medidos (ver `plan_jru1i`): Martín Posada
Martínez arriba a la izquierda (x 38–940, y 22–528), Jhonatan Sandoval arriba a la derecha (x 979–1881) y Víctor
Hugo Ospina Vargas abajo al centro (x 509–1410, y 551–1057). Víctor abre y pregunta (0:10,1 a 2:00,3); responde
Jhonatan (2:01,8 a 5:35,5), después Martín (5:39,9 a 9:59,9) y cierra Víctor (10:02,7 a 11:11,0). STT (Scribe):
1.355 palabras. Sin reinicios ni pedidos de corte; las pausas de más de 2 s (seis) son de quien piensa o cambios
de quien habla: **no se corta nada**.

**Nombre de la unidad.** «Plan de justicia restaurativa»: así está en el PDF del curso del 10 de noviembre
(`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`), en la estructura del curso (2.4). El texto que devuelve Drive de ese PDF
llega hasta la unidad 2: no se pudo leer el encabezado de la unidad 4 (3.1).

**Lower thirds.** Los de tres mosaicos de `plan_jru1i` (dos renglones, en el blanco libre de abajo), cada uno cuando
esa persona empieza a hablar. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar  # noqa: E402
from plan_jru1i import VICTOR_U, MARTIN_U, TERCERO, _LTU  # noqa: E402  (los rótulos de tres mosaicos)

globals().update(armar('jr_u4_cierre_fuente.mp4', 'UNIDAD 4/CIERRE',
                       'Unidad 4. Plan de justicia restaurativa',
                       'JR - U4 - CIERRE', 'justiciarestaurativa - U4 - CIERRE', 'JRU4C', 280, 20144))

PREFILTRO = 'drawbox=x=0:y=0:w=iw:h=2:color=0xFCFCFC:t=fill'

ITEMS = [
    ('lt01', 'lt', 11.5, 19.0, VICTOR_U),
    ('lt02', 'lt', 122.6, 130.1, (TERCERO[0], TERCERO[1], dict(_LTU, x=1440, top=575))),
    ('lt03', 'lt', 340.9, 348.4, MARTIN_U),
]
