# -*- coding: utf-8 -*-
r"""Guion de los casos introductorios del curso «Gerencia judicial»
(PRIORIDAD 2) · documento «Gerencia judicial - Casos varios» del Drive.

QUE HAY EN EL DOCUMENTO
    Tres temas -Primer, Tercer y Cuarto; el Segundo no viene- y cada uno
    abre con un CASO INTRODUCTORIO. Alrededor de cada caso hay material que
    NO es del video: la pregunta que guia el tema y los conceptos clave
    (Tema 1), la referencia al caso real de la Corte Suprema y la lista de
    decisiones (i)-(vi) (Tema 3). Va a Moodle y no nos corresponde.

LO QUE LA AGENCIA MARCO, COMENTARIO POR COMENTARIO (29 oct 2026)
    Tema 1  «Solo esto en video»: el parrafo del caso, del «Un fiscal recien
            nombrado» hasta «sin investigar». Ni la pregunta ni los
            conceptos.
    Tema 3  «Video»: los cuatro parrafos de la hipotesis, del «Usted es
            fiscal delegado» hasta «la totalidad del incremento
            patrimonial». NO el parrafo del caso real (Triple A, cincuenta
            y cuatro ordenes, veintisiete mil millones) ni las decisiones.
    Tema 4  «Video» sobre TODA la hipotesis, del «Usted ejerce funciones
            de coordinacion» al final, y otro «Video» anidado de «La
            primera ocurre dentro del equipo» al final. El anidado se puso
            catorce segundos ANTES que el grande (14:14:53 contra 14:15:07):
            primero marcaron las situaciones y despues ampliaron la marca
            para que entrara el encuadre de la coordinacion. Es UN video.

TRES VIDEOS, NO CUATRO
    Sebastian dijo «3 o 4». El documento marca tres textos, y el cuarto
    tema no se parte: sus dos situaciones existen como PAR -«dos
    situaciones que, en apariencia, pertenecen a ambitos completamente
    distintos»- y la segunda arranca con «Ese mismo dia», que suelto no
    tiene a que referirse. Si se quiere partir, la rejilla ya tiene el corte
    natural en la frontera de c04 («La primera ocurre...»).

DOS TEXTOS POR BLOQUE, COMO EN TODA LA SERIE
    `texto`  el documento VERBATIM. Va al carton. Las comillas del
             documento pasan a angulares «», que es la tipografia de la
             serie, y las negritas del documento se pierden (son enfasis
             de lectura, no texto); ninguna palabra cambia.
    `tts`    lo mismo dicho para que ElevenLabs lo pronuncie: numeros en
             letras, siglas deletreadas, parentesis pasados a comas. Solo
             existe cuando hace falta. La diferencia es SIEMPRE de numeral,
             de sigla o de puntuacion, nunca de contenido.

LAS PAUSAS
    1,0 s antes de un movimiento nuevo · 0,9 s antes de una frase que va a
    carton verbatim · 0,8 s el resto.

LAS VOCES
    Pilar y Carlos, las de la serie, alternadas por tema: T1 Pilar, T3
    Carlos, T4 Pilar. En el T4 las DOS CITAS -lo que responde el
    coordinador y lo que sostiene el investigador- las dice Carlos: el
    documento las escribe en primera persona y entre comillas, son
    parlamentos del texto y no invencion nuestra. La frase que las
    introduce («Uno de los coordinadores responde:») va pegada al bloque
    anterior en la voz de Pilar, para que la rejilla no deje una ranura de
    un segundo y medio entre la narradora y la cita.
"""

PREFIJO = 'GJ_'

MOVIMIENTO = 1.0
CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.8

DRIVE = ('https://docs.google.com/document/d/'
         '1kZrQeecvuwx4Jj9h_7PDxAZFMtCGakATgyvjp_W-7QE/edit')
DRIVE_VIDEOS = ('https://drive.google.com/drive/folders/'
                '1hUGpHHn9iHFbTFtslGhYya6H5MF6vKGo')

ANTE = 'Gerencia judicial'

# clave -> (carpeta, voz narradora, tema como lo titula el documento)
TEMAS = {
 'T1': ('TEMA 1 - El despacho de los 2000 casos', 'Pilar',
        'Primer tema',
        'Marco institucional y direccionamiento estratégico de la Fiscalía '
        'General de la Nación'),
 'T3': ('TEMA 3 - Aceptar o negociar', 'Carlos',
        'Tercer tema',
        'Justicia premial como herramienta de gestión: más allá de lo '
        'jurídico'),
 'T4': ('TEMA 4 - Dos situaciones al comenzar la semana', 'Pilar',
        'Cuarto tema',
        'Enfoques diferenciales en la gestión del talento humano y en la '
        'persecución penal'),
}
VIDEOS = sorted(TEMAS)

# --------------------------------------------------------------- bloques
# (id, voz, texto_verbatim, tts_o_None, pausa_antes)
BLOQUES = {}

BLOQUES['T1'] = [
 ('p01_el_despacho', 'Pilar',
  'Un fiscal recién nombrado asume la dirección de un despacho con más de '
  '2.000 casos acumulados.',
  'Un fiscal recién nombrado asume la dirección de un despacho con más de '
  'dos mil casos acumulados.',
  0.0),

 ('p02_el_orden_de_llegada', 'Pilar',
  'Al no conocer la misión, la visión ni los objetivos de la Fiscalía '
  'General de la Nación, su equipo atiende las denuncias en el estricto '
  'orden en que llegan, gastando tiempo importante en casos menores '
  'mientras los delitos graves se quedan sin investigar.',
  None,
  CARTON),
]

BLOQUES['T3'] = [
 ('t01_la_investigacion', 'Carlos',
  'Usted es fiscal delegado y conoce una investigación relacionada con la '
  'administración irregular de recursos de una empresa prestadora de '
  'servicios públicos.',
  None,
  0.0),

 ('t02_ordenes_ficticias', 'Carlos',
  'Los elementos materiales probatorios recaudados permiten inferir que, '
  'durante varios años, algunos de sus directivos habrían utilizado órdenes '
  'de pedido ficticias y contratos simulados para extraer recursos de la '
  'compañía en beneficio propio y de terceros.',
  None,
  CARTON),

 ('t03_el_directivo', 'Carlos',
  'Uno de los investigados ocupaba un cargo directivo y habría participado '
  'en la autorización y ejecución de varias de esas operaciones.',
  None,
  MOVIMIENTO),

 ('t04_el_incremento', 'Carlos',
  'La Fiscalía le atribuye conductas que produjeron un importante '
  'incremento patrimonial ilícito.',
  None,
  NORMAL),

 ('t05_aceptar', 'Carlos',
  'Antes de avanzar al juicio, el procesado manifiesta que desea aceptar '
  'responsabilidad.',
  None,
  CARTON),

 ('t06_interrogantes', 'Carlos',
  'La manifestación plantea varios interrogantes. El fiscal debe '
  'determinar, inicialmente, si se encuentra ante una aceptación unilateral '
  'de cargos o ante una verdadera negociación.',
  None,
  MOVIMIENTO),

 ('t07_la_distincion', 'Carlos',
  'La distinción no es netamente terminológica. De ella dependerán el '
  'origen y alcance del beneficio punitivo, las reglas que resultan '
  'aplicables y, particularmente, el tratamiento del reintegro previsto en '
  'el artículo 349 de la Ley 906 de 2004 (en adelante CPP).',
  'La distinción no es netamente terminológica. De ella dependerán el '
  'origen y alcance del beneficio punitivo, las reglas que resultan '
  'aplicables y, particularmente, el tratamiento del reintegro previsto en '
  'el artículo trescientos cuarenta y nueve de la Ley novecientos seis de '
  'dos mil cuatro, en adelante, ce, pe, pe.',
  CARTON),

 ('t08_restituida', 'Carlos',
  'Además, durante la actuación se advierte que apenas una parte reducida '
  'de los recursos ha sido restituida.',
  None,
  MOVIMIENTO),

 ('t09_victimas_y_defensa', 'Carlos',
  'Las víctimas reclaman reparación y la defensa sostiene que el procesado '
  'no fue destinatario final de la totalidad del incremento patrimonial.',
  None,
  CARTON),
]

BLOQUES['T4'] = [
 ('c01_la_coordinacion', 'Pilar',
  'Usted ejerce funciones de coordinación en una dependencia de la '
  'Fiscalía General de la Nación.',
  None,
  0.0),

 ('c02_responsabilidades', 'Pilar',
  'Dentro de sus responsabilidades se encuentra orientar el trabajo de '
  'fiscales, asistentes, investigadores y personal de apoyo, distribuir '
  'cargas, resolver dificultades operativas y acompañar la toma de '
  'decisiones en investigaciones que presentan distintos niveles de '
  'complejidad.',
  None,
  NORMAL),

 ('c03_dos_situaciones', 'Pilar',
  'Al comenzar la semana se presentan dos (2) situaciones que, en '
  'apariencia, pertenecen a ámbitos completamente distintos:',
  'Al comenzar la semana se presentan dos situaciones que, en apariencia, '
  'pertenecen a ámbitos completamente distintos.',
  CARTON),

 ('c04_dentro_del_equipo', 'Pilar',
  'La primera ocurre dentro del equipo. Una servidora informa que tiene una '
  'discapacidad visual y explica que el nuevo aplicativo utilizado por la '
  'dependencia para circular documentos no es plenamente compatible con el '
  'lector de pantalla que emplea.',
  None,
  MOVIMIENTO),

 ('c05_lo_que_pide', 'Pilar',
  'Puede realizar las funciones esenciales de su cargo y no solicita que '
  'otra persona asuma sus responsabilidades. Pide que determinados '
  'documentos se remitan también en un formato accesible y que, mientras se '
  'corrige la barrera tecnológica, se establezca un mecanismo que le '
  'permita participar en igualdad de condiciones. Uno de los coordinadores '
  'responde:',
  None,
  NORMAL),

 ('c06_cita_coordinador', 'Carlos',
  '«Aquí todos debemos trabajar con las mismas herramientas. Si empezamos a '
  'hacer excepciones, dejamos de tratar a las personas por igual».',
  'Aquí todos debemos trabajar con las mismas herramientas. Si empezamos a '
  'hacer excepciones, dejamos de tratar a las personas por igual.',
  CARTON),

 ('c07_ese_mismo_dia', 'Pilar',
  'Ese mismo día, la dependencia debe orientar una investigación por '
  'violencia sexual en la que la víctima es una adolescente perteneciente a '
  'un pueblo indígena. La actuación continuará ante la jurisdicción '
  'ordinaria.',
  None,
  MOVIMIENTO),

 ('c08_la_joven', 'Pilar',
  'Sin embargo, el equipo advierte que la joven vive en una zona rural '
  'distante, que su lengua materna no es el castellano y que existen '
  'particularidades culturales que pueden incidir en la manera en que '
  'comprende la actuación y se relaciona con las autoridades.',
  None,
  NORMAL),

 ('c09_auto_456', 'Pilar',
  'Una situación semejante fue examinada por la Corte Constitucional en el '
  'Auto 456 de 2024, en el que advirtió que la permanencia del asunto en la '
  'jurisdicción ordinaria no elimina la obligación de incorporar los '
  'enfoques étnico y de género ni de evitar que factores geográficos, '
  'económicos, culturales o lingüísticos se conviertan en barreras de '
  'acceso a la justicia. Un investigador sostiene:',
  'Una situación semejante fue examinada por la Corte Constitucional en el '
  'Auto cuatrocientos cincuenta y seis de dos mil veinticuatro, en el que '
  'advirtió que la permanencia del asunto en la jurisdicción ordinaria no '
  'elimina la obligación de incorporar los enfoques étnico y de género ni '
  'de evitar que factores geográficos, económicos, culturales o '
  'lingüísticos se conviertan en barreras de acceso a la justicia. Un '
  'investigador sostiene:',
  CARTON),

 ('c10_cita_investigador', 'Carlos',
  '«El procedimiento penal es el mismo para todo el mundo. Lo más objetivo '
  'es no hacer ninguna diferencia».',
  'El procedimiento penal es el mismo para todo el mundo. Lo más objetivo '
  'es no hacer ninguna diferencia.',
  CARTON),

 ('c11_tercer_dato', 'Pilar',
  'Mientras se revisan los primeros actos de investigación aparece un '
  'tercer dato: algunos testigos afirman que, durante la agresión, el '
  'presunto responsable utilizó expresiones despectivas asociadas con la '
  'identidad y la expresión de género que él atribuía a la víctima.',
  None,
  MOVIMIENTO),

 ('c12_irrelevantes', 'Pilar',
  'El investigador que recibió inicialmente el asunto considera que esas '
  'expresiones son irrelevantes porque, a su juicio, basta establecer si '
  'existió o no la agresión.',
  None,
  CARTON),
]


def bloques(clave):
    """Devuelve [(id, voz, texto_verbatim, texto_tts, pausa_antes)]."""
    return [(i, v, t, (s if s is not None else t), p)
            for i, v, t, s, p in BLOQUES[clave]]


def palabras(clave):
    return sum(len(t.split()) for _, _, t, _, _ in BLOQUES[clave])


def contexto(clave):
    """El caso entero, verbatim, como un solo texto."""
    return ' '.join(t for _, _, t, _, _ in BLOQUES[clave])


if __name__ == '__main__':
    tot = 0.0
    for k in VIDEOS:
        carpeta, voz, tema, titulo = TEMAS[k]
        n = palabras(k)
        seg = n / 150.0 * 60 * 1.10
        tot += seg
        print('%-3s %4d palabras  ~%5.1f s de voz  %-7s %s'
              % (k, n, seg, voz, carpeta))
    print('voz de los tres: ~%.0f s' % tot)
