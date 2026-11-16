# -*- coding: utf-8 -*-
r"""Inicio de la unidad 5 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ok ahora vamos a continuar con inicio unidad 5 ddhh, de pe a pa».

**Fuente.** `10. Video Inicio U5.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080,
30 fps parejos (5120 cuadros en 170,7 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. STT (Scribe, WAV a 16 kHz, 414 palabras), cuadros y RMS en ventanas de 50 ms. No hay
arranques en falso, frases repetidas ni pausas largas (la más larga, 1,4 s antes de «La Fiscalía
debe tomar…»), así que va entera.

**Unidad 5:** «Decidir como garante: integración, control de convencionalidad aplicado y
transferencia al despacho» (ficha).

**Textos.** Sus palabras recortadas, contrastadas con la ficha de la U5 (video de bienvenida y
presentación), que él reescribe bastante. El STT oye «Esta unidad no integra estándares nuevos.
Los integra…»; la ficha dice «no agrega estándares nuevos: los integra», y esa frase no va en
pantalla. Tampoco «reponderar si empezar de cero» (la ficha: «reponderar sin empezar de cero»):
el cartón dice solo «Reponderar» y lo que sigue, que se oye claro.

**Gráficos.** Cartones (un antetítulo por lección) y tres listas de AE: lo que hay en la carpeta
(cinco filas, sin título), lo que hay que resolver desde el rol y los productos de la unidad
(cuatro filas, sin título). Quedan sin gráfico «Wilmer Acosta está detenido…» (la lista lo
sigue), «La Fiscalía debe tomar una decisión de fondo», las dos objeciones («Alguien
propondrá…») y «Esta unidad no integra estándares nuevos», para no pasar del 80 % de cobertura.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 5 - INICIO PROFE'
BIN = BIN_CURSO + ['UNIDAD 5 - INICIO PROFE']
ORIGINAL = R + '/01 VIDEO/10. Video Inicio U5.mp4'
COMPUESTO = R + '/01 VIDEO/DH5I_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u5 inicio.mp4'
SUB = ('Unidad 5. Decidir como garante: integración, control de convencionalidad aplicado y '
       'transferencia al despacho')
NOMBRE_LINEA = 'DH - U5 - INICIO PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 5 INICIO-v%d'
PREFIJO = 'DH5I'
TMP = 'D:/DAE/_tmp/dh_profe/dh5i'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [(0.0, 170.6, None)]
T0, T1 = 0.0, 170.6
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 0.5, 8.0, PROFE),
    ('m01_carpeta', 'mg_lista', 15.7, 31.4, lista(
        None,
        ('mazo', 'Captura en flagrancia', 17.0),
        ('lupa_doc', 'Análisis de panfletos', 18.82),
        ('doc_check', 'Extracción del celular', 21.40),
        ('persona', 'Testimonio de vecina', 25.08),
        ('libreta', 'Registro de amenazas', 27.0))),
    ('m02_resolver', 'mg_lista', 38.6, 53.7, lista(
        'Resolver desde su rol',
        ('firma', 'Acusar u otra decisión legalmente prevista', 41.64),
        ('escudo', 'Mantener la protección a la víctima', 47.14),
        ('balanza', 'Qué pasa con las medidas', 49.30))),
    ('c01_giro', 'carton', 53.8, 72.6, c_ante(
        'El caso reserva un giro', 'Dos hechos nuevos',
        'Un testigo clave se retracta y Carmen Elisa recibe una nueva amenaza, con Acosta detenido.')),
    ('c02_reponderar', 'carton', 83.8, 93.0, c_tit(
        'Reponderar',
        'Sostener su decisión frente a las objeciones que le harían un juez o una defensa.')),
    ('c03_primera', 'carton', 99.4, 109.7, c_ante(
        'Primera lección', 'Todo lo aprendido, en un solo método',
        'Una decisión que proteja y restrinja a la vez.')),
    ('c04_acusar', 'carton', 110.3, 115.9, cita('La decisión correcta no siempre es acusar.')),
    ('c05_segunda', 'carton', 116.0, 128.1, c_ante(
        'Segunda lección', 'El oficio de argumentar',
        'Que la motivación no sea una lista de normas, y citar la jurisprudencia con pertinencia.')),
    ('c06_tercera', 'carton', 128.7, 141.7, c_ante(
        'Tercera lección', 'El ángulo institucional',
        'Cómo cada actuación del despacho previene o produce la responsabilidad internacional del '
        'Estado.')),
    ('m03_productos', 'mg_lista', 142.3, 163.6, lista(
        None,
        ('firma', 'La decisión integral escrita', 142.38),
        ('dialogo', 'La sustentación de la decisión', 149.74),
        ('ruta', 'Un plan de transferencia', 151.70),
        ('doc_check', 'La autoevaluación de cierre', 157.84))),
    ('c07_bienvenida', 'carton', 163.9, 170.5, c_ante(
        'Bienvenida y bienvenido a la unidad 5', 'Todo el curso en una sola decisión')),
]
