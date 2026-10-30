# -*- coding: utf-8 -*-
r"""Guion del curso «Justicia restaurativa» (PRIORIDAD 1) · seis videos.

LAS FUENTES (Drive, carpeta compartida por JP Soluciones Digitales)
    «Casos 1 y 2»  1Yvl7ORJWYWkP6eiIdQHXcYn3TzTZQ1z8LaEkmiI1SZQ
        El CASO 1 es un enlace a «Preguntas sobre Mediación. Curso JR»
        (1UIVZtzRLg-t4DMHffDhEzJOTJJo40mVb, .pptx): una diapositiva «CASO
        PLANTEADO (normatividad; exégesis)» con el caso, y tres preguntas.
        El CASO 2 «(de lesividad alta)», «Fase 1 — La historia»: nota
        metodológica, hechos, tres tablas y la acusación.
    «Unidad 1»  1qfMktq16FumRacfW-wv0IeasBxOsIXt4ivdZy6TGawI  (la carretera)
    «Unidad 2»  1Edh0CoxVfEFErGt1XrNw5z205q6UgduoEObS5QLiNfU  (Juana)
    «Unidad 3»  1hkKAjI_eN1-kLi7IqRnDTKwiZKwehfzD272sal6_kBg  (el perdón)
    «Unidad 4»  15AC_eHPdbjnKD1wNFgYzCMAB4_TLiLpSzKQ4jz72Qz0  (para qué)

SIN PREGUNTAS (Sebastián, 30 oct: «all questions segments must not be part
of the video itself … they will deploy it thru the moodle»)
    Sale todo el segmento de pregunta: el enunciado, las opciones, la
    respuesta marcada y la retroalimentación que la explica. En la Unidad 1
    eso incluye los comentarios de cada fase («Este es el punto más temprano
    de intervención…», «La prevención ya no es posible…») y el cierre que
    va dentro de la respuesta C («No todos los conflictos terminan en
    tragedia…», el rol del fiscal, conflicto y delito): dicho en el video,
    le daría la respuesta a la pregunta que Moodle hace después. En la
    Unidad 2 sale el «RESPUESTA: Falso…». Quedan guardados abajo, en
    `FUERA_DEL_VIDEO`, por si la agencia los quiere de vuelta.

DOS TEXTOS POR BLOQUE, COMO EN TODA LA SERIE
    `texto`  el documento VERBATIM, para el cartón. Comillas «».
    `tts`    lo mismo dicho para ElevenLabs: números en letras, siglas
             leídas, paréntesis a comas, nombres extranjeros escritos como
             se dicen (Van Gog, Jílman, Yung, Tiebó). Solo cuando hace falta.

LAS TABLAS DEL CASO 2
    Se leen como están: «rótulo: valor». Lo único que se agrega es lo que
    las une como frase («Situación judicial de los dos:»). Ninguna palabra
    de la tabla cambia.

ERRATAS DEL DOCUMENTO (la regla de la casa: «corregir lo obvio»)
    U2  «se enorgullecían, envanece y arrepentían» -> «envanecían».
    U3  «no tiene qué» -> «no tiene que».
    C2  «Sepulveda» -> «Sepúlveda».
    Y UNA QUE NO SE CORRIGE, porque no es ortografía sino contenido: la U2
    dice «Pierre, soldado francés, estaba frente al pelotón de fusilamiento
    ruso». En «Guerra y paz» Pierre Bezújov es ruso, civil, y la mirada es
    con el mariscal francés Davout. Va verbatim y se le avisa a Sebastián.

LAS VOCES
    C1 Pilar · C2 Carlos · U1 Pilar · U2-U4 Carlos y Juana.
    En la U2-U4 el narrador le habla a «usted, fiscal»: el fiscal es quien
    mira (la cámara). Lo que el fiscal dice entre comillas -y lo que lee en
    voz alta: Tolstói, Hillman, Thiebaut, la historia de Rubiano- va en la
    misma voz del narrador, Carlos. Juana dice SUS parlamentos, los que el
    documento escribe entre comillas, con otra voz: Elisa María, la de la
    cuenta de Sebastián (CH U1). Las acotaciones («le dice», «le pregunta»)
    las dice el narrador, pegadas al bloque vecino cuando se puede.
    «doctor(a)»: la voz del fiscal es la de Carlos, así que se dice
    «doctor»; el cartón conserva «doctor(a)».
"""

PREFIJO = 'JR_'

MOVIMIENTO = 1.0
CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.8
CAPITULO = 1.1
DIALOGO = 0.35

DRIVE = 'https://drive.google.com/drive/folders/1Bzc28eFvCSbYng8nxjhLEQ3GOxoH53Rl'
DRIVE_VIDEOS = None          # se llena al crear la carpeta «Videos»

ANTE = 'Justicia restaurativa'

# clave -> (carpeta, voz narradora, antetitulo, titulo del carton)
TEMAS = {
 'C1': ('CASO 1 - Una discusion en un sitio publico', 'Pilar',
        'Caso 1', 'Una discusión en un sitio público'),
 'C2': ('CASO 2 - Fase 1 La historia', 'Carlos',
        'Caso 2 (de lesividad alta)', 'Fase 1 — La historia'),
 'U1': ('UNIDAD 1 - El encuentro en la carretera', 'Pilar',
        'Unidad 1', 'El encuentro en la carretera'),
 'U2': ('UNIDAD 2 - La situacion reflexiva', 'Carlos',
        'Unidad 2', 'La situación reflexiva'),
 'U3': ('UNIDAD 3 - Prosigue la situacion reflexiva', 'Carlos',
        'Unidad 3', 'Prosigue la situación reflexiva'),
 'U4': ('UNIDAD 4 - Culminamos la situacion', 'Carlos',
        'Unidad 4', 'Culminamos la situación con diversas reflexiones'),
}
VIDEOS = ['C1', 'C2', 'U1', 'U2', 'U3', 'U4']

# nombre del archivo de entrega
ENTREGA = {
 'C1': 'PRIO 1 - JUSTICIA RESTAURATIVA - CASO 1 UNA DISCUSION EN UN SITIO PUBLICO',
 'C2': 'PRIO 1 - JUSTICIA RESTAURATIVA - CASO 2 FASE 1 LA HISTORIA',
 'U1': 'PRIO 1 - JUSTICIA RESTAURATIVA - UNIDAD 1 EL ENCUENTRO EN LA CARRETERA',
 'U2': 'PRIO 1 - JUSTICIA RESTAURATIVA - UNIDAD 2 LA SITUACION REFLEXIVA',
 'U3': 'PRIO 1 - JUSTICIA RESTAURATIVA - UNIDAD 3 PROSIGUE LA SITUACION REFLEXIVA',
 'U4': 'PRIO 1 - JUSTICIA RESTAURATIVA - UNIDAD 4 CULMINAMOS LA SITUACION',
}

# --------------------------------------------------------------- bloques
# (id, voz, texto_verbatim, tts_o_None, pausa_antes)
BLOQUES = {}

BLOQUES['C1'] = [
 ('c01_la_discusion', 'Pilar',
  'El 01 de enero de 2025, en un sitio público, se presenta una discusión '
  'entre Juan Rodríguez y Ana Pérez, quienes son mayores de edad.',
  'El primero de enero de dos mil veinticinco, en un sitio público, se '
  'presenta una discusión entre Juan Rodríguez y Ana Pérez, quienes son '
  'mayores de edad.',
  0.0),
 ('c02_el_hospital', 'Pilar',
  'El joven Juan se exalta, al punto, que golpea con sus manos en tres '
  'oportunidades a Ana; ella cae y es llevada al hospital más cercano, '
  'lugar en donde es atendida y recibe los cuidados necesarios para su '
  'recuperación.',
  None, CARTON),
 ('c03_le_corresponde', 'Pilar',
  'La señora Pérez pone en conocimiento la noticia criminal y, con '
  'posterioridad, le corresponde a usted este caso en su condición de '
  'fiscal local radicado/a.',
  'La señora Pérez pone en conocimiento la noticia criminal y, con '
  'posterioridad, le corresponde a usted este caso en su condición de '
  'fiscal local radicado o radicada.',
  MOVIMIENTO),
 ('c04_el_legista', 'Pilar',
  'En la tercera ocasión que la víctima asiste al médico legista, este '
  'profesional determina una incapacidad definitiva para trabajar, sin '
  'secuelas, de 65 días.',
  'En la tercera ocasión que la víctima asiste al médico legista, este '
  'profesional determina una incapacidad definitiva para trabajar, sin '
  'secuelas, de sesenta y cinco días.',
  CARTON),
 ('c05_la_mediacion', 'Pilar',
  'Al salir de la audiencia concentrada el señor Rodríguez, acompañado por '
  'su defensor de confianza o privado, le manifiestan, al fiscal, el '
  'decidido interés de acudir al mecanismo de justicia restaurativa (JR) de '
  'la mediación, en aras de buscar gestionar el conflicto, máxime porque han '
  'intentado dialogar con la víctima de manera directa, pero han sido '
  'rechazados.',
  'Al salir de la audiencia concentrada el señor Rodríguez, acompañado por '
  'su defensor de confianza o privado, le manifiestan, al fiscal, el '
  'decidido interés de acudir al mecanismo de justicia restaurativa de la '
  'mediación, en aras de buscar gestionar el conflicto, máxime porque han '
  'intentado dialogar con la víctima de manera directa, pero han sido '
  'rechazados.',
  MOVIMIENTO),
]

BLOQUES['C2'] = [
 ('n01_nota', 'Carlos',
  'Los nombres de este apartado son ficticios. Los hechos y la calificación '
  'jurídica corresponden al expediente real, tal como se conocían al '
  'momento en que la defensa radicó la solicitud de principio de '
  'oportunidad.',
  None, 0.0),
 ('n02_los_hechos', 'Carlos',
  'Los hechos. Una noche de mediados de 2026, en una de las localidades de '
  'Bogotá se presentó una riña múltiple frente a una tienda de barrio.',
  'Los hechos. Una noche de mediados de dos mil veintiséis, en una de las '
  'localidades de Bogotá se presentó una riña múltiple frente a una tienda '
  'de barrio.',
  MOVIMIENTO),
 ('n03_la_amiga', 'Carlos',
  'El señor Camilo Andrés Ferreira Buitrago se involucró en la riña junto '
  'con una amiga que lo acompañaba, cuyos familiares eran los dueños del '
  'negocio, con el fin de defenderlos.',
  None, NORMAL),
 ('n04_por_la_espalda', 'Carlos',
  'En el desarrollo de la riña, Ferreira fue agredido por la espalda con un '
  'arma cortopunzante y, al huir herido, cayó pocos metros más adelante.',
  None, CARTON),
 ('n05_de_nuevo', 'Carlos',
  'En ese momento, dos hombres que participaban en la riña, aprovechando su '
  'condición de indefensión, lo alcanzaron y lo agredieron de nuevo con '
  'arma blanca, causándole heridas que comprometieron órganos vitales y '
  'pusieron en riesgo real su vida.',
  None, NORMAL),
 ('n06_flagrancia', 'Carlos',
  'Los dos agresores fueron capturados en flagrancia. La víctima no tenía '
  'ningún conflicto previo con los dos procesados: no se conocían entre '
  'sí, y solo coincidieron con él en el desarrollo de la riña.',
  None, CARTON),
 ('n07_perfil_victima', 'Carlos',
  'Perfil de la víctima. Nombre en el caso, ficticio: Camilo Andrés '
  'Ferreira Buitrago. Edad y ocupación: 27 años, trabajador independiente. '
  'Relación con los procesados: ninguna; no se conocían antes de los '
  'hechos.',
  'Perfil de la víctima. Nombre en el caso, ficticio: Camilo Andrés '
  'Ferreira Buitrago. Edad y ocupación: veintisiete años, trabajador '
  'independiente. Relación con los procesados: ninguna; no se conocían '
  'antes de los hechos.',
  MOVIMIENTO),
 ('n08_lesiones', 'Carlos',
  'Lesiones sufridas: herida por arma cortopunzante en tórax posterior '
  'izquierdo con hemoneumotórax (requirió cirugía de urgencia) y laceración '
  'en el brazo derecho. Incapacidad médico-legal: 30 días, con carácter '
  'provisional.',
  'Lesiones sufridas: herida por arma cortopunzante en tórax posterior '
  'izquierdo con hemoneumotórax, que requirió cirugía de urgencia, y '
  'laceración en el brazo derecho. Incapacidad médico legal: treinta días, '
  'con carácter provisional.',
  CARTON),
 ('n09_delito_imputado', 'Carlos',
  'Delito imputado por estos hechos: homicidio agravado (arts. 103 y 104, '
  'num. 7, CP) en grado de tentativa (art. 27 CP).',
  'Delito imputado por estos hechos: homicidio agravado, artículos ciento '
  'tres y ciento cuatro, numeral siete, del Código Penal, en grado de '
  'tentativa, artículo veintisiete del Código Penal.',
  CARTON),
 ('n10_perfil_procesados', 'Carlos',
  'Perfil de los procesados. Procesado 1: Jairo Ortiz Cuéllar, 21 años, '
  'conductor de servicio público. Procesado 2: Jaime Rincón Sepúlveda, '
  '39 años, comerciante independiente.',
  'Perfil de los procesados. Procesado uno: Jairo Ortiz Cuéllar, veintiún '
  'años, conductor de servicio público. Procesado dos: Jaime Rincón '
  'Sepúlveda, treinta y nueve años, comerciante independiente.',
  MOVIMIENTO),
 ('n11_situacion', 'Carlos',
  'Situación judicial de los dos: capturado en flagrancia; imputado y con '
  'medida de aseguramiento intramural. Antecedentes: sin antecedentes '
  'relevantes documentados.',
  None, NORMAL),
 ('n12_condiciones', 'Carlos',
  'Condiciones restaurativas de los procesados. Capacidad económica: '
  'limitada; el pago pactado con la víctima se estructuró en cuotas. '
  'Aceptación formal de cargos: ninguno de los dos aceptó cargos.',
  None, MOVIMIENTO),
 ('n13_disposicion', 'Carlos',
  'Disposición hacia la víctima: suscribieron con la víctima un acuerdo '
  'privado de indemnización y un compromiso de no agresión futura, mediado '
  'por su firma.',
  None, CARTON),
 ('n14_acusacion', 'Carlos',
  'El delito, tal como quedó formulado en la acusación. La Fiscalía imputó '
  'inicialmente tentativa de homicidio agravado en concurso con hurto '
  'calificado y agravado, con la circunstancia de mayor punibilidad de '
  'pluralidad de agentes.',
  None, MOVIMIENTO),
 ('n15_la_pena', 'Carlos',
  'Al formular la acusación, retiró el cargo de hurto por falta de '
  'elementos probatorios, y mantuvo únicamente la acusación por tentativa '
  'de homicidio agravado, con una pena imponible, en caso de condena, de '
  'entre 200 y 450 meses de prisión.',
  'Al formular la acusación, retiró el cargo de hurto por falta de '
  'elementos probatorios, y mantuvo únicamente la acusación por tentativa '
  'de homicidio agravado, con una pena imponible, en caso de condena, de '
  'entre doscientos y cuatrocientos cincuenta meses de prisión.',
  CARTON),
 ('n16_el_acuerdo', 'Carlos',
  'Lo único que se sabía hasta ahora. Semanas después de la imputación, '
  'los dos procesados suscribieron con la víctima un acuerdo privado de '
  'indemnización integral de perjuicios, y la víctima manifestó estar «a '
  'paz y salvo» y renunciar a cualquier reclamación.',
  None, MOVIMIENTO),
 ('n17_la_solicitud', 'Carlos',
  'Con base en ese convenio, el defensor solicitó formalmente a la '
  'Fiscalía adelantar un principio de oportunidad «de acuerdo con los '
  'postulados de justicia restaurativa».',
  None, CARTON),
]

BLOQUES['U1'] = [
 ('u01_inicio', 'Pilar', 'Inicio: el encuentro en la carretera.', None, 0.0),
 ('u02_el_bloqueo', 'Pilar',
  'Un hombre adinerado, Diego, conduce su Audi por una carretera solitaria. '
  'Al intentar adelantar a un viejo automóvil, el otro conductor (Mario) '
  'lo bloquea.',
  'Un hombre adinerado, Diego, conduce su Audi por una carretera solitaria. '
  'Al intentar adelantar a un viejo automóvil, el otro conductor, Mario, '
  'lo bloquea.',
  NORMAL),
 ('u03_escalada', 'Pilar', 'Escalada: el orgullo entra en juego.', None,
  CAPITULO),
 ('u04_el_pinchazo', 'Pilar',
  'Alterado, Diego logra adelantar a Mario y lo insulta, siguiendo su '
  'camino. Más adelante, Diego sufre un pinchazo y se detiene.',
  None, NORMAL),
 ('u05_mario_aparece', 'Pilar',
  'Mario aparece… y reconoce al hombre que lo insultó. Hay ofensas mutuas.',
  'Mario aparece... y reconoce al hombre que lo insultó. Hay ofensas '
  'mutuas.',
  NORMAL),
 ('u06_confrontacion', 'Pilar', 'Confrontación directa.', None, CAPITULO),
 ('u07_se_enfrentan', 'Pilar',
  'Ambos conductores se enfrentan físicamente.', None, NORMAL),
 ('u08_explosion', 'Pilar', 'Explosión: punto sin retorno.', None,
  CAPITULO),
 ('u09_la_violencia', 'Pilar',
  'La violencia escala rápidamente: destruyen los vehículos, se golpean '
  'brutalmente, se hieren gravemente.',
  None, NORMAL),
 ('u10_atrapados', 'Pilar',
  'En un momento extremo, uno intenta matar al otro con el auto y terminan '
  'atrapados en una lucha salvaje dentro del vehículo.',
  None, NORMAL),
 ('u11_desenlace', 'Pilar', 'Desenlace: destrucción mutua.', None,
  CAPITULO),
 ('u12_calcinado', 'Pilar',
  'El auto se incendia y los dos conductores mueren dentro de él. La '
  'policía llega tras el incendio del vehículo. Encuentran el auto '
  'completamente calcinado.',
  None, NORMAL),
]

BLOQUES['U2'] = [
 ('a01_juana_se_acerca', 'Carlos',
  'Juana, prima de Alberto, víctima de tortura, se le acerca a usted, '
  'fiscal, y le dice:',
  None, 0.0),
 ('a02_impunidad', 'Juana',
  '«Juanito Lagunas me recomendó acudir a la justicia restaurativa para el '
  'caso de mi primo…, pero yo no sé…, la justicia restaurativa me suena '
  'como a impunidad…, además, ¿eso no es solo para delitos menores?»',
  'Juanito Lagunas me recomendó acudir a la justicia restaurativa para el '
  'caso de mi primo... pero yo no sé... la justicia restaurativa me suena '
  'como a impunidad... además, ¿eso no es solo para delitos menores?',
  DIALOGO),
 ('a03_tolstoi', 'Carlos',
  'Tras contestarle, usted, de repente, recuerda una frase que leyó en '
  'Guerra y Paz de Tolstói cuando Pierre, soldado francés, estaba frente al '
  'pelotón de fusilamiento ruso:',
  None, MOVIMIENTO),
 ('a04_la_mirada', 'Carlos',
  '«Se miraron mutuamente durante un minuto. Esa mirada salvó a Pierre. En '
  'ella, además de todas las condiciones de la guerra y de un juicio, '
  'entre esas dos personas se establecieron relaciones humanas.',
  'Se miraron mutuamente durante un minuto. Esa mirada salvó a Pierre. En '
  'ella, además de todas las condiciones de la guerra y de un juicio, '
  'entre esas dos personas se establecieron relaciones humanas.',
  CARTON),
 ('a05_hijos_del_planeta', 'Carlos',
  'En ese instante, ambos experimentaron una incontable cantidad de cosas '
  'e ideas: los dos eran hijos de este planeta, los dos tenían o habían '
  'tenido una madre que les quería y a la que querían, los dos hacían el '
  'bien y el mal y se enorgullecían, envanecían y arrepentían».',
  'En ese instante, ambos experimentaron una incontable cantidad de cosas '
  'e ideas: los dos eran hijos de este planeta, los dos tenían o habían '
  'tenido una madre que les quería y a la que querían, los dos hacían el '
  'bien y el mal y se enorgullecían, envanecían y arrepentían.',
  NORMAL),
 ('a06_encontrarse', 'Carlos',
  'Esa frase, usted le dice a Juana, resume la importancia de la justicia '
  'restaurativa. En la posibilidad, sobre todo, de encontrarse con el '
  'otro, sea quien sea…',
  'Esa frase, usted le dice a Juana, resume la importancia de la justicia '
  'restaurativa. En la posibilidad, sobre todo, de encontrarse con el '
  'otro, sea quien sea...',
  MOVIMIENTO),
 ('a07_dubitativa', 'Carlos',
  'Juana le agradece, pero, todavía dubitativa, pregunta:',
  None, CARTON),
 ('a08_como_aplicar', 'Juana',
  '«¿Cómo aplicar la justicia restaurativa en el proceso penal?»…',
  '¿Cómo aplicar la justicia restaurativa en el proceso penal?',
  DIALOGO),
]

BLOQUES['U3'] = [
 ('b01_su_primo', 'Carlos',
  'Juana le agradece por todas sus orientaciones sobre cómo y cuándo '
  'aplicar la justicia restaurativa en la práctica. Sin embargo, ella no '
  'deja de pensar en su primo, en los padecimientos que sufrió, en lo '
  'atroz del delito del cual fue la víctima directa y en los daños '
  'irreparables que le ocasionaron…',
  'Juana le agradece por todas sus orientaciones sobre cómo y cuándo '
  'aplicar la justicia restaurativa en la práctica. Sin embargo, ella no '
  'deja de pensar en su primo, en los padecimientos que sufrió, en lo '
  'atroz del delito del cual fue la víctima directa y en los daños '
  'irreparables que le ocasionaron...',
  0.0),
 ('b02_el_vaso', 'Carlos',
  'Juana, con un vaso de agua en una mano, le pregunta a usted, fiscal:',
  None, MOVIMIENTO),
 ('b03_el_perdon', 'Juana',
  '«¿Pero usted en verdad cree que una víctima va a terminar pidiendo '
  'perdón por lo que le hicieron? Porque es que todo pareciera muy '
  'orientado como hacia el perdón y el abrazo…»',
  '¿Pero usted en verdad cree que una víctima va a terminar pidiendo '
  'perdón por lo que le hicieron? Porque es que todo pareciera muy '
  'orientado como hacia el perdón y el abrazo...',
  DIALOGO),
 ('b04_van_gogh', 'Carlos',
  'Usted, por algún motivo, recuerda una pintura de Van Gogh.',
  'Usted, por algún motivo, recuerda una pintura de Van Gog.',
  MOVIMIENTO),
 ('b04b_pie_de_foto', 'Carlos',
  'Cansado. Vincent van Gogh. 1882. Lápiz sobre papel.',
  'Cansado. Vincent van Gog. Mil ochocientos ochenta y dos. Lápiz sobre '
  'papel.',
  CARTON),
 ('b05_rubiano', 'Carlos',
  'En paralelo, recuerda una historia escrita por el director Fabio '
  'Rubiano que usted (que tiene buena memoria) leyó en una revista '
  'cultural:',
  'En paralelo, recuerda una historia escrita por el director Fabio '
  'Rubiano que usted, que tiene buena memoria, leyó en una revista '
  'cultural:',
  MOVIMIENTO),
 ('b06_el_jardin', 'Carlos',
  'Una madre juega con su hijo en el jardín que tienen frente a su casa. '
  'Mientras lo hacen, un hombre se acerca, toma al niño por un brazo y le '
  'dice a la madre:',
  None, NORMAL),
 ('b07_debo_raptar', 'Carlos',
  '«Perdón, señora, debo raptar a su hijo. Cuando yo era niño en mi casa no '
  'teníamos jardín y mi mamá jamás jugó conmigo, jamás me llevó a un '
  'parque, no puedo soportar ver una escena que yo nunca viví.',
  'Perdón, señora, debo raptar a su hijo. Cuando yo era niño en mi casa no '
  'teníamos jardín y mi mamá jamás jugó conmigo, jamás me llevó a un '
  'parque, no puedo soportar ver una escena que yo nunca viví.',
  DIALOGO),
 ('b08_perdoneme', 'Carlos',
  'Tampoco he podido perdonar a mi mamá por no haberme dado eso que usted '
  'sí le entrega a su hijo. En ese orden, para que su hijo valore el hecho '
  'de tener una madre cariñosa, me lo llevo y, tal vez, se lo regrese en '
  'unos días. Esto puede ser brutal para usted, por eso le pido que me '
  'perdone, perdóneme».',
  'Tampoco he podido perdonar a mi mamá por no haberme dado eso que usted '
  'sí le entrega a su hijo. En ese orden, para que su hijo valore el hecho '
  'de tener una madre cariñosa, me lo llevo y, tal vez, se lo regrese en '
  'unos días. Esto puede ser brutal para usted, por eso le pido que me '
  'perdone, perdóneme.',
  NORMAL),
 ('b09_la_madre_lo_mira', 'Carlos',
  'La madre lo mira, mira el brazo del niño rodeado por la mano enorme del '
  'raptor y le dice:',
  None, NORMAL),
 ('b10_te_perdono', 'Carlos',
  '«Entiendo su situación. Dado que me aclaraste las razones por las cuales '
  'estás haciendo esto, y me diste un panorama del contexto geográfico y '
  'emocional en el que creciste, lo que acabas de hacer es comprensible, '
  'te perdono».',
  'Entiendo su situación. Dado que me aclaraste las razones por las cuales '
  'estás haciendo esto, y me diste un panorama del contexto geográfico y '
  'emocional en el que creciste, lo que acabas de hacer es comprensible, '
  'te perdono.',
  DIALOGO),
 ('b11_aliviado', 'Carlos',
  '«Gracias, señora», responde el hombre y se aleja aliviado llevándose al '
  'niño.',
  'Gracias, señora, responde el hombre y se aleja aliviado llevándose al '
  'niño.',
  NORMAL),
 ('b12_juana_se_rie', 'Carlos',
  'Juana se ríe de la historia y le dice:', None, MOVIMIENTO),
 ('b13_es_una_broma', 'Juana', '«Es una broma, ¿no?»',
  'Es una broma, ¿no?', DIALOGO),
 ('b14_no_le_cree', 'Carlos',
  'Usted, con un gesto irónico, le dice que no, que no es una broma. Juana '
  'no le cree.',
  None, DIALOGO),
 ('b15_a_la_fuerza', 'Carlos',
  'Usted le confiesa que, en efecto, se trata de una broma y procede a '
  'explicarle que, como en la historia, exigir el perdón a la fuerza sería '
  'un gesto o un actuar irresponsable.',
  None, NORMAL),
 ('b16_encontrarse', 'Carlos',
  'Lo fundamental en la justicia restaurativa es la posibilidad de '
  'encontrarse con el otro, de preguntarle, de reconocerse. Pero también, '
  'la posibilidad de encontrarse con uno mismo.',
  None, CARTON),
 ('b17_no_tiene_que', 'Carlos',
  'No hay que perdonar a quien hace el daño, quien quiera perdonar, pues lo '
  'hace… Pero si no quiere hacerlo, no tiene que. La justicia restaurativa '
  'ofrece, sobre todo, la posibilidad de reconciliarse con lo sucedido, con '
  'los recuerdos…',
  'No hay que perdonar a quien hace el daño, quien quiera perdonar, pues lo '
  'hace... Pero si no quiere hacerlo, no tiene que. La justicia restaurativa '
  'ofrece, sobre todo, la posibilidad de reconciliarse con lo sucedido, con '
  'los recuerdos...',
  NORMAL),
 ('b18_lea_esto', 'Carlos',
  '«Lea esto», le dice usted a Juana, mostrándole una frase en su celular. '
  '«La frase», usted le explica, «es de James Hillman, un psicoanalista '
  'norteamericano»:',
  'Lea esto, le dice usted a Juana, mostrándole una frase en su celular. La '
  'frase, usted le explica, es de James Jílman, un psicoanalista '
  'norteamericano:',
  MOVIMIENTO),
 ('b19_hillman_1', 'Carlos',
  'El perdón, como la humildad, es sólo un término a menos que uno haya '
  'sido totalmente humillado o totalmente agraviado. El perdón sólo tiene '
  'sentido cuando uno no puede ni olvidar ni perdonar. Y nuestros sueños '
  'no nos permiten olvidar.',
  None, CARTON),
 ('b20_hillman_2', 'Carlos',
  'Cualquiera puede olvidar un insulto insignificante, una afrenta '
  'personal. Pero si uno ha sido llevado paso a paso a una implicación en '
  'la que la sustancia era la propia confianza, ha desnudado su alma, y '
  'luego ha sido profundamente traicionado en el sentido de entregado a sus '
  'enemigos, externos o internos, el perdón adquiere un gran significado.',
  None, NORMAL),
 ('b21_hillman_3', 'Carlos',
  'Puede muy bien ser que la traición no tenga otro resultado positivo que '
  'el perdón, y que la experiencia del perdón sólo sea posible si uno ha '
  'sido traicionado.',
  None, NORMAL),
 ('b22_la_sal', 'Carlos',
  'Ese perdón es un perdón que no es un olvido, sino el recuerdo del mal '
  'transformado en un contexto más amplio o, como Jung ha dicho, la sal de '
  'la amargura transformada en la sal de la sabiduría.',
  'Ese perdón es un perdón que no es un olvido, sino el recuerdo del mal '
  'transformado en un contexto más amplio o, como Yung ha dicho, la sal de '
  'la amargura transformada en la sal de la sabiduría.',
  CARTON),
 ('b23_silencio', 'Carlos',
  'Juana termina de leer y se queda pensativa… Ambos hacen silencio…',
  'Juana termina de leer y se queda pensativa... Ambos hacen silencio...',
  CIERRE),
]

BLOQUES['U4'] = [
 ('d01_el_agua', 'Carlos',
  'Usted sigue en su oficina, Juana también. Se da cuenta de que ella ya se '
  'terminó su agua. Juana sigue pensando en su respuesta sobre el perdón… '
  'Usted le ofrece otro agua o café. Ella le agradece, pero no quiere nada.',
  'Usted sigue en su oficina, Juana también. Se da cuenta de que ella ya se '
  'terminó su agua. Juana sigue pensando en su respuesta sobre el perdón... '
  'Usted le ofrece otro agua o café. Ella le agradece, pero no quiere nada.',
  0.0),
 ('d02_aprovecha', 'Carlos',
  'Por el contrario, todavía dubitativa sobre la justicia restaurativa, '
  'aprovecha para preguntarle:',
  None, NORMAL),
 ('d03_para_que', 'Juana',
  '«¿Para qué la justicia restaurativa? Es decir»,',
  '¿Para qué la justicia restaurativa? Es decir,',
  DIALOGO),
 ('d04_le_dice', 'Carlos', 'le dice,', None, DIALOGO),
 ('d05_mi_primo', 'Juana',
  '«¿por qué le resultaría mejor a mi primo acudir a la justicia '
  'restaurativa?»',
  '¿por qué le resultaría mejor a mi primo acudir a la justicia '
  'restaurativa?',
  DIALOGO),
 ('d06_thiebaut', 'Carlos',
  'Usted, fiscal, se sirve otro café y toma un libro que tiene sobre su '
  'escritorio. El libro se titula «Daño y silencio» de Carlos Thiebaut. '
  'Usted procede a leerle un fragmento:',
  'Usted, fiscal, se sirve otro café y toma un libro que tiene sobre su '
  'escritorio. El libro se titula Daño y silencio, de Carlos Tiebó. Usted '
  'procede a leerle un fragmento:',
  MOVIMIENTO),
 ('d07_nombrarlo', 'Carlos',
  'Aprender el sufrimiento y aprender a atenderlo al concebir esa conducta, '
  'precisamente, como doliente es, en un grado cero, aprender a nombrarlo, '
  'tal vez por vez primera.',
  None, CARTON),
 ('d08_una_imagen', 'Carlos',
  'Dar una imagen, un nombre, a algo que todavía no lo tenía es, en gran '
  'medida, haber sabido fijarlo en un concepto o en un lenguaje y poder, '
  'entonces, ubicarlo en un tejido de significados que nos permitan '
  'comprenderlo como pena o como dolor; en virtud de ello, quienes están '
  'junto al doliente pueden llegar a verse concernidos por ese dolor y '
  'responder a la demanda que plantea.',
  None, NORMAL),
 ('d09_las_palabras', 'Carlos',
  'Las palabras, pues, permiten nombrar los dolores y las penas y permiten '
  'comprenderlas como daños, como aquello que debe ser atendido y, cuando '
  'posible sea, como aquello que debe ser evitado.',
  None, CARTON),
 ('d10_mas_practico', 'Carlos',
  'Juana, cansada de tantas frases, le dice que no entiende, le pide que '
  'sea más práctico.',
  None, MOVIMIENTO),
 ('d11_a_punta', 'Juana',
  '«¿Cómo es que a punta de palabras la justicia restaurativa puede ayudar '
  'a mi primo?»,',
  '¿Cómo es que a punta de palabras la justicia restaurativa puede ayudar '
  'a mi primo?',
  DIALOGO),
 ('d12_otro_fragmento', 'Carlos',
  'le indaga con insistencia. Usted, persistente, procede a leerle otro '
  'fragmento:',
  None, DIALOGO),
 ('d13_acciones', 'Carlos',
  'Pero el daño no solo reclama palabras. Demanda también acciones. '
  'Atender al reclamo de un dolor, sanarlo o paliarlo, es hacer algo en el '
  'mundo; aquello, precisamente, que las palabras han nombrado o aquello '
  'que los conceptos que empleamos nos han indicado que debe ser curado, '
  'atendido, o evitado.',
  None, CARTON),
 ('d14_su_etica', 'Carlos',
  'Requiere, por decirlo de manera concreta, transitar de la pragmática de '
  'los silencios a su ética.',
  None, NORMAL),
 ('d15_el_silencio', 'Carlos',
  'El silencio, por ejemplo, dice que en algunos casos no hay ya cura '
  'posible para un daño que se sufrió o que todavía no la hay. Fija lo '
  'irrecuperable, entonces, lo que no puede suturarse del daño sufrido '
  'pero reconoce, no obstante, que debería haber sido o que debería ser '
  'otro el curso del mundo.',
  None, NORMAL),
 ('d16_no_reiteracion', 'Carlos',
  'El silencio pone una marca que recuerda que ya no hay sutura en el daño '
  'o en la pérdida sufridos, pero a la vez impone otra marca, la de un '
  'motivo o un compromiso, la de un deseo o un imperativo de no '
  'reiteración del daño.',
  None, CARTON),
 ('d17_no_convencida', 'Carlos',
  'Juana le agradece por la lectura, pero no parece muy convencida de la '
  'ruta restaurativa.',
  None, MOVIMIENTO),
 ('d18_escarbar', 'Juana',
  '«Me parece muy fuerte someter a mi primo a todo eso. ¿Para qué cavar y '
  'cavar y escarbar en el dolor?»,',
  'Me parece muy fuerte someter a mi primo a todo eso. ¿Para qué cavar y '
  'cavar y escarbar en el dolor?',
  DIALOGO),
 ('d19_voluntariedad', 'Carlos',
  'le dice. Usted le responde que justo por eso, por lo que implica lidiar '
  'con el dolor y con lo atroz, lo fundamental en la justicia restaurativa '
  'es la voluntariedad.',
  None, DIALOGO),
 ('d20_nadie_obligado', 'Carlos',
  '«Nadie está obligado a avanzar por ese camino. Pero quien emprende ese '
  'camino tampoco está solo. De ahí la importancia de las personas '
  'mediadoras o facilitadoras. Se trata de terceros que son cuidadosos, '
  'que se encargan de llevar el proceso.',
  'Nadie está obligado a avanzar por ese camino. Pero quien emprende ese '
  'camino tampoco está solo. De ahí la importancia de las personas '
  'mediadoras o facilitadoras. Se trata de terceros que son cuidadosos, '
  'que se encargan de llevar el proceso.',
  CARTON),
 ('d21_divina_comedia', 'Carlos',
  '¿Usted leyó la Divina Comedia?», le pregunta a Juana.',
  '¿Usted leyó la Divina Comedia?, le pregunta a Juana.',
  NORMAL),
 ('d22_en_el_colegio', 'Juana',
  '«Sí, pero la leí en el colegio, hace mucho tiempo ya»,',
  'Sí, pero la leí en el colegio, hace mucho tiempo ya.',
  DIALOGO),
 ('d23_nueve_circulos', 'Carlos',
  'le responde. «Tal vez recuerde que en la primera parte, Infierno, Dante '
  'recorre los nueve círculos del Infierno, viendo las imágenes y los '
  'horrores más atroces…»',
  'le responde. Tal vez recuerde que en la primera parte, Infierno, Dante '
  'recorre los nueve círculos del Infierno, viendo las imágenes y los '
  'horrores más atroces...',
  DIALOGO),
 ('d24_aja', 'Juana', '«Ajá…»,', 'Ajá...', DIALOGO),
 ('d25_confundida', 'Carlos', 'le responde Juana, confundida.', None,
  DIALOGO),
 ('d26_que_tiene_que_ver', 'Juana',
  '«¿Eso qué tiene que ver con la justicia restaurativa?»,',
  '¿Eso qué tiene que ver con la justicia restaurativa?',
  DIALOGO),
 ('d27_virgilio', 'Carlos',
  'le pregunta. «Pues, señora Juana, Dante logra regresar del Infierno '
  'gracias a que va acompañado por Virgilio. Virgilio es su guía, lo '
  'orienta, le advierte, le muestra el camino. Eso, señora Juana, es lo que '
  'hace un mediador».',
  'le pregunta. Pues, señora Juana, Dante logra regresar del Infierno '
  'gracias a que va acompañado por Virgilio. Virgilio es su guía, lo '
  'orienta, le advierte, le muestra el camino. Eso, señora Juana, es lo que '
  'hace un mediador.',
  DIALOGO),
 ('d28_tan_poetico', 'Juana', '«Tan poético usted»,', 'Tan poético usted.',
  CARTON),
 ('d29_se_rien', 'Carlos', 'le responde Juana y ambos se ríen.', None,
  DIALOGO),
 ('d30_muchas_gracias', 'Juana',
  '«Lo comentaré con mi primo y le cuento, doctor(a). Muchas gracias»,',
  'Lo comentaré con mi primo y le cuento, doctor. Muchas gracias.',
  NORMAL),
 ('d31_se_levanta', 'Carlos', 'le dice y se levanta de su silla.', None,
  DIALOGO),
]

# Lo que NO entra al video (es del segmento de preguntas), guardado aquí por
# si la agencia lo quiere de vuelta.
FUERA_DEL_VIDEO = {
 'C1': 'Preguntas 1, 2 y 3 de la diapositiva, con sus cuatro opciones.',
 'U1': ('Las cinco preguntas con sus opciones y respuestas; los comentarios '
        '«Este es el punto más temprano de intervención. Aún es posible '
        'evitar la escalada», «El conflicto empieza a escalar…», «El '
        'conflicto ya no gira en torno al hecho inicial…», «La prevención ya '
        'no es posible…», «La intervención temprana es clave…»; y la '
        'respuesta C con «No todos los conflictos terminan en tragedia. Pero '
        'todos necesitan ser gestionados», el rol del fiscal y la distinción '
        'entre conflicto y delito.'),
 'U2': ('Las dos preguntas a Juana (impunidad; delitos menores, falso o '
        'verdadero) y el «RESPUESTA: Falso, la justicia restaurativa tiene '
        'respaldo constitucional y legal…».'),
}


def bloques(clave):
    """Devuelve [(id, voz, texto_verbatim, texto_tts, pausa_antes)]."""
    return [(i, v, t, (s if s is not None else t), p)
            for i, v, t, s, p in BLOQUES[clave]]


def palabras(clave):
    return sum(len(t.split()) for _, _, t, _, _ in BLOQUES[clave])


def contexto(clave):
    return ' '.join(t for _, _, t, _, _ in BLOQUES[clave])


if __name__ == '__main__':
    tot = 0.0
    for k in VIDEOS:
        carpeta, voz, ante, titulo = TEMAS[k]
        n = palabras(k)
        seg = n / 150.0 * 60 * 1.10
        tot += seg
        print('%-3s %4d palabras %2d bloques ~%5.1f s de voz  %-7s %s'
              % (k, n, len(BLOQUES[k]), seg, voz, carpeta))
    print('voz de los seis: ~%.0f s' % tot)
