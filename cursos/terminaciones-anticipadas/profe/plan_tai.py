# -*- coding: utf-8 -*-
r"""Inicio del curso de «Terminaciones anticipadas» (17 nov 2026).

**Fuente.** `ta_inicio_curso_fuente.mp4` (Drive del curso → VIDEOS,
`1YmOIgt9Qo49ayMXJm804QYeZWTUWjRDn`): grabación de Teams, 1280×720, 30 fps parejos (14.517
cuadros, 483,9 s), BT.601, AAC estéreo a −15,8 LUFS. Juan David Peña Gómez, leído al guion y de
corrido: STT (Scribe, WAV a 16 kHz) de 1.128 palabras, de 0,30 a 483,60 s, sin pausas de más de
2 s ni frases repetidas. Va entera.

**Textos.** Sus palabras recortadas. Las cuatro unidades se nombran como él las nombra
(«La primera unidad se ocupa del archivo de la indagación»…).

**Gráficos.** Cartones y siete listas de AE, todas de cuatro filas como mucho y sin título (la
columna es de 470): las cuatro figuras, lo que se estudia en la unidad 1, las causales de
preclusión, lo que exige examinar el principio de oportunidad, lo que puede la justicia
consensuada, de dónde parte la negociación, qué es motivar, las garantías y el propósito del
curso. En las enumeraciones de cinco, dos términos van en una fila. Quedan sin gráfico, para
que la imagen respire: «Quiero comenzar con una idea…», «En el sistema penal acusatorio…»,
«Esta manera de abordar los casos exige resistir dos automatismos», «La objetividad aquí
también obliga…», «La precisión importa…», «Motivar no consiste en llenar una decisión de
citas…», «Piensen en casos…» y la despedida.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_ta_profe import *  # noqa: E402,F401,F403
from base_ta_profe import armar, PROFE, cita, c_tit, c_ante, lista  # noqa: E402

globals().update(armar('ta_inicio_curso_fuente.mp4', 'INICIO DEL CURSO', 'Presentación del curso',
                       'TA - CURSO - INICIO', 'terminacionesanticipadas - CURSO - INICIO', 'TAI', 0, 14517))

ITEMS = [
    ('lt01', 'lt', 3.6, 11.6, PROFE),
    ('c01_juicio', 'carton', 18.9, 27.1, cita(
        'No todas las actuaciones penales culminan en el juicio oral.')),
    ('c03_bien', 'carton', 44.1, 56.5, c_tit(
        'Una actuación termina bien',
        'Cuando la decisión corresponde a la situación fáctica, jurídica y probatoria.')),
    ('m01_figuras', 'mg_lista', 75.0, 85.8, lista(
        None,
        ('carpeta', 'El archivo de la indagación', 75.3),
        ('mazo', 'La preclusión', 77.0),
        ('balanza', 'El principio de oportunidad', 78.1),
        ('apreton', 'Los preacuerdos', 79.8))),
    ('c05_confundir', 'carton', 86.8, 91.4, cita('Confundirlos no es un error de nomenclatura.')),
    ('c06_significar', 'carton', 91.6, 104.9, cita(
        'Puede significar que se evada un control judicial o que se cierre una posibilidad de '
        'respuesta para las víctimas.')),
    ('c07_pregunta', 'carton', 105.0, 113.7, c_ante(
        'El punto de partida del curso', '¿Qué problema tengo realmente enfrente?')),
    ('c08_noticia', 'carton', 115.1, 121.4, cita(
        '¿Hechos que no permiten caracterizar objetivamente un delito?')),
    ('c09_causal', 'carton', 121.5, 128.6, cita(
        '¿Una causal legal que impide continuar la acción penal?')),
    ('c10_hipotesis', 'carton', 128.7, 137.4, cita(
        '¿Una hipótesis excepcional que permite aplicar el principio de oportunidad?')),
    ('c11_consensuada', 'carton', 137.5, 144.6, cita(
        '¿Una posibilidad de justicia consensuada que puede construirse con la defensa?')),
    ('c12_primero', 'carton', 149.1, 158.6, c_ante(
        'Primer automatismo', 'La persecución a toda costa',
        'Impulsar el caso hasta obtener una condena.')),
    ('c13_segundo', 'carton', 163.9, 175.4, c_ante(
        'Segundo automatismo', 'El cierre por conveniencia',
        'La presión por los tiempos, la carga laboral o la dificultad de una investigación.')),
    ('c14_ni', 'carton', 175.5, 184.5, cita(
        'Ni la persecución indefinida ni el cierre apresurado son expresiones de una justicia '
        'responsable.')),
    ('c15_u1', 'carton', 184.6, 191.1, c_ante(
        'Primera unidad', 'El archivo de la indagación')),
    ('m02_u1', 'mg_lista', 192.7, 204.6, lista(
        None,
        ('bifurcacion', 'Archivo, inadmisión de denuncia y preclusión', 193.6),
        ('ciclo', 'Desarchivo y reactivación de la investigación', 198.8))),
    ('c17_u2', 'carton', 215.2, 227.4, c_ante(
        'Segunda unidad', 'La preclusión',
        'La decisión de terminar la actuación corresponde al juez de conocimiento.')),
    ('m03_causales', 'mg_lista', 236.6, 252.4, lista(
        None,
        ('balanza', 'La posibilidad de ejercer la acción', 236.9),
        ('lupa_doc', 'La existencia del hecho', 241.2),
        ('persona', 'La intervención de la persona', 244.5),
        ('escudo', 'La presunción de inocencia', 246.3))),
    ('c19_u3', 'carton', 260.0, 273.0, c_ante(
        'Tercera unidad', 'El principio de oportunidad',
        'Suspender, interrumpir o renunciar al ejercicio de la acción penal.')),
    ('c20_discrecional', 'carton', 274.7, 280.3, cita(
        'No es una autorización discrecional.')),
    ('m04_examinar', 'mg_lista', 280.4, 293.0, lista(
        None,
        ('lupa_doc', 'La causal y las prohibiciones', 281.1),
        ('balanza', 'El test de proporcionalidad', 283.8),
        ('personas', 'La situación de las víctimas', 286.8),
        ('mazo', 'El control judicial', 288.6))),
    ('c22_u4', 'carton', 301.7, 307.6, c_ante(
        'Cuarta unidad', 'Los preacuerdos y las negociaciones')),
    ('m05_consensuada', 'mg_lista', 308.5, 319.8, lista(
        None,
        ('mano_corazon', 'Humanizar la actuación', 309.4),
        ('reloj', 'Una respuesta oportuna', 311.1),
        ('apreton', 'La solución del conflicto', 313.3),
        ('personas', 'La reparación de las víctimas', 315.6))),
    ('c23_consenso', 'carton', 320.0, 327.2, cita(
        'El consenso no convierte la responsabilidad penal en un objeto de libre disposición.')),
    ('m06_negociacion', 'mg_lista', 327.4, 341.4, lista(
        None,
        ('lupa_doc', 'Hechos relevantes respaldados', 327.6),
        ('balanza', 'La congruencia y la calificación jurídica', 329.2),
        ('finanzas', 'La consecuencia punitiva', 333.4),
        ('mazo', 'Un control judicial', 336.8))),
    ('c24_hilo', 'carton', 341.5, 347.4, c_ante(
        'Un hilo común entre las cuatro unidades', 'La motivación')),
    ('m07_razonamiento', 'mg_lista', 354.0, 368.0, lista(
        None,
        ('lupa_doc', 'Qué hechos y qué información', 355.0),
        ('balanza', 'Qué problema jurídico se identifica', 358.6),
        ('bifurcacion', 'Por qué un mecanismo', 360.9),
        ('ruta', 'Cuáles son sus efectos', 363.8))),
    ('c26_victimas', 'carton', 377.5, 385.0, c_tit(
        'Los derechos de las víctimas', 'Presentes desde el inicio.')),
    ('m08_victimas', 'mg_lista', 385.1, 394.0, lista(
        None,
        ('dialogo', 'Informar', 385.8),
        ('ojo', 'Escuchar', 386.7),
        ('balanza', 'Considerar intereses', 387.5),
        ('doc_check', 'Explicar los efectos de la decisión', 388.9))),
    ('c27_veto', 'carton', 394.2, 401.8, cita(
        'Reconocer a las víctimas no significa atribuirles un poder de veto.')),
    ('c28_garantias', 'carton', 401.9, 408.0, c_tit(
        'Las garantías de la persona indiciada o procesada', 'Tampoco son negociables.')),
    ('m09_garantias', 'mg_lista', 408.1, 418.9, lista(
        None,
        ('escudo', 'La presunción de inocencia', 409.0),
        ('dialogo', 'El derecho de defensa', 410.7),
        ('libro_ley', 'El debido proceso y la legalidad', 412.4),
        ('firma', 'El consentimiento libre y voluntario', 414.7))),
    ('c30_criterio', 'carton', 437.2, 447.8, c_tit(
        'No buscamos respuestas automáticas',
        'Buscamos fortalecer el criterio para distinguir, verificar y argumentar.')),
    ('c31_respuesta', 'carton', 455.0, 462.4, c_ante(
        'El propósito', 'Dar a cada asunto la respuesta que jurídicamente corresponde')),
    ('m10_respuesta', 'mg_lista', 462.5, 477.3, lista(
        None,
        ('lupa_doc', 'Investigar', 462.7),
        ('doc_check', 'Terminar', 465.4),
        ('mazo', 'Acudir al juez', 468.1),
        ('apreton', 'Explorar soluciones', 471.3))),
]
