# -*- coding: utf-8 -*-
"""Las placas del PRIORIDAD 03 Caso 3 (Ruta del Golfo), con el prompt literal,
la semilla y el identificador de Magnific de cada una.

ESTE ARCHIVO SE REHIZO EL 21 DE OCTUBRE, DESPUES DE LA REVISION
    La primera version registraba las 28 placas del montaje inicial. De esas,
    diecinueve salieron de la linea: Sebastian marco que la pieza mostraba
    "puros cuadros vacios" y tenia razon, porque 21 de las 28 eran entorno sin
    nadie. Entraron dieciocho placas nuevas -dieciseis de repertorio y dos
    camas-. PLACAS es ahora lo que esta en la linea; DESCARTADAS es lo que
    salio, con el motivo, porque el prompt de una placa descartada sigue
    sirviendo de referencia.

COMO SE AMARRO CADA PROMPT A SU ARCHIVO
    Por medicion, nunca por memoria ni por nombre de archivo. Se baja la vista
    previa de 1024 px de cada creacion, se reduce a 64x36 en gris normalizado y
    se compara contra el PNG crudo. Las 22 candidatas dieron distancia 0.0000
    a 0.0003 con un unico ganador; el segundo lugar mas cercano quedo en
    0.2763, y eso fue entre las dos versiones de la MISMA placa. La version
    que quedo en 01 PLANOS se resolvio aparte, por md5. Esta en
    `_tmp/p3c3/rev/casar.py`.

    Dos trampas, las dos pagadas ya:
    - La miniatura de Magnific es un recorte CUADRADO de 400x400 de un cuadro
      16:9. Emparejar contra ella dio tres parejas falsas. Se usa la vista
      previa, y contra el crudo, nunca contra la placa graduada.
    - El borrador local del prompt NO es lo que se envio. Comparadas las seis
      del primer lote contra el historial: las dos con rostro coinciden al
      caracter, y las cuatro sin rostro traen en el borrador una frase de mas
      -"Figures are 8 to 8.5 heads tall"- que no se mando. El historial manda.

EL METODO QUE PRODUJO LAS NUEVAS, Y QUE HAY QUE REPETIR EN LOS CASOS 4 Y 5
    Es el metodo de prompts hero de CLAUDE.md, aplicado de verdad: la posicion
    de la camara es el argumento, el gesto unico antes que la cara, la emocion
    va en las manos, media accion y nunca el pico -congelado, no borroso-, y
    el negativo escrito contra los fracasos de ESE plano.

    Donde el caso no permite caras -el equipo, los funcionarios, por la regla
    SRPA de "sin personal identificable"- la accion va en las MANOS. No es un
    rodeo a la regla: es el plano canonico del metodo, y la regla empuja hacia
    el. Tres de las placas nuevas son manos sin cara y son las mejores de la
    tanda.

MODELO
    seedream-5-pro, 2560x1440, resolucion 2k, 100 creditos por placa.

LAS TRES REGLAS QUE ESTE CASO DEJO, Y UNA CUARTA
    1. El tono plano. El modelo INVENTA textura en cualquier superficie grande
       y vacia, y la clausula tiene que nombrar TODAS las superficies grandes,
       no solo la que fallo la vez pasada. El tinte perdona el grano, no un
       patron.
    2. El acento. El tono no separa el acento de la piel; la saturacion si.
       Ver acentos.py.
    3. La piel. Decir "grey" no basta, hay que dar el numero. Esta en
       CLAUSULAS['piel'] y va en toda placa con figura.
    4. Un color que tiene que destacar se pide como UNICO. La banda amarilla
       de Omar salia generada a 0.34 de saturacion, por debajo del piso de
       0.45 de grade_placas, y `forzar` no mueve el tope. Se arregla en el
       prompt: "THAT YELLOW BAND IS THE ONLY SATURATED COLOUR ANYWHERE IN THE
       WHOLE IMAGE".

LAS TRES RANURAS QUE NO SON PLACA
    r03, r22 y r28 son las graficas de motion de graficas_p3c3.py.

LO QUE NO SE ILUSTRA
    Ninguna placa muestra un encuentro, una retencion, una agresion ni una
    amenaza en acto, y ningun viajero esta individualizado. kf12, que era la
    unica que rompia esa regla, salio de la linea.
"""


CLAUSULAS = {'piel': 'Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20. It must read as grey with a faint warm tint, never as brown and never as a saturated skin colour.',
    'tonos': 'The frame must have three clearly separate tonal zones: deep dark, mid grey and light. No large area of near-black and no large area of near-white anywhere.',
    'planos': 'EVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not plaster texture, not wallpaper, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.',
    'limpia': 'Clean plate: no legible text, no lettering, no numbers, no signage, no labels, no logos, no emblem.',
    'negativo': 'Not a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.'}

MODELO = {'mode': 'seedream-5-pro', 'width': 2560, 'height': 1440,
          'resolution': '2k', 'creditos': 100}

# las tres ranuras que no son placa, de graficas_p3c3.py
GRAFICAS = {'r03': 168, 'r22': 358, 'r28': 377}

# nombre -> ranura, cuadros horneados, que es, personaje, id, semilla, prompt
PLACAS = {
    'cama_calle_medellin': {
        'ranura': 'r01',
        'cuadros': 202,
        'que': 'la calle de Medellin al amanecer',
        'personaje': '',
        'id': '9ZmpYjgNYZ',
        'semilla': 371830,
        'prompt': 'Wide establishing shot of an ordinary street on the edge of Medellín at first light, seen straight on. Modest low rendered buildings with plain frames and plain doors, a narrow pavement, a kerb, hills faintly visible behind. Overcast, flat even light. The street is empty: no people, no vehicles. Ordinary and unremarkable, not sinister, not derelict. No window bars, no grilles, no padlocks.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'r02_terminal_viajeros': {
        'ranura': 'r02',
        'cuadros': 243,
        'que': 'la terminal, un viajero cruzando el vestibulo hacia la van',
        'personaje': '',
        'id': '8awSaEhIrU',
        'semilla': 124647,
        'prompt': 'Wide shot across the concourse of an intercity bus terminal, the camera standing on the concourse at the eye level of someone walking through it. In the middle distance, at the kerb, a plain passenger van waits with its doors closed, side on, lit. In the FOREGROUND, close to camera and clearly out of focus, the back and shoulder of an ordinary traveller crossing the frame from left to right, MID-STEP with the back foot still lifted, a plain bag in one hand. Further back, two more ordinary travellers: one stopped and facing away, one walking out of frame. No face is readable anywhere: every figure is seen from behind or in silhouette.\n\nBare grey concourse with plain columns and a row of empty benches. Overcast daytime. The van is the only vehicle. Nothing is being loaded, nobody is boarding, no luggage is being handed over.\n\nWhat the camera asserts by standing in the middle of the concourse at walking height: this is an ordinary departure point, seen the way anyone passing through would see it, before there was any reason to look harder.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the foreground figure and the near columns, a MID GREY across the concourse floor and the van, and a genuinely LIGHT value in the open daylight beyond the kerb. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not plaster texture, not tile, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no destination boards, no logos, no emblem, no number plate.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'kf02_los_cuatro_espaldas': {
        'ranura': 'r04',
        'cuadros': 303,
        'que': 'los cuatro de espaldas en el anden',
        'personaje': '',
        'id': 'BhSkQEboQR',
        'semilla': 159047,
        'prompt': 'Wide shot from behind of FOUR TRAVELLERS standing together on a kerb with their backs to camera, each carrying a small plain grey backpack, looking away down an empty road. Four adults of about thirty, two men and two women, each in plain grey everyday clothes, no colour anywhere on any of them, distinct in build and hair. No faces visible. Bare grey roadside behind them, overcast flat light, no other person in frame, no vehicles, no signage.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. Skin stays in a desaturated warm grey range, barely tinted, never a saturated skin tone. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'cama_formulario': {
        'ranura': 'r05',
        'cuadros': 178,
        'que': 'el formulario con la casilla migratoria en blanco',
        'personaje': '',
        'id': 'N2hIvaX6D9',
        'semilla': 686871,
        'prompt': 'Close shot, straight on and slightly from above, of a single blank printed form lying alone on a desk, the sheet occupying the middle of the frame. The form carries a plain empty header band and a column of short abstract grey bars standing in for unfilled fields: they are SOLID FLAT GREY and contain absolutely nothing inside them, and every field box on the sheet is EMPTY. The sheet is LIGHT GREY. THE DESK SURFACE IS A PERFECTLY UNIFORM FLAT MID GREY, plain and smooth: not stone, not marble, not granite, not wood grain, not concrete, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain and no pattern of any kind. A DARK GREY desk edge across the bottom and the shadow under the sheet anchor the lower part of the frame. No hands, no fingers, no people, no pen, no stamp.\n\nThe frame must have three clearly separate tonal zones: deep dark in the desk edge and the shadow under the sheet, mid grey across the desk surface, light only on the sheet. No large area of near-black and no large area of near-white anywhere. NO LARGE EMPTY BACKGROUND SURFACE AT ALL: the desk and the sheet fill the frame edge to edge.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no signature, no logos, no coat of arms, no emblem, no national insignia of any country.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_sello_sin_fecha': {
        'ranura': 'r06',
        'cuadros': 167,
        'que': 'el sello sin fecha',
        'personaje': '',
        'id': 'aF4gGhwfSh',
        'semilla': 659732,
        'prompt': 'Three-quarter angled shot of a desk corner: a MID GREY desktop with eleven small printed screenshots laid out across it in a loose grid, each one a LIGHT GREY rectangle with faint illegible mid grey bars suggesting lines of a chat conversation, some sitting slightly askew. A DARK GREY desk edge runs along the bottom of the frame and a DARK GREY wall fills the upper third behind the desk. Nothing else. No hands, no people, no device. Flat even light. The frame has three clearly separate tonal zones: dark wall and desk edge, mid grey desktop, light screenshots.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no dates, no logos, no emoji — the marks on the screenshots are abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'r07_luis_cuenta': {
        'ranura': 'r07',
        'cuadros': 178,
        'que': 'Luis sobre el hombro, la mano detenida antes del teclado',
        'personaje': 'Luis',
        'id': 'lJM0jVKgv9',
        'semilla': 536524,
        'prompt': "Medium close shot taken from BEHIND AND JUST ABOVE LUIS'S RIGHT SHOULDER, so the camera sees what he sees and not his face. The back of his shoulder and the edge of his jaw occupy the DARK lower left corner of the frame, close to camera and clearly out of focus, reduced to a simple soft shape. The plain open laptop on the MID GREY desk fills the lit centre of the frame, seen from his side. THE LAPTOP SCREEN IS A PLAIN LIGHT GREY RECTANGLE WITH ABSOLUTELY NOTHING ON IT: no window, no column, no bars, no icons, no cursor.\n\nLUIS is a man of about thirty-five, medium build, medium height, short dark hair neatly combed, wearing a plain mid-grey collared shirt over plain grey trousers and grey shoes, with a plain institutional yellow band running down the front placket of the shirt. His left hand lies flat and completely still on the desk beside the laptop. His right hand is RAISED AND STOPPED HALFWAY to the keyboard, fingers slightly apart, hovering and not touching the keys: he is about to type and is not typing. The desk is otherwise bare. No other person anywhere in the frame.\n\nThe camera stays behind his shoulder, locked and perfectly level, and does not move. What the camera asserts by standing there: we are looking at the account from his side of the desk, and it is telling us nothing.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not plaster texture, not wallpaper, not wood grain, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nThe frame must have three clearly separate tonal zones: deep dark, mid grey and light. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, readable at a glance, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20. It must read as grey with a faint warm tint, never as brown and never as a saturated skin colour. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia, no badge.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.",
    },
    'r08_mesa_manos': {
        'ranura': 'r08',
        'cuadros': 237,
        'que': 'la mesa del equipo en cenital, ocho manos y una hoja a medio deslizar',
        'personaje': '',
        'id': 'ovUldy7829',
        'semilla': 918831,
        'prompt': 'Overhead shot looking STRAIGHT DOWN at a DARK GREY institutional meeting table, the camera directly above the table top and perfectly level, so the table surface fills the whole frame and NO FACE, NO HEAD AND NO SHOULDER IS VISIBLE ANYWHERE: only the table and the plain forearms and hands that enter from the edges of the frame.\n\nFour pairs of hands are placed around the table edge, in plain mid grey sleeves with plain cuffs and nothing on them. One hand is HALFWAY THROUGH PUSHING a single LIGHT GREY sheet toward the centre of the table, the sheet caught mid-slide and still under the fingertips. A second hand holds a plain dark pen upright, point above the table, not writing. A third lies flat and open, palm down. A fourth is loosely closed beside a plain closed folder. The gestures are all different from one another.\n\nA few plain LIGHT GREY sheets lie scattered across the MID GREY table top. No uniforms, no cuffs with markings, no rings, no watches. What the camera asserts by standing directly overhead: this is a mechanism being operated, not a group of people.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not plaster texture, not wallpaper, not wood grain, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nThe frame must have three clearly separate tonal zones: deep dark, mid grey and light. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20. It must read as grey with a faint warm tint, never as brown and never as a saturated skin colour. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia, no badge.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'r09_teresa_cocina': {
        'ranura': 'r09',
        'cuadros': 150,
        'que': 'Teresa sola en la cocina del alojamiento',
        'personaje': 'Teresa',
        'id': 'vQPOHIoa47',
        'semilla': 617083,
        # se repitio: la primera version quedo en 1lYzl9Yr4r
        'repetida': '1lYzl9Yr4r',
        'prompt': 'Medium shot of TERESA alone in the plain kitchen of a modest lodging house, the camera standing just inside the doorway and slightly low, so the depth of the kitchen opens behind her and the near door frame darkens the left edge of the frame. She stands at the worktop, turned three-quarters toward the camera.\n\nTERESA is a woman of about forty-five, medium build, medium height, dark hair tied back, wearing a PLAIN INSTITUTIONAL BLUE APRON over a plain light grey blouse and plain grey trousers. THE BLUE APRON IS A WIDE, STRONGLY SATURATED INSTITUTIONAL BLUE GARMENT and is THE ONLY SATURATED COLOUR ANYWHERE IN THE WHOLE IMAGE; it carries no mark, no logo and no emblem.\n\nHER POSE, EXACTLY: both hands are together LOW, AT WAIST HEIGHT, just above the worktop, holding and twisting a small folded cloth between them. HER ELBOWS STAY DOWN AND CLOSE TO HER SIDES. HER ARMS ARE NEVER RAISED ABOVE WAIST HEIGHT, neither arm is extended away from her body, and neither hand goes anywhere near her face. Her shoulders are level and relaxed. Her head is tilted slightly down, looking at her own hands, not at the camera. Her mouth is closed. Her expression is plain ordinary concentration, neither kind nor hard, neither sad nor cheerful.\n\nShe is NOT reaching for anything, NOT recoiling, NOT sneezing, NOT wiping her face, NOT waving and NOT gesturing to anyone. There is nobody else in the frame to gesture to.\n\nA bare worktop with a plain sink, a plain shelf with unlabelled containers, a doorway through to a dark corridor behind her. Nothing is being handed to anyone, no money and no documents anywhere.\n\nWhat the camera asserts by standing in the doorway: this is a working house and the work in it is hers.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the near door frame and the corridor behind her, a MID GREY across the kitchen walls and worktop, and a genuinely LIGHT value on the wall beside the sink. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not plaster texture, not tile, not wood grain, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, readable at a glance, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. Figures are 8 to 8.5 heads tall. The environment is entirely in greys apart from the one blue apron. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'cama_pasillo': {
        'ranura': 'r10',
        'cuadros': 223,
        'que': 'el pasillo del alojamiento, tres puertas cerradas',
        'personaje': '',
        'id': 'rgWzcDFxtc',
        'semilla': 876932,
        'prompt': 'Medium shot, straight on, looking down the narrow corridor of a modest lodging house, with three plain closed DARK GREY doors along the right wall and one at the far end, their frames and a low skirting board breaking the walls into clear panels. A single plain door handle on each door. The corridor walls are MID GREY and the floor running away from camera is DARK GREY. Light falls only on the far end wall and the top of the nearest door. Completely empty: no people, no hands, no furniture, no pictures, no notices, no numbers on the doors. Flat even light. Ordinary and quiet, not derelict.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth. THE WALLS ARE A PERFECTLY UNIFORM FLAT MID GREY: not stone, not marble, not granite, not concrete, not plaster texture, not wallpaper, not tile, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern and no pattern of any kind. THE FLOOR IS A PERFECTLY UNIFORM FLAT DARK GREY, with no tiles, no boards and no pattern of any kind. THE DOORS ARE PERFECTLY UNIFORM FLAT PANELS OF SOLID GREY.\n\nThe frame must have three clearly separate tonal zones: deep dark in the floor and the nearest door, mid grey across the walls, light only on the far end wall. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no labels, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'r11_tienda_esquina': {
        'ranura': 'r11',
        'cuadros': 257,
        'que': 'la tienda de la esquina, el brazo detenido antes del estante',
        'personaje': '',
        'id': '5jG2lxXKxe',
        'semilla': 533632,
        # se repitio: la primera version quedo en UPeDPV8wny
        'repetida': 'UPeDPV8wny',
        'prompt': 'Medium shot inside a SMALL neighbourhood corner shop, the camera standing behind the shop counter at the height of someone working there, looking out across the counter at the customer side. The shop is cramped and narrow: the far wall is close behind the customer, not distant.\n\nCOMPOSITION, EXACTLY: the DARK GREY counter top runs across the BOTTOM THIRD of the frame, close to camera and out of focus. The customer stands in the MIDDLE of the frame at medium distance, SEEN FROM BEHIND AND SLIGHTLY TO ONE SIDE so no face is visible. Plain grey shelving packed with plain unlabelled packets fills the WHOLE BACKGROUND directly behind him, close and filling the upper two thirds of the frame.\n\nHis right arm is RAISED AND STOPPED HALFWAY toward a packet on the shelf at shoulder height, the hand open, fingers apart, NOT YET TOUCHING IT. His left hand rests on the counter edge. He wears plain grey everyday clothes with no colour anywhere.\n\nNO MONEY, NO COINS, NO NOTES, NO WALLET, NO CARD AND NO TILL anywhere in the frame, and nothing is being handed from one person to another. No second customer, no shopkeeper in frame.\n\nWhat the camera asserts by standing behind the counter: we are inside the ordinary life of the neighbourhood, on the side that watches it come and go.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the near counter top, a MID GREY across the figure and the shelving, and a genuinely LIGHT value in the doorway at one side. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no price tags, no labels, no logos, no emblem, no brand name on any packet.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'cama_informe_esfero': {
        'ranura': 'r12',
        'cuadros': 169,
        'que': 'el informe y el esfero',
        'personaje': '',
        'id': 'fH9SsedCDY',
        'semilla': 370203,
        'prompt': 'Close overhead shot of a plain open report on a bare institutional desk, its pages covered in faint illegible grey bars standing in for lines of text, with a plain pen lying across one corner. Nothing else on the desk. No hands, no people. Flat even light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no logos, no emblem — the marks on the pages are abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'r13_certificado_luz': {
        'ranura': 'r13',
        'cuadros': 229,
        'que': 'el certificado de empleo a contraluz',
        'personaje': '',
        'id': '1lYzlD8r4r',
        'semilla': 30445,
        'prompt': 'Close shot of a single plain LIGHT GREY certificate sheet HELD UP TO THE LIGHT by two hands, the camera low and slightly behind the sheet so the light comes THROUGH the paper toward us and the fibres of the sheet glow faintly. The sheet fills the lit centre of the frame, held at a slight angle, one corner bending very slightly under its own weight.\n\nTwo plain hands hold it: one thumb and forefinger pinching the top left corner, the other hand flat behind the lower edge, steadying it. The hands are a plain flat desaturated warm grey, smooth and even. NO FACE, NO HEAD, NO SHOULDERS AND NO BODY anywhere in the frame: only the two forearms entering from the bottom corners in plain mid grey sleeves.\n\nThe printed content of the certificate is reduced to a plain empty header band and a few short abstract grey bars standing in for lines: SOLID FLAT GREY, containing absolutely nothing readable. A DARK GREY room beyond, simplified and out of focus.\n\nWhat the camera asserts by sitting under the sheet and looking through it: this document is being held up against the light, which is exactly what the case does to it.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the room behind and the near forearms, a MID GREY in the hands and sleeves, and a genuinely LIGHT value in the lit sheet itself. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth, with no mottling, no speckle, no veining, no blotches, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no signature, no stamp impression, no logos, no coat of arms, no emblem, no national insignia of any country.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading, no blotchy skin. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks.',
    },
    'cama_visado': {
        'ranura': 'r14',
        'cuadros': 228,
        'que': 'el pasaporte abierto en el visado',
        'personaje': '',
        'id': 'YMbEp4DWeC',
        'semilla': 171596,
        'prompt': 'Close shot, from above and slightly to the side, of a plain LIGHT GREY passport lying open on a desk at its visa page, the booklet occupying the middle of the frame. The visa page carries a plain empty rectangle and a few short abstract grey bars standing in for printed fields: they are SOLID FLAT GREY and contain absolutely nothing inside them. THE DESK SURFACE IS A PERFECTLY UNIFORM FLAT MID GREY, plain and smooth: not stone, not marble, not wood grain, with no mottling, no speckle and no pattern of any kind. A DARK GREY desk edge and the shadow under the booklet anchor the lower part of the frame. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the desk edge and the shadow under the booklet, mid grey across the desk surface, light only on the open pages. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no photograph, no face, no stamp impression, no logos, no coat of arms, no emblem, no national insignia of any country.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'r15_nidia_mostrador': {
        'ranura': 'r15',
        'cuadros': 210,
        'que': 'Nidia sola en el mostrador de su local',
        'personaje': 'Nidia',
        'id': 'WD5qDOncXe',
        'semilla': 632759,
        'prompt': 'Medium shot of NIDIA alone behind the plain counter of a very small street-front office, the camera standing on the customer side at counter height, straight on and level, so we see what someone walking in would see.\n\nNIDIA is a woman of about forty, slim, medium height, dark hair worn loose to the shoulders, wearing a plain mid-grey blouse over plain grey trousers, WITH NO COLOUR ANYWHERE ON HER AT ALL. Her left hand rests flat on a plain CLOSED ledger on the counter. Her right arm is RAISED AND STOPPED HALFWAY toward a plain shelf behind her, the hand open, not yet touching anything. She is looking at the shelf, not at the camera. Her expression is plain ordinary attention, neither welcoming nor hostile, neither warm nor cold.\n\nBehind her, a plain grey back wall and one plain shelf with unlabelled folders. The counter top is bare apart from the closed ledger. NO PASSPORTS, NO DOCUMENTS, NO RECEIPTS, NO MONEY and NO OTHER PERSON anywhere in the frame; nothing is being handed to anyone and nothing is being held back from anyone.\n\nWhat the camera asserts by standing on the customer side: this is what you would see if you walked in, and it is a very small room.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the counter front and the corners of the little room, a MID GREY across Nidia and the back wall, and a genuinely LIGHT value falling on the counter top. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not plaster texture, not wallpaper, not wood grain, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, readable at a glance, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'r16_pasaportes_cenital': {
        'ranura': 'r16',
        'cuadros': 233,
        'que': 'los pasaportes y los recibos en cenital',
        'personaje': '',
        'id': '0ek5eYfTfW',
        'semilla': 998752,
        'prompt': 'Close overhead shot looking STRAIGHT DOWN at an open desk drawer, the camera directly above and perfectly level, the drawer pulled out so its interior fills most of the frame. Inside: three plain passport booklets stacked loosely and slightly fanned, and a small pile of plain receipt slips beside them, all reduced to flat grey shapes.\n\nONE PLAIN HAND IS WITHDRAWING from the drawer, fingers still open and no longer touching anything, already moving out of the top edge of the frame. Nothing is being taken and nothing is being put in: the hand is leaving empty.\n\nTHE DRAWER INTERIOR IS A PLAIN FLAT LIGHT GREY. The DARK GREY drawer face and the dark inner shadow frame the shot on all sides, leaving almost no background visible. No faces, no heads, no bodies, no second hand.\n\nWhat the camera asserts by standing directly above the drawer: here is everything there is, counted from above, and it is very little.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the drawer face and the inner shadow, a MID GREY across the booklets and the hand, and a genuinely LIGHT value on the empty drawer interior. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth, with no mottling, no speckle, no veining, no blotches, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no photograph, no face, no stamp impression, no logos, no coat of arms, no emblem, no national insignia of any country.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading, no blotchy skin. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks.',
    },
    'r17_dos_carpetas': {
        'ranura': 'r17',
        'cuadros': 101,
        'que': 'dos carpetas separadas, y nada cruzando el vacio entre ellas',
        'personaje': '',
        'id': 'P3Io9V242C',
        'semilla': 739356,
        # se repitio: la primera version quedo en 1lYG5d5r4r
        'repetida': '1lYG5d5r4r',
        'prompt': 'Overhead shot looking STRAIGHT DOWN at a desk, the camera directly above and perfectly level. THE DESK SURFACE IS A LIGHT GREY, clearly the lightest thing in the frame. Two plain closed DARK GREY folders lie flat on it, WELL APART, reading as two dark rectangles against the light desk, with a WIDE BAND OF BARE EMPTY LIGHT GREY DESK between them: that empty gap is the subject of the picture and must be clearly wider than either folder.\n\nABSOLUTELY NOTHING CROSSES THE GAP: no paper, no hand, no pen, no line, no string, no cable and no shadow bridges the two folders. One plain hand is WITHDRAWING from the left folder, fingers still open and no longer touching it, already moving out of the left edge of the frame. The hand is a plain flat desaturated warm grey, smooth and even, with no blotches and no mottling.\n\nA DARK GREY desk edge runs across the bottom of the frame. No faces, no heads, no bodies, no second hand. What the camera asserts by standing directly overhead: here are two things side by side, and nothing joining them.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the folders and the desk edge, a MID GREY in the sleeve and the shadows, and a genuinely LIGHT GREY across the open desk surface. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not plaster texture, not wallpaper, not wood grain, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20. It must read as grey with a faint warm tint, never as brown, never pink and never as a saturated skin colour. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia, no badge.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading, no freckles, no veins and no blotchy skin. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'r18_puesto_control': {
        'ranura': 'r18',
        'cuadros': 170,
        'que': 'el puesto de control de carretera, vacio',
        'personaje': '',
        'id': 'DojroZHpcl',
        'semilla': 672738,
        'prompt': "Wide shot of a small roadside migration control post seen from the road itself, the camera standing on the tarmac at the height of a driver's eye, straight on and perfectly level. A plain booth with a wide window stands beside the road; a plain barrier arm is RAISED HALFWAY, caught mid-lift at an angle, neither down nor fully up. A plain grey car has stopped just short of the barrier, seen from behind, its brake lights not lit.\n\nInside the booth window there is only a plain dark SHAPE of a seated figure, kept small, unlit and completely unidentifiable: no face, no features, no uniform, no cap, no insignia, no badge and no markings of any kind anywhere in the frame. Nobody is standing on the road, nobody is approaching the car, no document is being passed and nothing is being inspected.\n\nA bare grey hut behind, flat low scrub on both sides, an overcast sky. Ordinary and quiet, not derelict and not a checkpoint of the military kind.\n\nWhat the camera asserts by standing on the road at a driver's height: this is the single point that was asked about, and it is small.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the booth interior and the car, a MID GREY across the road and the hut, and a genuinely LIGHT value in the sky. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not concrete texture, not gravel, not stone, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no road signs, no flags, no logos, no emblem, no insignia, no number plate.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.",
    },
    'r19_informe_dedo': {
        'ranura': 'r19',
        'cuadros': 197,
        'que': 'el informe con el dedo detenido a mitad de un renglon',
        'personaje': '',
        'id': 'rgWnSlgxtc',
        'semilla': 866738,
        'prompt': "Close shot taken STEEPLY FROM ABOVE AND BEHIND a plain open report lying on a desk, the camera looking down over the top edge of the page at a sharp angle, so the page recedes away from us and we read it from the reader's own position.\n\nTwo plain hands hold the report: the left thumb presses the left page flat against the spine, the fingers splayed; the right index finger is STOPPED HALFWAY DOWN a line of the right page, not moving, the rest of that hand curled back. The hands are a plain flat desaturated warm grey, smooth and even.\n\nThe pages are a plain LIGHT GREY and their content is reduced to faint illegible grey bars standing in for lines of text: SOLID FLAT GREY blocks of different lengths, with absolutely nothing readable, no numbers and no dates. A DARK GREY desk surface around the report and a dark edge at the bottom of the frame.\n\nNO FACE, NO HEAD AND NO SHOULDERS anywhere in the frame: only the two forearms entering from the bottom corners in plain mid grey sleeves, with no cuff markings, no watch and no ring.\n\nWhat the camera asserts by looking down over the reader's own shoulder: somebody is reading this as proof, and the finger has stopped on the line where that happens.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the desk and the near edge, a MID GREY in the hands and sleeves, and a genuinely LIGHT value across the open pages. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth, with no mottling, no speckle, no veining, no blotches, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no logos, no emblem, no insignia.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading, no blotchy skin. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks.",
    },
    'r20_documento_mostrador': {
        'ranura': 'r20',
        'cuadros': 104,
        'que': 'el documento recien soltado en el mostrador, sin que nadie lo recoja',
        'personaje': '',
        'id': 'eIsxMA7dqL',
        'semilla': 10727,
        'prompt': 'Close shot from the SIDE at counter height, the camera low and exactly level with the counter top so the laminate runs across the frame as one hard horizontal edge. A single folded LIGHT GREY document lies on the MID GREY counter in the lit centre of the frame, its fold standing slightly proud.\n\nOne plain hand HAS JUST LET GO of it: the fingers are still curved in the shape of the fold and hover a few centimetres above the paper, no longer touching it. THERE IS NO SECOND HAND ANYWHERE IN THE FRAME and nobody is reaching for the document. No faces, no heads, no bodies: only that one forearm entering from the right edge in a plain mid grey sleeve.\n\nThe DARK GREY front of the counter fills the lower part of the frame. Behind, a plain MID GREY partition, simplified and out of focus. What the camera asserts by sitting at the height of the counter: the document has been produced, and nobody has yet picked it up.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not plaster texture, not wallpaper, not wood grain, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nThe frame must have three clearly separate tonal zones: deep dark, mid grey and light. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20. It must read as grey with a faint warm tint, never as brown and never as a saturated skin colour. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia, no badge.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'r21_sala_alto': {
        'ranura': 'r21',
        'cuadros': 173,
        'que': 'la sala de reunion desde la esquina alta',
        'personaje': '',
        'id': 'Eb695j4uuO',
        'semilla': 181252,
        'prompt': 'Wide shot of a plain institutional meeting room taken FROM A HIGH CORNER of the room, the camera up near the ceiling line looking down across the long table, so the whole room and everyone in it is seen from above and behind. A long bare table runs away from the camera with plain chairs along both sides.\n\nFive ordinary people are seated around it, ALL SEEN FROM ABOVE AND FROM BEHIND: we see shoulders, the crowns of heads and forearms, and NO FACE IS VISIBLE OR READABLE ANYWHERE. They wear plain mid grey clothes with no uniform, no insignia, no badge, no lanyard and no markings of any kind. One has pushed a chair back and turned it slightly away from the table, caught mid-turn. Another leans forward with both forearms on the table. One chair at the far end stands EMPTY and turned away.\n\nA few plain LIGHT GREY sheets lie on the MID GREY table. A plain blank wall at the far end. Nothing is being handed across the table, no screen, no projection.\n\nWhat the camera asserts by sitting high in the corner: the decision is being taken in a room by a group, and no single person in it owns the decision.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the near foreground and the chairs, a MID GREY across the floor and the seated figures, and a genuinely LIGHT value on the table top and the far wall. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not concrete, not plaster texture, not wallpaper, not wood grain, not carpet pattern, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia, no flag, no coat of arms.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'r23_omar_volante': {
        'ranura': 'r23',
        'cuadros': 171,
        'que': 'Omar al volante, la mano a medio camino de la palanca',
        'personaje': 'Omar',
        'id': 'bxAZKZF5Y2',
        'semilla': 297321,
        # se repitio: la primera version quedo en xScnk1NjfW
        'repetida': 'xScnk1NjfW',
        'prompt': 'Medium shot taken from INSIDE THE CAB of a plain passenger van, from the empty passenger seat at seat height, looking across at OMAR behind the wheel. The DARK GREY dashboard runs across the bottom of the frame close to camera and out of focus; the near door pillar frames the right edge; the windscreen is the LIGHT part of the frame.\n\nOMAR is a man of about forty, stocky, medium height, short dark hair and a close-trimmed moustache, wearing a plain mid-grey work shirt over plain grey trousers. ACROSS THE CHEST OF HIS WORK SHIRT RUNS A WIDE BAND OF STRONG SATURATED INSTITUTIONAL YELLOW, from one side seam to the other, cut off square at both ends like a sewn-in panel of the garment. THAT YELLOW BAND IS THE ONLY SATURATED COLOUR ANYWHERE IN THE WHOLE IMAGE and must be clearly stronger and brighter than everything around it; it is a wide band, never a small patch, never a badge, never a logo, and it carries no mark of any kind.\n\nHis left hand is low on the steering wheel. His right hand is HALFWAY TO THE GEAR LEVER and has not reached it, fingers open, caught mid-reach. HE IS LOOKING AT THE WING MIRROR ON HIS SIDE, not at the camera and not straight ahead; his mouth is closed and his expression is plain working attention, neither grim nor friendly, neither heroic nor defeated.\n\nThrough the windscreen, a plain road and flat open ground, simplified and softly out of focus. No other person in the van. No cargo, no luggage, no passengers, no documents, nothing being handed to anyone.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the dashboard and the door pillar, a MID GREY across Omar and the cab interior, and a genuinely LIGHT value in the windscreen. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth, with no mottling, no speckle, no veining, no blotches, no grain, no noise and no pattern of any kind.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, readable at a glance, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20. It must read as grey with a faint warm tint, never as brown, never orange and never as a saturated skin colour. Figures are 8 to 8.5 heads tall. The environment is entirely in greys apart from the one yellow band. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia, no badge.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'cama_telefono_omar': {
        'ranura': 'r24',
        'cuadros': 180,
        'que': 'el telefono de Omar, solo',
        'personaje': '',
        'id': 'N2heC7F6D9',
        'semilla': 321566,
        'prompt': 'Close overhead shot of a plain dark grey mobile phone lying face up and alone on a MID GREY desk, its screen a light grey rectangle with two faint illegible mid grey message bars on it. The phone fills about a third of the frame, with the desk visible around it on all sides. No hands, no people. Flat even light. The image has a wide tonal range: the phone body is deep dark grey, the desk is mid grey, only the screen is light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no app icons, no logos, no emoji — the screen content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf15_conversacion_pantalla': {
        'ranura': 'r25',
        'cuadros': 175,
        'que': 'la conversacion en la pantalla',
        'personaje': '',
        'id': 'lJMGAfkgv9',
        'semilla': 695287,
        'prompt': 'Close shot, straight on, of a plain desktop monitor on a bare grey desk, its screen filled with a long continuous column of faint illegible grey message bars running from top to bottom, suggesting a complete conversation. Nothing else in frame. No hands, no people, no keyboard. Flat even light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no app icons, no logos, no emoji — the screen content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'r26_pantalla_mensajes': {
        'ranura': 'r26',
        'cuadros': 122,
        'que': 'la columna de mensajes, con la luz de la pantalla cayendo sobre el escritorio',
        'personaje': '',
        'id': 'p8LrVWdehw',
        'semilla': 891911,
        'prompt': 'Medium shot, straight on and perfectly level, of a plain DARK GREY desktop monitor standing on a MID GREY desk. The screen fills the lit centre of the frame with a LONG CONTINUOUS COLUMN of faint illegible grey message bars of different lengths, running from the top of the screen to the bottom without a break, reduced to plain flat grey blocks with no readable character anywhere.\n\nThe pale light of the screen falls FORWARD ONTO THE DESK SURFACE in front of the monitor as a soft widening wedge that reaches and touches the near edge of the desk. IT MUST NOT APPEAR AS A FREE-FLOATING BRIGHT RECTANGLE hanging in the air or on a wall: the light is only ever on the desk, attached to the desk.\n\nIn the DARK foreground, close to camera and clearly out of focus, the plain back of an office chair, and one plain hand resting still on the near edge of the desk. No face, no head and no shoulders are visible above the chair back. What the camera asserts by standing square to the screen: the whole conversation is here, and it is being read straight on.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not plaster texture, not wallpaper, not wood grain, with no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind.\n\nThe frame must have three clearly separate tonal zones: deep dark, mid grey and light. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20. It must read as grey with a faint warm tint, never as brown and never as a saturated skin colour. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem, no insignia, no badge.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks: the movement is carried by the pose alone, frozen, never smeared.',
    },
    'r27_cuaderno_bajo': {
        'ranura': 'r27',
        'cuadros': 267,
        'que': 'el cuaderno de cuentas, las dos paginas cubiertas de renglones',
        'personaje': '',
        'id': 'tCJwEl4mZJ',
        'semilla': 948150,
        'prompt': 'Close shot, three-quarter angle and LOW, almost at the level of the worktop, of a plain ruled accounts notebook lying open on a bare grey worktop, the near page curving slightly up toward the camera so the spine and both pages recede away.\n\nBoth pages are covered in faint illegible grey bars arranged in TWO NARROW COLUMNS running down each page: SOLID FLAT GREY blocks, with absolutely nothing readable, no numbers, no dates and no currency marks. The bars reach the very bottom of both pages without a gap and without a closing line: the columns simply keep going off the edge of the page.\n\nONE PLAIN HAND IS JUST LEAVING the notebook: the fingertips have lifted off the right page and the hand is already moving out of the right edge of the frame, fingers still slightly curved. A plain pen lies across the gutter of the notebook, at rest, not held.\n\nA DARK GREY worktop edge runs across the bottom of the frame close to camera. NO FACE, NO HEAD AND NO BODY anywhere: only the one forearm in a plain mid grey sleeve.\n\nWhat the camera asserts by sitting almost on the worktop: we are at the height of the book itself, and the columns run off the page without ever closing.\n\nThe frame must have three clearly separate tonal zones and all three must be present: a DEEP DARK in the near worktop edge and the shadow under the notebook, a MID GREY across the worktop and the sleeve, and a genuinely LIGHT value on the open pages. No large area of near-black and no large area of near-white anywhere.\n\nEVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA OF SOLID GREY, plain and smooth, with no mottling, no speckle, no veining, no blotches, no grain, no noise and no pattern of any kind.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Skin is a desaturated warm grey: hue around 25 degrees and saturation no higher than 0.20, never brown, never pink. The environment is entirely in greys. Flat even light, perfectly level camera, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading, no blotchy skin. Out-of-focus areas are PAINTED blur: simplified shapes with soft edges, never circular bokeh discs. No motion blur, no speed lines and no streaks.',
    },
    'kf17_dos_viajeros_se_van': {
        'ranura': 'r29',
        'cuadros': 177,
        'que': 'dos viajeros que se van',
        'personaje': '',
        'id': 'XmgKKm1Bfo',
        'semilla': 572396,
        'prompt': 'Wide shot from behind of TWO TRAVELLERS walking away from camera down an empty road, each carrying a small plain grey backpack, already some distance off. A man and a woman of about thirty in plain grey everyday clothes, no colour anywhere on either of them. No faces visible. Bare grey roadside, overcast flat light, no other person in frame, no vehicles, no signage.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading.',
    },
    'cama_carretera_golfo': {
        'ranura': 'r30',
        'cuadros': 153,
        'que': 'la carretera hacia el Golfo',
        'personaje': '',
        'id': 'nVqvvv5YQD',
        'semilla': 64859,
        'prompt': 'Wide shot of an empty two-lane road running away from camera towards the Gulf of Urabá, flat low scrub on both sides and a faint line of sea and sky at the horizon. Overcast daytime, flat even light. Completely empty: no people, no vehicles, no buildings, no signage. Ordinary and quiet, not desolate.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
}

# fuera de la linea desde el 21 de octubre. El prompt se conserva:
# una placa descartada sigue sirviendo de referencia.
DESCARTADAS = {
    'cama_cajon': {
        'ranura': 'historico',
        'motivo': 'se repitio como dos carpetas con el vacio entre ellas',
        'cuadros': 101,
        'que': 'el cajon vacio',
        'personaje': '',
        'id': 'eIskC6vdqL',
        'semilla': 869065,
        'prompt': 'Very close shot of one open drawer of a DARK GREY metal filing cabinet, the drawer filling most of the frame, seen straight on and slightly from above. The drawer is pulled fully out and is COMPLETELY EMPTY: nothing inside it, no papers, no folders, no documents, only the plain flat LIGHT GREY empty interior and its dark inner shadow. The dark grey cabinet front and the dark grey drawer face frame the shot on all sides, leaving almost no background visible. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the cabinet front and the inner shadow, mid grey across the drawer face, light only on the empty drawer interior. No large area of near-black and no large area of near-white anywhere. NO LARGE EMPTY BACKGROUND SURFACE AT ALL: the cabinet fills the frame edge to edge.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Every surface is a perfectly uniform flat area of solid grey meeting the next at a hard edge, smooth and plain: no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind anywhere in the image. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no labels, no signage, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_mesa_equipo': {
        'ranura': 'historico',
        'motivo': 'mesa vacia; se repitio con ocho manos a media accion',
        'cuadros': 237,
        'que': 'la mesa del equipo',
        'personaje': '',
        'id': 'nVqvKA2YQD',
        'semilla': 777749,
        'prompt': 'Overhead shot looking straight down at a DARK GREY institutional meeting table in a bare grey office, with four empty chairs tucked in around it, a closed plain light grey folder and a plain pen set at each place. The table is otherwise bare. The floor around it is mid grey. Completely empty: no people, no hands. Flat even overhead light. The image has a wide tonal range: deep dark greys in the table and the chairs, mid greys in the floor, light greys only in the folders.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_pantalla': {
        'ranura': 'historico',
        'motivo': 'el cuadrado de luz flotaba; se repitio con la luz en la mesa',
        'cuadros': 184,
        'que': 'el monitor de lado',
        'personaje': '',
        'id': 'N2hBzcX6D9',
        'semilla': 207172,
        'prompt': 'Wide shot of an empty office desk seen from the side and slightly behind, with a plain DARK GREY computer monitor turned three quarters away from camera so only the edge of its LIGHT GREY screen is visible, its pale light falling on the MID GREY wall beside it. An empty chair is pushed back from the desk. The desk surface is mid grey and bare except for a closed plain notebook. The foreground floor and the near edge of the desk are dark grey. Completely empty: no people, no hands. Flat even light. Ordinary and quiet.\n\nThe frame must have three clearly separate tonal zones: deep dark in the monitor body, the chair and the foreground, mid grey across the wall and the desk, light only on the visible sliver of screen and the patch of wall it lights. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no icons, no logos, no brand name on the monitor.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_sala_reunion': {
        'ranura': 'historico',
        'motivo': 'sala vacia; se repitio desde la esquina alta',
        'cuadros': 173,
        'que': 'la sala de reunion vacia',
        'personaje': '',
        'id': '5jG94j2Kxe',
        'semilla': 157984,
        'prompt': 'Wide shot of a plain institutional meeting room seen straight on from one end, a long bare table with empty chairs along both sides, a blank grey wall panel at the far end, plain grey walls. Completely empty: no people, no uniforms. Flat even overhead light. No whiteboard writing, no posters, no flags.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no coat of arms, no emblem of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_tienda_esquina': {
        'ranura': 'historico',
        'motivo': 'tienda vacia; se repitio con el brazo detenido',
        'cuadros': 257,
        'que': 'la tienda de la esquina',
        'personaje': '',
        'id': 'u5i7S3TQLD',
        'semilla': 208431,
        'prompt': 'Medium wide shot of the counter of a small neighbourhood corner shop seen from the customer side, plain grey shelving behind holding unlabelled packages, a bare counter with two unlabelled grocery packets on it. Completely empty: no shopkeeper, no customer, no people. Flat even light. No price labels, no packaging text, no notices.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf01_terminal_vehiculo': {
        'ranura': 'historico',
        'motivo': 'van vacia; la ranura pide gente a media accion',
        'cuadros': 243,
        'que': 'la van esperando en la terminal',
        'personaje': '',
        'id': 'u5i7jhxQLD',
        'semilla': 886543,
        'prompt': 'Wide shot of a plain passenger van parked and waiting at the kerb outside an intercity bus terminal, seen from the side, doors closed. Bare grey concourse behind with plain columns and empty benches. Overcast daytime, flat even light. Completely empty: no people, no other vehicles, no signage.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no number plate.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf03_luis_computador': {
        'ranura': 'historico',
        'motivo': 'el gesto se leia como llevarse la mano a la cara',
        'cuadros': 178,
        'que': 'Luis en el escritorio',
        'personaje': 'LUIS',
        'id': 'huysKsivqL',
        'semilla': 525702,
        'prompt': 'Medium shot, waist up, of LUIS seated at a plain desk in a bare grey interior, one hand resting beside a plain laptop whose screen is blank grey, looking down at it. LUIS is a man of about thirty-five, medium build, medium height, short dark hair neatly combed, wearing a plain mid-grey collared shirt over plain grey trousers, with a plain institutional yellow band running down the front placket of the shirt. Composed, withheld expression. The desk is otherwise empty. No other person in frame, nothing written or displayed anywhere.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, readable at a glance, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted, never a saturated skin tone. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The yellow band is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf04_marta_giros': {
        'ranura': 'historico',
        'motivo': 'Marta no tiene frase propia; su dato va en el carton ae00',
        'cuadros': 167,
        'que': 'Marta en la oficina de giros',
        'personaje': 'MARTA',
        'id': 'ksn6JVb16B',
        'semilla': 127285,
        'prompt': 'Medium shot of MARTA standing at the counter of a small money-transfer office, seen from the side, one hand flat on the counter. MARTA is a woman of about thirty-five, medium build, medium height, dark hair tied back, wearing a plain light grey blouse over plain grey trousers, with a plain institutional yellow scarf knotted at the neck. Composed, withheld expression, not smiling. Plain grey counter and plain grey partition behind, nothing on the counter. No clerk, no other person in frame, no forms, no notices, no money visible.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The yellow scarf is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf05_omar_volante': {
        'ranura': 'historico',
        'motivo': 'se repitio con la mano a medio camino de la palanca',
        'cuadros': 150,
        'que': 'Omar al volante de la van',
        'personaje': 'OMAR',
        'id': 'aF4UheIfSh',
        'semilla': 725866,
        'prompt': 'Medium shot from outside the open driver window of a plain MID GREY van, looking slightly down at OMAR behind the wheel, his whole torso clearly visible and unobstructed, both hands low on the steering wheel so that NOTHING crosses his chest. OMAR is a man of about forty, stocky, medium height, short dark hair and a close-trimmed moustache, wearing a plain MID GREY work shirt over plain grey trousers, with A WIDE PLAIN INSTITUTIONAL YELLOW BAND RUNNING STRAIGHT ACROSS THE CHEST OF THE WORK SHIRT FROM ONE SIDE SEAM TO THE OTHER, horizontal, continuous, fully visible end to end, unbroken and not covered by his arms. The band is a flat uniform area of solid colour with no pattern, no emblem, no lettering and no marking of any kind. He looks ahead through the windscreen, calm and ordinary, nothing menacing. The DARK GREY van door and window frame surround him; the sky beyond the windscreen is light. No other person in frame, no cargo, no passengers.\n\nThe frame must have three clearly separate tonal zones: deep dark in the van door and the cab interior, mid grey across his shirt and the van body, light only in the windscreen and the sky beyond. No large area of near-white anywhere.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no plate number, no logos, no brand name on the van.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading.',
    },
    'kf06_teresa_cocina': {
        'ranura': 'historico',
        'motivo': 'se repitio con Teresa trabajando, no de pie',
        'cuadros': 223,
        'que': 'Teresa en la cocina de la pension',
        'personaje': 'TERESA',
        'id': 'Eb6wgP7uuO',
        'semilla': 774546,
        'prompt': 'Medium wide shot of TERESA standing in the plain kitchen of a modest lodging house, one hand on the edge of a bare worktop, facing camera. TERESA is a woman of about forty-five, medium build, dark hair tied back, wearing a plain institutional blue apron over a plain light grey blouse and plain grey trousers. Settled, matter-of-fact expression. Behind her a plain grey worktop with two unlabelled pots and a stack of plain plates. No other person in frame, no food, no packaging, no notices.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The blue apron is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf07_certificado_empleo': {
        'ranura': 'historico',
        'motivo': 'filetes casi negros; se rehizo a contraluz',
        'cuadros': 229,
        'que': 'el certificado de empleo',
        'personaje': '',
        'id': 'nVqfGhiYQD',
        'semilla': 414940,
        'prompt': 'Medium close shot, straight on and slightly from above, of a single plain LIGHT GREY employment certificate lying on a desk, the sheet occupying the middle of the frame. The sheet carries a short block of abstract grey bars standing in for lines of text and a plain empty rectangle near its lower right corner standing in for a seal: the bars and the rectangle are SOLID FLAT GREY and contain absolutely nothing inside them. THE DESK SURFACE IS A PERFECTLY UNIFORM FLAT MID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not wood grain, with no mottling, no speckle, no veining, no blotches and no pattern of any kind. A DARK GREY desk edge and its shadow run along the bottom of the frame. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the desk edge and the shadow under it, mid grey across the desk surface, light only on the sheet. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no signature, no stamp impression, no logos, no coat of arms, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf08_nidia_local': {
        'ranura': 'historico',
        'motivo': 'se repitio con Nidia en el mostrador, a media accion',
        'cuadros': 210,
        'que': 'Nidia detras del mostrador',
        'personaje': 'NIDIA',
        'id': 'MBxFuF3DCm',
        'semilla': 237277,
        'prompt': 'Medium shot of NIDIA standing behind the plain counter of a very small street-front office, both hands resting on the counter top, facing camera. NIDIA is a woman of about forty, slim, dark hair worn loose to the shoulders, wearing a plain mid-grey blouse over plain grey trousers, no colour anywhere on her. Composed, withheld expression. Behind her a bare grey wall and a single empty shelf. The counter is empty. No other person in frame, no notices, no posters.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf09_pasaportes_recibos': {
        'ranura': 'historico',
        'motivo': 'se repitio en cenital',
        'cuadros': 233,
        'que': 'el cajon con los pasaportes',
        'personaje': '',
        'id': '4RtDVW49Aa',
        'semilla': 220595,
        'prompt': 'Close shot of an open desk drawer seen from slightly above, containing three plain passport booklets stacked loosely and a small pile of plain receipt slips beside them. The drawer interior is bare. No hands, no people. Flat even light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no logos, no coat of arms, no emblem — the passport covers and the slips are blank.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf10_puesto_control': {
        'ranura': 'historico',
        'motivo': 'se repitio con el puesto como arquitectura',
        'cuadros': 170,
        'que': 'el puesto de control en la via',
        'personaje': '',
        'id': 'WD5fv1bcXe',
        'semilla': 47454,
        'prompt': 'Wide shot of a small roadside migration control post seen straight on, a plain booth with a raised barrier beside an empty road, a bare grey hut behind. Overcast daytime, flat even light. Completely empty: no officers, no uniforms, no people, no vehicles. Ordinary and neutral, not threatening. No flags, no shields, no signage.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no coat of arms, no emblem of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf11_informe_dos_meses': {
        'ranura': 'historico',
        'motivo': 'se repitio con el dedo detenido en el renglon',
        'cuadros': 197,
        'que': 'el informe de los dos meses',
        'personaje': '',
        'id': '4RtDH3h9Aa',
        'semilla': 698280,
        'prompt': 'Three-quarter angled shot of a desk: a MID GREY desktop with a single LIGHT GREY sheet of a migration response lying on it, its content reduced to faint illegible mid grey bars with one short bar near the top isolated from the rest, and a DARK GREY closed folder lying beside it. A DARK GREY wall fills the upper third of the frame behind the desk. Nothing else. No hands, no people. Flat even light. The frame has three clearly separate tonal zones: dark wall and folder, mid grey desktop, light sheet.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no dates, no logos, no coat of arms, no emblem — the content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf12_viajero_documento': {
        'ranura': 'historico',
        'motivo': 'se le veia la cara a un viajero, contra la regla',
        'cuadros': 104,
        'que': 'un viajero con su documento',
        'personaje': 'viajero',
        'id': 'rgW3Vzqxtc',
        'semilla': 166847,
        'prompt': 'Medium shot of one of THE FOUR TRAVELLERS, a man of about thirty in plain grey everyday clothes with no colour anywhere, standing against a MID GREY wall and holding out a single plain light grey folded document towards camera at chest height, looking down at it. Composed, matter-of-fact expression. No other person in frame. The document is blank: no printing of any kind on it. The image has a wide tonal range: the wall is mid grey, his clothes are mid to dark grey, only the document is light.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Skin stays in a desaturated warm grey range, barely tinted. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no stamps, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf13_marta_lejos': {
        'ranura': 'historico',
        'motivo': 'el guion no le da frase propia; salio de la linea',
        'cuadros': 170,
        'que': 'Marta sola y pequena',
        'personaje': 'MARTA',
        'id': '1lYi624r4r',
        'semilla': 183382,
        'prompt': 'Wide shot of MARTA standing alone and small in the middle of a bare grey interior, full figure, arms at her sides, facing camera from a distance. MARTA is a woman of about thirty-five, medium build, dark hair tied back, wearing a plain light grey blouse over plain grey trousers, with a plain institutional yellow scarf knotted at the neck. Composed, withheld expression, not smiling. The room is empty: plain walls, a plain floor, no furniture, no other person in frame.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The yellow scarf is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf14_orden_servicio': {
        'ranura': 'historico',
        'motivo': 'filetes casi negros',
        'cuadros': 182,
        'que': 'la orden de servicio',
        'personaje': '',
        'id': 'xSc21MvjfW',
        'semilla': 424838,
        'prompt': 'Medium close shot, straight on and slightly from above, of a small stack of plain LIGHT GREY printed forms lying on a desk, the top sheet a service order filled with abstract grey bars arranged in three columns standing in for rows of typed entries, with a wider solid grey band across its lower third. The bars and the band are SOLID FLAT GREY and contain absolutely nothing inside them. THE DESK SURFACE IS A PERFECTLY UNIFORM FLAT MID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not wood grain, with no mottling, no speckle, no veining, no blotches and no pattern of any kind. A DARK GREY desk edge and the shadow under the stack anchor the bottom of the frame. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the desk edge and the shadow under the stack, mid grey across the desk surface, light only on the forms. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no signature, no stamp, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf16_cuaderno_teresa': {
        'ranura': 'historico',
        'motivo': 'se repitio con las dos paginas llenas de renglones',
        'cuadros': 201,
        'que': 'el cuaderno de cuentas de Teresa',
        'personaje': '',
        'id': 'lJMGAsjgv9',
        'semilla': 213682,
        'prompt': 'Close overhead shot of a plain ruled accounts notebook lying open on a bare grey worktop, both pages covered in faint illegible grey bars arranged in columns, the last column running on without a closing line. Nothing else in frame. No hands, no people. Flat even light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no figures, no currency symbols, no logos — the content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
}



def revisar():
    """Integridad del archivo. No juzga los prompts, solo el registro."""
    fallos = []
    if len(PLACAS) != 27:
        fallos.append('hay %d placas en linea, se esperaban 27' % len(PLACAS))
    if len(DESCARTADAS) != 19:
        fallos.append('hay %d descartadas, se esperaban 19' % len(DESCARTADAS))
    for campo in ('id', 'ranura'):
        v = [p[campo] for p in PLACAS.values()]
        if len(set(v)) != len(v):
            fallos.append('hay %s repetidos' % campo)
    for n, v in PLACAS.items():
        if 'no legible text' not in v['prompt']:
            fallos.append('%s no pide placa limpia' % n)
        if v['personaje'] and 'saturation no higher' not in v['prompt']:
            fallos.append('%s tiene figura y no pide la piel con numero' % n)
    # las placas en linea mas las tres graficas tienen que dar el bloque
    # entero de ranuras de montar_p3c3.py: 6100 cuadros
    total = sum(v['cuadros'] for v in PLACAS.values()) + sum(GRAFICAS.values())
    if total != 6100:
        fallos.append('los cuadros suman %d y el bloque de ranuras es 6100'
                      % total)
    ran = sorted(int(v['ranura'][1:]) for v in PLACAS.values())
    ran += [int(k[1:]) for k in GRAFICAS]
    if sorted(ran) != list(range(1, 31)):
        fallos.append('las ranuras no son r01..r30 sin huecos')
    return fallos


def deuda():
    """Lo que estas placas NO llevaban, y que por eso hubo que arreglar
    despues con piel.py y acentos.py.

    Ninguna de las siete placas con figura de la PRIMERA tanda pidio la piel
    con numero: el prompt decia 'desaturated warm grey range, barely tinted' y
    el modelo lo leyo como cafe. De ahi salio piel.py. Las placas nuevas si la
    llevan, y por eso esta lista deberia venir vacia para PLACAS y llena para
    DESCARTADAS.
    """
    return ([n for n, v in sorted(PLACAS.items())
             if v['personaje'] and 'saturation no higher' not in v['prompt']],
            [n for n, v in sorted(DESCARTADAS.items())
             if v['personaje'] and 'saturation no higher' not in v['prompt']])


if __name__ == '__main__':
    for n, v in sorted(PLACAS.items(), key=lambda x: int(x[1]['ranura'][1:])):
        print('%-4s %-28s %-9s %7s  %4d cuadros  %5d car%s' % (
            v['ranura'], n, v['personaje'] or '-', v['semilla'],
            v['cuadros'], len(v['prompt']),
            '  (2a version)' if v.get('repetida') else ''))
    print()
    print('%d placas en linea, %d descartadas, %d cuadros horneados' % (
        len(PLACAS), len(DESCARTADAS),
        sum(v['cuadros'] for v in PLACAS.values())))
    f = revisar()
    print('REVISION:', 'sin fallos' if not f else '')
    for x in f:
        print('   ', x)
    a, b = deuda()
    print('sin piel con numero: en linea %s, descartadas %d' % (a or 'ninguna',
                                                                len(b)))
