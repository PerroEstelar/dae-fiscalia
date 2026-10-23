# -*- coding: utf-8 -*-
r"""El repertorio del P3C4 v2: ONCE ESCENAS filmadas desde treinta y nueve
angulaciones, bajo la BIBLIA_puesta_en_escena_P3.

POR QUE ONCE Y NO TREINTA Y NUEVE
    La v1 tenia 34 placas distintas para 39 ranuras. Con 34 cosas que
    inventar y una historia de revision de expedientes, toda invencion
    terminaba siendo otro objeto sobre otra mesa: 17 cenitales y 32 placas
    con manos, contra 4 con una cara. Tener que ser siempre nuevo fue lo que
    los hizo a todos iguales.

    Aqui hay ONCE LUGARES y cada uno se filma desde dos a cinco angulaciones
    -general, medio, primer plano, detalle-. Es la economia de la serie SRPA
    (15 placas entrando 27 veces; 14 entornos para seis piezas) y el
    espectador recibe un mundo en vez de un pase de diapositivas.

LA PIEZA SE LLAMA «PUERTO DE SALIDA» Y NO TENIA UN PUERTO
    Ahora el muelle es la escena B, es el plano HERO de la pieza (r05) y
    vuelve tres veces. El titulo por fin esta en la imagen.

LOS ROLES RECUPERAN CARA, Y HAY UN CHEQUEO QUE LO PROTEGE
    El fiscal, el investigador, la jueza, la otra fiscal, la representante y
    la vecina se dibujan como personas. La objecion de la v1 -«un retrato de
    una jueza decidiendo mal»- la responde el paso 11 del montaje, que ya
    exige que NINGUNA propuesta equivocada caiga sobre una cara. El carton
    lleva la decision; la imagen lleva a alguien haciendo su trabajo.

LAS DOS REGLAS DE COLOCACION, QUE SE COMPRUEBAN
    1. Las seis ranuras de propuesta -r08, r10, r15, r20, r24, r29- NO llevan
       cara de nadie. Es el paso 11.
    2. Los primeros planos solo caen en ranuras SIN carton. Un carton denso
       encima de un primer plano tapa lo unico que ese plano tiene.

LOS CENITALES: TRES, Y CADA UNO SE GANA EL SITIO
    r29  las dos entradas en una hoja -Ines y Alba existen en la pieza solo
         como lo que el caso tiene de ellas, y eso es literalmente una hoja-.
    r35  la carpeta unica rebosada y sin indice, que es el alegato final.
    r33  la direccion tachada y escrita encima.
    Eran diecisiete.

LA RIMA, QUE AHORA ES UN LUGAR Y NO UN BODEGON
    r01 / r39   la misma fachada del alojamiento, la misma calle y la misma
                camara. Al abrir, al amanecer y vacia. Al cerrar, al final
                del dia y con gente pasando. El caso se movio y el sitio
                sigue ahi. Las dos pasan por graduar_par.py.
"""

# ranura -> (cuadros, escena, plano, registro, [personas], acento, texto)
#            0        1        2      3          4          5       6
R = {}

# ───────────────────────── A · EL ALOJAMIENTO, LA CALLE ────────────────────
R[1] = (240, 'A', 'general', 'dia', [], False, """
Wide establishing shot of the plain street facade of a modest three-storey lodging house in a Colombian city, seen straight on from the opposite pavement, the whole building in frame with a strip of road across the bottom.

It is first light. The sun is still low and behind the building, so the facade itself is in shade and the upper floor catches a pale edge of light along its top. The street is EMPTY: no people, no vehicles, no movement. A single plain door, rendered windows with plain frames, a narrow pavement, a kerb.

Ordinary and unremarkable: not sinister, not derelict, not picturesque. No window bars, no grilles, no padlocks, no shop fronts.

What the camera asserts by standing across the street at this hour: this is the address the case is about, and at this moment there is nothing to see at it.
""")

R[2] = (180, 'A', 'medio', 'contraluz', ['nora'], True, """
Medium shot of %(nora)s, taken from OUTSIDE a plain room looking in through an open doorway. The dark grey door frame runs down the left of the frame close to camera, slightly out of focus, and boxes her.

She stands just inside the room with one hand STILL RESTING ON THE EDGE OF THE OPEN DOOR, her body already turned away toward the room and her head TURNED BACK over her shoulder, looking past the camera and not at it. The folded cardigan is over her other forearm. Her mouth is closed.

Behind her a window at the far wall is the only bright thing in the picture; she reads as a near-silhouette with light along one cheek and one shoulder.

What the camera asserts by standing outside the door: we are being shown her from the threshold, which is as far as anything here has actually been established.
""")

R[3] = (150, 'A', 'primer plano', 'contraluz', ['nora'], True, """
CLOSE-UP of %(nora)s, head and shoulders, turned three-quarters to camera, the top of the folded cardigan just in the bottom of the frame.

Distant expression: her gaze is level and directed past the lens to the side, mouth closed and relaxed, brow flat. She is NOT defiant, NOT frightened, NOT pleading, NOT sad. She is simply not answering.

A window out of frame behind her left shoulder puts a clean edge of light down that side of her face and jaw and leaves the other side in deep shadow. The background is a plain dark wall with nothing on it.
""")

# ───────────────────────── B · EL PUERTO DE SALIDA ─────────────────────────
R[4] = (146, 'B', 'detalle', 'hero', [], False, """
Detail shot from INSIDE the cab of a plain van, the camera at the height of the dashboard looking forward and slightly down.

A plain dark grey phone lies FACE DOWN on the dashboard shelf, close to camera and sharp. Beyond it, through the windscreen and softly out of focus, a low working jetty and flat water at the end of the day, with the far bank dissolved in haze.

The cab interior nearest the camera is almost black. The only light in the picture is the pale band of water and sky through the glass.

No hands, no people. No number plate, no instrument markings, no text anywhere.

What the camera asserts: the thing that carries the instructions is here, turned over, and the place it is pointed at is out there.
""")

R[5] = (244, 'B', 'general', 'hero', ['ivan'], True, """
THE HERO SHOT OF THE PIECE. Wide shot of a small coastal loading dock at the very end of the day, the camera at standing height on the quay and perfectly level.

A low concrete jetty runs from the lower right of the frame out into flat still water. Beyond the water the far bank is a soft dark band dissolved in haze. The sun is already down; the sky is a long pale gradient low on the horizon and everything in front of it is dark.

A plain van is parked on the quay at the left, side on, unlit. %(ivan)s stands SMALL beside its front wheel, a dark upright figure with the pale water behind him, one arm down and the phone in that hand, looking out along the jetty and away from the camera. He occupies very little of the frame.

Most of the picture is dark quay and dark water. No cargo, no crates, no boats, no other people, no bollards with writing, no signage of any kind.

What the camera asserts by standing this far back at this hour: this is the point of exit the case is named for, and one man is standing at it doing nothing in particular.
""")

R[6] = (209, 'B', 'medio', 'contraluz', ['ivan'], True, """
Medium shot of %(ivan)s at the OPEN DRIVER'S DOOR of the plain van, seen from outside and slightly in front, the camera at chest height and level.

He is HALFWAY INTO GETTING IN: one foot already up on the sill, one hand on the top of the door frame, his weight still on the ground, his head turned to look back down the quay the way he came. The phone is in the hand on the door frame. The sleeves are rolled twice.

The open door and the dark cab behind him fill the right of the frame. The pale water and low sky at the left are the only bright values, so he reads largely as silhouette with light along his forearm and the line of his jaw.

What the camera asserts by catching him between the ground and the cab: he is in the middle of leaving, and the picture does not say where to.
""")

# ──────────────────── C · LA OFICINA DEL FISCAL, 7 DE LA TARDE ─────────────
R[7] = (285, 'C', 'medio', 'contraluz', ['fiscal'], False, """
Medium shot of %(fiscal)s at his desk in a small office at seven in the evening, the camera at seated eye level and level, him in the RIGHT THIRD of the frame and turned three-quarters away toward the window.

He has just PUSHED BACK from the desk: his chair is turned out, his spine against the backrest, one hand still resting on the desk edge and a plain pencil still held in it, the other arm hanging. He is looking out of the window, not at the screen. The plain metal thermos stands near his elbow.

Behind him a tall window holds the last blue of the day and is the brightest thing in the room. A desk lamp low on the desk throws a small warm pool over the papers and leaves the ceiling and the far wall in deep shadow.

The LEFT HALF of the frame is bare dark office wall, deliberately empty.

What the camera asserts by leaving half the frame empty at this hour: the decision is being made at the end of a long day, by one tired person, alone.
""")

R[8] = (260, 'C', 'detalle', 'dia', ['investigador'], False, """
Shot taken from BESIDE the prosecutor's shoulder, looking across his desk at the chair opposite. NO FACE IS VISIBLE ANYWHERE IN THIS PICTURE.

The investigator sits in that chair, seen only from the chest down: a plain mid grey open zip jacket, forearms on his knees, both hands open and turned upward in the middle of explaining something. His head is ABOVE the top edge of the frame and is not visible.

On the floor beside his chair a grey box file sits OPEN with its lid leaning against the chair leg, stuffed with plain grey folders standing upright, far more of them than the desk could hold.

Ordinary office daylight from a window at the left: a clear lit side and a clear shadow side.

What the camera asserts by cutting the head off: what is being proposed matters here, and who is proposing it does not.
""")

R[9] = (162, 'D', 'general', 'dia', [], False, """
Wide shot of a plain two-storey residential building on an ordinary Colombian street, seen from the opposite pavement at midday, straight on and level.

Rendered walls, a closed metal gate at street level, plain windows with the curtains drawn on the upper floor. Flat midday light from high and slightly left, so the wall is bright and the gate recess is in deep shadow.

The street is empty of people. Ordinary and unremarkable: not sinister, not derelict.

No window bars, no grilles, no padlocks, no numbers, no signage, no text anywhere.

What the camera asserts by standing across the street: this is a different address from the first one, and it looks like every other house on its block.
""")

R[10] = (234, 'D', 'detalle', 'dia', [], False, """
Detail shot of the closed metal gate of that same residential building, the camera close and level, filling the frame with the gate and the strip of rendered wall beside it. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

A plain doorbell button on its small plate is at the right of the frame, and nothing else. The gate is shut. The letterbox slot is empty and dark.

Hard midday light rakes across the gate from the left, so the vertical bars throw clean parallel shadows onto the wall behind them.

No hands, no people, no numbers, no name plate, no text of any kind.

What the camera asserts by coming this close to a closed gate: everything that is known about this address was said from the pavement.
""")

# ───────────────── E · EL CORREDOR DE CONTROL, LAS SEIS DE LA MANANA ───────
R[11] = (152, 'E', 'medio', 'contraluz', ['nora'], True, """
Medium wide shot of %(nora)s SEATED ALONE on a plain bench against the wall of a long institutional corridor, the camera at seated eye level, level, and far enough back to show the empty bench continuing away on both sides of her.

She sits upright with her hands in her lap and the folded cardigan across her knees, her head level and turned slightly toward the far end of the corridor. She is waiting and she is composed. Nobody else is in the frame.

The far end of the corridor is a tall window full of grey early light, and it is the only bright thing in the picture. She and the bench and the near wall are almost in silhouette against it, with a thin edge of light along her shoulder.

NO ARREST, no restraint, no hands on her, no escort, no cell, no bars.

What the camera asserts: whatever happened, happened before this, and what the case records is this — a time, a place, and a person sitting in it.
""")

R[12] = (208, 'E', 'detalle', 'contraluz', [], False, """
Detail shot of a plain round institutional wall clock high on a corridor wall, seen from BELOW AND SLIGHTLY TO THE SIDE, from the eye level of somebody sitting on a bench underneath it.

The clock face is plain and pale with two plain hands and NO numerals and no text of any kind. The wall around it is bare.

The corridor window out of frame to the right throws a long shadow of the clock body across the wall. The rest of the wall falls into deep shade toward the top of the frame.

No people, no hands, no furniture other than the wall.

What the camera asserts by looking up from the bench: the hour is the thing that had to be written down, and it is the only thing in this corridor worth looking at.
""")

# ───────────────── F · LA RECEPCION DEL ALOJAMIENTO, LA MANANA ─────────────
R[13] = (209, 'F', 'medio', 'dia', ['recepcionista'], True, """
Medium shot of %(recepcionista)s ARRIVING at the plain reception counter of the lodging house, seen from inside the hall, the camera at standing height and level.

He is in the middle of coming through the gap at the end of the counter: one hand pushing the hinged counter flap up and back, the other hand holding a ring of plain keys and a grey jacket folded over the same forearm. His weight is on the forward foot. He is looking down at the counter top as he comes, not at the camera.

Behind him the open street door is a bright rectangle of ordinary morning. Behind the counter, plain pigeonholes and a closed ledger.

Nobody else in the frame. No luggage, no guests, no register entries visible, no numbers on the pigeonholes.

What the camera asserts by catching him on the way in: he arrives afterwards, and this is what arriving for work looks like.
""")

R[14] = (167, 'F', 'general', 'dia', ['recepcionista'], True, """
Wide shot of the whole reception hall of the lodging house seen from the FAR END, the camera at standing height and perfectly level, so the counter is small and off to the right and most of the frame is bare hall, plain staircase and plain floor.

%(recepcionista)s stands behind the counter, SMALL in the frame, both forearms resting on the counter top, the keys on the wood beside his hand, head slightly lowered. He is not doing anything.

Ordinary morning light comes in from the street door at the left, lies in a long bright band across the floor, and leaves the staircase and the depth of the hall in shadow.

Nobody else anywhere in the frame.

What the camera asserts by standing this far back: a whole building, one person in it, and nothing visibly happening.
""")

R[15] = (167, 'E', 'general', 'contraluz', [], False, """
Wide shot straight down the length of that same long institutional corridor, the camera at standing height and perfectly level, the plain bench empty along the left wall. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

The far end is a tall window full of flat grey light; the near two thirds of the corridor are in deep shade, with the bench, the skirting and the closed doors reading as edges.

Completely empty: nobody on the bench, nobody in the corridor, no furniture other than the bench and the closed doors.

No padlocks, no bars, no bolts, no numbers on the doors, no notices, no text.

What the camera asserts by showing the same corridor with nobody in it: the rule being proposed here does not depend on anybody in particular, and that is the problem with it.
""")

# ───────────────────── G · LA SALA DE AUDIENCIAS ───────────────────────────
R[16] = (272, 'G', 'general', 'dia', ['fiscal', 'nora'], True, """
Wide shot of a modest hearing room from the BACK of the public benches, the camera at seated height and perfectly level, taking in the whole room: empty benches in the foreground, a plain low bench-table across the far end, plain tables left and right.

%(fiscal)s stands at the left-hand table, side on to camera, one hand flat on an open folder, mid-sentence, addressing the far end of the room. %(nora)s sits at the right-hand table, small, turned slightly toward him, the folded cardigan on the table beside her.

Tall plain windows run down the right-hand wall and put a bright band along that side of the room; the public benches nearest the camera are in shadow.

The far bench-table is EMPTY in this shot. No robes, no gowns, no insignia, no coat of arms, no flags, no plaques, no text anywhere.

What the camera asserts by sitting at the back: this is what a request looks like when it is made properly, from the distance at which the public would see it.
""")

R[17] = (257, 'G', 'medio', 'dia', ['fiscal'], True, """
Medium shot of %(fiscal)s standing at the plain table in the hearing room, taken from BEHIND AND SLIGHTLY TO HIS LEFT so the camera sees his shoulder, the side of his jaw, and what he is looking at rather than his full face.

He stands with his weight even, one hand resting flat on an open folder on the table and the other lifted slightly from the elbow, held still in the middle of saying something. The thermos is on the table behind the folder.

Beyond him, out of focus, the far end of the room and the plain bench-table.

The window light comes from the right and rims his shoulder and the side of his head, leaving his near side in shade.

What the camera asserts by standing at his shoulder: it matters what he is saying and it does not matter what his face is doing while he says it.
""")

R[18] = (102, 'G', 'detalle', 'dia', [], False, """
Detail shot of a single plain empty chair at a plain table in the hearing room, seen from the FAR END of the room, the camera low and level, the chair pushed slightly back from the table as if someone has just stood up from it.

A soft grey cardigan is folded over the back of the chair. Nothing else on the table.

The window light from the left falls across the seat of the chair and the table top and leaves the floor under the table in deep shadow.

No people, no hands, no face anywhere. No papers with writing, no numbers.

What the camera asserts from the far end of the room: the seat is occupied by somebody in this case, and from here you can see the chair and not the person.
""")

R[19] = (152, 'G', 'primer plano', 'dia', ['jueza'], False, """
CLOSE-UP of %(jueza)s, head and shoulders, facing the camera almost straight on, seated.

Resolved expression: level gaze directed slightly past the lens, mouth closed and relaxed, brow untroubled, chin level. She is NOT stern, NOT severe, NOT dismissive, NOT triumphant and NOT troubled. She is a person at the end of a working day who has decided something.

The reading glasses are folded in one hand at the bottom of the frame.

Plain window light from the left gives a clear lit side and a clear shadow side across her face. The background is a plain out-of-focus wall with nothing on it.

No robe, no gown, no sash, no insignia, no emblem, no nameplate, no text.
""")

R[20] = (237, 'G', 'medio', 'contraluz', [], False, """
Shot of the plain low bench-table at the far end of the hearing room, taken from the body of the room at standing height and perfectly level. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

The bench-table is EMPTY: a plain writing surface, one plain empty chair behind it pushed in, a closed grey folder squared on the top, and nothing else.

A tall window directly behind the bench fills the back of the frame with flat grey light, so the bench and the chair read almost entirely as dark silhouette and edge against it, and the floor in front of them is in shade.

No robe, no gown, no insignia, no coat of arms, no flag, no plaque, no gavel, no text.

What the camera asserts by looking at an empty bench against the light: a decision was taken here, and what it rested on is not visible from the room.
""")

R[21] = (131, 'K', 'general', 'dia', [], False, """
Wide shot of the front door of an ordinary small house on a residential street, seen straight on from the pavement, the camera at standing height and level.

The door is plain and CLOSED. A narrow step, a plain rendered wall either side, a window with the curtain drawn. Ordinary flat daylight from high and left: a bright wall, a dark recess at the door.

Completely empty: no people, no movement, no objects on the step.

No numbers, no nameplate, no signage, no padlock, no grille, no text.

What the camera asserts: the measure that was asked for was this door, and it is the only thing in the case that nobody argued about.
""")

# ──────────────── H · EL CORREDOR DEL JUZGADO ─────────────────────────────
R[22] = (215, 'H', 'medio', 'contraluz', ['ivan'], True, """
Medium shot of %(ivan)s SEATED on a plain bench in a courthouse corridor, the camera at seated eye level, level, a little to one side so the empty bench runs away behind him.

He sits forward with his elbows on his knees and both hands loose between them, the phone face down on the bench beside his thigh. His head is up and turned to look down the corridor toward the light. His sleeves are rolled twice.

The far end of the corridor is a tall bright window; he is largely in silhouette with a clean edge of light along his forearms, the top of his back and the line of his jaw.

Nobody else is in the frame. No restraint of any kind, no escort, no cell, no bars.

What the camera asserts: he is waiting, the same as anybody waits, and nothing in this picture says what for.
""")

R[23] = (300, 'H', 'general', 'contraluz', ['ivan', 'representante'], True, """
Wide shot straight down a long courthouse corridor, the camera at standing height and perfectly level, a plain bench along the left wall and closed doors along the right.

%(ivan)s sits SMALL on the bench in the middle distance, leaning forward, a dark shape against the light. Much nearer the camera and at the right, %(representante)s stands with her back half to us, the grey document wallet held against her chest with both arms, STOPPED, looking down the corridor toward him.

They are far apart and there is a long stretch of empty floor between them.

The far end of the corridor is a tall window full of flat grey light. Everything nearer the camera is in deep shade.

No confrontation, no gesture, no approach, no restraint, nobody else in the corridor.

What the camera asserts by putting the whole corridor between them: two things are being asked for in the same place, and they have not met.
""")

R[24] = (294, 'H', 'detalle', 'contraluz', [], False, """
Detail shot of a plain grey document wallet lying CLOSED on a plain corridor bench, the camera close and at bench height, level. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

The wallet is squared on the bench slat with its flap down and its tie wound shut. A plain dark grey phone lies beside it, FACE DOWN. Nothing else on the bench.

The corridor window far out of frame throws a long low band of light across the bench top and across the top of the wallet, and leaves everything below the bench edge in deep shade.

No hands, no people, no labels, no numbers, no text of any kind.

What the camera asserts by photographing a closed wallet: what is inside it is what the defence is asking to see, and in this picture it is shut.
""")

# ───────────────────── I · LA SALA PEQUENA, LINA ───────────────────────────
R[25] = (206, 'I', 'primer plano', 'dia', ['lina'], True, """
CLOSE-UP of %(lina)s, head and shoulders, facing the camera three-quarters on. The top of the thin folded paper she holds is just visible at the bottom edge of the frame, held in both hands.

Guarded expression: her head is inclined slightly down and her eyes are raised toward something past the lens, mouth closed, brow flat, chin tucked. She is NOT frightened, NOT tearful, NOT defiant, NOT ashamed. She is listening to something being read out and waiting to understand it.

Plain window light from the left gives a clear lit side and a clear shadow side across her face. The background is a plain out-of-focus grey wall with nothing on it.
""")

R[26] = (232, 'I', 'medio', 'dia', ['lina'], True, """
Medium shot of %(lina)s STANDING ALONE in a small plain hearing room, the camera at her eye level and perfectly level, her body square to camera and a wide margin of bare room on both sides of her.

She stands with her weight even, both hands holding the thin folded paper at waist height, her head level and turned slightly to one side as she listens. The yellow cuff band is on her left sleeve.

A plain table and one plain empty chair sit behind her, out of focus. The room is otherwise bare.

Light comes from a window out of frame at the left: a bright wall on that side, a clear shadow on the other, and the corners of the room dark.

Nobody else in the frame.

What the camera asserts by leaving so much empty room around her: what is being said about her is wide enough to fit anybody, and she is the one standing in it.
""")

R[27] = (289, 'I', 'general', 'dia', ['lina'], True, """
Wide shot of the whole small hearing room from the BACK CORNER, the camera at standing height and perfectly level, taking in two bare walls, the plain table, the empty chairs and a lot of plain floor.

%(lina)s stands SMALL and alone near the middle of the room, facing away from the camera toward the plain table, the folded paper in both hands at waist height. She occupies very little of the frame.

A tall window on the left wall lays a hard bright parallelogram of light across the floor; she is standing just outside it, in the shade.

Nobody else anywhere in the room.

What the camera asserts from the corner of the room: one sentence was read here, it named nothing, and this is the whole of what it was read into.
""")

# ───────────── J · LA SALA DE TRABAJO DEL EQUIPO, DE NOCHE ────────────────
R[28] = (285, 'J', 'medio', 'hero', ['otra_fiscal'], False, """
Medium shot of %(otra_fiscal)s alone at a long work table in a team room at night, the camera at seated eye level and perfectly level, her at the right of the frame.

She is HALFWAY THROUGH LIFTING a plain grey folder out of a stack: it is already clear of the pile and still tilted, both her hands under it, her head down and turned toward it. The grey enamel mug stands near her elbow. Two more stacks sit further along the table.

One low desk lamp at her end of the table is the only light in the room. It lifts her face, her hands and the near corner of the table out of the dark, and everything beyond — the far end of the table, the walls, the ceiling — falls away into near-black.

Nobody else in the room. No text, no labels, no numbers on anything.

What the camera asserts at this hour with one lamp on: somebody is reading this file for the first time, late, and alone.
""")

R[29] = (118, 'J', 'cenital', 'hero', [], False, """
CENITAL — ONE OF ONLY THREE IN THIS PIECE.

Overhead shot looking STRAIGHT DOWN at a single plain sheet of paper lying on a dark work table, the camera directly above and perfectly level. NO HEAD, NO FACE, NO HAND AND NO SHOULDER ANYWHERE IN THIS PICTURE.

On the sheet there are exactly TWO SHORT ENTRIES, one under the other, each reduced to a plain flat grey bar, with a wide empty margin of paper under them and nothing else on the page. The rest of the table around the sheet is bare and dark.

A desk lamp out of frame at one side lights the sheet and the table immediately around it and leaves the edges of the frame in near-black.

No writing, no readable character, no numbers, no names, no hands, no people.

What the camera asserts by coming straight down on two lines: this is everything the file holds about two people, and it is being proposed that it is enough.
""")

# ─────────────── B otra vez · EL MUELLE, AHORA DE DIA ──────────────────────
R[30] = (285, 'B', 'medio', 'dia', ['ivan'], True, """
Medium shot of %(ivan)s standing beside the plain van on the same coastal quay, but now in ORDINARY FLAT DAYLIGHT, the camera at chest height and perfectly level.

He stands square and still with his weight even on both feet, one hand resting on the open edge of the van's side door and the other at his side holding the phone, looking along the quay away from the camera. Shoulders level. Sleeves rolled twice.

The side door of the van is slid open behind him and the inside of it is plainly visible and EMPTY.

Behind the quay, the flat water and the low far bank under an overcast sky. Daylight from high and slightly left: a lit side and a shadow side on the van, a clear dark under it.

Nobody else in the frame. No cargo, no crates, no passengers, no number plate, no signage.

What the camera asserts by coming back here in daylight: the same place, the same man and the same vehicle, and this time the case can say exactly what it is alleging happened in it.
""")

R[31] = (113, 'B', 'detalle', 'dia', [], False, """
Detail shot into the open side door of the plain van from outside, the camera at the height of the sill and level, the doorway filling most of the frame. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

Inside there are FOUR plain seat places in two rows, all of them EMPTY, the upholstery plain grey and unmarked. Daylight from behind the camera reaches the first row and the second row falls into shadow.

Nothing on the seats and nothing on the floor of the van. No luggage, no people, no straps, no markings, no text.

What the camera asserts by counting empty seats: four is a number the case can state, and it is the kind of thing a description is supposed to contain.
""")

# ─────────── J otra vez · LA SALA DE TRABAJO, LAS MODIFICACIONES ───────────
R[32] = (161, 'J', 'general', 'hero', ['otra_fiscal', 'investigador'], False, """
Wide shot of the team room at night from the FAR END of the long table, the camera at standing height and perfectly level.

%(otra_fiscal)s sits at the near end in the pool of the one desk lamp, bent over an open folder. Further down the same table and at the edge of that light, %(investigador)s stands with the grey box file under one arm, half turned away, on his way out of the room.

The length of the table between them is covered in plain stacks. Beyond the lamp the room goes to near-black: the walls, the ceiling and the far door are only edges.

Nobody else in the room. No screens, no text, no labels, no numbers.

What the camera asserts from the end of the table: the work happens here, at night, with one lamp, and the distance between the two of them is the shape of the problem.
""")

R[33] = (189, 'J', 'cenital', 'hero', [], False, """
CENITAL — ONE OF ONLY THREE IN THIS PIECE.

Overhead shot looking STRAIGHT DOWN at a plain sheet lying on the dark work table under the lamp, the camera directly above and perfectly level. NO HEAD, NO FACE AND NO SHOULDER ANYWHERE.

One plain flat grey bar on the sheet has been STRUCK THROUGH with a single clean horizontal line, and a second plain flat grey bar is written in the space immediately above it. Everything else on the sheet is untouched. The paper around it is otherwise plain.

One bare hand in a plain light grey sleeve rests flat on the table at the edge of the frame, still, not touching the sheet.

The lamp lights the sheet and the hand and leaves the rest of the table in near-black.

No readable character anywhere, no numbers, no names, no letters.

What the camera asserts by coming down on one struck line: a correction was made, it is visible, and the thing underneath it is still there.
""")

R[34] = (241, 'J', 'primer plano', 'hero', ['otra_fiscal'], False, """
CLOSE-UP of %(otra_fiscal)s at the work table at night, head and shoulders, three-quarters to camera, her head slightly down.

Her expression is plain working concentration with a trace of doubt: eyes directed down and to one side at something on the table, mouth closed, brow very slightly drawn. She is NOT alarmed, NOT suspicious, NOT accusing, NOT weary to the point of drama.

The desk lamp is low and out of frame at her side: it lights one side of her face and the front of her shoulder cleanly and leaves the other side and the whole background in near-black.
""")

# ───────────── J otra vez · LA CARPETA UNICA Y EL FINAL DEL DIA ────────────
R[35] = (109, 'J', 'cenital', 'hero', [], False, """
CENITAL — THE THIRD AND LAST IN THIS PIECE.

Overhead shot looking STRAIGHT DOWN at ONE single grey folder lying closed on the dark work table, the camera directly above and perfectly level. NO HEAD, NO FACE, NO HAND AND NO SHOULDER ANYWHERE.

The folder is OVERFULL: the sheets inside it are far too many for the cover, they bulge it open along the fore edge, and several of them stick out past the edges of the cover at different angles. There are NO dividers, NO tabs, NO index and NO separation of any kind in the stack: it is one undifferentiated block of paper.

The table around it is bare and dark.

The lamp out of frame lights the folder and a little of the table and leaves the frame edges in near-black.

No readable character, no numbers, no labels, no tabs, no colour.

What the camera asserts by coming straight down on one bulging folder: everything is in here, and nothing in here is separated from anything else.
""")

R[36] = (205, 'J', 'medio', 'hero', ['otra_fiscal'], False, """
Medium shot of %(otra_fiscal)s at the work table at night, the camera at seated eye level and perfectly level.

She is HALFWAY THROUGH CLOSING the overfull folder: both hands are on the cover pressing it down toward the stack, the cover still tilted and not yet flat, the fore edge still bulging under her palms. Her head is down and her shoulders are forward with the effort of it. The mug is pushed away to the edge of the table.

The one desk lamp lights her hands, the folder and her lowered face and leaves the room behind her in near-black.

Nobody else in the room. No text, no labels, no numbers.

What the camera asserts: the last thing anybody does with this file is force it shut.
""")

R[37] = (145, 'J', 'general', 'hero', [], False, """
Wide shot of the empty team room at night, the camera at standing height and perfectly level, the long work table running away from the camera. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

The one desk lamp is still ON at the far end of the table, throwing its small pool of light over the overfull grey folder and the empty chair pushed back from it. Everything else — the length of the table, the walls, the ceiling, the door — is in near-black and reads only as edges.

Nobody in the room. No screens, no text, no labels, no numbers.

What the camera asserts by staying after everybody has gone: the file is finished, the light is still on, and this is the state it will be handed over in.
""")

# ───────────────── K · EL CORREDOR, Y LA RIMA DEL CIERRE ───────────────────
R[38] = (292, 'H', 'general', 'contraluz', ['otra_fiscal'], False, """
Wide shot straight down the long courthouse corridor at the end of the day, the camera at standing height and perfectly level, the plain bench empty along the left wall.

%(otra_fiscal)s is WALKING AWAY from the camera down the middle of the corridor, SMALL, seen from behind, the grey box file carried under one arm, mid-stride. She is almost at the far end.

The tall window at the far end is full of low evening light and she reads as a dark upright shape against it, with a thin edge of light down one side of her.

Nobody else in the corridor. No doors open, no notices, no text.

What the camera asserts by watching somebody leave down the whole length of it: the six actuaciones are behind her, and the review the piece asks for starts now.
""")

R[39] = (163, 'A', 'general', 'dia', [], False, """
THE CLOSING HALF OF THE RHYME. Wide shot of the plain street facade of the SAME modest three-storey lodging house, from the SAME position on the opposite pavement, the SAME camera height and the SAME framing as the opening shot. The building must match it exactly: same number of floors, same windows, same door, same kerb.

What has changed is the hour and the street. It is now the END OF THE DAY: the light is low and warm-grey and comes from the left along the street, so the facade is lit across its front and throws a long shadow to the right.

And the street is NO LONGER EMPTY: four or five ordinary people are passing along the pavement in both directions, each one occupied with their own business, none of them looking at the building, all of them small and none of them individually identifiable. No vehicles.

No window bars, no grilles, no padlocks, no signage, no text.

What the camera asserts by coming back to the same frame at dusk: the case moved through all of this and the address is still an address, with people walking past it.
""")

CARTONES = {1, 7, 8, 10, 14, 15, 18, 20, 21, 23, 24, 26, 27, 29, 31, 37}
PROPUESTAS = {8, 10, 15, 20, 24, 29}

# CUERPO SI, CARA NO
#     El paso 11 del montaje prohibe que una propuesta equivocada caiga sobre
#     una CARA, no sobre una persona. r08 lleva al investigador explicando,
#     pero encuadrado del pecho para abajo: la cabeza queda por encima del
#     borde del cuadro. Es el plano canonico para esto -lo que se propone
#     importa, quien lo propone no- y se declara aqui para que el chequeo no
#     lo confunda con un descuido.
SIN_ROSTRO = {8}


def comprobar():
    """Las reglas de colocacion de la biblia, antes de gastar un credito."""
    fallos = []
    tot = sum(v[0] for v in R.values())
    if len(R) != 39:
        fallos.append('hay %d ranuras, no 39' % len(R))
    if tot != 8006:
        fallos.append('suman %d cuadros, no 8006' % tot)
    for n in sorted(PROPUESTAS):
        if R[n][4] and n not in SIN_ROSTRO:
            fallos.append('r%02d es propuesta y muestra una cara: %s'
                          % (n, R[n][4]))
        if n in SIN_ROSTRO and 'NO FACE' not in R[n][6].upper():
            fallos.append('r%02d se declara sin rostro y el prompt no lo exige'
                          % n)
    for n, v in sorted(R.items()):
        if v[2] == 'primer plano' and n in CARTONES:
            fallos.append('r%02d es primer plano y lleva carton' % n)
    cen = [n for n, v in sorted(R.items()) if v[2] == 'cenital']
    if len(cen) > 3:
        fallos.append('%d cenitales, el tope es 3: %s' % (len(cen), cen))
    seg = [n for n in sorted(R) if n + 1 in R
           and R[n][2] == 'cenital' and R[n + 1][2] == 'cenital']
    if seg:
        fallos.append('cenitales seguidos en %s' % seg)
    return fallos, tot


if __name__ == '__main__':
    import collections
    fallos, tot = comprobar()
    print('%-5s %5s %-4s %-13s %-10s %-28s %s'
          % ('ran', 'cuad', 'esc', 'plano', 'luz', 'gente', 'carton'))
    for n, v in sorted(R.items()):
        print('r%02d  %5d %-4s %-13s %-10s %-28s %s'
              % (n, v[0], v[1], v[2], v[3], ','.join(v[4]) or '-',
                 ('PROPUESTA' if n in PROPUESTAS else 'si') if n in CARTONES else ''))
    print()
    esc = collections.Counter(v[1] for v in R.values())
    pl = collections.Counter(v[2] for v in R.values())
    lu = collections.Counter(v[3] for v in R.values())
    gente = collections.Counter(p for v in R.values() for p in v[4])
    print('escenas  ', dict(sorted(esc.items())))
    print('planos   ', dict(pl))
    print('luz      ', dict(lu))
    print('reparto  ', dict(gente.most_common()))
    print('con gente %d de %d ranuras' % (sum(1 for v in R.values() if v[4]), len(R)))
    print('%d cuadros' % tot)
    print()
    print('FALLOS:', fallos or 'NINGUNO')
