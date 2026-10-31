# -*- coding: utf-8 -*-
r"""UNIDAD 5 «La decisión integral y el giro» · 13 ranuras · pieza 3504.

LO QUE SE OYE ENCIMA (cruce_dh.json)
    Parte A «El cierre»
    r01     Julian: el estado del caso
    r02     Sandra: los elementos de prueba
    r03     Andres, por altavoz: no hay conexas sin asignar
    r04     Quintero: «Hoy cerramos… todo coherente»
    r05-07  voz en off: la decision integral y la prueba de coherencia
    Parte B «El giro»
    r08     Julian: el comerciante se retracta
    r09     Carmen Elisa, por altavoz: otro mensaje
    r10     Quintero le responde
    r11-13  Quintero: reponderar, tres preguntas, las tareas

UNA ESCENA: el despacho de la U2 al final de la tarde (r01 ANCLA, con la
U2 r01 como referencia del lugar). La luz baja por la ventana; el reloj de
pared sin numeros marca las cinco y cuarenta en la r08. La silla vacia de
la r05 es la misma idea de la U2 r25: la del participante.

QUIEN NO SE VE
    Andres y Carmen Elisa solo se oyen, por el altavoz (el guion: «solo
    voz»). No hay acento en esta pieza: ella no esta. El contenido del
    mensaje no se muestra.
"""

TARDE = ('Late afternoon: low warm sunlight comes in through the wide window '
         'behind the desk, long soft shadows across the room; the slopes '
         'outside are turning dark.')

R = {}

R[1] = (299, 'contraluz', ('quintero', 'julian', 'sandra'), False, False, 'despacho', '''
Medium-wide shot of the prosecutor's office at the end of the afternoon, the
camera at standing height near the door, perfectly level. Mid-action:
%(julian)s stands at the end of the small meeting table reading aloud from a
single sheet he holds in both hands; %(quintero)s sits at the head of the
table with the complete case file in front of her, a thick stack held with a
black binder clip, her reading glasses on; %(sandra)s sits at the side of the
table with her dark notebook. The wide window behind them is the brightest
thing in the room. ''' + TARDE + '\n')

R[2] = (262, 'dia', ('sandra',), False, False, 'despacho', '''
Medium shot of %(sandra)s seated at the meeting table in the prosecutor's
office, from the waist up, in three-quarter view, the camera at seated height
across the table, perfectly level. Mid-action: she lays the fourth of four
items in a row on the table in front of her -a thin grey report folder, a
small sealed cardboard evidence box with a blank tag, a clear bag with a
folded blank sheet, and a phone sealed in a clear evidence bag- speaking as
she does it. Low warm afternoon light from the window on one side.
''')

R[3] = (120, 'dia', ('quintero',), False, False, 'despacho', '''
Close shot at table height of a plain desk telephone on the meeting table,
its speaker on: one small plain round light on it is lit, and nothing else on
it carries any mark. A woman's hand, the cuff of a plain charcoal grey blazer
at the wrist, rests beside it on the table. Low warm afternoon light from the
window. No face in frame.
''')

R[4] = (272, 'dia', ('quintero',), False, False, 'despacho', '''
Medium-close shot of %(quintero)s seated at the head of the meeting table,
from the chest up, frontal, the camera at seated height, perfectly level.
Mid-action: she speaks to her team, one hand flat on the closed case file in
front of her, her reading glasses in the other hand, her eyes moving from one
to the other. Low warm afternoon light from the window behind her and to one
side. She is ALONE in the frame and appears ONCE; nobody else is visible.

Her state: decisive, calm; everything has to hold together.
''')

R[5] = (183, 'dia', (), False, False, 'despacho', '''
Medium shot of the meeting table in the prosecutor's office, the camera at
seated height, perfectly level, looking at an EMPTY chair pulled back from
the table at its near side. On the table in front of the empty chair, four
plain closed folders lie side by side in a neat row, nothing written on them,
and a plain pen beside them. Low warm afternoon light from the window lays
long soft shadows across the table and the chair.

What the camera asserts: this place is yours.
''')

R[6] = (182, 'dia', (), False, False, 'despacho', '''
(reusa r05: las cuatro carpetas, mas cerca)
''')

R[7] = (262, 'dia', ('quintero',), False, False, 'despacho', '''
Close shot at table height of the meeting table, the camera low and level.
Mid-action: a woman's two hands, the cuffs of a plain charcoal grey blazer at
the wrists, square two plain closed folders together edge to edge on the
table, so that they line up exactly; the folders never leave the table. Low
warm afternoon light from the window. No face in frame.
''')

R[8] = (270, 'contraluz', ('julian', 'quintero'), False, False, 'despacho', '''
Medium-wide shot of the prosecutor's office at dusk, the camera at seated
height from the meeting table, perfectly level. Mid-action: %(julian)s comes
in through the open door holding a single sheet of paper, mid-step; at the
table %(quintero)s looks up at him. On the wall beside the door, the plain
round clock with NO numerals shows its two hands at twenty to six. The window
is a pale band of evening sky; the room is dimmer now.
''')

R[9] = (186, 'dia', ('quintero',), False, False, 'despacho', '''
Close shot at table height of a mobile phone lying face up on the meeting
table, its screen lit with only a plain grey rectangle, nothing legible.
Mid-action: a woman's forefinger, the cuff of a plain charcoal grey blazer at
the wrist, touches the lower edge of the screen to turn on the speaker. The
phone never leaves the table. Evening light, dim. No face in frame.
''')

R[10] = (175, 'dia', ('quintero', 'sandra'), False, False, 'despacho', '''
Close-up of %(quintero)s leaning toward the phone on the table, face and
shoulders, in three-quarter view, the camera at seated height, perfectly
level. Mid-action: she speaks toward the phone, calm and firm; behind her, out
of focus, %(sandra)s already stands up, her own phone in her hand. Dim
evening light from the window.

Her state: steady; acting at once.
''')

R[11] = (191, 'contraluz', ('quintero',), False, False, 'despacho', '''
Medium shot of %(quintero)s standing at the wide window of her office at
dusk, turning from the window toward the room, from the waist up, the camera
at standing height inside the room, perfectly level. The pale evening sky in
the window is the only bright thing; she reads mostly as silhouette and
edge, her face half lit. She is ALONE in the room and appears ONCE.

Her state: thinking it through again, not starting over.
''')

R[12] = (199, 'dia', ('julian', 'sandra'), False, False, 'despacho', '''
Medium two-shot of %(julian)s and %(sandra)s seated at the meeting table,
from the waist up, the camera at seated height across the table, perfectly
level. Mid-action: both look up toward someone standing off frame, listening;
Julian holds his pencil over his notebook, Sandra her phone in her hand. Dim
evening light from the window.
''')

R[13] = (253, 'contraluz', ('quintero', 'julian', 'sandra'), False, False, 'despacho', '''
Medium-wide shot of the prosecutor's office at dusk, the camera at standing
height near the door, perfectly level. Mid-action: the team moves at once:
%(julian)s gets up from the table with his notebook, %(sandra)s stands with
her phone at her ear, and %(quintero)s stands at the head of the table, one
hand on the case file. The evening window behind them is the only bright
thing; the desk lamp is on.

What the camera asserts: the case is not over; the work goes on.
''')

NOMBRE = {1: 'el_estado_del_caso', 2: 'los_elementos', 3: 'el_altavoz',
          4: 'hoy_cerramos', 5: 'la_silla_vacia', 6: 'la_silla_vacia_b',
          7: 'coherencia', 8: 'julian_entra', 9: 'el_celular',
          10: 'gracias_por_avisar', 11: 'reponderar', 12: 'el_equipo',
          13: 'se_abre_hoy'}

REUSA = {
 6: (5, dict(encuadre=0.7, empuje=0.04, centro=[0.5, 0.55])),
}

CON_PERSONA = {1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13}
SILUETAS = set()
CARTONES = set(range(1, 14))
CENITALES = set()
SOLO_MANOS = {3, 7, 9}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
PIEZA = 3504
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['quintero', 'julian', 'sandra'], 2: ['sandra'], 4: ['quintero'],
         8: ['julian', 'quintero'], 10: ['quintero', 'sandra'],
         11: ['quintero'], 12: ['julian', 'sandra'],
         13: ['quintero', 'julian', 'sandra']}

DESPACHO_U2 = 'DH_U2_r01_el_escrito'
ANCLA5 = 'DH_U5_r01_el_estado_del_caso'
REF_PLACA = {
 1: ([DESPACHO_U2], 'lugar', 'It is now the END OF THE AFTERNOON: low warm light. '),
}
for _n in (2, 3, 4, 5, 7, 9, 10, 12):
    REF_PLACA[_n] = ([ANCLA5], 'lugar', '')
for _n in (8, 11, 13):
    REF_PLACA[_n] = ([ANCLA5], 'lugar', 'It is now DUSK: the window is a pale band of evening sky and the room is dimmer. ')

DET = {
 (4, 'la_mano_en_el_expediente'): dict(cuadros=72, entra=110, registro='dia',
     personas=('quintero',),
     escena='Extreme close shot of a woman\'s hand resting flat on a closed '
            'thick case file held with a black binder clip, the cuff of a '
            'plain charcoal grey blazer at the wrist, warm low light.',
     gesto='The fingers press very slightly on the file and relax. The file '
           'does not move. Nothing else moves.'),
 (12, 'el_lapiz'): dict(cuadros=60, entra=80, registro='dia',
     personas=('julian',),
     escena='Extreme close shot of a young man\'s hand holding a plain pencil '
            'above an open notebook with grey bars, the cuff of a light grey '
            'shirt under a dark grey knitted vest, dim evening light.',
     gesto='The pencil tip lowers to the page and rests on it, without '
           'writing. Nothing else moves.'),
}

BROLL = {}

MOV = {
 8: 'kling: Julián da un paso adentro con la hoja; Quintero levanta la cabeza',
 13: 'kling: Julián se levanta y sale; Sandra al teléfono',
 5: 'camara de la casa (empuje lento), sin modelo',
}

LOWER_THIRD = {1: 'Julián Mora', 2: 'Sandra Ibáñez', 4: 'Marina Quintero'}


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
    for n, (m, _c) in REUSA.items():
        if m in REUSA or m not in R:
            fallos.append('r%02d reusa r%02d, que no es placa madre' % (n, m))
    return fallos, tot, mejor
