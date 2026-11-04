# -*- coding: utf-8 -*-
r"""Curso «Enfoque diferencial en la práctica del fiscal» (PRIORIDAD 2) ·
cinco videos.

LA FUENTE (Drive de la agencia)
    Carpeta «PRIORIDAD 2 - ENFOQUE DIFERENCIAL EN LA PRÁCTICA DEL FISCAL»
    https://drive.google.com/drive/folders/1gp1dof3SncgICHNNiuEW3HHBYxdSCZDJ
    «Caso: Édgar Molano»                         1n2um_ejZs1sDQLp-Il1G3nsiHVYigqJHnCFYNg19Mu0
    «Caso: Jairo Montero Salas»                  18Dh4Ez_pKGdfhMPjpoTZUjzbRFWDl1814WWlyqcCUIs
    «Caso: el patrullero Wilmer»                 1PDSbCfkrhv0y4PSVUcmEX5eEJrIOHeiYVSkM612ylRw
    «Caso: la niña del resguardo de Putumayo»    157Z6fbWlkv0BaY1ArQs-nz7xREii0XOpulEToytgOQU
    «Caso: la denuncia de Valentina»             1EQLkbB2Qh83Cf8drTzhu-hFBT6Xze3sFI7hngeohDV0
    Numerados en el orden en que la agencia los subió.

EL ENCARGO (Sebastián, 3 nov 2026)
    «Our script actually only starts after the subtitle "Fase de experiencia
    concreta"»: la voz empieza en el primer párrafo después de ese
    subtítulo. El título del caso va al cartón de entrada; la nota en
    cursiva («Caso construido con fines pedagógicos…») no entra.
    No pertenecen a ninguna unidad: una carpeta VIDEOS en el Drive.
    «Make it cinematic, feel like a movie, different camera angles, same
    characters, consistency, mid action stills, several complementary shots
    of the same scene». Créditos: reservar ~2.000 de lo que queda.

DOS TEXTOS POR BLOQUE, COMO EN TODA LA SERIE
    `texto`  el documento VERBATIM, para el cartón. Comillas «».
             Los números en dígitos.
    `tts`    lo mismo dicho para ElevenLabs: números en letras, siglas
             desplegadas, paréntesis y rayas a comas. Solo cuando hace falta.

ERRATAS DEL DOCUMENTO (la regla de la casa: «corregir lo obvio»)
    C5  «decidió denunciar que un excompañero sentimental que la había
        seguido» -> «decidió denunciar que un excompañero sentimental la
        había seguido» (sobra el segundo «que»).
    Las comillas rectas del documento pasan a «».

LAS VOCES (ElevenLabs, cuenta de Sebastián)
    Narran Carlos (C1, C3) y Pilar (C2, C4, C5).
    Las dos citas que el documento pone en boca de una persona con nombre o
    con oficio, y que son lo que el caso discute, las dice esa persona:
        C3  Wilmer: «lo que más me dolió no fueron los golpes…» -> Andres
        C5  el funcionario: «¿ese es su nombre real o es un apodo?» y
            «¿pero su pareja o su amante?» -> Julian
    No se inventa ningún parlamento: son las palabras del documento, en la
    voz de quien el documento dice que las dijo. Las frases de los
    agresores y del coronel las dice el narrador (citadas, a distancia).
"""

PREFIJO = 'ED_'

CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.7
PARRAFO = 1.1
CITA = 0.45

DRIVE = 'https://drive.google.com/drive/folders/1gp1dof3SncgICHNNiuEW3HHBYxdSCZDJ'
DRIVE_VIDEOS = '1qKmKVuwmNGKaTLbzgtm2pc5-uqf98k9u'

CURSO = 'Enfoque diferencial en la práctica del fiscal'
ANTE = 'Enfoque diferencial'

# clave -> (tipo, unidad, carpeta de la pieza, voz, antetitulo, titulo)
PIEZAS = {
 'C1': ('video', 0, 'CASO 1 - Edgar Molano', 'Carlos',
        'Caso 1', 'Édgar Molano'),
 'C2': ('video', 0, 'CASO 2 - Jairo Montero Salas', 'Pilar',
        'Caso 2', 'Jairo Montero Salas'),
 'C3': ('video', 0, 'CASO 3 - El patrullero Wilmer', 'Carlos',
        'Caso 3', 'El patrullero Wilmer'),
 'C4': ('video', 0, 'CASO 4 - La nina del resguardo de Putumayo', 'Pilar',
        'Caso 4', 'La niña del resguardo de Putumayo'),
 'C5': ('video', 0, 'CASO 5 - La denuncia de Valentina', 'Pilar',
        'Caso 5', 'La denuncia de Valentina'),
}
UNIDADES = {0: 'VIDEOS'}

VIDEOS = [k for k, v in PIEZAS.items() if v[0] == 'video']
IMAGENES = []

# compatibilidad con las herramientas de la serie (dh_pieza & co.):
# TEMAS[clave] = (carpeta relativa a la raiz del curso, voz, antetitulo, titulo)
TEMAS = {k: (UNIDADES[v[1]] + '\\' + v[2], v[3], v[4], v[5])
         for k, v in PIEZAS.items()}

ENTREGA = {
 'C1': 'PRIO 2 - ENFOQUE DIFERENCIAL - CASO 1 EDGAR MOLANO',
 'C2': 'PRIO 2 - ENFOQUE DIFERENCIAL - CASO 2 JAIRO MONTERO SALAS',
 'C3': 'PRIO 2 - ENFOQUE DIFERENCIAL - CASO 3 EL PATRULLERO WILMER',
 'C4': 'PRIO 2 - ENFOQUE DIFERENCIAL - CASO 4 LA NIÑA DEL RESGUARDO DE PUTUMAYO',
 'C5': 'PRIO 2 - ENFOQUE DIFERENCIAL - CASO 5 LA DENUNCIA DE VALENTINA',
}

# (id, voz, texto VERBATIM, tts o None, pausa antes en segundos)
BLOQUES = {}

BLOQUES['C1'] = [
 ('a01_el_fiscal', 'Carlos',
  'Édgar Molano es el fiscal asignado a una Unidad de Atención a Víctimas de '
  'Violencia Sexual.',
  None, 0.0),
 ('a02_la_denuncia', 'Carlos',
  'Recibe la denuncia de Yolanda, una mujer de 29 años con discapacidad '
  'cognitiva leve, diagnosticada desde la infancia, quien manifiesta haber '
  'sido accedida carnalmente por un vecino del barrio, varios años mayor que '
  'ella, en reiteradas ocasiones durante los últimos meses.',
  'Recibe la denuncia de Yolanda, una mujer de veintinueve años con '
  'discapacidad cognitiva leve, diagnosticada desde la infancia, quien '
  'manifiesta haber sido accedida carnalmente por un vecino del barrio, varios '
  'años mayor que ella, en reiteradas ocasiones durante los últimos meses.',
  NORMAL),
 ('a03_la_historia_clinica', 'Carlos',
  'En la entrevista inicial, el fiscal Molano revisa la historia clínica de '
  'Yolanda y encuentra el diagnóstico de discapacidad cognitiva leve '
  'certificado por su EPS.',
  'En la entrevista inicial, el fiscal Molano revisa la historia clínica de '
  'Yolanda y encuentra el diagnóstico de discapacidad cognitiva leve '
  'certificado por su E P S.',
  PARRAFO),
 ('a04_la_imputacion', 'Carlos',
  'Con ese solo documento, formula la imputación por el delito de acceso '
  'carnal abusivo con incapaz de resistir (artículo 210 del Código Penal), '
  'sustentando toda la hipótesis de incapacidad para consentir en el '
  'diagnóstico médico.',
  'Con ese solo documento, formula la imputación por el delito de acceso '
  'carnal abusivo con incapaz de resistir, artículo doscientos diez del Código '
  'Penal, sustentando toda la hipótesis de incapacidad para consentir en el '
  'diagnóstico médico.',
  NORMAL),
 ('a05_no_ordena', 'Carlos',
  'No ordena entrevista psicológica forense centrada en la comprensión y '
  'voluntariedad de Yolanda frente a esos hechos específicos;',
  None, NORMAL),
 ('a06_no_indaga', 'Carlos',
  'no indaga sobre la naturaleza de la relación entre ella y el procesado, ni '
  'sobre posibles patrones de manipulación, engaño o aprovechamiento de una '
  'posición de poder;',
  None, 0.5),
 ('a07_tampoco', 'Carlos',
  'tampoco explora si Yolanda tenía la capacidad de comprender la relación '
  'sexual y expresar su voluntad frente a ella.',
  None, 0.5),
 ('a08_la_defensa', 'Carlos',
  'En la audiencia de formulación de acusación, la defensa del procesado '
  'invoca la Sentencia C-163 de 2021 y argumenta que la Fiscalía incurrió '
  'exactamente en la presunción que la Corte Constitucional declaró '
  'inadmisible:',
  'En la audiencia de formulación de acusación, la defensa del procesado '
  'invoca la Sentencia C ciento sesenta y tres de dos mil veintiuno y '
  'argumenta que la Fiscalía incurrió exactamente en la presunción que la '
  'Corte Constitucional declaró inadmisible:',
  PARRAFO),
 ('a09_equiparar', 'Carlos',
  'equiparar automáticamente el diagnóstico de discapacidad con la incapacidad '
  'de resistir, sin acreditar que, en el caso concreto, Yolanda careciera '
  'realmente de la posibilidad de comprender el acto o de oponerse a él.',
  None, 0.5),
 ('a10_modelo_social', 'Carlos',
  'La defensa sostiene que, conforme al modelo social de discapacidad '
  'adoptado por la Convención sobre los Derechos de las Personas con '
  'Discapacidad, Yolanda se presume con plena autonomía para su vida sexual,',
  None, NORMAL),
 ('a11_solo_el_diagnostico', 'Carlos',
  'y que la Fiscalía no aportó ninguna prueba de coacción, engaño o '
  'aprovechamiento, sino solamente el diagnóstico.',
  None, 0.4),
 ('a12_el_juez', 'Carlos',
  'El juez de conocimiento, acogiendo este planteamiento, señala que la '
  'acusación tiene un vacío probatorio serio:',
  None, PARRAFO),
 ('a13_el_vacio', 'Carlos',
  'no existe evidencia sobre el contexto de la relación, la posible asimetría '
  'de poder, el engaño o la coacción —elementos que sí habrían permitido '
  'sostener la ausencia de consentimiento real—, y que la sola referencia al '
  'diagnóstico no basta.',
  'no existe evidencia sobre el contexto de la relación, la posible asimetría '
  'de poder, el engaño o la coacción, elementos que sí habrían permitido '
  'sostener la ausencia de consentimiento real, y que la sola referencia al '
  'diagnóstico no basta.',
  0.5),
 ('a14_el_receso', 'Carlos',
  'El fiscal Molano debe entonces solicitar un receso y reorientar la '
  'investigación:',
  None, NORMAL),
 ('a15_la_valoracion', 'Carlos',
  'ordena una valoración psicológica forense específica sobre la comprensión '
  'y voluntariedad de Yolanda en relación con los hechos denunciados, '
  'entrevista a su red de apoyo familiar,',
  None, 0.5),
 ('a16_bases_solidas', 'Carlos',
  'indaga sobre la dinámica de la relación con el procesado y recauda '
  'evidencia sobre el contexto de vulnerabilidad manifiesta, antes de poder '
  'sostener nuevamente la acusación sobre bases sólidas.',
  None, 0.4),
]

BLOQUES['C2'] = [
 ('b01_el_profesor', 'Pilar',
  'Jairo Montero Salas era profesor universitario, de origen venezolano, '
  'radicado hacía varios años en una ciudad intermedia del Caribe colombiano.',
  None, 0.0),
 ('b02_el_activista', 'Pilar',
  'Era un reconocido defensor de derechos humanos y líder del activismo LGBTI '
  'en su ciudad.',
  'Era un reconocido defensor de derechos humanos y líder del activismo ele '
  'ge be te i en su ciudad.',
  NORMAL),
 ('b03_las_amenazas', 'Pilar',
  'En los días previos a su muerte había recibido amenazas relacionadas con su '
  'labor como activista.',
  None, NORMAL),
 ('b04_la_manana', 'Pilar',
  'Una mañana de finales de agosto, en su vivienda del barrio donde residía, '
  'Jairo fue asesinado de manera extremadamente violenta:',
  None, PARRAFO),
 ('b05_la_herramienta', 'Pilar',
  'recibió varios golpes en el rostro con una herramienta artesanal que él '
  'mismo había traído de un viaje al Pacífico, con heridas profundas.',
  None, 0.5),
 ('b06_el_cumpleanos', 'Pilar',
  'Su cuerpo fue hallado al día siguiente, coincidiendo con la fecha de su '
  'cumpleaños; sobre una silla de su habitación permanecía la ropa que había '
  'preparado para la celebración.',
  None, NORMAL),
 ('b07_nada_robado', 'Pilar',
  'No se sustrajo ningún objeto de valor de la vivienda.',
  None, 0.6),
 ('b08_el_prejuicio', 'Pilar',
  'Desde las primeras horas, la actuación institucional estuvo marcada por el '
  'prejuicio.',
  None, PARRAFO),
 ('b09_el_coronel', 'Pilar',
  'El entonces comandante de la Policía Metropolitana de la región, coronel '
  'Hernán Ocampo Rueda, declaró públicamente que se trataba de un «caso de '
  'maricones» y lo calificó como un «crimen absolutamente pasional», '
  'señalando que la víctima «llevaba una vida desordenada» y era «promiscua».',
  None, NORMAL),
 ('b10_antes_de', 'Pilar',
  'Estas declaraciones, hechas por la máxima autoridad policial de la región a '
  'cargo del caso, se emitieron antes de que existiera una sola línea de '
  'investigación seria sobre el móvil del homicidio.',
  None, NORMAL),
 ('b11_la_escena', 'Pilar',
  'El manejo de la escena del crimen también presentó irregularidades: '
  'miembros de la Policía ingresaron sin la debida protección del lugar de los '
  'hechos, lo que comprometió elementos materiales probatorios.',
  None, PARRAFO),
 ('b12_la_camisa', 'Pilar',
  'No se recolectaron elementos que podían resultar determinantes, como la '
  'camisa que se había comprado para sus cumpleaños y el pantalón de la '
  'víctima, no se realizó la toma de huellas, el piso de la vivienda fue '
  'lavado antes de que se recogieran muestras.',
  None, NORMAL),
 ('b13_la_custodia', 'Pilar',
  'Además, en la escena había rastros y posibles elementos con las mismas '
  'características del arma homicida, que no fueron embalados ni custodiados '
  'conforme a la cadena de custodia, entre otras omisiones que se evidenciaron '
  'en el expediente.',
  None, NORMAL),
 ('b14_el_despacho', 'Pilar',
  'El caso pasó por distintos despachos, y el fiscal a cargo en una de sus '
  'etapas fundamentó la hipótesis de «crimen pasional» señalando que la '
  'víctima recibía «muchos sujetos» en su vivienda y no tenía «pareja '
  'estable»',
  None, NORMAL),
 ('b15_mauricio', 'Pilar',
  '—pese a que, en realidad, Jairo mantenía una relación sentimental de más de '
  'ocho años con Mauricio Reyes—.',
  'pese a que, en realidad, Jairo mantenía una relación sentimental de más de '
  'ocho años con Mauricio Reyes.',
  0.45),
 ('b16_parte_civil', 'Pilar',
  'La pareja de Jairo intentó ser reconocida como parte civil dentro del '
  'proceso, al igual que una fundación creada por activistas LGBTI de la '
  'ciudad específicamente a raíz de este crimen.',
  'La pareja de Jairo intentó ser reconocida como parte civil dentro del '
  'proceso, al igual que una fundación creada por activistas ele ge be te i '
  'de la ciudad específicamente a raíz de este crimen.',
  PARRAFO),
 ('b17_negadas', 'Pilar',
  'Ambas solicitudes fueron negadas o resueltas de manera extemporánea por el '
  'despacho a cargo.',
  None, 0.6),
 ('b18_la_desidia', 'Pilar',
  'Según el informe de la fundación, «todas las actuaciones surtidas al '
  'interior de ese despacho denotaron una permanente desidia frente a la '
  'práctica de interrogatorios»,',
  None, NORMAL),
 ('b19_la_vida_sexual', 'Pilar',
  'y gran parte del esfuerzo investigativo se concentró en indagar sobre la '
  'vida sexual de la víctima, en lugar de sobre la evidencia forense '
  'disponible.',
  None, 0.4),
 ('b20_diez_anos', 'Pilar',
  'Diez años después de los hechos, el caso seguía en etapa de indagatoria, '
  'sin una sola persona imputada.',
  None, PARRAFO),
 ('b21_decenas', 'Pilar',
  'La fundación documentó, en el mismo periodo, decenas de homicidios y '
  'amenazas contra personas LGBTI en la región, con participación o '
  'complicidad policial señalada en varios de esos casos.',
  'La fundación documentó, en el mismo periodo, decenas de homicidios y '
  'amenazas contra personas ele ge be te i en la región, con participación o '
  'complicidad policial señalada en varios de esos casos.',
  NORMAL),
 ('b22_impune', 'Pilar',
  'El crimen de Jairo Montero Salas permanece impune.',
  None, 0.9),
]

BLOQUES['C3'] = [
 ('c01_el_turno', 'Carlos',
  'Wilmer llevaba seis años en la Policía Nacional y esa noche hacía turno en '
  'el aeropuerto de una capital de departamento.',
  None, 0.0),
 ('c02_la_llamada', 'Carlos',
  'Recibió una llamada de la tripulación de un vuelo próximo a despegar: dos '
  'pasajeros, en evidente estado de embriaguez, se negaban a descender pese a '
  'que el reglamento aeronáutico lo exigía por razones de seguridad.',
  None, NORMAL),
 ('c03_la_aeronave', 'Carlos',
  'Wilmer subió a la aeronave junto a un compañero. Se acercó a los '
  'pasajeros, les explicó con calma la situación y les pidió que lo '
  'acompañaran a la salida.',
  None, PARRAFO),
 ('c04_los_golpes', 'Carlos',
  'Los dos hombres se negaron y, ante la insistencia de Wilmer, se resistieron '
  'físicamente: cuando él los tomó del brazo para conducirlos hacia la puerta, '
  'ambos empezaron a golpearlo repetidamente —uno de ellos con mayor '
  'intensidad que el otro—,',
  'Los dos hombres se negaron y, ante la insistencia de Wilmer, se resistieron '
  'físicamente: cuando él los tomó del brazo para conducirlos hacia la puerta, '
  'ambos empezaron a golpearlo repetidamente, uno de ellos con mayor '
  'intensidad que el otro,',
  NORMAL),
 ('c05_los_celulares', 'Carlos',
  'mientras los demás pasajeros, con los celulares en alto, grababan la '
  'escena.',
  None, 0.4),
 ('c06_el_video', 'Carlos',
  'El video se difundió esa misma noche en redes sociales y generó '
  'indignación pública.',
  None, NORMAL),
 ('c07_el_traslado', 'Carlos',
  'Una vez controlada la situación, Wilmer condujo a los dos hombres hacia la '
  'estación de Policía ubicada en el aeropuerto.',
  None, PARRAFO),
 ('c08_los_insultos', 'Carlos',
  'Fue solo entonces, durante el traslado, cuando comenzaron las expresiones '
  'racistas: de manera reiterada lo llamaron «negro hijueputa» y «negro '
  'malparido» y, en medio de los insultos, uno de ellos manifestó: «por eso es '
  'que matan a los negros».',
  None, NORMAL),
 ('c09_la_estacion', 'Carlos',
  'Las agresiones verbales continuaron al llegar a la estación. Allí volvieron '
  'a dirigirse a Wilmer con expresiones como «negro malparido» y «negro '
  'hijueputa».',
  None, NORMAL),
 ('c10_el_coronel', 'Carlos',
  'Además, en dos oportunidades le dijeron: «ya estamos llamando al coronel '
  'para que lo trasladen a usted, negro».',
  None, NORMAL),
 ('c11_la_imputacion', 'Carlos',
  'Los dos agresores fueron capturados por agresión a servidor público, pero '
  'el fiscal de turno les imputó únicamente el delito de violencia contra '
  'servidor público,',
  None, PARRAFO),
 ('c12_sin_considerar', 'Carlos',
  'sin considerar la circunstancia de agravación punitiva por móvil '
  'discriminatorio prevista en el artículo 58, numeral 3, del Código Penal, ni '
  'el posible delito autónomo de hostigamiento (art. 134B).',
  'sin considerar la circunstancia de agravación punitiva por móvil '
  'discriminatorio prevista en el artículo cincuenta y ocho, numeral tres, del '
  'Código Penal, ni el posible delito autónomo de hostigamiento, artículo '
  'ciento treinta y cuatro be.',
  0.45),
 ('c13_en_libertad', 'Carlos',
  'Esa misma noche quedaron en libertad con esa calificación jurídica.',
  None, NORMAL),
 ('c14_las_disculpas', 'Carlos',
  'Semanas después, ante la presión mediática, los agresores ofrecieron '
  'disculpas públicas a Wilmer.',
  None, PARRAFO),
 ('c15_declaro', 'Carlos',
  'Él, sin embargo, declaró a un medio local:',
  None, 0.5),
 ('c16_wilmer', 'Andres',
  '«lo que más me dolió no fueron los golpes, fue que nadie, al principio, '
  'quiso llamar las cosas por su nombre».',
  'Lo que más me dolió no fueron los golpes... fue que nadie, al principio, '
  'quiso llamar las cosas por su nombre.',
  CITA),
 ('c17_la_revision', 'Carlos',
  'Solo tiempo después, al revisar el caso, la Fiscalía advirtió que el patrón '
  'verbal reiterado documentado durante el traslado y en la estación '
  '—separado en el tiempo de la agresión física inicial— no había sido '
  'valorado en la calificación jurídica original.',
  'Solo tiempo después, al revisar el caso, la Fiscalía advirtió que el patrón '
  'verbal reiterado documentado durante el traslado y en la estación, separado '
  'en el tiempo de la agresión física inicial, no había sido valorado en la '
  'calificación jurídica original.',
  PARRAFO),
 ('c18_la_adicion', 'Carlos',
  'Mediante una adición a la imputación, se incorporaron tanto la '
  'circunstancia de agravación del artículo 58.3 como el delito autónomo de '
  'hostigamiento (art. 134B), en concurso con la violencia contra servidor '
  'público ya imputada.',
  'Mediante una adición a la imputación, se incorporaron tanto la '
  'circunstancia de agravación del artículo cincuenta y ocho, numeral tres, '
  'como el delito autónomo de hostigamiento, artículo ciento treinta y cuatro '
  'be, en concurso con la violencia contra servidor público ya imputada.',
  NORMAL),
 ('c19_la_correccion', 'Carlos',
  'Esta corrección procesal, más que un simple ajuste técnico, evidencia cómo '
  'una primera lectura de los hechos invisibilizó su dimensión racial, y cómo '
  'fue necesaria una revisión posterior para restituirla a la calificación '
  'jurídica.',
  None, NORMAL),
]

# 4 nov (revision de Sebastian, C4): «Taita se pronuncia con tilde en la
# primera a». En d02 ElevenLabs dijo «taíta» (tres silabas). En el TTS va
# «Táita» (el verbatim del carton sigue «Taita»); la toma de d02 se corrigio
# injertando la palabra (`voz/taita_c4.py`).
BLOQUES['C4'] = [
 ('d01_el_resguardo', 'Pilar',
  'En un resguardo indígena cercano a Puerto Guzmán, Putumayo, Yaneth '
  'Payaguaje —niña de la comunidad— pasaba todos los días frente a la vivienda '
  'de Hipólito Jacanamijoy,',
  'En un resguardo indígena cercano a Puerto Guzmán, Putumayo, Yaneth '
  'Payaguaje, niña de la comunidad, pasaba todos los días frente a la vivienda '
  'de Hipólito Jacanamijoy,',
  0.0),
 ('d02_el_taita', 'Pilar',
  'autoridad indígena (Taita) de un cabildo con una estructura política y '
  'organizativa débil y escasa capacidad de gobierno propio.',
  'autoridad indígena, Táita, de un cabildo con una estructura política y '
  'organizativa débil y escasa capacidad de gobierno propio.',
  0.35),
 ('d03_la_rutina', 'Pilar',
  'Después de conocer su rutina durante varias semanas, Jacanamijoy, '
  'aprovechando su posición de autoridad y la confianza que esta le confería '
  'ante la familia y la comunidad,',
  None, NORMAL),
 ('d04_la_llamo', 'Pilar',
  'la llamó reiteradamente a su casa, donde abusó sexualmente de ella en '
  'varias ocasiones.',
  None, 0.4),
 ('d05_la_madre', 'Pilar',
  'Cuando la madre de la menor tuvo conocimiento de los hechos, acudió primero '
  'ante las autoridades del cabildo para denunciar.',
  None, PARRAFO),
 ('d06_la_reunion', 'Pilar',
  'Estas se reunieron para tratar el caso —como corresponde al procedimiento '
  'propio de la comunidad— pero en la deliberación concluyeron que no tenían '
  'la fuerza política ni los mecanismos internos para actuar contra el Taita,',
  'Estas se reunieron para tratar el caso, como corresponde al procedimiento '
  'propio de la comunidad, pero en la deliberación concluyeron que no tenían '
  'la fuerza política ni los mecanismos internos para actuar contra el Táita,',
  NORMAL),
 ('d07_el_desequilibrio', 'Pilar',
  'dado el desequilibrio de poder que este ostentaba dentro del resguardo: '
  'investigarlo a él, siendo la máxima autoridad de la comunidad, no era algo '
  'que el cabildo se sintiera en capacidad de emprender.',
  None, 0.45),
 ('d08_la_justicia', 'Pilar',
  'Ante esta respuesta, la madre acudió a la justicia occidentalizada.',
  None, PARRAFO),
 ('d09_sin_claridad', 'Pilar',
  'El fiscal que recibió el caso no tenía claridad sobre cómo proceder frente '
  'a un hecho ocurrido en territorio ancestral y protagonizado por una '
  'autoridad indígena.',
  None, NORMAL),
 ('d10_los_colegas', 'Pilar',
  'Consultó a varios colegas de la unidad: algunos le recomendaron quedarse '
  'con el caso y avocar conocimiento directamente, mientras otros insistían en '
  'que lo devolviera al resguardo por tratarse de un asunto de competencia de '
  'la JEI.',
  'Consultó a varios colegas de la unidad: algunos le recomendaron quedarse '
  'con el caso y avocar conocimiento directamente, mientras otros insistían en '
  'que lo devolviera al resguardo por tratarse de un asunto de competencia de '
  'la Jurisdicción Especial Indígena.',
  NORMAL),
 ('d11_la_mesa', 'Pilar',
  'Ante la falta de consenso, el fiscal gestionó la conformación de una mesa '
  'técnica interinstitucional para resolver la duda.',
  None, PARRAFO),
 ('d12_la_recomendacion', 'Pilar',
  'En esa mesa, la recomendación mayoritaria fue devolver el caso a la '
  'jurisdicción indígena, considerando el lugar de ocurrencia de los hechos y '
  'la pertenencia étnica del presunto agresor.',
  None, NORMAL),
 ('d13_remitio', 'Pilar',
  'Con base en esa recomendación, el fiscal remitió el caso de vuelta al '
  'resguardo.',
  None, NORMAL),
 ('d14_punto_muerto', 'Pilar',
  'La menor y su madre quedaron así en un punto muerto:',
  None, PARRAFO),
 ('d15_ninguna', 'Pilar',
  'el cabildo ya había señalado que no podía actuar contra su propia '
  'autoridad, y ahora la justicia occidentalizada, tras deliberar '
  'internamente, también declinaba el caso.',
  None, 0.45),
 ('d16_en_su_cargo', 'Pilar',
  'Ninguna de las dos jurisdicciones lo asumió, mientras el agresor —Taita del '
  'resguardo— permanecía en ejercicio de su cargo, sin que se activara medida '
  'de protección alguna a favor de la víctima.',
  'Ninguna de las dos jurisdicciones lo asumió, mientras el agresor, Táita del '
  'resguardo, permanecía en ejercicio de su cargo, sin que se activara medida '
  'de protección alguna a favor de la víctima.',
  NORMAL),
]

BLOQUES['C5'] = [
 ('e01_valentina', 'Pilar',
  'Valentina, mujer trans de 29 años, decidió denunciar que un excompañero '
  'sentimental la había seguido y amenazado durante varios días.',
  'Valentina, mujer trans de veintinueve años, decidió denunciar que un '
  'excompañero sentimental la había seguido y amenazado durante varios días.',
  0.0),
 ('e02_el_valor', 'Pilar',
  'Reunió el valor para acercarse a la Fiscalía de su ciudad y relatar lo '
  'ocurrido.',
  None, NORMAL),
 ('e03_la_recepcion', 'Pilar',
  'En la recepción, el funcionario le solicitó su documento de identidad.',
  None, PARRAFO),
 ('e04_en_voz_alta', 'Pilar',
  'Al ver que el nombre registrado no coincidía con el nombre por el cual ella '
  'se presentó, le preguntó en voz alta, frente a otras personas que esperaban '
  'de turno:',
  None, NORMAL),
 ('e05_el_apodo', 'Julian',
  '«¿ese es su nombre real o es un apodo?».',
  '¿Ese es su nombre real... o es un apodo?',
  CITA),
 ('e06_su_nombre', 'Pilar',
  'Valentina explicó que Valentina era su nombre identitario.',
  None, CITA),
 ('e07_el', 'Pilar',
  'Durante la diligencia, el funcionario se refirió a ella varias veces como '
  '«él», pese a que Valentina lo corrigió en más de una ocasión.',
  None, PARRAFO),
 ('e08_alias', 'Pilar',
  'Al diligenciar el formato de denuncia, consignó el nombre legal como el '
  'nombre de la denunciante y escribió «alias Valentina» en el campo de '
  'observaciones',
  None, NORMAL),
 ('e09_el_campo', 'Pilar',
  '—el mismo campo que normalmente se usa para registrar apodos de personas '
  'investigadas por un delito, no de víctimas.',
  'el mismo campo que normalmente se usa para registrar apodos de personas '
  'investigadas por un delito, no de víctimas.',
  0.4),
 ('e10_la_pareja', 'Pilar',
  'En un momento de la entrevista, al preguntarle por las circunstancias del '
  'hostigamiento, el funcionario se sorprendió al escuchar que la persona que '
  'la seguía había sido su pareja sentimental, y le preguntó:',
  None, PARRAFO),
 ('e11_o_su_amante', 'Julian',
  '«¿pero su pareja o su amante?»,',
  '¿Pero su pareja... o su amante?',
  CITA),
 ('e12_convencional', 'Pilar',
  'dando a entender que no concebía que Valentina pudiera tener una relación '
  'de pareja convencional.',
  None, CITA),
 ('e13_la_casilla', 'Pilar',
  'Más adelante, el formulario lo llevó a preguntarle por su orientación '
  'sexual en lugar de su identidad de género —porque esa era, literalmente, la '
  'única casilla disponible en el formato de la Fiscalía—.',
  'Más adelante, el formulario lo llevó a preguntarle por su orientación '
  'sexual en lugar de su identidad de género, porque esa era, literalmente, la '
  'única casilla disponible en el formato de la Fiscalía.',
  PARRAFO),
 ('e14_hombre_gay', 'Pilar',
  'Pero en lugar de consignar con precisión lo que Valentina le respondió, el '
  'funcionario, guiado por sus propias ideas preconcebidas sobre lo que '
  '«debía» ser una persona trans, escribió en la casilla «hombre gay»,',
  None, NORMAL),
 ('e15_nunca', 'Pilar',
  'una categoría que Valentina nunca manifestó y que no correspondía ni a su '
  'identidad de género ni a lo que ella había expresado sobre sí misma.',
  None, 0.4),
 ('e16_la_suposicion', 'Pilar',
  'El funcionario no transcribió la respuesta de la víctima: la sustituyó por '
  'su propia suposición.',
  None, NORMAL),
 ('e17_salio', 'Pilar',
  'Valentina salió de la estación sintiendo que, en lugar de haber sido '
  'escuchada como víctima, había quedado señalada como si fuera ella la '
  'irregular, y registrada además con una etiqueta que ni siquiera era la '
  'suya.',
  None, PARRAFO),
 ('e18_no_volvio', 'Pilar',
  'No volvió a insistir en el trámite de la denuncia.',
  None, 0.8),
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
    for k in VIDEOS:
        n = palabras(k)
        seg = n / 150.0 * 60 * 1.10
        print('%-3s %4d palabras %2d bloques ~%5.1f s de voz  %s'
              % (k, n, len(BLOQUES[k]), seg, TEMAS[k][0]))
