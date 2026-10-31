# -*- coding: utf-8 -*-
r"""Guion del curso «Derechos humanos aplicados a la función judicial»
(PRIORIDAD 2) · cinco videos.

LAS FUENTES (Drive, carpeta compartida por JP Soluciones Digitales)
    https://drive.google.com/drive/folders/1rRgeOZ2lEWinTMDhOrk7Y3w8zG_58ALC
    «Guión animado 1 (Unidad 1)»  1Xh-74ikYMaSmH_MS3aJWSfye_QtVCTWNtdrvT-ym_wI
    «Guión Animado 2 (Unidad 2)»  1qY_LuQ-TacvdjtR02eScCc6aFkyRQx7E3pQeZ2Q_4Bs
    «Guión animado 3 (Unidad 3)»  1GvGp-8rzhQnvgY8xn21WucXNXKww_Zfzv7HdaXmYLec
    «Guión animado 4 (Unidad 4)»  1jsfGwEkwR2Rsvnqj8N_btg5P1I9xezVZVkIT8sCfdI0
    «Guión animado 5 (Unidad 5)»  143EoBika5MUsoJLpV7ZsG2J6ot6r5u4xTEB7WqOZu8I

    Un solo expediente atraviesa el curso: las amenazas contra Carmen Elisa
    Rojas, locutora de la emisora comunitaria y vocera de la mesa de
    víctimas. U1 la denuncia (día cero) · U2 la defensa invoca un tratado ·
    U3 semana ocho, dos versiones de la misma entrevista · U4 semana diez,
    la audiencia de medida de aseguramiento · U5 semana doce, el cierre y el
    giro.

SIN PREGUNTAS NI RESPUESTAS (Sebastián, 31 oct: «en ninguno de los videos
puede ir las secciones de preguntas o respuestas»)
    Sale todo lo que es de la interacción H5P: las instrucciones al
    participante, las pausas con su enunciado, sus opciones y la
    retroalimentación, la «pantalla de texto» de la U4 («si usted fuera la
    fiscal, ¿qué pediría hoy…»), los botones, y en la U2 la «instrucción al
    participante», las retroalimentaciones A y B (son la respuesta a cada
    camino) y el «enlace directo a la plantilla». Queda guardado en
    `FUERA_DEL_VIDEO`.
    SÍ van, porque son la voz en off del guion y no una pregunta: «Deténgase
    aquí… registre su primera decisión» (U1), «márquelo cuando lo escuche»
    (U3), «Anote en su bitácora…» (U3) y la instrucción de la decisión
    integral (U5). Son el lugar donde la agencia pone la pausa del H5P.

DOS TEXTOS POR BLOQUE, COMO EN TODA LA SERIE
    `texto`  el documento VERBATIM, para el cartón. Comillas «».
    `tts`    lo mismo dicho para ElevenLabs: números en letras, siglas
             leídas, paréntesis a comas. Solo cuando hace falta.

ERRATAS DEL DOCUMENTO (la regla de la casa: «corregir lo obvio»)
    U3  la cuarta marca está escrita «R3» dos veces: la segunda es «R4».
    U5  «Los Elementos de prueba» -> «Los elementos de prueba».
    U3  el título del documento repite el de la U1 («Llega la noticia»): el
        video se titula con su propia voz en off, «Dos versiones de la misma
        entrevista».

LAS VOCES (ElevenLabs, cuenta de Sebastián, eleven_multilingual_v2)
    Voz en off       Carlos      (el narrador de la serie)
    Carmen Elisa     Elisa María (colombiana, joven)
    Andrés Peña      Leo         (colombiano, joven)
    Entrevistador 1  Johan       (colombiano, conversacional)
    Sandra Ibáñez    Milena      (latinoamericana, media)
    Marina Quintero  Pilar       (colombiana, media)
    Julián Mora      Alejandro   (colombiano, joven)
    Abogada Salgado  Milena      (no comparte video con Sandra hablando: en
                                  la U4 Sandra está en la mesa y no habla)
    Juez             Horacio     (colombiano, medio, seguro)
    Los bloques cuyo id termina en `_tel` se oyen por teléfono (altavoz):
    `armar_dh` les pasa un filtro de banda telefónica.
    Un bloque de voz `SILENCIO` es un silencio de los segundos que dice su
    `tts`: el epílogo sin diálogo de la U4 («La otra silla»).
"""

PREFIJO = 'DH_'

MOVIMIENTO = 1.0
CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.8
CAPITULO = 1.6
DIALOGO = 0.45

DRIVE = 'https://drive.google.com/drive/folders/1rRgeOZ2lEWinTMDhOrk7Y3w8zG_58ALC'
DRIVE_VIDEOS = None          # se llena al crear la carpeta «Videos»

ANTE = 'Derechos humanos aplicados a la función judicial'

# clave -> (carpeta, voz narradora, antetitulo, titulo del carton)
TEMAS = {
 'U1': ('UNIDAD 1 - Llega la noticia', 'Carlos',
        'Unidad 1', 'Llega la noticia'),
 'U2': ('UNIDAD 2 - La defensa invoca un tratado', 'Carlos',
        'Unidad 2', 'La defensa invoca un tratado'),
 'U3': ('UNIDAD 3 - Dos versiones de la misma entrevista', 'Carlos',
        'Unidad 3', 'Dos versiones de la misma entrevista'),
 'U4': ('UNIDAD 4 - La medida de aseguramiento', 'Carlos',
        'Unidad 4', 'La medida de aseguramiento'),
 'U5': ('UNIDAD 5 - La decision integral y el giro', 'Carlos',
        'Unidad 5', 'La decisión integral y el giro'),
}
VIDEOS = ['U1', 'U2', 'U3', 'U4', 'U5']

ENTREGA = {
 'U1': 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 1 LLEGA LA NOTICIA',
 'U2': 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 2 LA DEFENSA INVOCA UN TRATADO',
 'U3': 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 3 DOS VERSIONES DE LA MISMA ENTREVISTA',
 'U4': 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 4 LA MEDIDA DE ASEGURAMIENTO',
 'U5': 'PRIO 2 - DERECHOS HUMANOS - UNIDAD 5 LA DECISION INTEGRAL Y EL GIRO',
}

# --------------------------------------------------------------- bloques
# (id, voz, texto_verbatim, tts_o_None, pausa_antes)
BLOQUES = {}

BLOQUES['U1'] = [
 ('a01_noticia_criminal', 'Carlos',
  'En la Fiscalía General de la Nación, todo empieza con una noticia '
  'criminal. Lo que ocurra con ella en las primeras horas puede proteger '
  'derechos o ponerlos en riesgo. Esta es la historia de una decisión: la '
  'suya.',
  None, 0.0),
 ('a02_vengo_a_denunciar', 'Carmen',
  'Buenos días. Vengo a poner una denuncia. Trabajo en la emisora '
  'comunitaria y soy vocera de la mesa de víctimas del municipio. Desde '
  'hace dos semanas me están amenazando.',
  None, CAPITULO),
 ('a03_con_calma', 'Andres',
  'Cuénteme qué ha pasado, con toda la calma.', None, DIALOGO),
 ('a04_las_cuotas', 'Carmen',
  'Hace quince días hablé al aire de las cuotas que están cobrando a los '
  'comerciantes del mercado. Desde entonces: este panfleto que apareció '
  'bajo la puerta de la emisora...',
  None, DIALOGO),
 ('a05_la_moto', 'Carmen',
  '...dos llamadas de número desconocido diciéndome que me calle, y el '
  'martes una moto me siguió desde la emisora hasta mi casa. Dos cuadras, '
  'despacio, detrás mío.',
  'dos llamadas de número desconocido diciéndome que me calle, y el '
  'martes una moto me siguió desde la emisora hasta mi casa. Dos cuadras, '
  'despacio, detrás mío.',
  1.0),
 ('a06_los_numeros', 'Andres',
  '¿Conserva los números de las llamadas y la hora exacta?', None, CAPITULO),
 ('a07_una_vecina', 'Carmen',
  'Sí, aquí están. Y una vecina vio la moto; está dispuesta a contarlo.',
  None, DIALOGO),
 ('a08_vive_con_alguien', 'Andres',
  '¿Vive con alguien? ¿Ha cambiado sus rutinas? ¿Alguien más de la mesa de '
  'víctimas ha recibido amenazas?',
  None, DIALOGO),
 ('a09_mi_mama', 'Carmen',
  'Vivo con mi mamá. Y sí: a otro compañero le dejaron un papel parecido, '
  'pero él no quiere denunciar. Tiene miedo. Yo también, pero alguien tiene '
  'que hacerlo.',
  None, DIALOGO),
 ('a10_los_del_cerro', 'Carmen',
  'Una cosa más. En el pueblo todos sabemos quiénes cobran esas cuotas. Son '
  '«Los del Cerro». Eso también lo dije al aire.',
  'Una cosa más. En el pueblo todos sabemos quiénes cobran esas cuotas. Son '
  'Los del Cerro. Eso también lo dije al aire.',
  CAPITULO),
 # [Silencio. Andrés sostiene la mirada; el peso de la información es
 # visible sin subrayados musicales.]
 ('a11_detengase', 'Carlos',
  'Deténgase aquí. Usted acaba de recibir esta noticia criminal. Antes de '
  'cualquier teoría, registre su primera decisión.',
  None, 3.0),
 ('a12_bienvenido', 'Carlos',
  'Este expediente lo acompañará durante todo el curso. Cada unidad le '
  'exigirá una decisión nueva; ninguna será en abstracto. Bienvenido y '
  'bienvenida: este caso, desde hoy, también es suyo.',
  None, CIERRE + 0.8),
]

BLOQUES['U2'] = [
 ('b01_el_escrito', 'Carlos',
  'En el despacho, Julián, el asistente, entrega a la fiscal Quintero un '
  'escrito de la abogada Salgado, defensora de Wilmer Acosta, citado a '
  'interrogatorio. El escrito dice, en lo esencial:',
  None, 0.0),
 ('b02_vida_privada', 'Salgado',
  '«La obtención de los registros telefónicos de mi representado desconoció '
  'el derecho a la vida privada reconocido en el artículo 11 de la '
  'Convención Americana sobre Derechos Humanos y el artículo 17 del Pacto '
  'Internacional de Derechos Civiles y Políticos, tratados que prevalecen '
  'en el orden interno.',
  'La obtención de los registros telefónicos de mi representado desconoció '
  'el derecho a la vida privada reconocido en el artículo once de la '
  'Convención Americana sobre Derechos Humanos y el artículo diecisiete del '
  'Pacto Internacional de Derechos Civiles y Políticos, tratados que '
  'prevalecen en el orden interno.',
  NORMAL),
 ('b03_se_excluya', 'Salgado',
  'Solicito, en consecuencia, que esa información se excluya de la '
  'actuación».',
  'Solicito, en consecuencia, que esa información se excluya de la '
  'actuación.',
  0.5),
 ('b04_camino_a', 'Carlos',
  'Camino A: «Eso es derecho internacional, aquí aplicamos la ley '
  'colombiana».',
  'Camino A: Eso es derecho internacional, aquí aplicamos la ley '
  'colombiana.',
  CAPITULO),
 ('b05_desestimando', 'Carlos',
  'El despacho responde desestimando el argumento «por tratarse de normas '
  'extranjeras no aplicables». Semanas después, en audiencia, el juez de '
  'control de garantías lee la respuesta y pregunta:',
  'El despacho responde desestimando el argumento, por tratarse de normas '
  'extranjeras no aplicables. Semanas después, en audiencia, el juez de '
  'control de garantías lee la respuesta y pregunta:',
  NORMAL),
 ('b06_derecho_extranjero', 'Juez',
  '«¿La Fiscalía considera que la Convención Americana es derecho '
  'extranjero? ¿Conoce el artículo 93 de la Constitución?».',
  '¿La Fiscalía considera que la Convención Americana es derecho '
  'extranjero? ¿Conoce el artículo noventa y tres de la Constitución?',
  DIALOGO),
 ('b07_riesgo_de_exclusion', 'Carlos',
  'La evidencia queda en riesgo de exclusión y la respuesta del despacho, en '
  'el expediente.',
  None, NORMAL),
 ('b08_camino_b', 'Carlos',
  'Camino B: «Mejor retiremos esa evidencia para evitar problemas».',
  'Camino B: Mejor retiremos esa evidencia para evitar problemas.',
  CAPITULO),
 ('b09_renuncia', 'Carlos',
  'El despacho renuncia a los registros telefónicos. Sin ese soporte, la '
  'identificación preliminar de Acosta se debilita y el caso de Carmen '
  'Elisa pierde su línea de investigación más sólida.',
  None, NORMAL),
 ('b10_bastó_invocar', 'Carlos',
  'La defensa no tuvo que demostrar nada: bastó invocar un tratado para que '
  'la actuación retrocediera.',
  None, NORMAL),
 ('b11_camino_c', 'Carlos',
  'Camino C: «Hagamos el análisis de convencionalidad completo».',
  'Camino C: Hagamos el análisis de convencionalidad completo.',
  CAPITULO),
 ('b12_obliga', 'Carlos',
  '¿El tratado obliga a Colombia y qué rango tiene? (CADH y PIDCP '
  'ratificados; bloque de constitucionalidad, art. 93 CP).',
  '¿El tratado obliga a Colombia y qué rango tiene? La Convención Americana '
  'y el Pacto Internacional, ratificados; bloque de constitucionalidad, '
  'artículo noventa y tres de la Constitución.',
  NORMAL),
 ('b13_estandar', 'Carlos',
  '¿Cuál es el estándar aplicable? (la injerencia en la vida privada es '
  'legítima si es legal, necesaria y proporcional).',
  '¿Cuál es el estándar aplicable? La injerencia en la vida privada es '
  'legítima si es legal, necesaria y proporcional.',
  NORMAL),
 ('b14_lo_cumplio', 'Carlos',
  '¿El acto lo cumplió? (los registros se obtuvieron con orden y control '
  'judicial, con fin investigativo legítimo).',
  '¿El acto lo cumplió? Los registros se obtuvieron con orden y control '
  'judicial, con fin investigativo legítimo.',
  NORMAL),
 ('b15_se_motiva', 'Carlos',
  '¿Cómo se motiva la respuesta? (citando la fuente, el estándar y su '
  'aplicación a los hechos).',
  '¿Cómo se motiva la respuesta? Citando la fuente, el estándar y su '
  'aplicación a los hechos.',
  NORMAL),
 ('b16_con_estandares', 'Carlos',
  'En audiencia, el juez valora la respuesta motivada: el argumento de la '
  'defensa se resuelve con estándares, no con reflejos.',
  None, MOVIMIENTO),
 ('b17_fortalecida', 'Carlos',
  'La evidencia se mantiene y la actuación sale fortalecida: quedó '
  'demostrado que el despacho ejerce control de convencionalidad, que es '
  'tarea de cualquier autoridad pública (Gelman vs. Uruguay, 2011, párr. '
  '239).',
  'La evidencia se mantiene y la actuación sale fortalecida: quedó '
  'demostrado que el despacho ejerce control de convencionalidad, que es '
  'tarea de cualquier autoridad pública. Gelman contra Uruguay, dos mil '
  'once, párrafo doscientos treinta y nueve.',
  NORMAL),
 ('b18_ni_rechazo', 'Carlos',
  'Ni rechazo reflejo (camino A) ni retirada refleja (camino B): análisis '
  '(camino C).',
  'Ni rechazo reflejo, camino A, ni retirada refleja, camino B: análisis, '
  'camino C.',
  CIERRE),
 ('b19_el_musculo', 'Carlos',
  'Ese es el músculo que entrenará en la matriz de convencionalidad de esta '
  'unidad.',
  None, NORMAL),
]

BLOQUES['U3'] = [
 ('c01_semana_ocho', 'Carlos',
  'Semana ocho. Los nuevos hechos del expediente exigen volver a hablar con '
  'Carmen Elisa. Va a escuchar dos versiones de la misma entrevista. En la '
  'primera, algo falla cuatro veces: márquelo cuando lo escuche.',
  None, 0.0),
 # [Rótulo: «Primera versión»]
 ('c02_otra_vez_todo', 'Entrevistador',
  'Siga, siéntese. A ver... ¿usted es la de la emisora, cierto? Cuénteme '
  'otra vez todo desde el principio, que aquí no aparece nada en el '
  'sistema.',
  None, 2.4),
 ('c03_ya_lo_conte', 'Carmen',
  '¿Otra vez? Ya lo conté cuando denuncié, y la semana pasada a otro '
  'funcionario...',
  None, 1.2),
 ('c04_se_expone', 'Entrevistador',
  'Sí, pero a mí me toca oírlo de nuevo. ¿Y usted por qué sigue diciendo '
  'esas cosas al aire, sabiendo cómo es este pueblo? ¿No le parece que se '
  'expone usted misma?',
  None, DIALOGO),
 ('c05_mi_trabajo', 'Carmen',
  'Yo informo lo que le pasa a la gente. Eso es mi trabajo.', None, 1.2),
 ('c06_un_exnovio', 'Entrevistador',
  'Bueno. ¿Las llamadas esas... seguro no era un exnovio, alguien '
  'despechado? Porque aquí dice que usted vive solo con la mamá...',
  None, DIALOGO),
 ('c07_me_callara', 'Carmen',
  'No. Eran por lo del mercado. Me dijeron que me callara o...',
  None, 1.2),
 ('c08_un_momentico', 'Entrevistador',
  'Un momentico que me entró un mensaje... Listo, siga. ¿O qué?',
  None, 1.4),
 ('c09_dejelo_asi', 'Carmen',
  '...Nada. Déjelo así.', 'Nada. Déjelo así.', 2.0),
 ('c10_cuatro_marcas', 'Carlos',
  'Cuatro marcas. Uno: le pidió repetir todo desde el principio sin '
  'consultar lo ya actuado. Dos: la culpó de exponerse.',
  None, 2.6),
 ('c11_tres_cuatro', 'Carlos',
  'Tres: redujo la amenaza a un asunto pasional, desde el prejuicio y no '
  'desde los hechos. Cuatro: la interrumpió por un mensaje justo cuando iba '
  'a decir lo más difícil, y ella se cerró.',
  None, NORMAL),
 ('c12_falta_de_metodo', 'Carlos',
  'Ninguna fue crueldad: fue falta de método.', None, NORMAL),
 ('c13_con_metodo', 'Carlos',
  'Ahora vea la misma diligencia, conducida con método y con humanidad.',
  None, CAPITULO),
 # [Rótulo: «Segunda versión»]
 ('c14_gracias_por_venir', 'Sandra',
  'Carmen Elisa, gracias por venir. Antes de empezar: revisé su denuncia y '
  'las actuaciones; no necesito que repita lo que ya contó, solo voy a '
  'precisar algunos puntos nuevos. Si en algún momento quiere una pausa, la '
  'hacemos. ¿Le parece?',
  None, 2.4),
 ('c15_empezar_de_cero', 'Carmen',
  'Le agradezco. Es la primera vez que no me toca empezar de cero.',
  None, DIALOGO),
 ('c16_el_contenido', 'Sandra',
  'Sobre los mensajes de la última semana: usted mencionó que el contenido '
  'cambió. ¿Puede contarme eso?',
  None, DIALOGO),
 ('c17_dicen_cosas', 'Carmen',
  'Ya no es solo que me calle. Ahora dicen cosas...', None, DIALOGO),
 # [Sandra deja el bolígrafo y espera: tres segundos de silencio real.]
 ('c18_tomese_su_tiempo', 'Sandra', 'Tómese su tiempo.', None, 3.0),
 ('c19_por_ser_mujer', 'Carmen',
  '...por ser mujer. Cosas que no le decían a mi compañero de la mesa.',
  'por ser mujer. Cosas que no le decían a mi compañero de la mesa.',
  1.0),
 ('c20_lo_vamos_a_tomar', 'Sandra',
  'Entiendo, y lamento que esté pasando por esto. Ese dato es importante y '
  'lo vamos a tomar en serio: cambia la valoración del riesgo y las medidas '
  'que vamos a solicitar.',
  None, DIALOGO),
 ('c21_me_lo_busque', 'Carmen',
  'A veces pienso que yo misma me lo busqué, por hablar al aire.',
  None, 1.0),
 ('c22_no_se_lo_busco', 'Sandra',
  'Usted no se lo buscó. Informar es su trabajo, y es un derecho. De estas '
  'amenazas responde quien las hace, no usted.',
  None, DIALOGO),
 ('c23_que_sigue', 'Sandra',
  'También quiero que sepa qué sigue: qué vamos a hacer nosotros, qué puede '
  'esperar usted y a quién llamar si algo pasa antes.',
  None, 0.5),
 ('c24_de_metodo', 'Carlos',
  'La diferencia no fue de amabilidad: fue de método.', None, CIERRE + 0.8),
 ('c25_su_bitacora', 'Carlos',
  'Anote en su bitácora cuál de las cuatro fallas podría ocurrir hoy en su '
  'propio puesto de trabajo. En la clínica de errores verá cómo esas '
  'fallas, sostenidas en el tiempo, construyen una investigación fallida.',
  None, NORMAL),
]

BLOQUES['U4'] = [
 ('d01_semana_diez', 'Carlos',
  'Semana diez. Wilmer Acosta fue capturado en flagrancia cuando dejaba un '
  'nuevo panfleto en la emisora, con un arma de fuego sin permiso.',
  None, 0.0),
 ('d02_legalizada', 'Carlos',
  'La captura fue legalizada y se le imputaron amenazas agravadas y porte '
  'ilegal de armas. Ahora el juez escucha la solicitud de medida de '
  'aseguramiento.',
  None, NORMAL),
 ('d03_constato', 'Juez',
  'Constato la presencia del defensor: sin él no hay audiencia válida. '
  'Escucho a la Fiscalía. Le pido que presente su solicitud:',
  None, CAPITULO),
 ('d04_solicita', 'Quintero',
  'Señor juez, la Fiscalía solicita imponer a Wilmer Acosta medida de '
  'aseguramiento privativa de la libertad en establecimiento carcelario, '
  'por amenazas agravadas y porte ilegal de armas de fuego.',
  None, DIALOGO),
 ('d05_tres_cargas', 'Quintero',
  'La urgencia: el riesgo para la víctima está en curso. Sustento la '
  'solicitud en tres cargas.',
  None, 0.5),
 ('d06_primera_carga', 'Quintero',
  'Primera carga: la inferencia razonable de autoría. No pido certeza; pido '
  'que, con estos elementos, sea probable que el imputado es autor.',
  None, NORMAL),
 ('d07_hecho_uno', 'Quintero',
  'Hecho uno: dejó un panfleto amenazante en la emisora de la víctima; lo '
  'percibieron directamente los servidores que lo capturaron, según el '
  'informe de captura.',
  None, 0.6),
 ('d08_hecho_dos', 'Quintero',
  'Hecho dos: portaba un arma de fuego sin permiso; acta de incautación y '
  'cadena de custodia.',
  None, 0.6),
 ('d09_hecho_tres', 'Quintero',
  'Hecho tres: el panfleto coincide en diseño y texto con los que la '
  'víctima recibió desde el día cero; informe técnico de cotejo.',
  None, 0.6),
 ('d10_hecho_cuatro', 'Quintero',
  'Hecho cuatro: su teléfono registra mensajes al número desde el cual se '
  'amenazó a la víctima; informe de extracción con control judicial.',
  None, 0.6),
 ('d11_convergen', 'Quintero',
  'Cuatro hechos con fuentes independientes que convergen en una sola '
  'explicación razonable: el imputado ejecuta las amenazas contra Carmen '
  'Elisa Rojas.',
  None, 0.6),
 ('d12_segunda_carga', 'Quintero',
  'Segunda carga: los fines. No invoco la gravedad del delito: la '
  'calificación jurídica provisional no es, por sí misma, determinante. '
  'Invoco dos fines con hechos.',
  None, NORMAL),
 ('d13_peligro', 'Quintero',
  'Peligro para la víctima: fue capturado ejecutando una nueva amenaza '
  'contra la misma persona.',
  None, 0.6),
 ('d14_obstruccion', 'Quintero',
  'Obstrucción de la justicia: actúa por encargo de una estructura con '
  'presencia en el territorio y capacidad de presionar testigos.',
  None, 0.6),
 ('d15_arraigo', 'Quintero',
  'No alego riesgo de no comparecencia: el imputado tiene arraigo, y lo '
  'reconozco.',
  None, 0.6),
 ('d16_tercera_carga', 'Quintero',
  'Tercera carga: el tipo de medida. Los delitos imputados admiten la '
  'detención preventiva en establecimiento carcelario por su pena mínima, '
  'pero la ley me impone probar que las medidas no privativas son '
  'insuficientes.',
  None, NORMAL),
 ('d17_el_catalogo', 'Quintero',
  'Examiné el catálogo. La prohibición de acercarse a la víctima y las '
  'presentaciones periódicas no neutralizan a quien actúa por encargo de '
  'una estructura criminal y ya desafió la investigación en curso.',
  None, 0.6),
 ('d18_vigilancia', 'Quintero',
  'La vigilancia electrónica controla la ubicación, no la coordinación de '
  'nuevas amenazas. La detención en la residencia tampoco: el riesgo se '
  'ejecuta por teléfono y a través de terceros.',
  None, 0.6),
 ('d19_el_costo', 'Quintero',
  'Asumo el costo de lo que pido: un procesado que se presume inocente irá '
  'a un sistema que la Corte Constitucional declaró en estado de cosas '
  'inconstitucional.',
  None, NORMAL),
 ('d20_no_desproporcional', 'Quintero',
  'Frente al riesgo actual para la vida y la libertad de expresión de la '
  'víctima, la medida no es desproporcional en estricto sentido.',
  None, 0.6),
 ('d21_la_defensa', 'Salgado',
  'Señor juez, mi representado tiene arraigo, trabajo estable y familia en '
  'el municipio, y no tiene antecedentes. La Fiscalía habla de una '
  'estructura que no ha probado y pide prisión por la gravedad del delito y '
  'por la alarma del caso, no por un riesgo real.',
  None, CAPITULO),
 ('d22_menos_gravosa', 'Salgado',
  'La presunción de inocencia exige la medida menos gravosa. Si el despacho '
  'encuentra algún riesgo, la defensa propone vigilancia electrónica más '
  'prohibición de comunicarse con la víctima: cubren el mismo fin sin '
  'cárcel.',
  None, 0.6),
 ('d23_resuelvo', 'Juez',
  'Resuelvo en el orden los requisitos normativos. Primera: la inferencia '
  'razonable existe; cuatro hechos con fuente independiente convergen en la '
  'autoría y la defensa no controvirtió ninguno.',
  None, CAPITULO),
 ('d24_deciden_los_hechos', 'Juez',
  'Segunda: la calificación jurídica no decide nada por sí misma; deciden '
  'los hechos. El peligro para la víctima está acreditado por la captura '
  'ejecutando una nueva amenaza, y la llamada a su madre muestra que el '
  'riesgo se extiende a su familia.',
  None, 0.7),
 ('d25_la_obstruccion', 'Juez',
  'La obstrucción tiene soporte en los mensajes con el remitente de las '
  'amenazas. La no comparecencia no se configura, como la propia Fiscalía '
  'reconoció.',
  None, 0.6),
 ('d26_tercera', 'Juez',
  'Tercera: la detención en establecimiento carcelario es procedente por la '
  'pena mínima del tipo penal. Examiné la combinación que propone la '
  'defensa: controla dónde está el imputado y el contacto directo, pero no '
  'la coordinación por teléfono y por terceros, que está acreditada.',
  None, 0.7),
 ('d27_impongo', 'Juez',
  'Las no privativas son insuficientes. Impongo detención preventiva en '
  'establecimiento carcelario.',
  None, 0.6),
 ('d28_la_suya', 'Carlos',
  'Así termina la audiencia. Lo que esta unidad evalúa no es la decisión '
  'del juez, sino la sustentación: la suya.',
  None, CIERRE + 0.8),
 # Escena 7, «La otra silla»: sin diálogo. El texto sobre negro va en
 # cartón, sobre este silencio.
 ('d29_la_otra_silla', 'SILENCIO',
  'La persona que el juez acaba de enviar aquí se presume inocente. Si la '
  'medida era necesaria, esto era exactamente lo que la tercera carga debía '
  'justificar.',
  '13.0', CAPITULO),
]

BLOQUES['U5'] = [
 # Parte A: «El cierre»
 ('e01_estado_del_caso', 'Julian',
  'Estado del caso: imputación vigente por amenazas agravadas y porte '
  'ilegal de armas; medida de aseguramiento decidida en la semana diez; '
  'Carmen Elisa con medidas de protección; y hoy vence el término para '
  'definir la acusación.',
  None, 0.0),
 ('e02_las_piezas', 'Sandra',
  'Los elementos de prueba: testimonio de los agentes captores; el arma '
  'incautada; los mensajes del teléfono al número amenazante; y el análisis '
  'del panfleto.',
  None, DIALOGO),
 ('e03_asignaciones_tel', 'Andres',
  'Desde asignaciones: no hay noticias criminales conexas sin asignar.',
  None, DIALOGO),
 ('e04_hoy_cerramos', 'Quintero',
  'Hoy cerramos: acusación, situación de la víctima y revisión de la '
  'medida. Todo junto y todo coherente. Lo que decidamos de un lado no '
  'puede deshacer lo del otro.',
  None, DIALOGO),
 ('e05_decision_integral', 'Carlos',
  'Este es el momento de la decisión integral. Con lo visto en unidades '
  'anteriores, redacte desde su rol la actuación de cierre: qué se decide y '
  'con qué soporte; cómo queda protegida la víctima; qué pasa con la '
  'medida;',
  None, CAPITULO),
 ('e06_prueba_de_coherencia', 'Carlos',
  'con qué fuentes y estándares; y la prueba de coherencia: ninguna '
  'protección vulnera garantías, ninguna restricción desprotege.',
  None, 0.3),
 # Parte B: «El giro»
 ('e07_se_retracta', 'Julian',
  'Fiscal, llegó esto: el comerciante que declaró haber visto a Acosta '
  'dejar el panfleto de la semana ocho se retracta por escrito. Dice que '
  'pudo confundirse.',
  None, 3.2),
 ('e08_otro_mensaje_tel', 'Carmen',
  'Fiscal, me acaba de llegar otro mensaje. Es de un número distinto. Dice '
  'que lo de Acosta no cambia nada.',
  None, 1.8),
 ('e09_gracias_por_avisar', 'Quintero',
  'Carmen Elisa, gracias por avisar de inmediato. Sandra la llama en cinco '
  'minutos para activar lo que sigue.',
  None, DIALOGO),
 ('e10_reponderar', 'Quintero',
  'Reponderar no es empezar de cero. Tres preguntas. ¿Qué cambia la '
  'retractación en la solidez de la acusación?',
  None, CAPITULO),
 ('e11_la_fuente_real', 'Quintero',
  '¿Qué dice el mensaje nuevo sobre la fuente real del riesgo y sobre si la '
  'protección basta? ¿Y cambia la necesidad de la medida?',
  None, 0.5),
 ('e12_los_determinadores', 'Quintero',
  'Julián, verifique si alguien contactó al comerciante. Sandra, la nueva '
  'amenaza es noticia criminal conexa, y la línea de los determinadores se '
  'abre hoy.',
  None, 0.6),
]

# Lo que NO entra al video (es de la interacción H5P), guardado aquí por si
# la agencia lo quiere de vuelta.
FUERA_DEL_VIDEO = {
 'U1': ('Instrucciones para el participante («Vea el video sin adelantar…») '
        'y la PAUSA INTERACTIVA: «¿qué es lo primero que hace con este caso '
        'y por qué? Escríbalo en tres a cinco líneas», la comparación con '
        'las respuestas de referencia y el botón «continuar».'),
 'U2': ('La instrucción al participante («La fiscal le pide a usted… Elija '
        'el camino»), la retroalimentación A (bloque de constitucionalidad, '
        'art. 93 CP, Sentencia C-225 de 1995; «Vuelva al nodo…»), la '
        'retroalimentación B («El control de convencionalidad no es pánico '
        'convencional…»), la consigna de arrastrar las cuatro verificaciones '
        'y el enlace a la plantilla de la matriz.'),
 'U3': ('Las pausas 1 (qué se perdió en R4), 2 (qué falla evitó Sandra) y 3 '
        '(verdadero/falso sobre la amabilidad), con sus opciones y '
        'retroalimentaciones.'),
 'U4': ('La pantalla de texto «Antes de seguir: si usted fuera la fiscal, '
        '¿qué pediría hoy…?» con su botón, y las pausas 1, 2 y 3 con sus '
        'opciones y retroalimentaciones.'),
 'U5': ('Las pausas A1 (la prueba de coherencia), B1 (la retractación) y B2 '
        '(la nueva amenaza), con sus opciones y retroalimentaciones.'),
}


def bloques(clave):
    """Devuelve [(id, voz, texto_verbatim, texto_tts, pausa_antes)]."""
    return [(i, v, t, (s if s is not None else t), p)
            for i, v, t, s, p in BLOQUES[clave]]


def palabras(clave):
    return sum(len(t.split()) for _, v, t, _, _ in BLOQUES[clave] if v != 'SILENCIO')


def contexto(clave):
    return ' '.join(t for _, _, t, _, _ in BLOQUES[clave])


if __name__ == '__main__':
    tot = 0.0
    for k in VIDEOS:
        carpeta, voz, ante, titulo = TEMAS[k]
        n = palabras(k)
        seg = n / 150.0 * 60 * 1.10
        tot += seg
        print('%-3s %4d palabras %2d bloques ~%5.1f s de voz  %s'
              % (k, n, len(BLOQUES[k]), seg, carpeta))
    print('voz de los cinco: ~%.0f s' % tot)
