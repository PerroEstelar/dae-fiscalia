# -*- coding: utf-8 -*-
r"""SITUACIÓN 01 · ¿Quién responde por una violación de derechos humanos? ·
12 ranuras · 1235 cuadros. Narra Carlos.

LO QUE SE OYE ENCIMA
    r01-r02  en una región de Colombia se denuncia la desaparición de un líder
             comunitario | que había recibido amenazas de una estructura criminal
    r03-r04  sus familiares informan que, antes de la desaparición, | habían
             puesto en conocimiento de distintas autoridades las amenazas
    r05-r06  la Fiscalía inicia una investigación penal para establecer las
             circunstancias de los hechos | y determinar las responsabilidades
    r07-r08  transcurridos varios años, la familia considera que sus derechos
             no han sido garantizados | y decide acudir a una organización de DD. HH.
    r09-r10  durante una reunión, uno de los familiares pregunta | si es
             posible presentar el caso ante una autoridad internacional
    r11-r12  otro integrante de la familia sostiene que un tribunal
             internacional | debería condenar penalmente a los responsables

QUIÉN LLEVA CARA
    El líder (antes), su esposa, la hija, el hijo, la abogada, la fiscal.
    Nunca se dibuja la desaparición ni la amenaza en acto (biblia §3): el
    papel en el umbral, de noche, es el después. La ruana mostaza es el
    acento: sobre él en r01, r02 y r04; colgada en r07; doblada en brazos de
    su esposa desde r08.
"""

R = {}

R[1] = (100, 'dia', ('lider', 'vecinos'), None, False, 'vereda', '''
Wide shot in front of the small concrete community hall of the hamlet in the
morning, the camera at standing height, perfectly level. Under the covered
porch, %(lider)s stands and speaks to %(vecinos)s seated in a loose semicircle
in front of him, most of them seen from behind or in three-quarter back view;
his open right hand rests on his chest, mid-sentence, his straw hat in his
left hand. Behind the hall, steep green slopes with coffee bushes and high
mountains with drifting cloud. He appears ONCE.
''')

R[2] = (110, 'hero', ('lider',), None, False, 'puerta_noche', '''
Medium shot at night of the front of his house, the camera outside at
standing height, perfectly level. %(lider)s stands in the half-open wooden
doorway under the single bare bulb, the mustard ruana on his shoulders; in his
hands, held low, a folded sheet of plain paper he has just picked up from the
threshold, its inside only plain grey bars. His eyes are not on the paper:
he looks out into the dark road, his jaw set. The red-earth road falls away
into darkness; nobody else anywhere. He appears ONCE.
''')

R[3] = (100, 'dia', ('esposa', 'hija', 'fiscal_s01'), None, False, 'despacho', '''
Over-the-shoulder shot from BEHIND the prosecutor at her desk, the camera at
seated height, perfectly level. In the left foreground, the back of the head
and the navy-grey shoulder of %(fiscal_s01)s, filling the left third of the
frame. Across the desk, %(esposa)s speaks, mid-sentence, her two hands
pressing a thick clear plastic folder of papers flat on the desk; beside her
%(hija)s sits upright, her eyes on the prosecutor. Each person appears ONCE.
''')

R[4] = (120, 'dia', ('lider', 'esposa', 'funcionaria'), None, False, 'oficina_pueblo', '''
Medium shot at the counter of the small-town public office by day, the camera
at standing height beside the counter, perfectly level. %(lider)s, the mustard
ruana on his shoulders, and %(esposa)s stand side by side at the counter in
three-quarter view; he slides a folded sheet of plain paper across the counter
with two fingers, his eyes on the official. On the other side of the counter
only the two hands and the plain grey sleeves of %(funcionaria)s receive it.
Sunlight from the street window. Each person appears ONCE.
''')

R[5] = (133, 'dia', ('investigadores',), None, False, 'vereda', '''
Wide shot of the red-earth road of the same hamlet by day, the camera at
standing height on the road, perfectly level. %(investigadores)s walk up the
road toward the houses, caught mid-stride, one of them carrying a plain dark
bag; behind them a plain white pickup truck with no markings is parked at the
bend. On a porch at the side, two neighbours watch, small. Green mountains
with cloud behind.
''')

R[6] = (84, 'dia', ('fiscal_s01',), None, False, 'despacho', '''
Medium-close shot of %(fiscal_s01)s at her desk, frontal three-quarter, the
camera at her seated eye level, perfectly level. She opens a new plain manila
case folder and reads its first page, pen in her right hand, her brows drawn
together slightly. The page shows only plain grey bars. Shelves of cardboard
case folders behind her. She appears ONCE.
''')

R[7] = (143, 'contraluz', ('esposa',), 'ruana', False, 'casa_lider', '''
Medium shot inside the house, the camera at seated height, perfectly level.
Years later: %(esposa)s, a little older, more grey in her plait, sits at the
heavy wooden table by the small window in three-quarter view, the clear
plastic folder in front of her now thick with papers. She looks toward the
door: on the plain wooden peg by the door hangs the matte mustard wool ruana,
alone. The bright window behind her; she is in soft shadow. She appears ONCE.
''')

R[8] = (83, 'dia', ('esposa', 'hija', 'hijo', 'abogada'), 'ruana', False, 'ong', '''
Medium-wide shot inside the small office of the human rights organization,
the camera at standing height, perfectly level. %(abogada)s holds the door
open and greets the family as they come in: %(esposa)s first, the thick clear
plastic folder held to her chest and the folded mustard ruana over her
forearm, then %(hija)s and %(hijo)s behind her, caught mid-step. Each person
appears ONCE.
''')

R[9] = (82, 'dia', ('esposa', 'hija', 'hijo', 'abogada'), 'ruana', False, 'ong', '''
Wide shot of the meeting around the long plain table of the organization,
the camera at seated height at the end of the table, perfectly level.
%(abogada)s sits at the far end with her notebook open; along the right side
sit %(esposa)s, %(hija)s and %(hijo)s; on the table in front of the mother lie
the thick clear plastic folder and the folded mustard ruana. The daughter
leans forward, about to speak. Each person appears ONCE.
''')

R[10] = (86, 'dia', ('hija',), None, False, 'ong', '''
Close-up of %(hija)s from the shoulders up, three-quarter view, the camera at
her seated eye level, perfectly level. She asks a question: her lips parted
mid-word, her brows lifted slightly, her eyes steady on the lawyer out of
frame to the left, the iris and pupil clear. Serious, not tearful. The plain
office wall behind her, soft. She appears ONCE.
''')

R[11] = (94, 'dia', ('hijo', 'esposa'), 'ruana', False, 'ong', '''
Medium shot of %(hijo)s at the table, frontal three-quarter, the camera at
seated height, perfectly level. He speaks firmly, mid-sentence, leaning
forward, both hands flat on the table. Beside him, %(esposa)s keeps one hand
resting on the folded mustard ruana on the table and looks at him. Each
person appears ONCE.
''')

R[12] = (100, 'dia', ('abogada', 'hijo'), None, False, 'ong', '''
Over-the-shoulder shot from BEHIND the son, the camera at seated height,
perfectly level. In the right foreground, the back of his head and his dark
grey shoulder, out of focus. Across the table, %(abogada)s listens: her pen
held still above the open notebook, her head tilted slightly, her eyes on him,
thoughtful. Each person appears ONCE.
''')

NOMBRE = {1: 'el_lider', 2: 'la_amenaza', 3: 'la_familia', 4: 'la_alcaldia',
          5: 'la_investigacion', 6: 'la_fiscal', 7: 'varios_anos',
          8: 'la_organizacion', 9: 'la_reunion', 10: 'la_pregunta',
          11: 'el_hijo', 12: 'la_abogada'}

CON_PERSONA = set(R)
SILUETAS = set()
CARTONES = {1, 4, 6, 7, 10, 12}
CENITALES = set()
SOLO_MANOS = set()
SIN_CARA = set()
TOPE_SIN_GENTE = 3
TOTAL = 1235
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['lider'], 2: ['lider'], 3: ['esposa', 'hija'],
         4: ['lider', 'esposa'], 7: ['esposa'],
         8: ['esposa', 'hija', 'hijo', 'abogada'],
         9: ['esposa', 'hija', 'hijo', 'abogada'], 10: ['hija'],
         11: ['hijo', 'esposa'], 12: ['abogada']}

ANCLAS = {1, 2, 3, 4, 7, 8}

REF_PLACA = {
 1: (['EI_ANCLA_pueblo'], 'estilo', ''),
 2: (['EI_ANCLA_noche_int'], 'estilo', ''),
 3: (['EI_ANCLA_oficina'], 'estilo', ''),
 4: (['EI_ANCLA_recepcion'], 'estilo', ''),
 7: (['EI_ANCLA_noche_int'], 'estilo', ''),
 8: (['EI_ANCLA_oficina'], 'estilo', ''),
 5: (['EI_S01_r01_el_lider'], 'lugar', 'It is the SAME hamlet. '),
 6: (['EI_S01_r03_la_familia'], 'lugar', 'It is the SAME office and the SAME prosecutor. '),
 9: (['EI_S01_r08_la_organizacion'], 'lugar', 'It is the SAME office and the SAME people. '),
 10: (['EI_S01_r08_la_organizacion'], 'lugar', ''),
 11: (['EI_S01_r08_la_organizacion'], 'lugar', ''),
 12: (['EI_S01_r08_la_organizacion'], 'lugar', ''),
}

REUSA = {}
DET = {}
BROLL = {}

MOV = {
 1: 'kling: el líder habla a los vecinos, la mano en el pecho; los vecinos asienten',
 5: 'kling: los dos investigadores suben por el camino',
 8: 'kling: la familia entra a la oficina',
 10: 'kling: la hija pregunta (boca)',
 11: 'kling: el hijo habla firme (boca)',
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
