# -*- coding: utf-8 -*-
"""El repertorio del P3C5: una escena por ranura, disenada CONTRA la frase
medida que se oye encima de ella (P3C5_cruce.json), no contra el bloque.

LAS CINCO RIMAS, QUE SON EL ARGUMENTO
    r33 / r35   LA RIMA MAYOR. La misma mesa en cenital, la misma camara, la
                misma altura. Sobre r33 hay CUATRO cosas separadas que llenan
                el cuadro; sobre r35 hay DOS y una franja ancha de mesa
                desnuda. Es, literalmente, el resultado de la practica
                probatoria. Nadie lo comenta en locucion.
    r01 / r43   apertura y cierre. Dos bandejas vacias e iguales al abrir; las
                mismas dos al cerrar, con contenido y DESIGUALES.
    r21 / r22   la misma pantalla y la misma onda. En r21 Lucia esta al lado y
                la mira; en r22 la silla esta vacia. La diferencia entre una
                voz que alguien reconoce y una que no se ha establecido.
    r27 / r28   Lucia, encuadre identico. En r27 sostiene la anotacion y mira
                hacia abajo; en r28 tiene las manos vacias y mira afuera.
    r12 / r13   Andres. Lo que percibio y lo que recibio, en dos pares de
                manos.

LA BALANZA, HEREDADA DEL CASO 4
    Lo que si estaba sustentado se filma DENSO Y LLENO; lo que no, con aire
    vacio alrededor del unico dato que hay. El vacio es la falta. Por eso el
    cuaderno de r17 esta solo en medio de una mesa enorme, y por eso la mesa
    de Tomas en r35 tiene mas madera que papeles.

QUIEN TIENE CARA
    Ocho planos de cuarenta y tres: Oscar dos, Lucia tres, Renata uno, Tomas
    dos. Ningun funcionario, en ninguno. La tercera mujer del alegato NO se
    dibuja: en r40 hay un sitio vacio en la mesa y nada mas.

LAS CUATRO RANURAS A CABALLO
    13, 15, 27 y 43: la frase principal cubre menos de la mitad y la escena
    tiene que servir para las dos frases. Estan resueltas poniendo las dos
    cosas EN EL MISMO CUADRO, no eligiendo una.
"""

# nombre -> (ranura, cuadros, con_rostro, con_acento, que, escena)
E = {}

E['r01_dos_bandejas'] = (1, 167, False, False,
 'los dos momentos, todavia vacios', """
Overhead shot looking STRAIGHT DOWN at a wide DARK GREY table, the camera directly above and perfectly level, so the table fills the whole frame and no head, face or shoulder is visible anywhere.

Two identical shallow MID GREY document trays sit side by side in the middle of the table, the same size, the same distance from the camera, perfectly square with each other. BOTH ARE COMPLETELY EMPTY. The table around them is bare.

One bare forearm in a plain mid grey sleeve rests along the bottom edge of the frame, the hand open and palm down, not reaching for either tray.

What the camera asserts by standing directly overhead: these are two stages of one single thing, and nothing has been put in either of them yet.
""")

E['r02_lo_que_se_ofrece'] = (2, 300, False, False,
 'lo que se ofrece, antes de que nada se admita', """
Medium shot across a plain MID GREY table, the camera at table height and perfectly level.

A single hand in a plain mid grey sleeve enters from the left and HOLDS A CLOSED FOLDER OUT over the table, the folder still in the air, still gripped, not yet set down. The fingers are closed around its spine.

The far side of the table, where the folder would land, is COMPLETELY BARE: plain flat grey surface running to the edge of frame, nothing on it at all.

Behind the table a plain MID GREY wall, and further back a simple metal-framed window letting in flat even light.

What the camera asserts: the thing being offered is still in the hand, and the place where it would become something is empty.
""")

E['r03_oscar'] = (3, 230, True, 'band',
 'Oscar, de pie, sin hacer nada', """
Medium shot of OSCAR standing in the corridor of a modest lodging house, the camera at his eye level and perfectly level, him slightly off centre to the left.

OSCAR is %(oscar)s. He stands with his weight on both feet, ONE HAND LOOSELY AT HIS SIDE and the other resting flat against the corridor wall beside him. His head is turned slightly toward the camera's left, looking past it, not at it. His mouth is closed. His expression is plain ordinary attention: he is NOT menacing, NOT guilty, NOT pleading, NOT smiling.

He is not holding anything, not handing anything over, not taking anything. The corridor behind him runs away into a LIGHT doorway, with plain closed doors along one side.

What the camera asserts: this is the man the charge is about, and nothing he is doing in this frame is any part of it.
""")

E['r04_corredor'] = (4, 183, False, False,
 'el alojamiento, sin nadie', """
Wide shot straight down the corridor of a modest lodging house, the camera at standing eye level and perfectly level, the corridor running away from camera toward a LIGHT doorway at the far end.

Plain closed MID GREY doors line the left wall at regular intervals. The right wall is bare. The floor is plain flat grey.

NOBODY is in the frame. No figure, no silhouette, no shadow of a person.

What the camera asserts by standing in the middle of an empty corridor: the place is established, which is more than can be said for most of what is alleged to have happened in it.
""")

E['r05_tomas'] = (5, 199, True, 'band',
 'Tomas, quieto, y nada alrededor', """
Medium shot of TOMAS seated on a plain MID GREY chair against a plain MID GREY wall, the camera at his eye level and perfectly level, him centred.

TOMAS is %(tomas)s. He sits upright with BOTH HANDS RESTING ON HIS KNEES, palms down, completely still. His head faces forward, his eyes toward the camera's right, not at the lens. His mouth is closed. His expression is plain ordinary waiting: he is NOT defiant, NOT anxious, NOT evasive.

The frame around him is almost bare: the wall, the chair, a plain flat grey floor. THERE IS NO MAP, NO VEHICLE, NO BORDER, NO MONEY, NO TELEPHONE AND NO OTHER PERSON anywhere in the image.

What the camera asserts by giving him an empty room: everything attributed to this man is attributed, and the frame refuses to illustrate any of it.
""")

E['r06_tres_bloques'] = (6, 117, False, False,
 'los cargos, individualizados', """
Overhead shot looking STRAIGHT DOWN at a single plain LIGHT GREY sheet of paper lying on a DARK GREY table, the camera directly above and perfectly level, the sheet filling most of the frame.

The writing on the sheet is reduced to plain flat grey bars, arranged in THREE CLEARLY SEPARATE BLOCKS with generous empty paper between them. Each block is the same width. The separation between the blocks is obvious and deliberate.

No hand is in the frame.

What the camera asserts: these three things have been told apart from each other, which is the whole merit of the document.
""")

E['r07_el_sitio_vacio'] = (7, 189, False, False,
 'lo que no se acusa', """
Overhead shot looking STRAIGHT DOWN at the SAME plain LIGHT GREY sheet on the SAME dark grey table, the same camera height and the same framing as before.

The three separate blocks of grey bars sit in the upper half of the sheet. THE ENTIRE LOWER HALF OF THE SHEET IS BLANK PAPER, with nothing on it at all.

One hand in a plain mid grey sleeve rests flat on the table BESIDE the sheet, fingers together, not touching the paper and not pointing at anything.

What the camera asserts by leaving half the page empty: what is not written there is not part of this, and the hand beside it is not adding anything.
""")

E['r08_el_bloque_unico'] = (8, 137, False, False,
 'el informe con todos sus anexos, pedido como una sola cosa', """
Medium shot across a plain MID GREY counter, the camera at counter height and perfectly level.

A THICK SINGLE STACK of papers and folders sits on the counter, squared up into one solid block as tall as it is wide, with ONE PLAIN BAND running around the whole of it holding everything together. It reads as a single object, not as a set of things.

A hand in a plain mid grey sleeve is JUST LEAVING the top of the stack, the fingers already clear of it and still curved, the arm withdrawing toward the right edge of frame.

What the camera asserts: this was asked for as one thing, and one band is holding it that way.
""")

E['r09_los_anexos'] = (9, 246, False, False,
 'lo que hay dentro, todavia sin separar', """
Overhead shot looking STRAIGHT DOWN at the same thick stack, now lying open on a DARK GREY table, the camera directly above and perfectly level.

The stack is OPEN but still one pile: the different items inside are visible only as LAYERS of slightly different greys stepping down through the edge of the pile, overlapping, none of them pulled out, none of them set apart. Pages, a stiffer card, a flatter rectangle, all pressed together.

A hand in a plain mid grey sleeve rests at the edge of the table beside the pile, palm down, not separating anything.

What the camera asserts: the things are all there, and they are all still in the same place.
""")

E['r10_la_otra_copia'] = (10, 168, False, False,
 'la defensa tambien lo tiene, y a tiempo', """
Medium shot across a wide plain MID GREY table, the camera at table height and perfectly level, looking along the length of the table.

TWO IDENTICAL THICK STACKS of papers sit on the table, one on the near side and one on the far side, the same height and squared the same way. On each stack rests ONE HAND in a plain mid grey sleeve, palm down, flat, still.

Nothing is being passed between them. The two arms come in from opposite edges of the frame.

What the camera asserts by giving both sides the same pile: the handing over happened, and it happened in time. That part is not the problem.
""")

E['r11_la_banda'] = (11, 159, False, False,
 'el tratamiento unitario, de cerca', """
Tight close shot of the middle of the thick stack, the camera level and very close, so the stack fills the whole frame and the table is barely visible.

ONE PLAIN BAND runs around the entire bundle, pressing the layers together. At the edges of the band the different sheets and cards are squeezed into a single compressed mass; no individual item can be told from the one above or below it.

No hand is in the frame.

What the camera asserts by standing this close: from here it is one object, and nothing inside it has been given a job of its own.
""")

E['r12_la_pagina_mezclada'] = (12, 122, False, False,
 'el informe mezcla dos cosas', """
Overhead shot looking STRAIGHT DOWN at one plain LIGHT GREY page on a DARK GREY table, the camera directly above and perfectly level.

The writing is reduced to plain flat grey bars, and there are TWO VISIBLY DIFFERENT KINDS of bar on the page: one kind slightly darker and shorter, the other slightly lighter and longer. THE TWO KINDS RUN STRAIGHT INTO EACH OTHER with no gap, no rule, no heading and no indent between them, alternating down the page as if they were the same thing.

No hand is in the frame.

What the camera asserts: two different sorts of statement are sharing one page and nothing on the page tells them apart.
""")

E['r13_el_telefono_que_llega'] = (13, 197, False, False,
 'lo que vio y lo que le entregaron, en el mismo cuadro', """
Medium shot at chest height, the camera perfectly level, in the corridor of a modest lodging house.

In the FOREGROUND, filling the lower half of the frame, TWO PAIRS OF HANDS in plain mid grey sleeves: one pair is HOLDING OUT a plain dark rectangle the size of a telephone, and the other pair is RECEIVING it, fingers just closing around the edge. The handover is caught mid-way, the object supported by both pairs at once. No faces, no heads, no shoulders are visible: the frame is cut at the chest.

In the BACKGROUND, deeper and slightly out of focus, the corridor runs away to a LIGHT open doorway with a plain closed door beside it.

What the camera asserts by holding both in one frame: what he saw is back there, and what he was handed is here in the foreground, and they did not arrive the same way.
""")

E['r14_el_cuaderno_en_su_sitio'] = (14, 277, False, False,
 'donde estaba el cuaderno', """
Medium shot of a plain MID GREY shelf fixed to a wall in a back room of a lodging house, the camera at shelf height and perfectly level.

On the shelf, among a few ordinary objects, lies a CLOSED handwritten notebook with a soft cover and visibly worn corners. It is one object among several and nothing marks it out. The shelf and the wall are plain flat grey.

No hand is in the frame, and nobody is in the room.

What the camera asserts by showing it on a shelf among other things: this was found here, which is what is known about it so far.
""")

E['r15_la_pagina_del_cuaderno'] = (15, 113, False, False,
 'la columna, las cifras y las tres anotaciones', """
Overhead shot looking STRAIGHT DOWN at the notebook lying OPEN on a DARK GREY table, the camera directly above, perfectly level and close, so the two open pages fill the frame.

The handwriting is reduced to plain flat grey bars. The layout is clearly readable AS A LAYOUT: a left-hand COLUMN of short bars running down the page like a list of names, a narrower column of small bars beside it like dates, a column of still shorter bars like daily figures, and at the right margin THREE SEPARATE SHORT MARKS set apart from the rest, each on its own line.

No hand is in the frame.

What the camera asserts by standing straight above it: the shape of this page is the whole of what is known about it, and the shape is a ledger.
""")

E['r16_levantar_el_cuaderno'] = (16, 120, False, False,
 'se lo quiere introducir', """
Medium shot across a plain MID GREY table, the camera at table height and perfectly level.

One hand in a plain mid grey sleeve has LIFTED the open notebook clear of the table, holding it up at an angle, still gripped, the table surface visible beneath it. The gesture is of presenting something, not of reading it.

The table beyond is bare.

What the camera asserts: the thing is being put forward, and it is still only a thing being put forward.
""")

E['r17_el_cuaderno_solo'] = (17, 228, False, False,
 'la sustentacion, y el aire que le falta', """
Overhead shot looking STRAIGHT DOWN at a VERY WIDE DARK GREY table, the camera directly above and perfectly level, the table running past all four edges of the frame.

In the EXACT CENTRE of the frame, small, lies the closed notebook. IT IS THE ONLY OBJECT IN THE WHOLE IMAGE. Around it in every direction stretches bare flat grey table, and the empty area is many times larger than the notebook itself.

No hand is in the frame.

What the camera asserts by pulling this far back: this is everything that was offered in support, and the room around it is the size of what was not said.
""")

E['r18_la_linea_acordada'] = (18, 152, False, False,
 'lo que las partes acuerdan, que es una sola linea', """
Overhead shot looking STRAIGHT DOWN at a plain LIGHT GREY sheet on a DARK GREY table, the camera directly above and perfectly level.

Near the TOP of the sheet there is ONE SHORT LINE of plain flat grey bars, and nothing else on the paper at all. From the left and right edges of the frame, two hands in plain mid grey sleeves rest at the margins of the sheet, fingertips touching the paper, both still.

What the camera asserts: two sides have put their hands on one line, and the line is short.
""")

E['r19_la_pluma_suspendida'] = (19, 198, False, False,
 'lo que se le quiere anadir', """
Overhead shot looking STRAIGHT DOWN at the SAME sheet with the SAME single short line of bars at the top, the same camera height and the same framing as before.

A hand in a plain mid grey sleeve now holds a plain pen OVER THE LARGE BLANK AREA BELOW THAT LINE, the nib hovering a little above the paper, NOT TOUCHING IT. Nothing has been written in the blank area.

What the camera asserts by holding the nib off the page: what is being claimed is in the empty space under the agreement, and it has not been agreed.
""")

E['r20_el_rollo_sin_cortar'] = (20, 167, False, False,
 'seis meses, sin precisar nada', """
Medium shot across a plain MID GREY table, the camera at table height and perfectly level.

A CONTINUOUS PRINTED ROLL of paper lies across the table and SPILLS OVER THE NEAR EDGE, falling out of the bottom of the frame, with more of it visible further back still unrolled. It is one unbroken strip: the grey bars printed on it run end to end WITH NO DIVISION, no gap, no heading and no break anywhere along its length.

A hand in a plain mid grey sleeve rests on the table beside it, not holding it, not cutting it.

What the camera asserts by letting it run off the edge: this was asked for as one continuous thing, and nothing in it has been marked off from anything else.
""")

E['r21_la_onda_reconocida'] = (21, 194, True, 'band',
 'la grabacion que la interlocutora puede reconocer', """
Medium shot of a plain MID GREY monitor standing on a plain table, the camera at seated eye level and perfectly level, the screen turned toward the camera and filling the left half of the frame.

On the screen, a single AUDIO WAVEFORM runs horizontally across a plain flat background: a simple symmetrical band of peaks, no text, no numbers, no interface, no buttons.

Seated beside the monitor on the right, LUCIA is %(lucia)s. She is turned toward the screen, HEAD SLIGHTLY INCLINED, looking at the waveform. Her hands rest together in her lap. Her mouth is closed and her expression is plain ordinary recognition: she is NOT distressed, NOT frightened, NOT crying.

What the camera asserts by putting her in the same frame as the waveform: there is somebody here who can say what this is.
""")

E['r22_la_onda_sin_nadie'] = (22, 131, False, False,
 'la otra voz, que no se ha establecido', """
Medium shot of THE SAME plain mid grey monitor on THE SAME table, the camera at exactly the same height and the same framing as before, the screen turned toward the camera and filling the left half of the frame.

On the screen, an AUDIO WAVEFORM of the same kind runs horizontally across the plain flat background.

To the right of the monitor, where a person would sit, THE CHAIR IS EMPTY. Nobody is in the frame: no figure, no hand, no shoulder, no silhouette and no shadow of a person anywhere.

What the camera asserts by repeating the shot without the person: it is the same kind of thing on the screen, and this time there is nobody who can say whose it is.
""")

E['r23_renata_presente'] = (23, 241, True, 'band',
 'Renata, disponible y aceptando declarar', """
Medium shot of a plain MID GREY monitor standing on a plain table in an ordinary room, the camera at seated eye level and perfectly level, the screen turned toward the camera and filling most of the frame.

ON THE SCREEN, CLEARLY AND BRIGHTLY VISIBLE, is RENATA: %(renata)s. She is shown from the chest up, FACING FORWARD and looking toward the camera, her head upright, her mouth closed, her expression plain ordinary readiness: she is NOT distressed, NOT reluctant, NOT absent.

THE SCREEN IS FULLY LIT AND THE PICTURE ON IT IS SHARP AND COMPLETE: it is not dark, not blank, not frozen, not breaking up, not showing an error. There is no empty chair anywhere in the image.

What the camera asserts by giving her a clear picture on a working screen: she is reachable, she is here, and she has said she will answer questions.
""")

E['r24_la_carpeta_delante'] = (24, 203, False, False,
 'la entrevista en lugar de la persona', """
Medium shot of THE SAME monitor on THE SAME table, the camera at the same height and the same framing as before.

The monitor is now TURNED AWAY from the camera, showing its plain grey back and edge. Standing upright ON THE TABLE DIRECTLY IN FRONT OF IT, blocking where the screen was, is a CLOSED FOLDER, propped so that it faces the camera squarely.

A hand in a plain mid grey sleeve has just set the folder down, fingers still against its edge.

What the camera asserts by putting the document where the face was: the easier thing has been placed in front of the harder one.
""")

E['r25_los_dos_patrones'] = (25, 293, False, False,
 'dos relatos que coinciden, puestos a coincidir', """
Overhead shot looking STRAIGHT DOWN at a DARK GREY table, the camera directly above and perfectly level.

TWO separate plain LIGHT GREY pages lie side by side, squared up and the same distance apart from each other as from the frame edges. The writing on both is reduced to plain flat grey bars, and THE PATTERN OF BARS ON THE TWO PAGES IS VISIBLY THE SAME: the same lengths in the same order, line for line, so that the two pages read as a matched pair.

Two hands in plain mid grey sleeves rest at the outer edge of each page, as if they have just been aligned.

What the camera asserts by laying them out matched: the likeness between these two is being offered as if the likeness itself proved something.
""")

E['r26_los_flujos_sin_separar'] = (26, 296, False, False,
 'la grafica que no separa nada', """
Overhead shot looking STRAIGHT DOWN at a large plain LIGHT GREY sheet on a DARK GREY table, the camera directly above and perfectly level, the sheet filling the frame.

Printed on the sheet is a SIMPLE FLOW DIAGRAM: several plain circles at the outer edges, and ARROWS running inward from all of them into ONE circle at the centre. EVERY ARROW IS EXACTLY THE SAME WIDTH AND EXACTLY THE SAME SHADE OF GREY as every other, and they all enter the central circle in the same way. Nothing in the drawing distinguishes one arrow from another: no thickness, no tone, no dash, no label, no grouping.

No hand is in the frame.

What the camera asserts: everything here has been drawn as the same kind of movement, and the drawing is where that decision was made.
""")

E['r27_lucia_consulta'] = (27, 222, True, 'band',
 'consulta la anotacion, y entonces la recuerda', """
Medium shot of LUCIA seated on a plain chair against a plain MID GREY wall, the camera at her eye level and perfectly level, her body centred and squarely facing the camera.

LUCIA is %(lucia)s. She holds A SMALL SLIP OF PAPER IN BOTH HANDS, raised to chest height, and is LOOKING DOWN AT IT, her head inclined, her eyes on the paper. Her mouth is closed. Her expression is plain ordinary concentration: she is NOT upset, NOT uncertain, NOT ashamed.

The writing on the slip is reduced to plain flat grey bars. The wall behind her is bare.

What the camera asserts: she is looking at something that was handed over in time, and that is all she is doing.
""")

E['r28_lucia_sin_la_hoja'] = (28, 151, True, 'band',
 'la amenaza que ahora sostiene que no recibio', """
Medium shot of LUCIA seated on the SAME plain chair against the SAME plain mid grey wall, the camera at EXACTLY the same height and the same framing as before, her body centred and squarely facing the camera.

LUCIA is %(lucia)s. HER HANDS ARE NOW EMPTY AND OPEN, resting apart on her lap, palms upward. She is LOOKING UP AND AWAY past the camera's right shoulder, her head lifted. Her mouth is closed. Her expression is plain ordinary recollection: she is NOT lying, NOT evasive, NOT distressed, NOT defiant.

There is no paper anywhere in the image.

What the camera asserts by repeating the shot with nothing in her hands: the same person, the same seat, and this time nothing in front of her.
""")

E['r29_la_transcripcion_entera'] = (29, 284, False, False,
 'leer integra, como si fuera lo mismo', """
Medium shot across a plain MID GREY table, the camera at table height and perfectly level.

TWO hands in plain mid grey sleeves hold a LONG CONTINUOUS TRANSCRIPT open between them, unfolded wide so that it stretches from one edge of the frame to the other. The grey bars of text run unbroken across the whole length. THERE IS NOT A SINGLE MARK, UNDERLINE, TAB, BRACKET OR FOLD anywhere on it: nothing on the page has been picked out from anything else.

What the camera asserts by stretching it the full width: the whole of it is being handled as one move.
""")

E['r30_las_dos_cosas'] = (30, 134, False, False,
 'lo que la defensa quiere examinar', """
Overhead shot looking STRAIGHT DOWN at a DARK GREY table, the camera directly above and perfectly level.

TWO small separate objects lie on the table with clear bare space between them: on the left a single plain LIGHT GREY slip of paper with a few grey bars, on the right a small plain ledger card with a short column of grey bars. They are the same size and set at the same distance from the centre.

One hand in a plain mid grey sleeve rests between them, fingers open, touching neither.

What the camera asserts by separating them: these are two different questions, and the hand has not yet reached for either.
""")

E['r31_la_puerta_abierta'] = (31, 181, False, False,
 'la premisa que la pregunta da por cierta', """
Medium shot taken from INSIDE a plain room looking out through a DOORWAY into the corridor of a lodging house, the camera at standing eye level and perfectly level.

THE DOOR STANDS FULLY OPEN, swung back against the inner wall, and the corridor beyond is plainly visible and empty, running away to a LIGHT doorway at the far end. There is no lock, no bar, no chain and no obstacle anywhere in the frame. The floor runs unbroken from the room into the corridor.

NOBODY is in the image: no figure, no hand, no shadow of a person.

What the camera asserts by showing the way out standing open: this is the fact the question is built on, and the question treats it as the end of the matter.
""")

E['r32_oscar_sentado'] = (32, 243, True, 'band',
 'Oscar, al final de la practica probatoria', """
Medium shot of OSCAR seated on a plain MID GREY chair against a plain MID GREY wall, the camera at his eye level and perfectly level, him centred.

OSCAR is %(oscar)s. He sits with his hands LOOSELY FOLDED IN HIS LAP, shoulders square, completely still. His head faces forward and his eyes are toward the camera's left, not at the lens. His mouth is closed. His expression is plain ordinary attention: he is NOT defeated, NOT defiant, NOT remorseful.

The frame around him is bare: wall, chair, plain flat grey floor.

What the camera asserts by giving him the same stillness as before: nothing in his posture decides anything. What decides it is on the table in the next shot.
""")

E['r33_la_mesa_de_oscar'] = (33, 242, False, False,
 'lo que quedo establecido, LA RIMA MAYOR A', """
Overhead shot looking STRAIGHT DOWN at a wide DARK GREY table, the camera directly above, perfectly level, and at a clearly defined height so the table fills the frame edge to edge.

FOUR separate items are laid out across the table in a clear arrangement, evenly spaced and all square with the table edge: two plain LIGHT GREY document sheets, a small plain dark rectangle the size of a telephone, and a plain ledger card with a short column of grey bars. THE FOUR TOGETHER OCCUPY ALMOST THE WHOLE SURFACE: the bare table visible between and around them is narrow.

No hand is in the frame.

What the camera asserts by filling the table: four things stood up, and there is very little room left over.
""")

E['r34_el_acta_aparte'] = (34, 152, False, False,
 'el acta firmada, puesta a un lado', """
Overhead shot looking STRAIGHT DOWN at the edge of the same dark grey table, the camera directly above and perfectly level.

At the left edge of the frame, the corner of the arrangement of four items is just visible. SET WELL APART FROM THEM, alone on the right half of the frame with clear bare table between, lies ONE plain LIGHT GREY sheet carrying a short line of grey bars and, at its foot, a single small looping mark where a signature would be.

No hand is in the frame.

What the camera asserts by moving it out of the group: this one was kept, and it was kept out of the pile that did the work.
""")

E['r35_la_mesa_de_tomas'] = (35, 146, False, False,
 'lo que quedo probado, LA RIMA MAYOR B', """
Overhead shot looking STRAIGHT DOWN at THE SAME wide DARK GREY table, the camera directly above, perfectly level, and at EXACTLY THE SAME HEIGHT AND FRAMING as the shot of the four items, so the table again fills the frame edge to edge.

THIS TIME THERE ARE ONLY TWO ITEMS on the table: one plain ledger card with a short column of grey bars, and one small plain LIGHT GREY slip. They sit close together near one side, square with the table edge.

THE REST OF THE TABLE IS COMPLETELY BARE: a wide unbroken band of flat grey surface, far larger than the two items, running across the whole of the rest of the frame.

No hand is in the frame.

What the camera asserts by repeating the shot exactly: same table, same height, same light. Two things instead of four, and the difference is the empty part.
""")

E['r36_el_renglon_en_blanco'] = (36, 184, False, False,
 'los datos no identifican a nadie', """
Overhead shot looking STRAIGHT DOWN at the plain ledger card, the camera directly above, perfectly level and close, so the card fills most of the frame.

The card carries a short column of plain flat grey bars, evenly spaced, all of them the same. AT THE TOP OF THE COLUMN, WHERE A HEADING OR A NAME WOULD GO, THE LINE IS COMPLETELY BLANK: clean flat paper, clearly the place for something, and clearly empty.

No hand is in the frame.

What the camera asserts by framing the blank line dead centre: the figures are all there, and the one thing that would say whose they are is not.
""")

E['r37_la_mano_sobre_el_blanco'] = (37, 183, False, False,
 'y nadie lo llena', """
Overhead shot looking STRAIGHT DOWN at the SAME ledger card in the SAME framing, the camera directly above and perfectly level.

A hand in a plain mid grey sleeve is now HELD IN THE AIR OVER THE BLANK LINE, fingers slightly apart, palm down, NOT TOUCHING THE CARD and holding nothing. There is no pen in the hand. The blank line remains clean and empty beneath it.

What the camera asserts by suspending an empty hand over an empty line: there is nothing to put there.
""")

E['r38_tres_hojas'] = (38, 99, False, False,
 'el alegato sostiene tres cosas', """
Overhead shot looking STRAIGHT DOWN at a DARK GREY table, the camera directly above and perfectly level.

THREE plain LIGHT GREY sheets are being laid out in a row, evenly spaced, each carrying a few grey bars. Two are already flat on the table; THE THIRD IS STILL TILTED, held at its corner by a hand in a plain mid grey sleeve entering from the right, halfway through being set down.

What the camera asserts: three claims, being put on the table one after another.
""")

E['r39_cuatro_iguales'] = (39, 253, False, False,
 'cuatro informes, y el mismo patron en los cuatro', """
Overhead shot looking STRAIGHT DOWN at a DARK GREY table, the camera directly above and perfectly level.

FOUR separate folders are fanned out across the table, each lying open at its first page. THE PATTERN OF PLAIN GREY BARS ON ALL FOUR FIRST PAGES IS IDENTICAL: the same number of lines, the same lengths in the same order, line for line, so that the four pages are visibly copies of one another.

No hand is in the frame.

What the camera asserts by laying out four of the same thing: they can be counted to four, and they say one thing.
""")

E['r40_el_sitio_de_la_cuarta'] = (40, 214, False, False,
 'la tercera mujer: un sitio vacio y nada mas', """
Overhead shot looking STRAIGHT DOWN at the DARK GREY table, the camera directly above and perfectly level, the same framing as the row of three sheets.

The THREE plain LIGHT GREY sheets lie flat in their row, evenly spaced. To the right of the third sheet, where a FOURTH would continue the row, THERE IS ONLY BARE TABLE: a clean empty space exactly the size and shape of one sheet, with nothing in it.

NOTHING AND NOBODY occupies that space: no paper, no outline, no shadow, no silhouette, no figure, no chair, no mark of any kind.

What the camera asserts by leaving the place in the row empty: a fourth thing has been spoken of, and there is nothing there.
""")

E['r41_la_puerta_y_el_pago'] = (41, 195, False, False,
 'lo que la defensa dice que basta', """
Medium shot of a plain room, the camera at standing eye level and perfectly level.

TWO ordinary things share the frame with clear space between them. On the LEFT, a doorway with THE DOOR STANDING OPEN onto a plain corridor. On the RIGHT, on a plain MID GREY table, a SMALL LOW STACK OF NOTES, partly spread, as if some had been counted out and some not.

NOBODY is in the image: no figure, no hand, no shadow of a person.

What the camera asserts by giving the two equal room: here are the two facts being offered, side by side, and the frame adds nothing to either.
""")

E['r42_empezar_a_separar'] = (42, 131, False, False,
 'revisar, medio por medio', """
Overhead shot looking STRAIGHT DOWN at a DARK GREY table, the camera directly above and perfectly level.

A loose pile of plain LIGHT GREY sheets and folders lies in the middle of the table, and TWO hands in plain mid grey sleeves are HALFWAY THROUGH PULLING IT APART into two groups: a few items have already been drawn clear to the left, a few to the right, and the rest are still in the middle. One sheet is still held between finger and thumb, lifted slightly off the table, not yet placed on either side.

What the camera asserts by catching it half done: the sorting is the work, and it is being done one item at a time.
""")

E['r43_dos_bandejas_desiguales'] = (43, 266, False, False,
 'el cierre: las mismas dos bandejas, y lo que falta', """
Overhead shot looking STRAIGHT DOWN at THE SAME wide DARK GREY table with THE SAME two shallow MID GREY document trays, the camera directly above, perfectly level, and at EXACTLY THE SAME HEIGHT AND FRAMING as the opening shot.

THE TWO TRAYS ARE NO LONGER EQUAL. The left-hand tray holds a THICK squared stack of sheets that rises well above its rim. The right-hand tray holds TWO thin sheets lying flat, barely covering its floor, with the tray's grey bottom clearly visible around them.

One bare forearm in a plain mid grey sleeve rests along the bottom edge of the frame, the hand open and palm down, not reaching for either tray.

What the camera asserts by coming back to the first shot: the two began the same, and the difference between them now is the only thing this case decided.
""")


if __name__ == '__main__':
    import sys
    sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
    caras = [k for k, v in E.items() if v[2]]
    print('%d escenas' % len(E))
    print('con cara: %d  ->  %s' % (len(caras), ', '.join(sorted(caras))))
    n = sorted(v[0] for v in E.values())
    print('ranuras cubiertas: %d..%d  %s'
          % (n[0], n[-1], 'sin huecos' if n == list(range(1, len(n) + 1)) else 'HAY HUECOS'))
    print('cuadros: %d' % sum(v[1] for v in E.values()))
