# -*- coding: utf-8 -*-
r"""Las piezas de Sebastián del curso «Investigación y judicialización de
delitos contra el medio ambiente y los recursos naturales» (PRIORIDAD 3).

DE DÓNDE SALE
    El PDF del curso (`6_11_2026_CURSO_DELITOS AMBIENTALES_DEFINITIVO.pdf`,
    Drive 1HOT5p71fNf2kfg93Q-NnQZMMdYRHv0Xa) reparte las notas para la
    virtualización entre el equipo con resaltados. Los que dicen «Video
    sebastián», «Sebas» o «Sebastian» son estos seis (página del PDF):

    V01  p10 (y p27)  U1 L1  Video introductorio: problemática ambiental y
                             criminalidad. Insumo: DOCUMENTO 1 - LINKS VÍDEOS.
    V02  p81 (y p93)  U3 L1  Video explicativo: Plan de priorización de la FGN.
                             Insumo: DOCUMENTO 1 - PLAN DE PRIORIZACIÓN DE LA FGN
                             (es el Direccionamiento Estratégico 2024-2028).
    V03  p87          U3 L3  Video animado/interactivo: técnicas especiales de
                             investigación (la casa, la ventana, el vuelo, el
                             Dr. Porras). Insumo: DOCUMENTO 3 - TÉCNICAS
                             ESPECIALES DE INVESTIGACIÓN.
    V04  p109         U4 L1  Ficha de virtualización: «El Río y la Fábrica:
                             Midiendo el Daño para Reparar».
    V05  p112         U4 L2  Caso práctico «Operación Raíces Profundas»
                             (virtualizar de forma animada).
    V06  p121         U4 L5  Video narrativo del caso Francisco. Insumo:
                             DOCUMENTO 1 - CASO FRANCISCO (trae libreto).

    Lo de Esteban (interactivos, mapas, infografías) y lo que dice «Esto lo
    hago yo» no es nuestro.

EL GUION ES NUESTRO en V01, V02 y V03: la nota pide el recurso y da insumos,
no texto. En V04 y V05 la narración sale del caso escrito en el PDF; en V06,
del libreto del documento. Las cifras de V01 tienen fuente pública y van
literales en el cartón (en la voz, en letras):
    - IDEAM, deforestación 2025: 119.483 ha (2024: 113.608), ~65 % en la
      Amazonía (77.805 ha). El Espectador, 31 jul 2026.
    - Gobierno nacional y UNODC, EVOA 2025: 118.410 ha con evidencias de
      explotación de oro de aluvión; 75 % ilícita; 49 % en áreas donde la
      minería no está permitida; 85,6 % de los municipios con EVOA tienen
      presencia de al menos un grupo armado. MinEnergía, 2 oct 2026.
    - Los seis motores de la deforestación y «el eslabón visible / subir por
      la cadena» son del propio curso (U2 L4 §3.1, U2 L3 c), art. 330A).
"""

PREFIJO = 'DA_'

CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.7
PARRAFO = 1.1
COMA = 0.35

DRIVE = 'https://drive.google.com/drive/folders/1l9Kyx9IbpAwYmXBGI_tLDMI1wRKzVsnn'
DOC_FUENTE = '1HOT5p71fNf2kfg93Q-NnQZMMdYRHv0Xa'
DRIVE_VIDEOS = '1ti3YDj4-u4i7lGVzo65js9TlhZWKHdTh'      # creada el 7 nov

CURSO = ('Investigación y judicialización de delitos contra el medio '
         'ambiente y los recursos naturales')
ANTE = 'Delitos contra el medio ambiente'

UNIDADES = {1: 'UNIDAD 1', 3: 'UNIDAD 3', 4: 'UNIDAD 4'}

# clave -> (tipo, unidad, carpeta, voz, antetitulo, titulo)
PIEZAS = {
 'V01': ('video', 1, 'VIDEO 01 - Problematica ambiental y criminalidad',
         'Carlos', 'Video introductorio',
         'Problemática ambiental y criminalidad'),
 'V02': ('video', 3, 'VIDEO 02 - Plan de priorizacion de la FGN',
         'Pilar', 'Video explicativo',
         'Plan de priorización de la Fiscalía General de la Nación'),
 'V03': ('video', 3, 'VIDEO 03 - Tecnicas especiales de investigacion',
         'Carlos', 'Video interactivo',
         'Técnicas especiales de investigación'),
 'V04': ('video', 4, 'VIDEO 04 - El rio y la fabrica',
         'Pilar', 'Caso', 'El río y la fábrica: midiendo el daño para reparar'),
 'V05': ('video', 4, 'VIDEO 05 - Operacion Raices Profundas',
         'Carlos', 'Caso práctico', 'Operación «Raíces Profundas»'),
 'V06': ('video', 4, 'VIDEO 06 - Caso Francisco',
         'Pilar', 'Video narrativo', 'El caso Francisco'),
}
VIDEOS = [k for k, v in PIEZAS.items() if v[0] == 'video']
IMAGENES = []

TEMAS = {k: (UNIDADES[v[1]] + '\\' + v[2], v[3], v[4], v[5])
         for k, v in PIEZAS.items()}

ENTREGA = {
 'V01': 'PRIO 3 - DELITOS AMBIENTALES - U1 - VIDEO 01 PROBLEMATICA AMBIENTAL Y CRIMINALIDAD',
 'V02': 'PRIO 3 - DELITOS AMBIENTALES - U3 - VIDEO 02 PLAN DE PRIORIZACION DE LA FGN',
 'V03': 'PRIO 3 - DELITOS AMBIENTALES - U3 - VIDEO 03 TECNICAS ESPECIALES DE INVESTIGACION',
 'V04': 'PRIO 3 - DELITOS AMBIENTALES - U4 - VIDEO 04 EL RIO Y LA FABRICA',
 'V05': 'PRIO 3 - DELITOS AMBIENTALES - U4 - VIDEO 05 OPERACION RAICES PROFUNDAS',
 'V06': 'PRIO 3 - DELITOS AMBIENTALES - U4 - VIDEO 06 CASO FRANCISCO',
}

TEXTOS = {}

# (id, voz, texto verbatim -el del cartón-, texto tts o None, pausa antes)
BLOQUES = {}

BLOQUES['V01'] = [
 ('d01_techo', 'Carlos',
  'Desde el aire, la selva colombiana parece intacta. Pero bajo ese techo '
  'verde, y a lo largo de sus ríos, avanza un daño que no siempre se ve '
  'desde arriba.',
  None, 0.0),
 ('d02_draga', 'Carlos',
  'En el río, una draga remueve el lecho de día y de noche. El oro se separa '
  'con mercurio, y el metal tóxico vuelve al agua, viaja aguas abajo, entra '
  'en los peces y llega a la mesa de las comunidades ribereñas.',
  None, PARRAFO),
 ('d03_aluvion', 'Carlos',
  'Según el Gobierno nacional y Naciones Unidas, en 2025 Colombia tenía '
  '118.410 hectáreas con evidencias de explotación de oro de aluvión. Tres '
  'de cada cuatro eran ilícitas.',
  'Según el Gobierno nacional y Naciones Unidas, en dos mil veinticinco '
  'Colombia tenía ciento dieciocho mil cuatrocientas diez hectáreas con '
  'evidencias de explotación de oro de aluvión. Tres de cada cuatro eran '
  'ilícitas.',
  NORMAL),
 ('d04_fosas', 'Carlos',
  'En tierra firme, las retroexcavadoras abren el suelo y lo dejan convertido '
  'en pozos de agua estancada y montañas de arena, donde antes había bosque.',
  None, PARRAFO),
 ('d05_bosque', 'Carlos',
  'Lejos de los ríos, el bosque se tala, se quema y se convierte en potrero. '
  'Según el IDEAM, en 2025 el país perdió 119.483 hectáreas de bosque '
  'natural, casi dos de cada tres en la Amazonía.',
  'Lejos de los ríos, el bosque se tala, se quema y se convierte en potrero. '
  'Según el Ideam, en dos mil veinticinco el país perdió ciento diecinueve '
  'mil cuatrocientas ochenta y tres hectáreas de bosque natural, casi dos de '
  'cada tres en la Amazonía.',
  PARRAFO),
 ('d06_motores', 'Carlos',
  'Detrás de esa pérdida hay motores concretos: el acaparamiento de tierras, '
  'la ganadería extensiva, los cultivos de uso ilícito, la apertura de vías '
  'ilegales, la explotación ilícita de minerales y el aprovechamiento ilegal '
  'de madera.',
  None, NORMAL),
 ('d07_dinero', 'Carlos',
  'Nada de esto ocurre por azar. La maquinaria, el combustible y el mercurio '
  'mueven dinero, y donde se mueve dinero ilícito aparece quien lo controla.',
  None, PARRAFO),
 ('d08_grupos', 'Carlos',
  'En muchos territorios, grupos armados organizados regulan estas '
  'economías: imponen reglas, cobran por dejar trabajar y controlan los ríos '
  'y las trochas. Más de ocho de cada diez municipios con explotación de oro '
  'de aluvión tienen presencia de al menos uno.',
  None, NORMAL),
 ('d09_lavado', 'Carlos',
  'El oro se vende como si fuera legal; la tierra arrasada se llena de ganado '
  'y se negocia como finca. Las ganancias se mezclan con negocios lícitos a '
  'través de testaferros y empresas fachada, y regresan convertidas en más '
  'máquinas y más control.',
  None, PARRAFO),
 ('d10_intervencion', 'Carlos',
  'Cuando las autoridades intervienen una draga o inmovilizan una '
  'retroexcavadora, el golpe es real. Pero si la investigación se queda en '
  'la máquina, el negocio sigue intacto.',
  None, PARRAFO),
 ('d11_infracciones', 'Carlos',
  'Por eso, la deforestación y la explotación ilícita de minerales ya no '
  'pueden verse como simples infracciones administrativas. Son fuentes de '
  'financiación de estructuras criminales.',
  None, PARRAFO),
 ('d12_cadena', 'Carlos',
  'Quien opera la draga o empuña la motosierra es solo el eslabón visible. '
  'La investigación penal tiene que subir por la cadena: hasta quien '
  'promueve, financia, dirige y se beneficia del daño.',
  None, PARRAFO),
 ('d13_curso', 'Carlos',
  'Ese es el recorrido que propone este curso.',
  None, PARRAFO),
]


# V02 (7 nov): guion propio desde el Direccionamiento Estratégico 2024-2028 de
# la FGN (primer pilar, tres niveles, los dos enfoques transversales: textos
# del documento) y la lección U3 L1 del curso (programa metodológico, trabajo
# en equipo, nulidades y exclusión). Lo disciplinario: el artículo 6 de la
# Constitución, sin más derecho que ese.
BLOQUES['V02'] = [
 ('e01_proposito', 'Pilar',
  'La Fiscalía General de la Nación no puede investigar todos los hechos al '
  'mismo tiempo ni con la misma intensidad. Por eso, su Direccionamiento '
  'Estratégico 2024-2028 parte de una decisión: priorizar.',
  'La Fiscalía General de la Nación no puede investigar todos los hechos al '
  'mismo tiempo ni con la misma intensidad. Por eso, su Direccionamiento '
  'Estratégico dos mil veinticuatro a dos mil veintiocho parte de una '
  'decisión: priorizar.',
  0.0),
 ('e02_pilar', 'Pilar',
  'El primer pilar de ese direccionamiento es priorizar las investigaciones '
  'con enfoque territorial: cada región identifica los fenómenos criminales '
  'que más la afectan y les da un orden para investigarlos y judicializarlos.',
  None, PARRAFO),
 ('e03_niveles', 'Pilar',
  'La priorización se construye en tres niveles que trabajan articulados: el '
  'local, en cada Dirección Seccional; el regional, que reúne varias '
  'seccionales y direcciones especializadas; y el nacional, para los '
  'fenómenos de impacto en todo el país.',
  None, NORMAL),
 ('e04_ambiente', 'Pilar',
  'En muchos territorios, esos fenómenos son ambientales. La deforestación, '
  'la explotación ilícita de minerales y el tráfico de madera no son hechos '
  'aislados: tienen patrones, rutas y financiadores.',
  None, PARRAFO),
 ('e05_enfoques', 'Pilar',
  'Por eso, los planes de priorización incorporan dos enfoques transversales: '
  'comprender la criminalidad en su relación con la delincuencia organizada, '
  'y afectar su componente financiero, buscando los capitales ilícitos y las '
  'economías con apariencia de legalidad.',
  None, NORMAL),
 ('e06_programa', 'Pilar',
  'Priorizar exige método. El fiscal dirige la investigación y aprueba el '
  'programa metodológico: hipótesis claras, tareas, responsables, plazos y '
  'objetivos probatorios. Planear, en lugar de improvisar.',
  None, PARRAFO),
 ('e07_equipo', 'Pilar',
  'Y exige equipo: fiscales, investigadores de campo, analistas financieros, '
  'peritos y autoridades ambientales trabajando sobre el mismo caso.',
  None, NORMAL),
 ('e08_disciplinario', 'Pilar',
  'Dirigir la investigación es una función pública, y quien la ejerce '
  'responde por ella. La Constitución dice que los servidores públicos son '
  'responsables por infringir la Constitución y las leyes, y también por '
  'omisión o extralimitación en el ejercicio de sus funciones.',
  None, PARRAFO),
 ('e09_disciplinario_b', 'Pilar',
  'Una investigación descuidada no solo pone en riesgo el caso: puede dar '
  'lugar a una investigación disciplinaria contra quien la dirigió.',
  None, NORMAL),
 ('e10_consecuencias', 'Pilar',
  'Las consecuencias de investigar mal son concretas: evidencia excluida por '
  'haberse obtenido sin respetar los derechos fundamentales, cadenas de '
  'custodia rotas, nulidades e hipótesis que no se sostienen en el juicio '
  'oral.',
  None, PARRAFO),
 ('e11_dano', 'Pilar',
  'Y en materia ambiental hay una consecuencia más: mientras el proceso '
  'fracasa, el daño continúa. El río sigue contaminado, el bosque sigue '
  'cayendo, y la estructura que lo financia sigue intacta.',
  None, NORMAL),
 ('e12_cierre', 'Pilar',
  'Priorizar bien, planear con rigor e investigar con debida diligencia es la '
  'manera de que la acción penal llegue a tiempo.',
  None, PARRAFO),
]

# V03 (7 nov): guion propio desde el DOCUMENTO 3 (Ley 906 de 2004, arts. 233,
# 235, 236, 239-244). La nota pide un recorrido: la casa, la ventana que se
# abre, el vuelo, cada técnica como un enlace, y al final la figura del Dr.
# Porras que da paso a su video. En video lineal cada técnica es un capítulo
# con su enlace dibujado (mg_da), para que virtualización lo vuelva clic.
BLOQUES['V03'] = [
 ('g01_casa', 'Carlos',
  'Para investigar a una organización que destruye el ambiente no basta con '
  'lo que se ve desde afuera. La Ley 906 de 2004 le da a la Fiscalía '
  'herramientas especiales para ver más allá.',
  'Para investigar a una organización que destruye el ambiente no basta con '
  'lo que se ve desde afuera. La Ley novecientos seis de dos mil cuatro le da '
  'a la Fiscalía herramientas especiales para ver más allá.',
  0.0),
 ('g02_control', 'Carlos',
  'Como interfieren con derechos fundamentales, como la intimidad y el '
  'secreto de las comunicaciones, todas están sometidas al control de un juez '
  'de control de garantías, antes o inmediatamente después de su ejecución.',
  None, NORMAL),
 ('g03_ventana', 'Carlos',
  'Abramos la ventana y recorramos el territorio.',
  None, PARRAFO),
 ('g04_personas', 'Carlos',
  'La vigilancia y seguimiento de personas observa y registra los '
  'movimientos, las actividades y las rutinas del indiciado, de forma directa '
  'o con cámaras, GPS o drones.',
  'La vigilancia y seguimiento de personas observa y registra los '
  'movimientos, las actividades y las rutinas del indiciado, de forma directa '
  'o con cámaras, ge pe ese o drones.',
  PARRAFO),
 ('g05_cosas', 'Carlos',
  'La vigilancia de cosas monitorea los inmuebles, vehículos, naves o '
  'aeronaves que se sospecha que se usan para planear delitos, ocultar '
  'evidencia o almacenar lo que producen.',
  None, PARRAFO),
 ('g06_analisis', 'Carlos',
  'El análisis e infiltración de organización criminal permite perfilar al '
  'grupo y comprender su estructura, su jerarquía, su forma de operar y sus '
  'conexiones.',
  None, PARRAFO),
 ('g07_encubierto', 'Carlos',
  'Con la actuación de agentes encubiertos, un funcionario de policía judicial '
  'oculta su identidad y se infiltra en el entorno del sospechoso. Puede '
  'documentar y participar, pero nunca provocar el delito: en Colombia, el '
  'agente provocador está prohibido.',
  None, PARRAFO),
 ('g08_entrega', 'Carlos',
  'La entrega vigilada deja que una carga ilícita siga su camino bajo '
  'vigilancia permanente, para identificar a toda la red: desde quien la '
  'produce hasta quien la recibe y la financia.',
  None, PARRAFO),
 ('g09_correspondencia', 'Carlos',
  'La retención de correspondencia permite interceptar envíos, cartas o '
  'paquetes remitidos por el indiciado o dirigidos a él.',
  None, PARRAFO),
 ('g10_interceptacion', 'Carlos',
  'La interceptación de comunicaciones permite escuchar, grabar y analizar sus '
  'llamadas, y debe someterse a control de legalidad ante un juez dentro de '
  'las 24 horas siguientes.',
  'La interceptación de comunicaciones permite escuchar, grabar y analizar sus '
  'llamadas, y debe someterse a control de legalidad ante un juez dentro de '
  'las veinticuatro horas siguientes.',
  PARRAFO),
 ('g11_internet', 'Carlos',
  'La recuperación de información dejada al navegar por internet rastrea su '
  'huella digital: historiales, correos, direcciones IP y registros de '
  'actividad.',
  'La recuperación de información dejada al navegar por internet rastrea su '
  'huella digital: historiales, correos, direcciones i pe y registros de '
  'actividad.',
  PARRAFO),
 ('g12_bases', 'Carlos',
  'Y la búsqueda selectiva en bases de datos cruza información confidencial '
  'en registros públicos o privados, como los financieros o comerciales. Esta '
  'técnica exige siempre la autorización previa del juez.',
  None, PARRAFO),
 ('g13_exclusion', 'Carlos',
  'Una regla las cubre a todas: la evidencia obtenida sin motivos fundados, '
  'por fuera de los plazos o sin control judicial es nula de pleno derecho y '
  'no puede usarse en el juicio.',
  None, PARRAFO),
 ('g14_porras', 'Carlos',
  'Cómo se aplican estas técnicas en un caso real lo cuenta quien lo ha '
  'hecho. Escuchemos la experiencia del doctor Jairo Porras.',
  None, PARRAFO),
]

# V04 (7 nov): la narración es la ficha del caso del PDF (U4 L1, p. 109),
# casi literal; el cierre, las preguntas de la valoración del daño (p. 110).
BLOQUES['V04'] = [
 ('h01_empresa', 'Pilar',
  'Una empresa agrícola dedicada a la producción a gran escala es investigada '
  'por la Fiscalía tras ser sorprendida desviando sus aguas residuales, sin '
  'tratamiento previo, directamente hacia un río local.',
  None, 0.0),
 ('h02_pasivo', 'Pilar',
  'La empresa se niega a reparar el río. Su defensa argumenta la existencia '
  'de un pasivo ambiental: demuestra que el río ya estaba altamente '
  'contaminado desde hace diez años, por los relaves de una antigua mina de '
  'oro abandonada río arriba.',
  None, PARRAFO),
 ('h03_lesion', 'Pilar',
  'El problema jurídico es preciso. Según la jurisprudencia de la Corte '
  'Suprema, el daño a los recursos naturales es un delito de lesión.',
  'El problema jurídico es preciso. Según la jurisprudencia de la Corte '
  'Suprema de Justicia, el daño a los recursos naturales es un delito de '
  'lesión.',
  PARRAFO),
 ('h04_limites', 'Pilar',
  'La Fiscalía no puede imputar responsabilidad penal basándose únicamente en '
  'la violación de la norma administrativa, desviar el agua sin permiso, ni '
  'obligar a la empresa a limpiar la contaminación histórica de la mina.',
  None, NORMAL),
 ('h05_peritaje', 'Pilar',
  'La prueba clave es un peritaje: un dictamen técnico de la autoridad '
  'ambiental que establece una medición matemática.',
  None, PARRAFO),
 ('h06_medicion', 'Pilar',
  'El estudio prueba que, exactamente a partir del tubo de desagüe de la '
  'empresa, el nivel de oxígeno del agua disminuyó un 30 % adicional, y que '
  'desaparecieron dos especies de peces que aún sobrevivían a la '
  'contaminación minera.',
  'El estudio prueba que, exactamente a partir del tubo de desagüe de la '
  'empresa, el nivel de oxígeno del agua disminuyó un treinta por ciento '
  'adicional, y que desaparecieron dos especies de peces que aún sobrevivían '
  'a la contaminación minera.',
  NORMAL),
 ('h07_aislar', 'Pilar',
  'Con un daño medible, cuantificable y verificable, la Fiscalía logra aislar '
  'la responsabilidad de la empresa del pasivo ambiental histórico.',
  None, PARRAFO),
 ('h08_preacuerdo', 'Pilar',
  'Se suspende la etapa de juicio oral a cambio de un plan de reparación '
  'estrictamente proporcional al daño causado.',
  None, PARRAFO),
 ('h09_plan', 'Pilar',
  'Primero, la construcción inmediata de una planta de tratamiento de aguas '
  'residuales en la fábrica. Segundo, un programa técnico de repoblamiento '
  'exclusivo para las dos especies de peces afectadas, bajo la supervisión de '
  'la autoridad ambiental.',
  None, NORMAL),
 ('h10_medir', 'Pilar',
  'Para reparar, primero hay que medir: qué se afectó, cuál era su estado '
  'previo, qué alteración se produjo y cuál es su vínculo causal con la '
  'conducta investigada.',
  None, PARRAFO),
]

# V05 (7 nov): el caso práctico del PDF (U4 L2, pp. 112-113), casi literal,
# con las cuatro preguntas orientadoras como columna.
BLOQUES['V05'] = [
 ('k01_empresa', 'Carlos',
  'Una empresa fachada, vinculada a una red de criminalidad organizada, '
  'ingresó maquinaria pesada al territorio del Resguardo Indígena Río Sagrado '
  'para extraer oro.',
  None, 0.0),
 ('k02_dano', 'Carlos',
  'La actividad contaminó con mercurio las fuentes hídricas y destruyó zonas '
  'de bosque donde la comunidad recolectaba plantas medicinales.',
  None, NORMAL),
 ('k03_oportunidad', 'Carlos',
  'La Fiscalía interviene, y los procesados buscan acogerse a un principio de '
  'oportunidad reparando el daño.',
  None, PARRAFO),
 ('k04_cabildo', 'Carlos',
  'Para construir el plan de reparación, la Fiscalía y la autoridad ambiental '
  'no pueden decidir solas: deben coordinarse con el Cabildo Gobernador, la '
  'autoridad indígena, a partir de cuatro preguntas.',
  None, PARRAFO),
 ('k05_quienes', 'Carlos',
  'Primera: ¿quiénes fueron afectados? Las 120 familias indígenas del '
  'resguardo, que dependen del río para su consumo de agua y su pesca.',
  'Primera: ¿quiénes fueron afectados? Las ciento veinte familias indígenas '
  'del resguardo, que dependen del río para su consumo de agua y su pesca.',
  PARRAFO),
 ('k06_sabedores', 'Carlos',
  'Y los médicos tradicionales, los sabedores o jaibanás, que perdieron el '
  'acceso a un área del bosque considerada sagrada para sus rituales de '
  'sanación.',
  None, NORMAL),
 ('k07_como', 'Carlos',
  'Segunda: ¿cómo afectó el daño su territorio y su forma de vida? El daño no '
  'es solo ecológico o económico; es un daño a su cosmovisión.',
  None, PARRAFO),
 ('k08_ninos', 'Carlos',
  'El río contaminado enfermó a los niños y alteró su seguridad alimentaria. '
  'Y sin el bosque, los sabedores ya no tienen dónde enseñar a los jóvenes la '
  'botánica tradicional.',
  None, NORMAL),
 ('k09_medidas', 'Carlos',
  'Tercera: ¿qué medidas son necesarias para restaurar el daño? Aquí se unen '
  'la ciencia estatal y el saber tradicional.',
  None, PARRAFO),
 ('k10_mercurio', 'Carlos',
  'El procesado debe financiar la extracción técnica del mercurio y la '
  'estabilización de los suelos, bajo la supervisión de la Corporación '
  'Autónoma Regional.',
  None, NORMAL),
 ('k11_semillas', 'Carlos',
  'La reforestación no se hace con cualquier semilla comercial, sino con '
  'especies endémicas y con las plantas medicinales que exigen los sabedores. '
  'Y el procesado debe financiar los rituales de armonización y limpieza '
  'espiritual del territorio.',
  None, NORMAL),
 ('k12_guardia', 'Carlos',
  'Cuarta: ¿cómo participa la comunidad en la implementación y el '
  'seguimiento? La Guardia Indígena será dotada con equipos de monitoreo de '
  'agua: ellos serán los veedores directos.',
  None, PARRAFO),
 ('k13_firmas', 'Carlos',
  'Y para que el juez declare cumplido el acuerdo y se cierre el caso penal, '
  'el informe final debe llevar dos firmas: la del perito de la autoridad '
  'ambiental y el aval del Cabildo Gobernador.',
  None, NORMAL),
]

# V06 (7 nov): la narración del libreto DOCUMENTO 1 - CASO FRANCISCO, literal,
# un bloque por paso. Los títulos de los ocho pasos van en pantalla (mg_da),
# no en la voz.
BLOQUES['V06'] = [
 ('m01_noticia', 'Pilar',
  'Nuestra noticia criminal no nace de una denuncia escrita, sino de una '
  'captura en flagrancia en el corazón del Amazonas. El origen y la fuente son '
  'claros: el informe policial de vigilancia. Se sorprende a Francisco '
  'cortando un árbol, rodeado de seis tablas de madera, presumiendo su '
  'participación en la cadena de deforestación.',
  None, 0.0),
 ('m02_norma', 'Pilar',
  'El encuadre jurídico inicial es drástico pero literal: Francisco estaba '
  'afectando el recurso natural. La norma seleccionada es el aprovechamiento '
  'ilícito. Se surten las etapas formales: legalización de captura, '
  'imputación y acusación. La norma encaja con la acción física, pero... ¿es '
  'la respuesta adecuada para este actor en particular?',
  None, PARRAFO),
 ('m03_hipotesis', 'Pilar',
  'Al construir la hipótesis delictiva, la estructura se quiebra en el '
  'reproche de culpabilidad. Francisco no es el gran determinador. Es una '
  'víctima de la violencia armada, perdió a su familia, está desplazado, solo '
  'y en pobreza extrema. Actuó bajo la necesidad, contratado por un empresario '
  'maderero que opera en las sombras.',
  None, PARRAFO),
 ('m04_objeto', 'Pilar',
  'Los interrogantes cambian radicalmente. Ya no nos preguntamos solo si '
  'cortó el árbol, sino: ¿Vale la pena llevar a juicio a un eslabón '
  'vulnerable? ¿Quién es el verdadero financiador de la tala? y ¿Qué '
  'mecanismo legal repara realmente el daño causado sin destruir aún más la '
  'vida del procesado?',
  None, PARRAFO),
 ('m05_utilidad', 'Pilar',
  'La evidencia útil aquí no es solo la madera incautada. El elemento '
  'material probatorio más valioso es la caracterización de la situación '
  'vital de Francisco. Documentamos su calidad de víctima de grupos al margen '
  'de la ley, su estado de viudez, su orfandad familiar y su precariedad '
  'laboral.',
  None, PARRAFO),
 ('m06_legalidad', 'Pilar',
  'La obtención de esta información y la búsqueda de salidas se hace con '
  'estricto respeto a los derechos fundamentales. Interviene la defensa '
  'técnica de Francisco, y se suma un equipo especializado: la Fiscalía de '
  'Medio Ambiente trabajando de la mano con la Unidad de Justicia '
  'Restaurativa para garantizar un enfoque humano y legal.',
  None, PARRAFO),
 ('m07_suficiencia', 'Pilar',
  'Con las pruebas sobre la mesa, la suficiencia nos indica que un juicio '
  'tradicional es desproporcionado e inútil. La ley nos ofrece una '
  'herramienta superior: el principio de oportunidad a través de la causal '
  'séptima, abriendo la puerta a la justicia restaurativa. El objetivo ya no '
  'es castigar, sino reparar el tejido social y ambiental.',
  None, PARRAFO),
 ('m08_viabilidad', 'Pilar',
  'La viabilidad se alcanza materializando el acuerdo. Se estructuran '
  'reuniones de acercamiento. Francisco, apoyado por la Fiscalía y '
  'Corpoamazonia, asume compromisos de reparación con su entorno. El juez de '
  'control de garantías avala este acuerdo.',
  None, PARRAFO),
 ('m09_precedente', 'Pilar',
  'Los hechos jurídicamente relevantes se transforman: la historia de un '
  'delito ambiental se convierte en un precedente de justicia restaurativa, '
  'sanación y protección del Amazonas.',
  None, NORMAL),
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
