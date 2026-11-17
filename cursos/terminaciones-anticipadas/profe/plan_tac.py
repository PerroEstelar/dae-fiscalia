# -*- coding: utf-8 -*-
r"""Cierre del curso de «Terminaciones anticipadas» (17 nov 2026).

**Fuente.** `ta_cierre_curso_fuente.mp4` (Drive del curso → VIDEOS,
`1AA096BLK_v7yd9aE3qISuidZvfX5M0nh`): grabación de Teams, 1280×720, 30 fps parejos (14.168
cuadros, 472,27 s), BT.601, AAC estéreo a −14,2 LUFS. Juan David Peña Gómez, leído al guion: STT
(Scribe, WAV a 16 kHz) de 1.086 palabras, de 0,66 a 471,60 s. Va entera. En 358,5 se traba
(«analizar qué, qué elementos deben te-- ser tenidos en cuenta»): se deja, y encima va la lista de
lo que piden las actividades.

**Textos.** Sus palabras recortadas. De las siete preguntas del «control de calidad» van en
pantalla las cuatro que duran lo bastante para leerse, cada una mientras la dice.

**Gráficos.** Cartones y listas de AE de cuatro filas como mucho, sin título (columna de 470).
En las enumeraciones de cinco (lo que hay que establecer, lo que puede generar una decisión
apresurada, en qué inciden las decisiones) queda fuera un término; las cinco respuestas del
final van en dos listas seguidas. Quedan sin gráfico, para que la imagen respire: el
agradecimiento del arranque, «No debemos comenzar por buscar una figura…», «El mecanismo no
puede ser una etiqueta…», «motivar significa hacer visible el razonamiento», «Tampoco debemos
confundir participación con transferencia de la decisión», las garantías en el archivo, la
preclusión y el principio de oportunidad, tres de las siete preguntas y la despedida.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ta_profe import *  # noqa: E402,F401,F403
from base_ta_profe import armar, PROFE, cita, c_tit, c_ante, lista  # noqa: E402

globals().update(armar('ta_cierre_curso_fuente.mp4', 'CIERRE DEL CURSO', 'Cierre del curso',
                       'TA - CURSO - CIERRE', 'terminacionesanticipadas - CURSO - CIERRE', 'TAC', 0, 14168))

ITEMS = [
    ('lt01', 'lt', 1.0, 9.0, PROFE),
    ('c02_archivo', 'carton', 34.2, 45.4, c_tit(
        'El archivo de la indagación',
        'Valorar si los hechos permiten una caracterización penal objetiva.')),
    ('c03_preclusion', 'carton', 45.5, 54.6, c_tit(
        'La preclusión', 'Identificar una causal legal y solicitar al juez de conocimiento que la examine.')),
    ('c04_oportunidad', 'carton', 54.7, 68.2, c_tit(
        'El principio de oportunidad',
        'En supuestos excepcionales y reglados, con un juicio de proporcionalidad y control judicial.')),
    ('c05_preacuerdos', 'carton', 69.1, 79.4, c_tit(
        'Los preacuerdos',
        'Una solución consensuada, pero dentro de límites que no pueden ser desplazados.')),
    ('c06_primera', 'carton', 79.5, 88.1, c_ante(
        'Primera enseñanza', 'La selección del mecanismo debe venir después de comprender el caso.')),
    ('m01_establecer', 'mg_lista', 94.1, 108.0, lista(
        None,
        ('lupa_doc', 'Qué ocurrió', 95.1),
        ('carpeta', 'Qué información tenemos', 96.3),
        ('balanza', 'Cuál es el problema jurídico', 99.7),
        ('mazo', 'Qué autoridad tiene competencia', 101.6))),
    ('c08_segunda', 'carton', 115.1, 122.0, c_ante(
        'Segunda enseñanza', 'La motivación siempre constituye una garantía.')),
    ('m02_motivar', 'mg_lista', 122.2, 148.0, lista(
        None,
        ('carpeta', 'Archivo: qué se investigó', 122.4),
        ('mazo', 'Preclusión: la causal y los hechos', 127.6),
        ('balanza', 'Oportunidad: la proporcionalidad', 133.5),
        ('apreton', 'Preacuerdos: qué se negoció', 142.1))),
    ('c10_tercera', 'carton', 162.3, 169.9, c_ante(
        'Tercera enseñanza', 'La eficiencia no puede medirse únicamente en tiempos o cifras.')),
    ('m03_apresurada', 'mg_lista', 170.8, 180.9, lista(
        None,
        ('doc_check', 'Impugnaciones', 171.8),
        ('ciclo', 'Reactivaciones', 172.8),
        ('mazo', 'Nulidades', 174.1),
        ('reloj', 'Audiencias fallidas', 174.9))),
    ('c11_valiosa', 'carton', 182.0, 192.2, c_tit(
        'La eficiencia jurídicamente valiosa', 'El mecanismo adecuado en el momento correcto.')),
    ('c12_victimas', 'carton', 194.1, 199.8, cita(
        'El lugar de las víctimas en todas estas instituciones.')),
    ('m04_victimas', 'mg_lista', 200.0, 231.0, lista(
        None,
        ('carpeta', 'Archivo: conocer las razones', 200.2),
        ('mazo', 'Preclusión: sus derechos e intereses', 208.0),
        ('balanza', 'Oportunidad: ser escuchadas', 214.1),
        ('apreton', 'Preacuerdos: su participación', 224.7))),
    ('c13_simbolica', 'carton', 231.9, 240.4, cita(
        'En ninguna de estas figuras la víctima debe convertirse en una presencia simbólica.')),
    ('c15_condena', 'carton', 249.8, 256.2, cita(
        'Escuchar a la víctima no significa prometer una condena.')),
    ('m05_significa', 'mg_lista', 256.4, 265.7, lista(
        None,
        ('mano_corazon', 'Comprender el daño', 256.9),
        ('balanza', 'Considerar sus intereses', 258.0),
        ('dialogo', 'Explicar la decisión', 259.7))),
    ('c16_garantias', 'carton', 266.2, 273.2, c_tit(
        'Las garantías del indiciado o procesado', 'Son igualmente esenciales.')),
    ('m06_preacuerdos', 'mg_lista', 288.6, 301.2, lista(
        None,
        ('firma', 'Aceptación libre, consciente e informada', 289.5),
        ('dialogo', 'Una defensa técnica', 293.8),
        ('libro_ley', 'Un beneficio con fundamento jurídico', 297.1))),
    ('c17_justicia', 'carton', 301.3, 307.7, cita(
        'La justicia no se fortalece sacrificando las garantías de una persona.')),
    ('c18_efectos', 'carton', 307.8, 315.2, cita(
        'Las decisiones de terminación anticipada tienen efectos que van más allá del caso.')),
    ('m07_inciden', 'mg_lista', 315.4, 329.6, lista(
        None,
        ('mano_corazon', 'La vida de las víctimas', 315.7),
        ('persona', 'Las personas procesadas', 317.4),
        ('grupos', 'La confianza ciudadana', 320.0),
        ('balanza', 'La legitimidad del sistema', 324.0))),
    ('m08_preguntarnos', 'mg_lista', 332.9, 344.0, lista(
        None,
        ('ruta', 'Qué finalidad cumple', 333.9),
        ('ciclo', 'Qué consecuencias produce', 336.3),
        ('dialogo', 'Si podemos justificarla públicamente', 338.1))),
    ('m09_actividades', 'mg_lista', 359.4, 370.6, lista(
        None,
        ('bifurcacion', 'Distinguir problemas', 360.4),
        ('ruta', 'Seleccionar mecanismos', 361.7),
        ('lupa_doc', 'Valorar elementos de conocimiento', 363.1),
        ('dialogo', 'Argumentar decisiones', 365.1))),
    ('c20_despachos', 'carton', 370.8, 376.9, c_ante(
        'Cuando regresen a sus despachos', 'Un control de calidad')),
    ('c21_problema', 'carton', 377.0, 382.7, cita('¿Qué problema estoy resolviendo realmente?')),
    ('c22_figura', 'carton', 386.1, 392.0, cita('¿Estoy utilizando la figura que corresponde?')),
    ('c23_defender', 'carton', 395.9, 403.0, cita(
        '¿Puedo defender la decisión ante el juez y ante una revisión posterior?')),
    ('c24_sostenible', 'carton', 403.1, 409.2, cita(
        '¿Una respuesta jurídicamente sostenible o simplemente una salida rápida?')),
    ('c25_proposito', 'carton', 409.3, 416.8, c_ante(
        'El propósito de este curso', 'Que cada actuación reciba la respuesta que corresponde')),
    ('m10_respuestas', 'mg_lista', 416.9, 427.5, lista(
        None,
        ('lupa_doc', 'Continuar investigando', 417.1),
        ('carpeta', 'Archivar', 420.3),
        ('mazo', 'Solicitar la preclusión', 423.3))),
    ('m11_respuestas', 'mg_lista', 427.6, 438.0, lista(
        None,
        ('balanza', 'Aplicar el principio de oportunidad', 427.8),
        ('apreton', 'Negociar', 432.3))),
    ('c26_legitimidad', 'carton', 438.4, 445.0, cita(
        'La legitimidad del sistema penal se construye en estas decisiones.')),
    ('c27_rigor', 'carton', 459.0, 467.6, cita(
        'Ejercer la función fiscal con rigor, objetividad y sensibilidad.')),
]
