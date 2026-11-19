# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3 de «Justicia restaurativa en la práctica del fiscal» (19 nov 2026). Entrega provisional.

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u3_cierre_fuente.mp4` (Drive del curso → VIDEOS, «Justica restuaraativa-  Unidad 3 cierre.mp4»,
`1gC1QllKcxwjnSVrsBI0sjmFu0HhTA4X0`, 304 MB, del 18 nov): 1920×1080, 30 fps parejos, 29.494 cuadros (16:23,2),
etiquetada `smpte170m` (BT.601: no lleva `MATRIZ_FUENTE`), pico de −4,3 dBFS. Trae pegados la intro (cuadros 0–277)
y el outro (desde el 29215: la diferencia entre cuadros salta a 83 y el brillo a 235). Entra del cuadro 280 al
29215.

- **Una raya negra en el borde de arriba**, como en las otras fuentes del curso: fila 0 en 1 y fila 1 en 127 sobre
  el lienzo blanco (252), medida en tres cuadros (0:20, 8:11 y 16:11). `PREFILTRO` pinta esas dos filas del blanco
  del lienzo, como en el cierre de la U4.
- **Diferencia entre cuadros en toda la fuente** (`prep2_cierre.py`): ningún empalme del editor dentro del cuerpo;
  los picos (3 a 5) son gestos de Martín. El brillo medio sube y baja entre 152,5 y 156,5 en tramos largos: es la
  luz de la cámara de Martín, no un corte.

**Qué es.** Los tres mosaicos de la unidad 1, con los mismos bordes medidos (ver `plan_jru1i`): Martín Posada
Martínez arriba a la izquierda (x 38–940, y 22–528), Jhonatan Sandoval arriba a la derecha (x 979–1881) y Víctor
Hugo Ospina Vargas abajo al centro (x 509–1410, y 551–1057). Víctor abre y pregunta (0:11,6 a 1:55,3); responde
Jhonatan (1:56,9 a 5:00,5), después Martín (5:03,5 a 11:53,4) y cierra Víctor (11:55,1 a 16:12,5). STT (Scribe):
1.954 palabras, tres hablantes. Sin reinicios ni pedidos de corte; las seis pausas de más de 2 s son de quien
piensa o cambios de quien habla: **no se corta nada**.

**Termina** con «…muchos éxitos con el cuestionario que van a desarrollar culminando esta unidad tres.» (972,50 s)
y 1,3 s de silencio hasta el outro.

**Nombre de la unidad.** «Implementación de la justicia restaurativa»: el del PDF del curso del 10 de noviembre
(`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`), el mismo del inicio de la unidad.

**Lower thirds.** Los de tres mosaicos de `plan_jru1i` (dos renglones, en el blanco libre de abajo), cada uno cuando
esa persona empieza a hablar. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar  # noqa: E402
from plan_jru1i import VICTOR_U, MARTIN_U, TERCERO, _LTU  # noqa: E402  (los rótulos de tres mosaicos)

globals().update(armar('jr_u3_cierre_fuente.mp4', 'UNIDAD 3/CIERRE',
                       'Unidad 3. Implementación de la justicia restaurativa',
                       'JR - U3 - CIERRE', 'justiciarestaurativa - U3 - CIERRE', 'JRU3C', 280, 29215))

PREFILTRO = 'drawbox=x=0:y=0:w=iw:h=2:color=0xFCFCFC:t=fill'

ITEMS = [
    ('lt01', 'lt', 12.9, 20.4, VICTOR_U),
    ('lt02', 'lt', 118.0, 125.5, (TERCERO[0], TERCERO[1], dict(_LTU, x=1440, top=575))),
    ('lt03', 'lt', 304.7, 312.2, MARTIN_U),
]
