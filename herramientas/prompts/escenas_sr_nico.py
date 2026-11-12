# -*- coding: utf-8 -*-
r"""CASO NICO · Importancia del principio de culpabilidad en la justicia penal
para adolescentes (SRPA, U1). Narra Pilar; el defensor (n28, n29) es Julian.
74 ranuras cortadas por la voz (Scribe, palabra por palabra).

LAS ESCENAS (biblia §4: lugar + quién + hora + qué pasa)
    A  el pueblo y el puente            r01-r07   la mañana fría, la niebla
    B  la plaza: comer                  r08-r13   la vendedora, las sobras
    C  la plaza: el comportamiento      r14-r20   el comedor, las discusiones,
                                                  la reunión de la noche
    D  el domingo                       r21-r33   la familia, el desayuno, la
                                                  huida, el andén, el video
    E  la Policía                       r34-r42   la patrulla, la entrega, lo
                                                  que no se hizo, el CIP
    F  el defensor                      r43-r62   la sala de entrevistas, la
                                                  oficina, el pasillo
    G  el CAE                           r63-r74   la recepción, la enfermería,
                                                  el corte, el aislamiento

LO QUE NO SE DIBUJA (base_sr): ningún golpe en cuadro; los comerciantes que
lo persiguen y lo golpean van de espaldas o en silueta; el consejo del
defensor va sobre el hombro y en las manos; las órdenes del CAE, en manos y
espaldas. Nico con dignidad, nunca caricatura.

R[n] = (cuadros, registro, gente, acento, fuego, lugar, escena)
"""

R = {}

# ------------------------------------------------------------ A el puente
R[1] = (100, 'dia', ('transeuntes',), None, False, 'pueblo', '''
High wide view over a small cold Andean town of Cundinamarca in the early
morning, the camera on a hillside above the last houses looking down at a
gentle angle, perfectly level: brick and whitewashed houses, the long low
corrugated roof of the municipal market in the middle, and crossing the main
road that enters the town, a plain grey steel pedestrian footbridge; tiny
townspeople and a small bus on the road; grey mist sitting on the green
mountains all around.
''')

R[2] = (100, 'dia', ('nico', 'transeuntes'), None, False, 'puente', '''
Medium-wide shot at the foot of the footbridge stair, the camera at standing
height across the pavement, perfectly level: %(nico)s sits on the lowest
concrete steps, elbows on his knees, hands loose between them, watching the
road; above him, on the steel walkway, %(transeuntes)s cross the bridge
without looking down. Morning, cold, grey.
''')

R[3] = (100, 'dia', ('nico',), None, False, 'puente', '''
Close shot of the boy's face in three-quarter view, the camera at his eye
level, perfectly level: %(nico)s sits under the footbridge stair and looks
out at the road, his eyes tired and steady, his mouth a straight line, the
underside of the concrete stair and the grey street soft behind him.
''')

R[4] = (100, 'dia', ('nico', 'transeuntes'), None, False, 'puente', '''
Wide shot from across the road, the camera at standing height, perfectly
level: on the steel footbridge above the road a mother walks holding a small
child by the hand and a father carries a little boy on his shoulders; below
them, at the foot of the stair, %(nico)s sits alone, small in the frame,
looking up at them.
''')

R[5] = (100, 'dia', ('nico', 'escolares'), None, False, 'puente', '''
Medium-wide shot on the pavement beside the footbridge stair, the camera at
standing height, perfectly level: in the foreground %(escolares)s walk past
along the pavement, mid-stride, chatting, one laughing; behind them
%(nico)s sits on the stair with his hands in the pouch of his sweatshirt and
follows them with his eyes.
''')

R[6] = (100, 'dia', ('nico',), None, False, 'puente', '''
Wide shot of the footbridge over the road, the camera at the roadside a
little lower than the walkway, perfectly level: the long plain grey steel
walkway on its concrete pillars, small buses and motorcycles passing under
it, and two blocks beyond it the long low corrugated roof of the municipal
market; small in the frame, %(nico)s comes down the stair with one hand on
the railing, mid-step.
''')

R[7] = (100, 'contraluz', ('nico',), None, False, 'cambuche', '''
Low shot on the ground under the footbridge stair, the camera at the height
of the cardboard bed, perfectly level: early morning; %(nico)s is waking up
on the flattened cardboard under two worn grey blankets, propped on one
elbow, pulling the blanket off his shoulder; his folded old clothes as a
pillow and the knotted plastic bag beside him; behind him the bright grey
opening toward the road.
''')

# ------------------------------------------------------------ B la plaza: comer
R[8] = (100, 'dia', ('nico', 'transeuntes'), None, False, 'plaza', '''
Medium-wide shot along the outer aisle of the covered market, the camera at
standing height, perfectly level: %(nico)s walks slowly past stalls heaped
with potatoes, onions and fruit, mid-step, hands in the pouch of his
sweatshirt, his head turned toward a basket of fruit; %(transeuntes)s shop
around him without noticing him.
''')

R[9] = (100, 'dia', ('vendedora', 'nico'), None, False, 'comedor', '''
Medium shot across the side of a food stall counter, the camera at standing
height, perfectly level: %(vendedora)s leans over her counter and hands a
plain plastic food container with a lid to %(nico)s, who takes it with both
hands; she holds it a moment longer and looks at him, kind and tired; a big
aluminium pot steams behind her.
''')

R[10] = (100, 'dia', ('nico',), None, False, 'plaza', '''
Detail shot at the edge of a bread stall, the camera at counter height from
the side, perfectly level: a basket stacked with small round arepas on the
wooden counter; a thin hand coming out of a frayed mustard sleeve has just
taken one and holds it low against the hip, palm down, fingers closed around
it, the thumb visible; in the soft background the stall keeper stands with
his back turned, weighing something.
''')

R[11] = (100, 'dia', ('vendedora', 'nico'), None, False, 'comedor', '''
Medium shot at the back of the food stall, the camera at seated height,
perfectly level: %(nico)s sits on an upturned plastic crate and eats broth
from a plain bowl with a spoon, hunched over it; beside him %(vendedora)s
stirs her big aluminium pot with a long ladle and glances down at him.
''')

R[12] = (100, 'contraluz', ('comerciante', 'nico'), None, False, 'plaza', '''
Over-the-shoulder shot from behind a market stall, the camera behind %(comerciante)s,
who stands behind his counter with his arms crossed, seen from behind as a
dark shape: across the aisle %(nico)s walks past with his eyes down, mid-step,
the bright grey light of the market entrance behind him.
''')

R[13] = (100, 'contraluz', ('comerciantes', 'nico'), None, False, 'plaza', '''
Wide shot down the central aisle of the covered market, the camera at standing
height, perfectly level: in the foreground two of %(comerciantes)s stand side
by side with their backs to us, one tilting his head toward the far end of the
aisle; far away, small, %(nico)s stands at the edge of the food section; the
wide bright entrance behind everything.
''')

# ------------------------------------------------------------ C el comedor
R[14] = (100, 'dia', ('vendedora', 'transeuntes'), None, False, 'comedor', '''
Wide shot of the market food section in the morning, the camera at standing
height at the end of a long table, perfectly level: %(vendedora)s sets down
plates in front of customers, %(transeuntes)s, who sit on the benches eating
tamales on plantain leaves, bowls of broth and arepas; steam rises from the
big pots behind the counters; enamel mugs of hot chocolate on the oilcloth.
''')

R[15] = (100, 'dia', ('nico', 'transeuntes'), None, False, 'comedor', '''
Medium-wide shot in the narrow passage between two long tables of the food
section, the camera at standing height, perfectly level: %(nico)s runs past,
mid-stride, his back foot still in the air, clutching a tamal on its leaf
against his chest with both hands, his eyes on the way out; a customer at the
table half turns with his empty hand still open above his plate.
''')

R[16] = (100, 'contraluz', ('comerciantes',), None, False, 'plaza', '''
Medium-wide shot between two stalls, the camera at standing height, perfectly
level: three of %(comerciantes)s argue, dark against the bright market
entrance: one raises an open hand in complaint, one shakes his head, one has
his hands on his hips. Nobody touches anybody.
''')

R[17] = (100, 'dia', (), None, False, 'comedor', '''
Detail shot on a food stall counter, the camera at counter height, perfectly
level: a plain tin cash box open on the wooden counter with only a few plain
grey coins in it; a stack of clean plates and a folded cloth beside it. No
person. Nothing legible on anything.
''')

R[18] = (100, 'dia', ('vendedora', 'transeuntes'), None, False, 'comedor', '''
Medium-wide shot of a food stall with its long table empty, the camera at
standing height, perfectly level: %(vendedora)s wipes the empty oilcloth with
a plain cloth, alone, her eyes on the next stall, whose table in the
background is full of %(transeuntes)s eating.
''')

R[19] = (100, 'hero', ('comerciantes',), None, False, 'plaza', '''
Wide shot inside the covered market after closing, the camera at standing
height, perfectly level: the stalls covered with plain tarpaulins and their
metal shutters half down; under a single bare hanging light bulb a group of
five of %(comerciantes)s stand in a loose circle, seen from behind and as dark
silhouettes, talking; the rest of the hall falls away into grey darkness.
''')

R[20] = (100, 'hero', ('comerciantes',), None, False, 'plaza', '''
Medium-wide shot of the same group under the bare bulb, the camera low at the
edge of the circle, perfectly level: one of %(comerciantes)s in the middle,
a dark silhouette, points with his whole arm toward the open entrance of the
market; the others turn their heads to look; outside, far and faint in the
grey night, the steel footbridge.
''')

# ------------------------------------------------------------ D el domingo
R[21] = (100, 'dia', ('transeuntes',), None, False, 'comedor', '''
High wide shot over the food section of the covered market on a busy Sunday
morning, the camera high near the roof trusses looking down at a gentle
angle, perfectly level: every long table full of families, %(transeuntes)s,
eating breakfast; cooks serving from the steaming pots; people squeezing
through the passages between the benches.
''')

R[22] = (100, 'dia', ('cliente', 'familia', 'vendedora'), None, False, 'desayuno', '''
Medium shot at a long table of the food section, the camera at seated height
across the table, perfectly level: %(cliente)s sits on the bench with
%(familia)s; %(vendedora)s sets down the breakfast in front of him; the girl
leans in to look at the steaming bowl.
''')

R[23] = (100, 'dia', ('cliente',), None, False, 'desayuno', '''
Detail shot of the breakfast on the oilcloth, the camera at table height
close to the plates, perfectly level: the tamal opened on its plantain leaf,
the deep bowl of rib broth steaming, the enamel mug of hot chocolate, a small
arepa; the man's hand rests on the table beside the bowl, holding a spoon.
''')

R[24] = (100, 'dia', ('cliente', 'familia', 'nico'), None, False, 'desayuno', '''
Medium-wide shot along the long table, the camera at seated height at its
end, perfectly level: %(cliente)s has turned toward his wife and talks,
laughing, one hand open; the girl looks at her mother; behind his shoulder,
at the edge of the table, %(nico)s has just stopped, standing, his eyes on the
plate.
''')

R[25] = (100, 'dia', ('nico', 'cliente'), None, False, 'desayuno', '''
Medium shot beside the table, the camera at standing height from the side,
perfectly level: %(nico)s turns away from the table mid-stride to run, the
tamal on its leaf in one hand and a plain lidded plastic container of broth
in the other, his body already leaning toward the passage; at the table
%(cliente)s turns his head back toward his empty place.
''')

R[26] = (100, 'dia', ('cliente', 'familia', 'transeuntes'), None, False, 'comedor', '''
Medium-wide shot in the food section, the camera at standing height,
perfectly level: %(cliente)s stands up from the bench and shouts after the
boy, mouth open mid-word, one arm raised calling for help; his wife holds the
girl; %(transeuntes)s at the next tables turn their heads.
''')

R[27] = (100, 'dia', ('comerciantes', 'nico'), None, False, 'plaza', '''
Wide shot down the central aisle of the market, the camera behind the
running men at standing height, perfectly level: three of %(comerciantes)s
run away from us down the aisle, mid-stride, aprons swinging; far ahead,
small, %(nico)s reaches the bright entrance.
''')

R[28] = (100, 'dia', ('nico', 'comerciantes', 'transeuntes'), None, False, 'anden', '''
High wide shot over the pavement in front of the market, the camera above the
street looking down at a gentle angle, perfectly level: %(nico)s runs along
the wide sidewalk, small in the frame, thirty metres from the market
entrance; from two sides %(comerciantes)s close in on him at a run, seen from
behind; %(transeuntes)s stop and step aside.
''')

R[29] = (100, 'dia', (), None, False, 'anden', '''
Detail shot at ground level on the concrete pavement, the camera low and
level just above the ground: the plain lidded plastic container lies
overturned, its broth spreading in a dark puddle across the concrete; the
tamal has fallen out of its plantain leaf beside it; around them, standing
still, men's rubber boots and worn shoes, cut off at the ankle by the frame.
No hand, no face.
''')

R[30] = (100, 'dia', ('comerciantes', 'vendedora'), None, False, 'anden', '''
High wide shot over the pavement, the camera high above the street looking
down, perfectly level: a tight ring of %(comerciantes)s stands on the
sidewalk, all seen from behind, shoulders together, so that whoever is in the
middle cannot be seen at all; at the market entrance %(vendedora)s has
stopped with one hand over her mouth.
''')

R[31] = (100, 'contraluz', ('vendedora', 'comerciantes', 'transeuntes'), None, False, 'anden', '''
Medium-wide shot at the market entrance, the camera just inside the market
looking out, perfectly level: in the foreground two of %(comerciantes)s, dark
silhouettes from behind, lean forward toward the street, one arm flung out as
they shout; in the middle %(vendedora)s and %(transeuntes)s watch from the
doorway, worried, one woman pulling a child back.
''')

R[32] = (100, 'dia', ('comerciante',), None, False, 'anden', '''
Over-the-shoulder shot from just behind %(comerciante)s, the camera at his
shoulder height, perfectly level: his raised hand holds a plain mobile phone
sideways at arm's length, recording; the phone screen is plain flat grey;
beyond it, soft and simplified, a cluster of people on the pavement.
''')

R[33] = (100, 'dia', ('nico',), None, False, 'anden', '''
Low shot at ground level on the pavement, the camera low and level near the
ground: %(nico)s lies curled on his side on the concrete, both forearms
crossed over his face, his knees drawn up, the hood of his sweatshirt
half over his head; around him, men's legs in trousers and rubber boots stand
still, cut off at the knee by the frame. No hand raised, no blow, no blood.
''')

# ------------------------------------------------------------ E la Policía
R[34] = (100, 'dia', ('policias', 'transeuntes'), None, False, 'patrulla', '''
Wide shot of the street in front of the market, the camera at standing
height on the opposite pavement, perfectly level: the white police pickup
has just stopped at the kerb; %(policias)s step out of the cab, one closing
his door; %(transeuntes)s on the sidewalk step back to make room.
''')

R[35] = (100, 'dia', ('comerciantes', 'nico', 'policias'), None, False, 'patrulla', '''
Medium-wide shot on the pavement beside the police pickup, the camera at
standing height, perfectly level: two of %(comerciantes)s, seen from behind,
hold %(nico)s by the upper arms and walk him toward %(policias)s; one merchant
points back toward the market with his free hand, explaining; the boy keeps
his head down.
''')

R[36] = (100, 'dia', ('policias', 'comerciante'), None, False, 'patrulla', '''
Medium shot by the police pickup, the camera at standing height, perfectly
level: one of %(policias)s bends and puts the dented lidded container and the
tamal on its leaf into a plain clear plastic bag; behind him the other
patrolman listens to %(comerciante)s and writes one quick line in a small
plain notebook.
''')

R[37] = (100, 'dia', ('comerciantes', 'policias'), None, False, 'patrulla', '''
Wide shot of the market entrance, the camera at standing height on the
street, perfectly level: %(comerciantes)s walk back into the market in twos
and threes, all seen from behind, already scattering among the stalls;
%(policias)s stand by the pickup at the kerb, looking at the boy, not at the
men going away.
''')

R[38] = (100, 'dia', ('comerciante',), None, False, 'anden', '''
Detail shot at waist height, the camera level beside a walking man: the hand
of %(comerciante)s slides the plain mobile phone, screen dark, into the front
pocket of his white apron as he walks away; behind him, soft and simplified,
the white police pickup at the kerb.
''')

R[39] = (100, 'dia', ('nico', 'policia'), None, False, 'patrulla', '''
Medium shot by the kerb, the camera at seated height on the street, perfectly
level: %(nico)s sits on the kerb next to the rear wheel of the white police
pickup, knees drawn up, one hand pressed to his cheekbone, his eyes on the
ground; beside him %(policia)s stands with his back turned, looking at the
market.
''')

R[40] = (100, 'dia', ('nico', 'policia'), None, False, 'patrulla', '''
Over-the-shoulder shot from behind %(policia)s, who stands writing in a
small plain notebook, the camera at his shoulder looking down at the kerb:
%(nico)s looks up at him from the kerb and speaks, mouth open mid-word, his
hand open on his knee.
''')

R[41] = (100, 'dia', ('nico',), None, False, 'patrulla', '''
Medium close shot inside the back seat of the police pickup, the camera on the
seat beside him, perfectly level: %(nico)s sits against the far door, his
face turned to the side window, his hands in the pouch of his sweatshirt;
through the window the brick houses and misty mountains of the town. No
reflection on the glass.
''')

R[42] = (100, 'dia', ('policia', 'nico', 'funcionaria'), None, False, 'cip', '''
Wide shot down the admission corridor of the preventive internment centre,
the camera at standing height at one end, perfectly level: %(policia)s walks
%(nico)s down the corridor, a hand on his shoulder, mid-step; at the far end,
small, %(funcionaria)s waits beside the open plain steel door.
''')

# ------------------------------------------------------------ F el defensor
R[43] = (100, 'dia', ('defensor',), None, False, 'cip', '''
Medium-wide shot in the corridor, the camera at standing height, perfectly
level: %(defensor)s walks toward us, mid-stride, the thin folder under one arm,
turning his wrist to look at his watch.
''')

R[44] = (100, 'dia', ('nico', 'defensor'), None, False, 'sala_defensa', '''
Wide shot of the small interview room, the camera at standing height in the
corner by the door, perfectly level: %(nico)s and %(defensor)s sit facing each
other across the small grey table, seen from the side; the thin folder lies
closed in front of the lawyer; grey daylight falls from the single high window
onto the table.
''')

R[45] = (100, 'dia', ('nico',), None, False, 'sala_defensa', '''
Close shot of the boy across the table, the camera at his eye level from the
lawyer's side, perfectly level: %(nico)s speaks quietly, mouth open
mid-word, eyes lowered, his thin hands holding his own wrists on the table.
''')

R[46] = (100, 'dia', ('nico', 'defensor'), None, False, 'sala_defensa', '''
Over-the-shoulder shot from behind %(defensor)s, his grey head and shoulder
large and soft in the foreground, the camera at seated height: across the
table %(nico)s talks, one hand lifted slightly from the table as he explains.
''')

R[47] = (100, 'dia', ('defensor', 'nico'), None, False, 'sala_defensa', '''
Medium shot of the two at the table seen exactly from the side, the camera at
seated height, perfectly level: %(defensor)s leans back in his chair and
talks, one hand open over the closed folder, his face in profile; across from
him %(nico)s listens, still.
''')

R[48] = (100, 'contraluz', ('nico',), None, False, 'sala_defensa', '''
Close shot of the boy, the camera at his eye level, perfectly level: %(nico)s
listens, his eyes rising toward the lawyer, brows lifted a little, the high
window bright and grey behind his shoulder.
''')

R[49] = (100, 'dia', ('defensor', 'nico'), None, False, 'sala_defensa', '''
Detail shot on the table between them, the camera at table height from the
side, perfectly level: the lawyer's two hands folded on top of the closed
thin folder, a pair of reading glasses beside it; across the table, the
boy's thin hands with the frayed mustard cuffs, flat on the grey surface.
''')

R[50] = (100, 'dia', ('defensor', 'nico'), None, False, 'sala_defensa', '''
Over-the-shoulder shot from directly behind %(defensor)s, his grey suit
jacket and the back of his head filling one side of the frame, the camera at
seated height: across the table %(nico)s listens intently, motionless, his
eyes on the lawyer's face.
''')

R[51] = (100, 'dia', ('defensor', 'nico'), None, False, 'sala_defensa', '''
Detail shot on the table, the camera at table height from the side,
perfectly level: the lawyer's index finger rests on the closed thin folder,
pressing it, the rest of his hand flat; across the table the boy's two thin
hands lie still beside each other.
''')

R[52] = (100, 'contraluz', ('nico',), None, False, 'sala_defensa', '''
Medium shot of the boy in profile, the camera at seated height, perfectly
level: %(nico)s has turned his head and looks up at the single high window,
its flat grey daylight on his face; the bare grey wall around it.
''')

R[53] = (100, 'dia', ('nico',), None, False, 'sala_defensa', '''
Close shot of the boy, the camera at his eye level across the table,
perfectly level: %(nico)s asks a question, mouth open mid-word, brows drawn
together, leaning slightly forward over the table.
''')

R[54] = (100, 'dia', ('defensor', 'nico'), None, False, 'sala_defensa', '''
Over-the-shoulder shot from behind the boy, his shoulder in the mustard
sweatshirt soft in the foreground, the camera at seated height: across the
table %(defensor)s lifts both palms and his shoulders a little, his face
turned aside toward the window.
''')

R[55] = (100, 'dia', ('defensor', 'nico'), None, False, 'sala_defensa', '''
Medium shot of the two at the table from the side, the camera at seated
height, perfectly level: %(defensor)s leans in over the table with his hand
flat on it between them, his face in profile; %(nico)s leans back a little in
his chair.
''')

R[56] = (100, 'contraluz', ('nico',), None, False, 'sala_defensa', '''
Close shot of the boy, the camera at his eye level, perfectly level: %(nico)s
nods slowly, his eyes down, lips pressed together, his hands clasped tight on
the table; the high window bright and grey behind him.
''')

R[57] = (100, 'dia', ('defensor',), None, False, 'despacho_defensor', '''
Medium-wide shot of the public defenders' office, the camera at standing
height, perfectly level: %(defensor)s sits at his desk with the telephone
receiver at his ear, writing on another case file; at the corner of the desk,
on top of a tall stack of folders, the thin folder of the boy lies closed.
''')

R[58] = (100, 'dia', (), None, False, 'despacho_defensor', '''
Detail shot on the corner of the desk, the camera at desk height, perfectly
level: the thin plain cardboard folder lies closed on top of a tall stack of
other folders tied with string; a plain coffee cup stands on it. No person.
Nothing legible.
''')

R[59] = (100, 'dia', ('defensor',), None, False, 'despacho_defensor', '''
Medium-wide shot of the office, the camera at standing height by the window,
perfectly level: %(defensor)s stands up from his desk, one arm already in the
sleeve of his grey jacket, the thin folder pinned under the other arm, turning
toward the door.
''')

R[60] = (100, 'dia', ('nico',), None, False, 'pasillo', '''
Wide shot of the courthouse corridor, the camera at standing height at one
end, perfectly level: %(nico)s sits alone on a plain wooden bench halfway
down the corridor, his hands between his knees, looking at the closed door
opposite; tall windows with flat daylight at the far end.
''')

R[61] = (100, 'dia', ('defensor', 'nico'), None, False, 'pasillo', '''
Medium-wide shot of the bench in the corridor, the camera at seated height
across the corridor, perfectly level: %(defensor)s sits beside %(nico)s on
the bench, saying a few words while he looks down at the plain mobile phone
in his hand, screen dark; the boy turns his face toward him.
''')

R[62] = (100, 'dia', ('nico',), None, False, 'pasillo', '''
Close shot of the boy on the bench, the camera at his eye level, perfectly
level: %(nico)s looks at the closed plain door of the hearing room, his jaw
tight, his eyes steady; the corridor soft behind him.
''')

# ------------------------------------------------------------ G el CAE
R[63] = (100, 'dia', ('nico',), None, False, 'cae_fachada', '''
Wide shot of the entrance of the specialised care centre, the camera at
standing height across the access road, perfectly level: the plain grey
steel gate in the high wall is sliding open; in front of it, small, %(nico)s
stands with his knotted plastic bag in one hand beside a plain grey van;
misty mountains behind the building.
''')

R[64] = (100, 'dia', ('funcionaria', 'nico'), None, False, 'cae_recepcion', '''
Medium shot in the admission office, the camera at seated height beside the
desk, perfectly level: %(funcionaria)s sits at the desk and looks up from her
clipboard at %(nico)s, who stands in front of the desk holding his knotted
plastic bag with both hands.
''')

R[65] = (100, 'dia', ('nico', 'enfermera'), None, False, 'enfermeria', '''
Medium-wide shot of the nursing room, the camera at standing height from the
side, perfectly level: %(nico)s sits on the edge of the examination couch,
barefoot, his tracksuit trousers rolled up to the ankle, hands gripping the
edge of the couch; %(enfermera)s kneels on one knee in front of him with her
clipboard, looking down at his feet; the feet are small and far in the frame,
plain grey shapes, no detail.
''')

R[66] = (100, 'dia', (), None, False, 'enfermeria', '''
Detail shot on the floor of the nursing room, the camera low and level near
the floor: a pair of old grey canvas sneakers with split soles and broken
laces stands beside the leg of the examination couch, worn down at the heels.
No person.
''')

R[67] = (100, 'dia', ('enfermera', 'nico'), None, False, 'enfermeria', '''
Medium close shot, the camera at the boy's eye level, perfectly level:
%(enfermera)s, gloved, turns his face gently toward the examination lamp with
two fingers under his chin and looks at a faint darker grey shadow on his
cheekbone; %(nico)s keeps his eyes down. No blood, no open wound.
''')

R[68] = (100, 'dia', ('nico', 'enfermera'), None, False, 'enfermeria', '''
Medium shot in the nursing room, the camera at standing height, perfectly
level: %(nico)s stands barefoot on the plain grey floor scale, thin, his arms
hanging at his sides; %(enfermera)s stands beside him reading the scale and
writing on her clipboard. The scale shows nothing legible.
''')

R[69] = (100, 'dia', ('funcionarios', 'nico'), None, False, 'enfermeria', '''
Medium-wide shot of the corridor outside the nursing room, the camera at
standing height, perfectly level: %(funcionarios)s talk in the foreground,
seen from behind, one of them tilting her head toward the half-open door;
through the doorway, small, %(nico)s sits on the examination couch alone.
''')

R[70] = (100, 'dia', ('jovenes',), None, False, 'patio_cae', '''
Wide shot of the common room of the centre, the camera at standing height in
a corner, perfectly level: %(jovenes)s play at the table-football game and sit
at a table with a board game, all seen from behind or in profile; grey
daylight from the high windows. Nobody looks at the camera.
''')

R[71] = (100, 'dia', ('funcionaria',), None, False, 'cae_recepcion', '''
Detail shot on the desk, the camera at desk height, perfectly level: the hand
of the staff member ticks a box on the sheet clipped to her clipboard with a
plain pen; the sheet is only plain grey bars and empty boxes. No face in the
frame.
''')

R[72] = (100, 'dia', ('nico_rapado',), None, False, 'lavadero', '''
Medium shot in the washroom, the camera at seated height in front of the boy,
perfectly level: %(nico_rapado)s sits on the plain plastic chair with a plain
grey cloth over his shoulders, his eyes down; behind him a staff member, seen
only from the chest down, no face in the frame, passes plain electric hair
clippers over his head; half of his head is already shaved and clumps of his
black hair lie on the cloth and on the floor.
''')

R[73] = (100, 'dia', (), None, False, 'aislamiento', '''
Medium shot in the corridor, the camera at standing height, perfectly level:
a hand in a plain light grey sleeve, its owner out of frame, pulls the plain
grey steel door of a single room shut; the small square window in the door
shows only the grey light inside. No face in the frame.
''')

R[74] = (100, 'contraluz', ('nico_rapado',), None, False, 'aislamiento', '''
Medium-wide shot of the small bare single room, the camera at standing height
in the corner, perfectly level: %(nico_rapado)s sits alone on the narrow bed
with his back against the bare wall and his knees drawn up, his arms around
them; the flat grey daylight from the small high window falls across the
floor; the plain steel door is closed.
''')

NOMBRE = {
 1: 'el_pueblo', 2: 'nico', 3: 'su_cara', 4: 'las_familias', 5: 'la_escuela',
 6: 'el_puente', 7: 'los_cartones', 8: 'la_plaza', 9: 'las_sobras',
 10: 'la_arepa', 11: 'la_ayuda', 12: 'otros', 13: 'lo_vigilan',
 14: 'los_desayunos', 15: 'sale_corriendo', 16: 'las_discusiones',
 17: 'las_ventas', 18: 'la_mesa_vacia', 19: 'la_reunion', 20: 'atraparlo',
 21: 'el_domingo', 22: 'la_familia', 23: 'el_desayuno', 24: 'se_acerca',
 25: 'la_huida', 26: 'el_grito', 27: 'lo_persiguen', 28: 'treinta_metros',
 29: 'el_caldo', 30: 'el_corro', 31: 'los_gritos', 32: 'el_celular',
 33: 'en_el_suelo', 34: 'la_patrulla', 35: 'la_entrega', 36: 'los_alimentos',
 37: 'se_dispersan', 38: 'el_video', 39: 'las_lesiones', 40: 'quince_anos',
 41: 'el_traslado', 42: 'el_cip', 43: 'el_defensor', 44: 'la_sala',
 45: 'el_hambre', 46: 'otras_veces', 47: 'le_explica', 48: 'escucha',
 49: 'las_manos', 50: 'mire', 51: 'si_acepta', 52: 'la_ventana',
 53: 'pregunta', 54: 'dependeria', 55: 'insiste', 56: 'acepta',
 57: 'la_oficina', 58: 'la_carpeta', 59: 'se_va', 60: 'el_banco',
 61: 'el_telefono', 62: 'la_puerta', 63: 'el_cae', 64: 'la_recepcion',
 65: 'la_valoracion', 66: 'los_zapatos', 67: 'el_rostro', 68: 'la_bascula',
 69: 'los_funcionarios', 70: 'los_demas', 71: 'la_orden', 72: 'el_corte',
 73: 'la_puerta_cerrada', 74: 'el_aislamiento'}

CORTE = {
 1: ('n01_nico', 'En el municipio'),
 2: ('n01_nico', 'vivía un adolescente'),
 3: ('n02_documentos', 'Nico no tenía'),
 4: ('n02_documentos', 'y tampoco se tenía'),
 5: ('n03_escuela', 'No figuraba'),
 6: ('n04_puente', 'Desde hacía'),
 7: ('n04_puente', 'Allí dormía'),
 8: ('n05_alimentacion', 'Su alimentación'),
 9: ('n05_alimentacion', 'de las sobras'),
 10: ('n05_alimentacion', 'y de pequeños'),
 11: ('n06_comerciantes', 'Los comerciantes'),
 12: ('n06_comerciantes', 'mientras que otros'),
 13: ('n07_recurrente', 'Con el paso'),
 14: ('n07_recurrente', 'Cuando los clientes'),
 15: ('n07_recurrente', 'Nico se acercaba'),
 16: ('n08_discusiones', 'Esta situación'),
 17: ('n08_discusiones', 'Algunos afirmaban'),
 18: ('n08_discusiones', 'y que los clientes'),
 19: ('n09_reunion', 'En una reunión'),
 20: ('n09_reunion', 'Uno de ellos'),
 21: ('n10_domingo', 'El domingo'),
 22: ('n11_desayuno', 'Un hombre'),
 23: ('n11_desayuno', 'cuyo valor'),
 24: ('n12_huida', 'Mientras el cliente'),
 25: ('n12_huida', 'tomó el tamal'),
 26: ('n13_persecucion', 'El propietario'),
 27: ('n13_persecucion', 'Varios comerciantes'),
 28: ('n13_persecucion', 'aproximadamente a'),
 29: ('n14_agresion', 'Una vez reducido'),
 30: ('n14_agresion', 'Uno de ellos'),
 31: ('n15_gritos', 'Durante la agresión'),
 32: ('n16_video', 'Un comerciante'),
 33: ('n16_video', 'En el video'),
 34: ('n17_patrulla', 'Aproximadamente'),
 35: ('n18_entrega', 'Los comerciantes'),
 36: ('n19_policias', 'Los policías'),
 37: ('n20_omisiones', 'Sin embargo'),
 38: ('n20_omisiones', 'No solicitaron'),
 39: ('n20_omisiones', 'y tampoco dejaron'),
 40: ('n21_quince', 'Nico manifestó'),
 41: ('n22_cip', 'Los uniformados'),
 42: ('n22_cip', 'y posteriormente'),
 43: ('n23_defensor', 'Una vez iniciadas'),
 44: ('n24_hambre', 'Durante una conversación'),
 45: ('n24_hambre', 'pero explicó'),
 46: ('n25_otras', 'También contó'),
 47: ('n26_cae', 'El defensor público'),
 48: ('n26_cae', 'donde tendría'),
 49: ('n27_relato', 'Según la conversación'),
 50: ('n28_mire', 'Mire'),
 51: ('n28_mire', 'Si acepta'),
 52: ('n29_afuera', 'Afuera'),
 53: ('n30_pregunta', 'Nico preguntó'),
 54: ('n31_respuesta', 'El defensor'),
 55: ('n31_respuesta', 'pero insistió'),
 56: ('n32_dispuesto', 'El adolescente'),
 57: ('n33_preparacion', 'Durante la preparación'),
 58: ('n33_preparacion', 'No verificó'),
 59: ('n33_preparacion', 'No solicitó'),
 60: ('n33_preparacion', 'y tampoco exploró'),
 61: ('n34_consecuencias', 'Tampoco explicó'),
 62: ('n34_consecuencias', 'ni verificó'),
 63: ('n35_ingreso', 'Una vez adelantadas'),
 64: ('n36_higiene', 'Durante el procedimiento'),
 65: ('n37_valoracion', 'En la valoración'),
 66: ('n38_olor', 'Olor intenso'),
 67: ('n39_lesiones', 'Lesiones visibles'),
 68: ('n40_peso', 'Bajo peso'),
 69: ('n41_convivencia', 'Algunos funcionarios'),
 70: ('n41_convivencia', 'podían representar'),
 71: ('n42_cabello', 'En consecuencia'),
 72: ('n42_cabello', 'se ordenó'),
 73: ('n43_aislamiento', 'Adicionalmente'),
 74: ('n43_aislamiento', 'se decidió'),
}

EXTRA_TOKENS = {}

# REF: la placa madre de la MISMA escena (lugar, gente o el mismo plano).
# Va al FINAL de las referencias. Las madres (sin REF) salen en la ola 1.
REF = {
 3: (2, 'gente', 'It is the SAME boy under the SAME footbridge, closer.'),
 4: (2, 'lugar', 'It is the SAME footbridge and the SAME boy, seen from across the road.'),
 5: (2, 'lugar', 'It is the SAME footbridge stair and the SAME boy.'),
 6: (2, 'lugar', 'It is the SAME footbridge, seen whole from the roadside.'),
 7: (2, 'gente', 'It is the SAME boy, under the SAME stair, at dawn.'),
 8: (9, 'gente', 'It is the SAME boy, now walking in the market hall.'),
 10: (9, 'lugar', 'It is the SAME market.'),
 11: (9, 'lugar', 'It is the SAME cook at the SAME food stall with the SAME boy.'),
 12: (9, 'lugar', 'It is the SAME market and the SAME boy.'),
 13: (9, 'lugar', 'It is the SAME market and the SAME boy, far away.'),
 15: (14, 'lugar', 'It is the SAME food section; the boy is the one of the first reference.'),
 16: (14, 'lugar', 'It is the SAME market.'),
 17: (14, 'lugar', 'It is the SAME food stall counter.'),
 18: (14, 'lugar', 'It is the SAME food section and the SAME cook.'),
 20: (19, 'mismo', 'The SAME group under the SAME bulb; the camera is now lower and closer and one man in the middle points toward the entrance.'),
 22: (21, 'lugar', 'It is the SAME food section on the SAME Sunday morning.'),
 23: (22, 'lugar', 'It is the SAME table and the SAME breakfast, much closer.'),
 24: (22, 'gente', 'It is the SAME family at the SAME table; the boy is the one of the first reference.'),
 25: (22, 'gente', 'It is the SAME table and the SAME man; the boy is the one of the first reference.'),
 26: (22, 'gente', 'It is the SAME man and the SAME family.'),
 27: (21, 'lugar', 'It is the SAME market hall.'),
 29: (28, 'lugar', 'It is the SAME pavement in front of the market, at ground level.'),
 30: (28, 'lugar', 'It is the SAME pavement in front of the SAME market.'),
 31: (28, 'lugar', 'It is the SAME market entrance and the SAME street.'),
 32: (28, 'lugar', 'It is the SAME street in front of the market.'),
 33: (28, 'lugar', 'It is the SAME pavement; the boy is the one of the first reference.'),
 35: (34, 'lugar', 'It is the SAME police pickup and the SAME two patrolmen.'),
 36: (34, 'lugar', 'It is the SAME police pickup and the SAME patrolmen.'),
 37: (34, 'lugar', 'It is the SAME market entrance and the SAME police pickup.'),
 38: (34, 'lugar', 'It is the SAME street and the SAME police pickup.'),
 39: (34, 'lugar', 'It is the SAME police pickup and patrolman; the boy is the one of the first reference.'),
 40: (34, 'lugar', 'It is the SAME patrolman; the boy is the one of the first reference.'),
 41: (34, 'lugar', 'It is the inside of the SAME police pickup.'),
 43: (42, 'lugar', 'It is the SAME corridor.'),
 45: (44, 'gente', 'It is the SAME boy in the SAME room, closer.'),
 46: (44, 'lugar', 'It is the SAME room, the SAME lawyer and the SAME boy.'),
 47: (44, 'lugar', 'It is the SAME room, the SAME lawyer and the SAME boy.'),
 48: (44, 'gente', 'It is the SAME boy in the SAME room, closer.'),
 49: (44, 'lugar', 'It is the SAME table in the SAME room, much closer.'),
 50: (44, 'lugar', 'It is the SAME room, the SAME lawyer and the SAME boy.'),
 51: (44, 'lugar', 'It is the SAME table in the SAME room, much closer.'),
 52: (44, 'lugar', 'It is the SAME room and the SAME boy.'),
 53: (44, 'gente', 'It is the SAME boy in the SAME room, closer.'),
 54: (44, 'lugar', 'It is the SAME room, the SAME lawyer and the SAME boy.'),
 55: (44, 'lugar', 'It is the SAME room, the SAME lawyer and the SAME boy.'),
 56: (44, 'gente', 'It is the SAME boy in the SAME room, closer.'),
 58: (57, 'lugar', 'It is the SAME desk in the SAME office, much closer.'),
 59: (57, 'lugar', 'It is the SAME office and the SAME lawyer.'),
 61: (60, 'lugar', 'It is the SAME corridor and the SAME bench; the lawyer is the one of the first reference.'),
 62: (60, 'gente', 'It is the SAME boy on the SAME bench, closer.'),
 66: (65, 'lugar', 'It is the SAME nursing room.'),
 67: (65, 'lugar', 'It is the SAME nurse and the SAME boy in the SAME room, closer.'),
 68: (65, 'lugar', 'It is the SAME nursing room, the SAME nurse and the SAME boy.'),
 69: (65, 'lugar', 'It is the SAME nursing room seen from the corridor outside.'),
 71: (64, 'lugar', 'It is the SAME desk in the SAME admission office, much closer.'),
 73: (74, 'lugar', 'It is the door of the SAME room, seen from the corridor outside.'),
}
# REF2: la hoja de personaje (identidad), PRIMERO. (hoja, quien)
REF2 = {}
for _n in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 24, 25, 28, 33, 35, 39, 40,
           41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 60, 61,
           62, 63, 64, 65, 67, 68, 69):
    REF2[_n] = ('SR_HOJA_nico', 'THE BOY')
for _n in (72, 74):
    REF2[_n] = ('SR_HOJA_nico_rapado', 'THE BOY')
for _n in (43, 57, 59):
    REF2[_n] = ('SR_HOJA_defensor', 'THE PUBLIC DEFENDER')
for _n in (14, 18, 22, 30, 31):
    REF2[_n] = ('SR_HOJA_vendedora', 'THE MARKET COOK')
# en las escenas de dos, la segunda identidad va como tercera referencia
REF3 = {
 9: ('SR_HOJA_vendedora', 'THE MARKET COOK'),
 11: ('SR_HOJA_vendedora', 'THE MARKET COOK'),
 44: ('SR_HOJA_defensor', 'THE PUBLIC DEFENDER'),
 61: ('SR_HOJA_defensor', 'THE PUBLIC DEFENDER'),
 65: ('SR_HOJA_enfermera', 'THE NURSE'),
 67: ('SR_HOJA_enfermera', 'THE NURSE'),
 68: ('SR_HOJA_enfermera', 'THE NURSE'),
}

# las anclas de estilo de la serie (cuenta nueva, placa_id_ei.json)
ANCLA_DE = {1: 'pueblo', 2: 'pueblo', 9: 'oficina', 14: 'oficina', 19: 'noche_int',
            21: 'oficina', 28: 'pueblo', 34: 'pueblo', 42: 'pasillo',
            44: 'oficina', 57: 'oficina', 60: 'pasillo', 63: 'pueblo',
            64: 'recepcion', 65: 'oficina', 70: 'oficina', 72: 'oficina',
            74: 'noche_int'}

CON_PERSONA = {n for n, v in R.items() if v[2]} - {1}
CENITALES = set()
SOLO_MANOS = {10, 49, 51, 71}
TOPE_SIN_GENTE = 3
TOTAL = 7400
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

GRIS = (30, 130)
SIN_TECHO = set()
RESPIRO = 74
# 12 nov: los patrulleros de la Policía Nacional (r34-r40; la r38 es la
# camioneta con su franja verde). La limpieza ACOTA el verde oliva y el
# chaleco en vez de apagarlos (la lección del C3 de Enfoque diferencial).
CHALECO = {34, 35, 36, 37, 38, 39, 40}

# 12 nov: el movimiento (V2, Kling 2.5 a 720p, 5 s, desde la placa GRADUADA
# como cuadro inicial). La regla de la casa: al modelo se le dice que pasa,
# con su destino, no que no pasa; la camara quieta se dice una vez; nadie
# queda «a punto de» tocar algo; el papel no se anima; para un grupo, gesto y
# habla en su sitio. Sin clip, con la camara de la casa:
#   - las ranuras bajo las listas de After Effects (22-23, 37-39, 48, 57-60,
#     65-68): el tinte las cubre;
#   - las de solo manos (10, 49, 51, 71) y las que valen por quietas (17 los
#     recipientes, 29 el caldo en el suelo, 66 los zapatos);
#   - la agresion (30-33): el corro, los gritos, el celular y el suelo. Kling
#     completa los gestos y ahi completaria un golpe (biblia: nada violento
#     en acto). Quietas se leen; en movimiento no se controla.
# 'aire' = toma alta que avanza (r01).
KLING = {
 1: ('aire', 'The camera glides slowly forward high over the small town toward the '
     'covered market; the grey mist drifts along the green mountains; tiny '
     'townspeople walk along the streets and a small bus drives along the main road.'),
 2: ('fija', 'People in woollen ruanas walk down the steps of the footbridge and '
     'along it, crossing from one side to the other; the boy sitting on the low '
     'steps follows them with his eyes, breathing slowly, his hands resting on '
     'his knees.'),
 3: ('fija', 'The boy slowly lowers his eyes, then lifts them again toward '
     'something passing beyond the frame; a light breeze moves a few strands of '
     'his long hair; he breathes slowly.'),
 4: ('fija', 'A family walks along the footbridge above, the mother holding a small '
     'child by the hand; the small bus drives along the road below and out of '
     'the frame; the boy sitting on the steps turns his head to watch them go.'),
 5: ('fija', 'The schoolchildren walk past the boy laughing and talking, their '
     'backpacks bouncing, and carry on walking out of the frame on the right; the '
     'boy stays seated and turns his head to follow them.'),
 6: ('fija', 'The boy walks down the footbridge steps one step at a time, his hands '
     'in the pouch of his sweatshirt, and reaches the bottom of the stairs; a '
     'motorcycle drives by on the road.'),
 7: ('fija', 'The boy pulls the grey blanket up over his shoulder, lies down on the '
     'cardboard, rests his head on his arm and closes his eyes.'),
 8: ('fija', 'The boy walks slowly along the market aisle, his head turned toward the '
     'fruit; around him the shoppers in ruanas choose vegetables, a vendor weighs '
     'potatoes, people pass behind him.'),
 9: ('fija', 'The cook hands the bowl across the counter and the boy takes it in both '
     'hands and draws it toward himself; steam rises from the big pot; she smiles '
     'a little and turns back to her griddle.'),
 11: ('fija', 'The boy eats the soup from the bowl with a spoon, bending over it; '
      'beside him the cook stirs the big pot with a ladle; steam rises.'),
 12: ('fija', 'At the market entrance the boy takes two slow steps inside and looks '
      'around at the stalls; in the foreground the merchant, seen from behind, '
      'folds his arms across his chest.'),
 13: ('fija', 'Far down the aisle the boy walks slowly between the stalls; in the '
      'foreground the two merchants, seen from behind, watch him, and one turns his '
      'head toward the other and says something.'),
 14: ('fija', 'The cook sets a plate of breakfast down on the table in front of a '
      'customer; the diners eat with spoons and lift their cups; steam rises from '
      'the pots behind them.'),
 15: ('fija', 'The boy runs between the tables with the tamal in his hands and out of '
      'the frame; the diners at the tables turn their heads to look after him.'),
 16: ('fija', 'The three dark silhouettes argue in their places: one shakes his open '
      'hand in complaint, one shakes his head, the third shifts his weight with '
      'his hands on his hips.'),
 18: ('fija', 'The cook wipes the empty table with a cloth in long slow strokes and '
      'straightens up; behind her the diners at the other tables keep eating.'),
 19: ('fija', 'The men under the single bare bulb talk in their loose circle; one '
      'nods, another gestures with an open hand; the bulb sways very slightly on '
      'its cable.'),
 20: ('fija', 'The man in the middle of the group raises his arm and points toward the '
      'open entrance of the market; the others turn their heads to look where he '
      'points.'),
 21: ('fija', 'The busy Sunday food hall: diners eat and talk at the long tables, the '
      'cooks stir the pots and turn arepas on the griddles, steam rises, people '
      'walk along the aisle.'),
 24: ('fija', 'The man laughs and talks to his wife with an open hand; his wife '
      'smiles and answers; the girl looks from one to the other; behind them the '
      'boy stands still, his eyes on the plate, breathing.'),
 25: ('fija', 'The boy runs off down the aisle with the tamal and the container of '
      'broth and out of the frame; the man turns his head and shoulders to look '
      'after him, surprised.'),
 26: ('fija', 'The man shouts after the boy with his arm raised high, calling for '
      'help; his wife pulls the girl close against her; the people at the next '
      'tables turn their heads.'),
 27: ('fija', 'The merchants run down the aisle away from the camera after the boy, '
      'their aprons flapping; far ahead the boy keeps running; the women at the '
      'stalls step back.'),
 28: ('fija', 'The merchants run across the pavement away from the camera toward the '
      'boy in the distance; the townspeople step aside to let them pass.'),
 34: ('fija', 'The two patrolmen stand by the pickup and look toward the market; one '
      'of them says something to the other and adjusts his cap; townspeople walk '
      'past behind them.'),
 35: ('fija', 'The two merchants walk the boy toward the patrolmen; one merchant points '
      'back toward the market with his free hand as he explains; the patrolmen '
      'step forward to meet them; the boy keeps his head down.'),
 36: ('fija', 'The bending patrolman places the container and the tamal into the clear '
      'plastic bag and ties it; the other patrolman writes in his small notebook '
      'while the merchant talks.'),
 40: ('fija', 'The boy looks up at the patrolman and talks, his mouth moving, his open '
      'hand lifting from his knee; the patrolman writes a line in his notebook.'),
 41: ('fija', 'The pickup is driving: outside the side window the brick houses and the '
      'misty mountains slide past; the boy sways gently with the vehicle and keeps '
      'looking out of the window.'),
 42: ('fija', 'The patrolman walks the boy along the corridor toward the camera, one '
      'hand on the boy\'s shoulder; they walk at an even pace; a staff member '
      'crosses the far end of the corridor.'),
 43: ('fija', 'The public defender walks along the corridor toward the camera, '
      'glances at his watch and lowers his arm, keeping his stride.'),
 44: ('fija', 'The lawyer talks to the boy across the table with a small open-hand '
      'gesture; the boy listens and nods once.'),
 45: ('fija', 'The boy speaks quietly, his mouth moving, his eyes lowered, his thumbs '
      'rubbing his own wrists.'),
 46: ('fija', 'The boy talks across the table, his mouth moving, and moves his raised '
      'hand as he explains; the lawyer\'s head nods slightly in the foreground.'),
 47: ('fija', 'The lawyer leans back in his chair and talks, moving his open hand over '
      'the closed folder; the boy listens without moving.'),
 50: ('fija', 'The boy listens to the lawyer without moving, blinks slowly and '
      'swallows; the lawyer\'s shoulder shifts slightly in the foreground.'),
 52: ('fija', 'The boy keeps looking up at the high window; the grey daylight brightens '
      'a little on his face; he breathes in slowly and lets the breath out.'),
 53: ('fija', 'The boy asks a question, his mouth moving, his brows drawn together, '
      'leaning a little further over the table.'),
 54: ('fija', 'Across the table the lawyer lifts both palms and his shoulders, '
      'glances toward the window, then lowers his hands back to the table.'),
 55: ('fija', 'The lawyer leans in over the table and talks, tapping his flat hand '
      'once on the table; the boy leans back in his chair.'),
 56: ('fija', 'The boy nods slowly twice, his eyes down, his lips pressed together, '
      'his clasped hands tightening on the table.'),
 61: ('fija', 'On the bench the lawyer says a few words without looking up from his '
      'phone; the boy turns his face toward him and waits.'),
 62: ('fija', 'The boy looks at the closed door, his jaw tight; he breathes in, his '
      'shoulders rising and falling once.'),
 63: ('fija', 'The boy standing by the van turns his head toward the gate of the '
      'centre; the leaves of the trees stir in the wind; the mist moves slowly '
      'over the mountains.'),
 64: ('fija', 'The staff member at the desk looks up at the boy and speaks, her mouth '
      'moving; the boy keeps his eyes down and holds his plastic bag in both '
      'hands.'),
 69: ('fija', 'The two staff members talk to each other in the foreground, seen from '
      'behind; the woman tilts her head toward the half-open door; through the '
      'doorway the boy sits still on the examination couch.'),
 70: ('fija', 'The other adolescents play: two spin the rods of the table football, '
      'another moves a chess piece; none of them looks toward the door.'),
 72: ('fija', 'The hand with the electric clipper passes slowly over the boy\'s head '
      'from front to back, and tufts of black hair fall onto the grey cape; the '
      'boy keeps his eyes down and does not move.'),
 73: ('fija', 'The hand pulls the grey steel door and the door swings shut and closes; '
      'the hand lets go and leaves the frame.'),
 74: ('fija', 'The boy sits curled on the bed, his arms around his knees; he breathes '
      'slowly and lowers his forehead toward his knees; the light from the small '
      'window lies still on the wall.'),
}
# caminatas hacia camara: el encuadre se abre en el conformado (`mov_sr.ABRE`)
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
             'flag, weapon, blood, punch, kick')


def comprobar():
    fallos = []
    tot = sum(v[0] for v in R.values())
    if sorted(R) != list(range(1, len(NOMBRE) + 1)):
        fallos.append('faltan ranuras')
    if sorted(CORTE) != sorted(R):
        fallos.append('CORTE no cubre las ranuras')
    if tot != TOTAL:
        fallos.append('los cuadros suman %d y la rejilla dice %d' % (tot, TOTAL))
    racha = mejor = 0
    for i in sorted(R):
        racha = 0 if i in CON_PERSONA else racha + 1
        mejor = max(mejor, racha)
    if mejor > TOPE_SIN_GENTE:
        fallos.append('%d ranuras seguidas sin gente' % mejor)
    return fallos, tot, mejor

# --- 12 nov: cuadros medidos (cortes de Scribe sobre la voz masterizada:
# cada ranura entra 3 cuadros antes de la primera palabra de su CORTE; la
# ultima termina con el master)
CUADROS = {1: 125, 2: 177, 3: 162, 4: 154, 5: 220, 6: 173, 7: 181, 8: 103, 9: 102, 10: 138, 11: 140, 12: 171, 13: 147, 14: 176, 15: 150, 16: 130, 17: 91, 18: 171, 19: 183, 20: 218, 21: 250, 22: 214, 23: 105, 24: 116, 25: 116, 26: 82, 27: 154, 28: 111, 29: 151, 30: 183, 31: 234, 32: 99, 33: 194, 34: 142, 35: 263, 36: 166, 37: 134, 38: 80, 39: 143, 40: 187, 41: 105, 42: 262, 43: 215, 44: 131, 45: 144, 46: 258, 47: 191, 48: 156, 49: 146, 50: 109, 51: 170, 52: 128, 53: 157, 54: 125, 55: 187, 56: 225, 57: 169, 58: 126, 59: 124, 60: 142, 61: 147, 62: 193, 63: 194, 64: 272, 65: 267, 66: 161, 67: 226, 68: 152, 69: 106, 70: 172, 71: 218, 72: 134, 73: 83, 74: 103}
for _n, _c in CUADROS.items():
    R[_n] = (_c,) + R[_n][1:]
TOTAL = 11934
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)
