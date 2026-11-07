# -*- coding: utf-8 -*-
r"""VIDEO 01 · Problemática ambiental y criminalidad (U1 L1, video
introductorio). Narra Carlos. 34 ranuras.

LA PROGRESIÓN (lo que pide la nota: del daño a la dinámica criminal)
    r01-r02   la selva intacta desde el aire · el río donde entra el agua turbia
    r03-r06   la draga · el mercurio en la batea · la descarga · el pescador
    r07       las cifras del oro de aluvión (gráfico sobre la mina vista de arriba)
    r08-r09   la retroexcavadora · el desierto de pozos y arena
    r10-r12   la tala · la quema y el potrero · las cifras del IDEAM (gráfico)
    r13-r18   los seis motores, en montaje rápido
    r19-r20   el combustible que llega · el dinero que se cuenta
    r21-r23   el grupo armado en el embarcadero · el cobro · la cifra (gráfico)
    r24-r27   el oro en la balanza · la finca · la oficina · la máquina nueva
    r28-r29   la intervención de la draga · la máquina sola
    r30-r33   la fiscal · el eslabón visible · subir por la cadena (gráfico)
    r34       el río limpio

EL AMARILLO SIGUE AL DINERO (base_da): el motor de la draga, el oro, la
retroexcavadora, la máquina nueva en la cama baja. En los planos de la gente
del río, del bosque y de la Fiscalía, ningún saturado.

QUIÉN LLEVA CARA
    El minero, el pescador, la mujer del río, el colono, el comprador, la
    fiscal, el investigador, la técnica. De espaldas o en silueta: el grupo
    armado, el cobrador, el empresario de la oficina, el dueño que cuenta el
    dinero, el operador en la cabina.

R[n] = (cuadros, registro, gente, acento, fuego, lugar, escena)
"""

R = {}

R[1] = (78, 'aire', (), None, False, 'selva_aire', '''
High aerial view of the Colombian Amazon rainforest, the camera far above and
looking down at a steep angle, the horizon level near the top of the frame. An
unbroken canopy of rounded tree crowns of many sizes fills the frame; a wide
river winds through it in two slow S-shaped meanders, pale sandbanks on the
inside of the bends, low white mist caught between the crowns along the
water. Vast, quiet, intact. No settlement, no road, no boat, no clearing.
''')

R[2] = (169, 'dia', (), None, False, 'rio', '''
Wide shot from a low riverbank under the trees, the camera at standing height,
perfectly level, looking across a wide river of the Colombian Pacific
lowlands. Two waters meet in the middle of the frame and do not mix: on the
right, the clean river, dark grey-green and glassy; from the left, a broad
tongue of opaque ochre-grey muddy water pushing into it from upstream, with a
sharp, wavy seam between the two. Overhanging branches and big leaves frame
the top and the left edge of the picture. Nobody in the frame.
''')

R[3] = (100, 'dia', ('minero',), 'the casing of the engine and pump on the dredge', False, 'draga', '''
Wide shot of the dredge anchored in the middle of the wide river, seen from a
small boat a stone's throw away, the camera low over the water, perfectly
level. The whole dredge is in frame, a little right of centre: the plank deck
on its barrels, the grey tarpaulin roof, the mustard-yellow engine and pump
under it, the thick black suction hose plunging into the river, the sluice box
at the back pouring grey water and sand into the river, where an ochre plume
spreads downstream. %(minero)s stands on the deck guiding the suction hose
with both hands, mid-action, his body leaning into it. The river around the
dredge is opaque ochre-grey; the forest wall on the far bank. He appears ONCE.
''')

R[4] = (40, 'dia', ('minero',), 'the tiny grains of gold in the pan', False, 'draga', '''
Close detail shot on the deck of the dredge, the camera low and close,
perfectly level, looking at %(minero)s from the side: his two forearms and
hands, wet, hold a wide shallow wooden gold pan (batea) at waist height and
tilt it in a slow circle; in the pan, a thin layer of grey sand with a cluster
of small bright silver beads of liquid mercury rolling together, and among
them a few tiny grains of gold. His soaked grey T-shirt and his chest fill the
top of the frame; his face is out of frame above. Exactly two hands, each
with five fingers, both attached to his arms. Planks and the river behind,
softly simplified.
''')

R[5] = (88, 'dia', (), None, False, 'draga', '''
Medium shot of the back of the dredge from the water, the camera low over the
river surface, perfectly level. The inclined wooden sluice box lined with dark
carpet pours a steady stream of grey water and sand off the end of the deck
into the river; where it falls, an opaque ochre-grey plume billows and spreads
away downstream across the frame, darkening the river. A blue-grey fuel drum
and a coil of rope at the edge of the deck. The forest on the far bank, soft.
Nobody in the frame.
''')

R[6] = (109, 'dia', ('pescador',), None, False, 'rio', '''
Medium shot of %(pescador)s standing in his narrow wooden dugout canoe on the
river, a little downstream of a village of stilt houses, the camera low at
water level and perfectly level. He hauls in his hand-made cast net with both
hands, mid-pull; in the net only three small fish. The water around the canoe
is opaque ochre-grey. His face in three-quarter view, eyes down on the net,
his mouth a straight line, the brows slightly drawn: a man reading what the
river gives him. The stilt houses small in the background. He appears ONCE.
''')

R[7] = (351, 'aire', (), 'the paint of the small machines', False, 'mina', '''
High aerial view of an open-pit alluvial gold mining zone in the lowland
rainforest of Choco, the camera far above looking down at a steep angle, the
horizon level near the top. A river turned opaque ochre braids between bare
grey sandbars; along it, a patchwork of rectangular pits filled with ochre
and grey-green stagnant water, heaps of sand, and a few tiny excavators
(mustard-yellow dots); the dark rainforest closes in around the scar on every
side. The LEFT half of the picture is calmer -forest and river- because a
graphic will be laid over it. No settlement, no lettering.
''')

R[8] = (82, 'dia', ('operador',), 'the excavator', False, 'mina', '''
Medium-wide shot at ground level at the edge of the mine, the camera at
standing height, perfectly level. %(retro)s, seen from the side in
three-quarter view, digs into the bank: its boom raised, the bucket coming up
full of wet grey-ochre earth and gravel that spills over its lip, water
streaming from it. In the glass cabin, small, %(operador)s at the controls.
Behind, the tall wall of standing rainforest at the top of the bank, felled
trunks pushed aside at its foot; in the foreground a pool of opaque ochre
water.
''')

R[9] = (160, 'dia', (), None, False, 'mina', '''
Wide shot from the top of a sand mound over the mined land, the camera at
standing height, perfectly level, looking across a wasteland: wide stagnant
ponds of opaque ochre and grey-green water separated by bare mounds of grey
sand and gravel, a few dead white tree trunks standing in the water, felled
trunks heaped at the edges, and far behind, the dark line of the rainforest
that used to cover all of it. Silent, empty. Nobody in the frame.
''')

R[10] = (54, 'dia', ('motosierrista',), None, False, 'tala', '''
Medium shot in the forest at the edge of the clearing, the camera at standing
height, perfectly level, three metres from %(motosierrista)s. He leans into a
huge tree trunk, the chainsaw biting deep into its base, a spray of pale
sawdust flying from the cut, his shoulders set, his face in profile with the
eyes narrowed against the dust. Behind him the clearing full of felled trunks
and, beyond, the tall standing forest. He appears ONCE.
''')

R[11] = (58, 'contra_ext', ('vaquero',), None, True, 'quema', '''
Wide shot across a burned clearing, the camera at standing height, perfectly
level. In the foreground, charred grey stumps and blackened fallen trunks
over ashen ground, pale grey smoke drifting low across the frame from right to
left. Beyond the burn, already turned to pasture, a few white-grey zebu cattle
graze among stumps, and %(vaquero)s rides slowly along the fence. The tall
dark forest wall behind, partly veiled by the smoke.
''')

R[12] = (282, 'aire', (), None, True, 'ninguno', '''
High aerial view of the agricultural frontier of the Colombian Amazon
(Caqueta), the camera far above looking down at a steep angle, the horizon
level near the top. The dark unbroken rainforest on the far side gives way to
a ragged edge of freshly opened clearings: geometric patches of grey pasture,
burned brown-grey patches with thin trails of pale smoke, isolated lone trees
standing in the open, a straight red-earth track. The RIGHT half of the
picture is calmer -forest and pasture- because a graphic will be laid over
it. No settlement, no lettering.
''')

R[13] = (117, 'dia', ('colono',), None, False, 'potrero', '''
Medium shot at the edge of the forest, the camera at standing height,
perfectly level. %(colono)s stretches a new strand of barbed wire between two
freshly cut wooden posts, pulling it taut with both hands, mid-pull; the line
of new posts runs straight into the stumps of the cleared forest, claiming
it. Behind him, the tall standing forest still uncut. He appears ONCE.
''')

R[14] = (47, 'dia', ('vaquero',), None, False, 'potrero', '''
Wide shot of a new pasture opened in the forest, the camera at standing
height, perfectly level. A herd of white-grey zebu cattle grazes among grey
stumps across the whole frame; lone tall trees left standing here and there;
%(vaquero)s small at the far side; the dark wall of the forest beyond.
''')

R[15] = (53, 'dia', (), None, False, 'coca', '''
Medium-wide shot of a small field of coca bushes in rows in a clearing of the
Amazon forest, the camera at standing height, perfectly level: knee-high
leafy shrubs in rows running away from the camera, grey stumps and fallen
branches between the rows, the dark forest wall all around. Nobody in the
frame.
''')

R[16] = (51, 'aire', (), None, False, 'via', '''
High aerial view looking straight down the line of a freshly opened red-earth
track that cuts through the Amazon rainforest like a scar, from the bottom of
the frame to the horizon; narrow cleared strips open on both sides of it. Far
along the track, one tiny motorcycle with a rider. The canopy dark and
unbroken on both sides.
''')

R[17] = (59, 'dia', (), 'the excavator', False, 'mina', '''
Wide shot of the mine pit at ground level, the camera at standing height,
perfectly level: %(retro)s stands idle on a sand mound above a pond of opaque
ochre water, its bucket resting on the ground, the forest wall beyond.
Nobody in the frame.
''')

R[18] = (84, 'dia', ('lanchero',), None, False, 'madera', '''
Medium-wide shot of a muddy river landing in the Colombian Amazon, the camera
at standing height, perfectly level. Stacks of freshly sawn planks and
squared beams are piled on the bank; %(lanchero)s carries one long plank on
his shoulder down a narrow board to a long wooden riverboat already loaded
with timber, mid-stride. The brown river and the forest beyond.
''')

R[19] = (154, 'dia', ('lanchero', 'minero'), 'the casing of the engine and pump on the dredge', False, 'draga', '''
Medium-wide shot on the river beside the dredge, the camera low over the water,
perfectly level. A long wooden boat with an outboard motor, steered by
%(lanchero)s, comes alongside the dredge loaded with a row of blue-grey
plastic fuel drums and a plain white sack; %(minero)s leans from the deck and
grabs the side of the boat to bring it in. The mustard-yellow engine visible
under the tarpaulin. Each person appears ONCE.
''')

R[20] = (98, 'hero', ('dueno',), None, False, 'draga', '''
Medium shot under the tarpaulin roof of the dredge at dusk, the camera at
seated height, perfectly level, from behind and beside %(dueno)s, who sits on
an upturned plastic crate. On a plank laid across a fuel drum in front of him,
a plain plastic bag open and a thick stack of banknotes; his two hands count
the notes, one note held up between finger and thumb. A single bare bulb
hangs from the roof pole. The banknotes are plain grey-green paper with no
readable print. His face is not visible.
''')

R[21] = (106, 'contra_ext', ('armados',), None, False, 'embarcadero', '''
Wide shot of the small floating wooden landing at a river bend, the camera on
the water at a distance, low and perfectly level. On the landing,
%(armados)s stand with their backs half to us, looking out over the river,
one of them talking into the small radio. The wide grey-brown river in the
foreground, the stilt hut and the dense forest behind them. Far downstream,
tiny, the dark shape of a dredge. Calm, controlled, ominous.
''')

R[22] = (123, 'contra_ext', ('cobrador', 'lanchero'), None, False, 'embarcadero', '''
Medium shot at the edge of the floating landing, the camera at standing
height on the landing, perfectly level, behind %(cobrador)s. A long wooden
boat has stopped against the landing; standing in it, %(lanchero)s, hands up a
folded bundle of banknotes; the man of the armed group takes it with one
hand and holds open his small notebook in the other. The boatman's face is
seen in three-quarter view, his eyes lowered, his mouth shut. The banknotes
are plain grey-green paper with no readable print. Each person appears ONCE.
''')

R[23] = (163, 'aire', (), 'the paint of the dredges', False, 'rio', '''
High aerial view of a long stretch of a wide river of the Colombian Pacific
lowlands, the camera far above looking down at a steep angle, the horizon
level near the top. Along the river, five small dredges anchored one after
another (each a tiny raft with a grey roof and a mustard-yellow engine), each
trailing an ochre plume downstream, so that the river grows muddier from top
to bottom of the frame; the forest dark on both banks. The LEFT half of the
picture is calmer -forest- because a graphic will be laid over it.
''')

R[24] = (65, 'dia', ('comprador',), 'the small grains and nuggets of gold on the scale', False, 'compraventa', '''
Medium-close shot across the glass counter of the gold-buying shop, the camera
at standing height, perfectly level. %(comprador)s, behind the counter, tips a
small heap of gold grains and little nuggets from a folded paper onto the pan
of the precision scale, his eyes on the display through his reading glasses.
The street outside the open security grille is bright and soft. He appears
ONCE.
''')

R[25] = (101, 'dia', ('colono', 'dueno'), None, False, 'finca', '''
Medium-wide shot at the wooden gate of a new cattle ranch, the camera at
standing height, perfectly level. Over the top bar of the gate, %(colono)s, and
%(dueno)s, shake hands -a deal closed-: the settler on the far side of the gate, facing
the camera, the second man on the near side with his back to the camera, his
hand and forearm stretched over the bar, palm sideways, thumb on top; a plain folded sheet of paper
sticks out of the back pocket of the second man's trousers. Behind them the wide new pasture with
white-grey zebu cattle and grey stumps, and the forest far away.
''')

R[26] = (143, 'dia', ('empresario',), None, False, 'oficina_empresa', '''
Medium shot in the city office, the camera at seated height behind and beside
%(empresario)s, perfectly level. He sits at the wide glass desk and signs a
plain document among a neat stack of plain papers, his pen mid-stroke; the
floor-to-ceiling window in front of him shows the Colombian city and the
mountains. The papers show only plain grey bars. His face is not visible.
''')

R[27] = (109, 'dia', (), 'the excavator on the trailer', False, 'carretera', '''
Medium-wide shot on a red-earth road into the Amazon forest, the camera at
standing height at the roadside, perfectly level. A heavy truck pulling a
low-bed trailer drives toward the forest, mid-way across the frame, carrying a
brand-new %(retro_corta)s; red mud splashes from the ruts under its wheels.
The cab of the truck is plain grey with no markings. The forest closes in at
the end of the road.
''')

R[28] = (156, 'dia', ('tecnica', 'investigador'), 'the casing of the engine and pump on the dredge', False, 'draga', '''
Medium-wide shot on the dredge, now stopped and intervened, the camera on the
deck at standing height, perfectly level. In the foreground %(tecnica)s
kneels at the edge of the deck and fills a plain clear sample bottle with
river water, her eyes on the bottle; behind her %(investigador)s photographs
the mustard-yellow engine with a plain camera. Moored alongside the dredge,
%(lancha)s, with two small figures in plain dark olive at its bow, far away
and not detailed. Each person appears ONCE.
''')

R[29] = (116, 'contra_ext', (), 'the excavator', False, 'mina', '''
Wide shot of the mine pit at the end of the day, the camera at standing
height, perfectly level. %(retro)s stands alone and still in the middle of the
wasteland of ochre ponds and sand, its bucket lowered to the ground and its
cabin door open; around its tracks a ring of plain grey-and-white plastic
barrier tape on short stakes, with nothing printed on it. The dark forest
behind. Nobody anywhere. The machine is stopped; the place around it is not
healed.
''')

R[30] = (187, 'dia', ('fiscal',), None, False, 'despacho', '''
Medium shot of %(fiscal)s at her desk in the prosecutor's office, the camera at
seated height in front of the desk, perfectly level. She studies two large
printed satellite images laid side by side on the desk -the same patch of
forest seen twice, intact on the left, cut into grey geometric clearings on
the right-, one hand flat on the left print, the pencil in the other hand
pointing at a clearing on the right. Her eyes on the prints, the brows drawn
together. She appears ONCE.
''')

R[31] = (101, 'dia', ('fiscal',), None, False, 'despacho', '''
Close shot of %(fiscal)s at her desk, the camera at her seated eye level,
perfectly level, her face and shoulders filling the right half of the frame
in three-quarter view. She has looked up from the prints and looks off-frame
to the left, past the camera: resolved, steady, her mouth a straight line,
the corners not raised. The blurred plain shelves of case folders behind her.
She appears ONCE.
''')

R[32] = (115, 'hero', ('minero',), 'the casing of the engine and pump on the dredge', False, 'draga', '''
Close shot of %(minero)s on the dredge at night, the camera at his eye level,
perfectly level, his face and shoulders in three-quarter view filling the
left half of the frame, lit from the side by the single white work lamp of
the dredge. Sweat and river water on his face; he looks out at the dark river,
tired and watchful, his mouth a straight line. Behind him, out of focus, the
mustard-yellow engine under the tarpaulin and the dark river. He appears ONCE.
''')

R[33] = (202, 'dia', ('fiscal', 'investigador'), None, False, 'despacho', '''
Medium-wide shot in the prosecutor's office, the camera at standing height,
perfectly level. On the wall, a large plain cork board with a vertical chain of
plain cards and small photographs connected by taut threads, rising from the
bottom of the board to the top: every card and photograph shows only plain
grey bars or a blank grey shape, no face, no letter. %(fiscal)s, in
three-quarter back view, reaches up and pins a new blank card at the very top
of the chain; %(investigador)s stands beside her with a folder under his arm,
looking up at the board. Each person appears ONCE.
''')

R[34] = (71, 'aire', ('pescador',), None, False, 'rio', '''
Aerial view low over a wide clean river of the Colombian Pacific lowlands
early in the day, the camera above the water looking ahead along the river,
the horizon level. The water is dark grey-green and glassy, with soft mist
along the forested banks; in the middle of the river, small, %(pescador)s
paddles his narrow dugout canoe upstream, leaving a long gentle wake. Calm,
wide, alive.
''')

NOMBRE = {1: 'la_selva', 2: 'las_dos_aguas', 3: 'la_draga', 4: 'la_batea',
          5: 'la_descarga', 6: 'el_pescador', 7: 'aluvion_aereo',
          8: 'la_retro', 9: 'los_pozos', 10: 'la_tala', 11: 'la_quema',
          12: 'frontera_aerea', 13: 'acaparamiento', 14: 'ganaderia',
          15: 'cultivos', 16: 'vias', 17: 'mineria', 18: 'madera',
          19: 'combustible', 20: 'el_dinero', 21: 'el_embarcadero',
          22: 'el_cobro', 23: 'dragas_aereo', 24: 'la_balanza', 25: 'la_finca',
          26: 'la_oficina', 27: 'la_maquina_nueva', 28: 'la_intervencion',
          29: 'la_maquina_sola', 30: 'la_fiscal', 31: 'la_fiscal_cerca',
          32: 'el_eslabon', 33: 'la_cadena', 34: 'el_rio_limpio'}

# los cortes salen de la voz (STT palabra por palabra); se rellenan con
# `cortes_da.py` y la suma tiene que dar TOTAL.
CORTE = {
 1: ('d01_techo', 'Desde'), 2: ('d01_techo', 'Pero'),
 3: ('d02_draga', 'En'), 4: ('d02_draga', 'El oro'), 5: ('d02_draga', 'y el metal'),
 6: ('d02_draga', 'entra'),
 7: ('d03_aluvion', 'Según'),
 8: ('d04_fosas', 'En'), 9: ('d04_fosas', 'y lo dejan'),
 10: ('d05_bosque', 'Lejos'), 11: ('d05_bosque', 'se quema'), 12: ('d05_bosque', 'Según'),
 13: ('d06_motores', 'Detrás'), 14: ('d06_motores', 'la ganadería'),
 15: ('d06_motores', 'los cultivos'), 16: ('d06_motores', 'la apertura'),
 17: ('d06_motores', 'la explotación'), 18: ('d06_motores', 'y el aprovechamiento'),
 19: ('d07_dinero', 'Nada'), 20: ('d07_dinero', 'y donde'),
 21: ('d08_grupos', 'En'), 22: ('d08_grupos', 'imponen'), 23: ('d08_grupos', 'Más'),
 24: ('d09_lavado', 'El oro'), 25: ('d09_lavado', 'la tierra'),
 26: ('d09_lavado', 'Las ganancias'), 27: ('d09_lavado', 'y regresan'),
 28: ('d10_intervencion', 'Cuando'), 29: ('d10_intervencion', 'Pero'),
 30: ('d11_infracciones', 'Por eso'), 31: ('d11_infracciones', 'Son'),
 32: ('d12_cadena', 'Quien'), 33: ('d12_cadena', 'La investigación'),
 34: ('d13_curso', 'Ese'),
}

EXTRA_TOKENS = {
 'retro': 'a hydraulic excavator of the ordinary tracked kind, its body, boom '
          'and bucket painted MATTE MUSTARD-YELLOW and streaked with dried mud, '
          'no brand, no number, no lettering anywhere on it',
 'retro_corta': 'tracked hydraulic excavator painted MATTE MUSTARD-YELLOW, with '
                'no brand, number or lettering',
 'lancha': 'a plain grey river patrol boat with no markings, numbers, flags or '
           'lettering anywhere',
}

CON_PERSONA = {3, 4, 6, 8, 10, 11, 13, 14, 16, 18, 19, 20, 21, 22, 24, 25, 26,
               28, 30, 31, 32, 33, 34}
AEREOS = {1, 7, 12, 16, 23, 34}
CENITALES = set()
SOLO_MANOS = {4}
TOPE_SIN_GENTE = 3
TOTAL = 3992
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

# los gráficos (09 MOTION GRAPHICS, `graficas/mg_da.py`) van en V5 MOTION
# GRAPHICS encima de estas ranuras; los motores, de la r13 (cuando la voz dice
# «el acaparamiento») a la r18.
GRAFICOS = {7: 'aluvion', 12: 'ideam', 13: 'motores', 23: 'municipios', 33: 'cadena'}

# el color (da_pieza): la sombra se levanta con la curva suave de la serie
# -la noche es gris, no negra- y las dos de noche van sin techo al medio tono
# del registro hero (la placa de la r20 y la r32 salen casi negras).
GRIS = (20, 110)
SIN_TECHO = {20, 32}

# la placa madre de cada lugar/persona (ola 2: se piden cuando la madre esté
# aprobada). (madre, 'lugar'|'mismo', nota)
REF = {
 4: (3, 'lugar', 'A CLOSE DETAIL of the SAME dredge worker on the SAME dredge.'),
 5: (3, 'lugar', 'It is the SAME dredge, seen from behind.'),
 9: (8, 'lugar', 'It is the SAME mine.'),
 14: (13, 'lugar', 'It is the SAME new pasture at the edge of the SAME forest.'),
 17: (8, 'lugar', 'It is the SAME mine and the SAME excavator, now idle.'),
 19: (3, 'lugar', 'It is the SAME dredge and the SAME worker.'),
 20: (3, 'lugar', 'It is the SAME dredge, under its roof, at dusk.'),
 22: (21, 'lugar', 'It is the SAME landing and the SAME men.'),
 25: (14, 'lugar', 'It is the SAME pasture, now a ranch.'),
 28: (3, 'lugar', 'It is the SAME dredge, now stopped by the authorities.'),
 29: (8, 'lugar', 'It is the SAME mine and the SAME excavator, now stopped.'),
 31: (30, 'lugar', 'It is the SAME prosecutor in the SAME office, closer.'),
 32: (3, 'lugar', 'It is the SAME dredge worker on the SAME dredge, at night.'),
 33: (30, 'lugar', 'It is the SAME prosecutor in the SAME office.'),
 34: (6, 'lugar', 'It is the SAME fisherman in the SAME canoe on a clean stretch of river.'),
}
OLA1 = sorted(n for n in range(1, 35) if n not in REF)

# el ancla de estilo de la serie cuando no hay madre (prompts_da.ANCLA)
ANCLA_DE = {20: 'noche_int', 24: 'pueblo', 26: 'oficina', 30: 'oficina',
            31: 'oficina', 32: 'noche_ext', 33: 'oficina'}

HOJAS = {}

# 7 nov: el movimiento (V2, Kling 2.5 a 720p, 5 s, desde la placa GRADUADA
# como cuadro inicial). La regla de la casa: al modelo se le dice que pasa, con
# su destino, no que no pasa; la camara quieta se dice una vez; nadie queda «a
# punto de» tocar algo; el papel no se anima; nada sale de cuadro. Sin clip:
# las ranuras bajo los graficos (7, 12, 23, 33), las que valen por quietas
# (9 los pozos, 17 y 29 la maquina sola) -esas llevan la camara de la casa-.
# 'aire' = toma de dron: ahi la camara si avanza.
KLING = {
 1: ('aire', 'The camera glides slowly forward high over the rainforest, following '
     'the river; the low white mist drifts gently along the water between the '
     'tree crowns.'),
 2: ('fija', 'The opaque ochre-grey muddy water slowly pushes further into the '
     'dark clean water; the wavy seam between the two waters curls and ripples '
     'as both currents flow; the leaves of the overhanging branches stir in the '
     'breeze.'),
 3: ('fija', 'The river churns and bubbles around the suction hose under the '
     'dredge; the sluice at the back pours a steady stream of grey water and '
     'sand into the river; the dredge worker on the deck guides the hose with '
     'both hands, shifting his weight; the tarpaulin roof ripples in the wind.'),
 4: ('fija', 'His two hands swirl the wooden gold pan in slow circles; the muddy '
     'water washes over the rim and runs off, leaving the dark sand and the '
     'tiny gold grains at the bottom of the pan.'),
 5: ('fija', 'The sluice keeps pouring grey water and sand off the end of the '
     'deck; where it falls the ochre-grey plume billows and spreads further '
     'downstream across the river.'),
 # 7 nov: la placa trae una red de mano con peces, no atarraya, y «la sube a
 # la canoa» salio con la red cambiando de forma y salpicones; quieto, sirve
 6: ('fija', 'He holds the net up with both hands, still and steady, and looks at '
     'the few small fish caught in it; the fish wriggle a little in the net and '
     'water drips from it into the river; the canoe rocks very gently; he '
     'breathes. The net and the pole stay where they are.'),
 8: ('fija', 'The excavator lifts its bucket full of wet earth, swings it to the '
     'side over the mound and dumps the earth, which slides down the mound; the '
     'operator in the cab works the levers.'),
 10: ('fija', 'He keeps sawing into the trunk with the chainsaw, leaning his '
      'weight into it; pale sawdust sprays out of the cut and drifts to the '
      'ground. The tree stays standing.'),
 11: ('fija', 'Pale grey smoke drifts low across the burned clearing from right to '
      'left; the zebu cattle graze and one walks a few steps; the cowhand rides '
      'slowly at a walk along the far side.'),
 13: ('fija', 'He pulls the barbed wire taut with both hands, wraps it twice '
      'around the fresh post and lets go; the wire stays tight.'),
 14: ('fija', 'The zebu cattle graze, lowering and raising their heads, and two '
      'of them walk slowly a few steps; the cowhand rides at a slow walk across '
      'the far side of the pasture.'),
 15: ('fija', 'A light breeze moves through the rows of coca bushes; the leaves '
      'stir and sway; the forest wall behind stays still.'),
 16: ('aire', 'The camera glides slowly forward along the red-earth track high '
      'above the forest; far ahead, the tiny motorcycle rides away along the '
      'track.'),
 # 7 nov: al dejar la tabla, la tabla se deformaba sobre su cabeza (2,1 s);
 # caminando con ella al hombro sale entera
 18: ('fija', 'He walks slowly and carefully down the narrow board toward the '
      'riverboat, step by step, with the one long plank resting steady on his '
      'right shoulder the whole time, his right hand holding it; he stops at the '
      'edge of the boat. The plank stays the same long straight plank on his '
      'shoulder from the first frame to the last.'),
 19: ('fija', 'The long wooden boat drifts the last metre and bumps gently '
      'against the dredge; the dredge worker grips the handle of the first '
      'fuel drum and lifts it onto the deck; the boatman holds the boat steady.'),
 20: ('fija', 'He counts the banknotes from one hand to the other, one by one, '
      'and lays the counted bundle on the stack; the work lamp swings very '
      'slightly under the tarpaulin.'),
 21: ('fija', 'The man with the radio lowers it from his mouth and clips it back '
      'on his chest; the three men stay in their places on the landing, looking '
      'out over the river; the river flows past the landing.'),
 22: ('fija', 'The boatman holds up the folded bundle; the man of the armed group '
      'takes it, slips it inside his jacket and writes one line in his small '
      'notebook; the boatman lowers his hands and his eyes.'),
 24: ('fija', 'The last gold grains slide off the folded paper onto the pan of '
      'the scale; he sets the paper down on the counter and reads the scale '
      'through his glasses, without a smile.'),
 25: ('fija', 'They shake hands firmly twice, let go, and the settler rests both '
      'hands on the top bar of the gate; behind them the zebu cattle graze.'),
 # 7 nov: SIN CLIP. Kling levanto una hoja (el papel no se anima) y el
 # lapicero desaparecio a 1,5 s: queda la placa con la camara de la casa
 # 26: ('fija', 'He finishes the signature, puts the pen down on the desk and lays '
      #  'the signed document on top of the stack; outside the window the city '
      #  'stays far away.'),
 27: ('fija', 'The truck drives slowly forward along the road toward the forest, '
      'the trailer and the excavator rolling with it; red mud splashes from the '
      'ruts under the wheels. The truck stays inside the frame.'),
 28: ('fija', 'She screws the cap onto the sample bottle and stands it upright on '
      'the deck beside her; behind her the investigator takes another photograph '
      'of the engine and lowers the camera.'),
 30: ('fija', 'Her eyes go from one print to the other and back, slowly; she '
      'breathes, and her hands stay resting on the desk beside the prints.'),
 31: ('fija', 'She breathes, blinks once and keeps looking off to the left, '
      'thinking; her head turns a very little toward the light.'),
 32: ('fija', 'He breathes, looks out at the dark river, then lowers his eyes; the '
      'edge of the tarpaulin moves in the night breeze.'),
 34: ('aire', 'The camera glides slowly forward low over the water; the fisherman '
      'paddles his canoe slowly up the river, the paddle dipping and rising; the '
      'mist drifts along the banks.'),
}
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
