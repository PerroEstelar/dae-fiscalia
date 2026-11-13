# -*- coding: utf-8 -*-
"""Plan de gráficos de los siete videos de profes del curso SRPA y justicia
restaurativa (11 nov 2026).

Molde: las introducciones de Delitos ambientales (`MA - U1 - INTRODUCCION`):
    V1  intro FGN 0–194 · clip compuesto desde el 409 · cartón de título de cierre
        (zoom 1,16, pan 145) · outro FGN
    V2  cartón de título 194–409 (nombre del curso y, debajo, la unidad) + cartones de caja
    V3  motion graphics de After Effects (aftr)
    V4  lower third
    A1  audio del intro, del clip y del outro

Todo va en la caja de la izquierda (x 62–790, y 250–720, anclado abajo en y=690)
con el dibujo de cartones_v3; el lower third va abajo a la izquierda, como el de
«Diana Carolina Florez Vallona» de la U1 de Delitos ambientales.

Los tiempos son SEGUNDOS DE LA FUENTE (la transcripción de Scribe en
`03 VOCES/stt/SRPA_<video>_stt.json`); `srpa.a_salida` los pasa al clip
compuesto (que en la u1b y la u3d lleva cortes). En la línea:
cuadro = 409 + round(a_salida(t) · 23,976).

Los textos son verbatim de lo que dice el profe, sin muletillas ni repeticiones;
lo único que se toma de la ficha del curso son los nombres oficiales de las
unidades y la grafía de los nombres propios (Manuel Enrique López Betancur,
Gabriela Rodríguez Beltrán). Las cifras van en dígitos.

Tipos:
    lt        lower third: (nombre, cargo)
    carton    cartón de caja: [(texto, peso, px, gap)]
    mg_act    After Effects: ícono + antetítulo, título (puede ser None) y cuerpo
    mg_lista  After Effects: título (puede ser None) y filas (ícono, rótulo, segundo)
              que entran cuando el profe las nombra
"""
import srpa as S

CLIP0 = 409
FPS = 24000 / 1001

ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16


def cuadro(clave, t):
    """Cuadro de LÍNEA del segundo t de la fuente."""
    return CLIP0 + int(round(S.a_salida(clave, t) * FPS))


def cita(t):
    return [(t, 'bold', TIT, 0)] if len(t) <= 78 else [(t, 'med', CUE, 0)]


def c_tit(titulo, cuerpo):
    return [(titulo, 'bold', TIT, 0), (cuerpo, 'med', CUE, GAP_TIT)]


def c_suelta(t):
    return [(t, 'bold', SUELTA, 0)]


def c_unidad(n, cuerpo=None):
    ls = [('Unidad %d' % n, 'med', ANTE, 0), (S.UNIDADES[n], 'bold', TIT, GAP_ANTE)]
    if cuerpo:
        ls.append((cuerpo, 'med', CUE, GAP_CUE + 8))
    return ls


def c_leccion(n, titulo):
    return [('Lección %d' % n, 'med', ANTE, 0), (titulo, 'bold', TIT, GAP_ANTE)]


def c_ante(ante, cuerpo):
    return [(ante, 'med', ANTE, 0), (cuerpo, 'med', CUE, GAP_ANTE)]


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}


ITEMS = {}

# --------------------------------------------------------------------------
# Presentación del curso — Estanislao Escalante Barreto (15:21)
ITEMS['curso'] = [
    ('lt01', 'lt', 19.3, 28.4, S.ESTANISLAO),
    ('c01_juventud', 'carton', 84.5, 94.4, cita(
        'Cómo comprendemos la juventud, cómo vemos la relación de los adolescentes con la '
        'cuestión criminal y con la cuestión penal.')),
    ('c02_cinco_unidades', 'carton', 96.0, 102.9, c_suelta('Cinco unidades temáticas')),
    ('c03_u1', 'carton', 103.4, 111.8, c_unidad(1)),
    ('c04_lenguaje', 'carton', 112.0, 128.9, c_tit(
        'La importancia del uso del lenguaje',
        'Cuál es el concepto de niñez más actual, más contemporáneo.')),
    ('c05_u2', 'carton', 129.4, 137.6, c_unidad(2)),
    ('c06_autoridades', 'carton', 137.8, 149.6, cita(
        'Cuáles son las autoridades del sistema, cuáles son sus roles: su enfoque diferencial, '
        'especializado, educativo y pedagógico.')),
    ('c07_u3', 'carton', 150.1, 158.0, c_unidad(3)),
    ('c08_pedagogico', 'carton', 168.5, 178.0, cita(
        'El principio pedagógico es transversal a toda la ley de infancia y adolescencia.')),
    ('c09_practicas', 'carton', 188.5, 202.4, cita(
        'Las prácticas restaurativas nos pueden permitir comprender la pedagogía del sistema '
        'y volverla una realidad material.')),
    ('c10_u4', 'carton', 202.8, 210.4, c_unidad(4)),
    ('c11_u5', 'carton', 210.6, 219.0, c_unidad(5)),
    ('c12_limitar', 'carton', 223.8, 237.6, cita(
        'Los requisitos que se deben tener en cuenta cuando se trata de limitar los derechos '
        'fundamentales de los adolescentes.')),
    ('c13_competencia', 'carton', 249.5, 263.8, c_tit(
        'Competencia general',
        'Que el servidor aplique los principios, las normas, los procedimientos y las '
        'competencias institucionales del sistema en actuaciones de investigación y '
        'judicialización.')),
    ('c14_competencia_b', 'carton', 264.0, 277.8, cita(
        'Incorporando el enfoque de justicia restaurativa para garantizar el debido proceso, '
        'la protección integral del adolescente y la atención de las necesidades de las víctimas.')),
    ('c15_cinco_competencias', 'carton', 279.0, 284.4, c_suelta('Cinco competencias específicas')),
    ('m01_comp1', 'mg_act', 284.6, 300.0, act(
        'bombilla', 'Competencia específica 1', None,
        'Comprenda la relación existente entre el sistema de responsabilidad para adolescentes, '
        'sus principios y fines con la política criminal del Estado colombiano.')),
    ('m02_comp2', 'mg_act', 327.0, 344.0, act(
        'balanza', 'Competencia específica 2', None,
        'Aplique estándares constitucionales e internacionales de derechos humanos en las '
        'actuaciones del sistema de responsabilidad penal de adolescentes.')),
    ('m03_comp3', 'mg_act', 352.0, 368.0, act(
        'bifurcacion', 'Competencia específica 3', None,
        'Aplique el principio de oportunidad, articulándolo con la justicia restaurativa y la '
        'protección integral, para adoptar decisiones motivadas.')),
    ('m04_comp4', 'mg_act', 373.9, 390.6, act(
        'apreton', 'Competencia específica 4', None,
        'Aplicar herramientas y estrategias de justicia restaurativa orientadas a la reparación '
        'del daño, la participación de las víctimas y la responsabilidad del adolescente.')),
    ('m05_comp5', 'mg_act', 391.0, 405.0, act(
        'libros', 'Competencia específica 5', None,
        'Identifique la finalidad pedagógica de las medidas y las sanciones del sistema de '
        'responsabilidad penal.')),
    ('c16_experiencia', 'carton', 421.0, 428.6, cita('Un modelo de aprendizaje basado en la experiencia.')),
    ('c17_insumo', 'carton', 446.5, 462.4, cita(
        'Que su experiencia, su conocimiento y su actividad profesional sean el insumo más importante.')),
    ('c18_algo_nuevo', 'carton', 462.7, 471.6, cita(
        'Cada vez que usted toma una decisión respecto de un problema jurídico, está creando algo nuevo.')),
    ('m06_ciclo', 'mg_lista', 479.2, 514.0, lista(
        None,
        ('carpeta', 'Experiencia concreta: el análisis de casos reales', 480.7),
        ('ojo', 'Observación reflexiva', 490.8),
        ('bombilla', 'Conceptualización abstracta', 495.3),
        ('engranaje', 'Experimentación activa: dilemas judiciales reales', 508.4))),
    ('m07_horas', 'mg_act', 514.2, 524.6, act(
        'reloj', 'El curso', '48 horas lectivas', 'Equivalentes a un crédito académico.')),
    ('c19_compromiso', 'carton', 529.5, 537.2, cita(
        'Con su compromiso, con su dedicación y especialmente con su esfuerzo.')),
    ('c20_ligero', 'carton', 545.4, 551.4, cita(
        'Un curso ligero, práctico, pero no por ello menos profundo.')),
    ('m08_rutina', 'mg_lista', 559.2, 578.9, lista(
        None,
        ('reloj', 'Un horario específico para entrar todos los días', 561.0),
        ('video', 'Revisar minuciosamente los videos introductorios', 568.7),
        ('doc_check', 'Participar activamente en sus tareas de autoformación', 572.8))),
    ('m09_lugar', 'mg_lista', 579.1, 596.0, lista(
        None,
        ('escritorio', 'Un lugar donde pueda concentrarse y tomar nota', 579.3),
        ('libreta', 'Lo que va aprendiendo y lo que va reflexionando', 588.5))),
    ('c21_anexos', 'carton', 598.5, 609.2, cita(
        'Tengan en cuenta los casos, los anexos: allí está el insumo fundamental para dinamizar '
        'su proceso de aprendizaje.')),
    ('m10_evaluacion', 'mg_lista', 613.5, 631.6, lista(
        'La evaluación',
        ('ciclo', 'Continua y permanente', 615.4),
        ('doc_check', 'Evaluaciones acumulativas y sumativas', 623.4))),
    ('m11_unidades', 'mg_lista', 632.0, 653.0, lista(
        None,
        ('torta', 'Cada unidad temática: el 20 % de la calificación', 634.6),
        ('ruta', 'Al final de cada unidad, una evaluación para pasar a la siguiente', 645.2))),
    ('c22_memoria', 'carton', 653.3, 660.8, cita(
        'No son evaluaciones de memoria o de fechas o de datos concretos.')),
    ('c23_competencias', 'carton', 661.0, 676.4, cita(
        'Se trata de evaluaciones que le permitan identificar si están cumpliendo las competencias.')),
    ('lt02', 'lt', 678.0, 687.0, S.ESTANISLAO),
    ('m12_perspectivas', 'mg_lista', 687.6, 756.0, lista(
        'Tres perspectivas',
        ('birrete', 'Desde la academia', 692.5),
        ('edificio', 'Como servidor público en la Defensoría del Pueblo', 710.5),
        ('mazo', 'Como asesor litigante', 745.2))),
    ('c24_responden', 'carton', 770.5, 786.0, cita(
        'Los adolescentes no son responsables como un adulto, pero sí responden penalmente en un '
        'sistema especial diferenciado.')),
    ('m13_carlos', 'mg_act', 801.2, 816.6, act(
        'persona', 'Docente autor', 'Carlos Humberto Ramírez Romero',
        'Juez penal del circuito para adolescentes con función de conocimiento.')),
    ('m14_manuel', 'mg_act', 817.1, 847.8, act(
        'persona', 'Docente autor', 'Manuel Enrique López Betancur',
        'Abogado especialista en derecho penal, con mucha experiencia en el ejercicio profesional y '
        'docente.')),
    ('m15_gabriela', 'mg_act', 848.5, 866.8, act(
        'persona', 'Auxiliar de investigación', 'Gabriela Rodríguez Beltrán',
        'Abogada con estudios de especialización en instituciones jurídico-penales.')),
    ('m16_jaime', 'mg_act', 867.2, 894.0, act(
        'persona', 'Invitado experto', 'Jaime Ignacio Acosta Aristizábal',
        'Jurista y consultor internacional senior, con más de 40 años de trayectoria.')),
    ('c25_fundamentos', 'carton', 899.0, 913.2, cita(
        'Cómo se llegó al sistema en el que estamos, cuál es su estructura, sus fines, sus '
        'fundamentos.')),
]

# --------------------------------------------------------------------------
# Unidad 1, bienvenida — Estanislao Escalante Barreto (8:39). Entre 256,55 y
# 277,10 se quita la toma falsa y hasta 303,8 va acercado: ahí no hay gráficos.
ITEMS['u1b'] = [
    ('lt01', 'lt', 1.8, 9.6, S.ESTANISLAO),
    ('c01_relacion', 'carton', 17.5, 32.5, cita(
        'La relación existente entre el sistema de responsabilidad penal para los adolescentes, '
        'sus principios y fines, y la política criminal del Estado colombiano.')),
    ('c02_enfoque', 'carton', 33.5, 46.0, cita(
        'Conforme a un enfoque garantista de derechos humanos, diferencial e inclusive desde una '
        'perspectiva transnacional.')),
    ('c03_sujetos', 'carton', 56.0, 71.0, cita(
        'Los adolescentes como sujetos de derechos de especial protección constitucional, aunque '
        'estén en conflicto con la ley penal.')),
    ('c04_u1', 'carton', 71.8, 81.2, c_unidad(1)),
    ('c05_lenguaje', 'carton', 107.5, 126.9, cita(
        'Sensibilizarnos sobre cuáles son esos principios, esos valores y especialmente el uso del '
        'lenguaje de la infancia y la adolescencia.')),
    ('c06_cuatro', 'carton', 127.6, 132.6, c_suelta('Cuatro lecciones')),
    ('c07_l1', 'carton', 132.9, 146.6, c_leccion(1, 'El sentido de un sistema especial y diferenciado')),
    ('c08_tutelar', 'carton', 155.5, 171.4, cita(
        'Antes primaba otro tipo de modelos de justicia tutelar, que no estaba relacionada con la '
        'protección integral, sino con modelos de situación irregular.')),
    ('c09_l2', 'carton', 174.8, 184.2, c_leccion(2, 'El enfoque diferencial en un sistema penal en '
                                                  'permanente construcción')),
    ('c10_adultos', 'carton', 184.5, 196.0, cita('No se trata de un sistema penal igual que el de los adultos.')),
    ('c11_diverso', 'carton', 218.4, 236.2, cita(
        'Colombia es un país supremamente diverso: se requiere de un enfoque diferencial para '
        'hacer realidad la justicia material.')),
    ('c12_l3', 'carton', 236.8, 246.4, c_leccion(3, 'Los principios orientadores de la responsabilidad '
                                                  'penal de los niños, niñas y adolescentes')),
    ('c13_constitucional', 'carton', 310.9, 324.0, cita(
        'Uno de los derechos más constitucionalizados en la historia de nuestro ordenamiento '
        'jurídico es el derecho de infancia-adolescencia.')),
    ('c14_dogmatica', 'carton', 358.0, 370.3, cita('La dimensión dogmática penal.')),
    ('m01_principios', 'mg_lista', 370.8, 388.2, lista(
        'Principios',
        ('mano_corazon', 'Interés superior del niño, la niña y el adolescente', 376.8),
        ('balanza', 'Prevalencia de los derechos', 381.1),
        ('circulo', 'Corresponsabilidad', 384.0),
        ('puerta_salida', 'No sanción', 386.3))),
    ('m02_principios_b', 'mg_lista', 388.3, 404.3, lista(
        'Principios',
        ('libros', 'Educativo y pedagógico', 388.3),
        ('bifurcacion', 'Principio de oportunidad', 394.1),
        ('apreton', 'Justicia restaurativa', 396.2))),
    ('c15_procesal', 'carton', 413.8, 422.0, cita('La dimensión procesal.')),
    ('c16_escenario', 'carton', 432.0, 441.0, cita(
        'El proceso penal debe entenderse como un escenario educativo y pedagógico.')),
    ('c17_l4', 'carton', 452.9, 463.0, c_leccion(4, 'El marco normativo internacional, nacional e '
                                                  'institucional')),
    ('c18_punitivo', 'carton', 473.0, 482.2, cita(
        'No es un sistema punitivo, no es un sistema de castigo, no es un sistema retributivo.')),
    ('c19_sujetos', 'carton', 482.4, 497.4, cita(
        'Los adolescentes no son criminales en potencia: son sujetos de derecho de especial '
        'protección constitucional.')),
    ('c20_ultima', 'carton', 500.8, 513.2, cita(
        'Como última ratio, la privación de la libertad, y la sanción con sentido educativo y '
        'restaurativo.')),
]

# --------------------------------------------------------------------------
# Unidad 3, bienvenida — Carlos Humberto Ramírez Romero (3:43)
ITEMS['u3b'] = [
    ('lt01', 'lt', 24.4, 34.6, S.CARLOS),
    ('c01_tesis', 'carton', 62.3, 76.5, cita(
        'Mi tesis de maestría estuvo relacionada con el principio de oportunidad del sistema de '
        'responsabilidad penal para adolescentes.')),
    ('c02_cuatro', 'carton', 100.5, 106.4, c_suelta('Cuatro lecciones')),
    ('c03_l1', 'carton', 106.6, 116.2, c_leccion(1, 'El principio de oportunidad en el sistema de '
                                                  'responsabilidad penal para adolescentes')),
    ('c04_l2', 'carton', 116.4, 123.8, c_leccion(2, 'Las prácticas restaurativas y el principio de '
                                                  'oportunidad')),
    ('c05_l3', 'carton', 124.0, 129.5, c_leccion(3, 'El principio de remisión de casos o medidas '
                                                  'extrajudiciales')),
    ('c06_l4', 'carton', 129.6, 139.0, c_leccion(4, 'La justicia terapéutica, el principio de '
                                                  'oportunidad y las audiencias de seguimiento')),
    ('m01_acompanamiento', 'mg_lista', 166.6, 180.4, lista(
        None,
        ('persona', 'Acompañamiento del docente', 168.4),
        ('ciclo', 'Seguimiento continuo', 173.4),
        ('doc_check', 'Retroalimentación de las evaluaciones', 174.7),
        ('libros', 'Recapitulación final de la unidad', 177.6))),
    ('c07_reflexion', 'carton', 193.5, 206.0, cita(
        'Mediante preguntas de reflexión, preguntas conceptuales y una aplicación de lo aprendido.')),
    ('m02_horas', 'mg_lista', 206.8, 216.0, lista(
        None,
        ('reloj', '8 horas de trabajo autónomo', 208.4),
        ('portatil', '2 horas de orientación virtual', 210.4))),
]

# --------------------------------------------------------------------------
# Unidad 3, desarrollo — Carlos Humberto Ramírez Romero (39:31). Termina en
# «Muchas gracias.» (2.363 s): lo que sigue es una charla con el técnico.
ITEMS['u3d'] = [
    ('lt01', 'lt', 1.0, 9.5, S.CARLOS),
    ('c01_diferencias', 'carton', 18.3, 35.0, cita(
        'Las diferencias del principio de oportunidad en el sistema penal acusatorio de la Ley 906 '
        'frente a la Ley 1098 de 2006, Código de la Infancia y la Adolescencia.')),
    ('m01_ley906', 'mg_act', 64.0, 85.4, act(
        'libro_ley', 'Ley 906 de 2004', 'Una excepción a la regla general',
        'La regla general es el principio de oficiosidad: la Fiscalía, en todos los casos, debe '
        'adelantar la investigación.')),
    ('m02_ley1098', 'mg_act', 85.8, 106.2, act(
        'familia', 'Ley 1098 de 2006', 'Un mandato general de aplicación preferente',
        'Artículo 174 del Código de la Infancia y la Adolescencia.')),
    ('c02_reglado', 'carton', 138.0, 152.8, cita(
        'En el sistema de adolescentes sigue siendo reglado por unas causales, pero ya no va a ser '
        'limitado a esas causales.')),
    ('m03_instrumentos', 'mg_lista', 204.5, 230.0, lista(
        'Instrumentos internacionales',
        ('mundo', 'Regla 11 de Beijing', 207.6),
        ('libro_ley', 'Observación general 24 de 2019', 210.0),
        ('mano_corazon', 'Convención de los Derechos del Niño, artículo 40', 217.4))),
    ('c03_limites', 'carton', 250.0, 280.4, cita(
        'En la Ley 906 tenemos límites normativos: la oportunidad procesal hasta antes de la '
        'audiencia de juzgamiento y las prohibiciones del artículo 199 de la Ley 1098.')),
    ('c04_no_aplicables', 'carton', 281.3, 292.0, cita(
        'Esas prohibiciones son aplicables a la Ley 906, mas no son aplicables al Código de la '
        'Infancia y la Adolescencia.')),
    ('c05_remision', 'carton', 293.0, 312.0, cita(
        'Por expresa aplicación de principios de derecho internacional, como el de remisión de casos.')),
    ('m04_etapa', 'mg_lista', 344.0, 368.4, lista(
        None,
        ('calendario', 'En cualquier etapa: hasta antes de que adquiera firmeza la sentencia', 346.0),
        ('balanza', 'En todos los casos y en todos los delitos, con el test estricto de proporcionalidad',
         359.7))),
    ('c06_facilitar', 'carton', 370.0, 392.4, cita(
        'Los fiscales delegados deberán facilitar la aplicación del principio de oportunidad y '
        'adoptar una interpretación favorable de la ley.')),
    ('c07_ajena', 'carton', 480.0, 497.0, cita(
        'La figura del principio de oportunidad es propia de los sistemas penales acusatorios: es '
        'una figura ajena a los sistemas de justicia penal juvenil.')),
    ('c08_adecuado', 'carton', 508.4, 528.6, cita(
        'Lo adecuado es desarrollar el concepto de remisión de casos o medidas extrajudiciales.')),
    ('c09_sin_desarrollo', 'carton', 548.0, 560.4, cita(
        'Esa figura del principio de remisión no tiene un desarrollo normativo interno en Colombia.')),
    ('c10_herramienta', 'carton', 611.8, 638.0, cita(
        'El principio de oportunidad se constituye en una herramienta para encauzar normativamente '
        'el principio de remisión de casos.')),
    ('m05_programas', 'mg_lista', 640.2, 660.0, lista(
        'Programas alternativos',
        ('apreton', 'De justicia restaurativa', 646.6),
        ('mano_corazon', 'De justicia terapéutica', 648.6))),
    ('m06_test', 'mg_lista', 692.0, 721.0, lista(
        'Principio de proporcionalidad',
        ('doc_check', 'Idoneidad', 700.6),
        ('bifurcacion', 'Necesidad', 701.8),
        ('balanza', 'Estricta proporcionalidad', 702.5))),
    ('c11_beijing', 'carton', 742.4, 762.6, c_tit(
        'Reglas de Beijing',
        'Reglas mínimas de las Naciones Unidas para la administración de justicia de menores.')),
    ('c12_bloque', 'carton', 764.0, 785.0, c_tit(
        'Bloque de constitucionalidad',
        'Un documento de derecho blando que termina siendo vinculante: sentencias C-203 de 2005 y '
        'C-684 de 2009.')),
    ('c13_regla11_1', 'carton', 817.1, 835.0, c_ante(
        'Regla 11.1 · Remisión de casos',
        'Se examinará la posibilidad, cuando proceda, de ocuparse de los menores delincuentes sin '
        'recurrir a las autoridades competentes para que los juzguen oficialmente.')),
    ('c14_regla11_2', 'carton', 835.0, 856.8, c_ante(
        'Regla 11.2',
        'La policía, el Ministerio fiscal y otros organismos que se ocupen de los casos de '
        'delincuencia de menores estarán facultados para fallar dichos casos discrecionalmente, '
        'sin necesidad de vista oficial.')),
    ('c15_regla11_3', 'carton', 857.0, 876.4, c_ante(
        'Regla 11.3',
        'Toda remisión que signifique poner a disposición de las instituciones pertinentes de la '
        'comunidad o de otro tipo estará supeditada al consentimiento del menor o al de sus padres '
        'o su tutor.')),
    ('c16_regla11_4', 'carton', 876.6, 890.0, c_ante(
        'Regla 11.4',
        'Se procurará facilitar a la comunidad programas de supervisión y orientación temporales, '
        'restitución y compensación a las víctimas.')),
    ('c17_cdn40', 'carton', 902.0, 923.6, c_ante(
        'Convención de los Derechos del Niño, artículo 40',
        'Siempre que sea apropiado y deseable, se deberán adoptar medidas para tratar a los niños '
        'sin recurrir a procedimientos judiciales.')),
    ('c18_como', 'carton', 924.6, 931.0, c_suelta('¿Cómo aplicamos el principio de oportunidad?')),
    ('m07_resolucion', 'mg_act', 1005.0, 1024.0, act(
        'doc_check', 'Fiscalía General de la Nación', 'Resolución 0351 de 2025',
        'Fundamental para la aplicación del principio de oportunidad en el sistema de '
        'responsabilidad penal para adolescentes.')),
    ('c19_causales', 'carton', 1028.4, 1043.0, c_tit(
        'Artículo 1',
        'Las causales son las mismas que se aplican en el sistema penal acusatorio de adultos.')),
    ('c20_directa', 'carton', 1043.7, 1069.8, c_tit(
        'Artículo 2: aplicación directa',
        'Ya no se requieren autorizaciones, vistos buenos o validaciones.')),
    ('c21_fiscal_caso', 'carton', 1070.3, 1090.6, cita(
        'El fiscal del caso, cualquiera sea su categoría, aplicará directamente el principio de '
        'oportunidad y lo presentará para su legalización ante el juez de control de garantías.')),
    ('m08_procedimiento', 'mg_lista', 1104.0, 1141.6, lista(
        None,
        ('lupa_doc', 'Verificar que no haya sido beneficiado por la misma conducta', 1107.3),
        ('calendario', 'Registrar el inicio de conversaciones con la defensa', 1130.8),
        ('dialogo', 'Conversaciones con la defensa, el postulante y la víctima', 1134.8))),
    ('m09_procedimiento_b', 'mg_lista', 1142.4, 1205.0, lista(
        None,
        ('firma', 'Acta de compromiso en las causales 4, 5 y 17', 1150.1),
        ('doc_check', 'Registrar si se llegó a un acuerdo', 1161.4),
        ('mazo', 'Control de legalidad ante el juez de control de garantías', 1191.8))),
    ('lt02', 'lt', 1206.4, 1215.4, S.CARLOS),
    ('c22_minimo', 'carton', 1228.0, 1246.0, c_tit(
        'Mínimo probatorio',
        'Debe permitir inferir al menos autoría y tipicidad de la conducta.')),
    ('c23_victimas', 'carton', 1274.0, 1301.0, c_tit(
        'La participación de las víctimas',
        'Deben estar enteradas del trámite y participar en él, independientemente de que se opongan.')),
    ('c24_causal7', 'carton', 1325.0, 1347.0, c_tit(
        'Numeral 7 del artículo 324',
        'La suspensión del procedimiento a prueba en el marco de la justicia restaurativa.')),
    ('c25_excelencia', 'carton', 1347.6, 1368.0, cita(
        'Es la causal por excelencia del sistema de responsabilidad penal para adolescentes.')),
    ('c26_seguimiento', 'carton', 1370.4, 1384.0, cita(
        'Esa causal va a permitir que se realicen audiencias de seguimiento.')),
    ('c27_199', 'carton', 1458.0, 1472.0, cita(
        'El artículo 199 de la Ley 1098 también establece limitaciones que impiden la aplicación del '
        'principio de oportunidad en todos los delitos.')),
    ('m10_t142', 'mg_act', 1473.0, 1493.0, act(
        'mazo', 'Corte Constitucional', 'Sentencia T-142 de 2019',
        'Delitos contra menores de edad que afecten la integridad y formación sexual.')),
    ('c28_herramienta', 'carton', 1501.2, 1520.0, cita(
        'El principio de proporcionalidad es la herramienta que permite superar los límites '
        'normativos.')),
    ('c29_absolutas', 'carton', 1573.2, 1590.0, cita(
        'Esas restricciones, esas prohibiciones, no son absolutas en el sistema de responsabilidad '
        'penal para adolescentes.')),
    ('m11_caso', 'mg_lista', 1590.4, 1620.6, lista(
        None,
        ('familia', 'Poco rango de diferencia de edad entre el ofensor y la víctima', 1598.3),
        ('mano_corazon', 'No se había presentado violencia', 1604.7),
        ('apreton', 'Las partes, interesadas en un mecanismo alternativo', 1608.9))),
    ('c30_excepcion', 'carton', 1640.0, 1661.0, cita(
        'Aplicar la excepción de inconstitucionalidad frente a la prohibición normativa.')),
    ('c31_pregunta', 'carton', 1705.0, 1730.0, c_tit(
        'La pregunta',
        '¿Se puede extender esa posición de la Corte a la totalidad de límites normativos que '
        'restringen la aplicación del principio de oportunidad?')),
    ('c32_respuesta', 'carton', 1760.0, 1777.0, cita(
        'Debe ser extendida a la totalidad de límites normativos y jurisdiccionales existentes.')),
    ('c33_alexy', 'carton', 1791.9, 1809.0, c_tit(
        'Robert Alexy',
        'Una colisión de principios se define a través del principio de ponderación o balanceo, el '
        'principio de proporcionalidad.')),
    ('m12_csj', 'mg_act', 1884.4, 1917.0, act(
        'mazo', 'Corte Suprema de Justicia', 'Radicación 60553',
        'Sentencia SP3520 de 2022: la remisión de casos en un escenario diferente al del principio '
        'de oportunidad.')),
    ('c34_art142', 'carton', 1918.0, 1941.0, c_tit(
        'Artículo 142 de la Ley 1098',
        'No serán juzgados ni declarados penalmente responsables los menores de 14 años, ni los de '
        '14 a 18 años que presenten una discapacidad psíquica o mental.')),
    ('c35_bienestar', 'carton', 1955.0, 1973.4, cita(
        'Le corresponde al juez de adolescentes hacer la remisión del caso a las instancias del '
        'Sistema Nacional de Bienestar Familiar.')),
    ('m13_fiscal', 'mg_lista', 2032.0, 2085.0, lista(
        'El fiscal delegado',
        ('lupa_persona', 'Acreditar la relación de la conducta con la discapacidad', 2041.2),
        ('carpeta', 'Aportar el dictamen pericial', 2054.7),
        ('mazo', 'Solicitar la remisión a programas extrajudiciales', 2064.4))),
    ('lt03', 'lt', 2085.3, 2094.2, S.CARLOS),
    ('c36_terapeutica', 'carton', 2140.0, 2154.4, c_tit(
        'Justicia terapéutica',
        'Considerar la ley, el proceso, el procedimiento como un agente terapéutico.')),
    ('c37_positivos', 'carton', 2170.0, 2182.4, cita(
        'Que los efectos de la intervención del proceso en el adolescente sean positivos.')),
    ('m14_tribunales', 'mg_act', 2195.0, 2232.0, act(
        'edificio', 'En el derecho comparado', 'Tribunales de solución de problemas',
        'Los más famosos, los tribunales de tratamiento de drogas: una alternativa al encarcelamiento.')),
    ('m15_restaurativa', 'mg_lista', 2233.4, 2256.0, lista(
        'Justicia restaurativa',
        ('persona', 'Responsabilización en el ofensor', 2241.6),
        ('mano_corazon', 'Reparación a las víctimas', 2244.0),
        ('circulo', 'Reintegración a la comunidad', 2245.3))),
    ('c38_audiencias', 'carton', 2256.3, 2280.0, c_tit(
        'Audiencias de seguimiento judicial',
        'Determinar si el adolescente está cumpliendo con los objetivos de intervención del proceso.')),
    ('c39_acuerdo', 'carton', 2328.0, 2348.0, cita(
        'Acuerdo 11995 de 2022 del Consejo Superior de la Judicatura.')),
]

# --------------------------------------------------------------------------
# Unidad 3, cierre — Carlos Humberto Ramírez Romero (11:21)
ITEMS['u3c'] = [
    ('lt01', 'lt', 2.4, 11.0, S.CARLOS),
    ('c01_rector', 'carton', 16.2, 32.0, c_tit(
        'Código de la Infancia y la Adolescencia',
        'El principio de oportunidad como un principio rector de aplicación preferente.')),
    ('c02_mandato', 'carton', 32.8, 52.6, cita(
        'Un mandato general del sistema aplicable en todos los delitos, en todos los asuntos.')),
    ('c03_spa', 'carton', 58.3, 71.2, c_tit(
        'Sistema penal acusatorio',
        'El principio de oportunidad es una excepción al principio de oficiosidad de la Fiscalía.')),
    ('c04_srpa', 'carton', 71.7, 90.4, c_tit(
        'Sistema de adolescentes',
        'El principio de oportunidad termina siendo un mandato general, y la excepción, el principio '
        'de oficiosidad.')),
    ('c05_alexy', 'carton', 99.0, 117.8, c_tit(
        'Robert Alexy',
        'Los principios como mandatos de optimización: cuando entran en conflicto, debe hacerse uso '
        'del principio de proporcionalidad.')),
    ('c06_t142', 'carton', 160.0, 185.6, c_tit(
        'Sentencia T-142 de 2019',
        'Reglas de decisión para hacer uso del principio de oportunidad en delitos sexuales contra '
        'menores de edad, a pesar de la prohibición del artículo 199.')),
    ('m01_test', 'mg_lista', 192.0, 214.0, lista(
        'Test estricto de proporcionalidad',
        ('doc_check', 'Idoneidad', 200.0),
        ('bifurcacion', 'Necesidad', 200.9),
        ('balanza', 'Proporcionalidad estricta', 201.6))),
    ('c07_pesa', 'carton', 263.0, 275.4, cita('¿Cuál de esas dos pesa más en el caso concreto?')),
    ('c08_extensiva', 'carton', 355.8, 377.0, cita(
        'La regla de decisión de esa sentencia puede hacerse extensiva a todos los delitos del '
        'sistema de responsabilidad penal para adolescentes.')),
    ('m02_resolucion', 'mg_act', 388.0, 430.0, act(
        'doc_check', 'Procedimiento interno', 'Resolución 0351 de 2025',
        'Aplicación directa del principio de oportunidad por parte del fiscal delegado; el juez '
        'realiza el control de legalidad.')),
    ('m03_remision', 'mg_lista', 434.3, 466.0, lista(
        'Remisión de casos o medidas extrajudiciales',
        ('mano_corazon', 'Convención de los Derechos del Niño, artículo 40', 444.9),
        ('mundo', 'Regla 11 de Beijing', 454.3),
        ('libro_ley', 'Observación general 24', 459.0))),
    ('c09_margen', 'carton', 478.0, 501.8, cita(
        'Mantener a los niños al margen del proceso judicial en cualquier momento: antes, durante e '
        'inclusive después de la sentencia.')),
    ('c10_propia', 'carton', 506.0, 522.6, cita(
        'La remisión de casos es una figura propia de los sistemas de justicia penal juvenil; el '
        'principio de oportunidad, del sistema penal acusatorio de adultos.')),
    ('m04_csj', 'mg_act', 560.6, 607.0, act(
        'mazo', 'Corte Suprema de Justicia', 'Radicación 60553',
        'Sentencia SP3520 de 2022: en casos de discapacidad psíquica o mental debe hacerse uso del '
        'principio de remisión.')),
    ('c11_terapeutica', 'carton', 640.0, 670.0, c_tit(
        'Justicia terapéutica',
        'La causal número séptima: audiencias de seguimiento para verificar el avance que ha tenido '
        'el joven.')),
    ('lt02', 'lt', 671.0, 679.8, S.CARLOS),
]

# --------------------------------------------------------------------------
# Unidad 4, cierre — Carlos Humberto Ramírez Romero (9:01)
ITEMS['u4c'] = [
    ('lt01', 'lt', 1.2, 9.6, S.CARLOS),
    ('c01_definiciones', 'carton', 14.0, 26.2, cita(
        'Repasamos las definiciones conceptuales de justicia restaurativa y de justicia terapéutica.')),
    ('m01_origenes', 'mg_lista', 36.6, 60.6, lista(
        None,
        ('circulo', 'Comunidades indígenas en Canadá, Nueva Zelanda y Estados Unidos', 45.1),
        ('grupos', 'Comunidades religiosas como la menonita', 49.7),
        ('libros', 'Howard Zehr: El pequeño libro de la justicia restaurativa', 54.1))),
    ('m02_terapeutica', 'mg_act', 60.7, 87.0, act(
        'edificio', 'Justicia terapéutica', 'Tribunales especializados en resolución de problemas',
        'En los Estados Unidos, en especial los de adicciones, desde los años ochenta.')),
    ('c02_impacto', 'carton', 95.0, 114.0, cita(
        'Que el impacto de ese proceso sea positivo, buscando la solución de los problemas que han '
        'generado la vinculación del adolescente.')),
    ('c03_dano', 'carton', 150.0, 168.0, c_tit(
        'Justicia restaurativa',
        'El énfasis no es en el delito, sino en el daño ocasionado a la comunidad o al otro.')),
    ('c04_victima', 'carton', 169.0, 182.4, cita(
        'No puede haber proceso o programa de justicia restaurativa de espaldas a la víctima.')),
    ('m03_zehr', 'mg_lista', 212.0, 237.0, lista(
        'Howard Zehr',
        ('lupa_persona', '¿Quién fue el dañado?', 222.2),
        ('mano_corazon', '¿Cuáles son sus necesidades?', 226.1),
        ('persona', '¿Quién tiene la responsabilidad de atender esas necesidades?', 228.2))),
    ('c05_causal', 'carton', 248.0, 267.0, c_tit(
        'Numeral 7 del artículo 324',
        'La suspensión del procedimiento a prueba en el marco de la justicia restaurativa.')),
    ('c06_seguimiento', 'carton', 283.0, 300.0, cita(
        'Audiencias de seguimiento judicial durante el tiempo de suspensión del proceso a prueba.')),
    ('c07_ordenes', 'carton', 312.0, 337.8, cita(
        'Emitir órdenes judiciales para garantizar un cumplimiento más estricto, o brindar muestras de '
        'felicitación y de apoyo.')),
    ('c08_renuncia', 'carton', 340.0, 359.6, cita(
        'Solamente al cumplir con todas las condiciones se puede resolver sobre la renuncia al '
        'ejercicio de la acción penal.')),
    ('m04_componentes', 'mg_lista', 386.0, 439.0, lista(
        'Procesos de justicia restaurativa',
        ('persona', 'Responsabilización del ofensor', 402.7),
        ('mano_corazon', 'Reparación a la víctima', 412.0),
        ('circulo', 'Reintegración en la comunidad', 424.7))),
    ('c09_efectos', 'carton', 444.0, 461.2, cita(
        'Sus resultados restaurativos deben ser utilizados en el proceso y el fiscal delegado debe '
        'otorgarles efectos jurídicos.')),
    ('c10_directrices', 'carton', 464.0, 490.0, c_tit(
        'Directrices',
        'Sistema Nacional de Coordinación de Responsabilidad Penal para Adolescentes.')),
    ('c11_mediacion', 'carton', 498.0, 513.6, c_tit(
        'Mediación penal', 'Mecanismo de justicia restaurativa.')),
    ('lt02', 'lt', 514.9, 523.4, S.CARLOS),
]

# --------------------------------------------------------------------------
# Unidad 5, cierre — Carlos Humberto Ramírez Romero (17:43)
ITEMS['u5c'] = [
    ('lt01', 'lt', 0.8, 9.5, S.CARLOS),
    ('c01_medidas', 'carton', 9.6, 22.2, c_tit(
        'Medidas restrictivas de derechos',
        'La más importante durante la indagación y la investigación: el internamiento preventivo.')),
    ('c02_art181', 'carton', 30.0, 46.0, c_tit(
        'Código de la Infancia y la Adolescencia, artículo 181',
        'Los requisitos para la utilización de la medida de internamiento preventivo.')),
    ('c03_regla13', 'carton', 55.2, 80.0, c_tit(
        'Regla 13 de Beijing',
        'El último recurso: solo puede ser utilizado cuando ya se han agotado todas las opciones '
        'posibles.')),
    ('m01_finalidades', 'mg_lista', 130.5, 159.3, lista(
        None,
        ('personas', 'Protección de la comunidad', 135.2),
        ('lupa_doc', 'Preservación de la prueba', 137.2),
        ('mano_corazon', 'Protección de las víctimas', 138.8),
        ('libros', 'Finalidades pedagógicas, educativas y restaurativas', 142.5))),
    ('c04_art308', 'carton', 217.9, 248.4, c_tit(
        'Artículo 308',
        'La inferencia razonable: si el imputado puede ser autor o partícipe de la conducta.')),
    ('m02_termino', 'mg_act', 275.7, 302.4, act(
        'reloj_arena', 'Internamiento preventivo', '4 meses',
        'Prorrogable por motivación un mes más; vencido el término, podrá sustituirse por una '
        'medida diferente.')),
    ('c05_control', 'carton', 317.0, 334.6, c_tit(
        'Actos de investigación',
        'El control judicial previo y posterior es el mismo que en el sistema penal acusatorio de '
        'adultos.')),
    ('c06_plus', 'carton', 398.0, 422.2, cita(
        'Un control adicional: la Convención de los Derechos del Niño, el interés superior, las '
        'reglas de Beijing y la presencia del defensor de familia.')),
    ('c07_finalidad', 'carton', 462.3, 474.6, cita(
        'Supeditadas a la finalidad educativa, protectora y restaurativa del sistema de adolescentes.')),
    ('c08_sanciones', 'carton', 485.0, 508.2, c_tit(
        'Las sanciones',
        'Privativas de la libertad en los eventos regulados por el artículo 187 del Código de la '
        'Infancia y la Adolescencia.')),
    ('m03_inciso1', 'mg_act', 509.0, 535.4, act(
        'calendario', 'Artículo 187, inciso 1', 'Edad y naturaleza del delito',
        'Entre 16 y 18 años, y un delito con pena mínima igual o superior a 6 años.')),
    ('m04_inciso3', 'mg_act', 538.4, 601.6, act(
        'calendario', 'Artículo 187, inciso 3', 'Desde los 14 años',
        'Homicidio doloso, secuestro, extorsión en todas sus formas y delitos agravados contra la '
        'libertad, integridad y formación sexual.')),
    ('m05_penas', 'mg_lista', 602.6, 616.0, lista(
        'Privación de la libertad',
        ('candado', 'Inciso 1: de 1 a 5 años', 607.3),
        ('candado', 'Inciso 3: de 2 a 8 años', 613.4))),
    ('c09_legalidad', 'carton', 622.4, 647.0, c_tit(
        'Criterio de legalidad',
        'Solo si se dan los requisitos del inciso primero o del inciso tercero del 187 puede haber '
        'privación de la libertad.')),
    ('c10_art189', 'carton', 690.0, 716.0, c_tit(
        'Artículo 189',
        'Una audiencia especial: el informe psicosocial del adolescente, que expresa el defensor de '
        'familia.')),
    ('c11_incumple', 'carton', 719.7, 739.0, cita(
        'Si el infractor no cumple con la medida no privativa de la libertad, podrá imponerse la '
        'sanción privativa de la libertad.')),
    ('c12_bloque', 'carton', 740.7, 762.0, c_tit(
        'Criterio del bloque de constitucionalidad',
        'Reglas y normas de instrumentos internacionales, como las reglas de Beijing.')),
    ('c13_coherencia', 'carton', 771.5, 800.0, c_tit(
        'Criterio de coherencia',
        'Si desde el inicio el infractor no ha sido privado de la libertad, no puede privársele de '
        'la libertad al imponer la sanción.')),
    ('m06_beijing', 'mg_lista', 856.0, 875.0, lista(
        'Reglas de Beijing',
        ('mundo', 'Regla 5: objetivos de la justicia de menores', 860.0),
        ('mazo', 'Regla 6: facultades discrecionales', 865.6),
        ('persona', 'Regla 7: derechos de los menores', 871.8))),
    ('m07_beijing_b', 'mg_lista', 875.2, 906.0, lista(
        'Reglas de Beijing',
        ('libro_ley', 'Regla 17: principios rectores de la sentencia', 875.3),
        ('lista', 'Regla 18: pluralidad de medidas resolutorias', 880.6),
        ('candado', 'Regla 19: último recurso y por el plazo más breve', 894.8))),
    ('c14_cita', 'carton', 925.4, 953.0, c_ante(
        'Corte Suprema de Justicia, SP2159 de 2018',
        '«Si la fiscalía […] no solicitó la medida de internamiento preventivo, se rompería el '
        'principio de coherencia […] si se dispusiera tardíamente la privación de la libertad».')),
    ('c15_flexibilidad', 'carton', 955.0, 986.0, c_tit(
        'Criterio de flexibilidad y discrecionalidad',
        'La sanción privativa de la libertad puede ser modificada en cualquier momento, incluso desde '
        'el momento de su imposición.')),
    ('c16_33510', 'carton', 1012.2, 1025.3, c_tit('Sala de Casación Penal', 'Radicación 33510 de 2010.')),
    ('c17_disney', 'carton', 1028.0, 1055.0, c_tit(
        'El caso Disney',
        'Un caso anonimizado para analizar la procedencia de las medidas restrictivas de derechos o de '
        'la sanción impuesta.')),
    ('lt02', 'lt', 1055.4, 1063.0, S.CARLOS),
]

# --------------------------------------------------------------------------
# Cierre del curso — Estanislao Escalante Barreto (7:25). Pedido del 13 nov 2026.
# Va a la ventana propia de `srpa.TRAMOS['cc']`. Los textos salen de la
# transcripción de Scribe (`D:\DAE\_tmp\srpa\cc\stt_full.json`, WAV a 16 kHz,
# 1.165 palabras, una sola voz). Se quitan las muletillas y las repeticiones, y
# se corrige la concordancia de «se gestionan la delincuencia» → «se gestiona».
# Las listas se midieron antes de rendir (cima ≥ 250): la m01 va sin título,
# la m03 y la m04 con los rótulos recortados a sus palabras y la m06 con el
# hurto en el antetítulo.
ITEMS['cc'] = [
    ('lt01', 'lt', 3.9, 12.8, S.ESTANISLAO),
    ('c01_viejas', 'carton', 25.7, 35.2, cita(
        'Quitando todas esas viejas ideas del menor como un sujeto criminal, como un sujeto '
        'peligroso o en situación irregular.')),
    ('c02_sujeto', 'carton', 35.4, 47.3, cita(
        'Un adolescente como sujeto de derechos, a quien se le debe escuchar y se le debe permitir '
        'participar en la construcción social de su propia realidad.')),
    ('c03_normativos', 'carton', 47.6, 56.2, cita(
        'Elementos normativos, constitucionales, filosóficos que nos permiten comprender la ley de '
        'infancia y adolescencia de otra manera.')),
    ('m01_segundo', 'mg_lista', 56.5, 73.1, lista(
        None,
        ('edificio', 'Las autoridades', 57.7),
        ('personas', 'Los enfoques diferenciales', 58.9),
        ('escudo', 'Cómo prevenir la delincuencia juvenil', 64.6),
        ('libros', 'Los principios pedagógicos, educativos y restaurativos', 68.8))),
    ('c04_no_merece', 'carton', 73.4, 83.2, cita(
        'La infancia y la adolescencia no merece la privación de la libertad por el solo hecho de '
        'la comisión de una conducta.')),
    ('c05_tipica', 'carton', 83.4, 93.0, cita(
        'Esa conducta, al igual que en adultos, debe ser típica, antijurídica y culpable para que '
        'merezca una sanción privativa de la libertad.')),
    ('c06_circulo', 'carton', 94.3, 106.9, cita(
        'Debemos preferir otro tipo de medidas que eviten que los adolescentes entren en ese '
        'círculo vicioso que es la privación de la libertad y la criminalización de la pobreza.')),
    ('m02_estratos', 'mg_act', 113.0, 127.4, act(
        'torta', 'Los jóvenes privados de la libertad', 'Estratos 1 y 2',
        'En muy poca medida, estrato 3. Nunca encontramos jóvenes de estrato 4, 5 o 6.')),
    ('c07_gestiona', 'carton', 128.3, 136.3, cita(
        'No es porque allí no se cometa el delito, sino porque se gestiona el conflicto social de '
        'una manera distinta.')),
    ('c08_vulnerables', 'carton', 136.6, 147.2, cita(
        'Un sistema que está diseñado de cierta manera para criminalizar casi siempre a los más '
        'vulnerables.')),
    ('c09_carceles', 'carton', 147.6, 162.9, cita(
        'Centros de privación de la libertad que funcionan como si fueran cárceles de adultos, pero '
        'donde se priva la libertad a menores de edad.')),
    ('m03_encontrado', 'mg_lista', 163.3, 184.5, lista(
        'Hemos encontrado',
        ('candado', 'Celdas de aislamiento y celdas de castigo', 167.0),
        ('curita', 'Castigo físico y castigos académicos', 172.7),
        ('balanza', 'Tratos crueles, inhumanos e injustos', 178.5))),
    ('c10_valoracion', 'carton', 195.5, 204.9, cita(
        'Debemos hacer una valoración muy seria de lo que es el sistema, cómo funciona el sistema y '
        'para quién funciona el sistema.')),
    ('m04_restaurativa', 'mg_lista', 212.8, 235.4, lista(
        'Una justicia restaurativa que permita',
        ('dialogo', 'Resolver los conflictos sociales', 215.6),
        ('libros', 'Materializar el principio pedagógico', 221.9),
        ('mano_corazon', 'Reparación de daños', 232.1))),
    ('c11_judicializacion', 'carton', 235.7, 242.8, cita(
        'Evitemos a toda costa la judicialización de los adolescentes que terminan involucrados en '
        'un círculo vicioso.')),
    ('c12_reflexion', 'carton', 259.4, 263.7, cita('Que haya dejado elementos para su reflexión.')),
    ('m05_ipanema', 'mg_act', 266.7, 276.2, act(
        'carpeta', 'Aprendamos de los casos', 'Ipanema',
        'Sufrió injustamente una privación de la libertad y la responsabilidad penal por un hecho que '
        'seguramente podía no haber sido punible.')),
    ('m06_comida', 'mg_act', 276.4, 291.0, act(
        'plato', 'Un adolescente que hurtaba comida', None,
        'No tuvo nunca la ayuda del Estado, la sociedad y la familia: la culpabilidad allí debería '
        'verse disminuida.')),
    ('c13_reproche', 'carton', 291.2, 304.0, cita(
        '¿Cómo exigirle un comportamiento conforme a la norma o hacerle un juicio de reproche cuando '
        'la familia, el Estado y la sociedad no le han dado nada?')),
    ('c14_iniciativa', 'carton', 325.7, 336.4, cita(
        'Que haya despertado en ustedes una iniciativa por comprender mejor los derechos y la '
        'situación de la infancia y la adolescencia en este país.')),
    ('m07_por_fuera', 'mg_lista', 341.0, 352.9, lista(
        'Resolver su conflicto',
        ('puerta_salida', 'Por fuera de la cárcel', 345.2),
        ('candado', 'Por fuera de la privación de la libertad', 346.4),
        ('libro_ley', 'Por fuera de las medidas restrictivas de derechos', 349.1))),
    ('c15_verdaderas', 'carton', 359.5, 367.7, cita(
        'Si visitamos los centros de internamiento, veremos que algunos son verdaderas cárceles para '
        'infancia y adolescencia.')),
    ('m08_llamado', 'mg_lista', 367.9, 386.4, lista(
        'Mi llamado de atención',
        ('ojo', 'Evitemos los eufemismos', 370.8),
        ('libro_ley', 'Que la ley de infancia y adolescencia se materialice', 373.1),
        ('bifurcacion', 'Hay alternativas para la solución del conflicto social', 381.5))),
    ('m09_invitamos', 'mg_lista', 387.6, 405.0, lista(
        'Los invitamos',
        ('doc_check', 'A hacer la evaluación del curso', 388.7),
        ('lista', 'A responder la encuesta', 393.2),
        ('birrete', 'A obtener su respectiva certificación', 401.8))),
    ('c16_privilegio', 'carton', 412.5, 421.3, cita(
        'Es un verdadero privilegio haber podido hacer parte de este proceso de formación y haber '
        'podido contarles nuestro pensamiento.')),
    ('lt02', 'lt', 426.5, 436.6, S.ESTANISLAO),
]
