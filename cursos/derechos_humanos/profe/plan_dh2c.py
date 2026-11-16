# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ahora lo mismo pero con el cierre de la unidad 2, de pe a pa».

**Fuente.** `05. Video Cierre U2.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080,
30 fps parejos (5502 cuadros en 183,4 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. Sin versión de Camtasia: los cortes salen del STT (Scribe, WAV a 16 kHz, 391 palabras),
de los cuadros y del RMS en ventanas de 50 ms (el audio trae tramos de silencio digital, −180 dB,
que marcan bien dónde cortar).
- **La apertura está dos veces.** «Felicitaciones. Ha completado la segunda unidad. Empezó con un
  escrito… o hacer el análisis completo.» va de 0,18 a 22,70 y otra vez, igual, de 22,98 a 45,52.
  Se queda la segunda (la repetición deliberada): el compuesto arranca en 22,80, en silencio.
- **Un arranque en falso con claqueta:** «Hoy sabe por lo que-- un, dos, tres.» (46,12–50,42).
  Se corta de 45,62 a 50,52 (los dos bordes en silencio digital); queda una pausa de 0,7 s.
- Después del corte, el plano cerrado hasta el final de «Hoy sabe por qué solo la tercera
  protege a la vez a la víctima y a la actuación.» (50,52–57,00), sin gráficos.

**Unidad 2:** «La caja de herramientas normativa: fuentes, bloque de constitucionalidad y control
de convencionalidad».

**Gráficos.** Sus palabras recortadas: cartones con antetítulo por cada parte («Primero»,
«Segundo», «Tercero»), una lista con quién interpreta en cada sistema y otra con los cuatro pasos
(sin título: cuatro filas en la columna de 520). Las tres reacciones van en un cartón y no en
lista: la tercera fila quedaba en pantalla 2 s antes del corte.

Los tiempos están en segundos de la fuente; `cuadro` los pasa a la línea descontando los cortes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, CERRADO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 2 - CIERRE PROFE'
BIN = BIN_CURSO + ['UNIDAD 2 - CIERRE PROFE']
ORIGINAL = R + '/01 VIDEO/05. Video Cierre U2.mp4'
COMPUESTO = R + '/01 VIDEO/DH2C_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u2 cierre.mp4'
SUB = ('Unidad 2. La caja de herramientas normativa: fuentes, bloque de constitucionalidad y control '
       'de convencionalidad')
NOMBRE_LINEA = 'DH - U2 - CIERRE PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 2 CIERRE-v%d'
PREFIJO = 'DH2C'
TMP = 'D:/DAE/_tmp/dh_profe/dh2c'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [
    (22.80, 45.62, None),        # la segunda toma de la apertura
    (50.52, 57.00, CERRADO),     # «Hoy sabe por qué solo la tercera protege…»
    (57.00, 183.4, None),
]
T0, T1 = 22.80, 183.4
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 23.0, 31.2, PROFE),
    ('c01_reacciones', 'carton', 32.4, 45.5, c_tit(
        'Tres reacciones posibles',
        'Rechazarlo como derecho extranjero, retirar la evidencia o hacer el análisis completo.')),
    ('c02_primero', 'carton', 57.5, 71.3, c_ante(
        'Primero: las fuentes tienen un orden', 'Por el artículo 93',
        'Los tratados de derechos humanos ratificados por Colombia entran al bloque de constitucionalidad.')),
    ('c03_aplicable', 'carton', 71.4, 76.6, cita('No son derecho extranjero: son Constitución aplicable.')),
    ('c04_segundo', 'carton', 90.9, 95.9, c_ante('Segundo', 'Cada tratado tiene quien lo interpreta')),
    ('m01_sistemas', 'mg_lista', 96.0, 106.0, lista(
        None,
        ('mundo', 'Sistema universal: los comités', 96.2),
        ('balanza', 'Sistema interamericano: la Comisión y la Corte', 98.4))),
    ('c05_subsidiario', 'carton', 106.6, 117.7, c_tit(
        'El sistema es subsidiario', 'El primer juez de los derechos humanos es el Estado mismo.')),
    ('c06_tercero', 'carton', 123.5, 134.9, c_ante(
        'Tercero', 'El control de convencionalidad',
        'Tarea de cualquier autoridad pública, no solo de los jueces.')),
    ('m02_pasos', 'mg_lista', 135.0, 148.6, lista(
        None,
        ('lupa_doc', 'Identificar la norma', 135.2),
        ('libro_ley', 'Identificar el estándar y su intérprete', 137.1),
        ('balanza', 'Contrastar, prefiriendo la interpretación conforme', 140.6),
        ('firma', 'Documentar el análisis', 144.0))),
    ('c07_regla', 'carton', 155.0, 163.2, c_tit(
        'La regla de oro', 'Ningún estándar entra a su argumento sin verificarlo en su fuente oficial.')),
    ('c08_proxima', 'carton', 164.1, 176.3, c_ante(
        'En la próxima unidad', 'El expediente se complica',
        'Nuevas amenazas, con un componente de género y un contexto de presencia armada.')),
    ('c09_cuestionario', 'carton', 177.4, 183.3, c_tit(
        'Resuelva el cuestionario de la unidad', 'Nos vemos en la unidad 3.')),
]
