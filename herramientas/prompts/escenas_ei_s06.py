# -*- coding: utf-8 -*-
r"""SITUACIÓN 06 · La muerte de dos jóvenes · 9 ranuras · 1088 cuadros.
Narra Carlos.

LO QUE SE OYE ENCIMA
    r01      la Fiscalía recibe información sobre la muerte de dos jóvenes
             durante una operación militar en una zona rural
    r02-r03  según el informe de la unidad que participó en el operativo, |
             los jóvenes pertenecían a una organización armada y murieron
             durante un enfrentamiento
    r04-r05  sin embargo, sus familiares manifiestan que ambos habían |
             salido de sus viviendas para asistir a una entrevista de trabajo
    r06      un testigo afirma haberlos visto ingresar a un vehículo militar
    r07-r08  la documentación médico-legal identifica lesiones cuya
             localización y características | podrían resultar incompatibles
             con la versión operacional
    r09      el fiscal del caso debe determinar las actuaciones

LO QUE NO SE DIBUJA (biblia §3: el hecho debatido no se ilustra)
    Ni el enfrentamiento del informe, ni la salida de los jóvenes, ni su
    subida al vehículo militar: son las versiones que el caso contrasta. Se
    dibuja la actuación: el informe que llega, la madre que trae la hoja de
    vida, el testigo que señala el camino VACÍO, la médica que compara. Los
    militares no se dibujan (camiones lejos, una manga verde oliva lisa).
    Los jóvenes tampoco: su ausencia es la chaqueta mostaza en la percha.
"""

R = {}

R[1] = (156, 'dia', (), None, False, 'montana', '''
Very wide shot of a rural valley in the Colombian mountains at dawn, the
camera high on a hillside, perfectly level. Steep green slopes with patches
of forest, low mist in the folds of the hills, a river; far below, on the
winding unpaved road along the valley floor, two plain olive-green military
trucks with canvas covers drive in a line, tiny in the frame, no people
visible. No flag, no marking.
''')

R[2] = (99, 'dia', ('manga_militar', 'fiscal_s06'), None, False, 'despacho', '''
Close shot at desk height, perfectly level: %(manga_militar)s sets down a
thick bound report with a plain grey cover onto the prosecutor's plain grey
desk; from the other side, two hands in white shirt cuffs reach for it. The
cover is completely plain. Exactly three hands. No face.
''')

R[3] = (135, 'dia', ('fiscal_s06',), None, False, 'despacho', '''
Medium shot of %(fiscal_s06)s at his desk, frontal three-quarter, the camera
at his seated eye level, perfectly level. He reads the open bound report held
in both hands, glasses on, his brows drawn together; its pages are only plain
grey bars. Behind him a window onto the green hills of a regional city and
metal shelving with cardboard folders. He appears ONCE.
''')

R[4] = (80, 'dia', ('madre_s06', 'padre_s06', 'fiscal_s06'), None, False, 'despacho', '''
Over-the-shoulder shot from BEHIND the prosecutor at his desk, the camera at
seated height, perfectly level. In the right foreground, the back of his head
and his white-shirted shoulder, filling the right third of the frame. Across
the desk, %(madre_s06)s speaks, mid-sentence, and with one hand slides a clear
plastic sleeve with a single sheet inside -only plain grey bars- across the
desk toward him; beside her sits %(padre_s06)s, his hat in his hands, eyes
down. Each person appears ONCE.
''')

R[5] = (83, 'contraluz', ('madre_s06',), 'chaqueta', False, 'casa_pueblo', '''
Medium shot inside the small family home, the camera at standing height,
perfectly level, looking toward the open front door. %(madre_s06)s stands in
the doorway with her back to the camera, a dark shape against the bright
empty street outside, her hand on the door frame. On the plain wooden peg on
the wall beside the door hangs one matte mustard-yellow cotton jacket, alone.
Nobody else; the street outside is empty. She appears ONCE.
''')

R[6] = (148, 'dia', ('testigo', 'investigador'), None, False, 'tienda', '''
Medium-wide shot of the roadside shop by day, the camera at standing height
beside the road, perfectly level. Behind his wooden counter, %(testigo)s
talks to %(investigador)s, who stands at the counter in three-quarter back
view writing in his notebook; the old man raises his right arm and points out
along the EMPTY unpaved road that runs past the shop into the hills, his
mouth open mid-word. Nobody on the road. Each person appears ONCE.
''')

R[7] = (129, 'dia', ('medica',), None, False, 'medicina_legal', '''
Medium shot of %(medica)s at her desk in the forensic office, frontal
three-quarter, the camera at her seated eye level, perfectly level. She reads
a stapled report held up in her left hand, its pages only plain grey bars,
her pen in her right hand; behind her, a plain bare pale-grey wall with
nothing on it (5 nov: la caja de luz con radiografias mostraba costillas -ningun
cuerpo ni hueso-; placa rehecha). Flat white light. She appears ONCE.
''')

R[8] = (125, 'dia', ('medica',), None, False, 'medicina_legal', '''
Close shot at desk height, perfectly level, of two documents lying side by
side on the desk: on the left the thick bound report with its plain grey
cover, open; on the right a stapled report of plain grey bars. Her right
index finger rests on one line of the stapled report while her left hand
holds the bound report open at a page. White lab coat cuffs. Exactly two
hands. No face. Flat white light.
''')

R[9] = (133, 'contraluz', ('fiscal_s06',), None, False, 'despacho', '''
Medium-close shot of %(fiscal_s06)s at his desk at the end of the day,
three-quarter view, the camera at his seated eye level, perfectly level. In
front of him lie the bound report, the clear plastic sleeve and the stapled
report. He has just taken off his glasses and holds them in his hand, looking
up and away, thinking. The window behind him bright with a plain overcast
neutral grey sky over the hills (5 nov: «last light» dio un cielo rosado de
atardecer; placa rehecha); his face in soft shadow. He appears ONCE.
''')

NOMBRE = {1: 'la_operacion', 2: 'el_informe', 3: 'la_lectura',
          4: 'la_hoja_de_vida', 5: 'la_chaqueta', 6: 'el_testigo',
          7: 'la_medica', 8: 'las_dos_versiones', 9: 'el_fiscal'}

CON_PERSONA = set(R) - {1}
SILUETAS = set()
CARTONES = {1, 3, 5, 6, 8, 9}
CENITALES = set()
SOLO_MANOS = {2, 8}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
TOTAL = 1088
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {3: ['fiscal_s06'], 4: ['madre_s06'], 5: ['madre_s06'], 9: ['fiscal_s06']}

ANCLAS = {1, 3, 5, 6, 7}

REF_PLACA = {
 1: (['EI_ANCLA_rural'], 'estilo', ''),
 3: (['EI_ANCLA_oficina'], 'estilo', ''),
 5: (['EI_ANCLA_noche_int'], 'estilo', ''),
 6: (['EI_ANCLA_rural'], 'estilo', ''),
 7: (['EI_ANCLA_recepcion'], 'estilo', ''),
 2: (['EI_S06_r03_la_lectura'], 'lugar', ''),
 4: (['EI_S06_r03_la_lectura'], 'lugar', 'It is the SAME office and the SAME prosecutor. '),
 8: (['EI_S06_r07_la_medica'], 'lugar', ''),
 9: (['EI_S06_r03_la_lectura'], 'lugar', 'It is the SAME office and the SAME prosecutor, at the end of the day. '),
}

REUSA = {}
DET = {}
BROLL = {}

MOV = {
 1: 'kling: los camiones avanzan por la carretera del valle; la niebla se mueve',
 4: 'kling: la madre habla y empuja la funda hacia él (boca)',
 6: 'kling: el testigo habla y señala el camino vacío',
 7: 'kling: la médica levanta la mirada del informe hacia la caja de luz',
 9: 'kling: el fiscal se quita las gafas y mira lejos',
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
