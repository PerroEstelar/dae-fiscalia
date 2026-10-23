# -*- coding: utf-8 -*-
r"""El repertorio del P3C5 v2: DOCE ESCENAS en cuarenta y tres angulaciones,
bajo la BIBLIA_puesta_en_escena_P3.

CONTRA LA v1
    43 placas distintas, 22 cenitales nadir, 7 con cara, 3 lugares.
    Aqui: 12 lugares, 3 cenitales, 26 ranuras con gente, 3 primeros planos.

LO QUE NO SE TOCA, PORQUE ES EL ARGUMENTO
    r33 / r35   LA RIMA MAYOR. La mesa de Oscar y la mesa de Tomas al
                terminar la practica probatoria: mismo encuadre, mismo
                cenital, y lo unico que cambia es lo que hay encima. Es el
                parrafo que el documento titula «resultado de la practica
                probatoria» puesto en una imagen, y es la razon de ser de la
                pieza. Se queda, y se gradua con graduar_par.py.

                Lo que cambia es que ahora NO ESTA SOLA: r32 es el primer
                plano de Oscar y r36 el de Tomas. Las dos mesas quedan
                abrazadas por las dos caras, y la asimetria -que es el
                contenido- aterriza entre dos personas y no entre dos
                bodegones.

    r01 / r43   las dos bandejas: lo ofrecido y lo admitido, que es la
                primera linea del documento. Se quedan, pero YA NO SON UNA
                INFOGRAFIA: se filman a altura de mesa en la sala, con la
                sala detras desenfocada. El mismo dato, dentro de un sitio.

LOS TRES CENITALES, Y POR QUE SE GANAN EL SITIO
    r15  la pagina del cuaderno, que es el verbatim de las tres anotaciones.
    r33  la mesa de Oscar.
    r35  la mesa de Tomas.
    Eran veintidos.

QUIEN GANA CARA, Y QUIEN NO
    Andres, la fiscal y el defensor dejan de ser mobiliario. La PERITA no:
    su ranura es justamente la de la propuesta de calificar credibilidad, y
    el paso 11 prohibe una cara ahi. Su plano es el atril vacio.

    La tercera mujer del alegato sigue sin dibujarse de ninguna forma.
"""

# ranura -> (cuadros, escena, plano, registro, [personas], acento, texto)
#            0        1        2      3          4          5       6
R = {}

# ───────────── D · LA MESA DE LOS MEDIOS, EN LA SALA ─────────────
R[1] = (167, 'D', 'detalle', 'dia', [], False, """
Detail shot across the evidence table of a hearing room, the camera AT TABLE HEIGHT and perfectly level, close to the table top so the wood runs away from the lens.

TWO identical shallow MID GREY document trays sit side by side in the middle of the table, the same size, square with each other and with the table edge. BOTH ARE COMPLETELY EMPTY. The table around them is bare.

Behind the table, softly out of focus, the body of the hearing room: plain empty benches, a plain wall, and a window further back. It is clearly a room, not a backdrop.

No hands, no people, no labels, no numbers, no text of any kind.

What the camera asserts by lying down level with the table: these are two stages of one single thing, and nothing has been put in either of them yet.
""")

R[2] = (300, 'C', 'general', 'contraluz', [], False, """
Wide shot of a modest hearing room from the BACK of the public benches, the camera at seated height and perfectly level, taking in the whole room before anything has begun.

Empty public benches in the foreground, a plain low bench-table across the far end, plain tables left and right, and the evidence table in the middle with two empty trays on it, small from here.

The room is COMPLETELY EMPTY: nobody anywhere, no papers out, no folders open.

Tall plain windows run down the right-hand wall and lay a bright band across that side of the floor; the benches nearest the camera are in shade.

No robes, no gowns, no insignia, no coat of arms, no flags, no plaques, no text anywhere.

What the camera asserts by sitting at the back of an empty room: everything that follows happened here, and from here you can see the whole of it.
""")

# ───────────── A · MEDELLIN: LA CALLE Y EL ALOJAMIENTO ─────────────
R[3] = (230, 'A', 'medio', 'contraluz', ['oscar'], True, """
Medium shot of %(oscar)s standing in the corridor of a modest lodging house, the camera at his eye level and perfectly level, him slightly off centre to the left.

HIS ARMS HANG STRAIGHT DOWN AT HIS SIDES, both of them, relaxed and close to his body, hands open and empty. NEITHER ARM IS RAISED OR EXTENDED and neither hand is gesturing. He stands with his weight even on both feet, shoulders level. His head is upright and level, his eyes looking horizontally toward the camera's left, past the lens. His mouth is closed.

He is not holding anything, not handing anything over, not taking anything.

The corridor runs away behind him to a bright open doorway at the far end, which is the only bright thing in the picture; he reads largely as silhouette with a clean edge of light down one side of his face and shoulder. Plain closed doors along one wall.

What the camera asserts: this is the man the charge is about, and nothing he is doing in this frame is any part of it.
""")

R[4] = (183, 'A', 'general', 'dia', [], False, """
Wide establishing shot of an ordinary street in a Colombian city, seen straight on from the opposite pavement, with the plain three-storey front of a modest lodging house in the middle of the frame and its neighbours either side.

Ordinary overcast midday. The street is quiet: two or three people pass along the pavement, small, each occupied with their own business, none of them identifiable and none of them looking at the building. No vehicles.

Plain rendered walls, a single plain door, plain windows, a narrow pavement, a kerb. Ordinary and unremarkable: not sinister, not derelict, not picturesque.

No window bars, no grilles, no padlocks, no shop fronts, no signage, no text.

What the camera asserts by standing across the street: this is the address and the city, and from the pavement it looks like every other address on the block.
""")

R[5] = (199, 'A', 'medio', 'dia', ['tomas'], True, """
Medium shot of %(tomas)s standing alone against a plain rendered street wall, the camera at his eye level and perfectly level, him centred with bare wall on both sides.

He stands square and still, weight even on both feet, both arms at his sides, hands open and visible. His head is level and turned slightly away from the lens. His mouth is closed. His expression is plain ordinary attention: he is NOT guilty, NOT defiant, NOT pleading, NOT anxious.

He is not holding anything. There is no vehicle, no bag, no document, no map and nobody else in the frame.

Ordinary daylight from one side: a clearly lit side of the wall, a clear shadow on the other, and a real cast shadow at his feet.

What the camera asserts by giving him a bare wall and nothing to do: almost nothing in this case has been established about him, and the picture refuses to suggest otherwise.
""")

# ───────────── C · LA SALA, LO QUE SE ACUSA Y LO QUE NO ─────────────
R[6] = (117, 'C', 'detalle', 'dia', [], False, """
Detail shot of the evidence table in the hearing room, the camera at table height and perfectly level.

THREE plain grey folders lie on the table, CLEARLY SEPARATE from one another, evenly spaced with bare table between them, each squared to the table edge. Nothing else on the table.

Behind the table, softly out of focus, the plain benches and wall of the room.

Window light from the left lays a band across the table and throws a clean small shadow to the right of each folder.

No hands, no people, no labels, no numbers, no text.

What the camera asserts by setting three things apart with space between them: these are three different charges and the picture keeps them apart.
""")

R[7] = (189, 'C', 'general', 'dia', [], False, """
Wide shot of the hearing room from the side, the camera at standing height and perfectly level, taking in the row of plain chairs along the near wall.

The chairs are EMPTY. At one end of the row there is a CLEAR GAP where a chair would be and there is none: bare floor, and the row continues on the other side of it. Nothing marks the gap, nothing fills it.

The room is otherwise ordinary and empty: no people, no papers, no folders.

Daylight from the windows at the right lays a bright band along the floor and leaves the near wall in shade.

No robes, no insignia, no plaques, no numbers on the chairs, no text.

What the camera asserts by photographing a gap in a row: there are two things that are NOT being charged here, and the only honest way to show them is the space where they are not.
""")

# ───────────── E · EL DESPACHO DE ANDRES ─────────────
R[8] = (137, 'E', 'medio', 'dia', ['andres'], False, """
Medium shot of %(andres)s at his desk in a small office, the camera at seated eye level and perfectly level, him at the right of the frame and turned three-quarters toward the desk.

A grey box file sits CLOSED on the desk in front of him, visibly overfull: the lid does not sit flat and the contents push it open along one edge. Both his hands rest on the lid. He is looking down at it.

Ordinary daylight from a window at the left: a clearly lit side of his face and the desk, a clear shadow on the other, and the far corner of the office in shade.

Nobody else in the room. No screens, no text, no labels.

What the camera asserts: the whole of it is here, in one box, and it is being offered as one thing.
""")

R[9] = (246, 'E', 'detalle', 'dia', [], False, """
Detail shot of that same grey box file now OPEN on the desk, the camera close and slightly above, at the height of somebody standing over it, level. NO FACE AND NO HEAD ANYWHERE.

Inside, plain grey folders and loose sheets stand upright packed tight together, far more of them than the box was made for. There are NO dividers, NO tabs, NO index and NO separation of any kind: it is one undifferentiated block of paper.

The lid leans against the side of the box. The desk around it is bare.

Window light from the left falls across the top of the stack and leaves the inside of the box in deep shade.

No readable character anywhere, no numbers, no labels, no tabs, no colour.

What the camera asserts by looking down into it: everything is in here, and nothing in here is separated from anything else.
""")

R[10] = (168, 'E', 'general', 'contraluz', ['andres'], False, """
Wide shot of the whole small office from the doorway, the camera at standing height and perfectly level, so the desk is small and off to one side and most of the frame is plain room.

%(andres)s sits at the desk, SMALL in the frame, bent over the open box file. He is the only person in the room.

The window behind the desk is the brightest thing in the picture; the desk, the chair and he himself read largely as silhouette and edge against it, and the floor and walls nearest the camera are in deep shade.

Nothing else in the room: no shelves of files, no screens, no notices, no text.

What the camera asserts from the door: one person, one box, and a whole room of nothing around it.
""")

R[11] = (159, 'E', 'detalle', 'hero', [], False, """
Detail shot, very close, of a plain wide elastic band stretched around the middle of a thick block of grey folders, the camera level and the band running across the frame. NO PERSON, NO FACE AND NO HANDS ANYWHERE IN THIS PICTURE.

The band squeezes the block so the paper bulges above and below it. Every sheet in the block is pressed against every other one. There are no tabs, no dividers, no coloured edges, nothing that would tell one part from another.

The block fills the frame. Nothing else is visible.

One dominant side light rakes across the paper edges so the band throws a clean shadow across them.

No readable character, no numbers, no labels, no text.

What the camera asserts by coming this close to one band: what holds all of this together as a single request is a piece of elastic.
""")

# ───────────── B · EL ALOJAMIENTO POR DENTRO ─────────────
R[12] = (122, 'B', 'medio', 'contraluz', ['andres'], False, """
Medium shot of %(andres)s standing in the corridor of the lodging house, seen from behind and slightly to one side, the camera at head height and level, so we see his shoulder and the side of his jaw and what he is looking at.

He has STOPPED in front of an OPEN DOORWAY along the corridor and is looking in. One hand hangs at his side, the other rests on the door frame. He is not entering.

Through the doorway, a plain room with a window: it is the brightest thing in the picture, and he is a dark shape against it with a rim of light down one side.

Nobody else in the corridor. The room beyond is empty: no people, no furniture other than a bare bed frame and a chair.

What the camera asserts by stopping him at the door: this is the part he saw with his own eyes, and the picture goes no further in than he did.
""")

R[13] = (197, 'E', 'medio', 'dia', ['andres'], False, """
Medium shot of %(andres)s at his desk, the camera at seated eye level and perfectly level, him at the left of the frame.

A SECOND HAND, in a plain light grey sleeve, enters from the RIGHT EDGE of the frame and is HOLDING OUT a plain dark grey phone to him. The person it belongs to is entirely OUT OF FRAME: no head, no face, no shoulder, only the forearm and the hand.

Andres is reaching to take it: his hand is already under the phone but has not closed on it. He is looking at the phone, not at the arm. The phone is in the air between the two hands, held by one and not yet by the other.

The box file sits closed on the desk beside them.

Window light from the left lights both hands and the phone cleanly and leaves the right of the frame in shade.

What the camera asserts by cutting the other person off at the elbow: this did not happen to him, it was handed to him, and the picture can say exactly that much and no more.
""")

# ───────────── B · EL CUADERNO ─────────────
R[14] = (277, 'B', 'detalle', 'contraluz', [], False, """
Detail shot of a plain closed notebook lying on the sill of a window in a bare room of the lodging house, the camera at sill height and perfectly level, close to it.

The notebook is ordinary, soft-covered, closed, slightly worn at the corners. It lies alone on the sill. Nothing else is on it.

Behind and above it the window is full of flat daylight, so the notebook reads as a dark shape with a clean rim of light along its top edge and spine, and the room to either side falls into deep shade.

No hands, no people, no writing visible, no labels, no text.

What the camera asserts by finding it where it was: this object was in this room, and that is the one thing about it nobody disputes.
""")

R[15] = (113, 'D', 'cenital', 'dia', [], False, """
CENITAL — ONE OF ONLY THREE IN THIS PIECE.

NADIR AERIAL VIEW. The camera is directly above the surface with the lens pointing VERTICALLY DOWNWARD at exactly 90 degrees, like a copy-stand. THE PAGE IS PARALLEL TO THE IMAGE PLANE.

ABSOLUTELY NO WALL, NO WINDOW, NO CEILING, NO ROOM AND NO BACKGROUND IS VISIBLE. NO HEAD, NO FACE, NO HAND AND NO SHOULDER anywhere.

An open notebook lies flat on a DARK GREY table, filling most of the frame. On the right-hand page there is a narrow COLUMN of short grey bars running down the left margin, and beside them a column of shorter bars. Lower down, set apart from the columns with clear blank paper around them, there are THREE separate short grey marks, one under the other.

Nothing else on the page and nothing else on the table.

Even overhead light. No readable character anywhere: no letters, no words, no numbers, no names. Only plain grey bars.

What the camera asserts by coming straight down on one page: this is the whole of what the notebook is said to contain, and three marks of it are what the argument is about.
""")

# ───────────── C · LA PERTINENCIA ─────────────
R[16] = (120, 'C', 'medio', 'dia', ['fiscal'], False, """
Medium shot of %(fiscal)s standing at the plain table in the hearing room, the camera at her eye level and perfectly level, her at the right of the frame.

She stands with her weight even, one hand resting flat on a closed grey folder on the table, the other arm at her side. Her head is turned toward the far end of the room, away from the lens, mid-sentence. Her mouth is closed between words.

Beyond her, softly out of focus, the empty bench-table at the far end of the room.

Window light from the right rims her shoulder and the side of her head and leaves her near side in shade.

No robe, no gown, no insignia, no badge, no text.

What the camera asserts: a reason is being given out loud, and this is what giving it looks like.
""")

R[17] = (228, 'D', 'general', 'contraluz', [], False, """
Wide shot of the hearing room's long evidence table seen from the far end, the camera at standing height and perfectly level, the table running away from the lens and filling the lower half of the frame.

ONE small notebook lies alone in the middle of all that bare table, tiny in the frame. There is nothing else on the table at all: no folders, no papers, no trays, no pen.

Behind the table, the plain empty room and a window at the back wall.

Daylight lays a long band down the table top and leaves the floor beneath it in shade.

No hands, no people, no labels, no numbers, no text.

What the camera asserts by giving one small object a whole table: this is what is being offered, and the room around it is the size of what is not.
""")

# ───────────── D · LA ESTIPULACION ─────────────
R[18] = (152, 'D', 'medio', 'dia', ['fiscal', 'defensor'], False, """
Medium shot across the evidence table in the hearing room, the camera at table height and perfectly level, taking in the table top and, beyond it, two people standing at opposite sides of it.

%(fiscal)s stands at the left and %(defensor)s at the right, both turned slightly toward the table and toward each other, both looking down at a single plain sheet lying between them. Each has one hand resting on the table, well away from the sheet. Neither is reaching.

On the sheet there is exactly ONE short grey bar, a single line, with a wide expanse of blank paper under it.

Window light from the left lays a band across the table and the sheet and leaves both figures half in shade.

No robes, no insignia, no badges, no readable character on the paper.

What the camera asserts by keeping both hands off it: one line was agreed, by two people, and the picture does not extend it.
""")

R[19] = (198, 'D', 'detalle', 'dia', [], False, """
Detail shot of that same plain sheet on the table, the camera close and at a shallow angle from table height, level. NO FACE AND NO HEAD ANYWHERE IN THIS PICTURE.

The single short grey bar sits near the top of the sheet. Everything below it is BLANK PAPER, filling most of the frame.

A plain pen is held SUSPENDED over that blank area by one bare hand in a plain grey sleeve, the nib a clear distance above the paper, not touching it, the hand quite still. The rest of the person is out of frame: only the forearm and the hand.

Nothing else on the table.

Window light from the left throws the shadow of the pen and the hand across the blank paper.

No readable character anywhere, no numbers, no labels.

What the camera asserts by stopping the nib in the air: what was agreed is the line at the top, and what is about to be added is everything under it.
""")

# ───────────── F · LA SALA DE ESCUCHA ─────────────
R[20] = (167, 'F', 'general', 'hero', [], False, """
Wide shot of a small listening room at night, the camera at standing height and perfectly level. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

A plain desk runs along one wall with a single dark screen on it, switched off, and one plain empty chair pushed back from it. The rest of the room is bare.

ONE low desk lamp at the end of the desk is the only light. It lifts the near corner of the desk and the edge of the chair out of the dark and leaves the screen, the walls, the ceiling and the far end of the room in near-black.

Completely empty: nobody in the chair, nobody in the room, nothing on the desk but the screen.

No cables in disarray, no equipment racks, no indicator lights, no numbers, no text.

What the camera asserts by photographing an empty room with one lamp on: six months of a line are being asked for from here, and the request does not say which part.
""")

R[21] = (194, 'F', 'medio', 'contraluz', ['lucia'], True, """
Medium shot of %(lucia)s seated at the desk in the listening room, the camera at her eye level and perfectly level, her at the right of the frame and turned three-quarters toward the screen.

On the screen beside her, a single plain WAVEFORM: one clear isolated burst of sound across an otherwise flat line. She is looking at it, head slightly inclined, both hands resting in her lap. She is still.

The screen is the brightest thing in the picture; she is lit along one side of her face and one shoulder by it and the rest of the room falls away dark behind her.

Nobody else in the room.

No readable character on the screen, no numbers, no labels, no interface, no buttons.

What the camera asserts: there is a recording here that the person in it can recognise, and she is the one looking at it.
""")

R[22] = (131, 'F', 'detalle', 'hero', [], False, """
Detail shot of the screen in the listening room, the camera square to it and perfectly level, the screen filling most of the frame. NO PERSON AND NO FACE ANYWHERE.

On it, a DIFFERENT waveform: a long continuous dense band of speech running the whole width, with no gap and no shape that stands out from any other part of it.

Beside the desk, at the edge of the frame and softly out of focus, ONE plain EMPTY chair, pushed back and turned slightly away.

The screen is the only light in the picture. The chair, the desk edge and the room are in near-black.

No readable character, no numbers, no labels, no interface.

What the camera asserts by putting an empty chair beside a voice: nobody has said whose this is.
""")

# ───────────── G · RENATA ─────────────
R[23] = (241, 'G', 'medio', 'contraluz', ['renata'], True, """
Medium shot of a plain screen standing on a table in a bare room, the camera at seated eye level and perfectly level, square to the screen.

On the screen, %(renata)s is present and clearly visible from the chest up, facing forward, looking into her own camera. She sits upright with her shoulders open and her hands resting in front of her. Her expression is plain ordinary attention: she is NOT distressed, NOT reluctant, NOT evasive.

Behind her, on her side, a plain neutral wall.

The screen is the brightest thing in the picture. The table it stands on, and the room around it, are in shade; an empty chair sits ready on this side of the table.

No interface, no buttons, no icons, no names on the screen, no readable character anywhere.

What the camera asserts by photographing a screen with somebody in it: she is reachable, she is here, and the only thing between her and the room is distance.
""")

R[24] = (203, 'G', 'detalle', 'contraluz', [], False, """
Detail shot of that same table, the camera at table height and perfectly level. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

The screen is now DARK and switched off, a flat near-black rectangle at the back of the frame. A plain closed grey folder has been placed on the table DIRECTLY IN FRONT OF IT, squared and flat, between the camera and the screen.

Nothing else on the table. The empty chair is still there at the edge of the frame.

A window out of frame at one side lays a thin band of light along the table top and across the top of the folder; the screen and the room behind it stay dark.

No labels, no numbers, no text, no interface.

What the camera asserts by setting a folder in front of a switched-off screen: the paper is being offered in the place of the person, and the person was available.
""")

# ───────────── C · LA PERITA ─────────────
R[25] = (293, 'C', 'medio', 'contraluz', [], False, """
Shot of a plain lectern and a plain chair at the side of the hearing room, the camera at standing height and perfectly level. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

The lectern is EMPTY: a bare sloped top with nothing on it. The chair beside it is EMPTY, squared and unoccupied.

A tall window directly behind them fills the back of the frame with flat grey light, so the lectern and the chair read almost entirely as dark silhouette and edge, and the floor in front of them is in shade.

Nobody anywhere in the room. No robe, no gown, no insignia, no microphone, no papers, no plaque, no text.

What the camera asserts by looking at an empty lectern against the light: what is being offered from here is an opinion about whether to believe someone, and the picture declines to put a face to it.
""")

# ───────────── J · LA SALA DE TRABAJO, DE NOCHE ─────────────
R[26] = (296, 'J', 'detalle', 'hero', [], False, """
Detail shot of a large plain chart lying flat on a work table at night, the camera close and slightly above, level. NO FACE AND NO HEAD ANYWHERE IN THIS PICTURE.

The chart is ONE single continuous band of plain grey bars running across the sheet, all the same height, the same width and the same tone, packed edge to edge with NO gaps, NO groupings, NO separations and NO difference between any part of it and any other. It reads as one undifferentiated mass.

Beside it on the table, a separate neat stack of plain sheets squared at the corner, clearly apart from the chart.

ONE desk lamp out of frame lights the chart and the near part of the table and leaves everything beyond in near-black.

No readable character, no numbers, no labels, no axis, no legend, no colour.

What the camera asserts by photographing one unbroken band: three different kinds of money went in here and the picture that came out does not tell them apart.
""")

# ───────────── H · LUCIA EN EL JUICIO ─────────────
R[27] = (222, 'H', 'medio', 'dia', ['lucia'], True, """
Medium shot of %(lucia)s seated on a plain chair against a plain mid grey wall in the hearing room, the camera at her eye level and perfectly level, her body centred and square to camera.

She HOLDS A SMALL SLIP OF PAPER IN BOTH HANDS, raised to chest height, and is LOOKING DOWN AT IT, her head inclined, her eyes on the paper. Her mouth is closed. Her expression is plain ordinary concentration: she is NOT upset, NOT uncertain, NOT ashamed.

The writing on the slip is reduced to plain flat grey bars. The wall behind her is bare.

Window light from the left gives a clear lit side and a clear shadow side across her and the wall.

What the camera asserts: she is looking at something that was handed over in time, and that is all she is doing.
""")

R[28] = (151, 'H', 'medio', 'dia', ['lucia'], True, """
Medium shot of %(lucia)s seated on the SAME plain chair against the SAME plain wall, the camera at EXACTLY the same height and the same framing as before, her body centred and square to camera.

HER HANDS ARE NOW EMPTY AND OPEN, resting apart on her lap, palms upward. She is LOOKING UP AND AWAY past the camera's right shoulder, her head lifted. Her mouth is closed. Her expression is plain ordinary recollection: she is NOT lying, NOT evasive, NOT distressed, NOT defiant.

There is no paper anywhere in the image.

The same window light from the left, the same lit side and shadow side, the same bare wall.

What the camera asserts by repeating the shot with nothing in her hands: the same person, the same seat, and this time nothing in front of her.
""")

R[29] = (284, 'H', 'primer plano', 'dia', ['lucia'], True, """
CLOSE-UP of %(lucia)s, head and shoulders, facing the camera three-quarters on, seated.

Her expression is plain ordinary recollection with nothing performed: eyes directed past the lens and slightly up, mouth closed, brow flat. She is NOT tearful, NOT frightened, NOT defiant, NOT ashamed. She is a person being asked to remember something precisely.

Window light from the left gives a clear lit side and a clear shadow side across her face. The background is a plain out-of-focus grey wall with nothing on it.
""")

# ───────────── C · LA DEFENSA EN EL JUICIO ─────────────
R[30] = (134, 'C', 'medio', 'dia', ['defensor'], False, """
Medium shot of %(defensor)s standing at the defence table in the hearing room, the camera at his eye level and perfectly level, him at the left of the frame.

He stands with one hand flat on a thin stack of marked pages on the table and the other lifted slightly from the elbow, held still in the middle of putting a question. His head is turned away from the lens toward the far side of the room. His jacket is unbuttoned.

Beyond him, out of focus, the body of the room.

Window light from the left: a clearly lit side of his face and the table, a clear shadow on the other.

No robe, no gown, no insignia, no badge, no readable character on the pages.

What the camera asserts: a question is being asked, and this is what asking it looks like.
""")

R[31] = (181, 'B', 'general', 'contraluz', [], False, """
Wide shot straight down the corridor of the lodging house, the camera at standing height and perfectly level, one door standing OPEN along the right-hand wall. NO PERSON AND NO FACE ANYWHERE IN THIS PICTURE.

The open doorway lets a block of flat daylight out across the corridor floor. The far end of the corridor is another bright doorway. Everything nearer the camera is in deep shade.

The corridor is COMPLETELY EMPTY: nobody in it, nobody in the open room, no luggage, no furniture.

No padlocks, no bars, no bolts, no numbers on the doors, no notices, no text.

What the camera asserts by photographing an open door with nobody in it: a door that is not locked is a fact about the door, and the question the case asks is about the person.
""")

# ───────────── EL EJE: LAS DOS MESAS, ABRAZADAS POR LAS DOS CARAS ─────────────
R[32] = (243, 'H', 'primer plano', 'dia', ['oscar'], True, """
CLOSE-UP of %(oscar)s, head and shoulders, facing the camera three-quarters on, seated.

His expression is plain ordinary attention with nothing performed: eyes level and directed past the lens, mouth closed, brow flat. He is NOT menacing, NOT guilty, NOT pleading, NOT defiant. He is a person at the end of a long proceeding, listening.

Window light from the left gives a clear lit side and a clear shadow side across his face. The background is a plain out-of-focus grey wall with nothing on it.
""")

R[33] = (242, 'D', 'cenital', 'dia', [], False, """
CENITAL — ONE OF ONLY THREE IN THIS PIECE. THE FIRST HALF OF THE MAJOR RHYME.

NADIR AERIAL VIEW. The camera is directly above the table with the lens pointing VERTICALLY DOWNWARD at exactly 90 degrees, like a copy-stand. THE TABLE IS PARALLEL TO THE IMAGE PLANE and fills the ENTIRE frame from edge to edge.

ABSOLUTELY NO WALL, NO WINDOW, NO CEILING, NO FLOOR, NO ROOM AND NO BACKGROUND IS VISIBLE. NO HEAD, NO FACE, NO HAND AND NO SHOULDER anywhere.

The surface is a wide MID GREY table. On it, FOUR separate things are laid out, well apart from one another, each squared to the frame, occupying most of the table between them: a thick block of sheets at the upper left, a wide open double page at the upper right, a small dark rectangle at the lower left, and a single sheet with several short grey bars on it at the lower right.

Nothing else on the table. The bare table shows between the four things but the frame is clearly OCCUPIED.

Even overhead light. No readable character anywhere, no numbers, no labels, no colour.

What the camera asserts by counting from directly overhead: this is what was established, and there are four of them.
""")

R[34] = (152, 'D', 'detalle', 'dia', [], False, """
Detail shot at table height of a single plain sheet lying by itself on the table, the camera level and close, the sheet at the left of the frame. NO FACE AND NO HEAD ANYWHERE.

The sheet carries a few short grey bars and, at its foot, ONE separate short mark set apart from the rest with blank paper around it.

The sheet has been PUSHED CLEARLY TO ONE SIDE: the rest of the table, running away to the right of the frame, is completely bare, and there is a wide empty gap between the sheet and everything else.

Window light from the left lays a band across the table and throws a thin shadow along the edge of the sheet.

No readable character anywhere, no numbers, no labels.

What the camera asserts by leaving it to one side with a gap: this one was signed, and it is being kept apart from what is being used.
""")

R[35] = (146, 'D', 'cenital', 'dia', [], False, """
CENITAL — ONE OF ONLY THREE IN THIS PIECE. THE SECOND HALF OF THE MAJOR RHYME.

NADIR AERIAL VIEW, from the SAME height, the SAME angle and the SAME framing as the other table: the camera directly above with the lens pointing VERTICALLY DOWNWARD at exactly 90 degrees. The SAME wide MID GREY table, parallel to the image plane, filling the ENTIRE frame.

ABSOLUTELY NO WALL, NO WINDOW, NO CEILING, NO ROOM AND NO BACKGROUND IS VISIBLE. NO HEAD, NO FACE, NO HAND AND NO SHOULDER anywhere.

On this table there are only TWO things, both small and both in the LOWER LEFT quarter of the frame, close together: one single sheet with a few short grey bars on it, and beside it a smaller slip with two short bars.

THE ENTIRE REST OF THE TABLE IS BARE. More than two thirds of the frame is empty table, unbroken, with nothing on it at all.

Even overhead light, the same as on the other table. No readable character anywhere, no numbers, no labels, no colour.

What the camera asserts by repeating the frame and the light exactly: the same table, the same practice, and this is what was established here.
""")

R[36] = (184, 'H', 'primer plano', 'dia', ['tomas'], True, """
CLOSE-UP of %(tomas)s, head and shoulders, facing the camera three-quarters on, seated.

His expression is plain ordinary attention with nothing performed: eyes level and directed past the lens, mouth closed, brow flat. He is NOT guilty, NOT relieved, NOT defiant, NOT anxious. He is a person who has been listening for a long time.

Window light from the left gives a clear lit side and a clear shadow side across his face. The background is a plain out-of-focus grey wall with nothing on it.
""")

R[37] = (183, 'H', 'general', 'contraluz', ['tomas'], True, """
Wide shot of the hearing room from the side, the camera at standing height and perfectly level, a long row of plain chairs running across the frame.

%(tomas)s sits ALONE on that row, SMALL in the frame and well off to one side, upright, hands resting on his knees, looking toward the far end of the room. Every other chair in the row is empty, and the empty chairs continue away from him to the edge of the frame.

Most of the picture is bare floor, bare wall and empty seating.

Window light from the right lays a bright band along the floor in front of the chairs and leaves the wall behind them in shade.

Nobody else anywhere in the room.

What the camera asserts by giving one person a whole row: almost nothing was established here, and the space around him is the size of it.
""")

# ───────────── K · EL ALEGATO ─────────────
R[38] = (99, 'K', 'medio', 'dia', ['fiscal'], False, """
Medium shot of %(fiscal)s standing to address the room at the end of the proceeding, the camera at her eye level and perfectly level, her centred.

She stands square, both hands resting on a closed grey folder held against the edge of the table in front of her, her head level and turned toward the far end of the room. Her mouth is closed between words.

Behind her, out of focus, the plain room.

Window light from one side gives a clearly lit side of her face and a clear shadow on the other.

No robe, no gown, no insignia, no badge, no text.

What the camera asserts: this is the part where what it all adds up to gets said out loud.
""")

R[39] = (253, 'K', 'detalle', 'dia', [], False, """
Detail shot at table height of FOUR plain grey folders laid out in a ROW across the table, the camera level and square to the row. NO PERSON, NO FACE AND NO HANDS ANYWHERE IN THIS PICTURE.

The four are IDENTICAL: the same size, the same thickness, the same tone, the same squared position, evenly spaced. Each lies slightly open so that the top sheet inside is visible, and the pattern of short grey bars on each of those four top sheets IS THE SAME PATTERN, repeated four times.

Nothing else on the table. Behind them, softly out of focus, the plain room.

Window light from the left lays one band across all four and throws four identical shadows.

No readable character anywhere, no numbers, no labels, no colour.

What the camera asserts by showing the same page four times: these are four copies of one thing, and they are being counted as four things.
""")

R[40] = (214, 'C', 'general', 'dia', [], False, """
Wide shot of the hearing room from the side, the camera at standing height and perfectly level, the same long row of plain chairs running across the frame.

THREE of the chairs are occupied by plain grey folders, one squared on each seat, evenly spaced. The FOURTH place in the row has NOTHING on it: bare seat, bare floor in front of it, nothing to mark it.

Nobody is in the room. No people anywhere.

Window light from the right lays a bright band along the floor and leaves the wall in shade. The empty seat is lit exactly like the other three.

No labels, no numbers, no names, no text.

What the camera asserts by leaving one seat bare in a row of four: a fourth is being asked for, and there is nothing there.
""")

R[41] = (195, 'B', 'detalle', 'hero', [], False, """
Detail shot at table height of two things lying SIDE BY SIDE on a plain table with a clear gap between them, the camera level and square. NO PERSON, NO FACE AND NO HANDS ANYWHERE.

At the left, a plain door key on a plain ring, lying flat. At the right, a small neat stack of plain unmarked notes, squared. Nothing else on the table.

Behind the table, softly out of focus, the plain wall of a room.

Window light from the left lights both evenly and throws a clean small shadow beside each.

No labels, no numbers, no denominations, no text, no logos.

What the camera asserts by setting two ordinary objects apart on a bare table: these are the two facts the argument rests on, and the picture puts them down without joining them.
""")

# ───────────── EL CIERRE ─────────────
R[42] = (131, 'J', 'medio', 'hero', ['andres'], False, """
Medium shot of %(andres)s at the work table at night, the camera at seated eye level and perfectly level, him at the right of the frame.

He is HALFWAY THROUGH separating a stack: he has lifted one group of sheets clear of the pile and is setting it down in a NEW place on the table, a clear gap away from the rest. The lifted group is still tilted, both hands under it. Two groups already sit separated on the table in front of him, each with bare table around it.

ONE desk lamp is the only light. It lifts his hands, his lowered face and the near part of the table out of the dark and leaves the room beyond in near-black.

Nobody else in the room. No text, no labels, no numbers.

What the camera asserts: the work the piece is asking for is this, one at a time, by hand.
""")

R[43] = (266, 'D', 'detalle', 'dia', [], False, """
THE CLOSING HALF OF THE RHYME. Detail shot across the evidence table of the hearing room, the camera AT TABLE HEIGHT and perfectly level, from the SAME position, the SAME distance and the SAME framing as the opening shot of the two trays.

The SAME two identical shallow mid grey trays sit side by side in the same places. What has changed is what is in them.

The LEFT tray is FULL: a thick stack of sheets and a folder with its tab standing up, heaped to above the rim.

The RIGHT tray holds only TWO plain sheets lying flat in the bottom of it, side by side, with the empty floor of the tray visible all around them.

The table around the trays is bare. Behind them, softly out of focus, the same plain benches and wall of the same room.

No hands, no people, no labels, no numbers, no text.

What the camera asserts by coming back to exactly the same frame: everything that was offered is on the left, everything that was admitted and practised is on the right, and the difference is the whole of the case.
""")

CARTONES = {1, 2, 6, 7, 11, 13, 15, 17, 19, 20, 22, 24, 25, 26, 31, 34, 39, 40, 41}
PROPUESTAS = {11, 19, 20, 24, 25, 31, 39, 40, 41}
# cuerpo si, cara no: el paso 11 prohibe una CARA, no una persona
SIN_ROSTRO = {13, 19}
RIMAS = [(1, 43), (33, 35), (27, 28)]


def comprobar():
    fallos = []
    tot = sum(v[0] for v in R.values())
    if len(R) != 43:
        fallos.append('hay %d ranuras, no 43' % len(R))
    if tot != 8307:
        fallos.append('suman %d cuadros, no 8307' % tot)
    for n in sorted(PROPUESTAS):
        if R[n][4] and n not in SIN_ROSTRO:
            fallos.append('r%02d es propuesta y muestra una cara: %s' % (n, R[n][4]))
    for n in sorted(SIN_ROSTRO):
        if 'NO FACE' not in R[n][6].upper():
            fallos.append('r%02d se declara sin rostro y el prompt no lo exige' % n)
    for n, v in sorted(R.items()):
        if v[2] == 'primer plano' and n in CARTONES:
            fallos.append('r%02d es primer plano y lleva carton' % n)
    cen = [n for n, v in sorted(R.items()) if v[2] == 'cenital']
    if len(cen) > 3:
        fallos.append('%d cenitales, el tope es 3: %s' % (len(cen), cen))
    seg = [n for n in sorted(R) if n + 1 in R and R[n][2] == 'cenital' and R[n + 1][2] == 'cenital']
    if seg:
        fallos.append('cenitales seguidos en %s' % seg)
    for a, b in RIMAS:
        if R[a][3] != R[b][3]:
            fallos.append('la rima r%02d/r%02d lleva dos registros de luz: %s y %s'
                          % (a, b, R[a][3], R[b][3]))
    return fallos, tot


if __name__ == '__main__':
    import collections
    f, tot = comprobar()
    print('%-5s %5s %-4s %-13s %-10s %-24s %s' % ('ran','cuad','esc','plano','luz','gente','carton'))
    for n, v in sorted(R.items()):
        print('r%02d  %5d %-4s %-13s %-10s %-24s %s'
              % (n, v[0], v[1], v[2], v[3], ','.join(v[4]) or '-',
                 ('PROPUESTA' if n in PROPUESTAS else 'si') if n in CARTONES else ''))
    print()
    print('escenas  ', dict(sorted(collections.Counter(v[1] for v in R.values()).items())))
    print('planos   ', dict(collections.Counter(v[2] for v in R.values())))
    print('luz      ', dict(collections.Counter(v[3] for v in R.values())))
    print('reparto  ', dict(collections.Counter(p for v in R.values() for p in v[4]).most_common()))
    print('con gente %d de %d' % (sum(1 for v in R.values() if v[4]), len(R)))
    print('%d cuadros' % tot)
    print()
    print('FALLOS:', f or 'NINGUNO')
