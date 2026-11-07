# -*- coding: utf-8 -*-
r"""VIDEO 03 · Técnicas especiales de investigación (U3 L3, video
interactivo). Narra Carlos. 24 ranuras.

LA NOTA DEL PDF pide un recorrido: la casa, la ventana que se abre, el vuelo
sobre el territorio, cada técnica como un punto que se puede tocar, y al
final la figura del doctor Porras que da paso a su video. En video lineal:
cada técnica es un capítulo con su placa y su rótulo-enlace (mg_da: el
círculo sobre la placa y el nombre con su artículo), para que virtualización
lo vuelva clic sin rehacer nada.

LA PROGRESIÓN
    r01-r02   la casa cerrada del pueblo minero · la fiscal abre el código
    r03-r04   el juez de control de garantías (gráfico: antes o después)
    r05-r06   la ventana que se abre · el vuelo sobre el territorio
    r07-r08   vigilancia de personas (art. 239): el carro · el dron
    r09-r10   vigilancia de cosas (art. 240): la lancha · la bodega
    r11-r12   análisis e infiltración (art. 241): la red · la mesa en cenital
    r13-r14   agente encubierto (art. 242): entre los mineros · sus notas
    r15-r16   entrega vigilada (art. 243): la lancha cargada · el camión seguido
    r17       retención de correspondencia (art. 233): el paquete
    r18-r19   interceptación (art. 235): los audífonos · las 24 horas ante el juez
    r20       internet (art. 236): el computador incautado
    r21       bases de datos (art. 244): la autorización previa
    r22       la regla de exclusión: la jueza aparta una carpeta
    r23-r24   la casa, ya vigilada · la silueta del doctor Porras

NINGUNA CARA DEL OTRO LADO: el indiciado, el agente encubierto y el doctor
Porras van de espaldas o en silueta (el encubierto oculta su identidad; de
Porras no tenemos foto y no se inventa una cara).

R[n] = (cuadros, registro, gente, acento, fuego, lugar, escena)
"""

R = {}

R[1] = (100, 'dia', (), 'the engine under the tarpaulin', False, 'pueblo', '''
Wide shot of a closed two-storey house at the end of the main street of the
mining town, by the river, the camera at standing height across the street,
perfectly level. Plain rendered concrete walls, every window shut with plain
metal shutters, a high plain wall around the yard; through the half-open
yard gate, under a grey tarpaulin, the corner of a mustard-yellow dredge
engine. Nobody in the street. The house gives nothing away.
''')

R[2] = (100, 'dia', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s at her desk, the camera at seated height across the
desk, perfectly level. She has a thick plain law book open in front of her,
bound in plain dark grey cloth, and runs her pencil down one page, reading
closely; beside the book, a plain photograph of a closed house lies face up.
''')

R[3] = (100, 'dia', ('jueza_gar',), None, False, 'despacho', '''
Medium shot in the office of a judge of guarantees, the camera at seated
height behind the prosecutor's shoulder, perfectly level: across a plain desk
%(jueza_gar)s reads a request of a few pages held in both hands. In the near
foreground, seen only from behind, the prosecutor sits upright: her straight
dark jaw-length hair and the shoulders of her dark grey blazer, her folder
closed on her knees. Behind the judge, plain metal shelving with cardboard
folders and a window with a plain blind. Only ONE face in the picture: the
judge's.
''')

R[4] = (100, 'dia', ('jueza_gar',), None, False, 'despacho', '''
Close medium shot of %(jueza_gar)s at her plain desk, the camera at her seated
eye level, perfectly level: she signs the last page of the request with a
plain pen, her other hand flat on the page, palm down, fingers together,
thumb visible; a plain desk lamp and a stack of folders beside her.
''')

R[5] = (100, 'dia', (), None, False, 'ninguno', '''
Medium shot from inside a plain room toward a window with two plain wooden
shutters, the camera at standing height, perfectly level. The two shutters
stand half open toward the outside; through the opening, the corrugated zinc
roofs of a Colombian river town, a few palm trees and banana plants, the wide
grey-brown river and the dense tropical rainforest beyond under a plain grey
sky; never tiled roofs, never pine trees, never a European village. Nobody in
the room. The room is dim; the light comes only through the window.
''')

R[6] = (100, 'aire', (), None, False, 'selva_aire', '''
High aerial view over a wide river of the Colombian Pacific lowlands, the
camera far above looking down at a steep angle, the horizon level near the
top: the small river town on the near bank, its zinc roofs and its plank
landing; the wide river curving away into the forest; far upriver, small, two
dredges and a pale ochre-grey plume in the water.
''')

R[7] = (100, 'dia', ('investigador', 'empresario'), None, False, 'pueblo', '''
Medium shot over the shoulder of %(investigador)s, sitting behind the wheel
of a plain grey parked car, the camera behind his right shoulder, perfectly
level: through the windscreen, across the street, %(empresario)s walks out
of the gate of the closed house toward a white pickup truck, a phone at his
ear. The investigator's notebook lies open on the passenger seat.
''')

R[8] = (100, 'aire', (), None, False, 'carretera', '''
High aerial view looking straight down at a red-earth road through the
forest, as seen by a small drone far above, the camera looking straight
down: a single white pickup truck drives along the road, small in the frame,
its shadow beside it; the forest canopy on both sides. No screen, no
interface, no markings, no frame lines.
''')

R[9] = (100, 'contra_ext', ('investigador', 'lanchero'), None, False, 'embarcadero', '''
Wide shot of the floating wooden landing at the river bend, the camera on
the bank among tall grass at a distance, perfectly level. %(lanchero)s loads
plain blue-grey plastic fuel drums into a long wooden motor boat moored at
the landing; in the near foreground, small and seen only from behind,
%(investigador)s crouches in the grass and photographs the boat with a plain
camera with a long lens.
''')

R[10] = (100, 'dia', (), 'the engine', False, 'pueblo', '''
Medium-wide shot of a plain concrete warehouse at the river edge of the
mining town, the camera at standing height across a muddy yard, perfectly
level. Its roll-down metal shutter is half open; inside, in shadow, plain
fuel drums in rows and a mustard-yellow dredge engine on a pallet. A plain
security camera, small, on a pole at the corner of the yard looks at the
shutter. Nobody in the frame.
''')

R[11] = (100, 'dia', ('analista', 'fiscal'), None, False, 'sala_analisis', '''
Medium shot in the criminal analysis room, the camera at standing height,
perfectly level. %(analista)s sits in front of a large plain wall screen
showing only an abstract grey network diagram: plain grey dots joined by
lines, one dot larger at the top; %(fiscal)s stands behind his chair, one
hand on its backrest, looking at the larger dot. Nothing legible on the
screen.
''')

R[12] = (100, 'dia', (), None, False, 'sala_analisis', '''
Close top-down shot of a plain table, the camera looking straight down: a
dozen plain small photographs laid out in a pyramid, each showing only a
plain grey silhouette of a head and shoulders, with plain grey threads
connecting them from the wide base up to the single photograph at the top; a
plain pencil and a plain notebook at the edge. No hand in the frame. Nothing
legible anywhere.
''')

R[13] = (100, 'contra_ext', ('encubierto', 'mineros'), None, False, 'draga', '''
Medium-wide shot on the plank deck of the dredge, the camera at standing
height at the edge of the deck, perfectly level. %(encubierto)s stands among
%(mineros)s, holding the black suction hose with them, his back half turned
to us; the men around him talk while they work. The river around the dredge
is a dull opaque ochre-grey.
''')

R[14] = (100, 'hero', ('encubierto',), None, False, 'ninguno', '''
Medium shot of a bare rented room in the mining town at night, the camera at
standing height behind %(encubierto)s, perfectly level: he sits on the edge of
a plain bed with his back to us, writing in a small plain notebook on his
knee by the light of a single plain bulb; his rubber boots stand by the door.
The plain painted walls fall away into soft grey shadow.
''')

R[15] = (100, 'contra_ext', ('lanchero',), None, False, 'rio', '''
Wide shot of the wide river, the camera low over the water from the bank,
perfectly level: a long wooden motor boat goes downriver loaded with plain
grey sacks under a grey tarpaulin, %(lanchero)s at the outboard motor at the
back, a long wake behind it. The forest on the far bank.
''')

R[16] = (100, 'dia', ('investigador',), None, False, 'carretera', '''
Medium shot from inside a plain car on a road through the countryside, the
camera in the back seat behind %(investigador)s at the wheel, perfectly
level: through the windscreen, far ahead on the road, a truck loaded with
plain grey sacks under a tarpaulin; the investigator keeps his distance,
both hands on the wheel.
''')

R[17] = (100, 'dia', ('investigador', 'empleada'), None, False, 'ninguno', '''
Medium shot at the counter of a small courier office in a Colombian town,
the camera at standing height beside the counter, perfectly level. A plain
brown parcel lies on a plain scale; %(empleada)s holds it steady with both
hands while %(investigador)s shows her a plain judicial order of one page;
plain shelves of parcels behind them. His belt is plain and nothing hangs
from it. Nothing legible on any label or paper.
''')

R[18] = (100, 'hero', ('analista',), None, False, 'sala_analisis', '''
Medium close shot of %(analista)s at his desk in the dim analysis room, the
camera at his seated eye level from the side, perfectly level: he wears
plain grey headphones and listens with his eyes down, a plain pen in his
hand over a plain notebook; on the screen in front of him only a plain grey
audio waveform. Nothing legible on the screen.
''')

R[19] = (100, 'dia', ('fiscal', 'jueza_gar'), None, False, 'despacho', '''
Medium shot in the office of the judge of guarantees, the camera at standing
height by the door, perfectly level: %(fiscal)s walks in with her folder
under her arm toward the plain desk where %(jueza_gar)s waits; a
plain round wall clock with hands and NO numerals above the door frame.
''')

R[20] = (100, 'dia', ('perito_inf',), None, False, 'laboratorio', '''
Medium shot of a plain forensic computer bench, the camera at seated height,
perfectly level: %(perito_inf)s connects a closed seized laptop, sealed in a
plain clear evidence bag with its lid open, to his own plain computer with a
plain grey cable; on his screen only plain grey bars and an abstract grey
map of linked dots. Nothing legible anywhere.
''')

R[21] = (100, 'dia', ('fiscal', 'analista'), None, False, 'sala_analisis', '''
Medium shot in the analysis room, the camera at seated height, perfectly
level: %(fiscal)s hands %(analista)s a printed order of one page with a plain
signature line at the bottom, covered in plain grey bars; he takes it in one
hand, his other hand on the keyboard; his screen shows only two plain grey
tables side by side. Nothing legible anywhere.
''')

R[22] = (100, 'dia', ('jueza_gar', 'defensor'), None, False, 'sala', '''
Medium shot of the hearing room, the camera at standing height at the back,
perfectly level: %(jueza_gar)s, at her plain desk on the low platform, lifts one
folder from the pile in front of her and sets it apart on the far corner of
the desk, away from the others; at the defence table %(defensor)s watches,
leaning forward.
''')

R[23] = (100, 'dia', (), 'the engine under the tarpaulin', False, 'pueblo', '''
Wide shot of the same closed two-storey house at the end of the main street
of the mining town, the camera at standing height further down the street,
perfectly level: the same shut windows and yard gate, the mustard-yellow
engine under the tarpaulin; in the foreground, small and out of the way, a
plain grey parked car. Nobody in the street.
''')

R[24] = (100, 'contraluz', ('porras',), None, False, 'ninguno', '''
Medium-wide shot of a plain office, the camera at standing height, perfectly
level: %(porras)s stands at a tall window looking out at the river, a dark
grey silhouette against the bright grey daylight, one hand in his pocket, the
other resting on the window frame. The room is plain and quiet.
''')

NOMBRE = {1: 'la_casa', 2: 'el_codigo', 3: 'la_solicitud', 4: 'la_firma',
          5: 'la_ventana', 6: 'el_vuelo', 7: 'el_carro', 8: 'el_dron',
          9: 'la_lancha', 10: 'la_bodega', 11: 'la_red', 12: 'la_piramide',
          13: 'el_encubierto', 14: 'las_notas', 15: 'la_carga',
          16: 'el_seguimiento', 17: 'el_paquete', 18: 'los_audifonos',
          19: 'las_24_horas', 20: 'el_computador', 21: 'la_orden',
          22: 'la_exclusion', 23: 'la_casa_vigilada', 24: 'porras'}

CORTE = {
 1: ('g01_casa', 'Para investigar'),
 2: ('g01_casa', 'La Ley'),
 3: ('g02_control', 'Como interfieren'),
 4: ('g02_control', 'todas están'),
 5: ('g02_control', 'su ejecución'),   # 7 nov: la ventana tenía 21 cuadros; abre en la pausa
 6: ('g03_ventana', 'y recorramos'),
 7: ('g04_personas', 'La vigilancia'),
 8: ('g04_personas', 'de forma directa'),
 9: ('g05_cosas', 'La vigilancia'),
 10: ('g05_cosas', 'que se sospecha'),
 11: ('g06_analisis', 'El análisis'),
 12: ('g06_analisis', 'su estructura'),
 13: ('g07_encubierto', 'Con la actuación'),
 14: ('g07_encubierto', 'Puede documentar'),
 15: ('g08_entrega', 'La entrega'),
 16: ('g08_entrega', 'para identificar'),
 17: ('g09_correspondencia', 'La retención'),
 18: ('g10_interceptacion', 'La interceptación'),
 19: ('g10_interceptacion', 'y debe someterse'),
 20: ('g11_internet', 'La recuperación'),
 21: ('g12_bases', 'Y la búsqueda'),
 22: ('g13_exclusion', 'Una regla'),
 23: ('g14_porras', 'Cómo se aplican'),
 24: ('g14_porras', 'Escuchemos'),
}

EXTRA_TOKENS = {
 'jueza_gar': ('the judge of guarantees, a Colombian woman of about sixty, '
               'short curly grey hair, no glasses, in a plain black blazer over '
               'a plain grey blouse'),
 'encubierto': ('AN UNDERCOVER AGENT dressed as a miner, a Colombian man in a '
                'plain faded grey T-shirt, plain dark trousers and rubber '
                'boots, seen ONLY FROM BEHIND or in profile turned away: his '
                'face is never visible'),
 'mineros': ('two dredge workers in plain grey work clothes and rubber boots'),
 'empleada': ('the clerk of the courier office, a Colombian woman of about '
              'thirty, dark hair tied back, in a plain grey polo shirt'),
 'perito_inf': ('a computer forensics expert of the prosecution service, a '
                'Colombian man of about thirty, short dark hair, in a plain '
                'light grey shirt'),
 'porras': ('A MAN of about sixty in a plain dark suit, seen ONLY as a dark '
            'silhouette from behind against the window: no face, no features'),
}

# la fiscal y la jueza son las mismas de todo el curso; el resto, madres de
# este video (ola 2)
REF = {
 2: ('DA_V01_r30_la_fiscal', 'lugar', 'It is the SAME prosecutor, at her own desk.'),
 4: (3, 'lugar', 'It is the SAME judge in the SAME office, closer.'),
 19: (3, 'lugar', 'It is the SAME office and the SAME judge.'),
 22: (3, 'gente', 'It is the SAME judge, now in the hearing room.'),
 11: ('DA_V02_r10_el_analisis', 'lugar', 'It is the SAME analyst in the SAME analysis room.'),
 12: ('DA_V02_r10_el_analisis', 'lugar', 'It is a table of the SAME analysis room.'),
 18: ('DA_V02_r10_el_analisis', 'gente', 'It is the SAME analyst, at night.'),
 21: ('DA_V02_r10_el_analisis', 'lugar', 'It is the SAME analyst in the SAME room; the prosecutor is the one of the first reference.'),
 7: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator is the SAME man.'),
 9: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator is the SAME man.'),
 16: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator is the SAME man.'),
 17: ('DA_V01_r28_la_intervencion', 'gente', 'The investigator is the SAME man.'),
 23: (1, 'lugar', 'It is the SAME house in the SAME street, from further away.'),
 13: ('DA_V01_r03_la_draga', 'lugar', 'It is the SAME dredge.'),
 6: ('DA_V01_r23_dragas_aereo', 'lugar', 'It is the SAME river, further downstream at the town.'),
}
REF2 = {19: 'DA_V01_r30_la_fiscal',
        21: 'DA_V01_r30_la_fiscal', 11: 'DA_V01_r30_la_fiscal'}

ANCLA_DE = {3: 'oficina', 1: 'pueblo', 5: 'oficina', 8: 'rural', 10: 'pueblo', 14: 'noche_int',
            15: 'rural', 20: 'oficina', 24: 'oficina'}

CON_PERSONA = {2, 3, 4, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24}
AEREOS = {6, 8}
CENITALES = {8, 12}
SOLO_MANOS = set()
TOPE_SIN_GENTE = 3
TOTAL = 2400
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

GRIS = (20, 110)
SIN_TECHO = {14, 18}

# el gráfico del control judicial (r04) y los nueve rótulos-enlace de las
# técnicas: el círculo sobre la placa y el nombre con su artículo (mg_da)
GRAFICOS = {4: 'control', 7: 't239', 9: 't240', 11: 't241', 13: 't242',
            15: 't243', 17: 't233', 18: 't235', 20: 't236', 21: 't244'}

KLING = {
 1: ('fija', 'A light breeze stirs the leaves of the trees and the banana plants '
     'around the closed house and lifts one edge of the grey tarpaulin over the '
     'engine; the river flows slowly past in the foreground.'),
 2: ('fija', 'She runs the tip of her pencil slowly down the page of the open law '
     'book, line by line, stops on one line, and lifts her eyes to the '
     'photograph of the house beside the book.'),
 3: ('fija', 'The judge reads the request, her eyes moving slowly along the lines, '
     'then lowers the pages a little and looks up over them at the prosecutor; '
     'the prosecutor in the foreground keeps her head level and still.'),
 5: ('fija', 'A light breeze moves the palm trees and the banana plants outside the '
     'window; the wide river beyond flows slowly; the two wooden shutters stay '
     'as they are.'),
 6: ('aire', 'The camera glides slowly forward high over the river toward the '
     'dredges upriver; the pale ochre-grey plume drifts slowly downstream.'),
 8: ('libre', 'The white pickup truck drives steadily along the red-earth road from '
     'the bottom of the frame toward the top, its shadow travelling beside it. '
     'The camera hovers in place high above, looking straight down.'),
 10: ('fija', 'The small security camera on its pole turns slowly from the shutter '
      'toward the yard and stops there; a light breeze stirs the trees behind the '
      'warehouse and ripples the river in the foreground.'),
 11: ('fija', 'The analyst leans a little toward the wall screen; the prosecutor, '
      'her hand on the backrest of his chair, turns her head to him and says a few '
      'words; he nods once. The screen stays as it is.'),
 13: ('fija', 'The men keep working the black suction hose together, swaying it '
      'slowly as the current pulls; the man beside him talks and he nods; the '
      'ochre-grey water swirls around the edge of the deck. Every man stays in '
      'his place on the deck.'),
 14: ('fija', 'He writes slowly in the small notebook on his knee, his pen moving '
      'along the line; he pauses, lifts his head toward the dark doorway for a '
      'moment, and goes back to writing. The bulb light stays steady.'),
 16: ('libre', 'The car drives steadily along the road behind the loaded truck, '
      'keeping the same distance; the road and the countryside slide slowly '
      'toward the camera on both sides; the investigator keeps both hands on the '
      'wheel. The camera rides in the car.'),
 17: ('fija', 'She holds the parcel steady on the scale with both hands and looks '
      'up from it at the investigator; he holds up the order and points at it '
      'with one finger while he speaks. The parcel stays on the scale.'),
 18: ('fija', 'He listens, writes a short line in the notebook with his pen and '
      'pauses; on the screen the grey waveform scrolls slowly from right to left.'),
 19: ('fija', 'The prosecutor walks in from the door to the front of the desk, the '
      'folder under her arm, and stops there; the judge looks up at her from '
      'behind the desk.'),
 20: ('fija', 'He types a few keys on his keyboard with one hand and watches his '
      'screen; the grey bars on the screen fill slowly from left to right. The '
      'seized laptop in its bag stays where it is.'),
 21: ('fija', 'She holds out the one-page order and speaks; he lifts his eyes from '
      'his screen to her face and nods once. The order stays in her hand.'),
 22: ('fija', 'The judge sets the folder she holds down apart on the far corner of '
      'the desk and rests both hands on the desk; at the defence table the lawyer '
      'leans forward a little and watches her.'),
 23: ('fija', 'A light breeze moves the trees at the end of the street and the '
      'tarpaulin over the engine; the power cables sway slightly. The parked grey '
      'car in the foreground stays where it is.'),
 24: ('fija', 'He breathes slowly and turns his head a little to look further '
      'along the river, then stays still at the window; outside the river flows '
      'past.'),
}
# r12 (las fotos sobre la mesa) no va: es papel, y el plano es la quietud.
# r07, r09 y r15 tampoco: el rotulo marca a alguien que el clip moveria
# (el empresario caminando, el lanchero, la lancha).
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
CUADROS = {1: 137, 2: 164, 3: 139, 4: 144, 5: 73, 6: 68, 7: 152, 8: 118, 9: 114, 10: 167, 11: 122, 12: 141, 13: 217, 14: 211, 15: 139, 16: 166, 17: 195, 18: 130, 19: 151, 20: 274, 21: 308, 22: 287, 23: 108, 24: 80}
for _n, _c in CUADROS.items():
    R[_n] = (_c,) + R[_n][1:]
TOTAL = 3805
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)
