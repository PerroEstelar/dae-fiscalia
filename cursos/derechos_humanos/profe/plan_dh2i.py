# -*- coding: utf-8 -*-
r"""Inicio de la unidad 2 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ahora continuemos con inicio unidad 2 DDHH, todo el proceso».

**Fuente.** `4. Video Inicio U2.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080, 30 fps
parejos (7923 cuadros en 264,1 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, mismo fondo y
mismo encuadre que la presentación. Esta vez no hay versión de Camtasia con la que comparar: los
cortes salen de la transcripción (Scribe, WAV a 16 kHz, 547 palabras) y de mirar los cuadros.
- No hay arranques en falso ni frases repetidas.
- Una pausa de 3,1 s entre «…a la víctima y a la actuación.» (142,74) y «La pregunta de esta
  unidad…» (145,86). Está quieto mirando a cámara: se deja en 1,1 s (corte de 143,35 a 145,35)
  y lo que sigue hasta el final de la frase va en plano cerrado, sin gráficos (145,35–150,15).

**Unidad 2:** «La caja de herramientas normativa: fuentes, bloque de constitucionalidad y control
de convencionalidad» (ficha).

**Textos.** Sus palabras recortadas, contrastadas con el guion de la ficha de la U2 (video de
bienvenida). Dos lugares donde el STT no es confiable y por eso no van en pantalla: «El sistema
es subordinado» (la ficha dice «subsidiario») y «sencilla de formular y exige responder» (la
ficha: «exigente de responder»).

**Gráficos.** Cartones, un antetítulo por cada lección («Primera», «Segunda», «Tercera») y cuatro
listas de AE: los dos tratados que invoca la defensa, el análisis completo, quién interpreta en
cada sistema y el método de cuatro pasos del control de convencionalidad. Las de cuatro filas van
sin título (columna de 520), como en Bienes y en la presentación.

Los tiempos están en segundos de la fuente; `cuadro` los pasa a la línea descontando el corte.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, CERRADO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 2 - INICIO PROFE'
BIN = BIN_CURSO + ['UNIDAD 2 - INICIO PROFE']
ORIGINAL = R + '/01 VIDEO/4. Video Inicio U2.mp4'
COMPUESTO = R + '/01 VIDEO/DH2I_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u2 inicio.mp4'
SUB = ('Unidad 2. La caja de herramientas normativa: fuentes, bloque de constitucionalidad y control '
       'de convencionalidad')
NOMBRE_LINEA = 'DH - U2 - INICIO PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 2 INICIO-v%d'
PREFIJO = 'DH2I'
TMP = 'D:/DAE/_tmp/dh_profe/dh2i'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [
    (0.0, 143.35, None),
    (145.35, 150.15, CERRADO),   # «La pregunta de esta unidad es sencilla de formular…»
    (150.15, 264.1, None),
]
T0, T1 = 0.0, 264.1
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 1.3, 9.6, PROFE),
    ('c01_semanas', 'carton', 11.6, 20.6, c_ante(
        'Seis semanas después', 'Los registros telefónicos', 'Obtenidos con orden y control judicial.')),
    ('c02_acosta', 'carton', 20.7, 35.2, c_tit(
        'Wilmer Acosta', 'Identificado preliminarmente como presunto responsable. Rindió interrogatorio como '
        'indiciado, asistido por su abogada.')),
    ('c03_escrito', 'carton', 47.5, 55.5, c_tit(
        'El escrito de la defensa', 'La obtención de los registros desconoció el derecho a la vida privada.')),
    ('m01_tratados', 'mg_lista', 55.6, 67.6, lista(
        'Que protegen',
        ('libro_ley', 'El artículo 11 de la Convención Americana', 56.2),
        ('mundo', 'El artículo 17 del Pacto de Derechos Civiles y Políticos', 60.1))),
    ('c04_responde', 'carton', 67.8, 74.6, c_ante('Y pide excluir esa información', '¿Qué responde?')),
    ('c05_extranjero', 'carton', 85.0, 90.2, c_tit('«Es derecho extranjero»', 'Y aquí se aplica la ley colombiana.')),
    ('c06_retirar', 'carton', 104.7, 117.9, c_tit(
        '«Mejor retirar la evidencia»',
        'El despacho pierde su línea de investigación más sólida sin que la defensa haya tenido que '
        'demostrar nada.')),
    ('m02_analisis', 'mg_lista', 119.0, 136.4, lista(
        None,
        ('libro_ley', 'Si el tratado obliga a Colombia', 123.1),
        ('balanza', 'Cuál es el estándar aplicable', 128.3),
        ('doc_check', 'Si el acto lo cumplió', 130.7),
        ('firma', 'Cómo se motiva la respuesta', 132.3))),
    ('c07_tercera', 'carton', 136.5, 143.3, cita('La tercera protege a la vez a la víctima y a la actuación.')),
    ('c08_pregunta', 'carton', 150.2, 158.2, cita(
        '¿De dónde vienen los estándares que usted aplica y cómo se sostienen?')),
    ('c09_primera', 'carton', 166.2, 181.9, c_ante(
        'Primera: las fuentes tienen un orden', 'Artículo 93 de la Constitución',
        'Los tratados de derechos humanos ratificados por Colombia entran al bloque de constitucionalidad.')),
    ('c10_aplicable', 'carton', 182.0, 187.1, cita('No son derecho extranjero: son Constitución aplicable.')),
    ('c11_segunda', 'carton', 187.2, 191.8, c_ante('Segunda', 'Cada tratado tiene quien lo interpreta')),
    ('m03_sistemas', 'mg_lista', 191.9, 206.6, lista(
        None,
        ('mundo', 'Sistema universal: los comités de las Naciones Unidas', 192.0),
        ('balanza', 'Sistema interamericano: la Comisión o la Corte', 196.2))),
    ('c12_estado', 'carton', 207.7, 218.0, c_tit(
        'El primer juez es el Estado mismo', 'Cada falla sostenida abre la puerta del examen internacional.')),
    ('c13_tercera', 'carton', 219.0, 227.5, c_ante(
        'Tercera', 'El control de convencionalidad',
        'Tarea de cualquier autoridad pública, no solo de los jueces.')),
    ('m04_pasos', 'mg_lista', 227.6, 244.7, lista(
        None,
        ('lupa_doc', 'Identificar la norma o práctica', 232.3),
        ('libro_ley', 'Identificar el estándar', 234.5),
        ('balanza', 'Contrastar, prefiriendo la interpretación conforme', 236.9),
        ('firma', 'Documentar el análisis', 240.6))),
    ('c14_regla', 'carton', 244.8, 252.6, c_tit(
        'Una regla de oro', 'Ningún estándar entra a su argumento sin verificarlo en la fuente oficial.')),
    ('c15_cita', 'carton', 252.7, 261.0, cita(
        'Un tratado bien citado fortalece su actuación; una cita inexacta la debilita.')),
]
