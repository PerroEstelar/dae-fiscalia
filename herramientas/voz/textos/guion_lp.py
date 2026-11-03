# -*- coding: utf-8 -*-
r"""Curso «Ley 1826 de 2017: procedimiento penal especial abreviado y acusador
privado» (PRIORIDAD 1) · 8 láminas y 5 videos.

LA FUENTE (Drive de la agencia)
    Carpeta «PRIORIDAD 1 - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO»
    https://drive.google.com/drive/folders/1T7Lzpllmqh-MtWJyKdPCoLbCt8I5S2vq
    «Unidad 1»  19sUHVAjN274yGppu5FfycjWOD3aNIJlZn6roKfB8g3I
    «Unidad 2»  1vcQ0m43uwjbM8z91CjxIRs8iz0SF5G8LB7wL3h0PbCQ
    «Unidad 3»  1KW16n185CvAqImjWceADFgSdXQSR1LyN1p-ttAYJ3Go
    «Unidad 4»  1hcAKvKVVySOw3YK65tzZIx_mDn7xc9ICgf0YnbzOjmM
    Las unidades se llaman como en la ficha del curso («Prioridad 1 -
    Presentacion Vaciado_Ortotipo_Corrección_Curso Ley 1826 de 2017»).

EL ENCARGO (Sebastián, 3 nov 2026)
    U1  cinco LÁMINAS: ilustración vívida, imaginativa, «casi como un afiche
        de cine», con el estilo de la serie, y a un lado el texto. Solo la
        «Síntesis fáctica del caso». Composición y lenguaje de las láminas
        de «16 situaciones» (Desaparición forzada).
    U2  dos VIDEOS animados con la receta de la serie (la de Derechos
        humanos). SOLO LOS HECHOS (él lo eligió: el vaciado trae módulos con
        «Solución», no entran).
    U3  tres LÁMINAS, solo la «Premisa fáctica».
    U4  tres VIDEOS muy cortos, los «Casos de análisis», verbatim.
    Créditos de Magnific: mitad y mitad con la serie siguiente (~6.800 para
    esta tanda de 13.706).

DOS TEXTOS POR BLOQUE, COMO EN TODA LA SERIE
    `texto`  el documento VERBATIM, para el cartón y la lámina. Comillas «».
             Los números en dígitos (es lo que se lee).
    `tts`    lo mismo dicho para ElevenLabs: números en letras, siglas
             desplegadas («VIF» -> «violencia intrafamiliar»), placas
             deletreadas, paréntesis a comas. Solo cuando hace falta.

ERRATAS DEL DOCUMENTO (la regla de la casa: «corregir lo obvio»)
    U1 C5  «José A.C. Y María T.C.» -> «José A.C. y María T.C.».
    U2 C1  «constató que etiquetas y los tapas» -> «constató que las
           etiquetas y las tapas».
    U4 C1  «con el argumento de que que la inasistencia» -> «de que la».
    U4 C2  doble espacio después de «velocidad,».
    Las comillas rectas del documento pasan a «».

LAS VOCES (ElevenLabs, cuenta de Sebastián, las del curso de Desaparición
forzada: Carlos y Pilar se turnan de video a video)
    U2 C1 Carlos · U2 C2 Pilar · U4 C1 Carlos · U4 C2 Pilar · U4 C3 Carlos.
    Nadie más habla: todo es narración en tercera persona del documento; la
    frase del agresor en U2 C2 la dice la narradora, entre comillas en el
    cartón. No se inventan parlamentos.
"""

PREFIJO = 'LP_'

CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.7
PARRAFO = 1.1

DRIVE = 'https://drive.google.com/drive/folders/1T7Lzpllmqh-MtWJyKdPCoLbCt8I5S2vq'
DRIVE_IMAGENES = None        # se llenan al crear las carpetas
DRIVE_VIDEOS = None

CURSO = 'Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado'
ANTE = 'Ley 1826 de 2017'

UNIDADES = {
 1: 'UNIDAD 1 - Finalidad ambito de aplicacion y procedencia',
 2: 'UNIDAD 2 - Procedimiento investigacion traslado audiencia concentrada y juicio',
 3: 'UNIDAD 3 - Acusador privado conversion y reversion',
 4: 'UNIDAD 4 - Terminacion anticipada y mecanismos restaurativos',
}
UNIDAD_TITULO = {
 1: 'Finalidad, ámbito de aplicación y procedencia',
 2: 'Procedimiento: investigación, traslado, audiencia concentrada y juicio',
 3: 'Acusador privado, conversión y reversión',
 4: 'Terminación anticipada y mecanismos restaurativos',
}

# clave -> (tipo, unidad, carpeta de la pieza, voz, antetitulo, titulo)
PIEZAS = {
 'U1C1': ('imagen', 1, 'CASO DE ESTUDIO 1 - Traslado del escrito y congruencia',
          None, 'Caso de estudio 1', None),
 'U1C2': ('imagen', 1, 'CASO DE ESTUDIO 2 - Tecnica de redaccion de los HJR',
          None, 'Caso de estudio 2', None),
 'U1C3': ('imagen', 1, 'CASO DE ESTUDIO 3 - Concursos subsidiariedad y via procedimental',
          None, 'Caso de estudio 3', None),
 'U1C4': ('imagen', 1, 'CASO DE ESTUDIO 4 - Maltrato psicologico y libertad probatoria',
          None, 'Caso de estudio 4', None),
 'U1C5': ('imagen', 1, 'CASO DE ESTUDIO 5 - Nucleo familiar y duracion de la convivencia',
          None, 'Caso de estudio 5', None),
 'U2C1': ('video', 2, 'ESTUDIO REVERSO 1 - Escrito de acusacion flagrancia y nulidad',
          'Carlos', 'Unidad 2 · Estudio reverso de caso 1',
          'Escrito de acusación, flagrancia y nulidad'),
 'U2C2': ('video', 2, 'ESTUDIO REVERSO 2 - Audiencia de prueba anticipada',
          'Pilar', 'Unidad 2 · Estudio reverso de caso 2',
          'Audiencia de prueba anticipada'),
 'U3C1': ('imagen', 3, 'CASO DE ESTUDIO 1 - Viabilidad en delitos contra el patrimonio economico',
          None, 'Caso de estudio 1', None),
 'U3C2': ('imagen', 3, 'CASO DE ESTUDIO 2 - Improcedencia por concurso o inimputabilidad',
          None, 'Caso de estudio 2', None),
 'U3C3': ('imagen', 3, 'CASO DE ESTUDIO 3 - Reversion por desviacion de poder',
          None, 'Caso de estudio 3', None),
 'U4C1': ('video', 4, 'CASO DE ANALISIS 1', 'Carlos', 'Unidad 4',
          'Caso de análisis 1'),
 'U4C2': ('video', 4, 'CASO DE ANALISIS 2', 'Pilar', 'Unidad 4',
          'Caso de análisis 2'),
 'U4C3': ('video', 4, 'CASO DE ANALISIS 3', 'Carlos', 'Unidad 4',
          'Caso de análisis 3'),
}
VIDEOS = [k for k, v in PIEZAS.items() if v[0] == 'video']
IMAGENES = [k for k, v in PIEZAS.items() if v[0] == 'imagen']

# compatibilidad con las herramientas de la serie (dh_pieza & co.):
# TEMAS[clave] = (carpeta relativa a la raiz del curso, voz, antetitulo, titulo)
TEMAS = {k: (UNIDADES[v[1]] + '\\' + v[2], v[3], v[4], v[5])
         for k, v in PIEZAS.items() if v[0] == 'video'}

ENTREGA = {
 'U1C1': 'PRIO 1 - LEY 1826 - UNIDAD 1 CASO DE ESTUDIO 1',
 'U1C2': 'PRIO 1 - LEY 1826 - UNIDAD 1 CASO DE ESTUDIO 2',
 'U1C3': 'PRIO 1 - LEY 1826 - UNIDAD 1 CASO DE ESTUDIO 3',
 'U1C4': 'PRIO 1 - LEY 1826 - UNIDAD 1 CASO DE ESTUDIO 4',
 'U1C5': 'PRIO 1 - LEY 1826 - UNIDAD 1 CASO DE ESTUDIO 5',
 'U2C1': 'PRIO 1 - LEY 1826 - UNIDAD 2 ESTUDIO REVERSO 1 ESCRITO DE ACUSACION FLAGRANCIA Y NULIDAD',
 'U2C2': 'PRIO 1 - LEY 1826 - UNIDAD 2 ESTUDIO REVERSO 2 AUDIENCIA DE PRUEBA ANTICIPADA',
 'U3C1': 'PRIO 1 - LEY 1826 - UNIDAD 3 CASO DE ESTUDIO 1',
 'U3C2': 'PRIO 1 - LEY 1826 - UNIDAD 3 CASO DE ESTUDIO 2',
 'U3C3': 'PRIO 1 - LEY 1826 - UNIDAD 3 CASO DE ESTUDIO 3',
 'U4C1': 'PRIO 1 - LEY 1826 - UNIDAD 4 CASO DE ANALISIS 1',
 'U4C2': 'PRIO 1 - LEY 1826 - UNIDAD 4 CASO DE ANALISIS 2',
 'U4C3': 'PRIO 1 - LEY 1826 - UNIDAD 4 CASO DE ANALISIS 3',
}

# --------------------------------------------------------------- láminas
# El texto del panel: VERBATIM la «Síntesis fáctica del caso» (U1) o la
# «Premisa fáctica» (U3). Nada más entra (Sebastián: «solo la parte que
# dice síntesis fáctica del caso»).
TEXTOS = {
 'U1C1': ('El 11 de julio de 2024, bajo las reglas de la Ley 1826 de 2017, la '
          'Fiscalía corrió traslado del escrito de acusación a José A.C. En la '
          'sección de hechos se le imputó haber agredido a su compañera '
          'permanente María T.C. la noche del 5 de agosto de 2023 en su '
          'vivienda del barrio Prado Alto al golpearla con las manos e '
          'insultarla. La Fiscalía adecuó la conducta como VIF agravada (art. '
          '229, inciso 2 del CP). No obstante, en la acusación no se '
          'incluyeron hechos de contexto sobre actos de dominación o violencia '
          'previas e históricas contra la víctima.'),
 'U1C2': ('Al redactar el escrito de acusación para el traslado, el asistente '
          'de fiscalía incluyó dentro del capítulo de hechos transcripciones '
          'de la entrevista realizada a la víctima, así como apartes textuales '
          'de los dictámenes emitidos por el Instituto Nacional de Medicina '
          'Legal y Ciencias Forenses el 6 de agosto de 2023. La defensa '
          'formuló observaciones en la audiencia concentrada señalando '
          'vaguedad e imprecisión en los cargos.'),
 'U1C3': ('Durante el episodio del 5 de agosto de 2023, el agresor propinó '
          'golpes en el brazo a la víctima con los puños, le causó injurias '
          'verbales («gorda asquerosa, sucia y perra») y le impidió la salida '
          'de la habitación. La defensa solicitó en la audiencia concentrada '
          'la nulidad del trámite bajo el argumento de que debió investigarse '
          'un concurso heterogéneo de delitos (lesiones personales, injuria y '
          'constreñimiento ilegal), lo que exigiría agotar previamente la '
          'conciliación como requisito de procedibilidad respecto de la '
          'injuria o las lesiones querellables.'),
 'U1C4': ('En el examen de clínica forense realizado a la víctima el 6 de '
          'agosto de 2023 (un día después de los hechos), el perito de '
          'Medicina Legal no encontró huellas externas de lesión reciente ni '
          'fijó incapacidad médico-legal. Con posterioridad, el 20 de '
          'diciembre de 2023, la valoración psiquiátrica concluyó que la '
          'víctima presentaba «sintomatología ansiosa con elementos '
          'postraumáticos». La defensa argumentó que existía atipicidad al no '
          'haber lesiones físicas visibles y alegó falta de prueba sobre el '
          'nexo causal del daño psicológico.'),
 'U1C5': ('José A.C. y María T.C. convivieron bajo el mismo techo en un '
          'inmueble del barrio Prado Alto durante un período de cinco meses. '
          'Durante el juicio oral, la defensa argumentó que la conducta era '
          'atípica por ausencia del elemento normativo «núcleo familiar» y '
          'alegó que una convivencia tan corta solo constituía un «noviazgo '
          'informal» sin vocación de permanencia ni unidad marital '
          'consolidada.'),
 'U3C1': ('En un caso de estafa en masa donde resultaron afectadas quince '
          'personas naturales por una falsa promesa de inversión en '
          'criptoactivos en el año 2024, el apoderado judicial de las víctimas '
          'presenta una solicitud formal de conversión de la acción penal de '
          'pública a privada y adjunta poder especial debidamente autenticado '
          'suscrito por trece de los afectados.'),
 'U3C2': ('Una víctima de hurto agravado cometido en un establecimiento '
          'comercial por un ciudadano extranjero solicita la conversión de la '
          'acción penal a privada. En el curso de la indagación inicial de la '
          'Fiscalía, se recopilan dictámenes psiquiátricos del Instituto '
          'Nacional de Medicina Legal que sugieren fuertemente que el '
          'indiciado padece de esquizofrenia paranoide grave al momento de la '
          'comisión de los hechos fácticos.'),
 'U3C3': ('Una vez concedida la conversión en un delito de inasistencia '
          'alimentaria, el apoderado de la víctima investido como acusador '
          'privado radica citaciones periódicas de carácter intimidatorio en '
          'el domicilio laboral del indiciado, amenaza de forma directa a los '
          'testigos de la defensa con iniciar denuncias de falso testimonio si '
          'comparecen en el juicio oral y oculta sistemáticamente un recibo de '
          'pago por concepto de aportes de alimentos que el indiciado le '
          'remitió previo al traslado de acusación.'),
}
# en la lámina de U1 C2 «capítulo de hechos» va en cursiva, como en el documento
CURSIVA = {'U1C2': ['capítulo de hechos']}

# --------------------------------------------------------------- videos
# (id, voz, texto_verbatim, texto_tts_o_None, pausa_antes)
BLOQUES = {}

BLOQUES['U2C1'] = [
 ('a01_cali', 'Carlos',
  'El 15 de agosto de 2023, en el barrio Industrial de la ciudad de Cali, el '
  'supervisor de zona Jorge Eliécer Benavides sorprendió a Mario Alberto Gómez '
  'Parra (contratista activo de la distribuidora) y a Pedro Antonio Morales '
  'Rincón (extransportador)',
  'El quince de agosto de dos mil veintitrés, en el barrio Industrial de la '
  'ciudad de Cali, el supervisor de zona Jorge Eliécer Benavides sorprendió a '
  'Mario Alberto Gómez Parra, contratista activo de la distribuidora, y a '
  'Pedro Antonio Morales Rincón, extransportador,',
  0.0),
 ('a02_transbordo', 'Carlos',
  'realizando el transbordo clandestino de 45 botellas con etiquetas de la '
  'marca protegida Kombucha Valle desde un vehículo particular (Placa KTH412) '
  'hacia el camión repartidor oficial de la compañía (Placa WXN445).',
  'realizando el transbordo clandestino de cuarenta y cinco botellas con '
  'etiquetas de la marca protegida Kombucha Valle, desde un vehículo '
  'particular, placa ka, te, hache, cuatro, uno, dos, hacia el camión '
  'repartidor oficial de la compañía, placa doble ve, equis, ene, cuatro, '
  'cuatro, cinco.',
  0.35),
 ('a03_envases', 'Carlos',
  'Al inspeccionar los envases, el supervisor constató que las etiquetas y '
  'las tapas no correspondían a los estándares originales de la fábrica.',
  None, PARRAFO),
 ('a04_seguimiento', 'Carlos',
  'Asimismo, el supervisor venía haciendo seguimiento a la zona de '
  'distribución a cargo de Mario Alberto, debido a una caída atípica e '
  'injustificada en las ventas durante los meses anteriores.',
  None, NORMAL),
 ('a05_video', 'Carlos',
  'Sobre el hallazgo grabó un video de las botellas con su celular.',
  None, NORMAL),
 ('a06_sin_captura', 'Carlos',
  'La investigación se adelantó sin captura, recepcionándose entrevistas al '
  'personal de seguridad y recopilándose informes técnicos e investigaciones '
  'internas de la empresa en 2023.',
  'La investigación se adelantó sin captura, recepcionándose entrevistas al '
  'personal de seguridad y recopilándose informes técnicos e investigaciones '
  'internas de la empresa en dos mil veintitrés.',
  PARRAFO),
 ('a07_radicado', 'Carlos',
  'El escrito de acusación se radicó bajo las reglas del procedimiento penal '
  'especial abreviado (Ley 1826 de 2017) el 4 de febrero de 2026.',
  'El escrito de acusación se radicó bajo las reglas del procedimiento penal '
  'especial abreviado, Ley mil ochocientos veintiséis de dos mil diecisiete, '
  'el cuatro de febrero de dos mil veintiséis.',
  NORMAL),
]

BLOQUES['U2C2'] = [
 ('b01_tres_anos', 'Pilar',
  'Durante los últimos tres años, en vivienda conyugal ubicada en Medellín, '
  'Carlos Eduardo Restrepo Múnera ejerció actos continuados de maltrato '
  'físico, verbal y psicológico contra su cónyuge, María Elena Gutiérrez Ríos.',
  None, 0.0),
 ('b02_episodio', 'Pilar',
  'El episodio más grave ocurrió el 10 de enero de 2026, cuando el procesado '
  'agredió físicamente a María Elena, lo que le causó una incapacidad '
  'médico-legal definitiva de 25 días con deformidad física transitoria,',
  'El episodio más grave ocurrió el diez de enero de dos mil veintiséis, '
  'cuando el procesado agredió físicamente a María Elena, lo que le causó una '
  'incapacidad médico legal definitiva de veinticinco días con deformidad '
  'física transitoria,',
  PARRAFO),
 ('b03_la_mato', 'Pilar',
  'y le manifestó expresamente: «si me denuncia o habla en un juzgado, la '
  'mato a usted y a su mamá».',
  'y le manifestó expresamente: si me denuncia o habla en un juzgado, la mato '
  'a usted y a su mamá.',
  0.35),
 ('b04_intimidacion', 'Pilar',
  'Tras la denuncia interpuesta por un tercero y la emisión de una medida de '
  'protección de urgencia, el procesado ha iniciado una campaña de '
  'intimidación:',
  None, PARRAFO),
 ('b05_armados', 'Pilar',
  'ha enviado a familiares y terceros armados al lugar donde María Elena se '
  'encuentra refugiada y le ha exigido la retractación inmediata.',
  None, 0.35),
 ('b06_riesgo', 'Pilar',
  'Ante el riesgo inminente para la vida de la víctima y la necesidad de '
  'trasladarla de manera inmediata a un refugio confidencial en el exterior a '
  'través de la red de protección a víctimas de VBG (Ley 1257 de 2008),',
  'Ante el riesgo inminente para la vida de la víctima y la necesidad de '
  'trasladarla de manera inmediata a un refugio confidencial en el exterior, '
  'a través de la red de protección a víctimas de violencia basada en género, '
  'Ley mil doscientos cincuenta y siete de dos mil ocho,',
  PARRAFO),
 ('b07_no_esperar', 'Pilar',
  'la Fiscalía determina que no es viable esperar hasta la audiencia de '
  'juicio oral para recepcionar su testimonio.',
  None, 0.35),
 ('b08_prueba_anticipada', 'Pilar',
  'Por ello, la Fiscalía acude ante el juez de control de garantías para '
  'solicitar la práctica anticipada de su testimonio.',
  None, NORMAL),
]

BLOQUES['U4C1'] = [
 ('c01_noticia', 'Carlos',
  'Un fiscal local de Bogotá recibe una noticia criminal por un delito de '
  'inasistencia alimentaria (art. 233 del CP), cometido presuntamente por un '
  'ciudadano de 35 años de edad contra su hijo menor de edad.',
  'Un fiscal local de Bogotá recibe una noticia criminal por un delito de '
  'inasistencia alimentaria, artículo doscientos treinta y tres del Código '
  'Penal, cometido presuntamente por un ciudadano de treinta y cinco años de '
  'edad contra su hijo menor de edad.',
  0.0),
 ('c02_conciliacion', 'Carlos',
  'El fiscal decide, con el fin de agilizar el proceso preprocesal y resolver '
  'el conflicto de forma expedita, fijar fecha para diligencia de '
  'conciliación utilizando el formato FGN-MP02-F-10.',
  'El fiscal decide, con el fin de agilizar el proceso preprocesal y resolver '
  'el conflicto de forma expedita, fijar fecha para diligencia de '
  'conciliación utilizando el formato efe, ge, ene, eme, pe, cero dos, efe, '
  'diez.',
  PARRAFO),
 ('c03_recusacion', 'Carlos',
  'Sin embargo, la defensa del indiciado presenta una solicitud de recusación '
  'contra el fiscal y posterior solicitud de nulidad en la audiencia '
  'concentrada',
  None, PARRAFO),
 ('c04_no_querellable', 'Carlos',
  'con el argumento de que la inasistencia alimentaria no es un delito '
  'querellable y que exigir conciliación obligatoria vulnera el debido '
  'proceso.',
  None, 0.3),
]

BLOQUES['U4C2'] = [
 ('d01_mediacion', 'Pilar',
  'En el curso de un proceso por lesiones personales culposas en accidente de '
  'tránsito, las partes comparecen voluntariamente y solicitan de común '
  'acuerdo la aplicación del trámite de mediación penal.',
  None, 0.0),
 ('d02_mediador', 'Pilar',
  'El fiscal de conocimiento realiza el correspondiente trámite remitiendo el '
  'conflicto a un mediador del distrito judicial mediante el formato '
  'FGN-MP02-F-132.',
  'El fiscal de conocimiento realiza el correspondiente trámite remitiendo el '
  'conflicto a un mediador del distrito judicial mediante el formato efe, ge, '
  'ene, eme, pe, cero dos, efe, ciento treinta y dos.',
  NORMAL),
 ('d03_exceso', 'Pilar',
  'Durante la sesión de mediación, el indiciado acepta expresamente que '
  'conducía con exceso de velocidad, manifiesta un profundo arrepentimiento y '
  'se ofrece a pagar la suma de 10 millones de pesos como indemnización '
  'total.',
  'Durante la sesión de mediación, el indiciado acepta expresamente que '
  'conducía con exceso de velocidad, manifiesta un profundo arrepentimiento y '
  'se ofrece a pagar la suma de diez millones de pesos como indemnización '
  'total.',
  PARRAFO),
 ('d04_sin_acuerdo', 'Pilar',
  'Tras varias sesiones, no se llega a un acuerdo y se suscribe el formato '
  'FGN-MP02-F-133, certificando que no hubo acuerdo.',
  'Tras varias sesiones, no se llega a un acuerdo y se suscribe el formato '
  'efe, ge, ene, eme, pe, cero dos, efe, ciento treinta y tres, certificando '
  'que no hubo acuerdo.',
  NORMAL),
 ('d05_audio', 'Pilar',
  'Durante el juicio oral, el fiscal pretende introducir el audio de la sesión '
  'de mediación para demostrar que el acusado admitió el exceso de velocidad '
  'y la autoría de la agresión.',
  None, PARRAFO),
 ('d06_exclusion', 'Pilar',
  'El defensor formula oposición solicitando la regla de exclusión.',
  None, NORMAL),
]

BLOQUES['U4C3'] = [
 ('e01_denuncia', 'Carlos',
  'Una ciudadana de 28 años presenta denuncia por el delito de VIF sistemática '
  'en concurso con lesiones personales dolosas simples contra su cónyuge.',
  'Una ciudadana de veintiocho años presenta denuncia por el delito de '
  'violencia intrafamiliar sistemática, en concurso con lesiones personales '
  'dolosas simples, contra su cónyuge.',
  0.0),
 ('e02_desistir', 'Carlos',
  'La víctima asiste al despacho del fiscal en compañía de un abogado del '
  'consultorio jurídico de una universidad manifestando que voluntariamente '
  'desea desistir de la denuncia,',
  None, PARRAFO),
 ('e03_archivo', 'Carlos',
  'además solicita formalizar un acuerdo de mediación y posterior archivo de '
  'la carpeta penal,',
  None, 0.3),
 ('e04_terapia', 'Carlos',
  'alegando que su esposo ya se disculpó y prometió asistir a terapia de '
  'pareja y que ella depende económicamente de él.',
  None, 0.3),
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
        print('%-5s %4d palabras %2d bloques ~%5.1f s de voz  %s'
              % (k, n, len(BLOQUES[k]), seg, TEMAS[k][0]))
    for k in IMAGENES:
        print('%-5s lámina %4d caracteres' % (k, len(TEXTOS[k])))
