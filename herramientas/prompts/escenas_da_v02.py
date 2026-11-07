# -*- coding: utf-8 -*-
r"""VIDEO 02 · Plan de priorización de la FGN (U3 L1, video explicativo).
Narra Pilar.

LA PROGRESIÓN (lo que pide la nota: finalidad del plan y su relación con los
delitos ambientales · lo disciplinario · las consecuencias de investigar mal)
    r01-r02   no se puede todo a la vez: el archivo · la fiscal elige un caso
    r03-r05   el primer pilar (gráfico) · la región frente al mapa · los tres
              niveles (gráfico)
    r06-r09   los fenómenos son ambientales: el frente de deforestación, las
              dragas, el camión de madera, el tablero de la fiscal (las tres
              primeras placas son las del V01 que quedaron bajo gráficos)
    r10-r11   los dos enfoques (gráfico) · el analista financiero
    r12-r14   el programa metodológico (gráfico) · el equipo en terreno
    r15-r18   la responsabilidad: la fiscal sola · el artículo 6 (gráfico) ·
              el caso descuidado · la investigación disciplinaria
    r19-r21   el juicio que se cae (gráfico de las consecuencias)
    r22-r24   mientras tanto el daño sigue: la draga, la tala, el embarcadero
              (placas del V01)
    r25-r26   la fiscal y su equipo salen al terreno

LA FISCAL ES LA DEL V01 (la misma cara en todo el curso): su placa aprobada
va como madre de identidad en cada plano donde aparece.

R[n] = (cuadros, registro, gente, acento, fuego, lugar, escena)
"""

R = {}

R[1] = (100, 'dia', ('auxiliar',), None, False, 'archivo', '''
Wide shot down a long aisle of the case archive of a regional prosecution
office, the camera at standing height, perfectly level, the tall metal
shelves running away on both sides, every shelf packed to the ceiling with
cardboard case folders. Halfway down the aisle %(auxiliar)s carries a tall
stack of folders against his chest with both arms, walking toward the camera,
his chin over the top folder. More stacks of folders wait on a trolley and on
the floor. The sheer quantity of cases is the subject of the picture.
''')

R[2] = (100, 'dia', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s at her desk in her office, the camera at seated
height across the desk, perfectly level. In front of her a tall pile of
cardboard case folders; she has drawn ONE folder out of the pile and holds it
flat on the desk in front of her with both hands, the pile untouched beside
it, her eyes on that one folder. Her pencil lies on the desk.
''')

R[3] = (100, 'dia', ('colegas',), None, False, 'sala_reuniones', '''
Medium-wide shot of the meeting room, the camera at standing height behind
%(colegas)s, perfectly level, who stand with their backs to us in front of the
large wall map of Colombia, one of them pointing at a region in the south of
the map. The map shows only the plain outlines of the departments in light
grey, with a few plain grey pins clustered in two or three regions.
''')

R[4] = (100, 'dia', ('fiscal', 'investigador'), None, False, 'fiscalia_pueblo', '''
Medium shot inside the small prosecution office of a river town, the camera at
seated height, perfectly level. %(fiscal)s and %(investigador)s lean over a
plain paper map of the region spread on the desk, the fiscal's pencil resting
on a bend of the river drawn on the map, the investigator holding one corner
of the map flat with his palm. Through the window behind them, a hot street
with motorcycles.
''')

R[5] = (100, 'dia', (), None, False, 'sala_reuniones', '''
Close shot of the large wall map of Colombia in the meeting room, the camera
at standing height facing the wall, perfectly level: the plain light grey
outlines of the departments and a few plain grey pins in the south and on the
Pacific coast; the edge of the plain table and a glass of water in the lower
corner of the frame. Nobody in the frame. No names, no lettering on the map.
''')

R[8] = (100, 'dia', (), None, False, 'carretera', '''
Medium-wide shot of a red-earth road through the Colombian Amazon forest, the
camera at standing height at the roadside, perfectly level. An old heavy
truck with a plain grey cab and a long flatbed trailer loaded high with
freshly cut tree trunks, held by plain chains, drives past from left to
right, mid-way across the frame, a driver in a plain grey cap visible small
behind the side window of the cab; red mud splashes from the ruts under its
wheels. The forest is tall and dense on both sides of the road.
''')

R[10] = (100, 'dia', ('analista',), None, False, 'sala_analisis', '''
Medium-wide shot of the dim criminal analysis room, the camera at standing
height at the end of the row of desks, perfectly level. %(analista)s sits at
his desk in the foreground, his face lit by his screen, which shows only an
abstract grey network diagram of dots and lines; behind him two more
analysts work at their screens, small and soft. Nothing legible on any
screen.
''')

R[11] = (100, 'dia', ('analista',), None, False, 'sala_analisis', '''
Close shot over the shoulder of %(analista_min)s at his desk, the camera behind
his right shoulder, perfectly level: on the desk in front of him a printed
bank statement covered in plain grey bars with three lines marked by hand,
his right hand resting on it holding a plain pen, palm down, fingers together,
thumb visible; on the screen beyond, an abstract grey diagram of linked dots.
Nothing legible anywhere.
''')

R[12] = (100, 'dia', ('fiscal', 'investigador', 'tecnica'), None, False, 'sala_reuniones', '''
Medium shot of a working meeting at the long table, the camera at seated
height at the end of the table, perfectly level. %(fiscal)s stands at the
head of the table, one hand flat on a plain sheet of the plan laid on the
table, explaining; %(investigador_sala)s, and %(tecnica_sala)s, sit on either side
looking at the sheet, one of them writing in a plain notebook. Plain folders,
glasses of water. Nothing legible on any paper.
''')

R[13] = (100, 'dia', (), None, False, 'sala_reuniones', '''
Close top-down shot of the table, the camera looking straight down: a plain
sheet of the investigation plan laid flat, covered in plain grey bars in five
neat sections with plain tick boxes, a plain pencil beside it, a plain
satellite printout of a river and a forest clearing partly under it, a glass
of water at the edge. No hand in the frame. Nothing legible anywhere.
''')

R[14] = (100, 'dia', ('fiscal', 'investigador', 'tecnica', 'analista'), None, False, 'ribera', '''
Wide shot on the bank of a wide brown river in the Colombian Pacific
lowlands, the camera at standing height, perfectly level. A team walks along
the bank toward the camera in a loose line: %(fiscal)s in front with a
folder under her arm, %(investigador)s with a plain camera on a strap,
%(tecnica)s carrying a plain grey case of sample bottles, and %(analista)s
with a plain backpack. Far behind them on the river, small, the shape of a
dredge.
''')

R[15] = (100, 'hero', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s alone at her desk in her office in the evening,
the camera at seated height across the desk, perfectly level. A single plain
desk lamp lights an open case folder in front of her; she reads it with one
hand flat on the page and the other at her temple, her face serious and
still. The window behind her is dark grey; the rest of the office falls into
soft grey shadow.
''')

R[16] = (100, 'dia', (), None, False, 'despacho', '''
Close shot of a plain shelf in the prosecutor's office, the camera at
standing height facing the shelf, perfectly level: a row of thick plain
law books bound in plain dark grey and dark blue-grey cloth with completely
plain spines, a plain bookend, flat window light from the left. Nothing
written on any spine, no lettering anywhere. Nobody in the frame.
''')

R[17] = (100, 'dia', (), None, False, 'despacho', '''
Medium shot of an empty desk in a prosecution office, the camera at seated
height, perfectly level: a cardboard case folder lies forgotten under a pile
of other folders, its corner bent, its cover faded to a paler flat grey as if
nobody has touched it for months, no spots and no stains; beside
it a cold cup of coffee and a desk telephone; the chair pushed back from the
desk, empty. Nobody in the frame.
''')

R[18] = (100, 'dia', ('funcionario_disc',), None, False, 'pasillo', '''
Wide shot down the long plain corridor of a public office, the camera at
standing height, perfectly level. %(funcionario_disc)s walks away from the
camera along the corridor carrying a single cardboard folder in one hand,
toward a closed plain door at the far end; the tall window at the end lights
the floor. The benches along the wall are empty.
''')

R[19] = (100, 'dia', ('juez', 'fiscal', 'defensor'), None, False, 'sala', '''
Wide shot of the hearing room during a trial, the camera at standing height
at the back of the room behind the public benches, perfectly level. %(juez)s
sits at the centre behind his desk on the low platform, speaking into his
microphone; %(fiscal)s sits at the prosecution table on the left, very
still, a folder open in front of her; %(defensor)s sits at the defence
table on the right, leaning back. Only two people on the public benches,
seen from behind. The wall behind the judge is a plain empty painted wall,
with nothing in front of it and nothing hanging on it.
''')

R[20] = (100, 'dia', (), None, False, 'sala', '''
Close detail shot on the prosecution table in the hearing room, the camera
low at table height, perfectly level: a plain clear evidence bag lies on
the table with a small glass sample bottle of murky river water inside it,
the bottle's plain cap still closed, the bag's plain white seal strip torn
open and curling; beside it a plain cardboard folder and a pen. The judge's
desk is a soft grey shape far behind. No hand in the frame. Nothing legible
anywhere.
''')

R[21] = (100, 'dia', ('fiscal',), None, False, 'sala', '''
Medium close shot of %(fiscal)s at the prosecution table in the hearing
room, the camera at her seated eye level from the side, perfectly level. She
has closed her folder and rests both hands flat on it; her eyes are lowered
to the table, her mouth a straight line, her shoulders very slightly down.
Behind her, soft and grey, the empty public benches.
''')

R[25] = (100, 'dia', ('fiscal', 'investigador', 'tecnica'), None, False, 'embarcadero', '''
Medium-wide shot at a small floating wooden landing on a wide river under a
plain overcast grey sky, the camera at standing height on the bank, perfectly
level. A plain grey aluminium boat with an outboard motor waits at the
landing; %(investigador)s is already in the boat, one hand resting on the
landing post; %(tecnica)s stands on the landing holding the grey case of
sample bottles against her hip with both hands, her eyes on the boat; and
%(fiscal)s walks down the plank onto the landing with her folder under her
arm. Mist on the river, the forest beyond.
''')

R[26] = (100, 'dia', ('fiscal',), None, False, 'rio', '''
Close shot of %(fiscal)s seated in the bow of the moving boat on the wide
river, the camera low in the boat facing her in three-quarter view, perfectly
level. She looks ahead past the camera, toward the forest on the far bank,
her glasses catching the flat light, her face calm and determined, her mouth
closed. Behind her the brown river and the green wall of the forest, soft.
''')

# las placas que vienen del V01 (sus elegidas, limpias con esta ranura). Las
# tres primeras quedaron bajo los gráficos del V01 y casi no se vieron; las
# tres últimas son la vuelta al daño del V01, a propósito.
PRESTADA = {6: ('V01', 12), 7: ('V01', 23), 9: ('V01', 33),
            22: ('V01', 3), 23: ('V01', 10), 24: ('V01', 21)}
for _n, (_c, _m) in PRESTADA.items():
    R[_n] = (100, 'dia', (), None, False, 'ninguno', 'PRESTADA %s r%02d' % (_c, _m))
R[6] = (100, 'aire', (), None, False, 'ninguno', R[6][6])
R[7] = (100, 'aire', (), 'the dredges', False, 'ninguno', R[7][6])
R[9] = (100, 'dia', ('fiscal',), None, False, 'ninguno', R[9][6])
R[22] = (100, 'dia', ('minero',), 'the casing of the engine and pump on the dredge', False, 'ninguno', R[22][6])
R[23] = (100, 'dia', ('motosierrista',), None, False, 'ninguno', R[23][6])
R[24] = (100, 'contra_ext', ('armados',), None, False, 'ninguno', R[24][6])

NOMBRE = {1: 'el_archivo', 2: 'la_eleccion', 3: 'el_mapa', 4: 'la_region',
          5: 'los_niveles', 6: 'frontera_aerea', 7: 'dragas_aereo',
          8: 'el_camion', 9: 'el_tablero', 10: 'el_analisis',
          11: 'el_extracto', 12: 'el_plan', 13: 'la_hoja', 14: 'el_equipo',
          15: 'la_noche', 16: 'los_codigos', 17: 'el_olvido',
          18: 'el_pasillo', 19: 'el_juicio', 20: 'la_bolsa',
          21: 'la_fiscal_vencida', 22: 'la_draga', 23: 'la_tala',
          24: 'el_embarcadero', 25: 'la_salida', 26: 'la_fiscal_rio'}

# dónde empieza cada ranura: (bloque, primeras palabras que dice la voz)
CORTE = {
 1: ('e01_proposito', 'La Fiscalía'),
 2: ('e01_proposito', 'Por eso'),
 3: ('e02_pilar', 'El primer'),
 4: ('e02_pilar', 'cada región'),
 5: ('e03_niveles', 'La priorización'),
 6: ('e04_ambiente', 'En muchos'),
 7: ('e04_ambiente', 'la explotación'),
 8: ('e04_ambiente', 'y el tráfico'),
 9: ('e04_ambiente', 'tienen patrones'),
 10: ('e05_enfoques', 'Por eso'),
 11: ('e05_enfoques', 'y afectar'),
 12: ('e06_programa', 'Priorizar exige'),
 13: ('e06_programa', 'hipótesis claras'),
 14: ('e07_equipo', 'Y exige'),
 15: ('e08_disciplinario', 'Dirigir'),
 16: ('e08_disciplinario', 'La Constitución'),
 17: ('e09_disciplinario_b', 'Una investigación'),
 18: ('e09_disciplinario_b', 'puede dar'),
 19: ('e10_consecuencias', 'Las consecuencias'),
 20: ('e10_consecuencias', 'evidencia excluida'),
 21: ('e10_consecuencias', 'en el juicio'),   # 7 nov: las cuatro consecuencias caen en el gráfico de la r20
 22: ('e11_dano', 'Mientras'),   # 7 nov: la fiscal se queda con «Y en materia ambiental...»
 23: ('e11_dano', 'el bosque'),
 24: ('e11_dano', 'que lo financia'),   # 7 nov: la tala tenía 37 cuadros
 25: ('e12_cierre', 'Priorizar bien'),
 26: ('e12_cierre', 'es la manera'),
}

EXTRA_TOKENS = {
 # 7 nov: en minúscula al lado de un papel (en mayúscula se imprime como texto)
 'analista_min': ('the financial analyst of the prosecution service, a Colombian '
                  'man of about thirty-five, short dark hair, plain dark-framed '
                  'glasses, in a plain light grey shirt'),
 # 7 nov: en la sala de reuniones, sin guantes ni botas (salían raros)
 'investigador_sala': ('A CRIMINAL INVESTIGATOR of the prosecution service, a '
                       'Colombian man of about thirty-eight, short black hair, '
                       'a short beard, in a plain dark grey field jacket with '
                       'nothing printed on it, plain dark trousers'),
 'tecnica_sala': ('AN ENVIRONMENTAL TECHNICIAN, a Colombian woman of about '
                  'thirty, dark hair in a ponytail, in a plain light grey '
                  'long-sleeved field shirt, bare hands'),
 'funcionario_disc': ('AN OFFICIAL of the disciplinary office, a Colombian man '
                      'in a plain dark suit, seen ONLY FROM BEHIND'),
}

# la fiscal del V01 como madre de identidad; el resto, madres de este video
REF = {
 2: ('DA_V01_r30_la_fiscal', 'lugar', 'It is the SAME prosecutor, at her own desk.'),
 4: ('DA_V01_r30_la_fiscal', 'gente', 'It is the SAME prosecutor, in a small regional office.'),
 12: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator and the technician are the SAME man and woman; the prosecutor is the one of the first reference.'),
 14: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator and the technician are the SAME man and woman.'),
 15: (2, 'lugar', 'It is the SAME prosecutor in the SAME office, in the evening.'),
 17: (2, 'lugar', 'It is the SAME office, empty.'),
 21: (19, 'lugar', 'It is the SAME hearing room and the SAME prosecutor, closer.'),
 20: (19, 'lugar', 'It is the SAME hearing room.'),
 25: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator and the technician are the SAME man and woman.'),
 26: (2, 'gente', 'It is the SAME prosecutor, now on the river.'),
 11: (10, 'lugar', 'It is the SAME analyst at the SAME desk.'),
 13: (12, 'lugar', 'It is the SAME table of the SAME meeting room.'),
 5: (3, 'lugar', 'It is the SAME wall map in the SAME room.'),
 16: (2, 'lugar', 'It is the SAME office.'),
}
# un plano puede pedir una segunda madre de identidad (la fiscal) además del lugar
REF2 = {12: 'DA_V01_r30_la_fiscal', 14: 'DA_V01_r30_la_fiscal',
        19: 'DA_V01_r30_la_fiscal', 21: 'DA_V01_r30_la_fiscal',
        25: 'DA_V01_r30_la_fiscal'}

ANCLA_DE = {1: 'oficina', 3: 'oficina', 10: 'oficina', 18: 'oficina',
            19: 'oficina', 8: 'rural'}

CON_PERSONA = {1, 2, 3, 4, 8, 9, 10, 11, 12, 14, 15, 18, 19, 21, 22, 23, 24, 25, 26}
AEREOS = {6, 7}
CENITALES = {13}
SOLO_MANOS = set()
TOPE_SIN_GENTE = 3
TOTAL = 2600
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

# el color, como el V01: la sombra se levanta (la noche es gris, no negra) y
# la r15, de noche, sin techo
GRIS = (20, 110)
SIN_TECHO = {15}

GRAFICOS = {3: 'pilares', 5: 'niveles', 10: 'enfoques', 13: 'programa',
            16: 'articulo6', 20: 'consecuencias'}

# 7 nov: el movimiento. Sin clip: las seis ranuras de grafico y la r17 (el
# expediente olvidado: su sentido es que nadie lo toca; queda con la camara de
# la casa). Las r22-r24 son las placas del V01 con SUS clips (KLING_PRESTADO:
# se copia el crudo del V01, cero creditos). Las caminatas hacia camara (r01,
# r14) van con el encuadre que se abre (mov_da.ABRE).
KLING = {
 1: ('fija', 'The clerk walks two slow steps forward along the aisle toward the '
     'camera, carrying the tall stack of folders against his chest with both '
     'arms, and stops beside the trolley; dust drifts slowly in the band of '
     'light from the high window.'),
 2: ('fija', 'She opens the cover of the folder, lays it flat on the desk and '
     'reads the first page, her eyes moving slowly along the lines; the pile '
     'of folders beside her stays as it is.'),
 4: ('fija', 'She slides the tip of her pencil along the river drawn on the map '
     'and stops on one bend; the investigator leans in a little, looks where '
     'she points and nods once; outside the window a motorcycle rides past '
     'along the street and leaves the frame.'),
 6: ('aire', 'The camera glides slowly forward high over the forest toward the '
     'burned clearings; the thin grey smoke rises and drifts slowly to the '
     'right in the wind.'),
 7: ('aire', 'The camera glides slowly forward high over the river along the '
     'line of dredges; the muddy ochre-grey plumes behind each dredge drift '
     'slowly downstream.'),
 8: ('fija', 'The truck drives slowly forward along the road from left to right, '
     'its wheels turning through the mud of the ruts, the logs on the trailer '
     'rolling with it. The truck stays inside the frame.'),
 9: ('fija', 'She presses the card flat against the top of the board with her '
     'fingertips, then lowers her arm and steps half a step back to look at the '
     'whole chain of cards; the investigator beside her looks up at the board '
     'and nods.'),
 11: ('fija', 'He moves the tip of the pen slowly down the column of the bank '
      'statement, row by row, draws a short line under one row, and lifts his '
      'eyes to the diagram on the screen.'),
 12: ('fija', 'The prosecutor speaks, moving one hand across the plan from one '
      'section to the next; the investigator writes a line in his notebook; '
      'the technician nods and looks up at the prosecutor.'),
 14: ('fija', 'The four keep walking along the river bank toward the camera at '
      'an easy pace, side by side as they are; the river flows past behind '
      'them. They stay inside the frame.'),
 15: ('fija', 'She turns the page of the open case folder with one hand, lays it '
      'flat and keeps reading, her other hand still at her temple; the lamp '
      'light stays steady.'),
 18: ('fija', 'The official keeps walking away along the corridor toward the '
      'closed door at the far end, unhurried, the folder in his hand, and stops '
      'in front of the door.'),
 19: ('fija', 'The judge speaks into his microphone, his mouth moving, and turns '
      'a page on his desk; the prosecutor sits still and lowers her eyes to her '
      'folder; the defence lawyer leans back in his chair.'),
 21: ('fija', 'She breathes out slowly, her shoulders sink a little further, '
      'she closes her eyes for a moment and opens them again, still looking '
      'down at the closed folder under her hands.'),
 25: ('fija', 'The prosecutor walks across the landing to the edge beside the '
      'boat and stops; the technician hands the case of sample bottles down to '
      'the investigator, who takes it with both hands and sets it in the boat; '
      'mist drifts along the river.'),
 26: ('libre', 'The boat moves steadily up the river; the far bank and the '
      'forest slide slowly past behind her; she looks ahead toward the forest, '
      'breathes, and her hair moves a little in the wind. The camera rides in '
      'the boat with her.'),
}
# ranura de este video -> (video, ranura) cuyo crudo de Kling se copia
KLING_PRESTADO = {22: ('V01', 3), 23: ('V01', 10), 24: ('V01', 21)}
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
CUADROS = {1: 152, 2: 214, 3: 131, 4: 199, 5: 407, 6: 109, 7: 50, 8: 70, 9: 84, 10: 226, 11: 203, 12: 147, 13: 210, 14: 249, 15: 132, 16: 302, 17: 89, 18: 134, 19: 76, 20: 230, 21: 122, 22: 119, 23: 56, 24: 77, 25: 102, 26: 87}
for _n, _c in CUADROS.items():
    R[_n] = (_c,) + R[_n][1:]
TOTAL = 3977
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)
