# -*- coding: utf-8 -*-
r"""UNIDAD 4 · Caso de análisis 1 · 6 ranuras · pieza 1879. Narra Carlos.

LO QUE SE OYE ENCIMA (cruce_lp.json)
    r01  Un fiscal local de Bogotá recibe una noticia criminal por inasistencia
         alimentaria (art. 233 del CP),
    r02  cometido presuntamente por un ciudadano de 35 años contra su hijo
         menor de edad
    r03  el fiscal decide, para agilizar y resolver de forma expedita,
    r04  fijar fecha para diligencia de conciliación con el formato
         FGN-MP02-F-10
    r05  la defensa presenta recusación contra el fiscal y nulidad en la
         audiencia concentrada
    r06  con el argumento de que la inasistencia alimentaria no es querellable
         y exigir conciliación obligatoria vulnera el debido proceso

QUIÉN LLEVA CARA
    El fiscal decide mal (cita a conciliación lo que no es querellable): sin
    cara, de espaldas, sobre el hombro y manos (regla de la serie). El
    ciudadano se presume inocente: de espaldas. El niño no se dibuja: está
    su morral. La defensa sí lleva cara.
"""

R = {}

R[1] = (198, 'dia', ('fiscal_sin_cara',), None, False, 'despacho', '''
Over-the-shoulder shot from behind %(fiscal_sin_cara)s seated at his desk in a
prosecutor's office in Bogota, the camera at seated height, perfectly level.
Mid-action: from the right edge, a clerk's hand in a plain grey sleeve sets
down a new plain case folder on the desk in front of him, and his own hand is
already resting flat on it. Through the window beyond the desk: red-brown
brick buildings and the steep green eastern hills of Bogota under low grey
cloud.
''')

R[2] = (154, 'dia', ('indiciado',), None, False, 'calle_bogota', '''
Wide shot of a Bogota street on a grey morning, the camera at standing height
on the pavement, perfectly level. In the middle distance, %(indiciado)s walks
away from the camera along the pavement, hands in his pockets, seen from
behind. In the near foreground on the left, inside the half-open door of a
brick house, a small child's school backpack hangs alone from a plain hook.
No child in the frame.
''')

R[3] = (176, 'dia', ('fiscal_sin_cara',), None, False, 'despacho', '''
Close shot over the shoulder of %(fiscal_sin_cara)s at his desk: the open case
folder, and beside it a plain desk calendar of plain empty squares with no
numerals; his hand holds a plain pen above one empty square, about to mark a
date. Only his shoulder, his forearm and his hand; no face. Daylight from the
window.
''')

R[4] = (253, 'dia', ('fiscal_sin_cara',), None, False, 'despacho', '''
Overhead shot looking straight down at the desk: a one-page institutional
form lies in the middle, its boxes and lines drawn only as plain grey bars
and empty rectangles, nothing legible; a man's hand in a plain charcoal
jacket sleeve is filling in one of the boxes with a plain pen. Beside it the
open case folder and a plain rubber stamp lying on its side. Daylight from
one side.
''')

R[5] = (224, 'dia', ('defensor', 'indiciado'), None, False, 'sala', '''
Medium-wide shot of a concentrated hearing in a Colombian hearing room, the
camera at standing height from the side, perfectly level. Mid-action:
%(defensor)s stands at the defence table, presenting a plain written motion
held in one hand, the other hand open toward the judge's desk; seated beside
him, %(indiciado)s is seen from behind. Daylight from high windows.
''')

R[6] = (224, 'dia', ('defensor',), None, False, 'sala', '''
Medium-close shot of %(defensor)s standing at the defence table, from the
chest up, three-quarter view, the camera at his eye level, perfectly level.
Mid-argument: he holds a single sheet -the conciliation summons- up in one
hand and taps it once with two fingers of the other, his mouth half open
mid-word. Behind him, soft and out of focus, the hearing room. He is ALONE in
the frame and appears ONCE.
''')

NOMBRE = {1: 'la_noticia', 2: 'el_morral', 3: 'la_fecha',
          4: 'el_formato', 5: 'la_recusacion', 6: 'no_es_querellable'}

CON_PERSONA = {1, 2, 3, 4, 5, 6}
SILUETAS = set()
CARTONES = {1, 2, 4, 5, 6}
CENITALES = {4}
SOLO_MANOS = {3, 4}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
PIEZA = 1879
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {5: ['defensor'], 6: ['defensor']}

ANCLA = 'LP_U4C1_r01_la_noticia'
REF_PLACA = {
 1: (['LP_U2C1_r01_la_calle_de_bodegas'], 'estilo', ''),
 2: ([ANCLA], 'estilo', ''),
 3: ([ANCLA], 'lugar', ''),
 4: ([ANCLA], 'lugar', ''),
 5: ([ANCLA], 'estilo', ''),
 6: (['LP_U4C1_r05_la_recusacion'], 'lugar', ''),
}

REUSA = {}

DET = {}

BROLL = {}

MOV = {
 1: 'kling: la mano deja la carpeta y se retira; la de el se queda sobre ella',
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
