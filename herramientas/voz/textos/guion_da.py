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
