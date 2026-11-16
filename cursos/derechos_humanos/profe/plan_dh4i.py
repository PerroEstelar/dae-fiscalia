# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Derechos humanos aplicados a la función judicial» (16 nov 2026).

**Pedido.** Sebastián: «ahora lo mismo con el inicio de la unidad 4 de DDHH».

**Fuente.** `08. Video Inicio U4.mp4` del Drive de JP (`VIDEOS`), la toma cruda: 1620×1080,
30 fps parejos (7504 cuadros en 250,1 s), 16 Mb/s, BT.709, AAC estéreo. Mismo profe, fondo y
encuadre. Sin versión de Camtasia: STT (Scribe, WAV a 16 kHz, 567 palabras), cuadros y RMS en
ventanas de 50 ms. No hay arranques en falso, frases repetidas ni pausas largas (la más larga,
1,7 s antes de «Para decidir con fundamento…»), así que va entera.

**Unidad 4:** «Restringir con legitimidad: medidas de aseguramiento, privación de la libertad y
goce efectivo de los derechos de las Personas Privadas de la Libertad – PPL» (ficha, tal cual).

**Textos.** Sus palabras recortadas, contrastadas con la ficha de la U4 (video de bienvenida y
lección 2), que él amplía mucho. El STT oye «la inferencia razonable de autoridad o
participación»: la ficha dice «autoría o participación» (primera carga, art. 308 de la Ley 906), y
así va en pantalla.

**Gráficos.** Cartones (un antetítulo por cada cosa que entrega la cartilla: «Primero»,
«Segundo», «Tercero») y cinco listas de AE: las tres audiencias y la regla y la excepción (sin
título: con título no cabían), lo que la Fiscalía decide si pide, las tres cargas en orden y las
cuatro preguntas del test de Chaparro Álvarez (sin título). Quedan sin gráfico la extracción del teléfono, la audiencia con la
abogada Salgado y el producto de la unidad, para no pasar del 80 % de cobertura.

**v2 (16 nov 2026).** En la v1 la última fila de dos listas quedaba menos de 4 s: «Solicitud de
medida de aseguramiento» 2,9 s y «O se abstiene de pedirla» 1,8 s, y la lista ya se estaba yendo.
Se alargaron sobre la frase siguiente (`m01b`, `m03b`) y el cartón que sigue entra más tarde
(`c02b`, `c05b`); las claves nuevas dan archivos nuevos, para que Resolve no use la duración vieja
que tiene en caché. La v1 quedó en `_descartes`.

Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dh_profe import *  # noqa: E402,F401,F403
from base_dh_profe import CURSO, BIN_CURSO, cuadro_de, cita, c_tit, c_ante, lista  # noqa: E402

R = CURSO + '/UNIDAD 4 - INICIO PROFE'
BIN = BIN_CURSO + ['UNIDAD 4 - INICIO PROFE']
ORIGINAL = R + '/01 VIDEO/08. Video Inicio U4.mp4'
COMPUESTO = R + '/01 VIDEO/DH4I_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo dh u4 inicio.mp4'
SUB = ('Unidad 4. Restringir con legitimidad: medidas de aseguramiento, privación de la libertad y goce '
       'efectivo de los derechos de las Personas Privadas de la Libertad – PPL')
NOMBRE_LINEA = 'DH - U4 - INICIO PROFE'
EXPORT = 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 4 INICIO-v%d'
VERSION = 2
PREFIJO = 'DH4I'
TMP = 'D:/DAE/_tmp/dh_profe/dh4i'

PROFE = ('Yefri Yoel Torrado Verjel', 'Coautor del curso Derechos humanos aplicados a la función judicial')

TRAMOS = [(0.0, 250.1, None)]
T0, T1 = 0.0, 250.1
cuadro = cuadro_de(TRAMOS)

ITEMS = [
    ('lt01', 'lt', 1.0, 7.2, PROFE),
    ('c01_captura', 'carton', 7.3, 21.4, c_ante(
        'Semana diez', 'Wilmer Acosta, capturado en flagrancia',
        'Dejaba un nuevo panfleto en la emisora. Llevaba un arma de fuego sin permiso.')),
    ('m01b_audiencias', 'mg_lista', 37.6, 46.8, lista(
        None,
        ('mazo', 'Legalización de captura', 38.6),
        ('firma', 'Formulación de imputación', 40.7),
        ('balanza', 'Solicitud de medida de aseguramiento', 42.7))),
    ('c02b_libertad', 'carton', 46.8, 53.6, c_ante(
        'El momento más delicado de la función', 'Decidir sobre la libertad de una persona')),
    ('c03_otra_cara', 'carton', 54.7, 64.7, c_ante(
        'Hasta ahora, proteger', 'La otra cara de la doble incidencia: restringir derechos con legitimidad')),
    ('c04_art29', 'carton', 65.6, 78.3, c_ante(
        'Artículo 29 de la Constitución', 'Toda persona se presume inocente',
        'Mientras no se haya declarado judicialmente culpable, con sentencia ejecutoriada.')),
    ('m02_regla', 'mg_lista', 79.4, 90.7, lista(
        None,
        ('persona', 'La libertad es la regla', 81.6),
        ('balanza', 'Su restricción es la excepción', 83.3),
        ('mazo', 'Ninguna medida anterior a la condena es un castigo anticipado', 85.3))),
    ('m03b_decide', 'mg_lista', 101.2, 113.1, lista(
        'La Fiscalía decide si pide',
        ('carpeta', 'Una medida privativa de la libertad', 104.9),
        ('ruta', 'Una no privativa', 107.2),
        ('doc_check', 'O se abstiene de pedirla', 109.1))),
    ('c05b_detenida', 'carton', 113.2, 117.4, cita('Sin olvidar la perspectiva de la persona detenida.')),
    ('c06_incomodo', 'carton', 122.7, 135.5, c_ante(
        'Un ejercicio más incómodo y más útil', 'Los tres mejores argumentos contra su propia solicitud')),
    ('c07_primero', 'carton', 137.1, 145.8, c_ante(
        'La cartilla le entrega tres cosas', 'Primero: la estructura de la solicitud')),
    ('m04_cargas', 'mg_lista', 146.7, 160.3, lista(
        'Tres cargas, en orden',
        ('lupa_doc', 'Inferencia razonable de autoría o participación', 150.9),
        ('balanza', 'El fin legítimo', 153.7),
        ('doc_check', 'El tipo de medida', 156.2))),
    ('c08_chaparro', 'carton', 160.4, 170.8, c_ante(
        'Caso Chaparro Álvarez', 'El test de la Corte Interamericana',
        'Cuatro preguntas ante cada solicitud de medida.')),
    ('m05_test', 'mg_lista', 171.2, 186.1, lista(
        None,
        ('balanza', '¿Persigue un fin legítimo del proceso?', 171.3),
        ('lupa_doc', '¿Es idónea para alcanzarlo?', 174.0),
        ('escudo', '¿Es necesaria?', 176.3),
        ('mazo', '¿El sacrificio es proporcional?', 180.2))),
    ('c09_sustentada', 'carton', 186.2, 194.7, c_tit(
        'Cada respuesta debe estar sustentada',
        'En las evidencias y el material probatorio del expediente.')),
    ('c10_segundo', 'carton', 195.8, 209.3, c_ante(
        'Segundo', 'Garantías que no dependen del resultado',
        'Para la persona capturada y para la persona privada de la libertad.')),
    ('c11_tercero', 'carton', 209.8, 220.5, c_ante(
        'Tercero, un principio', 'Cuando una carga no se cumple',
        'La conclusión puede ser no pedir la medida o pedir una no privativa.')),
    ('c12_objetividad', 'carton', 220.6, 225.2, cita('Eso no es una derrota: es el deber de objetividad.')),
    ('c13_idea', 'carton', 234.8, 246.4, c_ante(
        'Lleve consigo una idea', 'La legitimidad de la restricción no se decreta: se sustenta, se controla y '
        'se revisa.')),
]
