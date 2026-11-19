# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3 de «Justicia restaurativa en la práctica del fiscal» (18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u3_inicio_fuente.mp4` (Drive del curso → VIDEOS, «Justicia restaurativa -  Unidad 3 Inicio.mp4»,
`15z_Xy-8qQWaRgp0vTAQnjsMYyNX-vROT`, 403 MB, del 17 nov): 1920×1080, 30 fps parejos, 20.842 cuadros (11:34,8), pico
de −0,4 dBFS. **No es como las otras cuatro**: es la grabación sin pasar por el editor.

- **No trae intro ni outro**: la conversación empieza en el primer cuadro y llega al último (brillo medido en los
  20.842 cuadros, parejo en 153; hoja de un cuadro cada 20 s: los tres mosaicos todo el tiempo).
- **Viene sin etiqueta de color y está en BT.709.** Las otras llegan etiquetadas `smpte170m` (BT.601). Se midió el
  rojo, el azul y el amarillo del logo de la Fiscalía en el mosaico de Víctor contra la fuente del cierre de la U1
  (etiquetada, leída como 601): rojo (234, 65, 65), azul (9, 89, 161), amarillo (237, 189, 27). Esta fuente leída
  como 709 da (233, 66, 62), (8, 89, 161) y (237, 190, 27); leída como 601, el rojo cae a (217, 57, 71). Lleva
  `MATRIZ_FUENTE = 'bt709'`.
- **Una raya negra en el borde de arriba**, de lado a lado: la fila 0 en negro (Y 16) y la fila 1 en gris (Y 125)
  sobre el lienzo blanco (Y 234). `PREFILTRO` pinta esas dos filas del blanco del lienzo. (La traen también las
  fuentes del inicio del curso y de los inicios y el cierre de las U1 y U2; ver el README.)

**Qué es.** Los tres mosaicos de la unidad 1 (medidos: mismos bordes que en `plan_jru1i`): Martín Posada Martínez
arriba a la izquierda, Jhonatan Sandoval arriba a la derecha y Víctor Hugo Ospina Vargas abajo al centro. Víctor
presenta la unidad (0:02,6 a 1:23,1), habla Jhonatan (1:23,9 a 5:23,3), después Martín (5:26,5 a 7:44,0) y cierra
Víctor (7:46,5 a 11:29,3). STT (Scribe): 1.437 palabras en la fuente. Scribe confunde los hablantes: da a Martín
la etiqueta de Víctor; quién habla sale de lo que dicen y de la imagen.

Entra del cuadro 45 (1,5 s; la primera palabra empieza en 2,56 s, antes hay silencio digital) al 20700 (690,0 s; la
última palabra, «poco.», termina en 689,15 s). **Lo que sigue no entra**: 3,5 s de silencio y un «Listo, profe» de
alguien, ya fuera de la toma (693,9 s).

**Un corte de 14,5 s** (cuadros 18762 a 19197 de la fuente; 625,40 a 639,90 s). Víctor se enreda y lo pide él:
«Seguramente quienes nos hemos dedicado a la justicia restaurativa hemos visto en esto, eh, un, una, una, eh… un
corte, por favor. Eh, hemos visto en esto, hemos visto en esto una gran motivación…». Sale desde el primer «hemos
visto en esto» hasta el segundo, y queda el tercero: «…a la justicia restaurativa | hemos visto en esto una gran
motivación…». Los dos bordes caen en silencio medido (RMS de 20 ms): la voz termina en 625,26 s y vuelve en
625,60; calla desde 638,80 y vuelve en 640,12. La pausa que queda es de 0,36 s (la original, 0,34). Es un corte
directo: con tres mosaicos no hay plano cerrado que lo disimule.

**Lo que se deja.** Jhonatan arranca con «Si me permites, Martín, ¿comienzo yo?»: es parte de la conversación.

**Nombre de la unidad.** «Implementación de la justicia restaurativa»: así está en el PDF del curso del 10 de
noviembre (`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`) las dos veces que aparece (2.4, estructura del curso, y 3.1, nombre
de la unidad No. 3).

**Lower thirds.** Los de tres mosaicos de `plan_jru1i` (dos renglones, en el blanco libre de abajo), cada uno cuando
esa persona empieza a hablar. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar, CLIP0, FPS, FQ  # noqa: E402
from plan_jru1i import VICTOR_U, MARTIN_U, TERCERO, _LTU  # noqa: E402  (los rótulos de tres mosaicos)

globals().update(armar('jr_u3_inicio_fuente.mp4', 'UNIDAD 3/INICIO',
                       'Unidad 3. Implementación de la justicia restaurativa',
                       'JR - U3 - INICIO', 'justiciarestaurativa - U3 - INICIO', 'JRU3I', 45, 20700))

MATRIZ_FUENTE = 'bt709'
PREFILTRO = 'drawbox=x=0:y=0:w=iw:h=2:color=0xFEFEFE:t=fill'

TRAMOS = [(T0, 18762 / FQ, None), (19197 / FQ, T1, None)]  # noqa: F821


def cuadro(t):
    """Segundos de la fuente → cuadro de la línea, descontando el corte."""
    acum = 0.0
    for a, b, _w in TRAMOS:
        if a - 1e-6 <= t <= b + 1e-6:
            return CLIP0 + int(round((acum + t - a) * FPS))
        acum += b - a
    raise ValueError('%.2f cae en el corte' % t)


ITEMS = [
    ('lt01', 'lt', 4.0, 11.5, VICTOR_U),
    ('lt02', 'lt', 84.8, 92.3, (TERCERO[0], TERCERO[1], dict(_LTU, x=1440, top=575))),
    ('lt03', 'lt', 327.5, 335.0, MARTIN_U),
]
