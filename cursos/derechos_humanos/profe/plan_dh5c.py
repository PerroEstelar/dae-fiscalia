# -*- coding: utf-8 -*-
r"""Cierre de la unidad 5 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ok ahora con el cierre de unidad 5, todo completo y con la mayor
excelencia».

**Fuente.** `11. Video Cierre U5.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080,
30 fps parejos (5007 cuadros en 166,9 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. STT (Scribe, WAV a 16 kHz, 381 palabras), cuadros y RMS en ventanas de 50 ms.

**Un corte.** En «exige el principio de proporcionalidad, garan-- respeto de garantías y trato
digno» se queda a medio decir «garan--» (74,10–74,45). Hay silencio a los dos lados (−50 a
−68 dB en 73,75–74,05; −48 a −103 dB en 74,50–74,90), así que se corta 74,00–74,70 y la pausa
que queda (0,57 s) suena natural. Después del corte, el plano cerrado hasta la pausa de 1,6 s
antes de «Y en esta» (78,00), sin gráficos; revisado a 4 cuadros por segundo: la cabeza y el
mentón quedan dentro y él está derecho. El otro tropiezo, «se pidió conexidad con-- de los
casos», no se corta: entre «conexidad» y «con» no hay silencio (−34 dB), y un corte ahí se
oiría.

**Unidad 5:** «Decidir como garante: integración, control de convencionalidad aplicado y
transferencia al despacho» (ficha).

**Textos.** Sus palabras recortadas, contrastadas con el guion de cierre de la ficha, que sigue
de cerca («Una decisión bien reponderada coincide en lo esencial con esta», donde la ficha dice
«Las decisiones modelo coinciden en lo esencial»). «Uno verificable, sí» resume «uno que pueda
verificar, sí».

**Gráficos.** Cartones y cuatro listas de AE: lo que se hizo ante la amenaza (sin título), el
repaso de las unidades 1 a 4 (cuatro filas, sin título; la 5 va en su propio cartón después del
plano cerrado), cómo se previene en el despacho y el plan de transferencia. Quedan sin gráfico «La
amenaza mostró que la fuente de riesgo es la estructura criminal», «Cinco unidades y un solo
aprendizaje», la primera sentencia de la Corte Interamericana y el agradecimiento, para no pasar
del 80 % de cobertura.

Los tiempos están en segundos de la fuente; `cuadro` los pasa a la línea descontando el corte.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, CERRADO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 5 - CIERRE PROFE'
BIN = BIN_CURSO + ['UNIDAD 5 - CIERRE PROFE']
ORIGINAL = R + '/01 VIDEO/11. Video Cierre U5.mp4'
COMPUESTO = R + '/01 VIDEO/DH5C_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u5 cierre.mp4'
SUB = ('Unidad 5. Decidir como garante: integración, control de convencionalidad aplicado y '
       'transferencia al despacho')
NOMBRE_LINEA = 'DH - U5 - CIERRE PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 5 CIERRE-v%d'
PREFIJO = 'DH5C'
TMP = 'D:/DAE/_tmp/dh_profe/dh5c'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [
    (0.0, 74.00, None),
    (74.70, 78.00, CERRADO),     # «respeto de garantías y trato digno.»
    (78.00, 166.8, None),
]
T0, T1 = 0.0, 166.8
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 0.6, 8.0, PROFE),
    ('c01_retractacion', 'carton', 13.7, 24.4, c_ante(
        'La retractación debilitó un episodio periférico', 'No el núcleo de la prueba',
        'La flagrancia, el arma, los mensajes.')),
    ('m01_amenaza', 'mg_lista', 28.7, 36.8, lista(
        None,
        ('escudo', 'Se reforzó la protección', 28.82),
        ('carpeta', 'Se pidió la conexidad de los casos', 30.18),
        ('lupa_doc', 'Se abrió una línea contra los determinadores', 32.68))),
    ('c02_inaceptable', 'carton', 36.8, 43.7, c_ante(
        'Lo inaceptable', 'Sostenerlo todo sin revisar nada', 'O soltarlo todo por el pánico.')),
    ('m02_unidades', 'mg_lista', 46.6, 73.9, lista(
        None,
        ('balanza', 'La dignidad y la doble incidencia', 46.70),
        ('libro_ley', 'De dónde vienen los estándares', 56.66),
        ('lupa_doc', 'Debida diligencia en cinco componentes', 61.50),
        ('mazo', 'Restringir con legitimidad', 67.88))),
    ('c03_esta', 'carton', 78.8, 84.4, c_ante(
        'Y en esta', 'Integrar, motivar y prevenir son una sola tarea')),
    ('c04_firma', 'carton', 86.0, 91.0, cita('Cuando usted firma, firma el Estado.')),
    ('c05_cancillerias', 'carton', 101.0, 111.9, c_tit(
        'La responsabilidad internacional no nace en las cancillerías',
        'Nace en las actuaciones de servidores de carne y hueso.')),
    ('m03_previene', 'mg_lista', 112.7, 127.9, lista(
        'En el despacho',
        ('libreta', 'Documentar el riesgo', 115.18),
        ('ruta', 'Actuar a tiempo', 116.70),
        ('escudo', 'Activar las rutas', 117.94),
        ('libro_ley', 'Control de convencionalidad', 119.32))),
    ('c06_manana', 'carton', 128.2, 133.8, cita('Los expedientes reales empiezan mañana.')),
    ('m04_plan', 'mg_lista', 133.8, 149.0, lista(
        'Plan de transferencia',
        ('persona', 'Qué hará distinto desde su rol', 140.42),
        ('lupa_doc', 'Cómo se verá en sus actuaciones', 142.58),
        ('doc_check', 'Cómo lo verificará en 30 días', 144.64))),
    ('c07_generico', 'carton', 149.0, 154.1, c_tit(
        'Un compromiso genérico no es un plan', 'Uno verificable, sí.')),
    ('c08_pregunta', 'carton', 157.8, 166.75, c_tit(
        '¿Qué derechos toca lo que voy a firmar hoy?', 'La pregunta que lo acompañó en todo el curso.')),
]
