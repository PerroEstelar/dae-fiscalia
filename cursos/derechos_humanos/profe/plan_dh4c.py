# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ahora lo mismo, de pe a pa, con el cierre de la unidad 4».

**Fuente.** `09. Video Cierre U4.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080,
30 fps parejos (5345 cuadros en 178,2 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. Sin versión de Camtasia: STT (Scribe, WAV a 16 kHz, 395 palabras), cuadros y RMS en
ventanas de 50 ms. No hay arranques en falso, frases repetidas ni pausas largas (la más larga,
2,2 s antes de «Ya tiene las dos caras…»), así que va entera.

**Unidad 4:** «Restringir con legitimidad: medidas de aseguramiento, privación de la libertad y
goce efectivo de los derechos de las Personas Privadas de la Libertad – PPL» (ficha, tal cual).

**Textos.** Sus palabras recortadas, contrastadas con el guion de cierre de la ficha, que él
amplía («y los elementos materiales probatorios e información legalmente obtenida…», «la señal de
calidad de su sustentación…»). Los números van en cifras en los cartones («36 horas»).

**Gráficos.** Cartones y dos listas de AE: por qué resistió la detención (el fin, la necesidad, la
proporcionalidad) y lo que el capturado debe poder hacer desde la aprehensión (cuatro filas, sin
título: con título no cabía; la cita de antes, «La legitimidad también se juega antes de la
audiencia», le da el contexto). Quedan sin gráfico «el juez la impuso», «con otros hechos…» y la
relación de sujeción especial, para no pasar del 80 % de cobertura.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 4 - CIERRE PROFE'
BIN = BIN_CURSO + ['UNIDAD 4 - CIERRE PROFE']
ORIGINAL = R + '/01 VIDEO/09. Video Cierre U4.mp4'
COMPUESTO = R + '/01 VIDEO/DH4C_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u4 cierre.mp4'
SUB = ('Unidad 4. Restringir con legitimidad: medidas de aseguramiento, privación de la libertad y goce '
       'efectivo de los derechos de las Personas Privadas de la Libertad – PPL')
NOMBRE_LINEA = 'DH - U4 - CIERRE PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 4 CIERRE-v%d'
PREFIJO = 'DH4C'
TMP = 'D:/DAE/_tmp/dh_profe/dh4c'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [(0.0, 178.1, None)]
T0, T1 = 0.0, 178.1
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 0.5, 8.0, PROFE),
    ('c01_pregunta', 'carton', 9.7, 21.9, c_tit(
        '¿Pudo sustentar su solicitud con hechos?',
        'No solo con la gravedad del delito, la presión del momento o la comodidad de la medida más '
        'fuerte.')),
    ('m01_resistio', 'mg_lista', 33.3, 62.6, lista(
        'Por qué resistió',
        ('escudo', 'El fin: proteger a la víctima', 33.4),
        ('lupa_doc', 'La necesidad se demostró, no se afirmó', 47.5),
        ('balanza', 'La proporcionalidad no escondió el costo', 56.1))),
    ('c02_metodo', 'carton', 71.9, 83.7, c_tit(
        'El método es idéntico',
        'El resultado cambia por los hechos, los elementos materiales probatorios y la información '
        'legalmente obtenida.')),
    ('c03_antes', 'carton', 84.3, 89.1, cita('La legitimidad también se juega antes de la audiencia.')),
    ('m02_aprehension', 'mg_lista', 89.2, 97.4, lista(
        None,
        ('lupa_doc', 'Conocer los motivos', 89.2),
        ('dialogo', 'Poder avisar a alguien', 90.9),
        ('persona', 'Guardar silencio', 92.3),
        ('libro_ley', 'Contar con un abogado', 93.4))),
    ('c04_36h', 'carton', 97.5, 106.3, c_ante(
        'Un límite que ninguna congestión justifica', '36 horas para ponerlo a disposición del juez')),
    ('c05_constitucion', 'carton', 107.3, 119.4, c_tit(
        'La persona no queda fuera de la Constitución',
        'La Corte Constitucional declaró un estado de cosas inconstitucional en el sistema carcelario.')),
    ('c06_senal', 'carton', 136.4, 154.4, c_ante(
        'La señal de calidad', 'Los argumentos en contra que tuvo en cuenta',
        'Si los tres mejores la derrotan, no estaba bien fundada.')),
    ('c07_ultima', 'carton', 156.5, 171.0, c_ante(
        'En la última unidad', 'Proteger y restringir a la vez, en una sola decisión',
        'Y sustentarla cuando un hecho nuevo la ponga a prueba.')),
    ('c08_cuestionario', 'carton', 171.9, 178.0, c_tit(
        'Resuelva el cuestionario de la unidad', 'Nos vemos en la unidad 5.')),
]
