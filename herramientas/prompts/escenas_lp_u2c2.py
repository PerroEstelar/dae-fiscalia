# -*- coding: utf-8 -*-
r"""UNIDAD 2 · Estudio reverso de caso 2 «Audiencia de prueba anticipada» ·
11 ranuras · pieza 2770. Narra Pilar.

LO QUE SE OYE ENCIMA (cruce_lp.json)
    r01  Durante los últimos tres años, en vivienda conyugal en Medellín,
         Carlos Eduardo Restrepo Múnera ejerció actos continuados
    r02  de maltrato físico, verbal y psicológico contra su cónyuge, María
         Elena Gutiérrez Ríos
    r03  El episodio más grave ocurrió el 10 de enero de 2026, cuando el
         procesado agredió físicamente a María Elena,
    r04  incapacidad médico-legal de 25 días con deformidad física transitoria
    r05  y le manifestó: «si me denuncia o habla en un juzgado, la mato a usted
         y a su mamá»
    r06  tras la denuncia de un tercero y la medida de protección de urgencia,
         una campaña de intimidación
    r07  familiares y terceros armados al lugar donde está refugiada; le exige
         la retractación
    r08  riesgo inminente; trasladarla a un refugio confidencial en el exterior
    r09  la red de protección a víctimas de VBG (Ley 1257 de 2008)
    r10  no es viable esperar hasta el juicio oral para su testimonio
    r11  la Fiscalía acude ante el juez de control de garantías: práctica
         anticipada del testimonio

LO QUE NO SE DIBUJA (la regla de toda la serie)
    Ni el maltrato, ni el golpe, ni la amenaza, ni un arma. Carlos Eduardo es
    SILUETA. El episodio del 10 de enero se cuenta con el DESPUÉS: la cocina
    vacía, una silla caída, una taza rota. La amenaza contra la madre se
    cuenta con el retrato de la madre, y la frase va en el cartón. Los
    «terceros armados» son siluetas lejos, sin arma a la vista.
    El acento mostaza es de María Elena: su cárdigan.
"""

R = {}

R[1] = (169, 'hero', (), None, False, 'ladera', '''
Wide shot of a hillside barrio of Medellin at dusk, the camera on a stairway
landing across the slope, perfectly level. Dense brick houses climb the
steep hill; the city lights begin far below in the valley. In the middle of
the frame, one small two-storey brick house has a single lit window. Nobody
in the street.
''')

R[2] = (169, 'hero', ('mariaelena', 'carloseduardo'), None, False, 'casa', '''
Medium shot of the small kitchen-dining room of that home at night, the
camera at seated height, perfectly level. %(mariaelena)s sits at the plain
table, both hands around a cup she does not drink from, her shoulders drawn
in, her eyes lowered to the table. In the doorway behind her, in the dark
hallway, stands %(carloseduardo)s, a solid dark shape filling the door frame,
motionless. One small lamp over the table.
''')

R[3] = (200, 'hero', (), None, False, 'casa', '''
Medium shot of the same small kitchen-dining room at night, EMPTY: one plain
chair lies on its side on the tiled floor, a plain cup lies broken in two
pieces near it, the table pushed slightly askew. The small lamp over the
table still on. Nobody in the frame. No blood, no stain, nothing else.
''')

R[4] = (175, 'dia', ('mariaelena',), None, False, 'consultorio', '''
Medium shot of %(mariaelena)s seated on the plain examination couch of a
forensic medical examination room, three-quarter view, the camera at seated
height, perfectly level. Her left forearm rests in a plain grey arm sling; a
small plain white dressing on her cheekbone. She looks down at the floor,
still. Daylight from one window. No wound visible, no blood.
''')

R[5] = (182, 'hero', ('mariaelena',), None, False, 'casa', '''
Close shot of a small plain shelf in a dim home: a framed photograph of an
older Colombian woman with grey hair in a simple frame, the photo drawn in
the same flat style; a woman's hand -the cuff of a plain matte
mustard-yellow knitted cardigan at the wrist- rests on the edge of the frame.
Low lamp light from one side. No face in frame.
''')

R[6] = (232, 'dia', ('fiscal_mujer',), None, False, 'despacho', '''
Medium shot of %(fiscal_mujer)s at her desk in the prosecutor's office,
three-quarter view, the camera at seated height, perfectly level.
Mid-action: she signs a plain one-page protection order with a plain pen,
the desk telephone receiver held between her ear and her shoulder, a thick
case file open beside her. Daylight from the window behind her.
''')

R[7] = (220, 'hero', ('mariaelena', 'armados'), None, False, 'barrio', '''
Night, inside a modest refuge home: %(mariaelena)s stands at a window in the
foreground, seen in three-quarter back view, holding the edge of a thin
curtain a few centimetres open with two fingers. Through the gap, down the
street under a single street lamp, %(armados)s stand near a parked car,
small and far away, waiting. Her face only half visible at the edge of the
light. No weapon visible anywhere.
''')

R[8] = (223, 'dia', ('mariaelena',), None, False, 'casa', '''
Close shot at bed height of a small plain suitcase lying open on a plain
bed, a few folded clothes inside. Mid-action: two women's hands, the cuffs of
a plain matte mustard-yellow knitted cardigan at the wrists, press the lid
down and hold it closed. Daylight from one side. No face in frame.
''')

R[9] = (187, 'dia', ('fiscal_mujer',), None, False, 'despacho', '''
Medium-close shot of %(fiscal_mujer)s standing at the window of her office,
the desk telephone receiver at her ear, a plain folder held against her
chest, looking out, speaking. The camera at her eye level, perfectly level,
from inside the room. Daylight on her face from the window. She is ALONE in
the frame and appears ONCE.
''')

R[10] = (169, 'contraluz', (), None, False, 'sala', '''
Wide shot of an EMPTY Colombian hearing room, the camera at the back by the
public benches, perfectly level. At the front, the witness chair stands
empty in a single band of light from a high window; the judge's desk and the
two tables are empty, the microphones off. Nobody in the frame.
''')

R[11] = (194, 'dia', ('fiscal_mujer', 'juez', 'defensor'), None, False, 'sala', '''
Medium-wide shot of a hearing of guarantees in a Colombian hearing room, the
camera at standing height from the side of the room, perfectly level.
Mid-action: %(fiscal_mujer)s stands at the prosecution table speaking toward
the judge, one hand open over her case file; at the centre, behind his plain
desk, %(juez)s listens with his hands joined; at the defence table,
%(defensor)s sits taking notes. Daylight from high windows.
''')

NOMBRE = {1: 'la_ladera', 2: 'la_cocina', 3: 'la_silla_caida',
          4: 'medicina_legal', 5: 'el_retrato', 6: 'la_medida',
          7: 'la_ventana', 8: 'la_maleta', 9: 'la_red', 10: 'la_silla_vacia',
          11: 'la_audiencia'}

CON_PERSONA = {2, 4, 5, 6, 7, 8, 9, 11}
SILUETAS = set()
CARTONES = {1, 3, 4, 5, 7, 9, 11}
CENITALES = set()
SOLO_MANOS = {5, 8}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
PIEZA = 2770
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {2: ['mariaelena'], 4: ['mariaelena'], 7: ['mariaelena'],
         6: ['fiscal_mujer'], 9: ['fiscal_mujer'], 11: ['fiscal_mujer']}

COCINA = 'LP_U2C2_r02_la_cocina'
DESPACHO = 'LP_U2C2_r06_la_medida'
REF_PLACA = {
 2: (['LP_U2C1_r01_la_calle_de_bodegas'], 'estilo', ''),
 3: ([COCINA], 'lugar', 'It is the SAME kitchen, now empty. '),
 5: ([COCINA], 'lugar', ''),
 8: ([COCINA], 'estilo', ''),
 1: ([COCINA], 'estilo', ''),
 4: ([COCINA], 'estilo', ''),
 7: ([COCINA], 'estilo', ''),
 6: ([COCINA], 'estilo', ''),
 9: ([DESPACHO], 'lugar', ''),
 10: ([DESPACHO], 'estilo', ''),
 11: ([DESPACHO], 'estilo', ''),
}

REUSA = {}

DET = {
 (9, 'el_telefono'): dict(cuadros=70, entra=90,
     registro='dia',
     personas=('fiscal_mujer',),
     escena='Extreme close shot of a woman\'s hand pressing the plain receiver '
            'of a desk telephone to her ear, the cuff of a plain charcoal grey '
            'blazer at the wrist, a strand of dark hair, window light.',
     gesto='The fingers tighten slightly on the receiver and stay. Nothing else '
           'moves.'),
}

BROLL = {}

MOV = {
 7: 'kling: ella abre un poco mas la cortina; abajo, un carro pasa despacio',
 8: 'kling: las manos cierran la maleta y la sostienen cerrada',
 1: 'camara de la casa (empuje lento), sin modelo',
}

LOWER_THIRD = {2: 'María Elena Gutiérrez Ríos'}


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
