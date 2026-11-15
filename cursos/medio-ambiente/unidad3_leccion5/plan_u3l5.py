# -*- coding: utf-8 -*-
"""Unidad 3, lección 5 de Delitos ambientales: la prueba pericial (15 nov 2026).

**Pedido.** Sebastián: «preparar este, profe hablando a cámara… Unidad 3 lección 5.
Ya tiene intro, pero verifica todos los procesos necesarios, de pe a pa».

**Fuente.** Drive, curso → `VIDEOS/HUGO SALAZAR/INTRO Unidad 3 - HUGO ASCENCIO
SALAZAR - Leccion 5.mov`. Es un montaje de septiembre, no la grabación cruda:
- 1920×1080 a 23,976, Rec.709, 6:55 (9.949 cuadros);
- cuadros 0–193: el intro FGN;
- cuadro 194: uno de paso, oscuro;
- 195–9754: el profe, con el rótulo azul «HUGO ASCENCIO SALAZAR» quemado abajo a la
  izquierda todo el tiempo;
- 9755 en adelante: negro y el outro FGN.
- Audio en −21,1 LUFS y −2,9 dBTP. «Muchas gracias» termina en 406,87 s, justo antes
  del sonido del outro (406,92).

De ese archivo se usa solo el tramo del profe (`TRAMOS`), y se rearma todo con lo
nuestro. Así no queda el intro dos veces, y se cambia el rótulo quemado por el lower
third de la serie.

**Profe.** «Hola, yo soy Hugo Ascencio Salazar. Soy ingeniero químico de la
Universidad Nacional de Colombia. Tengo una maestría en Desarrollo Sostenible y Medio
Ambiente de la Universidad de Manizales. Soy profesional investigador del Grupo
Investigativo contra la Criminalidad Organizada para los delitos contra los Recursos
Naturales y el Medio Ambiente del Cuerpo Técnico de Investigación».

**Lección** (`plan_intros.UNIDADES[3]`): «La prueba pericial. En materia procesal
penal frente a los delitos ambientales».

**Ventana: 1472×828 desde (0, 50), ×1,30.** Se midió el profe (`perfil2.py`, 199
cuadros del tramo, en coordenadas de la fuente):
- cima de la cabeza: mín. 72, p2 79, p50 156;
- borde izquierdo a la altura de la caja: p2 490–550, p10 630–700;
- borde derecho de la cabeza: p98 1270, máx. 1474.

Lo que da:
- **El ancho** sale del borde derecho. Con menos de 1472 la cabeza se sale por la
  derecha cuando él se corre.
- **El alto** termina en y=878. El rótulo quemado empieza en y≈980 y queda fuera.
- **El panel** DAE/Fiscalía (y 87–231) entra entero.
- **La caja:** el profe empieza en x≈640–720 de salida (p2), así que la columna de
  texto es de 470 (`MAXW`), como en la introducción de Bienes.
- **El lower third** lleva el nombre a 36 px y el cargo a 420 de ancho, en tres
  renglones (`LT`): termina en x≈559. Al principio él está cerca y la camisa blanca
  empieza en x≈614; con el nombre a 40 px el texto blanco tocaba la camisa
  (simulado sobre ocho cuadros del tramo).

`MATRIZ_FUENTE` = bt709 (la de Teams es BT.601) y `FPS_COMPUESTO` = 23,976 (la
fuente ya va a esa cadencia; a 30 se duplicarían cuadros).

**Textos.** Salen de Scribe (WAV a 16 kHz), sin muletillas. EMP es «elementos
materiales probatorios».

Los tiempos están en segundos del archivo de Drive. En la línea, cuadro = 409 +
round((t − T0) · 23,976), con T0 el cuadro 195.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'herramientas',
                                'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
T0 = 195 / FPS                  # primer cuadro del profe en la fuente (8,133 s)
T1 = 9755 / FPS                 # primer cuadro negro antes del outro (406,865 s)
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
R = CURSO + '/UNIDAD 3/LECCION 5'
BIN = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE', 'UNIDAD 3', 'LECCION 5']
ORIGINAL = R + '/01 VIDEO/ambiental_unidad3_leccion5.mov'
COMPUESTO = R + '/01 VIDEO/U3L5_compuesto_v2.mp4'
TITULO = R + '/02 CARTONES/carton titulo ambientales u3 leccion 5.mp4'
TITULO_BASE = CURSO + '/UNIDAD 1/02 CARTONES/carton titulo ambientales u1v2.mp4'
SUB = 'Unidad 3. Lección 5'
NOMBRE_LINEA = 'MA - U3 - LECCION 5'
EXPORT = 'delitosambientales - U3 - LECCION 5-v%d'
PREFIJO = 'U3L5'
TMP = 'D:/DAE/_tmp/ma/u3l5'
XY, VENTANA = (0, 50), (1472, 828)
# sin el intro, el cuadro de paso ni el outro del montaje viejo. Los bordes van a mitad de cuadro:
# con T1 justo en el borde, el trim (que redondea a 3 decimales) se llevó el primer cuadro negro
# (el compuesto v1, en _descartes, tenía 9.561 cuadros y el último negro)
TRAMOS = [(194.5 / FPS, 9754.5 / FPS, None)]
MATRIZ_FUENTE = 'bt709'
FPS_FUENTE = FPS
FPS_COMPUESTO = '24000/1001'
MAXW = 470                      # columna de cartones y listas (estándar 615): el profe está al centro
LT = (36, 420)                  # lower third: px del nombre y ancho del cargo (estándar 48 y 900)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
MASTER_DIR = 'D:/DAE/_masters_archivo/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/UNIDAD 3/LECCION 5'

ANCHO = MAXW
NOMBRE_CURSO = ('Investigación y judicialización de delitos contra el medio ambiente y los '
                'recursos naturales')
PROFE = ('Hugo Ascencio Salazar', 'Ingeniero químico y magíster en Desarrollo Sostenible y Medio Ambiente')


def cuadro(t):
    return CLIP0 + int(round((t - T0) * FPS))


def _p(texto, peso, px, gap):
    # renglones parejos (herramientas/cartones/balanceo.py): sin palabras solas abajo
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def c_ante(ante, titulo, cuerpo=None):
    ls = _p(ante, 'med', ANTE, 0) + _p(titulo, 'bold', TIT, GAP_ANTE)
    if cuerpo:
        ls += _p(cuerpo, 'med', CUE, GAP_CUE + 8)
    return ls


def c_suelta(t):
    return _p(t, 'bold', SUELTA, 0)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}


ITEMS = [
    ('lt01', 'lt', 8.7, 20.4, PROFE),
    ('c01_cti', 'carton', 20.9, 32.7, c_tit(
        'Investigador del CTI',
        'Grupo Investigativo contra la Criminalidad Organizada en delitos ambientales.')),
    ('m01_experiencia', 'mg_lista', 37.4, 70.4, lista(
        'Su experiencia',
        ('reloj', 'Desde 1997, consultorías', 40.4),
        ('lupa_doc', 'Desde 2000, conceptos técnicos', 53.4),
        ('mineria', 'Minería y deforestación', 66.0))),
    ('m02_funcion', 'mg_lista', 71.0, 84.0, lista(
        'El perito debe',
        ('lupa_doc', 'Identificar', 74.5),
        ('lista', 'Seleccionar', 75.5),
        ('carpeta', 'Recolectar', 76.3),
        ('balanza', 'Y sobre todo, valorar', 77.9))),
    ('c02_demostrar', 'carton', 86.4, 96.3, c_tit(
        'Para demostrar',
        'Si una o varias presiones antrópicas ponen en peligro un recurso natural, el medio '
        'ambiente o la salud.')),
    ('c03_infraccion', 'carton', 96.5, 108.0, c_tit(
        'O para establecer',
        'Si esas presiones son solo una infracción ambiental de carácter administrativo.')),
    ('c05_programa', 'carton', 119.0, 129.9, c_tit(
        'Desde el programa metodológico',
        'El aporte investigativo del perito ambiental empieza en los aspectos probatorios.')),
    ('c06_juicio', 'carton', 130.2, 138.9, cita(
        'Inicia en la construcción de la hipótesis y finaliza en un eventual juicio oral, con su '
        'testimonio.')),
    ('c07_lugar', 'carton', 139.2, 151.5, c_tit(
        'El lugar de los hechos',
        'Ahí se plasman los conceptos técnicos, documentos, guías y procedimientos del perito.')),
    ('m03_establecer', 'mg_lista', 158.2, 179.3, lista(
        'Hay que establecer',
        ('lupa_doc', 'Qué elementos recolectar', 161.2),
        ('carpeta', 'Cómo', 171.2),
        ('mapa', 'Dónde', 172.7),
        ('ojo', 'Para qué', 174.8))),
    ('c08_no_todo', 'carton', 179.4, 191.6, cita(
        'No todo lo que observamos en una escena ambiental se convierte en un elemento material con '
        'capacidad demostrativa.')),
    ('c09_unica', 'carton', 192.2, 201.9, c_tit(
        'La importancia del perito',
        'Muchas veces es la única oportunidad de abordar esa escena ambiental.')),
    ('a01_campo', 'mg_act', 207.0, 221.6, act(
        'reloj_arena', 'El orden público', 'Priman el tiempo y la seguridad',
        'Minería ilegal y deforestación en zonas de grupos armados.')),
    ('m04_soportes', 'mg_lista', 224.5, 256.2, lista(
        None,
        ('matraz', 'Reportes de laboratorio', 227.5),
        ('bidon', 'Muestras de agua, suelo y sedimentos', 229.2),
        ('candado', 'Cadena de custodia', 238.2),
        ('lupa_doc', 'Metales pesados y otros analitos', 251.0))),
    ('c11_profesiones', 'carton', 268.6, 282.2, c_tit(
        'Profesionales',
        'Ingenieros forestales, químicos, ambientales y civiles, geógrafos, ecólogos, biólogos y '
        'microbiólogos.')),
    ('c12_equipo', 'carton', 292.0, 303.2, c_tit(
        'Trabajo en equipo',
        'Con el investigador y el fiscal de conocimiento, consolida nuevos hallazgos investigativos.')),
    ('a02_conexos', 'mg_act', 312.4, 325.0, act(
        'lupa_doc', 'Estos llevan a', 'Delitos conexos',
        'Por mala administración del recurso público o falta de sistemas de tratamiento adecuado.')),
    ('c14_ejemplo', 'carton', 330.0, 343.0, c_ante(
        'Por ejemplo', 'El químico aporta lo cuantitativo',
        'Para que el ambiental cuantifique la matriz de impacto del agua.')),
    ('c16_alcance', 'carton', 364.2, 378.7, c_tit(
        'No olvidemos',
        'El alcance del concepto ambiental depende de una selección adecuada de los EMP y la '
        'evidencia física a comparar.')),
    ('a03_comparacion', 'mg_act', 382.5, 395.9, act(
        'balanza', 'El éxito de un resultado', 'Siempre depende de la comparación',
        'Se comparan las presiones con líneas base para establecer los cambios.')),
    ('c17_cambio', 'carton', 397.0, 406.2, cita(
        'Si no se demuestra algún cambio, nos quedamos solo con una eventual infracción ambiental.')),
]
