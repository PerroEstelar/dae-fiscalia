# -*- coding: utf-8 -*-
r"""UNIDAD 4 · Caso de análisis 3 · 4 ranuras · pieza 1460. Narra Carlos.

LO QUE SE OYE ENCIMA (cruce_lp.json)
    r01  Una ciudadana de 28 años denuncia VIF sistemática en concurso con
         lesiones personales dolosas simples contra su cónyuge
    r02  la víctima asiste al despacho del fiscal con un abogado del
         consultorio jurídico de una universidad: desea desistir
    r03  además pide formalizar un acuerdo de mediación y el archivo
    r04  alegando que su esposo se disculpó, prometió terapia de pareja, y
         que ella depende económicamente de él

CUATRO RANURAS LARGAS PARA UNA PIEZA CORTA
    Cada una lleva su inserto de detalle (V3) para que la pieza respire:
    la firma de la denuncia, la carpeta del consultorio, la solicitud que
    cruza el escritorio. El cuarto (las manos con el anillo) se pidio dos
    veces y las dos salio con DOS anillos, uno a medio sacar: se lee como que
    ella se quita la argolla, que es lo contrario de lo que el caso cuenta.
    Fuera; la r04 queda sola. (Antes era un telefono con un mensaje, que
    insinuaba como llego la disculpa y el expediente no lo dice.) El esposo no está en el despacho y no se
    dibuja. El fiscal todavía no decide: se le ve de espaldas, sobre el
    hombro. El acento mostaza es de la ciudadana: su cárdigan.
"""

R = {}

R[1] = (249, 'dia', ('ciudadana',), None, False, 'ventanilla', '''
Medium shot of %(ciudadana)s at the complaints counter of a prosecution
office, three-quarter view, the camera at standing height, perfectly level.
Mid-action: she slides a filled complaint form under the low opening of the
glass with one hand, the other hand holding her handbag strap tight, her
eyes on the form. Fluorescent light. She is ALONE on her side of the glass.
''')

R[2] = (244, 'dia', ('ciudadana', 'estudiante', 'fiscal_sin_cara'), None, False, 'despacho', '''
Over-the-shoulder shot from behind %(fiscal_sin_cara)s at his desk, the camera
at seated height, perfectly level. Across the desk, in two plain visitor
chairs: %(ciudadana)s, her hands clasped in her lap, eyes down; beside her,
%(estudiante)s speaks, leaning slightly forward, his grey folder open on his
knees. Daylight from the window.
''')

# 3 nov, revision de Sebastian: «hand anatomically incorrect». La primera
# placa traia el brazo entrando por la esquina superior y la mano de plano
# hacia la camara, con dos dedos visibles y sin pulgar. Se vuelve a pedir con
# una pose que se dibuja bien: camara a la altura de la mesa, de lado, la mano
# entra por el borde derecho, palma abajo, los cuatro dedos juntos y planos
# sobre la hoja y el pulgar visible a un lado, empujando hacia la izquierda.
R[3] = (128, 'dia', ('estudiante',), None, False, 'despacho', '''
Close shot at desk height, the camera level with the desktop and looking
across it from the side. From the RIGHT edge of the frame a young man's right
hand and forearm enter, the cuff of a plain light grey shirt under a dark grey
sweater: the hand is PALM DOWN, flat on a single written request, its four
fingers together, straight and side by side, the thumb resting visibly along
the near edge of the sheet, and it pushes the sheet slowly to the LEFT across
the desk toward a thick closed case folder. The hand is drawn with correct,
simple anatomy: exactly five fingers of natural length, the back of the hand
and the knuckles facing the viewer, nothing hidden or bent oddly. The request
carries only plain grey bars. Only the hand, the sleeve and the desk; no face,
no second hand. Daylight from one side.
''')

R[4] = (189, 'dia', ('ciudadana',), None, False, 'despacho', '''
Close shot of %(ciudadana)s seated in the visitor chair, from the chest up,
three-quarter view, the camera at her eye level, perfectly level. She looks
down at her own hands in her lap, turning a plain wedding ring on her finger,
her mouth a straight line. Behind her, soft and out of focus, the office
wall. She is ALONE in the frame and appears ONCE.
''')

NOMBRE = {1: 'la_denuncia', 2: 'el_despacho', 3: 'la_solicitud',
          4: 'el_anillo'}

CON_PERSONA = {1, 2, 3, 4}
SILUETAS = set()
CARTONES = {1, 2, 3, 4}
CENITALES = set()
SOLO_MANOS = {3}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
PIEZA = 1460
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['ciudadana'], 2: ['ciudadana', 'estudiante'], 4: ['ciudadana']}

ANCLA = 'LP_U4C3_r02_el_despacho'
REF_PLACA = {
 2: (['LP_U4C1_r01_la_noticia'], 'lugar', ''),
 1: ([ANCLA], 'estilo', ''),
 3: ([ANCLA], 'lugar', ''),
 4: ([ANCLA], 'lugar', ''),
}

REUSA = {}

DET = {
 (1, 'la_firma'): dict(cuadros=80, entra=150,
     registro='dia',
     personas=('ciudadana',),
     escena='Extreme close shot of a woman\'s hand signing the bottom of a '
            'plain complaint form with a plain pen, the cuff of a plain matte '
            'mustard-yellow knitted cardigan at the wrist; the form carries '
            'only plain grey bars. Fluorescent light.',
     gesto='The pen finishes the signature in one slow stroke and lifts off '
           'the paper. Nothing else moves.'),
 (2, 'la_carpeta'): dict(cuadros=72, entra=150,
     registro='dia',
     personas=('estudiante',),
     escena='Extreme close shot of a plain grey folder open on a young man\'s '
            'knees, his fingers holding a page of plain grey bars, the cuff of '
            'a plain light grey shirt under a dark grey sweater.',
     gesto='The fingers turn the page slowly and flatten it. Nothing else '
           'moves.'),
}

BROLL = {}

MOV = {
 2: 'kling: el estudiante habla y pasa una hoja; ella no levanta la vista',
}

LOWER_THIRD = {}


def comprobar():
    fallos = []
    tot = sum(v[0] for v in R.values())
    if sorted(R) != list(range(1, len(NOMBRE) + 1)):
        fallos.append('faltan ranuras')
    if tot != TOTAL:
        fallos.append('los cuadros suman %d y la rejilla dice %d' % (tot, TOTAL))
    racha = mejor = 0
    for i in sorted(R):
        racha = 0 if i in CON_PERSONA else racha + 1
        mejor = max(mejor, racha)
    if mejor > TOPE_SIN_GENTE:
        fallos.append('%d ranuras seguidas sin gente' % mejor)
    if len(CENITALES) > 3:
        fallos.append('%d cenitales' % len(CENITALES))
    return fallos, tot, mejor
