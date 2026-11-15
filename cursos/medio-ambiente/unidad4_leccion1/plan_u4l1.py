# -*- coding: utf-8 -*-
"""Unidad 4, lección 1 de Delitos ambientales: justicia restaurativa (15 nov 2026).

**Pedido.** Sebastián: «este otro video con otra profe hablando a cámara… todo el
proceso de profe hablando a cámara, de pe a pa». Lleva:
- intro y outro;
- cartones de entrada y salida con el nombre del curso, y de subtítulo «Unidad 4.
  Lección 1»;
- lower thirds con el nombre y el cargo de la profe;
- cartones de apoyo y gráficos de AE.

**Fuente.** Drive, curso → `VIDEOS/ambiental_unidad4_leccion1`.
- Es una grabación de 27:36, 1280×720 a 30 fps (smpte170m), con el fondo virtual del
  edificio y el panel DAE/Fiscalía.
- Audio: AAC 44,1 kHz estéreo, −15,9 LUFS, pico +0,7 dBTP.
- Scribe: 4.377 palabras, una voz, sin pausas de más de 2 s.

**Profe.** «Soy Daniela Escallón, fiscal delegada ante la Unidad Nacional de Justicia
Restaurativa de la Fiscalía General de la Nación». No dice su formación académica,
así que el lower third lleva el cargo.

**Dos bloques en un archivo.**
1. 0:00–15:37: el caso de Tito, un malacatero de 59 años capturado en una mina
   ilegal de carbón en Boyacá, y su proceso restaurativo.
2. 15:38–27:36: cómo funciona la Unidad Nacional de Justicia Restaurativa.
- Entre los dos, la fuente trae una transición de cubo de medio segundo
  (937,65–938,20), con el panel DAE/Fiscalía deformado y fuera de cuadro. Se cambia
  por un corte seco en la pausa: desde 937,65 se ve el primer cuadro limpio del
  bloque 2 (938,20), quieto, y en 938,20 sigue el video. El audio no se toca. Sobre
  ese medio segundo se oyen la pausa y la primera sílaba de «Hola de nuevo»
  (`CONGELA`).
- El bloque 2 lleva su propio lower third, porque ella se vuelve a presentar.

**Ventana:** 1143×643 desde (0, 0), ×1,68.
- La profe está muy cerca de la cámara. Se midió sobre 663 cuadros, con el fondo
  calculado como la mediana:
  - la cima de la cabeza está en y≈70 (p2), 86 (p10) y 116 (p50); en algún cuadro
    llega a 49;
  - el mentón queda hacia y≈450–500;
  - el borde izquierdo, en las filas de la caja: p10 530–568 y p2 480–548. El pelo
    se abre a los lados más abajo, y cuando ella se inclina llega a x≈420.
- La ventana estándar (desde y=40) dejaba la coronilla a 15 px del borde de arriba.
  Desde y=0 queda a 80 px. Abajo corta solo pecho; a la derecha, la punta del
  hombro.
- El panel DAE/Fiscalía (x 127–595, y 52–157) entra entero.
- **Columna de 560 px** (`MAXW`): el texto llega hasta x≈730, que es x≈435 de la
  fuente. El estándar es 615, hasta x 785, y con la profe inclinada el texto le
  pisaba el pelo (simulado sobre nueve cuadros).
- **Lower third:** nombre a 48 px y cargo a 460 de ancho (`LT`), para que no llegue
  al saco blanco.

**Textos.** Salen de Scribe (WAV a 16 kHz), sin muletillas.
- «resolución dos once de dos mil veinticinco» es la Resolución 0211 de 2025 de la
  FGN (está en el SIDN de la Rama Judicial).
- «artículo cinco veintiuno» es el artículo 521 del Código de Procedimiento Penal.
- «DEMMA» se escribe DEMA, como en el resto del curso.

Los tiempos están en segundos de la fuente. En la línea, cuadro = 409 + round(t · 23,976).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'herramientas',
                                'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
R = CURSO + '/UNIDAD 4/LECCION 1'
BIN = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE', 'UNIDAD 4', 'LECCION 1']
ORIGINAL = R + '/01 VIDEO/ambiental_unidad4_leccion1.mp4'
COMPUESTO = R + '/01 VIDEO/U4L1_compuesto_v1.mp4'
TITULO = R + '/02 CARTONES/carton titulo ambientales u4 leccion 1.mp4'
TITULO_BASE = CURSO + '/UNIDAD 1/02 CARTONES/carton titulo ambientales u1v2.mp4'
SUB = 'Unidad 4. Lección 1'
NOMBRE_LINEA = 'MA - U4 - LECCION 1'
EXPORT = 'delitosambientales - U4 - LECCION 1-v%d'
PREFIJO = 'U4L1'
TMP = 'D:/DAE/_tmp/ma/u4l1'
XY, VENTANA = (0, 0), (1143, 643)
MAXW = 560                 # columna de cartones y listas (estándar 615): la profe está cerca
LT = (48, 460)             # lower third: px del nombre y ancho del cargo (estándar 48 y 900)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
MASTER_DIR = 'D:/DAE/_masters_archivo/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/UNIDAD 4/LECCION 1'
CONGELA = [(937.65, 938.20)]   # la transición de cubo de la fuente: se ve quieto el cuadro de 938,20

ANCHO = MAXW
NOMBRE_CURSO = ('Investigación y judicialización de delitos contra el medio ambiente y los '
                'recursos naturales')
PROFE = ('Daniela Escallón', 'Fiscal delegada ante la Unidad Nacional de Justicia Restaurativa')


def cuadro(t):
    return CLIP0 + int(round(t * FPS))


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
    # ------------------------------------------------------------ bloque 1: Tito
    ('lt01', 'lt', 0.4, 8.4, PROFE),
    ('c01_alcance', 'carton', 8.8, 24.8, c_tit(
        'Esta intervención',
        'El alcance y la aplicación de la justicia restaurativa en las investigaciones por delitos '
        'contra el medio ambiente y los recursos naturales.')),
    ('m01_bloques', 'mg_lista', 25.2, 46.2, lista(
        'Dos bloques',
        ('lupa_persona', 'Un caso de estudio', 28.6),
        ('edificio', 'La Unidad Nacional de Justicia Restaurativa', 37.9))),
    ('c02_quien', 'carton', 47.5, 54.0, c_suelta('¿Quién es Tito?')),
    ('c03_tito', 'carton', 54.8, 68.1, c_tit(
        'Tito',
        'Un hombre de 59 años capturado en flagrancia en una mina ilegal de carbón en Boyacá, '
        'acusado de tres delitos ambientales.')),
    ('c04_que_hacer', 'carton', 68.6, 76.0, cita('¿Qué vamos a hacer con Tito?')),
    ('m02_contexto', 'mg_lista', 86.7, 118.0, lista(
        None,
        ('persona', 'Campesino de 59 años', 88.3),
        ('libros', 'Estudió hasta primero de primaria', 95.8),
        ('familia', 'Esposa, dos hijas y cuatro nietos', 106.2),
        ('casa_lote', 'Pobreza multidimensional', 112.7))),
    ('c05_malacatero', 'carton', 118.6, 129.6, c_tit(
        'Malacatero',
        'Entre abril de 2021 y marzo de 2022 trabajó por jornal en una mina de carbón.')),
    ('c06_permisos', 'carton', 136.1, 143.6, cita(
        'Tito no sabía si la mina tenía los permisos y las licencias para trabajar.')),
    ('c07_mirada', 'carton', 145.5, 164.5, cita(
        'No busco que vean a Tito como una víctima, sino como una persona investigada con unas '
        'circunstancias y un contexto concretos. De esa mirada parte la justicia restaurativa.')),
    ('c08_eslabon', 'carton', 169.1, 184.8, c_tit(
        'Un eslabón muy bajo de la cadena',
        'No era el propietario ni el administrador. Fue quien atendió a quienes llegaron a hacer '
        'el allanamiento.')),
    ('c09_captura', 'carton', 194.1, 206.7, cita(
        'En marzo de 2022 capturaron en flagrancia al administrador de la mina y a Tito, que '
        'maniobraba el malacate.')),
    ('c10_unidad', 'carton', 211.5, 224.0, c_ante(
        '2026', 'Un proceso restaurativo',
        'Se solicita el acompañamiento de la Unidad Nacional de Justicia Restaurativa.')),
    ('c11_momento1', 'carton', 236.9, 248.2, c_ante(
        'Tres momentos', 'Primero: entender quién era Tito',
        'Una caracterización restaurativa del ofensor.')),
    ('m03_capacidad', 'mg_lista', 252.2, 276.2, lista(
        'Su capacidad de',
        ('mano_corazon', 'Responsabilizarse por sus actos', 255.2),
        ('apreton', 'Proponer procesos de reparación', 262.4),
        ('ojo', 'Comprender el daño', 270.7))),
    ('c12_ciclo', 'carton', 276.6, 288.8, c_tit(
        'El daño ambiental',
        'Lo identifican peritos expertos, y repararlo es un ciclo que requiere mucho tiempo.')),
    ('c13_pregunta', 'carton', 300.4, 311.1, cita(
        '¿Qué puede reparar Tito, y en cuánto tiempo, para aportar a la recuperación ambiental?')),
    ('c14_momento2', 'carton', 311.3, 323.7, c_ante(
        'Segundo momento', 'Encontrarnos con el daño',
        'Peritos que determinen el daño al suelo, al aire y a las aguas.')),
    ('c15_comunitario', 'carton', 340.3, 354.3, c_tit(
        'Un poco más allá',
        'El daño no solo se da a los recursos naturales: la persona investigada también tiene que '
        'comprenderlo.')),
    ('c16_momento3', 'carton', 372.9, 386.1, c_ante(
        'Tercer momento', 'El mejor mecanismo de justicia restaurativa',
        'La reparación del daño frente a una mirada punitiva.')),
    ('c17_difusa', 'carton', 407.0, 417.8, c_tit(
        '¿Alcanza la justicia restaurativa?',
        'La objeción: en estos delitos la víctima es difusa.')),
    ('c18_colectivo', 'carton', 420.6, 434.7, cita(
        'El bien jurídico es colectivo y lo representan instituciones del Estado: no hay una '
        'víctima ni un daño individualizados.')),
    ('c19_vuelta', 'carton', 443.0, 458.9, c_tit(
        'Darle la vuelta a la objeción',
        'Las personas investigadas pueden tener mejores capacidades para reparar y para dar '
        'garantías de no repetición.')),
    ('m04_victimas', 'mg_lista', 472.4, 484.9, lista(
        'Dos víctimas institucionales',
        ('edificio', 'La Corporación Autónoma Regional', 475.8),
        ('engranaje', 'Acerías Paz del Río', 478.9))),
    ('c20_dialogos', 'carton', 486.4, 499.0, cita(
        'Las víctimas decidieron participar en unos diálogos sobre el daño y sobre lo que podían '
        'esperar de Tito.')),
    ('c21_capacidad', 'carton', 514.8, 530.2, cita(
        'Tito identificó que su capacidad de reparación era mayor, y que debía hacerse esas '
        'preguntas para no incurrir en conductas delictivas.')),
    ('c22_hoy', 'carton', 540.3, 554.7, cita(
        'Hoy Tito entiende que su trabajo es importante, pero que tiene que hacerse en el marco de '
        'ejercicios legales y legalizados.')),
    ('c23_participacion', 'carton', 566.0, 580.1, c_tit(
        'La participación de las víctimas',
        'Garantiza que la justicia esté orientada a la reparación y que haya garantías de no '
        'repetición.')),
    ('m05_arboles', 'mg_lista', 584.1, 621.9, lista(
        'La reparación',
        ('brote', 'Propone sembrar 500 árboles', 587.1),
        ('lupa_doc', 'Para la CAR no son suficientes', 594.1),
        ('manos_brote', 'Se compromete a sembrar 800', 617.1))),
    ('m06_tiene_que', 'mg_lista', 622.0, 632.5, lista(
        'Tito tiene que',
        ('billete', 'Adquirir los árboles', 622.6),
        ('brote', 'Sembrarlos', 625.2),
        ('reloj', 'Garantizar que vivan', 626.5))),
    ('c24_responsabilidad', 'carton', 642.9, 657.3, c_tit(
        'Ya no es una responsabilidad objetiva',
        'Reconoce que la siembra es necesaria, pone recursos y cuida los árboles para que vivan.')),
    ('c25_restauracion', 'carton', 679.8, 692.7, c_tit(
        'Restauración ecológica',
        'Núcleos de árboles nativos para recuperar coberturas vegetales y estabilizar el suelo.')),
    ('c26_posible', 'carton', 706.4, 717.8, cita(
        'Aunque no haya una víctima directa, los diálogos son posibles y la participación es '
        'posible.')),
    ('c27_tramite', 'carton', 723.4, 739.9, c_tit(
        'No fue de mero trámite',
        'La participación de las víctimas mejoró la propuesta de reparación y acompañó a Tito para '
        'que la reparación fuera efectiva.')),
    ('c28_impacto', 'carton', 743.0, 758.2, cita(
        'No es una justicia acrítica: la reparación tiene que tener un efecto en las víctimas, en '
        'la sociedad y sobre todo en estos delitos.')),
    ('c29_servicio', 'carton', 765.8, 778.6, cita(
        'La justicia restaurativa está al servicio del derecho penal, y las instituciones '
        'jurídico-penales, al servicio de la justicia restaurativa.')),
    ('c30_no_conciliables', 'carton', 779.0, 795.8, c_tit(
        'Tres delitos con penas altas',
        'No eran mediables ni conciliables: hay otros mecanismos de terminación anticipada que '
        'sirven en un proceso restaurativo.')),
    ('c31_causal7', 'carton', 800.9, 815.2, c_ante(
        'Principio de oportunidad', 'Causal 7',
        'La suspensión del procedimiento a prueba a través de un proceso de justicia restaurativa.')),
    ('m07_proceso', 'mg_lista', 817.1, 831.0, lista(
        None,
        ('dialogo', 'Diálogos con el ofensor y con la víctima', 819.0),
        ('doc_check', 'Un plan de reparación diseñado en conjunto', 822.8),
        ('brote', 'Su ejecución en la suspensión a prueba', 826.8))),
    ('c32_comunitaria', 'carton', 831.1, 841.9, c_tit(
        'Reparación comunitaria',
        'Además de sembrar los árboles, Tito tuvo un rol en su comunidad.')),
    ('c33_cartillas', 'carton', 859.7, 874.3, cita(
        'Cartillas de educación en protección del medio ambiente, a partir de la experiencia de '
        'Tito, que él entregará a su comunidad.')),
    ('c34_acompanadas', 'carton', 885.6, 899.2, c_tit(
        'Con la DEMA y la Unidad',
        'Cada daño al medio ambiente y a los recursos naturales tarda mucho tiempo en ser '
        'restaurado.')),

    # ------------------------------------------------------------ bloque 2: la Unidad
    ('lt02', 'lt', 938.2, 944.8, PROFE),
    ('c35_unidad', 'carton', 945.2, 958.0, c_tit(
        'La Unidad Nacional de Justicia Restaurativa',
        'Cómo funciona y cuál es su visión de la justicia restaurativa en la Fiscalía.')),
    ('c36_resolucion', 'carton', 958.3, 967.3, c_tit(
        'Resolución 0211 de 2025',
        'Expedida por la fiscal general de la Nación.')),
    ('c37_transversal', 'carton', 970.8, 985.5, c_tit(
        'Una unidad transversal',
        'Acompaña a todas las direcciones cuando los fiscales consideran posible un plan de '
        'reparación efectivo.')),
    ('a01_responsabilizacion', 'mg_act', 1006.9, 1019.5, act(
        'mano_corazon', 'Primera finalidad', 'La responsabilización del ofensor',
        'Que entienda que hay una víctima y un daño que merecen ser reparados.')),
    ('a02_reparacion', 'mg_act', 1039.7, 1050.7, act(
        'escudo', 'Segunda finalidad', 'Las necesidades de reparación de las víctimas',
        'A veces la privación de la libertad no es suficiente.')),
    ('a03_vinculos', 'mg_act', 1072.1, 1080.2, act(
        'apreton', 'Tercera finalidad', 'Restablecer los vínculos sociales',
        'Los que el delito rompe.')),
    ('c38_acompanar', 'carton', 1098.4, 1114.8, cita(
        'La Unidad acompaña a los fiscales en la búsqueda de diálogos asertivos entre procesados y '
        'víctimas, que lleven a planes de reparación efectivos.')),
    ('m08_mecanismos', 'mg_lista', 1122.2, 1142.0, lista(
        'Planes de reparación',
        ('dialogo', 'Mediación y conciliación (art. 521)', 1125.2),
        ('balanza', 'Principio de oportunidad', 1136.1),
        ('apreton', 'Preacuerdo', 1137.4))),
    ('c39_ampliar', 'carton', 1142.4, 1153.2, cita(
        'El proceso de reparación y de diálogo puede acompañar incluso la sanción penal en un '
        'preacuerdo.')),
    ('c40_dialogicos', 'carton', 1153.9, 1168.6, c_tit(
        'Ejercicios dialógicos',
        'Víctimas y procesados diseñan de manera conjunta planes de reparación que acompañan los '
        'procesos penales.')),
    ('c41_dema', 'carton', 1171.9, 1188.3, c_tit(
        'Con la DEMA',
        'Identificar los daños y darles una respuesta diferenciada con el principio de oportunidad '
        'o con preacuerdos con enfoque restaurativo.')),
    ('m09_comprender', 'mg_lista', 1215.8, 1229.0, lista(
        'Para un plan efectivo',
        ('persona', 'Quiénes son los investigados', 1218.8),
        ('manos_brote', 'Su capacidad de reparar', 1221.2),
        ('escudo', 'Las necesidades de las víctimas', 1223.7))),
    ('c42_tramites', 'carton', 1229.4, 1244.2, c_tit(
        'Una particularidad',
        'Las víctimas institucionales tienen trámites internos para evaluar los mecanismos de '
        'terminación anticipada.')),
    ('c43_activas', 'carton', 1247.6, 1263.1, cita(
        'Las víctimas en estos delitos son muy activas, y eso favorece la justicia restaurativa: '
        'permite nivelar sus expectativas de reparación.')),
    ('c44_no_todas', 'carton', 1270.5, 1283.0, cita(
        'No todas las personas procesadas por delitos ambientales tienen capacidad económica de '
        'resarcir el daño.')),
    ('c45_no_pago', 'carton', 1288.7, 1302.3, c_tit(
        'La reparación no siempre es un pago',
        'También parte de entender el fenómeno criminal que hay detrás de estos delitos.')),
    ('c46_correspondencia', 'carton', 1308.8, 1317.7, cita(
        'El contexto se estudia para que la reparación corresponda al daño.')),
    ('c47_test', 'carton', 1329.5, 1345.6, c_tit(
        'Esa correspondencia es clave',
        'Para el test de proporcionalidad de un principio de oportunidad y para unas garantías de '
        'no repetición efectivas.')),
    ('c48_estratificacion', 'carton', 1361.3, 1375.3, c_tit(
        'Una estratificación del fenómeno',
        'No es la misma responsabilidad la de un malacatero que la del dueño de una mina ilegal.')),
    ('c49_cada_quien', 'carton', 1387.1, 1401.0, cita(
        'Entender cómo se divide el trabajo permite comprender qué puede reparar cada quien y cuál '
        'es la mejor respuesta penal.')),
    ('m10_principios', 'mg_lista', 1401.5, 1414.8, lista(
        'Dos principios en tensión',
        ('balanza', 'Discrecionalidad', 1403.8),
        ('mazo', 'Máxima contundencia', 1408.8))),
    ('c50_contundencia', 'carton', 1426.3, 1442.2, cita(
        'Si los eslabones bajos reparan con un principio de oportunidad, es más fácil lograr la '
        'máxima contundencia contra los máximos responsables.')),
    ('m11_permite', 'mg_lista', 1472.0, 1511.2, lista(
        None,
        ('ojo', 'Comprender mejor el contexto', 1473.0),
        ('lupa_doc', 'Acceder a la verdad del fenómeno', 1475.5),
        ('brote', 'Reparación ambiental y comunitaria', 1481.6),
        ('mazo', 'Contundencia contra los máximos responsables', 1502.8))),
    ('c51_fines', 'carton', 1517.4, 1532.1, c_tit(
        'Fines constitucionales e interamericanos',
        'Un uso proporcional del derecho penal y la privación de la libertad como última ratio.')),
    ('c52_celere', 'carton', 1534.8, 1546.4, cita(
        'El legislador previó estos mecanismos para un acceso a la justicia célere, pronto y '
        'económico.')),
    ('c53_profunda', 'carton', 1550.2, 1565.3, cita(
        'La justicia restaurativa hace que esos mecanismos sean profundos y justos: garantías de no '
        'repetición y acceso real a la justicia.')),
    ('c54_humana', 'carton', 1568.9, 1586.1, c_tit(
        'El enfoque restaurativo',
        'Un mínimo daño del proceso penal en las personas, planes de reparación efectivos y '
        'relaciones restablecidas de manera más humana.')),
    ('c55_juicio', 'carton', 1601.8, 1617.1, c_tit(
        'También cuando hay juicio',
        'Mejora los incidentes de reparación integral y prepara a las víctimas para la '
        'judicialización y la sanción.')),
    ('c56_complementario', 'carton', 1627.7, 1644.2, cita(
        'La justicia restaurativa es complementaria al ejercicio del fiscal: da mejores respuestas '
        'a las necesidades de las comunidades y de las víctimas.')),
]
