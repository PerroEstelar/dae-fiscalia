# -*- coding: utf-8 -*-
"""El repertorio del P3C4: una escena por ranura, disenada CONTRA la frase
medida que se oye encima de ella (cruce_p3c4.json), no contra el bloque.

LAS DOS RIMAS DE LA PIEZA, QUE SON EL ARGUMENTO
    r01 / r39   las mismas seis carpetas, la misma camara cenital. Al abrir
                estan superpuestas y en desorden; al cerrar estan separadas y
                con pestana. Es literalmente lo que pide el cierre.
    r11 / r14   el MISMO escritorio y la MISMA camara. En r11 esta la orden
                judicial; en r14 no hay orden, solo una nota corta. El plano
                no dice que falta: se ve que falta.

LA BALANZA DE CADA ESCENA
    Seis escenas, y en cada una el guion narra primero lo sustentado. El
    repertorio lo sostiene con la ESCALA: lo sustentado se filma denso y
    lleno -el escrito de varias paginas, la orden completa, el episodio
    detallado-; lo que no, se filma con aire vacio alrededor del unico dato
    que hay. El vacio es la falta.

QUIEN TIENE CARA
    Seis planos de treinta y seis. Nora dos, Ivan dos, Lina uno, el
    recepcionista uno. Ningun operador juridico, en ninguno.

Y POR QUE NO SON TREINTA Y SEIS BODEGONES
    Porque casi todos llevan MANOS, y varios llevan dos manos que se oponen.
    La emocion va en las manos: es la regla del metodo y fue lo mejor del
    Caso 3.
"""

# nombre -> (ranura, cuadros, con_rostro, con_acento, que, escena)
E = {}

E['r01_seis_carpetas'] = (1, 240, False, False,
 'las seis actuaciones, todavia revueltas', """
Overhead shot looking STRAIGHT DOWN at a wide DARK GREY table, the camera directly above and perfectly level, so the table fills the whole frame and no head, face or shoulder is visible anywhere.

Six plain MID GREY document folders lie across the table in a rough left-to-right row, OVERLAPPING each other unevenly, none of them square with the table edge. One plain hand in a plain mid grey sleeve enters from the right edge and is HALFWAY THROUGH SETTING THE LAST ONE DOWN, the folder still tilted and not yet resting flat, the fingers still under its corner.

A second bare forearm in a plain mid grey sleeve rests across the far edge of the table, still, the hand open and palm down, not reaching for anything. No other object on the table.

What the camera asserts by standing directly overhead: these six things are stages of one single thing, and right now they are in no order at all.
""")

E['r02_nora_umbral'] = (2, 180, True, True,
 'Nora en el umbral, a medio girar', """
Medium shot of NORA, taken from OUTSIDE a plain room looking in through an open doorway, the camera at her eye level and perfectly level. The DARK GREY door frame runs down the left side of the frame close to camera and slightly out of focus, and frames her.

NORA is %(nora)s. She stands just inside the room with one hand STILL RESTING ON THE EDGE OF THE OPEN DOOR, her body already turned away toward the room and her head TURNED BACK over her shoulder, looking past the camera and not at it. Her other arm hangs at her side, the hand half closed. Her mouth is closed and her expression is plain ordinary attention: she is NOT alarmed, NOT defiant, NOT pleading.

The room behind her is a plain MID GREY wall and a LIGHT doorway further back. Nobody else is in the frame.

What the camera asserts by standing outside the door: we are being shown her from the threshold, which is as far as anything here has actually been established.
""")

E['r03_recepcion_vacia'] = (3, 150, False, False,
 'el mostrador del alojamiento, sin nadie', """
Medium shot taken from BEHIND the reception counter of a modest lodging house, the camera at the height of someone standing behind it, looking out across the counter into the empty hall.

The MID GREY counter top runs across the lower third of the frame close to camera, slightly out of focus. A plain ruled register book lies open on it, and one plain hand in a mid grey sleeve is LIFTING AWAY from the page, the fingers already clear of the paper and still curved.

Beyond the counter the hall is completely empty: a plain DARK GREY staircase going up at the right, a LIGHT doorway at the left, plain grey walls. No people anywhere beyond the single hand. No luggage, no furniture other than the stair and the counter.

What the camera asserts by standing behind the counter: this is the place from which arrivals are recorded, and nothing of what is alleged to happen here is visible from it.
""")

E['r04_tres_fuentes'] = (4, 146, False, False,
 'las tres fuentes, separadas', """
Overhead shot looking STRAIGHT DOWN at a MID GREY desk, the camera directly above and perfectly level. No head, face or shoulder anywhere.

THREE CLEARLY DIFFERENT THINGS lie on the desk, well apart from one another with bare desk between them: at the left a thick bound stack of ruled sheets; in the middle a plain DARK GREY phone lying face down; at the right a short strip of small plain paper stubs, fanned.

One plain hand in a mid grey sleeve is HALFWAY THROUGH PUSHING the strip of stubs into line with the other two, the stubs caught mid-slide under the fingertips. A second forearm in a plain mid grey sleeve enters from the opposite edge and lies flat and still beside the bound stack.

What the camera asserts by standing directly overhead: these are three different kinds of thing, and the picture does not join them.
""")

E['r05_ivan_telefono'] = (5, 244, True, True,
 'Ivan, la mano detenida antes de la puerta', """
Medium shot of IVAN taken from BEHIND AND SLIGHTLY ABOVE HIS LEFT SHOULDER, outdoors beside a plain passenger van, the camera at head height and perfectly level, so the camera sees what he sees and only the edge of his jaw and cheek.

IVAN is %(ivan)s. His left hand is RAISED to chest height holding a plain DARK GREY phone, and THE PHONE SCREEN IS A PLAIN LIGHT GREY RECTANGLE WITH ABSOLUTELY NOTHING ON IT: no window, no column, no bars, no icons, no cursor. His right hand is STOPPED HALFWAY toward the open side door of the van, fingers apart, not touching it.

The van's plain MID GREY flank fills the right of the frame, its open door a DARK rectangle. Behind, a flat LIGHT overcast sky and a low plain horizon. Nobody else anywhere in the frame.

What the camera asserts by standing behind his shoulder: we are looking at the trip from where he organises it, and nothing of what he is organising is visible.
""")

E['r07_seis_meses'] = (7, 285, False, False,
 'la solicitud, una casilla llena y el resto vacio', """
Overhead shot looking STRAIGHT DOWN at a MID GREY desk, close in, the camera directly above and perfectly level, so a single LIGHT GREY printed form fills most of the frame.

The form has ONE short field near the top FILLED with a plain flat grey bar, and every other field on the sheet is EMPTY: plain ruled boxes with nothing in them, taking up the whole lower two thirds of the sheet. One plain hand in a mid grey sleeve holds a plain dark pen, the nib STOPPED a few centimetres ABOVE the signature line at the foot of the page and clearly NOT TOUCHING IT.

In the DARK near corner of the frame, close to camera and clearly out of focus, the plain rounded edge of a shoulder in a mid grey sleeve, reduced to a simple soft shape. No face, no head.

What the camera asserts by standing directly overhead: this is an instrument being prepared, and we are being shown exactly how much of it has been filled in.
""")

E['r08_cuentas_de_mas'] = (8, 260, False, False,
 'la pila de extractos que se sale del cuadro', """
Overhead shot looking STRAIGHT DOWN at a MID GREY desk, the camera directly above and perfectly level. No head, face or shoulder.

A WIDE FAN OF IDENTICAL LIGHT GREY RULED SHEETS spreads across the desk and RUNS OFF THREE EDGES OF THE FRAME, far more sheets than the picture can hold, each one the same shape as the next. In the middle of the fan, one plain hand in a mid grey sleeve is STILL ADDING ANOTHER, the sheet caught mid-air just above the pile and not yet landed.

The small bare patch of DARK desk visible at one corner is the only part of the surface not covered. No other object.

What the camera asserts by standing directly overhead and framing tight: the pile is bigger than the frame, and that is the whole point.
""")

E['r09_fachada_vecina'] = (9, 162, False, False,
 'la fachada de enfrente, vista desde la acera', """
Medium wide shot of a plain closed house front, seen from ACROSS A NARROW STREET at the eye level of someone standing on the far pavement, the camera perfectly level.

The house front is a flat MID GREY wall with a plain closed DARK GREY door and two plain shuttered windows, all closed. In the DARK foreground, close to camera and out of focus, the near kerb and a short stretch of plain pavement run across the bottom of the frame: the viewer is clearly standing on the other side.

Completely empty: no people, no vehicles, no washing, no plants, nothing in any window. Flat overcast daylight, a LIGHT strip of plain sky above the roofline.

What the camera asserts by standing on the far pavement: this is everything that was seen, from here, and nothing else.
""")

E['r10_orden_en_blanco'] = (10, 234, False, False,
 'la orden de registro, con un solo renglon de motivos', """
Three-quarter angled close shot of a single LIGHT GREY printed sheet lying on a DARK GREY desk, the camera low and close so the sheet runs away from the viewer in perspective and fills most of the frame.

Near the top the sheet carries a short block of plain grey bars. Below it, under a plain ruled heading line, there is ONE SINGLE SHORT GREY BAR and then a LARGE COMPLETELY EMPTY AREA that takes up most of the sheet, down to the bottom edge. That emptiness is the subject of the picture.

One plain hand in a mid grey sleeve is WITHDRAWING from the sheet at the far edge, fingers still open and no longer touching it, already leaving the frame. No face, no head, no second hand.

What the camera asserts by sitting low and close: we are reading the reasons at the same height as the page, and there is almost nothing written there.
""")

E['r11_orden_vigente'] = (11, 152, False, False,
 'la orden judicial, completa', """
Three-quarter angled shot of a DARK GREY desk, the camera at desk height and perfectly level, the near edge of the desk running across the bottom of the frame close to camera and slightly out of focus.

A single LIGHT GREY document lies squarely in the lit centre of the desk, COMPLETELY FILLED: dense even rows of plain flat grey bars from the top margin to the foot, a plain rectangular block at the lower right where a seal would be, and a plain grey line above it. One plain hand in a mid grey sleeve is FLATTENING THE FOLD at the left edge with two fingers, the paper caught still slightly raised.

A plain MID GREY wall behind, simplified and out of focus. No face, no head.

What the camera asserts by sitting at desk height: this is a document being read, and everything that should be on it is on it.
""")

E['r12_hora_real'] = (12, 208, False, False,
 'la hora, escrita a mitad de trazo', """
Close shot from the SIDE and slightly BELOW of a plain clipboard held at waist height, the camera low and level so the board runs across the frame as a hard horizontal and the LIGHT ruled sheet on it fills the lit centre.

One plain hand in a mid grey sleeve holds a plain dark pen and is MID-STROKE writing into one ruled line, the nib touching the paper and the stroke clearly unfinished. The other hand steadies the board from underneath at the near edge. The written line is a plain flat grey mark, with no readable character.

High on the plain MID GREY wall behind, well out of focus and reduced to a simple soft shape, a plain round clock face with no numbers and no hands drawn in detail: only the circle.

What the camera asserts by standing at the height of the board: the record is being made here, now, while it happens.
""")

E['r13_recepcionista_llega'] = (13, 209, True, 'blue work shirt',
 'el recepcionista, entrando', """
Medium shot taken from INSIDE a plain lobby looking toward the entrance, the camera low at counter height and perfectly level.

THE RECEPCIONISTA is %(recepcionista)s. He is HALFWAY THROUGH PUSHING the plain DARK GREY entrance door inward WITH HIS SHOULDER, the door caught part way open and his body still leaning into it, his free hand carrying a plain grey shoulder bag that still swings slightly behind him. His head is TURNED INTO THE ROOM, looking past the camera, mouth closed, expression plain ordinary arrival: he is NOT startled, NOT furtive, NOT hurrying.

Behind him through the part-open door, a flat LIGHT rectangle of plain daylight. In the DARK near corner of the frame, close to camera and out of focus, the rounded end of the reception counter. Nobody else anywhere.

What the camera asserts by sitting low inside the room: we see him the way the room sees him, arriving, and that is all that is known about him here.
""")

E['r14_sin_orden'] = (14, 167, False, False,
 'el mismo escritorio, y no hay orden', """
Three-quarter angled shot of a DARK GREY desk, THE EXACT SAME DESK, THE EXACT SAME CAMERA POSITION, THE EXACT SAME HEIGHT AND THE EXACT SAME ANGLE as a previous shot of a document lying on it: the near edge runs across the bottom of the frame close to camera and slightly out of focus, and the plain MID GREY wall behind is simplified and out of focus.

THIS TIME THE CENTRE OF THE DESK IS BARE. There is no document in the lit centre, no seal block, no folded sheet: only clean empty desk surface where the document would be. Off to one side, well away from the centre, lies ONE SMALL TORN SCRAP of LIGHT GREY paper carrying two short plain grey bars and nothing else.

No hand anywhere in the frame. No face, no head, no object other than the scrap.

What the camera asserts by standing in exactly the same place and finding the centre empty: the thing that should be here is not here.
""")

E['r15_renglon_sin_fin'] = (15, 167, False, False,
 'el renglon que no termina', """
Very close overhead shot looking STRAIGHT DOWN at a single LIGHT GREY ruled page on a DARK GREY desk, the camera directly above and perfectly level, the page filling almost the whole frame.

ONE SINGLE CONTINUOUS GREY BAR of text runs from the left margin ALL THE WAY to the right edge of the sheet WITHOUT ANY BREAK, wraps, and continues across the next line, and the next, and then STOPS IN THE MIDDLE OF A LINE with no full stop and no mark of any kind after it. THE ENTIRE REST OF THE PAGE BELOW IT IS COMPLETELY BLANK.

One plain hand in a mid grey sleeve enters from the lower edge and ONE FINGERTIP RESTS at the very beginning of the first line, not moving along it. No face, no head, no second hand.

What the camera asserts by standing directly over the page: a single reason, written as something that simply keeps going, is holding up this whole sheet.
""")

E['r16_escrito_denso'] = (16, 272, False, False,
 'el escrito de varias paginas, lleno', """
Overhead shot looking STRAIGHT DOWN at a MID GREY desk, the camera directly above and perfectly level.

SEVERAL LIGHT GREY PAGES are fanned across the desk so that four or five of them are visible at once, overlapping like a hand of cards, and EVERY ONE OF THEM IS DENSELY FILLED edge to edge with even rows of plain flat grey bars, with narrow margins and small grey tick marks down the side of each page. The density is uniform and continues onto every visible sheet.

TWO plain hands in mid grey sleeves, entering from opposite edges, are SQUARING THE STACK: each one pressing a corner inward, the pages caught still slightly out of alignment. A third forearm in a plain mid grey sleeve rests across the far edge of the desk, still.

No face, no head, no shoulder.

What the camera asserts by standing directly overhead over a full desk: this one was worked through, and the picture can show how much of it there is.
""")

E['r17_condiciones'] = (17, 257, False, False,
 'la lista corta de condiciones, con aire', """
Close overhead shot looking STRAIGHT DOWN at a single LIGHT GREY page on a MID GREY desk, the camera directly above and perfectly level.

The page carries FOUR SHORT SEPARATE BLOCKS of plain flat grey bars, one under another, each only two lines long, with A WIDE BAND OF CLEAN EMPTY PAPER between each block and the next. The blocks are evenly spaced and clearly distinct from one another: it reads as four separate things, not as a paragraph.

One plain hand in a mid grey sleeve enters from the right edge and ONE FINGERTIP RESTS ON THE PAPER beside the third block, in the empty margin and not on the text. No face, no head.

What the camera asserts by standing over a page with this much air in it: each of these was meant to be read on its own.
""")

E['r18_dos_casillas'] = (18, 102, False, False,
 'las dos casillas que quedaron vacias', """
EXTREME close shot looking STRAIGHT DOWN at a small part of a LIGHT GREY printed form on a DARK GREY desk, the camera directly above and perfectly level, so that only a narrow strip of the sheet fills the entire frame.

Across that strip run several plain square checkboxes in a row. All of them to the left are FILLED with a solid grey mark. THE LAST TWO, side by side at the right of the frame, ARE COMPLETELY EMPTY: clean white-grey squares with nothing inside them, and they are the largest clear shapes in the picture.

A plain dark pen cap lies on the paper BESIDE the two empty boxes, not above them and not touching them. No hand, no face, no head.

What the camera asserts by coming this close: these two were reached, and left as they are.
""")

E['r19_nora_escucha'] = (19, 152, True, True,
 'Nora sentada, escuchando', """
Medium shot of NORA seated at a plain MID GREY table, taken from the SIDE at seated eye level, the camera perfectly level, so she is seen in profile and the table runs across the lower third of the frame.

NORA is %(nora)s. She sits still with both forearms resting on the table, HER HANDS LOOSELY CLASPED, one thumb CAUGHT HALFWAY THROUGH MOVING OVER THE OTHER. Her head is slightly lowered and TURNED AWAY from camera toward the far end of the room, which is out of frame. Her mouth is closed and her expression is plain concentrated listening: she is NOT distressed, NOT defiant, NOT pleading.

An empty plain grey chair stands beside her at the same table, turned slightly away. The wall behind is a flat MID GREY plane, with a LIGHT doorway further back. Nobody else in the frame.

What the camera asserts by sitting beside her at her own height: she is in the room while this is argued, and she is not the one speaking.
""")

E['r20_estrado_vacio'] = (20, 237, False, False,
 'el estrado, desde donde se esta de pie', """
Wide shot of a plain raised bench at the end of a hearing room, taken from THE FLOOR OF THE ROOM at the height of someone STANDING in front of it, the camera tilted very slightly up but kept level in framing, no dutch angle.

The bench is a plain DARK GREY raised desk on a plain MID GREY platform one step up, running across the upper middle of the frame, and IT IS COMPLETELY EMPTY: no person, no chair occupied, no papers, no microphone, nothing on its surface. Behind it a flat MID GREY wall with a LIGHT panel of plain daylight at one side.

In the DARK foreground, close to camera and out of focus, the plain top edge of a lectern runs across the bottom of the frame. Nobody anywhere in the picture.

What the camera asserts by standing on the floor and looking up at an empty bench: this is the position the decision came from, and the room it came into.
""")

E['r21_microfono_apartado'] = (21, 131, False, False,
 'el microfono apartado, y el atril vacio', """
Close shot at lectern height of a plain MID GREY lectern top, the camera level and square to it, so the lectern surface runs across the frame.

A plain DARK GREY desk microphone stands on the lectern, ITS HEAD TURNED AWAY from the frame and tipped down toward the surface, pointing at nothing. THE REST OF THE LECTERN IS COMPLETELY BARE: no paper, no notes, no water, no hand.

Behind, the room falls away into a plain MID GREY wall, simplified and well out of focus, with one LIGHT vertical band of daylight. No people anywhere.

What the camera asserts by standing square to an empty lectern: there was a place to say it from, and nothing was said from it.
""")

E['r22_ivan_sentado'] = (22, 215, True, True,
 'Ivan sentado, mirando al estrado', """
Medium shot of IVAN seated at a plain MID GREY table, taken from THREE-QUARTERS BEHIND AND SLIGHTLY TO THE SIDE at shoulder height, the camera perfectly level, so the back of his shoulder and the line of his jaw occupy the near part of the frame and his face is seen only in partial profile.

IVAN is %(ivan)s. Both forearms rest on the table with HIS HANDS LOOSELY CLASPED, one thumb CAUGHT MID-WAY through moving over the other. His head is TURNED AWAY from camera toward the far end of the room, which is out of frame. His back is straight and his shoulders are level: he is NOT slumped, NOT leaning forward, NOT tense.

A plain closed grey folder lies on the table beyond his hands, untouched. The room ahead of him is a flat MID GREY plane with a LIGHT panel of daylight. Nobody else in the frame.

What the camera asserts by sitting behind his shoulder: we are watching with him, toward the place where this is going to be decided.
""")

E['r23_sobre_nuevo'] = (23, 300, False, False,
 'el sobre que llega y no encaja', """
Overhead shot looking STRAIGHT DOWN at a MID GREY table, the camera directly above and perfectly level.

Across the table lie SEVERAL LIGHT GREY DOCUMENTS, all of them SQUARED NEATLY with the table edge and with each other, in a tidy block. One plain hand in a mid grey sleeve is SETTING DOWN, at the very edge of that block, A SINGLE PLAIN SEALED ENVELOPE that sits CLEARLY ASKEW, out of line with everything else, still under the fingertips and not yet released.

The envelope is plain, closed, with a flat grey rectangle where a label would be and nothing readable on it. No face, no head, no second hand.

What the camera asserts by standing over the tidy block: something has just arrived that does not line up with what was already here.
""")

E['r24_dos_peticiones'] = (24, 294, False, False,
 'las dos peticiones, y la mano que sostiene una', """
Overhead shot looking STRAIGHT DOWN at a MID GREY table, the camera directly above and perfectly level.

TWO plain LIGHT GREY documents lie on the table. THE FIRST sits squarely in the lit centre of the frame, straight and flat. THE SECOND has been PUSHED TO THE FAR EDGE and hangs HALF OFF THE TABLE, tilted, about to fall.

One plain hand in a mid grey sleeve rests FLAT AND FIRM on top of the first document, fingers spread, holding it where it is. A SECOND hand, in a plain mid grey sleeve, enters from the opposite edge and is REACHING for the second document but is STOPPED SHORT, fingers open and clearly NOT TOUCHING IT, with a visible gap of bare table between the fingertips and the paper.

No faces, no heads, no shoulders: only the two forearms entering from opposite sides.

What the camera asserts by standing directly overhead between them: one of these is being held in place and the other is being kept out of reach, and both of those are being done by a hand.
""")

E['r25_lina_de_pie'] = (25, 206, True, 'yellow belt',
 'Lina, que acaba de ponerse de pie', """
Medium shot of LINA taken from THE SIDE at standing eye level, the camera perfectly level, in a plain hearing room.

LINA is %(lina)s. She has JUST STOOD UP from a plain grey chair: the chair is still visible behind her knees, and ONE HEEL IS STILL LIFTING clear of the floor while the other foot is already flat. Her arms hang at her sides, both hands open and relaxed. Her head is TURNED AWAY from camera toward the far end of the room, which is out of frame. Her mouth is closed and her expression is plain ordinary attention: she is NOT frightened, NOT defiant, NOT resigned.

The wall behind is a flat MID GREY plane with a LIGHT panel of daylight at one side. A plain empty table runs in front of her, bare. NOBODY ELSE ANYWHERE IN THE FRAME: she is alone in the picture.

What the camera asserts by standing beside her at her own height: she is being addressed, and we are at the height of someone who is simply present.
""")

E['r26_una_sola_linea'] = (26, 232, False, False,
 'la pagina con una sola frase', """
Very close overhead shot looking STRAIGHT DOWN at a single LIGHT GREY sheet on a DARK GREY desk, the camera directly above and perfectly level, the sheet filling the frame from edge to edge.

Near the TOP of the sheet there is ONE SHORT PARAGRAPH, three plain flat grey bars long, and nothing else. THE WHOLE REST OF THE SHEET IS COMPLETELY BLANK: clean empty paper filling at least three quarters of the frame, with no ruling, no heading, no mark of any kind.

No hand, no pen, no face, no head, no second object: only the sheet and the desk edge at one corner.

What the camera asserts by framing the page this tight and finding it this empty: everything that was said fits in the top of the picture.
""")

E['r27_sello_sobre_la_hoja'] = (27, 289, False, False,
 'el sello sobre la hoja casi vacia', """
Close three-quarter angled shot at desk height of the SAME nearly blank LIGHT GREY sheet lying on a DARK GREY desk, the camera low and level so the sheet runs away in perspective and its wide empty lower half is clearly visible.

A plain DARK GREY stamp block has just been PRESSED ONTO THE FOOT of the sheet and one plain hand in a mid grey sleeve is STILL ON IT, the fingers closed around the handle and the block still flat on the paper. The mark under it is a plain flat grey rectangle with nothing readable in it.

Above the stamp, the sheet is empty all the way up to a single short paragraph at its top edge, at the far end of the frame. No face, no head, no second hand.

What the camera asserts by sitting low enough to see the whole sheet at once: the formal act is complete, and there is nothing between it and the top of the page.
""")

E['r28_dos_entradas'] = (28, 285, False, False,
 'las dos entradas en el indice', """
Close overhead shot looking STRAIGHT DOWN at a plain LIGHT GREY ruled index page on a MID GREY desk, the camera directly above and perfectly level.

The page is ruled into many empty rows. ONLY TWO OF THEM CARRY ANYTHING: two entries one under the other, each a short plain flat grey block in the left column and a single short grey bar in the right column. EVERY OTHER ROW ON THE PAGE IS EMPTY.

One plain hand in a mid grey sleeve enters from the lower edge and ONE FINGERTIP IS STOPPED in the left margin BESIDE THE FIRST of the two entries, resting on the paper and not on the entry itself. No face, no head, no second hand.

What the camera asserts by standing over a nearly empty index: here are two, named, on a page where everything else is still blank.
""")

E['r29_silla_de_la_defensa'] = (29, 118, False, False,
 'la silla de la defensa, vacia', """
Medium shot of a single plain grey chair at a plain MID GREY table, taken SQUARE ON from the far side of the room at seated eye level, the camera perfectly level.

THE CHAIR IS EMPTY and pushed slightly back from the table, turned a few degrees out of square. The stretch of table in front of it is COMPLETELY BARE: no paper, no folder, no pen, nothing.

Behind, a flat MID GREY wall, simplified. NO PEOPLE ANYWHERE IN THE PICTURE, no hands, no shoulders, no figure in the background.

What the camera asserts by standing opposite an empty chair at the height someone would sit in it: nothing was said from here, and that is being treated as an answer.
""")

E['r30_episodio_detallado'] = (30, 285, False, False,
 'el episodio descrito, y los cuatro renglones', """
Overhead shot looking STRAIGHT DOWN at a single LIGHT GREY page on a MID GREY desk, the camera directly above and perfectly level, the page filling most of the frame.

The upper half of the page carries ONE DENSE COMPLETE PARAGRAPH of plain flat grey bars, filling its block edge to edge with no gaps. Below it, under a short plain heading bar, FOUR SHORT SEPARATE ENTRIES are listed one under another, each a single grey bar of the same length, evenly spaced.

TWO plain hands in mid grey sleeves rest FLAT on the desk on either side of the page, fingers spread, holding it square. No face, no head, no shoulder.

What the camera asserts by standing over a page that is this complete: everything the picture can show about this one is on it.
""")

E['r31_tres_marcas'] = (31, 113, False, False,
 'las tres marcas al margen', """
EXTREME close shot looking STRAIGHT DOWN at the outer margin of a LIGHT GREY page, the camera directly above and perfectly level, so only a narrow vertical strip of paper and the DARK desk beside it fill the frame.

THREE small identical plain grey tick marks sit in the margin, evenly spaced one under another, each beside the start of a line of plain grey text that runs off the edge of the frame. A plain dark pen tip is STOPPED just beside the third mark, a visible gap of clean paper between the nib and the paper.

No hand beyond the pen, no face, no head.

What the camera asserts by coming this close to the margin: three separate things were checked, one at a time.
""")

E['r32_dos_pasajes_nuevos'] = (32, 161, False, False,
 'los dos pasajes de junio, encima de la carpeta', """
Close three-quarter angled shot at desk height of a plain closed MID GREY folder lying on a DARK GREY desk, the camera low and level so the folder runs away in perspective.

ON TOP of the closed folder, clearly separate from it and not inside it, lie TWO small plain LIGHT GREY travel stubs, side by side and crisp-edged, visibly newer and cleaner than the worn folder beneath them. One plain hand in a mid grey sleeve PINS THEM DOWN with two fingertips at one corner, the rest of the hand clear of them.

Nothing else on the desk. No face, no head.

What the camera asserts by sitting at the height of the folder: these two came from somewhere else and are being laid on top of what was already closed.
""")

E['r33_direccion_corregida'] = (33, 189, False, False,
 'la direccion tachada y escrita encima', """
EXTREME close shot looking STRAIGHT DOWN at ONE SINGLE LINE of a LIGHT GREY page, the camera directly above and perfectly level, so that one line and the two lines above and below it fill the entire frame.

The middle line has a SHORT HORIZONTAL STRIKE-THROUGH across part of it, and ABOVE that struck part, in the space between the lines, a SHORT CORRECTION has been written: a small plain flat grey bar. EVERY OTHER LINE VISIBLE IN THE FRAME IS COMPLETELY UNTOUCHED, clean and unmarked.

No hand, no pen, no face, no head: only the paper.

What the camera asserts by coming close enough to see only this: exactly one thing on this page was changed, and the picture shows how much of it.
""")

E['r34_pantalla_mensajeria'] = (34, 241, False, False,
 'el telefono sobre la mesa, con la luz en la mesa', """
Close shot from the SIDE at table height of a plain DARK GREY phone lying FACE UP AND FLAT on a MID GREY table, the camera low and exactly level with the table top so the surface runs across the frame as one hard horizontal edge.

The screen shows a LONG CONTINUOUS COLUMN of faint illegible grey message bars of different lengths, running from the top of the screen to the bottom without a break, reduced to plain flat grey blocks with no readable character and no icon anywhere.

The pale light of the screen falls FORWARD ONTO THE TABLE SURFACE around the phone as a soft low pool that stays ATTACHED TO THE TABLE. IT MUST NOT APPEAR AS A FREE-FLOATING BRIGHT RECTANGLE hanging in the air or on a wall.

One plain hand in a mid grey sleeve rests STILL on the table beside the phone, NOT TOUCHING IT, with a clear gap of table between them. No face, no head.

What the camera asserts by lying at the height of the table: the whole thread is here, flat, and nobody has picked it up.
""")

E['r35_tres_hojas_aplanadas'] = (35, 109, False, False,
 'las tres hojas aplanadas en una sola pila', """
Close overhead shot looking STRAIGHT DOWN at a MID GREY desk, the camera directly above and perfectly level.

THREE LIGHT GREY SHEETS have been squared into ONE SINGLE FLUSH STACK, their edges perfectly aligned so that from above they read as a single sheet with two thin shadow lines. One plain hand in a mid grey sleeve PRESSES DOWN FLAT on the top sheet, fingers spread, pushing the stack flatter.

A SECOND hand, in a plain mid grey sleeve, enters from the opposite edge and lies OPEN AND STILL on the bare desk beside the stack, palm up, clearly not helping and not reaching.

No faces, no heads, no shoulders.

What the camera asserts by standing directly over the stack: three things have been pressed into looking like one.
""")

E['r37_carpeta_sin_indice'] = (37, 145, False, False,
 'la carpeta unica, rebosada y sin separadores', """
Close shot from the SIDE at table height of a single thick MID GREY folder lying on a DARK GREY table, the camera low and exactly level with the table so the FOLDER'S THICKNESS reads as a tall stack across the frame.

The folder is OVERFULL and its contents stick out unevenly at the open edge: visibly DIFFERENT KINDS of thing jammed together with NO DIVIDERS AND NO TABS ANYWHERE — plain ruled sheets, one thicker card-shaped rectangle, a narrow printed strip, a folded sheet — all pressed into one block, some sticking out further than the folder cover.

One plain hand in a mid grey sleeve rests on top of the folder, pressing it closed, fingers spread. No face, no head.

What the camera asserts by lying at the height of the stack: everything is in here together, and from the outside there is no way to tell one kind from another.
""")

E['r39_seis_carpetas_separadas'] = (39, 163, False, False,
 'las mismas seis carpetas, ya separadas', """
Overhead shot looking STRAIGHT DOWN at a wide DARK GREY table, THE EXACT SAME TABLE, THE EXACT SAME CAMERA POSITION AND THE EXACT SAME HEIGHT as a previous overhead shot of six folders: the table fills the whole frame and no head, face or shoulder is visible anywhere.

THE SAME SIX plain MID GREY document folders lie across the table in a left-to-right row, but NOW THEY ARE SQUARE WITH THE TABLE EDGE AND WITH EACH OTHER, EVENLY SPACED, WITH A CLEAN BAND OF BARE TABLE BETWEEN EACH ONE AND THE NEXT, and NONE OF THEM OVERLAPS. Each folder carries ONE plain small tab standing proud of its upper edge, all six tabs at different heights along the row.

NO HAND ANYWHERE IN THE FRAME. Nothing else on the table.

What the camera asserts by standing in exactly the same place and finding them apart: these are still six stages of one thing, and now each one can be taken out on its own.
""")
