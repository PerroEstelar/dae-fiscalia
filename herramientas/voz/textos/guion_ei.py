# -*- coding: utf-8 -*-
r"""Curso «Estándares interamericanos · graves violaciones a los derechos
humanos» (PRIORIDAD 3) · 5 videos y 6 láminas.

LA FUENTE (Drive de la agencia)
    Carpeta «PRIORIDAD 3 - Estandares Interamericanos Graves violaciones VF»
    https://drive.google.com/drive/folders/1c7fmrN1YeM2uYtn1-6ThuNgRX5fOZLBa
    «Estándares Interamericanos - Actividades de aprendizaje»
        1er8p3nu7Ut2d97i0XsJV92v8mR516YiHlVV9o5yJOnE
    Un solo documento, sin unidades: actividades de aprendizaje con su
    situación, y después las preguntas H5P. Al final, tres actividades sin
    número se repiten tal cual (copia del documento): cuentan una vez.

EL ENCARGO (Sebastián, 5 nov 2026)
    Las situaciones con comentario «Video» o «Imagen» se hacen así. Las que
    no tenían comentario: «dependiendo de la longitud del caso, si vale la
    pena para video hacerlo como video, si no, ilustración». Medido en
    palabras de la situación, sin consigna:
        marcadas video   S01 121 · S04 86
        marcadas imagen  S02 38 · S03 30 · S05 51 · S10 61 (+139 de la
                         lectura) · S11 72
        sin marcar       S06 108 · S07 87 · S08 78  -> VIDEO (relato con
                         hechos que se suceden, a la altura de S04)
                         S09 63                     -> LÁMINA (en la franja
                         de las imágenes marcadas)
    Las preguntas, opciones, respuestas y retroalimentación NO entran (van en
    otra parte de la virtualización). La CONSIGNA tampoco («Su tarea consiste
    en…», «Usted deberá examinar…», «Consigna: Usted debe establecer…»,
    «Recuerde que…»): es para el participante, como en «16 situaciones».
    Magnific con la cuenta nueva (jpcolombia3, Pro, 300.000 créditos); techo
    de ~800 créditos por video «de ser necesario», más clips con movimiento.

LAS CLAVES, EN EL ORDEN DEL DOCUMENTO
    S01  video   AA1 ¿Quién responde por una violación de derechos humanos?
    S02  lámina  AA2 ¿Cómo se organiza la protección internacional…?
    S03  lámina  AA3 ¿Qué fuente internacional necesito consultar?
    S04  video   AA4 ¿Cómo utilizaría una fuente internacional…?
    S05  lámina  AA4 ¿Cómo utilizaría la jurisprudencia interamericana…?
    S06  video   Actividad inicial · la muerte de dos jóvenes
    S07  video   Actividad · la fosa clandestina
    S08  video   Actividad · bajo custodia policial
    S09  lámina  AA1 ¿Es suficiente abrir una investigación penal?
    S10  lámina  AA2 ¿Qué examina la Corte Interamericana…? (La Rochela)
    S11  lámina  AA3 ¿Qué decide y qué ordena la Corte Interamericana?
    El documento numera dos veces «Actividad 4» y empieza de nuevo en 1:
    por eso las claves son de situación, no de actividad.

LOS TÍTULOS
    S01-S05, S09-S11: el título de la actividad, como lo escribe el documento
    (con la mayúscula inicial que le falta). S06-S08 no tienen título en el
    documento: se usan palabras de su propia situación («la muerte de dos
    jóvenes», «una fosa clandestina», «bajo custodia policial»).

DOS TEXTOS POR BLOQUE, COMO EN TODA LA SERIE
    `texto`  el documento VERBATIM, para el cartón. Comillas «».
    `tts`    lo mismo dicho para ElevenLabs. Solo cuando hace falta.

ERRATAS / FORMA (la regla de la casa: «corregir lo obvio»)
    S10  «178\\. La Corte…», «179\\. Por todas…» (escape del documento) ->
         «178. La Corte…», «179. Por todas…».
    S11  el enlace «rodriguezvera.pdf» del documento no va en la lámina (en
         una imagen no se puede abrir); queda anotado aquí.

LAS VOCES (ElevenLabs, cuenta de Sebastián): narran Carlos y Pilar, se turnan
    S01 Carlos · S04 Pilar · S06 Carlos · S07 Pilar · S08 Carlos.
    Nadie más habla: la pregunta del familiar (S01) va en estilo indirecto,
    como en el documento. No se inventan parlamentos.
"""

PREFIJO = 'EI_'

CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.7
PARRAFO = 1.1
COMA = 0.35

DRIVE = 'https://drive.google.com/drive/folders/1c7fmrN1YeM2uYtn1-6ThuNgRX5fOZLBa'
DOC_FUENTE = '1er8p3nu7Ut2d97i0XsJV92v8mR516YiHlVV9o5yJOnE'
DRIVE_IMAGENES = '1UEghYotTn4q86O8TotyDspDDBLolXsZC'     # creadas el 5 nov
DRIVE_VIDEOS = '1j6v4nenqFDAL2RNu3x15nZzWxObP7q7Y'

CURSO = 'Estándares interamericanos · graves violaciones a los derechos humanos'
ANTE = 'Estándares interamericanos'

UNIDADES = {0: 'VIDEOS', 1: 'IMAGENES'}

# clave -> (tipo, unidad, carpeta de la pieza, voz, antetitulo / rotulo, titulo)
#   video:  antetitulo del carton de entrada y titulo
#   lamina: rotulo del panel (el subtitulo del documento) y titulo (para la
#           ficha; en la lamina no va)
PIEZAS = {
 'S01': ('video', 0, 'SITUACION 01 - Quien responde por una violacion de derechos humanos',
         'Carlos', 'Actividad de aprendizaje 1',
         '¿Quién responde por una violación de derechos humanos?'),
 'S02': ('imagen', 1, 'SITUACION 02 - Como se organiza la proteccion internacional',
         None, 'Situación de aprendizaje',
         '¿Cómo se organiza la protección internacional de los derechos humanos?'),
 'S03': ('imagen', 1, 'SITUACION 03 - Que fuente internacional necesito consultar',
         None, 'Situación de aprendizaje',
         '¿Qué fuente internacional necesito consultar?'),
 'S04': ('video', 0, 'SITUACION 04 - Como utilizaria una fuente internacional',
         'Pilar', 'Actividad de aprendizaje 4',
         '¿Cómo utilizaría una fuente internacional en una investigación penal?'),
 'S05': ('imagen', 1, 'SITUACION 05 - Como utilizaria la jurisprudencia interamericana',
         None, 'Situación inicial',
         '¿Cómo utilizaría la jurisprudencia interamericana en una investigación penal?'),
 'S06': ('video', 0, 'SITUACION 06 - La muerte de dos jovenes',
         'Carlos', 'Actividad de aprendizaje inicial',
         'La muerte de dos jóvenes'),
 'S07': ('video', 0, 'SITUACION 07 - La fosa clandestina',
         'Pilar', 'Actividad de aprendizaje', 'La fosa clandestina'),
 'S08': ('video', 0, 'SITUACION 08 - Bajo custodia policial',
         'Carlos', 'Actividad de aprendizaje', 'Bajo custodia policial'),
 'S09': ('imagen', 1, 'SITUACION 09 - Es suficiente abrir una investigacion penal',
         None, 'Situación',
         '¿Es suficiente abrir una investigación penal?'),
 'S10': ('imagen', 1, 'SITUACION 10 - Que examina la Corte Interamericana',
         None, 'Situación de aprendizaje',
         '¿Qué examina la Corte Interamericana de una investigación penal?'),
 'S11': ('imagen', 1, 'SITUACION 11 - Que decide y que ordena la Corte Interamericana',
         None, 'Situación de aprendizaje',
         '¿Qué decide y qué ordena la Corte Interamericana?'),
}
VIDEOS = [k for k, v in PIEZAS.items() if v[0] == 'video']
IMAGENES = [k for k, v in PIEZAS.items() if v[0] == 'imagen']

# compatibilidad con las herramientas de la serie (dh_pieza & co.):
# TEMAS[clave] = (carpeta relativa a la raiz del curso, voz, antetitulo, titulo)
TEMAS = {k: (UNIDADES[v[1]] + '\\' + v[2], v[3], v[4], v[5])
         for k, v in PIEZAS.items() if v[0] == 'video'}

ENTREGA = {
 'S01': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 01 QUIEN RESPONDE POR UNA VIOLACION DE DERECHOS HUMANOS',
 'S02': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 02 COMO SE ORGANIZA LA PROTECCION INTERNACIONAL',
 'S03': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 03 QUE FUENTE INTERNACIONAL NECESITO CONSULTAR',
 'S04': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 04 COMO UTILIZARIA UNA FUENTE INTERNACIONAL',
 'S05': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 05 COMO UTILIZARIA LA JURISPRUDENCIA INTERAMERICANA',
 'S06': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 06 LA MUERTE DE DOS JOVENES',
 'S07': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 07 LA FOSA CLANDESTINA',
 'S08': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 08 BAJO CUSTODIA POLICIAL',
 'S09': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 09 ES SUFICIENTE ABRIR UNA INVESTIGACION PENAL',
 'S10': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 10 QUE EXAMINA LA CORTE INTERAMERICANA',
 'S11': 'PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 11 QUE DECIDE Y QUE ORDENA LA CORTE INTERAMERICANA',
}

# --------------------------------------------------------------- láminas
# El texto del panel, VERBATIM, en párrafos. Cada párrafo es (estilo, texto):
#   'p'    cuerpo
#   'ref'  la referencia de la lectura (cuerpo, en cursiva)
#   'cita' el fragmento de la sentencia (cuerpo menor, sangrado, con filete)
#   'det'  una determinación: lo que va antes del primer punto, en negrita
TEXTOS = {
 'S02': [
  ('p', 'Un servidor de la Fiscalía debe preparar una presentación '
        'introductoria sobre los mecanismos internacionales de protección de '
        'los derechos humanos.'),
  ('p', 'Para ello, elaboró las siguientes afirmaciones.'),
  ('p', 'Antes de utilizarlas, solicita que sean revisadas para identificar '
        'posibles errores conceptuales.'),
 ],
 'S03': [
  ('p', 'Usted trabaja en una dependencia de la Fiscalía que adelanta '
        'investigaciones por graves violaciones a los derechos humanos.'),
  ('p', 'Durante una reunión de trabajo se presentan diferentes necesidades '
        'de consulta jurídica.'),
 ],
 'S05': [
  ('p', 'La Fiscalía adelanta una investigación relacionada con la presunta '
        'desaparición forzada de una persona.'),
  ('p', 'Durante el análisis jurídico del caso, el equipo investigador '
        'identifica decisiones de la Corte Interamericana relacionadas con la '
        'obligación estatal de investigar.'),
  ('p', 'Entre ellas se encuentran Velásquez Rodríguez vs. Honduras y '
        'Rodríguez Vera y otros vs. Colombia.'),
 ],
 'S09': [
  ('p', 'Una persona desaparece después de haber sido detenida por '
        'integrantes de un organismo estatal.'),
  ('p', 'Sus familiares denuncian los hechos ante las autoridades, pero las '
        'investigaciones iniciales no permiten establecer su paradero.'),
  ('p', 'Durante varios años se adelantan actuaciones judiciales sin que se '
        'esclarezcan las circunstancias de la desaparición.'),
  ('p', 'El Estado sostiene que cumplió su obligación porque permitió '
        'presentar denuncias y abrió una investigación penal.'),
 ],
 'S10': [
  ('p', 'En el caso de la Masacre de La Rochela, el Estado colombiano adelantó '
        'investigaciones penales durante varios años.'),
  ('p', 'La Corte Interamericana reconoció la complejidad de esos '
        'procedimientos, pero concluyó que las actuaciones realizadas no '
        'habían sido suficientes para garantizar un acceso efectivo a la '
        'justicia.'),
  ('ref', 'Lectura: Corte IDH, Caso de la Masacre de La Rochela vs. Colombia, '
          'párrafos 178 y 179.'),
  ('cita', '178. La Corte reconoce la complejidad de los asuntos que se '
           'investigan por los órganos judiciales internos en relación con '
           'esta masacre. Sin embargo, el Tribunal observa que debido a la '
           'naturaleza y gravedad de los acontecimientos, así como el número '
           'de partícipes involucrados en ellos (grupos paramilitares que '
           'actuaban con el apoyo de la fuerza pública), los medios '
           'utilizados y los resultados alcanzados no han sido suficientes '
           'para garantizar un efectivo acceso a la justicia.'),
  ('cita', '179. Por todas las anteriores consideraciones, el Tribunal '
           'concluye que los procesos penales en relación con los hechos de '
           'la masacre de La Rochela no han sido desarrollados en un plazo '
           'razonable, ni han constituido un recurso efectivo para asegurar '
           'los derechos de acceso a la justicia, la determinación de la '
           'verdad y la reparación de las presuntas víctimas y sus '
           'familiares.'),
 ],
 'S11': [
  ('p', 'Usted recibe una síntesis de la sentencia del caso Rodríguez Vera y '
        'otros vs. Colombia.'),
  ('p', 'La información comprende tres determinaciones:'),
  ('det', 'Determinación A. La Corte declaró la responsabilidad internacional '
          'de Colombia por violaciones de las garantías judiciales y la '
          'protección judicial.'),
  ('det', 'Determinación B. La Corte ordenó adelantar investigaciones para '
          'esclarecer los hechos y determinar las responsabilidades '
          'correspondientes.'),
  ('det', 'Determinación C. La Corte dispuso supervisar el cumplimiento de las '
          'medidas establecidas en la sentencia.'),
 ],
}

# --------------------------------------------------------------- videos
# (id, voz, texto_verbatim, texto_tts_o_None, pausa_antes)
BLOQUES = {}

BLOQUES['S01'] = [
 ('a01_el_lider', 'Carlos',
  'En una región de Colombia se denuncia la desaparición de un líder '
  'comunitario que había recibido amenazas por parte de integrantes de una '
  'estructura criminal.',
  None, 0.0),
 ('a02_las_amenazas', 'Carlos',
  'Sus familiares informan que, antes de la desaparición, habían puesto en '
  'conocimiento de distintas autoridades las amenazas recibidas.',
  None, PARRAFO),
 ('a03_la_investigacion', 'Carlos',
  'La Fiscalía inicia una investigación penal para establecer las '
  'circunstancias de los hechos y determinar las responsabilidades '
  'correspondientes.',
  None, PARRAFO),
 ('a04_varios_anos', 'Carlos',
  'Transcurridos varios años, la familia considera que sus derechos no han '
  'sido garantizados adecuadamente y decide acudir a una organización de '
  'derechos humanos.',
  None, PARRAFO),
 ('a05_la_pregunta', 'Carlos',
  'Durante una reunión, uno de los familiares pregunta si es posible '
  'presentar el caso ante una autoridad internacional.',
  None, PARRAFO),
 ('a06_condenar', 'Carlos',
  'Otro integrante de la familia sostiene que un tribunal internacional '
  'debería condenar penalmente a los responsables de la desaparición.',
  None, NORMAL),
]

BLOQUES['S04'] = [
 ('d01_la_investigacion', 'Pilar',
  'La Fiscalía General de la Nación adelanta una investigación por la '
  'presunta desaparición forzada de una persona.',
  None, 0.0),
 ('d02_la_revision', 'Pilar',
  'Durante la revisión jurídica del caso, un servidor identifica que el '
  'ordenamiento colombiano cuenta con disposiciones constitucionales y '
  'penales relacionadas con la conducta investigada.',
  None, PARRAFO),
 ('d03_la_convencion', 'Pilar',
  'También encuentra referencias a la Convención Americana sobre Derechos '
  'Humanos,',
  None, NORMAL),
 ('d04_las_decisiones', 'Pilar',
  'a la Convención Interamericana sobre Desaparición Forzada de Personas y a '
  'diferentes decisiones de la Corte Interamericana.',
  None, COMA),
 ('d05_determinar', 'Pilar',
  'El servidor debe determinar qué fuentes internacionales pueden resultar '
  'relevantes y cómo incorporarlas adecuadamente a su análisis jurídico.',
  None, PARRAFO),
]

BLOQUES['S06'] = [
 ('f01_la_informacion', 'Carlos',
  'La Fiscalía recibe información sobre la muerte de dos jóvenes durante una '
  'operación militar realizada en una zona rural.',
  None, 0.0),
 ('f02_el_informe', 'Carlos',
  'Según el informe de la unidad que participó en el operativo, los jóvenes '
  'pertenecían a una organización armada y murieron durante un '
  'enfrentamiento.',
  None, PARRAFO),
 ('f03_la_entrevista', 'Carlos',
  'Sin embargo, sus familiares manifiestan que ambos habían salido de sus '
  'viviendas para asistir a una entrevista de trabajo.',
  None, PARRAFO),
 ('f04_el_testigo', 'Carlos',
  'Un testigo afirma haberlos visto ingresar a un vehículo militar el día '
  'anterior a sus muertes.',
  None, NORMAL),
 ('f05_las_lesiones', 'Carlos',
  'La documentación médico-legal identifica lesiones cuya localización y '
  'características podrían resultar incompatibles con algunos aspectos de '
  'la versión operacional.',
  'La documentación médico legal identifica lesiones cuya localización y '
  'características podrían resultar incompatibles con algunos aspectos de '
  'la versión operacional.',
  PARRAFO),
 ('f06_el_fiscal', 'Carlos',
  'El fiscal del caso debe determinar las actuaciones que orientarán la '
  'investigación.',
  None, PARRAFO),
]

BLOQUES['S07'] = [
 ('g01_la_desaparicion', 'Pilar',
  'La Fiscalía investiga la desaparición de varias personas después de un '
  'operativo militar realizado en una zona rural.',
  None, 0.0),
 ('g02_la_fosa', 'Pilar',
  'Una fuente informa sobre la posible existencia de una fosa clandestina.',
  None, PARRAFO),
 ('g03_los_restos', 'Pilar',
  'Durante las actuaciones iniciales, los investigadores identifican restos '
  'humanos y algunas prendas de vestir.',
  None, NORMAL),
 ('g04_las_redes', 'Pilar',
  'También se obtiene información sobre fotografías y videos publicados en '
  'redes sociales durante los días del operativo.',
  None, PARRAFO),
 ('g05_la_publicacion', 'Pilar',
  'Una de las publicaciones muestra a personas que podrían corresponder a las '
  'víctimas.',
  None, NORMAL),
 ('g06_el_fiscal', 'Pilar',
  'El fiscal debe orientar las actuaciones de obtención y conservación de los '
  'elementos identificados.',
  None, PARRAFO),
]

BLOQUES['S08'] = [
 ('h01_la_custodia', 'Carlos',
  'La Fiscalía investiga la muerte de una persona que permanecía bajo '
  'custodia policial.',
  None, 0.0),
 ('h02_las_agresiones', 'Carlos',
  'Los familiares denuncian que la víctima había sufrido agresiones durante '
  'su detención.',
  None, PARRAFO),
 ('h03_el_video', 'Carlos',
  'También aportan información sobre un video publicado en redes sociales, en '
  'el que presuntamente se observan algunas de esas agresiones.',
  None, NORMAL),
 ('h04_las_inconsistencias', 'Carlos',
  'Durante las actuaciones iniciales se identifica que existen '
  'inconsistencias entre la información registrada por las autoridades '
  'policiales y los hallazgos médico-legales.',
  'Durante las actuaciones iniciales se identifica que existen '
  'inconsistencias entre la información registrada por las autoridades '
  'policiales y los hallazgos médico legales.',
  PARRAFO),
 ('h05_el_fiscal', 'Carlos',
  'El fiscal debe determinar qué instrumentos internacionales pueden orientar '
  'las actuaciones investigativas.',
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


def texto_lamina(clave):
    return '\n\n'.join(t for _, t in TEXTOS[clave])


if __name__ == '__main__':
    for k in VIDEOS:
        n = palabras(k)
        seg = n / 150.0 * 60 * 1.10
        print('%-4s %4d palabras %2d bloques ~%5.1f s de voz  %s'
              % (k, n, len(BLOQUES[k]), seg, TEMAS[k][0]))
    for k in IMAGENES:
        t = texto_lamina(k)
        print('%-4s lámina %4d palabras %4d caracteres' % (k, len(t.split()), len(t)))
