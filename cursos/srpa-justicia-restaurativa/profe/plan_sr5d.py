# -*- coding: utf-8 -*-
r"""Desarrollo de la unidad 5 de SRPA: la clase completa (17 nov 2026).

**Entrega provisional, sin gráficos en el cuerpo.** Sebastián, con el plan a medio escribir:
«el U5 desarrollo me confirman que por ahora solo hagamos intro y outro, placas de entrada y
salida y títulos del profe, provisionalmente, porque se trata de entregar rápido». Va entonces
con intro, cartón de título, lower third, cartón de cierre y outro. Los cartones y las listas de
AE quedan pendientes: cuando se pidan, se agregan a `ITEMS` (los tiempos están en segundos de la
fuente) y se rinde una v2 sobre el mismo compuesto.

**Fuente.** `srpa_u5_inicio_fuente.mp4` (ver `plan_sr5i`). Los primeros 3.424 cuadros son la
bienvenida de la unidad, que es otra pieza; esta va del cuadro 3437 (114,57 s, medio segundo
antes de «Queridos discentes, bienvenidos a la unidad número cinco») al 61786, el final del
archivo. STT (Scribe): la clase va de 115,06 a 2.059,14 s.

**La fuente ya viene montada con tomas**, muchas más que la de la unidad 4. Medido cuadro a
cuadro (`prep_u5.py`, `saltos_u5.py`, `saltos2_u5.py`; hojas en `D:\DAE\_tmp\sr_ta\saltos_u5_*.jpg`
y `tiras_cortes_a_*.jpg`):
- **Cuatro cubos 3D** entre bloques (cuadros 11125–11152, 36405–36434, 42171–42200 y
  49991–50015). Se tapan con el primer cuadro limpio de después, quieto (`CONGELA`). En el
  segundo se oye la cola de la última palabra (0,3 s) y en el cuarto el arranque de la frase
  siguiente (0,3 s): el cubo está ahí en la fuente, y no se puede mostrar.
- **Cortes secos de toma.** En esta fuente el panel DAE/Fiscalía no cambia de nivel entre tomas:
  se buscaron por el pico aislado de la diferencia entre cuadros y se midió cuánto cambia la zona
  de la persona de un cuadro al siguiente (`e`, a 640×360). El movimiento natural da hasta 8; un
  gesto de manos, más (el fondo virtual de Teams las hace aparecer y desaparecer). Los diez con
  `e` ≥ 13 son cortes de toma claros: cuadros 16545, 19736, 23086, 24123, 51013, 54828, 56485,
  58059, 59264 y 60494. Después de cada uno va el **plano cerrado** hasta la pausa siguiente,
  para que el salto se lea como cambio de plano. Dos vuelven al plano abierto justo en otro
  corte, más chico (55039 y 56670), que así también queda tapado.
- El undécimo plano cerrado es la despedida: del corte del cuadro 61263 (`e` 9) al final.
- Quedan cortes chicos, con `e` entre 9 y 11 (16374, 18027, 56221, 60342 y otros): casi no
  desplazan la imagen y se dejan, como el quinto de la unidad 4.
- **En tres cortes el profe termina la frase con el vaso de agua ya en la mano** (antes de los
  cuadros 51013, 54828 y 59264 se lo ve levantarlo y taparse la boca durante un segundo, con la
  voz 10 dB más baja). Se revisó el sonido contra la boca (`boca_u5.py`, `boca2_u5.py`): la
  imagen y el sonido van juntos en toda la fuente, así que no es un desfase; él habla con el
  vaso delante. Quitar esos cuadros se llevaría las últimas palabras de la frase: se dejan.

**Ventana 1143×643 desde (12, 30), ×1,68**, la de las unidades 3 y 4. Con la caja en x 86–750 de
salida, la persona pasa del 1,5 % de la caja 14 s en todo el archivo, casi todo en los cubos
(`caja_u5.log`).
**Plano cerrado 960×540 desde (140, 146), ×2,0**, sin el panel DAE/Fiscalía, en los once. El
tope de la cabeza va de y 176 a 268 según la toma (`cerrado_u5.log`): con la ventana que deja
el panel adentro (desde y=34) el mentón quedaba a 16 px del borde en las tomas bajas. Se miró
cada tramo entero a 4 cuadros por segundo, y el último medio segundo cada 3 cuadros
(`tiras_cerrado_B*.jpg`): la cabeza y el mentón entran en todos.
Cada plano cerrado vuelve en el cuadro más silencioso de su pausa (`cerrado_u5.py`).

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_sr_profe import *  # noqa: E402,F401,F403
from base_sr_profe import armar, columna, CARLOS  # noqa: E402

XY, VENTANA = (12, 30), (1143, 643)
MAXW = columna(560)
LT = (44, 560)
CERRADO = (140, 146, 960, 540)
K_INI, K_FIN = 3437, 61786
# cubos: (primer cuadro de la transición, primer cuadro limpio de después)
CUBOS = [(11125, 11153), (36405, 36435), (42171, 42201), (49991, 50016)]
# cortes de toma: (primer cuadro de la toma nueva, cuadro en que vuelve el plano abierto)
CORTES = [(16545, 16771), (19736, 19955), (23086, 23305), (24123, 24351), (51013, 51198),
          (54828, 55039), (56485, 56670), (58059, 58161), (59264, 59356), (60494, 60692),
          (61263, K_FIN)]


def _tramos():
    tr, k = [], K_INI
    for c, r in CORTES:
        tr.append((k / 30.0, c / 30.0, None))
        tr.append((c / 30.0, r / 30.0, CERRADO))
        k = r
    if k < K_FIN:
        tr.append((k / 30.0, K_FIN / 30.0, None))
    return tr


globals().update(armar(
    'srpa_u5_inicio_fuente.mp4', 'UNIDAD 5/DESARROLLO', 5, 'SRPA - U5 - DESARROLLO', 'srpa - U5 - DESARROLLO',
    'SR5D', _tramos()))
CONGELA = [(a / 30.0, b / 30.0) for a, b in CUBOS]

ITEMS = [
    ('lt01', 'lt', 115.4, 123.4, CARLOS),
]
