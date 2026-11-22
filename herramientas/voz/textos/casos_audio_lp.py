# -*- coding: utf-8 -*-
r"""Ley 1826 · audios de los casos para el aula (21 nov 2026). Un paréntesis en el trabajo de video.

EL PEDIDO
    «Audios de los casos: textos para grabar», de Samir Andrés Ardila para Sebastián (21/11/2026): en la reunión de
    ese día Juan pidió poner audio a la parte de los casos del curso, con ElevenLabs. 13 casos y 19 tramos: «A» es el
    planteamiento (suena al abrir la diapositiva del caso, voz de mujer) y «B» la resolución (suena al abrir la
    solución, voz de hombre). Un archivo por tramo, con su código como nombre (U1-C1-A.mp3). El texto es el del
    documento aprobado del curso (17/11/2026), tal cual; el pedido trae las cuatro frases que el aprobado corrigió
    frente a los documentos de Juan («las tapas», «se tomaron entrevistas», «recibir» y la pregunta corta del caso 3
    de la U3).

LAS VOCES
    Las del curso y de toda la serie, en la cuenta de Sebastián: Pilar para los planteamientos, Carlos para las
    resoluciones (el pedido propone mujer y hombre y dice que ninguna voz está definida).

DOS TEXTOS POR TRAMO, COMO EN TODA LA SERIE
    `texto` el del pedido, verbatim. `tts` lo mismo dicho para ElevenLabs, con las reglas del pedido: abreviaturas
    completas («art.» artículo, «CP» Código Penal, «CPP» Código de Procedimiento Penal, «VIF» violencia
    intrafamiliar, «HJR» hechos jurídicamente relevantes, «N°» número, «VBG» violencia basada en género); radicados
    y referencias de sentencia letra por letra y número por número, sin guiones; y las de la casa: números en letras,
    paréntesis a comas, placas y formatos deletreados como en los videos del curso (`guion_lp.py`).

ERRATAS (la regla de la casa: «corregir lo obvio»; las mismas que ya se corrigieron en `guion_lp.py`)
    U1-C5-B «la armonía familia» → «la armonía familiar».
    U2-C1-A «constató que etiquetas y las tapas» → «que las etiquetas y las tapas».
    U4-C1-A «con el argumento de que que la inasistencia» → «de que la».

SE LEE TAL CUAL, Y SE AVISA
    U1-C2-B: después de «la redacción correcta de los HJR en el escrito debe estructurarse así:» el documento trae
    dos párrafos entre comillas. El primero no es una redacción de HJR: repite, a medias, la síntesis del caso 1
    («…golpeándola con las manos e insultándola. La Fiscalía adecuó la conducta como VIF agravada… No obstante, en
    la acusación no se incluyeron hechos de contexto…»). Parece un pegado de más. Se lee, porque es el texto aprobado.
"""

PILAR = 'x6LHvMgpXmty838MUqHh'
CARLOS = 'Y4HwpMNrBWN5dFKi5Lw8'
VOZ = {'Mujer': PILAR, 'Hombre': CARLOS}

RAD = 'efe, ge, ene, ese, uno, dos, cero, dos, cuatro, seis, nueve, ocho, cero, seis, %s'
SP = 'ese, pe, cero, uno, cuatro, dos, cero, dos, seis'
SUJETOS = 'Sujetos: José A. C., acusado, y María T. C., víctima.'
VIF229 = 'Delito: violencia intrafamiliar, artículo doscientos veintinueve del Código Penal.'

# (código, voz, texto verbatim, tts)
TRAMOS = [
 ('U1-C1-A', 'Mujer',
  'Caso de estudio 1\nExpediente simulado N° 1\nRadicado: FGN-S1-2024-69806-A\nDelito: VIF (art. 229 del CP)\n'
  'Sujetos: José A.C. (acusado) / María T.C. (víctima)\nTema central: Traslado del escrito de acusación y principio '
  'de congruencia frente a circunstancias de agravación.\nSíntesis fáctica del caso: El 11 de julio de 2024, bajo las '
  'reglas de la Ley 1826 de 2017, la Fiscalía corrió traslado del escrito de acusación a José A.C. En la sección de '
  'hechos se le imputó haber agredido a su compañera permanente María T.C. la noche del 5 de agosto de 2023 en su '
  'vivienda del barrio Prado Alto al golpearla con las manos e insultarla. La Fiscalía adecuó la conducta como VIF '
  'agravada (art. 229, inciso 2 del CP). No obstante, en la acusación no se incluyeron hechos de contexto sobre actos '
  'de dominación o violencia previas e históricas contra la víctima.\nProblema jurídico: ¿Se vulnera el principio de '
  'congruencia y el derecho a la defensa si el juez o tribunal condena por la agravante del inciso 2 del artículo 229 '
  'del CP cuando en el traslado del escrito de acusación no se formularon hechos de contexto sobre dominación previa?',
  'Caso de estudio uno.\n\nExpediente simulado número uno.\n\nRadicado: ' + RAD % 'a' + '.\n\n' + VIF229 + '\n\n'
  + SUJETOS + '\n\nTema central: Traslado del escrito de acusación y principio de congruencia frente a '
  'circunstancias de agravación.\n\nSíntesis fáctica del caso: El once de julio de dos mil veinticuatro, bajo las '
  'reglas de la Ley mil ochocientos veintiséis de dos mil diecisiete, la Fiscalía corrió traslado del escrito de '
  'acusación a José A. C. En la sección de hechos se le imputó haber agredido a su compañera permanente María T. C. '
  'la noche del cinco de agosto de dos mil veintitrés en su vivienda del barrio Prado Alto, al golpearla con las '
  'manos e insultarla. La Fiscalía adecuó la conducta como violencia intrafamiliar agravada, artículo doscientos '
  'veintinueve, inciso dos, del Código Penal. No obstante, en la acusación no se incluyeron hechos de contexto sobre '
  'actos de dominación o violencia previas e históricas contra la víctima.\n\nProblema jurídico: ¿Se vulnera el '
  'principio de congruencia y el derecho a la defensa si el juez o tribunal condena por la agravante del inciso dos '
  'del artículo doscientos veintinueve del Código Penal, cuando en el traslado del escrito de acusación no se '
  'formularon hechos de contexto sobre dominación previa?'),

 ('U1-C1-B', 'Hombre',
  'Resolución: La respuesta es sí. En el procedimiento especial abreviado, el traslado del escrito de acusación '
  'equivale formal y materialmente a la audiencia de formulación de imputación (art. 536 del CPP). Por consiguiente, '
  'este acto delimita de forma inalterable la hipótesis fáctica sobre la cual el procesado ejercerá su defensa.\n'
  'Como lo ratificó la Corte Suprema de Justicia al confirmar el fallo de segunda instancia: al no atribuirse en el '
  'escrito de acusación trasladado hechos específicos o de contexto sobre actos de dominación previa, no es '
  'jurídicamente viable aplicar la circunstancia de agravación del inciso 2 del artículo 229 del CP. Condenar por la '
  'agravante violaría el principio de congruencia, por lo que el procesado únicamente puede ser condenado como autor '
  'del delito de VIF en su modalidad simple.',
  'Resolución: La respuesta es sí. En el procedimiento especial abreviado, el traslado del escrito de acusación '
  'equivale formal y materialmente a la audiencia de formulación de imputación, artículo quinientos treinta y seis '
  'del Código de Procedimiento Penal. Por consiguiente, este acto delimita de forma inalterable la hipótesis fáctica '
  'sobre la cual el procesado ejercerá su defensa.\n\nComo lo ratificó la Corte Suprema de Justicia al confirmar el '
  'fallo de segunda instancia: al no atribuirse en el escrito de acusación trasladado hechos específicos o de '
  'contexto sobre actos de dominación previa, no es jurídicamente viable aplicar la circunstancia de agravación del '
  'inciso dos del artículo doscientos veintinueve del Código Penal. Condenar por la agravante violaría el principio '
  'de congruencia, por lo que el procesado únicamente puede ser condenado como autor del delito de violencia '
  'intrafamiliar en su modalidad simple.'),

 ('U1-C2-A', 'Mujer',
  'Caso de estudio 2\nExpediente simulado N° 2\nRadicado: FGN-S1-2024-69806-B\nDelito: VIF (art. 229 del CP)\n'
  'Sujetos: José A.C. (acusado) / María T.C. (víctima)\nTema central: Técnica de redacción de los HJR e indebida '
  'inclusión de medios probatorios.\nSíntesis fáctica del caso: Al redactar el escrito de acusación para el traslado, '
  'el asistente de fiscalía incluyó dentro del capítulo de hechos transcripciones de la entrevista realizada a la '
  'víctima, así como apartes textuales de los dictámenes emitidos por el Instituto Nacional de Medicina Legal y '
  'Ciencias Forenses el 6 de agosto de 2023. La defensa formuló observaciones en la audiencia concentrada señalando '
  'vaguedad e imprecisión en los cargos.\nProblema jurídico procesal: ¿Cuál es la forma técnica correcta de redactar '
  'los HJR en un escrito de acusación por VIF y por qué constituye un error confundirlos con los medios de prueba?',
  'Caso de estudio dos.\n\nExpediente simulado número dos.\n\nRadicado: ' + RAD % 'be' + '.\n\n' + VIF229 + '\n\n'
  + SUJETOS + '\n\nTema central: Técnica de redacción de los hechos jurídicamente relevantes e indebida inclusión de '
  'medios probatorios.\n\nSíntesis fáctica del caso: Al redactar el escrito de acusación para el traslado, el '
  'asistente de fiscalía incluyó dentro del capítulo de hechos transcripciones de la entrevista realizada a la '
  'víctima, así como apartes textuales de los dictámenes emitidos por el Instituto Nacional de Medicina Legal y '
  'Ciencias Forenses el seis de agosto de dos mil veintitrés. La defensa formuló observaciones en la audiencia '
  'concentrada señalando vaguedad e imprecisión en los cargos.\n\nProblema jurídico procesal: ¿Cuál es la forma '
  'técnica correcta de redactar los hechos jurídicamente relevantes en un escrito de acusación por violencia '
  'intrafamiliar, y por qué constituye un error confundirlos con los medios de prueba?'),

 ('U1-C2-B', 'Hombre',
  'Resolución técnica y fundamento jurisprudencial (SP014-2026): La jurisprudencia de la Sala Penal de la Corte '
  'Suprema exige distinguir estrictamente entre HJR, hechos indicadores y medios de prueba. Dado que en el '
  'procedimiento abreviado el traslado del escrito es la única oportunidad de imputación, la inclusión de '
  'transcripciones de dictámenes o testimonios en los hechos constituye un error técnico metodológico.\n'
  'Debe señalarse que los HJR deben describir exclusivamente las conductas fácticas humanas que encajan en los '
  'ingredientes del tipo penal. Tomando los hechos validados en la Sentencia SP014-2026, la redacción correcta de los '
  'HJR en el escrito debe estructurarse así:\n'
  '"El 5 de agosto de 2023, en su vivienda del barrio Prado Alto, golpeándola con las manos e insultándola. La '
  'Fiscalía adecuó la conducta como VIF agravada (art. 229, inciso 2 del CP). No obstante, en la acusación no se '
  'incluyeron hechos de contexto sobre actos de dominación o violencia previas e históricas contra la víctima".\n'
  '"El 5 de agosto de 2023, aproximadamente a las 8:00 p.m., en el inmueble ubicado en la carrera 25 C N, N° 4-13 de '
  'Bogotá, el señor José A.C. agredió a su compañera permanente María T.C. al exigirle mostrar sus conversaciones '
  'sostenidas por redes sociales; ante su negativa, la golpeó en el brazo con los puños, le retiró el teléfono '
  'celular, cerró la puerta con llave para impedirle la salida, e incurrió en tratos humillantes con palabras soeces '
  '(gorda asquerosa, sucia y perra), generándole un estado de angustia y terror que la llevó a pernoctar en el baño '
  'de la vivienda encerrada".',
  'Resolución técnica y fundamento jurisprudencial, ' + SP + ': La jurisprudencia de la Sala Penal de la Corte '
  'Suprema exige distinguir estrictamente entre hechos jurídicamente relevantes, hechos indicadores y medios de '
  'prueba. Dado que en el procedimiento abreviado el traslado del escrito es la única oportunidad de imputación, la '
  'inclusión de transcripciones de dictámenes o testimonios en los hechos constituye un error técnico metodológico.'
  '\n\nDebe señalarse que los hechos jurídicamente relevantes deben describir exclusivamente las conductas fácticas '
  'humanas que encajan en los ingredientes del tipo penal. Tomando los hechos validados en la Sentencia ' + SP + ', '
  'la redacción correcta de los hechos jurídicamente relevantes en el escrito debe estructurarse así:\n\n'
  'El cinco de agosto de dos mil veintitrés, en su vivienda del barrio Prado Alto, golpeándola con las manos e '
  'insultándola. La Fiscalía adecuó la conducta como violencia intrafamiliar agravada, artículo doscientos '
  'veintinueve, inciso dos, del Código Penal. No obstante, en la acusación no se incluyeron hechos de contexto sobre '
  'actos de dominación o violencia previas e históricas contra la víctima.\n\n'
  'El cinco de agosto de dos mil veintitrés, aproximadamente a las ocho de la noche, en el inmueble ubicado en la '
  'carrera veinticinco ce, ene, número cuatro guion trece, de Bogotá, el señor José A. C. agredió a su compañera '
  'permanente María T. C. al exigirle mostrar sus conversaciones sostenidas por redes sociales; ante su negativa, la '
  'golpeó en el brazo con los puños, le retiró el teléfono celular, cerró la puerta con llave para impedirle la '
  'salida, e incurrió en tratos humillantes con palabras soeces, gorda asquerosa, sucia y perra, generándole un '
  'estado de angustia y terror que la llevó a pernoctar en el baño de la vivienda, encerrada.'),

 ('U1-C3-A', 'Mujer',
  'Caso de estudio 3\nExpediente simulado N° 3\nRadicado: FGN-S1-2024-69806-C\nDelito: VIF (art. 229 del CP)\n'
  'Sujetos: José A.C. (acusado) / María T.C. (víctima)\nTema central: Análisis de concursos de delitos, '
  'subsidiariedad típica del maltrato y vía procedimental.\nSíntesis fáctica del caso: Durante el episodio del 5 de '
  'agosto de 2023, el agresor propinó golpes en el brazo a la víctima con los puños, le causó injurias verbales '
  '("gorda asquerosa, sucia y perra") y le impidió la salida de la habitación. La defensa solicitó en la audiencia '
  'concentrada la nulidad del trámite bajo el argumento de que debió investigarse un concurso heterogéneo de delitos '
  '(lesiones personales, injuria y constreñimiento ilegal), lo que exigiría agotar previamente la conciliación como '
  'requisito de procedibilidad respecto de la injuria o las lesiones querellables.\nProblema jurídico procesal: ¿Cómo '
  'opera la regla de subsidiariedad y concurso cuando una misma secuencia de agresiones físicas y verbales en el hogar '
  'configura el delito de VIF? ¿Cuál es la vía procedimental aplicable?',
  'Caso de estudio tres.\n\nExpediente simulado número tres.\n\nRadicado: ' + RAD % 'ce' + '.\n\n' + VIF229 + '\n\n'
  + SUJETOS + '\n\nTema central: Análisis de concursos de delitos, subsidiariedad típica del maltrato y vía '
  'procedimental.\n\nSíntesis fáctica del caso: Durante el episodio del cinco de agosto de dos mil veintitrés, el '
  'agresor propinó golpes en el brazo a la víctima con los puños, le causó injurias verbales, gorda asquerosa, sucia '
  'y perra, y le impidió la salida de la habitación. La defensa solicitó en la audiencia concentrada la nulidad del '
  'trámite, bajo el argumento de que debió investigarse un concurso heterogéneo de delitos, lesiones personales, '
  'injuria y constreñimiento ilegal, lo que exigiría agotar previamente la conciliación como requisito de '
  'procedibilidad respecto de la injuria o las lesiones querellables.\n\nProblema jurídico procesal: ¿Cómo opera la '
  'regla de subsidiariedad y concurso cuando una misma secuencia de agresiones físicas y verbales en el hogar '
  'configura el delito de violencia intrafamiliar? ¿Cuál es la vía procedimental aplicable?'),

 ('U1-C3-B', 'Hombre',
  'Resolución técnica y fundamento jurisprudencial (SP014-2026): El delito de VIF (art. 229 del CP) es un tipo penal '
  'subsidiario (siempre que la conducta no constituya delito sancionado con pena mayor) y de consumación instantánea, '
  'lo que significa que un único episodio agresivo que menoscabe la armonía y unidad familiar absorbe las distintas '
  'manifestaciones de violencia física y moral.\nPor tanto, no es jurídicamente procedente fragmentar el episodio en '
  'varios delitos menores (como injuria o lesiones sin incapacidad). Al estar subsumidas todas las agresiones en el '
  'catálogo de VIF (numeral 2 del art. 534 del CPP), la actuación se rige de forma obligatoria y exclusiva por el '
  'procedimiento penal especial abreviado (Ley 1826 de 2017). Por tratarse de un delito investigable de oficio no '
  'requiere conciliación preprocesal como requisito de procedibilidad, siendo infundada la nulidad planteada por la '
  'defensa.',
  'Resolución técnica y fundamento jurisprudencial, ' + SP + ': El delito de violencia intrafamiliar, artículo '
  'doscientos veintinueve del Código Penal, es un tipo penal subsidiario, siempre que la conducta no constituya delito '
  'sancionado con pena mayor, y de consumación instantánea, lo que significa que un único episodio agresivo que '
  'menoscabe la armonía y unidad familiar absorbe las distintas manifestaciones de violencia física y moral.\n\n'
  'Por tanto, no es jurídicamente procedente fragmentar el episodio en varios delitos menores, como injuria o '
  'lesiones sin incapacidad. Al estar subsumidas todas las agresiones en el catálogo de violencia intrafamiliar, '
  'numeral dos del artículo quinientos treinta y cuatro del Código de Procedimiento Penal, la actuación se rige de '
  'forma obligatoria y exclusiva por el procedimiento penal especial abreviado, Ley mil ochocientos veintiséis de dos '
  'mil diecisiete. Por tratarse de un delito investigable de oficio, no requiere conciliación preprocesal como '
  'requisito de procedibilidad, siendo infundada la nulidad planteada por la defensa.'),

 ('U1-C4-A', 'Mujer',
  'Caso de estudio 4\nExpediente simulado N° 4\nRadicado: FGN-S1-2024-69806-D\nDelito: VIF (art. 229 del CP)\n'
  'Sujetos: José A.C. (acusado) / María T.C. (víctima)\nTema central: Adecuación típica del maltrato psicológico, '
  'libertad probatoria e irrelevancia de huellas físicas externas.\nSíntesis fáctica del caso: En el examen de clínica '
  'forense realizado a la víctima el 6 de agosto de 2023 (un día después de los hechos), el perito de Medicina Legal '
  'no encontró huellas externas de lesión reciente ni fijó incapacidad médico-legal. Con posterioridad, el 20 de '
  'diciembre de 2023, la valoración psiquiátrica concluyó que la víctima presentaba "sintomatología ansiosa con '
  'elementos postraumáticos". La defensa argumentó que existía atipicidad al no haber lesiones físicas visibles y '
  'alegó falta de prueba sobre el nexo causal del daño psicológico.\nProblema jurídico procesal: ¿La configuración '
  'del delito de VIF requiere la demostración de lesiones físicas visibles mediante dictamen pericial o incapacidad '
  'médica? ¿Cómo se demuestra el maltrato psicológico?',
  'Caso de estudio cuatro.\n\nExpediente simulado número cuatro.\n\nRadicado: ' + RAD % 'de' + '.\n\n' + VIF229
  + '\n\n' + SUJETOS + '\n\nTema central: Adecuación típica del maltrato psicológico, libertad probatoria e '
  'irrelevancia de huellas físicas externas.\n\nSíntesis fáctica del caso: En el examen de clínica forense realizado '
  'a la víctima el seis de agosto de dos mil veintitrés, un día después de los hechos, el perito de Medicina Legal no '
  'encontró huellas externas de lesión reciente ni fijó incapacidad médico legal. Con posterioridad, el veinte de '
  'diciembre de dos mil veintitrés, la valoración psiquiátrica concluyó que la víctima presentaba sintomatología '
  'ansiosa con elementos postraumáticos. La defensa argumentó que existía atipicidad al no haber lesiones físicas '
  'visibles, y alegó falta de prueba sobre el nexo causal del daño psicológico.\n\nProblema jurídico procesal: ¿La '
  'configuración del delito de violencia intrafamiliar requiere la demostración de lesiones físicas visibles mediante '
  'dictamen pericial o incapacidad médica? ¿Cómo se demuestra el maltrato psicológico?'),

 ('U1-C4-B', 'Hombre',
  'Resolución técnica y fundamento jurisprudencial (SP014-2026): La Corte Suprema de Justicia aclaró en la Sentencia '
  'SP014-2026 que no se exige un resultado de incapacidad médico-legal ni la presencia de huellas corporales visibles '
  'para la consumación del delito de VIF. En el sistema acusatorio rige el principio de libertad probatoria (art. 373 '
  'del CPP), de modo que la agresión física y el maltrato psicológico se pueden acreditar válidamente a través de la '
  'prueba testimonial de la víctima.\nEl maltrato psicológico consiste en toda conducta intencional que causa dolor '
  'emocional, terror, menosprecio, angustia o intimidación. El relato de la víctima sobre los insultos, la '
  'imposibilidad de salir y el terror de permanecer encerrada, relato respaldado por el testimonio de familiares que '
  'presenciaron su estado de choque y corroborado con la valoración psiquiátrica, otorga certeza sobre la existencia '
  'del maltrato psicológico autónomo.',
  'Resolución técnica y fundamento jurisprudencial, ' + SP + ': La Corte Suprema de Justicia aclaró en la Sentencia '
  + SP + ' que no se exige un resultado de incapacidad médico legal ni la presencia de huellas corporales visibles '
  'para la consumación del delito de violencia intrafamiliar. En el sistema acusatorio rige el principio de libertad '
  'probatoria, artículo trescientos setenta y tres del Código de Procedimiento Penal, de modo que la agresión física '
  'y el maltrato psicológico se pueden acreditar válidamente a través de la prueba testimonial de la víctima.\n\n'
  'El maltrato psicológico consiste en toda conducta intencional que causa dolor emocional, terror, menosprecio, '
  'angustia o intimidación. El relato de la víctima sobre los insultos, la imposibilidad de salir y el terror de '
  'permanecer encerrada, relato respaldado por el testimonio de familiares que presenciaron su estado de choque y '
  'corroborado con la valoración psiquiátrica, otorga certeza sobre la existencia del maltrato psicológico autónomo.'),

 ('U1-C5-A', 'Mujer',
  'Caso de estudio 5\nExpediente simulado N° 5\nRadicado: FGN-S1-2024-69806-E\nDelito: VIF (art 229 del CP)\n'
  'Sujetos: José A.C. (acusado) / María T.C. (víctima)\nTema central: Concepto del ingrediente normativo "núcleo '
  'familiar" y duración de la convivencia.\nSíntesis fáctica del caso: José A.C. Y María T.C. convivieron bajo el '
  'mismo techo en un inmueble del barrio Prado Alto durante un período de cinco meses. Durante el juicio oral, la '
  'defensa argumentó que la conducta era atípica por ausencia del elemento normativo "núcleo familiar" y alegó que una '
  'convivencia tan corta solo constituía un "noviazgo informal" sin vocación de permanencia ni unidad marital '
  'consolidada.\nProblema jurídico procesal: ¿Exige el artículo 229 del CP un tiempo mínimo de convivencia o la '
  'consolidación de una unión marital de hecho formal para dar por configurado el elemento normativo "núcleo '
  'familiar"?',
  'Caso de estudio cinco.\n\nExpediente simulado número cinco.\n\nRadicado: ' + RAD % 'e' + '.\n\n' + VIF229 + '\n\n'
  + SUJETOS + '\n\nTema central: Concepto del ingrediente normativo núcleo familiar y duración de la convivencia.\n\n'
  'Síntesis fáctica del caso: José A. C. y María T. C. convivieron bajo el mismo techo en un inmueble del barrio Prado '
  'Alto durante un período de cinco meses. Durante el juicio oral, la defensa argumentó que la conducta era atípica '
  'por ausencia del elemento normativo núcleo familiar, y alegó que una convivencia tan corta solo constituía un '
  'noviazgo informal, sin vocación de permanencia ni unidad marital consolidada.\n\nProblema jurídico procesal: '
  '¿Exige el artículo doscientos veintinueve del Código Penal un tiempo mínimo de convivencia, o la consolidación de '
  'una unión marital de hecho formal, para dar por configurado el elemento normativo núcleo familiar?'),

 ('U1-C5-B', 'Hombre',
  'Resolución técnica y fundamento Jurisprudencial (SP014-2026): La Sala de Casación Penal desestimó la tesis '
  'defensiva y precisó que el artículo 229 del CP no fija un límite temporal mínimo de convivencia ni exige '
  'formalidades jurídicas para que se entienda configurado el núcleo familiar.\nEl bien jurídico protegido es la '
  'coexistencia pacífica, la armonía, la honra y la dignidad del núcleo familiar. Factores objetivos como compartir el '
  'mismo techo, sostener relaciones íntimas habituales y adelantar un proyecto de vida común configuran materialmente '
  'el núcleo familiar bajo la condición de compañeros permanentes. En consecuencia, la brevedad de la convivencia (así '
  'sea de pocos meses) no impide la estructuración del delito ni resta protección penal a la víctima.\nNo se exige la '
  'consolidación formal de una unión marital de hecho para estructurar el elemento normativo. Los factores objetivos '
  'como cohabitar bajo el mismo techo, relaciones íntimas habituales y un proyecto de vida común configuran el bien '
  'jurídico de la armonía familia.',
  'Resolución técnica y fundamento jurisprudencial, ' + SP + ': La Sala de Casación Penal desestimó la tesis '
  'defensiva y precisó que el artículo doscientos veintinueve del Código Penal no fija un límite temporal mínimo de '
  'convivencia ni exige formalidades jurídicas para que se entienda configurado el núcleo familiar.\n\nEl bien '
  'jurídico protegido es la coexistencia pacífica, la armonía, la honra y la dignidad del núcleo familiar. Factores '
  'objetivos como compartir el mismo techo, sostener relaciones íntimas habituales y adelantar un proyecto de vida '
  'común configuran materialmente el núcleo familiar bajo la condición de compañeros permanentes. En consecuencia, la '
  'brevedad de la convivencia, así sea de pocos meses, no impide la estructuración del delito ni resta protección '
  'penal a la víctima.\n\nNo se exige la consolidación formal de una unión marital de hecho para estructurar el '
  'elemento normativo. Los factores objetivos como cohabitar bajo el mismo techo, relaciones íntimas habituales y un '
  'proyecto de vida común configuran el bien jurídico de la armonía familiar.'),

 ('U2-C1-A', 'Mujer',
  'Estudio reverso de caso 1: escrito de acusación flagrancia y nulidad\nHechos: El 15 de agosto de 2023, en el '
  'barrio Industrial de la ciudad de Cali, el supervisor de zona Jorge Eliécer Benavides sorprendió a Mario Alberto '
  'Gómez Parra (contratista activo de la distribuidora) y a Pedro Antonio Morales Rincón (extransportador) realizando '
  'el transbordo clandestino de 45 botellas con etiquetas de la marca protegida Kombucha Valle desde un vehículo '
  'particular (Placa KTH412) hacia el camión repartidor oficial de la compañía (Placa WXN445).\nAl inspeccionar los '
  'envases, el supervisor constató que etiquetas y las tapas no correspondían a los estándares originales de la '
  'fábrica. Asimismo, el supervisor venía haciendo seguimiento a la zona de distribución a cargo de Mario Alberto, '
  'debido a una caída atípica e injustificada en las ventas durante los meses anteriores. Sobre el hallazgo grabó un '
  'video de las botellas con su celular.\nLa investigación se adelantó sin captura, se tomaron entrevistas al personal '
  'de seguridad y recopilándose informes técnicos e investigaciones internas de la empresa en 2023. El escrito de '
  'acusación se radicó bajo las reglas del procedimiento penal especial abreviado (Ley 1826 de 2017) el 4 de febrero '
  'de 2026.',
  'Estudio reverso de caso uno: escrito de acusación, flagrancia y nulidad.\n\nHechos: El quince de agosto de dos mil '
  'veintitrés, en el barrio Industrial de la ciudad de Cali, el supervisor de zona Jorge Eliécer Benavides sorprendió '
  'a Mario Alberto Gómez Parra, contratista activo de la distribuidora, y a Pedro Antonio Morales Rincón, '
  'extransportador, realizando el transbordo clandestino de cuarenta y cinco botellas con etiquetas de la marca '
  'protegida Kombucha Valle, desde un vehículo particular, placa ka, te, hache, cuatro, uno, dos, hacia el camión '
  'repartidor oficial de la compañía, placa doble ve, equis, ene, cuatro, cuatro, cinco.\n\nAl inspeccionar los '
  'envases, el supervisor constató que las etiquetas y las tapas no correspondían a los estándares originales de la '
  'fábrica. Asimismo, el supervisor venía haciendo seguimiento a la zona de distribución a cargo de Mario Alberto, '
  'debido a una caída atípica e injustificada en las ventas durante los meses anteriores. Sobre el hallazgo grabó un '
  'video de las botellas con su celular.\n\nLa investigación se adelantó sin captura, se tomaron entrevistas al '
  'personal de seguridad y recopilándose informes técnicos e investigaciones internas de la empresa en dos mil '
  'veintitrés. El escrito de acusación se radicó bajo las reglas del procedimiento penal especial abreviado, Ley mil '
  'ochocientos veintiséis de dos mil diecisiete, el cuatro de febrero de dos mil veintiséis.'),

 ('U2-C2-A', 'Mujer',
  'Estudio reverso de caso 2: audiencia de prueba anticipada\nDurante los últimos tres años, en vivienda conyugal '
  'ubicada en Medellín, Carlos Eduardo Restrepo Múnera ejerció actos continuados de maltrato físico, verbal y '
  'psicológico contra su cónyuge, María Elena Gutiérrez Ríos. El episodio más grave ocurrió el 10 de enero de 2026, '
  'cuando el procesado agredió físicamente a María Elena, lo que le causó una incapacidad médico-legal definitiva de '
  '25 días con deformidad física transitoria, y le manifestó expresamente: "si me denuncia o habla en un juzgado, la '
  'mato a usted y a su mamá".\nTras la denuncia interpuesta por un tercero y la emisión de una medida de protección de '
  'urgencia, el procesado ha iniciado una campaña de intimidación: ha enviado a familiares y terceros armados al lugar '
  'donde María Elena se encuentra refugiada y le ha exigido la retractación inmediata.\nAnte el riesgo inminente para '
  'la vida de la víctima y la necesidad de trasladarla de manera inmediata a un refugio confidencial en el exterior a '
  'través de la red de protección a víctimas de VBG (Ley 1257 de 2008), la Fiscalía determina que no es viable esperar '
  'hasta la audiencia de juicio oral para recibir su testimonio. Por ello, la Fiscalía acude ante el juez de control '
  'de garantías para solicitar la práctica anticipada de su testimonio.',
  'Estudio reverso de caso dos: audiencia de prueba anticipada.\n\nDurante los últimos tres años, en vivienda conyugal '
  'ubicada en Medellín, Carlos Eduardo Restrepo Múnera ejerció actos continuados de maltrato físico, verbal y '
  'psicológico contra su cónyuge, María Elena Gutiérrez Ríos. El episodio más grave ocurrió el diez de enero de dos '
  'mil veintiséis, cuando el procesado agredió físicamente a María Elena, lo que le causó una incapacidad médico legal '
  'definitiva de veinticinco días con deformidad física transitoria, y le manifestó expresamente: si me denuncia o '
  'habla en un juzgado, la mato a usted y a su mamá.\n\nTras la denuncia interpuesta por un tercero y la emisión de '
  'una medida de protección de urgencia, el procesado ha iniciado una campaña de intimidación: ha enviado a familiares '
  'y terceros armados al lugar donde María Elena se encuentra refugiada, y le ha exigido la retractación inmediata.'
  '\n\nAnte el riesgo inminente para la vida de la víctima y la necesidad de trasladarla de manera inmediata a un '
  'refugio confidencial en el exterior, a través de la red de protección a víctimas de violencia basada en género, Ley '
  'mil doscientos cincuenta y siete de dos mil ocho, la Fiscalía determina que no es viable esperar hasta la audiencia '
  'de juicio oral para recibir su testimonio. Por ello, la Fiscalía acude ante el juez de control de garantías para '
  'solicitar la práctica anticipada de su testimonio.'),

 ('U3-C1-A', 'Mujer',
  'Caso de estudio 1: Viabilidad en delitos contra el patrimonio económico\nPremisa fáctica: En un caso de estafa en '
  'masa donde resultaron afectadas quince personas naturales por una falsa promesa de inversión en criptoactivos en el '
  'año 2024, el apoderado judicial de las víctimas presenta una solicitud formal de conversión de la acción penal de '
  'pública a privada y adjunta poder especial debidamente autenticado suscrito por trece de los afectados.',
  'Caso de estudio uno: Viabilidad en delitos contra el patrimonio económico.\n\nPremisa fáctica: En un caso de estafa '
  'en masa donde resultaron afectadas quince personas naturales por una falsa promesa de inversión en criptoactivos en '
  'el año dos mil veinticuatro, el apoderado judicial de las víctimas presenta una solicitud formal de conversión de la '
  'acción penal de pública a privada, y adjunta poder especial debidamente autenticado, suscrito por trece de los '
  'afectados.'),

 ('U3-C2-A', 'Mujer',
  'Caso de estudio 2: Improcedencia por concurso o inimputabilidad\nPremisa fáctica: Una víctima de hurto agravado '
  'cometido en un establecimiento comercial por un ciudadano extranjero solicita la conversión de la acción penal a '
  'privada. En el curso de la indagación inicial de la Fiscalía, se recopilan dictámenes psiquiátricos del Instituto '
  'Nacional de Medicina Legal que sugieren fuertemente que el indiciado padece de esquizofrenia paranoide grave al '
  'momento de la comisión de los hechos fácticos.',
  'Caso de estudio dos: Improcedencia por concurso o inimputabilidad.\n\nPremisa fáctica: Una víctima de hurto '
  'agravado cometido en un establecimiento comercial por un ciudadano extranjero solicita la conversión de la acción '
  'penal a privada. En el curso de la indagación inicial de la Fiscalía, se recopilan dictámenes psiquiátricos del '
  'Instituto Nacional de Medicina Legal que sugieren fuertemente que el indiciado padece de esquizofrenia paranoide '
  'grave al momento de la comisión de los hechos fácticos.'),

 ('U3-C3-A', 'Mujer',
  'Caso de estudio 3: Reversión por desviación de poder o incomparecencia del defensor\nPremisa fáctica: Una vez '
  'concedida la conversión en un delito de inasistencia alimentaria, el apoderado de la víctima investido como '
  'acusador privado radica citaciones periódicas de carácter intimidatorio en el domicilio laboral del indiciado, '
  'amenaza de forma directa a los testigos de la defensa con iniciar denuncias de falso testimonio si comparecen en el '
  'juicio oral y oculta sistemáticamente un recibo de pago por concepto de aportes de alimentos que el indiciado le '
  'remitió previo al traslado de acusación.\nProblema jurídico: ¿Proceden la reversión de la conversión de la acción '
  'penal pública a privada, y la compulsa de copias penales y disciplinarias contra el acusador privado, cuando en un '
  'trámite por inasistencia alimentaria este incurre en deslealtad procesal?',
  'Caso de estudio tres: Reversión por desviación de poder o incomparecencia del defensor.\n\nPremisa fáctica: Una vez '
  'concedida la conversión en un delito de inasistencia alimentaria, el apoderado de la víctima, investido como '
  'acusador privado, radica citaciones periódicas de carácter intimidatorio en el domicilio laboral del indiciado, '
  'amenaza de forma directa a los testigos de la defensa con iniciar denuncias de falso testimonio si comparecen en el '
  'juicio oral, y oculta sistemáticamente un recibo de pago por concepto de aportes de alimentos que el indiciado le '
  'remitió previo al traslado de acusación.\n\nProblema jurídico: ¿Proceden la reversión de la conversión de la acción '
  'penal pública a privada, y la compulsa de copias penales y disciplinarias contra el acusador privado, cuando en un '
  'trámite por inasistencia alimentaria este incurre en deslealtad procesal?'),

 ('U3-C3-B', 'Hombre',
  'Solución y justificación: El fiscal delegado de conocimiento, de oficio o a solicitud de la defensa, decretará la '
  'reversión inmediata de la acción penal de privada a pública mediante orden debidamente motivada.\nFundamento '
  'jurídico: El acusador privado está plenamente obligado a actuar bajo el principio de objetividad y lealtad '
  'procesal. El ocultamiento deliberado de elementos de prueba favorables a la contraparte y las amenazas a testigos '
  'constituyen una evidente desviación de poder y una vulneración grave del debido proceso. La Fiscalía asumirá '
  'inmediatamente el control y dirección del caso en el estado en que se encuentre, y compulsará de forma concomitante '
  'copias penales para investigar la posible comisión de fraude procesal o prevaricato y copias disciplinarias ante el '
  'Consejo Seccional de la Judicatura.',
  'Solución y justificación: El fiscal delegado de conocimiento, de oficio o a solicitud de la defensa, decretará la '
  'reversión inmediata de la acción penal de privada a pública, mediante orden debidamente motivada.\n\nFundamento '
  'jurídico: El acusador privado está plenamente obligado a actuar bajo el principio de objetividad y lealtad '
  'procesal. El ocultamiento deliberado de elementos de prueba favorables a la contraparte y las amenazas a testigos '
  'constituyen una evidente desviación de poder y una vulneración grave del debido proceso. La Fiscalía asumirá '
  'inmediatamente el control y dirección del caso en el estado en que se encuentre, y compulsará de forma concomitante '
  'copias penales para investigar la posible comisión de fraude procesal o prevaricato, y copias disciplinarias ante '
  'el Consejo Seccional de la Judicatura.'),

 ('U4-C1-A', 'Mujer',
  'Caso de análisis 1\nUn fiscal local de Bogotá recibe una noticia criminal por un delito de inasistencia alimentaria '
  '(art. 233 del CP), cometido presuntamente por un ciudadano de 35 años de edad contra su hijo menor de edad. El '
  'fiscal decide, con el fin de agilizar el proceso preprocesal y resolver el conflicto de forma expedita, fijar fecha '
  'para diligencia de conciliación utilizando el formato FGN-MP02-F-10. Sin embargo, la defensa del indiciado presenta '
  'una solicitud de recusación contra el fiscal y posterior solicitud de nulidad en la audiencia concentrada con el '
  'argumento de que que la inasistencia alimentaria no es un delito querellable y que exigir conciliación obligatoria '
  'vulnera el debido proceso.',
  'Caso de análisis uno.\n\nUn fiscal local de Bogotá recibe una noticia criminal por un delito de inasistencia '
  'alimentaria, artículo doscientos treinta y tres del Código Penal, cometido presuntamente por un ciudadano de treinta '
  'y cinco años de edad contra su hijo menor de edad. El fiscal decide, con el fin de agilizar el proceso preprocesal y '
  'resolver el conflicto de forma expedita, fijar fecha para diligencia de conciliación utilizando el formato efe, ge, '
  'ene, eme, pe, cero dos, efe, diez. Sin embargo, la defensa del indiciado presenta una solicitud de recusación contra '
  'el fiscal y posterior solicitud de nulidad en la audiencia concentrada, con el argumento de que la inasistencia '
  'alimentaria no es un delito querellable y que exigir conciliación obligatoria vulnera el debido proceso.'),

 ('U4-C2-A', 'Mujer',
  'Caso de análisis 2\nEn el curso de un proceso por lesiones personales culposas en accidente de tránsito, las partes '
  'comparecen voluntariamente y solicitan de común acuerdo la aplicación del trámite de mediación penal. El fiscal de '
  'conocimiento realiza el correspondiente trámite remitiendo el conflicto a un mediador del distrito judicial mediante '
  'el formato FGN-MP02-F-132. Durante la sesión de mediación, el indiciado acepta expresamente que conducía con exceso '
  'de velocidad, manifiesta un profundo arrepentimiento y se ofrece a pagar la suma de diez millones de pesos como '
  'indemnización total. Tras varias sesiones, no se llega a un acuerdo y se suscribe el formato FGN-MP02-F-133, '
  'certificando que no hubo acuerdo. Durante el juicio oral, el fiscal pretende introducir el audio de la sesión de '
  'mediación para demostrar que el acusado admitió el exceso de velocidad y la autoría de la agresión. El defensor '
  'formula oposición solicitando la regla de exclusión.',
  'Caso de análisis dos.\n\nEn el curso de un proceso por lesiones personales culposas en accidente de tránsito, las '
  'partes comparecen voluntariamente y solicitan de común acuerdo la aplicación del trámite de mediación penal. El '
  'fiscal de conocimiento realiza el correspondiente trámite remitiendo el conflicto a un mediador del distrito '
  'judicial mediante el formato efe, ge, ene, eme, pe, cero dos, efe, ciento treinta y dos. Durante la sesión de '
  'mediación, el indiciado acepta expresamente que conducía con exceso de velocidad, manifiesta un profundo '
  'arrepentimiento y se ofrece a pagar la suma de diez millones de pesos como indemnización total. Tras varias '
  'sesiones, no se llega a un acuerdo y se suscribe el formato efe, ge, ene, eme, pe, cero dos, efe, ciento treinta y '
  'tres, certificando que no hubo acuerdo. Durante el juicio oral, el fiscal pretende introducir el audio de la sesión '
  'de mediación para demostrar que el acusado admitió el exceso de velocidad y la autoría de la agresión. El defensor '
  'formula oposición solicitando la regla de exclusión.'),

 ('U4-C3-A', 'Mujer',
  'Caso de análisis 3\nUna ciudadana de 28 años presenta denuncia por el delito de VIF sistemática en concurso con '
  'lesiones personales dolosas simples contra su cónyuge. La víctima asiste al despacho del fiscal en compañía de un '
  'abogado del consultorio jurídico de una universidad manifestando que voluntariamente desea desistir de la denuncia, '
  'además solicita formalizar un acuerdo de mediación y posterior archivo de la carpeta penal, alegando que su esposo '
  'ya se disculpó y prometió asistir a terapia de pareja y que ella depende económicamente de él.',
  'Caso de análisis tres.\n\nUna ciudadana de veintiocho años presenta denuncia por el delito de violencia '
  'intrafamiliar sistemática, en concurso con lesiones personales dolosas simples, contra su cónyuge. La víctima asiste '
  'al despacho del fiscal en compañía de un abogado del consultorio jurídico de una universidad, manifestando que '
  'voluntariamente desea desistir de la denuncia; además, solicita formalizar un acuerdo de mediación y posterior '
  'archivo de la carpeta penal, alegando que su esposo ya se disculpó y prometió asistir a terapia de pareja, y que '
  'ella depende económicamente de él.'),
]


def palabras(t):
    return len(t.split())


if __name__ == '__main__':
    tot = 0
    for c, v, t, s in TRAMOS:
        n = palabras(t)
        tot += n
        print('%-8s %-6s %4d palabras  ~%4.0f s a 140 p/min' % (c, v, n, n / 140 * 60))
    print('total %d palabras, %d tramos' % (tot, len(TRAMOS)))
