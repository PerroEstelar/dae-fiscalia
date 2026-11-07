# -*- coding: utf-8 -*-
r"""VIDEO 04 · El río y la fábrica: midiendo el daño para reparar (U4 L1).
Narra Pilar. 18 ranuras. La narración es la ficha del caso del PDF (p. 109)
casi literal; el cierre, las preguntas de la valoración del daño (p. 110).

LA PROGRESIÓN
    r01-r02   la fábrica junto al río · el tubo que descarga, sorprendido
    r03-r05   la empresa se niega · la defensa y sus fotos · la mina vieja
    r06       el delito de lesión (gráfico sobre el río de dos aguas)
    r07-r08   lo que la Fiscalía no puede · la mina, río arriba
    r09-r10   el perito en el río · el laboratorio
    r11-r12   la medición (gráfico: el oxígeno y las dos especies) · la red vacía
    r13       la fiscal separa lo de la fábrica de lo de la mina
    r14       se suspende el juicio
    r15-r16   el plan (gráfico): la planta de tratamiento · el repoblamiento
    r17-r18   para reparar, medir (gráfico) · el río

LA EMPRESA NO TIENE NOMBRE NI LOGO; el gerente es el único de ella con cara.

R[n] = (cuadros, registro, gente, acento, fuego, lugar, escena)
"""

R = {}

R[1] = (100, 'aire', (), None, False, 'fabrica', '''
High aerial view of a large agro-industrial plant on the flat countryside of
the Colombian Magdalena valley, the camera far above looking down at a steep
angle, the horizon level near the top: long plain grey metal sheds, steel
tanks and silos, a concrete yard with trucks, and right behind the sheds the
slow wide brown-grey river lined with trees, flowing across the whole frame.
''')

R[2] = (100, 'dia', ('investigador', 'tecnica'), None, False, 'desague', '''
Medium-wide shot on the riverbank right below the plant, the camera at
standing height on the bank, perfectly level: the thick concrete drainage
pipe pours dirty grey-brown water into the river, a grey foam spreading
downstream; %(investigador)s, a few steps away on the bank, photographs the
pipe with a plain camera, and %(tecnica)s crouches at the water's edge
filling a plain glass sample bottle.
''')

R[3] = (100, 'dia', ('gerente', 'defensor'), None, False, 'ninguno', '''
Medium shot in the manager's office of the plant, the camera at seated height
across a plain meeting table, perfectly level: %(gerente)s sits back in his
chair with his arms folded, and with two fingers pushes a plain document of a
few pages back across the table, away from him; beside him %(defensor)s
keeps his hand flat on his own closed folder. A plain office inside the
plant: plain painted walls, a plain grey filing cabinet, no logo, no sign, no
lettering anywhere. Through the window behind them, the grey metal sheds of
the plant. This is Colombia; never Europe, never the United States.
''')

R[4] = (100, 'dia', ('defensor',), None, False, 'sala', '''
Medium close shot of %(defensor)s at the defence table in the hearing room,
the camera at his seated eye level from the side, perfectly level: he lays
three old plain photographs of a mine side by side on the table, one after
the other, his fingers pressing the last one flat; the photographs show only
grey heaps of tailings by a river.
''')

R[5] = (100, 'contra_ext', (), None, False, 'mina_vieja', '''
Wide shot of the abandoned gold mine upstream, the camera at standing height
on the opposite bank, perfectly level: rusting plain metal sluices, a
collapsed wooden shed, long grey heaps of old tailings sliding into the
river, small trees and bushes growing back over everything; the river runs a
dull ochre-grey past the tailings. Nobody in the frame. Everything here is
old and abandoned.
''')

R[6] = (100, 'aire', (), None, False, 'fabrica', '''
High aerial view of the river right below the plant, the camera far above
looking down at a steep angle: the slow river flows from left to right; at
the concrete drainage pipe on the bank, a plume of darker grey-brown water
with grey foam enters the river and spreads downstream, clearly darker than
the water upstream of the pipe; the grey sheds of the plant on the bank.
''')

R[7] = (100, 'dia', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s at her desk, the camera at seated height across the
desk, perfectly level: a plain paper map of the river is spread in front of
her; with her pencil she follows the river from a small square drawn far
upstream down to a second small square further down, and stops there,
thinking. A thin plain folder lies closed at the edge of the desk.
''')

R[8] = (100, 'contra_ext', ('fiscal', 'investigador'), None, False, 'desague', '''
Wide shot on the riverbank below the plant, the camera at standing height
behind them, perfectly level: %(fiscal)s and %(investigador)s stand side by
side on the bank, seen from behind, looking upstream along the river toward
the far grey hills where the old mine lies, small and distant. The river
runs past them.
''')

R[9] = (100, 'dia', ('perito',), None, False, 'desague', '''
Medium shot in the river right below the drainage pipe, the camera low near
the water, perfectly level: %(perito)s stands knee-deep in the brown-grey
water and holds a plain grey measuring probe on a cable down into the
current, his eyes on the small plain grey meter in his other hand; behind
him the concrete pipe pours its dirty water. Nothing legible on the meter.
''')

R[10] = (100, 'dia', ('perito',), None, False, 'laboratorio', '''
Medium shot of the laboratory of the environmental authority, the camera at
seated height beside the long white bench, perfectly level: %(perito)s,
without his boots now, sets one plain water sample bottle in a row of
identical bottles, upstream to downstream, and writes in a plain notebook;
the plain grey instrument beside him shows only plain grey bars.
''')

R[11] = (100, 'aire', (), None, False, 'fabrica', '''
Wide aerial view along the river, the camera high above and far to the side,
looking down the whole length of the valley, the horizon level near the top:
far upstream, small, the grey tailings of the old mine; in the middle, the
agro-industrial plant with its drainage pipe; downstream, the river winding
away between trees. One long continuous river from far to near.
''')

R[12] = (100, 'contra_ext', ('pescador_m',), None, False, 'rio_valle', '''
Medium-wide shot on the river downstream of the plant, the camera low over
the water, perfectly level: %(pescador_m)s stands in his dugout canoe and pulls
his hand-made cast net up out of the water with both hands; the net comes up
empty, water running out of it. Low trees on the bank behind him.
''')

R[13] = (100, 'dia', ('fiscal', 'perito'), None, False, 'despacho', '''
Medium shot at the fiscal's desk, the camera at seated height across the
desk, perfectly level: %(fiscal)s draws one firm pencil line straight across
the river on the plain paper map, right at the small square of the pipe;
%(perito)s, standing beside her desk, holds the plain report of the
measurements open and points at the same place. Nothing legible anywhere.
''')

R[14] = (100, 'dia', ('juez', 'fiscal', 'defensor'), None, False, 'sala', '''
Wide shot of the hearing room, the camera at standing height at the back
behind the public benches, perfectly level: %(juez)s, at the centre behind
his desk on the low platform, closes the case folder in front of him with
both hands; %(fiscal)s at the prosecution table on the left and
%(defensor)s at the defence table on the right look up at him.
''')

R[15] = (100, 'dia', ('obreros',), 'the small excavator', False, 'planta', '''
Wide shot of the new wastewater treatment plant under construction beside
the grey sheds, the camera at standing height, perfectly level: two round
concrete settling tanks, one finished and one still in plain wooden
formwork; %(obreros)s guide a bucket of fresh concrete from a small
mustard-yellow excavator into the formwork; the river and trees behind.
''')

R[16] = (100, 'contra_ext', ('perito', 'corpo'), None, False, 'rio_valle', '''
Medium shot at the river's edge downstream of the plant, the camera low near
the water, perfectly level: %(corpo)s tips a plain grey bucket and a small
shoal of young silver-grey fish slides out into the clear shallow water;
%(perito)s, beside her, holds a plain clipboard and watches the fish swim
away.
''')

R[17] = (100, 'dia', ('perito',), None, False, 'desague', '''
Medium shot on the riverbank below the plant, the camera at standing height,
perfectly level: %(perito)s crouches at the water's edge and dips the plain
grey measuring probe into the river again, calm, reading the small grey
meter; the drainage pipe beside him is dry and still, and the water at his
feet is clear.
''')

R[18] = (100, 'dia', ('pescador_m',), None, False, 'rio_valle', '''
Wide shot of the river downstream of the plant, the camera low over the
water, perfectly level: the river runs clear and dark grey-green between the
trees; far off %(pescador_m)s paddles his dugout canoe slowly upstream. The
plant is a soft grey shape far behind the trees.
''')

NOMBRE = {1: 'la_fabrica', 2: 'el_tubo', 3: 'la_negativa', 4: 'las_fotos',
          5: 'la_mina_vieja', 6: 'dos_aguas', 7: 'el_mapa', 8: 'rio_arriba',
          9: 'el_perito', 10: 'el_laboratorio', 11: 'el_valle',
          12: 'la_red_vacia', 13: 'la_linea', 14: 'se_suspende',
          15: 'la_planta', 16: 'los_peces', 17: 'medir', 18: 'el_rio'}

CORTE = {
 1: ('h01_empresa', 'Una empresa'),
 2: ('h01_empresa', 'tras ser'),
 3: ('h02_pasivo', 'La empresa se niega'),
 4: ('h02_pasivo', 'la existencia'),   # 7 nov: la negativa tenía 54
 5: ('h02_pasivo', 'por los relaves'),
 6: ('h03_lesion', 'El problema'),
 7: ('h04_limites', 'La Fiscalía no puede'),
 8: ('h04_limites', 'ni obligar'),
 9: ('h05_peritaje', 'La prueba'),
 10: ('h05_peritaje', 'que establece'),
 11: ('h06_medicion', 'El estudio'),
 12: ('h06_medicion', 'y que desaparecieron'),
 13: ('h07_aislar', 'Con un daño'),
 14: ('h08_preacuerdo', 'Se suspende'),
 15: ('h09_plan', 'Primero'),
 16: ('h09_plan', 'Segundo'),
 17: ('h09_plan', 'bajo la supervisión'),   # 7 nov: el perito con «bajo la supervisión... Para reparar, primero hay que medir»
 18: ('h10_medir', 'qué se afectó'),
}

EXTRA_TOKENS = {
 'pescador_m': ('A FISHERMAN of the Magdalena river, a Colombian man of about '
                'fifty-five, lean, short grey-black hair, in a faded plain grey '
                'shirt and rolled plain trousers, barefoot, a plain straw hat'),
}

REF = {
 7: ('DA_V02_r02_la_eleccion', 'lugar', 'It is the SAME prosecutor at her SAME desk.'),
 13: (7, 'lugar', 'It is the SAME prosecutor at her SAME desk; the expert is the one of the first reference.'),
 2: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator and the technician are the SAME man and woman.'),
 8: (2, 'lugar', 'It is the SAME riverbank below the SAME plant; the investigator is the SAME man.'),
 9: (2, 'lugar', 'It is the SAME pipe on the SAME riverbank.'),
 10: (9, 'gente', 'It is the SAME expert, now in the laboratory.'),
 17: (9, 'lugar', 'It is the SAME expert at the SAME place, months later: the pipe is dry.'),
 16: (9, 'gente', 'The expert is the SAME man.'),
 6: (1, 'lugar', 'It is the SAME plant and the SAME river, closer.'),
 11: (1, 'lugar', 'It is the SAME plant and the SAME river, from much further away.'),
 15: (1, 'lugar', 'It is the SAME plant.'),
 3: ('DA_V02_r19_el_juicio', 'gente', 'The defence lawyer is the SAME man.'),
 4: ('DA_V02_r19_el_juicio', 'lugar', 'It is the SAME hearing room and the SAME defence lawyer, closer.'),
 14: ('DA_V02_r19_el_juicio', 'lugar', 'It is the SAME hearing room with the SAME judge, prosecutor and defence lawyer.'),
 18: (12, 'lugar', 'It is the SAME river and the SAME fisherman, far off.'),
}
REF2 = {7: 'DA_V01_r30_la_fiscal', 8: 'DA_V01_r30_la_fiscal',
        13: ('DA_V04_r09_el_perito', 'THE ENVIRONMENTAL EXPERT'), 14: 'DA_V01_r30_la_fiscal'}

ANCLA_DE = {1: 'rural', 5: 'rural', 9: 'rural', 3: 'oficina', 12: 'rural'}

CON_PERSONA = {2, 3, 4, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18}
AEREOS = {1, 6, 11}
CENITALES = set()
SOLO_MANOS = set()
TOPE_SIN_GENTE = 3
TOTAL = 1800
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

GRIS = (20, 110)
SIN_TECHO = set()

GRAFICOS = {6: 'lesion', 11: 'oxigeno', 15: 'plan', 18: 'medir'}

KLING = {}
KLING_PRESTADO = {}
KLING_FIJA = 'Tripod shot: the camera stays where it is.'
KLING_AIRE = 'The camera moves only forward, smoothly, at the same height.'
KLING_FIN = ('Every movement travels all the way and arrives; nothing stops '
             'halfway. Keep the picture exactly as drawn in the first frame: the '
             'same flat graphic illustration with broad flat tonal planes, the '
             'same muted grey palette, the same people with the same faces.')
KLING_NEG = ('photorealistic, photograph, 3D render, texture, film grain, noise, '
             'ink outlines, colour shift, saturated colours, morphing, distorted '
             'face, extra people, extra hands, new objects, text, letters, logo, '
             'flag, weapon')


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
    return fallos, tot, mejor

# --- 7 nov: cuadros medidos (cortes de Scribe sobre la voz masterizada:
# cada ranura entra 3 cuadros antes de la primera palabra de su CORTE; la
# ultima termina con el master)
CUADROS = {1: 134, 2: 195, 3: 82, 4: 168, 5: 124, 6: 243, 7: 205, 8: 126, 9: 108, 10: 74, 11: 214, 12: 156, 13: 242, 14: 184, 15: 144, 16: 154, 17: 148, 18: 198}
for _n, _c in CUADROS.items():
    R[_n] = (_c,) + R[_n][1:]
TOTAL = 2899
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)
