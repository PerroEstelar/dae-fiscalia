# -*- coding: utf-8 -*-
r"""SITUACIÓN 08 · Bajo custodia policial · 7 ranuras · 880 cuadros.
Narra Carlos.

LO QUE SE OYE ENCIMA
    r01      la Fiscalía investiga la muerte de una persona que permanecía
             bajo custodia policial
    r02      los familiares denuncian que la víctima había sufrido agresiones
             durante su detención
    r03-r04  también aportan un video publicado en redes sociales, | en el que
             presuntamente se observan algunas de esas agresiones
    r05-r06  se identifica que existen inconsistencias | entre lo registrado
             por las autoridades policiales y los hallazgos médico-legales
    r07      el fiscal debe determinar qué instrumentos internacionales
             pueden orientar las actuaciones

LO QUE NO SE DIBUJA
    Ni la detención, ni las agresiones, ni lo que muestra el video: en la
    pantalla solo hay una mancha gris borrosa. Los patrulleros (de quienes se
    sospecha) van de espaldas, con el uniforme de la Policía Nacional (regla
    del 4 nov). La persona que murió no se dibuja: su buzo mostaza, devuelto
    en una bolsa transparente, es el acento (r02).
"""

R = {}

R[1] = (118, 'hero', ('patrullero',), None, False, 'estacion_noche', '''
Wide shot of the neighbourhood police station at night, the camera across
the street at standing height, perfectly level. The plain two-storey building
of rendered concrete with its lit plain doorway; a plain white pickup truck
with no markings parked in front; the wet pavement reflecting the white
street lamp. In the lit doorway, small, %(patrullero)s stands with his back
to the camera. Everything outside the light falls into deep grey darkness.
''')

R[2] = (127, 'dia', ('madre_s08', 'hermana', 'fiscal_s08'), 'buzo', False, 'despacho', '''
Over-the-shoulder shot from BEHIND the prosecutor at his desk, the camera at
seated height, perfectly level. In the left foreground, the back of his head
and his grey-suited shoulder, filling the left third of the frame. Across the
desk sit %(madre_s08)s and %(hermana)s. The mother holds on her lap a clear
plastic bag with a folded matte mustard-yellow hooded sweatshirt inside, both
hands on it; the sister speaks, mid-sentence, her eyes on the prosecutor.
Each person appears ONCE.
''')

R[3] = (105, 'dia', ('hermana', 'fiscal_s08'), None, False, 'despacho', '''
Medium shot across the prosecutor's desk, the camera at seated height from
the side, perfectly level. %(hermana)s, in profile facing right, holds her
mobile phone out across the desk with its screen turned toward
%(fiscal_s08)s, who leans forward in three-quarter view to look at it, his
brows drawn together. The screen glows plain grey. Each person appears ONCE.
''')

R[4] = (96, 'dia', ('fiscal_s08',), None, False, 'despacho', '''
Extreme close shot of a plain mobile phone held in a man's hand in a grey
suit cuff, the camera at the height of the phone, perfectly level. The screen
shows a dark, heavily blurred video frame: a dim grey corridor with vague
indistinct shapes, nothing readable, no face, no figure clear; below it a
plain grey progress bar. Exactly one hand.
''')

R[5] = (114, 'dia', ('investigadora_s08', 'patrullero'), None, False, 'estacion_dentro', '''
Medium shot at the front desk of the police station, the camera at standing
height, perfectly level. %(investigadora_s08)s stands at the counter in
three-quarter view, the thick plain bound logbook open in front of her, her
finger on one line of plain grey bars, her eyes lifted toward the other side
of the counter, where %(patrullero)s stands with his back to the camera.
Flat fluorescent light. Each person appears ONCE.
''')

R[6] = (147, 'dia', ('fiscal_s08',), None, False, 'despacho', '''
Overhead shot looking STRAIGHT DOWN at the prosecutor's plain grey desk, the
camera square to the desk. Side by side in the middle: on the left, a
photocopy of a ruled logbook page with lines of plain grey bars; on the right,
a stapled medical-legal report of plain grey bars with a plain grey round
stamp. His two hands in grey suit cuffs rest one on each document. Nothing
else on the desk.
''')

R[7] = (173, 'contraluz', ('fiscal_s08',), None, False, 'despacho', '''
Medium shot of %(fiscal_s08)s standing at a plain shelf by the window of his
office, three-quarter view, the camera at standing height, perfectly level.
From a row of thin plain booklets with blank grey covers he has taken one and
holds it open in both hands, reading, his head bent. The bright window beside
him; he is in soft shadow. He appears ONCE.
''')

NOMBRE = {1: 'la_estacion', 2: 'la_denuncia', 3: 'el_telefono',
          4: 'el_video', 5: 'el_libro_de_minuta', 6: 'las_inconsistencias',
          7: 'los_protocolos'}

CON_PERSONA = set(R)
SILUETAS = {1, 5}
CARTONES = {1, 2, 4, 6, 7}
CENITALES = {6}
SOLO_MANOS = {4, 6}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
TOTAL = 880
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {2: ['madre_s08', 'hermana'], 3: ['hermana', 'fiscal_s08'],
         7: ['fiscal_s08']}

ANCLAS = {1, 2, 5}

REF_PLACA = {
 1: (['EI_ANCLA_noche_ext'], 'estilo', ''),
 2: (['EI_ANCLA_oficina'], 'estilo', ''),
 5: (['EI_ANCLA_recepcion'], 'estilo', ''),
 3: (['EI_S08_r02_la_denuncia'], 'lugar', 'It is the SAME office, the SAME sister and the SAME prosecutor. '),
 4: (['EI_S08_r02_la_denuncia'], 'lugar', ''),
 6: (['EI_S08_r02_la_denuncia'], 'lugar', ''),
 7: (['EI_S08_r02_la_denuncia'], 'lugar', 'It is the SAME office. '),
}

REUSA = {}
DET = {}
BROLL = {}

MOV = {
 1: 'kling: el patrullero entra por la puerta; el reflejo en el piso mojado',
 2: 'kling: la hermana habla; la madre aprieta la bolsa',
 3: 'kling: el fiscal se inclina hacia la pantalla',
 5: 'kling: la investigadora levanta la vista del libro',
 7: 'kling: el fiscal pasa una página del folleto y levanta la vista',
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
    if set(LOWER_THIRD) & CARTONES:
        fallos.append('rotulo y carton en la misma ranura')
    for (n, _), d in DET.items():
        if (d['entra'] < 60 and not d.get('abre')) or d['entra'] + d['cuadros'] > R[n][0]:
            fallos.append('detalle r%02d fuera de su ranura' % n)
    return fallos, tot, mejor
