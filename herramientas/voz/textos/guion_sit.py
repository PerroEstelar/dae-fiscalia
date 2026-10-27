# -*- coding: utf-8 -*-
r"""Guion de las situaciones del curso «Investigacion Judicial y Forense de la
Desaparicion Forzada» · documento «16 situaciones» del Drive.

QUE HAY EN EL DOCUMENTO
    Se llama «16 situaciones» pero trae ONCE, de la A a la K. Cada una tiene
    dos partes: el CONTEXTO, que es el caso, y la CONSIGNA PARA EL
    PARTICIPANTE, que son las preguntas, las opciones interactivas, la
    retroalimentacion y las plantillas descargables.

    La consigna NO va en ninguna pieza: la agencia la marco en el propio
    documento, comentario por comentario, con «No incluir esto en el video»
    (A a E) y «No incluir esto en la IMAGEN» (F a K). Va despues, en Moodle,
    y no nos corresponde.

VIDEO O IMAGEN, Y POR QUE
    La misma marca de la agencia ya lo dice, y el largo del texto lo
    confirma por su cuenta:

        A  271 palabras  video        F   80 palabras  imagen
        B  246           video        G   90           imagen
        C  237           video        H  107           imagen
        D  258           video        I   74           imagen
        E  275           video        J   60           imagen
                                      K   60           imagen

    Entre la E (275) y la H (107) no hay nada: son dos poblaciones. Un
    contexto de 250 palabras son dos minutos de voz y tres o cuatro
    momentos distintos -un trayecto, una interceptacion, una ventanilla-,
    y eso pide montaje. Uno de 60 a 100 palabras es un solo momento, y eso
    es una imagen.

DOS TEXTOS POR BLOQUE, COMO EN EL CASO INTEGRADOR
    `texto`  el documento VERBATIM. Va al carton. Las comillas rectas del
             documento pasan a angulares «», que es la tipografia de la serie;
             ninguna palabra cambia.
    `tts`    lo mismo dicho para que ElevenLabs lo pronuncie: numeros en
             letras, horas leidas como se leen en un despacho («dieciocho
             horas y dos minutos»), siglas deletreadas, parentesis y rayas
             pasados a comas. Solo existe cuando hace falta. La diferencia es
             SIEMPRE de numeral, de sigla o de puntuacion, nunca de contenido.

LAS PAUSAS SON LAS DEL CASO INTEGRADOR
    1,0 s  antes de un movimiento nuevo · 0,9 s antes de una frase que va a
    carton verbatim · 0,8 s el resto.

LAS VOCES SON LAS DEL CURSO
    Carlos y Pilar, las mismas del caso integrador, alternadas por situacion
    como alli se alternaban por capitulo.
"""

PREFIJO = 'SIT_'

MOVIMIENTO = 1.0
CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.8

DRIVE = ('https://docs.google.com/document/d/'
         '13Q4a3gys0g72GVogX78s13zod5uUyFxM0VZDsxQnFh4/edit')

# letra -> (tipo, carpeta, voz)
SITUACIONES = {
 'A': ('video',  'SITUACION A - LA ULTIMA LLAMADA',            'Carlos'),
 'B': ('video',  'SITUACION B - LA NOTA SOBRE LA CAMA',        'Pilar'),
 'C': ('video',  'SITUACION C - EL PLAZO DE 24 HORAS',         'Carlos'),
 'D': ('video',  'SITUACION D - LA CRECIENTE DE LA MIEL',      'Pilar'),
 'E': ('video',  'SITUACION E - EL CAMION HACIA EL VERGEL',    'Carlos'),
 'F': ('imagen', 'SITUACION F - EL PRIMER CONTACTO',           None),
 'G': ('imagen', 'SITUACION G - LA VOCERA',                    None),
 'H': ('imagen', 'SITUACION H - DOS MUJERES DOS IMPACTOS',     None),
 'I': ('imagen', 'SITUACION I - LA MINUTA',                    None),
 'J': ('imagen', 'SITUACION J - LAS PIEZAS DEL EXPEDIENTE',    None),
 'K': ('imagen', 'SITUACION K - EL INFORME INTEGRAL',          None),
}

VIDEOS = [k for k, v in SITUACIONES.items() if v[0] == 'video']
IMAGENES = [k for k, v in SITUACIONES.items() if v[0] == 'imagen']

# --------------------------------------------------------------- videos
# (id, voz, texto_verbatim, tts_o_None, pausa_antes)
BLOQUES = {}

BLOQUES['A'] = [
 ('a01_carlos', 'Carlos',
  'Carlos Alberto Morales, de 34 años de edad, de ocupación transportador '
  'rural y reconocido líder comunal en la región.',
  'Carlos Alberto Morales, de treinta y cuatro años de edad, de ocupación '
  'transportador rural y reconocido líder comunal en la región.',
  0.0),

 ('a02_la_salida', 'Carlos',
  'El 14 de marzo de 2026, a las 17:00 horas, Carlos Alberto salió en su '
  'camioneta Toyota Hilux (placas XYZ-789) desde el casco urbano de San José '
  'de las Peñas con destino a la vereda La Esperanza.',
  'El catorce de marzo de dos mil veintiséis, a las diecisiete horas, Carlos '
  'Alberto salió en su camioneta Toyota Hilux, placas equis, ye, zeta, siete, '
  'ocho, nueve, desde el casco urbano de San José de las Peñas con destino a '
  'la vereda La Esperanza.',
  NORMAL),

 ('a03_ultima_llamada', 'Carlos',
  'A las 18:02 horas, el dispositivo móvil de Carlos registró la última '
  'llamada saliente hacia su esposa a través de la celda «San José Urbano».',
  'A las dieciocho horas y dos minutos, el dispositivo móvil de Carlos '
  'registró la última llamada saliente hacia su esposa a través de la celda '
  'San José Urbano.',
  CARTON),

 ('a04_desconexion', 'Carlos',
  'A las 18:45 horas, la terminal captó tráfico de datos en la radio '
  'estación «SJP-Sector El Vergel» y, a las 19:12 horas, se produjo la '
  'desconexión abrupta del teléfono por pérdida de energía o extracción de '
  'batería en la zona de la Finca El Vergel.',
  'A las dieciocho horas y cuarenta y cinco minutos, la terminal captó '
  'tráfico de datos en la radio estación ese, jota, pe, Sector El Vergel y, a '
  'las diecinueve horas y doce minutos, se produjo la desconexión abrupta del '
  'teléfono por pérdida de energía o extracción de batería en la zona de la '
  'Finca El Vergel.',
  NORMAL),

 ('a05_el_mirador', 'Carlos',
  'Pasadas las 18:15 horas del 14 de marzo, en el sector del antiguo '
  'estadero El Mirador, un camión de estacas bloqueó la vía.',
  'Pasadas las dieciocho horas y quince minutos del catorce de marzo, en el '
  'sector del antiguo estadero El Mirador, un camión de estacas bloqueó la '
  'vía.',
  MOVIMIENTO),

 ('a06_cuatro_sujetos', 'Carlos',
  'Cuatro sujetos con chalecos negros sin insignias y armas largas '
  'interceptaron la camioneta, bajaron a Carlos violentamente y lo subieron '
  'a la cabina del camión.',
  None,
  NORMAL),

 ('a07_la_patrulla', 'Carlos',
  'Pobladores del sector señalaron que una patrulla policial pasó 20 '
  'minutos después por el lugar sin atender las llamadas de auxilio de la '
  'comunidad.',
  'Pobladores del sector señalaron que una patrulla policial pasó veinte '
  'minutos después por el lugar sin atender las llamadas de auxilio de la '
  'comunidad.',
  NORMAL),

 ('a08_rosa_elena', 'Carlos',
  'Al no tener noticias de su hijo durante la noche, la señora Rosa Elena '
  'Morales acudió el 15 de marzo de 2026 a las 08:30 horas a la Subestación '
  'de Policía de San José de las Peñas.',
  'Al no tener noticias de su hijo durante la noche, la señora Rosa Elena '
  'Morales acudió el quince de marzo de dos mil veintiséis a las ocho horas y '
  'treinta minutos a la Subestación de Policía de San José de las Peñas.',
  MOVIMIENTO),

 ('a09_libro_de_poblacion', 'Carlos',
  'El comandante de guardia registró en el libro de población: «Posible '
  'retiro voluntario del hogar por deudas comerciales o desavenencias '
  'personales. Se sugiere a la familia esperar 72 horas para interponer '
  'denuncia formal».',
  'El comandante de guardia registró en el libro de población: posible '
  'retiro voluntario del hogar por deudas comerciales o desavenencias '
  'personales. Se sugiere a la familia esperar setenta y dos horas para '
  'interponer denuncia formal.',
  CARTON),
]

BLOQUES['B'] = [
 ('b01_julian', 'Pilar',
  'Julián David Morales, joven de 22 años, habitante de la zona urbana de '
  'San José de las Peñas, técnico en mantenimiento de vehículos y amigo '
  'cercano de jóvenes del sector rural.',
  'Julián David Morales, joven de veintidós años, habitante de la zona '
  'urbana de San José de las Peñas, técnico en mantenimiento de vehículos y '
  'amigo cercano de jóvenes del sector rural.',
  0.0),

 ('b02_la_nota', 'Pilar',
  'El 20 de marzo de 2026, la familia de Julián encuentra una nota '
  'manuscrita sobre su cama en la que se lee: «Me voy de la ciudad a buscar '
  'trabajo por mi cuenta. No me busquen, estoy bien y fue mi decisión».',
  'El veinte de marzo de dos mil veintiséis, la familia de Julián encuentra '
  'una nota manuscrita sobre su cama en la que se lee: me voy de la ciudad a '
  'buscar trabajo por mi cuenta. No me busquen, estoy bien y fue mi '
  'decisión.',
  CARTON),

 ('b03_tres_semanas', 'Pilar',
  'Pese a la existencia de la nota, la madre y dos allegados de Julián '
  'declaran bajo reserva que, durante las tres semanas previas a su '
  'ausencia, el joven mostró severos cambios de conducta, insomnio y estados '
  'de ansiedad.',
  None,
  MOVIMIENTO),

 ('b04_la_presion', 'Pilar',
  'Allegados señalan que miembros del grupo armado ilegal Bloque Central '
  'Renacer (que opera en los corredores rurales hacia la vereda La '
  'Esperanza) lo venían presionando e intimidando para que se vinculara a '
  'la estructura criminal como mecánico de su flotilla de vehículos y '
  'apoyara labores logísticas.',
  'Allegados señalan que miembros del grupo armado ilegal Bloque Central '
  'Renacer, que opera en los corredores rurales hacia la vereda La '
  'Esperanza, lo venían presionando e intimidando para que se vinculara a '
  'la estructura criminal como mecánico de su flotilla de vehículos y '
  'apoyara labores logísticas.',
  NORMAL),

 ('b05_la_llamada', 'Pilar',
  'La víspera de su desaparición, a las 21:30 horas, un compañero de trabajo '
  'observó a Julián recibir una llamada telefónica visiblemente alterado, '
  'tras la cual afirmó: «Si no me presento mañana a las 06:00 a.m. en el '
  'cruce de El Vergel, se meten con mi familia».',
  'La víspera de su desaparición, a las veintiuna horas y treinta minutos, '
  'un compañero de trabajo observó a Julián recibir una llamada telefónica '
  'visiblemente alterado, tras la cual afirmó: si no me presento mañana a '
  'las seis de la mañana en el cruce de El Vergel, se meten con mi familia.',
  MOVIMIENTO),

 ('b06_el_funcionario', 'Pilar',
  'Al acudir a la autoridad receptora, el funcionario de atención sugiere '
  'no abrir noticia criminal sosteniendo que «hay una nota clara firmada '
  'por el joven que prueba que se fue por su propia voluntad y que es mayor '
  'de edad».',
  'Al acudir a la autoridad receptora, el funcionario de atención sugiere '
  'no abrir noticia criminal sosteniendo que hay una nota clara firmada por '
  'el joven que prueba que se fue por su propia voluntad y que es mayor de '
  'edad.',
  CARTON),
]

BLOQUES['C'] = [
 ('c01_fernando', 'Carlos',
  'Fernando Ruiz, de 45 años, reconocido comerciante de insumos agrícolas y '
  'propietario de un almacén en el casco urbano de San José de las Peñas.',
  'Fernando Ruiz, de cuarenta y cinco años, reconocido comerciante de '
  'insumos agrícolas y propietario de un almacén en el casco urbano de San '
  'José de las Peñas.',
  0.0),

 ('c02_el_trayecto', 'Carlos',
  'El 5 de abril de 2026, a las 14:30 horas, Fernando transitaba en su '
  'vehículo particular por la periferia urbana de San José de las Peñas '
  'hacia la salida a la vereda La Esperanza.',
  'El cinco de abril de dos mil veintiséis, a las catorce horas y treinta '
  'minutos, Fernando transitaba en su vehículo particular por la periferia '
  'urbana de San José de las Peñas hacia la salida a la vereda La '
  'Esperanza.',
  NORMAL),

 ('c03_interceptado', 'Carlos',
  'Es interceptado de forma violenta por dos sujetos armados que '
  'descendieron de una motocicleta, lo obligaron a bajar de su automóvil a '
  'la fuerza y lo abordaron en un camión cerrado que huyó con rumbo '
  'desconocido.',
  None,
  NORMAL),

 ('c04_la_llamada', 'Carlos',
  'Dos horas después de la interceptación (16:30 horas), la esposa de '
  'Fernando recibe una llamada telefónica de un número desconocido.',
  'Dos horas después de la interceptación, dieciséis horas y treinta '
  'minutos, la esposa de Fernando recibe una llamada telefónica de un '
  'número desconocido.',
  MOVIMIENTO),

 ('c05_la_exigencia', 'Carlos',
  'Un hombre afirma tener en su poder a Fernando, exige la suma de '
  '$150.000.000 de pesos a cambio de respetarle la vida, aporta un detalle '
  'específico de las prendas que vestía la víctima como prueba de '
  'supervivencia y fija un plazo de 24 horas para la entrega del dinero en '
  'un punto rural.',
  'Un hombre afirma tener en su poder a Fernando, exige la suma de ciento '
  'cincuenta millones de pesos a cambio de respetarle la vida, aporta un '
  'detalle específico de las prendas que vestía la víctima como prueba de '
  'supervivencia y fija un plazo de veinticuatro horas para la entrega del '
  'dinero en un punto rural.',
  CARTON),

 ('c06_los_rumores', 'Carlos',
  'En el municipio circulan rumores sobre presuntos «cobros de deudas» y '
  'extorsiones por parte de delincuentes comunes y del grupo armado ilegal '
  'Bloque Central Renacer.',
  'En el municipio circulan rumores sobre presuntos cobros de deudas y '
  'extorsiones por parte de delincuentes comunes y del grupo armado ilegal '
  'Bloque Central Renacer.',
  MOVIMIENTO),

 ('c07_el_analista', 'Carlos',
  'Al recibir el reporte, el analista de denuncias duda si ingresar la '
  'noticia criminal bajo el delito de Desaparición Forzada (Art. 165 C.P.) '
  'o remitiendo inmediatamente la carpeta al grupo GAULA por el delito de '
  'Secuestro Extorsivo (Art. 169 C.P.)',
  'Al recibir el reporte, el analista de denuncias duda si ingresar la '
  'noticia criminal bajo el delito de Desaparición Forzada, artículo ciento '
  'sesenta y cinco del Código Penal, o remitiendo inmediatamente la carpeta '
  'al grupo Gaula por el delito de Secuestro Extorsivo, artículo ciento '
  'sesenta y nueve del Código Penal.',
  CARTON),
]

BLOQUES['D'] = [
 ('d01_manuel_antonio', 'Pilar',
  'Manuel Antonio Gómez, de 58 años, agricultor tradicional y habitante de '
  'la vereda La Esperanza en el municipio de San José de las Peñas.',
  'Manuel Antonio Gómez, de cincuenta y ocho años, agricultor tradicional y '
  'habitante de la vereda La Esperanza en el municipio de San José de las '
  'Peñas.',
  0.0),

 ('d02_la_tormenta', 'Pilar',
  'El 12 de abril de 2026, durante una fuerte tormenta tropical que provocó '
  'la creciente de varios afluentes de la región, Manuel Antonio salió a '
  'las 16:00 horas desde el casco urbano hacia su finca montado en su mulo '
  'de carga.',
  'El doce de abril de dos mil veintiséis, durante una fuerte tormenta '
  'tropical que provocó la creciente de varios afluentes de la región, '
  'Manuel Antonio salió a las dieciséis horas desde el casco urbano hacia su '
  'finca montado en su mulo de carga.',
  NORMAL),

 ('d03_el_vado', 'Pilar',
  'Para llegar a su predio debía cruzar el paso del vado de la quebrada La '
  'Miel, sector caracterizado por crecientes torrenciales intempestivas.',
  None,
  NORMAL),

 ('d04_el_hallazgo', 'Pilar',
  'A las 07:00 horas del día siguiente (13 de abril), vecinos de la zona '
  'encuentran al mulo con la enjalma desprendida y húmeda al otro lado de la '
  'ribera de la quebrada, junto con el sombrero de Don Manuel atascado entre '
  'unas palizadas a 300 metros río abajo.',
  'A las siete horas del día siguiente, trece de abril, vecinos de la zona '
  'encuentran al mulo con la enjalma desprendida y húmeda al otro lado de la '
  'ribera de la quebrada, junto con el sombrero de Don Manuel atascado entre '
  'unas palizadas a trescientos metros río abajo.',
  MOVIMIENTO),

 ('d05_sin_rastro', 'Pilar',
  'Sin embargo, no se observa rastro del agricultor.',
  None,
  NORMAL),

 ('d06_conocia_el_rio', 'Pilar',
  'Aunque el evento climático sugiere un arrastre de corriente por crecida '
  'del río, la familia señala que Don Manuel conocía perfectamente el río y '
  'nunca lo cruzaba si estaba crecido.',
  None,
  MOVIMIENTO),

 ('d07_los_linderos', 'Pilar',
  'Además, dos meses atrás había tenido discrepancias de linderos con un '
  'habitante de la zona vinculado al grupo armado Bloque Central Renacer.',
  None,
  NORMAL),

 ('d08_el_reporte', 'Pilar',
  'La familia acude al puesto de policía y al despacho judicial a reportar '
  'la ausencia.',
  None,
  MOVIMIENTO),

 ('d09_el_funcionario', 'Pilar',
  'El funcionario de turno rechaza recibir el reporte formal como noticia '
  'criminal argumentando: «Eso fue un ahogamiento por imprudencia invernal. '
  'La Fiscalía investiga delitos, no accidentes climáticos. Vayan a la '
  'Defensa Civil o al Comité de Gestión del Riesgo para que manden buzos o '
  'rescate».',
  'El funcionario de turno rechaza recibir el reporte formal como noticia '
  'criminal argumentando: eso fue un ahogamiento por imprudencia invernal. '
  'La Fiscalía investiga delitos, no accidentes climáticos. Vayan a la '
  'Defensa Civil o al Comité de Gestión del Riesgo para que manden buzos o '
  'rescate.',
  CARTON),
]

BLOQUES['E'] = [
 ('e01_gustavo_adolfo', 'Carlos',
  'Gustavo Adolfo Ramírez, de 38 años, comerciante de ganado y habitante de '
  'la vereda La Esperanza en el municipio de San José de las Peñas.',
  'Gustavo Adolfo Ramírez, de treinta y ocho años, comerciante de ganado y '
  'habitante de la vereda La Esperanza en el municipio de San José de las '
  'Peñas.',
  0.0),

 ('e02_el_mirador', 'Carlos',
  'El 28 de abril de 2026, a las 17:30 horas, mientras Gustavo Adolfo '
  'caminaba cerca del antiguo estadero El Mirador, es abordado por dos '
  'sujetos armados que descendieron de una motocicleta.',
  'El veintiocho de abril de dos mil veintiséis, a las diecisiete horas y '
  'treinta minutos, mientras Gustavo Adolfo caminaba cerca del antiguo '
  'estadero El Mirador, es abordado por dos sujetos armados que '
  'descendieron de una motocicleta.',
  NORMAL),

 ('e03_dos_disparos', 'Carlos',
  'Tras una breve discusión verbal, uno de los atacantes le dispara en dos '
  'oportunidades a la altura del tórax y la cabeza.',
  None,
  NORMAL),

 ('e04_los_testigos', 'Carlos',
  'Testigos presenciales (comerciantes y transeúntes del sector) observan '
  'cómo, de forma inmediata, un vehículo tipo camión de estacas se atraviesa '
  'en la vía.',
  'Testigos presenciales, comerciantes y transeúntes del sector, observan '
  'cómo, de forma inmediata, un vehículo tipo camión de estacas se atraviesa '
  'en la vía.',
  MOVIMIENTO),

 ('e05_el_camion', 'Carlos',
  'Los dos agresores suben a Gustavo Adolfo —quien se encontraba sangrando '
  'profusamente y sin signos aparentes de movilidad— a la parte trasera del '
  'vehículo y huyen a alta velocidad con rumbo a los callejones rurales de '
  'la Finca El Vergel.',
  'Los dos agresores suben a Gustavo Adolfo, quien se encontraba sangrando '
  'profusamente y sin signos aparentes de movilidad, a la parte trasera del '
  'vehículo y huyen a alta velocidad con rumbo a los callejones rurales de '
  'la Finca El Vergel.',
  NORMAL),

 ('e06_desaparece', 'Carlos',
  'Pese a los patrullajes y a las llamadas de auxilio de los testigos, el '
  'vehículo desaparece de la vista.',
  None,
  MOVIMIENTO),

 ('e07_setenta_y_dos_horas', 'Carlos',
  'Transcurridas 72 horas, no se ha recibido comunicación de los '
  'perpetradores, no ha ingresado ningún cuerpo con esas características a '
  'los centros hospitalarios ni a la morgue municipal, ni se conoce el lugar '
  'donde fue depositado o inhumado el cuerpo de Gustavo Adolfo.',
  'Transcurridas setenta y dos horas, no se ha recibido comunicación de los '
  'perpetradores, no ha ingresado ningún cuerpo con esas características a '
  'los centros hospitalarios ni a la morgue municipal, ni se conoce el lugar '
  'donde fue depositado o inhumado el cuerpo de Gustavo Adolfo.',
  NORMAL),

 ('e08_el_fiscal_de_turno', 'Carlos',
  'Al recibir el reporte, el fiscal de turno califica provisionalmente las '
  'diligencias de manera exclusiva como «Homicidio Agravado» y remite la '
  'carpeta al despacho seccional de delitos contra la vida, sosteniendo que '
  '«como hubo testigos de los disparos fatales, el hecho ya se consumó como '
  'homicidio y no corresponde a un caso de desaparición, por lo que no '
  'procede activar la búsqueda sino esperar la aparición fortuita del '
  'cadáver».',
  'Al recibir el reporte, el fiscal de turno califica provisionalmente las '
  'diligencias de manera exclusiva como homicidio agravado y remite la '
  'carpeta al despacho seccional de delitos contra la vida, sosteniendo que '
  'como hubo testigos de los disparos fatales, el hecho ya se consumó como '
  'homicidio y no corresponde a un caso de desaparición, por lo que no '
  'procede activar la búsqueda sino esperar la aparición fortuita del '
  'cadáver.',
  CARTON),
]

# --------------------------------------------------------------- imagenes
# El contexto VERBATIM de cada imagen. Es el texto que acompana la
# ilustracion en la lamina; la consigna queda fuera, como marco la agencia.
TEXTOS = {
 'F': ('El 15 de marzo de 2026, a las 08:30 hrs, la Sra. Rosa Elena Morales '
       'acude en estado de alta vulnerabilidad emocional a la oficina de '
       'recepción de denuncias. Refiere que su hijo Carlos Alberto Morales '
       '(34 años, transportador rural y líder comunal) no llegó a pernoctar '
       'tras salir hacia la vereda La Esperanza en su camioneta Toyota Hilux '
       '(placas XYZ-789). Manifiesta que su teléfono celular pasa '
       'directamente a buzón desde las 19:12 hrs del día anterior.'),
 'G': ('El 28 de mayo de 2026, la adolescente Mariana Morales (16 años), '
       'hermana menor de Carlos Alberto y vocera del colectivo de víctimas, '
       'asiste a la diligencia de exhumación en la Finca El Vergel y entrega '
       'declaraciones a medios locales exigiendo justicia. A las 18:00 hrs '
       'de ese mismo día no regresa a su domicilio. Su teléfono celular es '
       'desconectado tras recibir mensajes intimidantes de texto. La familia '
       'acude de inmediato a la fiscalía general de la Nación a reportar su '
       'desaparición y solicitar auxilio urgente.'),
 'H': ('En el municipio de San José de las Peñas, la desaparición de Carlos '
       'Alberto Morales genera un impacto diferenciado en dos mujeres de su '
       'núcleo familiar:\n'
       '1. Sra. Rosa Elena Morales (Madre / Mujer adulta mayor rural) quien '
       'asume de manera inmediata el rol de lideresa de la búsqueda de su '
       'hijo, afrontando estigmatización comunitaria, cargas económicas de '
       'subsistencia y afectaciones a la salud física y mental.\n'
       '2. Mariana Morales (Hermana / Adolescente de 16 años - Sub-caso '
       'I-09) toma la vocería del colectivo de víctimas, y tras visibilizar '
       'el caso en medios de comunicación es víctima de mensajes '
       'intimidantes y posterior desaparición.'),
 'I': ('El 15 de marzo de 2026, la Sra. Rosa Elena Morales acude en estado '
       'de alta vulnerabilidad emocional a la subestación de policía y '
       'posteriormente a la recepción de denuncias tras la no llegada de su '
       'hijo Carlos Alberto. El servidor de atención registra en la minuta: '
       '«Posible retiro voluntario del hogar por deudas comerciales o '
       'desavenencias personales. Se sugiere a la familia esperar 72 horas '
       'para interponer denuncia formal»'),
 'J': ('Durante la investigación del caso de Carlos Alberto Morales en San '
       'José de las Peñas, el equipo interdisciplinario recauda diversas '
       'fuentes de información que abarcan anotaciones policiales, '
       'entrevistas a testigos, reportes de celdas telefónicas, hallazgos de '
       'prospección GPR, actas de exhumación, dictámenes de '
       'antropología/odontología, análisis genético de ADN y matrices de '
       'patrones criminales (Documentos I-01 a I-08).'),
 'K': ('Ha culminado la recolección de pruebas en el caso de Carlos Alberto '
       'Morales (Documentos I-01 a I-08) y la atención de la emergencia de '
       'su hermana Mariana Morales (Sub-caso I-09). Como equipo '
       'interdisciplinario (Fiscal, Investigador CTI, Perito Forense y '
       'Analista de Contexto), deben consolidar la información fragmentada y '
       'elaborar el Informe Integral de Esclarecimiento del Caso.'),
}


def bloques(letra):
    """Devuelve [(id, voz, texto_verbatim, texto_tts, pausa_antes)]."""
    return [(i, v, t, (s if s is not None else t), p)
            for i, v, t, s, p in BLOQUES[letra]]


def palabras(letra):
    if letra in BLOQUES:
        return sum(len(t.split()) for _, _, t, _, _ in BLOQUES[letra])
    return len(TEXTOS[letra].split())


def contexto(letra):
    """El contexto entero, verbatim, como un solo texto."""
    if letra in BLOQUES:
        return ' '.join(t for _, _, t, _, _ in BLOQUES[letra])
    return TEXTOS[letra]


if __name__ == '__main__':
    print('%-3s %-7s %-8s %-9s %s' % ('', 'tipo', 'palabras', 'voz s', 'carpeta'))
    tot = 0.0
    for k in sorted(SITUACIONES):
        tipo, carpeta, voz = SITUACIONES[k]
        n = palabras(k)
        if tipo == 'video':
            seg = n / 142.0 * 60 + sum(p for *_, p in BLOQUES[k])
            tot += seg
            print('%-3s %-7s %-8d %6.1f s  %s' % (k, tipo, n, seg, carpeta))
        else:
            print('%-3s %-7s %-8d %9s  %s' % (k, tipo, n, '-', carpeta))
    print('\nnarracion de los cinco videos: %.0f s; con envoltorio %.0f s'
          % (tot, tot + 5 * (182 + 119 + 48 + 119 + 182) / 23.976))
