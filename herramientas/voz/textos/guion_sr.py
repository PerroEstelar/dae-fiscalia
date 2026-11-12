# -*- coding: utf-8 -*-
r"""Casos del curso «Sistema de responsabilidad penal para adolescentes y
justicia restaurativa» (PRIORIDAD 1) · narrados, con placas.

Los videos de profes a cámara de este mismo curso (11 nov) están en
`cursos/srpa-justicia-restaurativa` y tienen su propia receta (`srpa.py`).
Esto es lo otro: los CASOS, con la receta de los cursos de casos (Estándares
interamericanos, Delitos ambientales): voz de ElevenLabs, placas de Magnific,
Kling, cartones verbatim, rótulos, After Effects, música con ducking.

NICO (12 nov 2026)
    Fuente: Drive de la agencia, carpeta «PRIORIDAD 1 - SISTEMA DE
    RESPONSABILIDAD PENAL PARA ADOLESCENTES», documento «Caso Nico»
    (1TWtuxipDr0u5irRp8Dz_FfOaAV6tTkj_08bR1p-4bFg). Encabezado: «Prioridad 1
    SRPA · Importancia del principio de culpabilidad en la justicia penal para
    adolescentes». Sin preguntas ni consigna: es solo el caso.
    Unidad: la U1 del diseño del curso («Principios y sentido de un sistema
    de responsabilidad penal para adolescentes», lección 3, «Principios
    orientadores»; actividad «conocimiento de casos y problemas prácticos»).

LA REGLA DE SIEMPRE
    `texto`  el documento VERBATIM, para el cartón. Comillas «». Los números
             en dígitos (regla de Sebastián: 15 años, $18.000, 9:15 a. m.).
    `tts`    lo mismo dicho para ElevenLabs: números en letras, siglas
             desplegadas. Solo cuando hace falta.
    El documento se narra entero y en su orden; no se agrega ni se quita
    nada (comprobado palabra por palabra contra el documento: 1.127 de
    1.127). La lista de la valoración inicial (cinco viñetas) se dice como
    frases seguidas.

LAS VOCES (ElevenLabs, cuenta de Sebastián)
    Narra Pilar. La cita que el documento pone en boca del defensor público
    -«Mire, usted no tiene dónde vivir…»- es lo que el caso discute y la dice
    él: Julian (la voz del funcionario de Enfoque diferencial C5; lleva el
    paso alto contra los golpes de aire). Como en ED, no se inventa ningún
    parlamento. La frase del comerciante («esperarlo entre todos…») la dice
    la narradora, citada, a distancia: es la de un agresor.

ERRATA QUE NO SE TOCA
    «El domingo 12 de abril de 2022»: el 12 de abril de 2022 fue martes. No
    es una errata obvia (no se sabe cuál de los dos datos es el bueno) y la
    regla es el verbatim: va como está y se le avisa a Sebastián.
"""

PREFIJO = 'SR_'

NORMAL = 0.7
PARRAFO = 1.1
COMA = 0.35
CITA = 0.45

DRIVE = 'https://drive.google.com/drive/folders/1luN8d98E24b0fRY9c-pUSpPdIj1_ZWlL'
DOC_FUENTE = '1TWtuxipDr0u5irRp8Dz_FfOaAV6tTkj_08bR1p-4bFg'
# Entregas: el mismo sitio de los videos de profes del curso (11 nov):
# curso -> VIDEOS FINALIZADOS -> unidad 1
DRIVE_VIDEOS = '1mKRysBB50QhE1xAb4cDjaIXQKxXV8Gy7'

CURSO = 'Sistema de responsabilidad penal para adolescentes y justicia restaurativa'
ANTE = 'Sistema de responsabilidad penal para adolescentes'

UNIDADES = {1: 'UNIDAD 1'}

# clave -> (tipo, unidad, carpeta, voz, antetitulo, titulo)
PIEZAS = {
 'NICO': ('video', 1, 'CASO NICO - Principio de culpabilidad', 'Pilar',
          'Caso Nico',
          'Importancia del principio de culpabilidad en la justicia penal para '
          'adolescentes'),
}
VIDEOS = [k for k, v in PIEZAS.items() if v[0] == 'video']
IMAGENES = []

TEMAS = {k: (UNIDADES[v[1]] + '\\' + v[2], v[3], v[4], v[5])
         for k, v in PIEZAS.items()}

ENTREGA = {
 'NICO': 'PRIO 1 - SRPA - U1 - CASO NICO PRINCIPIO DE CULPABILIDAD',
}

# (id, voz, texto verbatim -el del cartón-, texto tts o None, pausa antes)
BLOQUES = {}

BLOQUES['NICO'] = [
 # --- quién es Nico
 ('n01_nico', 'Pilar',
  'En el municipio de San Miguel de los Andes, ubicado en el departamento de '
  'Cundinamarca, vivía un adolescente de aproximadamente 15 años, conocido por '
  'los habitantes del sector como «Nico».',
  'En el municipio de San Miguel de los Andes, ubicado en el departamento de '
  'Cundinamarca, vivía un adolescente de aproximadamente quince años, conocido '
  'por los habitantes del sector como Nico.',
  0.0),
 ('n02_documentos', 'Pilar',
  'Nico no tenía documentos de identidad conocidos, no había sido reconocido '
  'legalmente por sus progenitores y tampoco se tenía información sobre '
  'familiares que ejercieran su cuidado o representación.',
  None, NORMAL),
 ('n03_escuela', 'Pilar',
  'No figuraba matriculado en ninguna institución educativa y no existían '
  'registros conocidos de afiliación al sistema de salud.',
  None, NORMAL),
 ('n04_puente', 'Pilar',
  'Desde hacía varios meses habitaba debajo de un puente peatonal ubicado a '
  'pocas cuadras de la plaza de mercado municipal. Allí dormía sobre cartones, '
  'cobijas deterioradas y algunas prendas que había conseguido de los '
  'comerciantes del sector.',
  None, PARRAFO),
 ('n05_alimentacion', 'Pilar',
  'Su alimentación dependía de lo que encontraba en las inmediaciones de la '
  'plaza, de las sobras que algunos vendedores le entregaban ocasionalmente y '
  'de pequeños alimentos que conseguía sin autorización de sus propietarios.',
  None, NORMAL),
 # --- la plaza
 ('n06_comerciantes', 'Pilar',
  'Los comerciantes conocían su situación. Algunos habían intentado ayudarlo '
  'entregándole comida, mientras que otros manifestaban inconformidad por su '
  'presencia constante en los establecimientos.',
  None, PARRAFO),
 ('n07_recurrente', 'Pilar',
  'Con el paso de las semanas, varios comerciantes comenzaron a identificar un '
  'comportamiento recurrente: cuando los clientes recibían sus desayunos, '
  'especialmente tamales, caldo de costilla, arepas y bebidas calientes, Nico '
  'se acercaba a las mesas, tomaba los alimentos y salía corriendo sin pagar.',
  None, PARRAFO),
 ('n08_discusiones', 'Pilar',
  'Esta situación generó numerosas discusiones entre los propietarios de los '
  'establecimientos. Algunos afirmaban que el adolescente estaba afectando sus '
  'ventas y que los clientes comenzaban a evitar determinados locales por '
  'temor a que les quitaran sus alimentos.',
  None, PARRAFO),
 ('n09_reunion', 'Pilar',
  'En una reunión informal, varios comerciantes propusieron organizarse para '
  'impedir que Nico continuara realizando estas conductas. Uno de ellos sugirió '
  'que debían «esperarlo entre todos, atraparlo y entregarlo a la Policía para '
  'que aprendiera a respetar lo ajeno».',
  None, NORMAL),
 # --- el domingo
 ('n10_domingo', 'Pilar',
  'El domingo 12 de abril de 2022, aproximadamente a las 9:15 a. m., la plaza '
  'de mercado se encontraba especialmente concurrida.',
  'El domingo doce de abril de dos mil veintidós, aproximadamente a las nueve '
  'y quince de la mañana, la plaza de mercado se encontraba especialmente '
  'concurrida.',
  PARRAFO),
 ('n11_desayuno', 'Pilar',
  'Un hombre que había acudido al lugar con su familia recibió un desayuno '
  'compuesto por un tamal, una porción de caldo de costilla y una bebida '
  'caliente, cuyo valor comercial ascendía a $18.000.',
  'Un hombre que había acudido al lugar con su familia recibió un desayuno '
  'compuesto por un tamal, una porción de caldo de costilla y una bebida '
  'caliente, cuyo valor comercial ascendía a dieciocho mil pesos.',
  NORMAL),
 ('n12_huida', 'Pilar',
  'Mientras el cliente conversaba con sus acompañantes, Nico se acercó a la '
  'mesa, tomó el tamal y el recipiente con el caldo y emprendió la huida.',
  None, NORMAL),
 ('n13_persecucion', 'Pilar',
  'El propietario de los alimentos gritó solicitando ayuda. Varios comerciantes '
  'que se encontraban cerca comenzaron a perseguir al adolescente y lograron '
  'interceptarlo, aproximadamente a 30 metros del establecimiento.',
  'El propietario de los alimentos gritó solicitando ayuda. Varios comerciantes '
  'que se encontraban cerca comenzaron a perseguir al adolescente y lograron '
  'interceptarlo, aproximadamente a treinta metros del establecimiento.',
  NORMAL),
 ('n14_agresion', 'Pilar',
  'Una vez reducido, tres comerciantes lo sujetaron de los brazos, mientras '
  'otros comenzaron a golpearlo. Uno de ellos le propinó varios golpes en el '
  'rostro y otro lo pateó en las piernas cuando ya se encontraba en el suelo.',
  None, PARRAFO),
 ('n15_gritos', 'Pilar',
  'Durante la agresión, algunas personas le gritaban que estaban cansadas de '
  'sus robos y que esa era la única manera de conseguir que dejara de hacerlo.',
  None, NORMAL),
 ('n16_video', 'Pilar',
  'Un comerciante grabó parcialmente lo ocurrido con su teléfono celular. En el '
  'video se observa al adolescente en el suelo, rodeado por varias personas, '
  'mientras intenta cubrirse el rostro.',
  None, PARRAFO),
 # --- la Policía
 ('n17_patrulla', 'Pilar',
  'Aproximadamente 10 minutos después llegó una patrulla de la Policía Nacional.',
  'Aproximadamente diez minutos después llegó una patrulla de la Policía '
  'Nacional.',
  NORMAL),
 ('n18_entrega', 'Pilar',
  'Los comerciantes entregaron al adolescente a los uniformados y explicaron '
  'que lo habían retenido porque acababa de hurtar alimentos de uno de los '
  'establecimientos.',
  None, PARRAFO),
 ('n19_policias', 'Pilar',
  'Los policías recogieron los alimentos recuperados y escucharon brevemente la '
  'versión de algunos comerciantes.',
  None, PARRAFO),
 ('n20_omisiones', 'Pilar',
  'Sin embargo, no identificaron plenamente a todas las personas que '
  'participaron en la agresión, no solicitaron el video grabado por uno de los '
  'presentes y tampoco dejaron constancia inicial de las lesiones que '
  'presentaba el adolescente.',
  None, NORMAL),
 ('n21_quince', 'Pilar',
  'Nico manifestó que tenía 15 años, que vivía debajo del puente y que no tenía '
  'a nadie que pudiera responder por él.',
  'Nico manifestó que tenía quince años, que vivía debajo del puente y que no '
  'tenía a nadie que pudiera responder por él.',
  PARRAFO),
 ('n22_cip', 'Pilar',
  'Los uniformados lo trasladaron a un Centro de Internamiento Preventivo (CIP) '
  'y posteriormente iniciaron las actuaciones correspondientes para ponerlo a '
  'disposición de las autoridades del Sistema de Responsabilidad Penal para '
  'Adolescentes.',
  'Los uniformados lo trasladaron a un Centro de Internamiento Preventivo, y '
  'posteriormente iniciaron las actuaciones correspondientes para ponerlo a '
  'disposición de las autoridades del Sistema de Responsabilidad Penal para '
  'Adolescentes.',
  NORMAL),
 # --- el defensor
 ('n23_defensor', 'Pilar',
  'Una vez iniciadas las actuaciones judiciales, se le asignó un defensor '
  'público para que ejerciera su representación técnica.',
  None, PARRAFO),
 ('n24_hambre', 'Pilar',
  'Durante una conversación privada, Nico manifestó que efectivamente había '
  'tomado los alimentos, pero explicó que llevaba varios días sin comer y que '
  'no tenía dinero para comprarlos.',
  None, PARRAFO),
 ('n25_otras', 'Pilar',
  'También contó que no era la primera vez que lo hacía y que, en otras '
  'oportunidades, había tomado alimentos de diferentes establecimientos porque '
  'tenía hambre.',
  None, NORMAL),
 ('n26_cae', 'Pilar',
  'El defensor público le explicó que, si aceptaba los cargos, probablemente '
  'sería enviado a un Centro de Atención Especializada (CAE), donde tendría '
  'acceso a alimentación, alojamiento, atención médica y protección.',
  'El defensor público le explicó que, si aceptaba los cargos, probablemente '
  'sería enviado a un Centro de Atención Especializada, donde tendría acceso a '
  'alimentación, alojamiento, atención médica y protección.',
  PARRAFO),
 ('n27_relato', 'Pilar',
  'Según la conversación que posteriormente relató el adolescente, el abogado '
  'le manifestó:',
  None, PARRAFO),
 ('n28_mire', 'Julian',
  '«Mire, usted no tiene dónde vivir, no tiene familia y está pasando muchas '
  'necesidades. Si acepta lo que hizo y no se pone a discutir el proceso, puede '
  'quedarse en un lugar donde le van a dar comida, techo y atención.»',
  'Mire, usted no tiene dónde vivir, no tiene familia y está pasando muchas '
  'necesidades. Si acepta lo que hizo y no se pone a discutir el proceso, puede '
  'quedarse en un lugar donde le van a dar comida, techo y atención.',
  CITA),
 ('n29_afuera', 'Julian',
  '«Afuera no tiene nada. Piénselo bien, porque tal vez esto sea lo mejor que le '
  'pueda pasar.»',
  'Afuera no tiene nada. Piénselo bien, porque tal vez esto sea lo mejor que le '
  'pueda pasar.',
  NORMAL),
 ('n30_pregunta', 'Pilar',
  'Nico preguntó si, en caso de aceptar los cargos, tendría que regresar a vivir '
  'debajo del puente.',
  None, PARRAFO),
 ('n31_respuesta', 'Pilar',
  'El defensor le respondió que eso dependería de las decisiones que adoptaran '
  'las autoridades, pero insistió en que el centro especializado podía '
  'ofrecerle mejores condiciones que las que tenía actualmente.',
  None, NORMAL),
 ('n32_dispuesto', 'Pilar',
  'El adolescente manifestó entonces que estaba dispuesto a aceptar todo lo que '
  'le imputaran, siempre que no tuviera que volver a dormir en la calle.',
  None, PARRAFO),
 # --- la preparación de la audiencia
 ('n33_preparacion', 'Pilar',
  'Durante la preparación de la audiencia, el defensor no profundizó en las '
  'circunstancias de las anteriores sustracciones, no verificó si existían '
  'denuncias formalmente presentadas por los demás comerciantes, no solicitó la '
  'valoración médico-legal de las lesiones ocasionadas durante la retención y '
  'tampoco exploró las condiciones personales, familiares y sociales del '
  'adolescente.',
  'Durante la preparación de la audiencia, el defensor no profundizó en las '
  'circunstancias de las anteriores sustracciones, no verificó si existían '
  'denuncias formalmente presentadas por los demás comerciantes, no solicitó la '
  'valoración médico legal de las lesiones ocasionadas durante la retención y '
  'tampoco exploró las condiciones personales, familiares y sociales del '
  'adolescente.',
  PARRAFO),
 ('n34_consecuencias', 'Pilar',
  'Tampoco explicó de manera suficiente las consecuencias jurídicas de una '
  'aceptación de responsabilidad ni verificó si la decisión obedecía a una '
  'comprensión libre, consciente e informada de sus derechos.',
  None, NORMAL),
 # --- el CAE
 ('n35_ingreso', 'Pilar',
  'Una vez adelantadas las actuaciones judiciales correspondientes, Nico '
  'ingresó a un Centro de Atención Especializada (CAE).',
  'Una vez adelantadas las actuaciones judiciales correspondientes, Nico '
  'ingresó a un Centro de Atención Especializada.',
  PARRAFO),
 ('n36_higiene', 'Pilar',
  'Durante el procedimiento de recepción, el personal del establecimiento '
  'advirtió que el adolescente presentaba condiciones de higiene personal '
  'considerablemente deterioradas.',
  None, PARRAFO),
 ('n37_valoracion', 'Pilar',
  'En la valoración inicial se observaron: uñas de los pies engrosadas, '
  'decoloradas y deterioradas, con sospecha de infección micótica compatible '
  'con onicomicosis.',
  None, NORMAL),
 ('n38_olor', 'Pilar',
  'Olor intenso proveniente de sus pies y calzado. Presencia de pediculosis en '
  'el cuero cabelludo.',
  None, NORMAL),
 ('n39_lesiones', 'Pilar',
  'Lesiones visibles en el rostro y las extremidades inferiores, aparentemente '
  'relacionadas con los golpes recibidos durante su retención.',
  None, NORMAL),
 ('n40_peso', 'Pilar',
  'Bajo peso y signos físicos que motivaron la necesidad de una valoración '
  'nutricional.',
  None, NORMAL),
 ('n41_convivencia', 'Pilar',
  'Algunos funcionarios consideraron que las condiciones de higiene del '
  'adolescente podían representar un problema para la convivencia con los '
  'demás jóvenes que permanecían en el establecimiento.',
  None, PARRAFO),
 ('n42_cabello', 'Pilar',
  'En consecuencia, sin que mediara una valoración médica especializada que '
  'determinara la necesidad de alguna medida sanitaria particular, se ordenó '
  'cortarle completamente el cabello para eliminar los piojos.',
  None, NORMAL),
 ('n43_aislamiento', 'Pilar',
  'Adicionalmente, debido al olor proveniente de sus pies, se decidió ubicarlo '
  'en un espacio de aislamiento individual.',
  None, PARRAFO),
]


def bloques(clave):
    """Devuelve [(id, voz, texto_verbatim, texto_tts, pausa_antes)]."""
    return [(i, v, t, (s if s is not None else t), p)
            for i, v, t, s, p in BLOQUES[clave]]


def palabras(clave):
    return sum(len(t.split()) for _, v, t, _, _ in BLOQUES[clave])


def contexto(clave):
    return ' '.join(t for _, _, t, _, _ in BLOQUES[clave])


if __name__ == '__main__':
    for k in BLOQUES:
        n = palabras(k)
        seg = n / 150.0 * 60 * 1.10
        print('%-4s %4d palabras %2d bloques ~%5.1f s de voz  %s'
              % (k, n, len(BLOQUES[k]), seg, TEMAS[k][0]))
