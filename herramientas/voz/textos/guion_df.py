# -*- coding: utf-8 -*-
r"""Guion del curso «Investigacion Judicial y Forense de la Desaparicion
Forzada» · caso integrador MIRIAM Y MARIANA · cinco capitulos.

DOS TEXTOS POR BLOQUE, Y ESA ES LA REGLA NUEVA
    `texto`  es el documento VERBATIM. Es lo que va al carton y lo que la
             Fiscalia puede verificar palabra por palabra.
    `tts`    es lo mismo dicho de modo que ElevenLabs lo pronuncie bien en
             espanol colombiano. Solo existe cuando hace falta.

    La diferencia entre los dos es SIEMPRE ortografica o de numeral, nunca
    de contenido: `sicosocial` por `psicosocial`, `treinta y seis` por `36`,
    `uno cero uno` por `I-01`. Ni una palabra cambia de sitio.

    Es la leccion del 24 de octubre: separar lo que se OYE de lo que se LEE
    deja la voz limpia sin tocar el verbatim.

LO QUE NO SE NARRA
    Los codigos de documento entre parentesis -(Documento I-03), (Acta
    I-05)- no se leen en voz alta: son una referencia de archivo, no una
    frase. Aparecen en el carton, que es donde sirven. Si se leyeran, la
    narracion sonaria a inventario.

LAS PAUSAS
    1,2 s  antes del cierre del capitulo
    1,0 s  antes de un movimiento nuevo dentro del capitulo
    0,9 s  antes de cada frase que va a carton verbatim
    0,8 s  el resto
"""

PREFIJO = 'DF_'

MOVIMIENTO = 1.0
CARTON = 0.9
CIERRE = 1.2
NORMAL = 0.8

# (id, voz, texto_verbatim, tts_o_None, pausa_antes)
CAPITULOS = {}

CAPITULOS[1] = [
 ('b01_plaza', 'Carlos',
  'En el municipio de San José de las Peñas, Miriam, una mujer '
  'afrodescendiente de 36 años en su séptimo mes de embarazo, se ha ganado '
  'la vida y el afecto de la comunidad con su puesto ambulante de arepas en '
  'la plaza principal.',
  'En el municipio de San José de las Peñas, Miriam, una mujer '
  'afrodescendiente de treinta y seis años en su séptimo mes de embarazo, se '
  'ha ganado la vida y el afecto de la comunidad con su puesto ambulante de '
  'arepas en la plaza principal.',
  0.0),

 ('b02_casa', 'Carlos',
  'Miriam vive sumida en una severa violencia intrafamiliar ejercida por su '
  'esposo Gavino, un hombre alcohólico e inestable que le roba las ganancias '
  'de su negocio para comprar licor y la encierra junto a sus dos hijos de 7 '
  'y 9 años durante fines de semana completos.',
  'Miriam vive sumida en una severa violencia intrafamiliar ejercida por su '
  'esposo Gavino, un hombre alcohólico e inestable que le roba las ganancias '
  'de su negocio para comprar licor y la encierra junto a sus dos hijos de '
  'siete y nueve años durante fines de semana completos.',
  MOVIMIENTO),

 ('b03_porque_no_se_va', 'Carlos',
  'Miriam no lo abandona porque su expareja la ha amenazado con quitarle a '
  'su hijo mayor de 12 años si la ve sola.',
  'Miriam no lo abandona porque su expareja la ha amenazado con quitarle a '
  'su hijo mayor de doce años si la ve sola.',
  NORMAL),

 ('b04_vacuna', 'Carlos',
  'Hace tres meses, tres sujetos armados que se identificaron como '
  'integrantes del Bloque Central Renacer empezaron a exigirle el pago de '
  'una vacuna extorsiva para proteger su puesto, amenazándola con ir tras '
  'sus hijos.',
  None,
  MOVIMIENTO),

 ('b05_catorce_de_mayo', 'Carlos',
  'Al no poder cumplir el pago porque Gavino le robó el dinero del puesto, '
  'la noche del 14 de mayo dos disidentes la interceptaron al cerrar el '
  'negocio, la llevaron a un potrero oscuro, le rasgaron la blusa, la '
  'manosearon e intimidaron dándole una semana de plazo para pagar.',
  'Al no poder cumplir el pago porque Gavino le robó el dinero del puesto, '
  'la noche del catorce de mayo dos disidentes la interceptaron al cerrar el '
  'negocio, la llevaron a un potrero oscuro, le rasgaron la blusa, la '
  'manosearon e intimidaron dándole una semana de plazo para pagar.',
  NORMAL),

 ('b06_televisor', 'Carlos',
  'Desesperada, al día siguiente Miriam vendió el televisor de la casa a su '
  'vecina Gregoria mientras Gavino no estaba. Esa noche, al descubrir la '
  'venta del TV, Gavino desató una violenta discusión a gritos que '
  'estremeció a la cuadra.',
  'Desesperada, al día siguiente Miriam vendió el televisor de la casa a su '
  'vecina Gregoria mientras Gavino no estaba. Esa noche, al descubrir la '
  'venta del televisor, Gavino desató una violenta discusión a gritos que '
  'estremeció a la cuadra.',
  NORMAL),

 ('b07_nadie_la_vio', 'Carlos',
  'Desde esa noche, nadie volvió a ver a Miriam ni a su puesto. Tras varios '
  'días de ausencia, Gregoria acudió a la subestación de policía a reportar '
  'la desaparición.',
  None,
  MOVIMIENTO),

 ('b08_minuta', 'Carlos',
  'El comandante de guardia registró en la minuta: «mujer con hijos de '
  'varios hombres, se fue con otro tipo, espere 72 horas para interponer '
  'denuncia».',
  'El comandante de guardia registró en la minuta: mujer con hijos de varios '
  'hombres, se fue con otro tipo, espere setenta y dos horas para interponer '
  'denuncia.',
  CARTON),

 ('b09_rumores', 'Carlos',
  'Un mes después, comenzaron los macabros rumores de que en municipios '
  'vecinos se encontraron los cuerpos de tres mujeres embarazadas reportadas '
  'como desaparecidas, halladas con el vientre abierto tras ser asesinadas '
  'para robarles el bebé.',
  None,
  CIERRE),
]

CAPITULOS[2] = [
 ('b01_rosa_elena', 'Pilar',
  'Ante la indolencia policial, la señora Rosa Elena Morales, madre de '
  'Miriam y lideresa campesina afrodescendiente, asumió la búsqueda de su '
  'hija y de su nieto por nacer.',
  None,
  0.0),

 ('b02_mariana', 'Pilar',
  'Junto a ella, la adolescente Mariana Morales, de 16 años, hermana menor '
  'de Miriam, asumió la vocería del colectivo de familias buscadoras en el '
  'municipio.',
  'Junto a ella, la adolescente Mariana Morales, de dieciséis años, hermana '
  'menor de Miriam, asumió la vocería del colectivo de familias buscadoras '
  'en el municipio.',
  NORMAL),

 ('b03_vocería', 'Pilar',
  'Mariana organizó marchas, difundió la ficha de búsqueda en redes sociales '
  'y entregó declaraciones a medios regionales denunciando la omisión de la '
  'policía local y las amenazas de las disidencias.',
  None,
  NORMAL),

 ('b04_veintiocho', 'Carlos',
  'El 28 de mayo, tras participar en una marcha pacífica y exigir respuestas '
  'en la estación de policía, Mariana no regresó a su casa a las 18:00 '
  'horas.',
  'El veintiocho de mayo, tras participar en una marcha pacífica y exigir '
  'respuestas en la estación de policía, Mariana no regresó a su casa a las '
  'seis de la tarde.',
  MOVIMIENTO),

 ('b05_telefono', 'Carlos',
  'Su teléfono móvil fue desconectado abruptamente tras recibir panfletos '
  'digitales del Bloque Central Renacer amenazándola para que «dejaran de '
  'escarbar el pasado».',
  'Su teléfono móvil fue desconectado abruptamente tras recibir panfletos '
  'digitales del Bloque Central Renacer amenazándola para que dejaran de '
  'escarbar el pasado.',
  CARTON),

 ('b06_fiscalia', 'Pilar',
  'La señora Rosa Elena acudió deshecha a la Fiscalía.',
  None,
  MOVIMIENTO),

 ('b07_mbu', 'Pilar',
  'En esta fase, el equipo misional debe actuar de inmediato: activa el '
  'Mecanismo de Búsqueda Urgente, de la Ley 971 de 2005, y simultáneamente '
  'la Alerta Rosa, de la Ley 2326 de 2023 y el Decreto 1428 de 2024.',
  'En esta fase, el equipo misional debe actuar de inmediato: activa el '
  'Mecanismo de Búsqueda Urgente, de la Ley novecientos setenta y uno de dos '
  'mil cinco, y simultáneamente la Alerta Rosa, de la Ley dos mil '
  'trescientos veintiséis de dos mil veintitrés y el Decreto mil '
  'cuatrocientos veintiocho de dos mil veinticuatro.',
  CARTON),

 ('b08_disposiciones', 'Pilar',
  'Disponiendo la difusión masiva multicanal, el rastreo de celdas y el '
  'ingreso obligatorio de la Información Ante Mortem en el Registro Nacional '
  'de Desaparecidos.',
  None,
  CIERRE),
]

CAPITULOS[3] = [
 ('b01_fricciones', 'Pilar',
  'La carpeta de investigación de Miriam y Mariana genera serias fricciones '
  'internas en la Fiscalía Seccional.',
  None,
  0.0),

 ('b02_falta_comunicacion', 'Pilar',
  'La falta de comunicación entre el Fiscal de conocimiento, los '
  'investigadores del CTI y el equipo de atención al usuario amenaza con '
  'paralizar el caso.',
  'La falta de comunicación entre el Fiscal de conocimiento, los '
  'investigadores del ce te í y el equipo de atención al usuario amenaza con '
  'paralizar el caso.',
  NORMAL),

 ('b03_trasvase', 'Carlos',
  'Además, un intento apresurado de trasvase administrativo del expediente '
  'hacia una unidad de delincuencia común provoca el traspapeleo temporal de '
  'los folios que contenían la sábana de celdas telefónicas y la entrevista '
  'clave del Testigo Protegido.',
  None,
  MOVIMIENTO),

 ('b04_asume', 'Pilar',
  'Ante el riesgo de impunidad y pérdida de memoria probatoria, la Fiscal '
  'Especializada en Desaparición Forzada asume la dirección estratégica de '
  'la investigación.',
  None,
  MOVIMIENTO),

 ('b05_roles', 'Pilar',
  'Reorganiza el equipo de trabajo definiendo con precisión los roles del '
  'Fiscal, Asistente, Investigador de Policía Judicial, Analista Criminal y '
  'Perito Forense.',
  None,
  CARTON),

 ('b06_ruta', 'Pilar',
  'Asimismo, establece la ruta de articulación interinstitucional con la '
  'Unidad de Búsqueda de Personas dadas por Desaparecidas, el Instituto '
  'Nacional de Medicina Legal y Ciencias Forenses y la Jurisdicción Especial '
  'para la Paz.',
  None,
  CARTON),

 ('b07_diferencia', 'Pilar',
  'Diferenciando la búsqueda humanitaria extrajudicial del proceso penal '
  'probatorio.',
  None,
  CIERRE),
]

CAPITULOS[4] = [
 ('b01_viacrucis', 'Carlos',
  'La señora Rosa Elena Morales vive un viacrucis institucional al acudir '
  'repetidamente a las dependencias judiciales en busca de noticias sobre '
  'sus dos hijas.',
  None,
  0.0),

 ('b02_ventanilla', 'Carlos',
  'Inicialmente es sometida a tratos fríos en ventanillas abiertas, '
  'interrogatorios intimidantes donde se le cuestiona la vida privada de sus '
  'hijas y cancelaciones de citas sin explicación.',
  None,
  NORMAL),

 ('b03_duelo', 'Carlos',
  'Esta violencia institucional sume a la madre en un profundo duelo '
  'suspendido e incertidumbre devastadora.',
  None,
  CARTON),

 ('b04_giro', 'Pilar',
  'El caso da un giro ético cuando la Fiscal Especializada aplica el '
  'Protocolo de Atención Digna con Enfoque Diferencial, Étnico e '
  'Interseccional y el principio de Acción Sin Daño.',
  None,
  MOVIMIENTO),

 ('b05_espacio', 'Pilar',
  'Se habilita un espacio privado y reservado para atender a Rosa Elena, se '
  'reconoce su condición de mujer buscadora afrodescendiente y de especial '
  'protección constitucional, y se le brinda contención psicosocial.',
  'Se habilita un espacio privado y reservado para atender a Rosa Elena, se '
  'reconoce su condición de mujer buscadora afrodescendiente y de especial '
  'protección constitucional, y se le brinda contención sicosocial.',
  NORMAL),

 ('b06_adn', 'Pilar',
  'Se procede a la toma científica de muestras biológicas de referencia para '
  'el Banco de ADN de la Fiscalía General de la Nación.',
  'Se procede a la toma científica de muestras biológicas de referencia para '
  'el Banco de a de ene de la Fiscalía General de la Nación.',
  CARTON),

 ('b07_canal', 'Pilar',
  'Y se establece un canal permanente de comunicación transparente, '
  'preparándola psicosocialmente para la notificación de avances y la '
  'eventual Entrega Digna de restos mortales.',
  'Y se establece un canal permanente de comunicación transparente, '
  'preparándola sicosocialmente para la notificación de avances y la '
  'eventual Entrega Digna de restos mortales.',
  CIERRE),
]

CAPITULOS[5] = [
 ('b01_articula', 'Pilar',
  'El equipo interdisciplinario articula la investigación tecnológica, la '
  'prospección geofísica y el análisis de contexto.',
  None,
  0.0),

 ('b02_cruce', 'Carlos',
  'El cruzamiento del Informe de Celdas con la declaración del Testigo, '
  'quien observó el camión de estacas azul en El Mirador y la omisión de la '
  'patrulla policial, permite delimitar la hipótesis espacial en el sector '
  'oriental de la Finca El Vergel.',
  None,
  MOVIMIENTO),

 ('b03_georradar', 'Carlos',
  'La inspección con georradar detecta una anomalía en la estratigrafía del '
  'suelo.',
  'La inspección con geo-rradar detecta una anomalía en la estratigrafía del '
  'suelo.',
  CARTON),

 ('b04_minnesota', 'Pilar',
  'Bajo los estándares del Protocolo de Minnesota, se ejecuta la exhumación '
  'arqueológico-forense.',
  None,
  MOVIMIENTO),

 ('b05_hallazgo', 'Pilar',
  'Hallando a 1.25 metros de profundidad el cuerpo en esqueletización de una '
  'mujer con ataduras de cuerda roja en las muñecas, trauma craneal por '
  'disparo de arma de fuego 9 milímetros y signos de cesárea o apertura '
  'traumática abdominal.',
  'Hallando a un metro veinticinco de profundidad el cuerpo en '
  'esqueletización de una mujer con ataduras de cuerda roja en las muñecas, '
  'trauma craneal por disparo de arma de fuego de nueve milímetros y signos '
  'de cesárea o apertura traumática abdominal.',
  NORMAL),

 ('b06_dictamenes', 'Pilar',
  'El Dictamen Antropológico establece el perfil biológico de mujer gestante '
  'y el Dictamen Genético confirma la coincidencia de ADN con Rosa Elena '
  'Morales con una probabilidad del 99.9999 por ciento.',
  'El Dictamen Antropológico establece el perfil biológico de mujer gestante '
  'y el Dictamen Genético confirma la coincidencia de a de ene con Rosa '
  'Elena Morales con una probabilidad del noventa y nueve coma nueve nueve '
  'nueve nueve por ciento.',
  CARTON),

 ('b07_matriz', 'Carlos',
  'Finalmente, el Analista de Contexto integra la Matriz, relacionando este '
  'hallazgo con otros cuerpos exhumados en la misma finca para demostrar la '
  'existencia de un patrón macrocriminal de ejecución y disposición '
  'clandestina de cadáveres operado por el Bloque Central Renacer en '
  'connivencia con agentes locales.',
  None,
  MOVIMIENTO),

 ('b08_informe', 'Carlos',
  'El Fiscal consolida el caso redactando el Informe Integral de '
  'Esclarecimiento en 20 Numerales.',
  'El Fiscal consolida el caso redactando el Informe Integral de '
  'Esclarecimiento en veinte numerales.',
  CIERRE),
]


def bloques(cap):
    """Devuelve [(id, voz, texto_verbatim, texto_tts, pausa_antes)]."""
    return [(i, v, t, (s if s is not None else t), p)
            for i, v, t, s, p in CAPITULOS[cap]]


def palabras(cap):
    return sum(len(t.split()) for _, _, t, _, _ in CAPITULOS[cap])


if __name__ == '__main__':
    tot = 0
    print('%-4s %-8s %-7s %-9s %s' % ('cap', 'bloques', 'palabras', 'duracion',
                                      'voces'))
    for c in sorted(CAPITULOS):
        n = palabras(c)
        pausas = sum(p for _, _, _, _, p in CAPITULOS[c])
        seg = n / 142.0 * 60 + pausas
        tot += seg
        vs = sorted({v for _, v, _, _, _ in CAPITULOS[c]})
        print('%-4d %-8d %-7d %6.1f s   %s'
              % (c, len(CAPITULOS[c]), n, seg, ','.join(vs)))
    print('')
    print('narracion de los cinco: %.1f s = %d:%02d'
          % (tot, int(tot // 60), int(tot % 60)))
    print('mas envoltorio (intro 182 + entrada 119 + cierre 119 + outro 182 '
          'por pieza) = %.1f s' % (tot + 5 * (182 + 119 + 119 + 182) / 23.976))
