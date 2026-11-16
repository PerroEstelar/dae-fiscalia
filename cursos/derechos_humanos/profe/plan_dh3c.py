# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ahora lo mismo con el cierre de la unidad 3».

**Fuente.** `07. Video Cierre U3.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080,
30 fps parejos (4730 cuadros en 157,7 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. Sin versión de Camtasia: STT (Scribe, WAV a 16 kHz, 344 palabras), cuadros y RMS en
ventanas de 50 ms. No hay arranques en falso, frases repetidas ni pausas largas (la más larga,
1,8 s antes de «Dos errores frecuentes…»), así que va entera.

**Unidad 3:** «Proteger con debida diligencia: investigación, víctimas y enfoques diferenciales»
(ficha).

**Textos.** Sus palabras recortadas, contrastadas con el guion de cierre de la ficha, que sigue
casi al pie de la letra. En «Oportunidad» el STT oye «la diligencia es la diligencia a tiempo»
(la ficha: «la diligencia debida es diligencia a tiempo»): no va en pantalla. Él no menciona el
cuestionario, así que el cartón final es la decisión que viene y la cita en la unidad 4.

**Gráficos.** Cartones y dos listas de AE: los cinco componentes de la debida diligencia (una
palabra por fila, entran a medida que los nombra; sin título, porque con cinco filas no cabe:
lo dice el cartón de antes) y la idea del inicio hecha método. Los dos errores frecuentes van en
un cartón, y los tres controles («cada hipótesis tiene actos que podrían refutarla…») y la
bitácora quedan sin gráfico para no pasar del 80 % de cobertura.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 3 - CIERRE PROFE'
BIN = BIN_CURSO + ['UNIDAD 3 - CIERRE PROFE']
ORIGINAL = R + '/01 VIDEO/07. Video Cierre U3.mp4'
COMPUESTO = R + '/01 VIDEO/DH3C_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u3 cierre.mp4'
SUB = 'Unidad 3. Proteger con debida diligencia: investigación, víctimas y enfoques diferenciales'
NOMBRE_LINEA = 'DH - U3 - CIERRE PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 3 CIERRE-v%d'
PREFIJO = 'DH3C'
TMP = 'D:/DAE/_tmp/dh_profe/dh3c'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [(0.0, 157.6, None)]
T0, T1 = 0.0, 157.6
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 0.9, 8.6, PROFE),
    ('c01_fallas', 'carton', 14.1, 24.7, c_tit(
        'Cuatro fallas pequeñas silenciaban a una víctima',
        'Ocho fallas sumadas construyen una condena internacional.')),
    ('c02_cinco', 'carton', 25.6, 29.7, c_tit('Cinco componentes', 'Que funcionan como un sistema.')),
    ('m01_componentes', 'mg_lista', 29.8, 64.8, lista(
        None,
        ('libro_ley', 'Oficiosidad', 29.96),
        ('ruta', 'Oportunidad', 35.38),
        ('lupa_doc', 'Exhaustividad', 45.40),
        ('balanza', 'Imparcialidad', 51.38),
        ('dialogo', 'Participación', 57.46))),
    ('c03_eleva', 'carton', 68.5, 78.2, c_ante(
        'Belém do Pará', 'El estándar se eleva',
        'Frente a la violencia contra las mujeres, periodistas y personas defensoras.')),
    ('c04_victima', 'carton', 78.7, 90.9, c_tit(
        'La víctima no es un tercero incómodo',
        'Es titular de los derechos a la verdad, la justicia y la reparación, con garantías de no '
        'repetición.')),
    ('m02_metodo', 'mg_lista', 91.0, 103.9, lista(
        'Se volvió método',
        ('dialogo', 'Escuchar sin juzgar', 94.7),
        ('ruta', 'Informar desde el primer contacto', 97.1),
        ('carpeta', 'No obligar a nadie a repetir su historia', 99.3))),
    ('c05_errores', 'carton', 104.0, 117.7, c_tit(
        'Dos errores frecuentes',
        'Archivar por la sola retractación o inasistencia de la víctima, y convertir su declaración en '
        'el único eje de la prueba.')),
    ('c06_proxima', 'carton', 138.3, 148.4, c_ante(
        'Hasta aquí, el curso le ha pedido proteger',
        'En la próxima unidad: restringir derechos con legitimidad')),
    ('c07_libertad', 'carton', 149.2, 157.5, c_tit(
        'Su siguiente decisión será sobre la libertad de una persona', 'Nos vemos en la unidad 4.')),
]
