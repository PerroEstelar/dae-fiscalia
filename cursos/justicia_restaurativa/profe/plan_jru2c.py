# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Justicia restaurativa en la práctica del fiscal» (19 nov 2026). Entrega provisional.

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u2_cierre_fuente.mp4` (Drive del curso → VIDEOS, «Justica restuaraativa-  Unidad 2 cierre.mp4»,
`1xFAc3bR31B6qONEN_aRL_TCvkAA7MpFX`, 259 MB, del 18 nov): 1920×1080, 30 fps parejos, 37.393 cuadros (20:46,5),
etiquetada `smpte170m` (BT.601: no lleva `MATRIZ_FUENTE`), pico de −1,0 dBFS. Trae pegados la intro (cuadros 0–277)
y el outro (desde el 37114: la diferencia entre cuadros salta a 47 y el brillo a 234); brillo medido en los 37.393
cuadros: parejo en 188 del 278 al 37113. Entra del cuadro 280 al 37114.

- **Una raya negra en el borde de arriba**, como en las otras fuentes del curso: fila 0 en 0–3 y fila 1 en 125 sobre
  el lienzo blanco (fila 2 en 251, después 254–255), medida en tres cuadros (0:20, 10:23 y 20:34). `PREFILTRO`
  pinta las filas 0 a 2 del blanco del lienzo.
- **Diferencia entre cuadros en toda la fuente** (`prep2_cierre.py`): ningún empalme del editor dentro del cuerpo;
  los picos (3 a 5) son gestos.

**Qué es.** Dos mosaicos sobre blanco, como el inicio de la unidad: Víctor Hugo Ospina Vargas a la izquierda
(x 53–940) y Jhonatan Sandoval, el profesor invitado, a la derecha (x 979–1866), los dos en y 290–789. Víctor abre
y pregunta (0:10,3 a 6:43,0), responde Jhonatan (6:44,0 a 11:54,7) y cierra Víctor (11:57,2 a 20:35,5). STT
(Scribe): 2.265 palabras, dos hablantes.

**Un corte que pide el profesor.** A las 12:36 Víctor dice «…para terminar con este video y con este, eh, esta
unidad tres— esta unidad dos. Voy a repetir ahí porque de pronto no queda bien el corte.» y vuelve a empezar
«Entonces, colegas, para poder culminar con esta unidad dos…». Sale todo el arranque fallido: de 755,83 s (0,74 s
después de «…de este curso.», en silencio digital, −77 dB en RMS de 20 ms) a 774,67 s (0,40 s antes del segundo
«Entonces», −84 dB), cuadros 22675 a 23239: 18,8 s. Los dos puntos se eligieron entre los pares de cuadros con
menos diferencia de imagen en los dos silencios (3,3 contra 0,1 entre cuadros seguidos: los dos se acomodaron en la
silla), y el corte va con `SUAVE = 3` (tres cuadros de mezcla; ver `ic_pieza.tramos_vf`). Las otras seis pausas de
más de 2 s son cambios de quien habla o de quien piensa: se dejan.

**Termina** con «…sin ninguna duda debe estar transversalizado por el enfoque restaurativo.» (1235,54 s) y 1,6 s
de silencio hasta el outro. Así llegó.

**Nombre de la unidad.** Del PDF del curso del 10 de noviembre (`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`), el mismo del
inicio de la unidad: «Aplicación jurídica de la justicia restaurativa en el proceso penal».

**Lower thirds.** Los de dos mosaicos del inicio de la unidad (`plan_jru2i`): Víctor al empezar, y Jhonatan cuando
Víctor lo presenta («la importante presencia del invitado Jonathan Sandoval», 0:30,3) y cuando toma la palabra.
Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar, VICTOR, CLIP0, FPS, FQ  # noqa: E402
from plan_jru2i import JHONATAN  # noqa: E402  (el rótulo de dos mosaicos)

globals().update(armar('jr_u2_cierre_fuente.mp4', 'UNIDAD 2/CIERRE',
                       'Unidad 2. Aplicación jurídica de la justicia restaurativa en el proceso penal',
                       'JR - U2 - CIERRE', 'justiciarestaurativa - U2 - CIERRE', 'JRU2C', 280, 37114))

PREFILTRO = 'drawbox=x=0:y=0:w=iw:h=3:color=0xFEFEFE:t=fill'

TRAMOS = [(T0, 22675 / FQ, None), (23240 / FQ, T1, None)]  # noqa: F821
SUAVE = 3            # cuadros de mezcla en el corte (la ventana no cambia)


def cuadro(t):
    """Segundos de la fuente → cuadro de la línea, descontando el corte."""
    acum = 0.0
    for a, b, _w in TRAMOS:
        if a - 1e-6 <= t <= b + 1e-6:
            return CLIP0 + int(round((acum + t - a) * FPS))
        acum += b - a
    raise ValueError('%.2f cae en el corte' % t)


ITEMS = [
    ('lt01', 'lt', 11.5, 19.0, VICTOR),
    ('lt02', 'lt', 31.5, 39.0, JHONATAN),
    ('lt03', 'lt', 405.2, 412.7, JHONATAN),
]
