# -*- coding: utf-8 -*-
"""Las 28 placas del PRIORIDAD 03 Caso 3 (Ruta del Golfo), con el prompt
literal, la semilla y el identificador de Magnific de cada una.

POR QUE EXISTE ESTE ARCHIVO
    El Caso 1 guardo sus prompts; el Caso 3 no. Se recuperaron del historial
    de Magnific y se amarraron a los archivos por medicion, no por memoria:
    correlacion normalizada de luminancia entre cada PNG crudo de
    01 PLANOS/_crudo_*.png y la vista previa de 1024 px de cada candidato.
    Las 28 dieron 1.0000 con un unico ganador y el segundo lugar por debajo
    de 0.84. El primer intento, hecho contra la miniatura de 400x400, dio
    tres parejas equivocadas (kf05, kf07, kf14): la miniatura es un recorte
    CUADRADO de un cuadro 16:9 y la correlacion se midio sobre otra imagen.
    Si alguna vez hay que repetir esto: la vista previa, nunca la miniatura,
    y contra el crudo, nunca contra la placa ya graduada.

LA DIFERENCIA CON placas_p3c1.py
    Alli el prompt se armaba de constantes (ESTILO + TOKEN + escena +
    NEGATIVO) y el archivo las guarda por separado. Aqui no: el bloque de
    estilo fue corrigiendose placa por placa durante la jornada, asi que
    factorizarlo mentiria sobre lo que de verdad se envio. Lo que queda es
    el prompt entero de cada una. Lo que SI es comun va mas abajo, en
    CLAUSULAS, y eso es lo que hay que reusar en los casos 4 y 5.

MODELO
    seedream-5-pro, 2560x1440, resolucion 2k, 100 creditos por placa.
    28 placas = 2.800 creditos. Las que se repitieron no estan aqui; solo
    la version que quedo en 01 PLANOS.

LAS TRES REGLAS QUE ESTE CASO DEJO
    1. El tono plano. Una placa falla cuando un solo tono plano llena el
       cuadro. El modelo INVENTA textura en cualquier superficie grande y
       vacia, y la clausula de "perfectamente uniforme" tiene que nombrar
       TODAS las superficies grandes, no solo la que fallo la vez pasada.
       cama_cajon fallo dos veces con una pared en camuflaje; la tercera
       salio al encuadrar el cajon tan cerca que ya no quedaba pared
       (razon 4.99 -> 1.13). El tinte perdona el grano, no un patron: un
       46 % de azul esconde grano sub-pixel y no esconde un laberinto de
       20 px.
    2. El acento. El tono no separa el acento de la piel (la panoleta de
       Marta a 25.7 grados, su piel a 13.2). La saturacion si: acento
       0.50-1.00, piel 0.30-0.40. Ver acentos.py.
    3. La piel. Decir "grey" no basta; hay que dar el numero. La clausula
       que funciona esta abajo en CLAUSULAS['piel'] y es la que hay que
       pegar en toda placa con figura de aqui en adelante.

LAS TRES RANURAS QUE NO SON PLACA
    La linea tiene 31 ranuras y aqui hay 28. r03, r22 y r29 no son placa:
    son las tres graficas de motion de graficas_p3c3.py (la_ruta 168,
    antes_y_despues 358, los_recursos 176).

LO QUE NO SE ILUSTRA
    Ninguna placa muestra un encuentro, una retencion, una agresion ni una
    amenaza en acto, y ningun viajero esta individualizado salvo kf12, que
    quedo marcado para revision de Sebastian. Es la regla heredada de la
    biblia SRPA.
"""

CLAUSULAS = {
    'piel': (
        'Skin is a desaturated warm grey: hue around 25 degrees and '
        'saturation no higher than 0.20. It must read as grey with a faint '
        'warm tint, never as brown and never as a saturated skin colour.'),
    'tonos': (
        'The frame must have three clearly separate tonal zones: deep dark, '
        'mid grey and light. No large area of near-black and no large area '
        'of near-white anywhere.'),
    'planos': (
        'EVERY LARGE SURFACE IN THIS IMAGE IS A PERFECTLY UNIFORM FLAT AREA '
        'OF SOLID GREY, plain and smooth: not stone, not marble, not '
        'granite, not concrete, not plaster texture, not wallpaper, with no '
        'mottling, no speckle, no veining, no blotches, no camouflage, no '
        'maze pattern, no grain, no noise and no pattern of any kind.'),
    'limpia': (
        'Clean plate: no legible text, no lettering, no numbers, no '
        'signage, no labels, no logos, no emblem.'),
    'negativo': (
        'Not a photograph, not a 3D render, not painterly. No ink outlines, '
        'no multicolour gradients, no paper grain, no brush texture, no '
        'childish or cartoon-mascot styling.'),
}

MODELO = {'mode': 'seedream-5-pro', 'width': 2560, 'height': 1440,
          'resolution': '2k', 'creditos': 100}

# las tres ranuras que no son placa, de graficas_p3c3.py
GRAFICAS = {'r03': 168, 'r22': 358, 'r29': 176}

# nombre -> ranura, cuadros horneados, que es, personaje, id, semilla, prompt
PLACAS = {
    'kf01_terminal_vehiculo': {
        'ranura': 'r02',
        'cuadros': 243,
        'que': 'la van esperando en la terminal',
        'personaje': '',
        'id': 'u5i7jhxQLD',
        'semilla': 886543,
        'prompt': 'Wide shot of a plain passenger van parked and waiting at the kerb outside an intercity bus terminal, seen from the side, doors closed. Bare grey concourse behind with plain columns and empty benches. Overcast daytime, flat even light. Completely empty: no people, no other vehicles, no signage.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no number plate.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
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
    'kf03_luis_computador': {
        'ranura': 'r05',
        'cuadros': 178,
        'que': 'Luis en el escritorio',
        'personaje': 'LUIS',
        'id': 'huysKsivqL',
        'semilla': 525702,
        'prompt': 'Medium shot, waist up, of LUIS seated at a plain desk in a bare grey interior, one hand resting beside a plain laptop whose screen is blank grey, looking down at it. LUIS is a man of about thirty-five, medium build, medium height, short dark hair neatly combed, wearing a plain mid-grey collared shirt over plain grey trousers, with a plain institutional yellow band running down the front placket of the shirt. Composed, withheld expression. The desk is otherwise empty. No other person in frame, nothing written or displayed anywhere.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, readable at a glance, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted, never a saturated skin tone. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The yellow band is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf04_marta_giros': {
        'ranura': 'r06',
        'cuadros': 167,
        'que': 'Marta en la oficina de giros',
        'personaje': 'MARTA',
        'id': 'ksn6JVb16B',
        'semilla': 127285,
        'prompt': 'Medium shot of MARTA standing at the counter of a small money-transfer office, seen from the side, one hand flat on the counter. MARTA is a woman of about thirty-five, medium build, medium height, dark hair tied back, wearing a plain light grey blouse over plain grey trousers, with a plain institutional yellow scarf knotted at the neck. Composed, withheld expression, not smiling. Plain grey counter and plain grey partition behind, nothing on the counter. No clerk, no other person in frame, no forms, no notices, no money visible.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive, but simplified and graphic: clearly defined eyes with brow, a simple nose and a simple mouth, no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The yellow scarf is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf05_omar_volante': {
        'ranura': 'r09',
        'cuadros': 150,
        'que': 'Omar al volante de la van',
        'personaje': 'OMAR',
        'id': 'aF4UheIfSh',
        'semilla': 725866,
        'prompt': 'Medium shot from outside the open driver window of a plain MID GREY van, looking slightly down at OMAR behind the wheel, his whole torso clearly visible and unobstructed, both hands low on the steering wheel so that NOTHING crosses his chest. OMAR is a man of about forty, stocky, medium height, short dark hair and a close-trimmed moustache, wearing a plain MID GREY work shirt over plain grey trousers, with A WIDE PLAIN INSTITUTIONAL YELLOW BAND RUNNING STRAIGHT ACROSS THE CHEST OF THE WORK SHIRT FROM ONE SIDE SEAM TO THE OTHER, horizontal, continuous, fully visible end to end, unbroken and not covered by his arms. The band is a flat uniform area of solid colour with no pattern, no emblem, no lettering and no marking of any kind. He looks ahead through the windscreen, calm and ordinary, nothing menacing. The DARK GREY van door and window frame surround him; the sky beyond the windscreen is light. No other person in frame, no cargo, no passengers.\n\nThe frame must have three clearly separate tonal zones: deep dark in the van door and the cab interior, mid grey across his shirt and the van body, light only in the windscreen and the sky beyond. No large area of near-white anywhere.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no plate number, no logos, no brand name on the van.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading.',
    },
    'kf06_teresa_cocina': {
        'ranura': 'r10',
        'cuadros': 223,
        'que': 'Teresa en la cocina de la pension',
        'personaje': 'TERESA',
        'id': 'Eb6wgP7uuO',
        'semilla': 774546,
        'prompt': 'Medium wide shot of TERESA standing in the plain kitchen of a modest lodging house, one hand on the edge of a bare worktop, facing camera. TERESA is a woman of about forty-five, medium build, dark hair tied back, wearing a plain institutional blue apron over a plain light grey blouse and plain grey trousers. Settled, matter-of-fact expression. Behind her a plain grey worktop with two unlabelled pots and a stack of plain plates. No other person in frame, no food, no packaging, no notices.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The blue apron is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf07_certificado_empleo': {
        'ranura': 'r13',
        'cuadros': 229,
        'que': 'el certificado de empleo',
        'personaje': '',
        'id': 'nVqfGhiYQD',
        'semilla': 414940,
        'prompt': 'Medium close shot, straight on and slightly from above, of a single plain LIGHT GREY employment certificate lying on a desk, the sheet occupying the middle of the frame. The sheet carries a short block of abstract grey bars standing in for lines of text and a plain empty rectangle near its lower right corner standing in for a seal: the bars and the rectangle are SOLID FLAT GREY and contain absolutely nothing inside them. THE DESK SURFACE IS A PERFECTLY UNIFORM FLAT MID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not wood grain, with no mottling, no speckle, no veining, no blotches and no pattern of any kind. A DARK GREY desk edge and its shadow run along the bottom of the frame. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the desk edge and the shadow under it, mid grey across the desk surface, light only on the sheet. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no signature, no stamp impression, no logos, no coat of arms, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf08_nidia_local': {
        'ranura': 'r15',
        'cuadros': 210,
        'que': 'Nidia detras del mostrador',
        'personaje': 'NIDIA',
        'id': 'MBxFuF3DCm',
        'semilla': 237277,
        'prompt': 'Medium shot of NIDIA standing behind the plain counter of a very small street-front office, both hands resting on the counter top, facing camera. NIDIA is a woman of about forty, slim, dark hair worn loose to the shoulders, wearing a plain mid-grey blouse over plain grey trousers, no colour anywhere on her. Composed, withheld expression. Behind her a bare grey wall and a single empty shelf. The counter is empty. No other person in frame, no notices, no posters.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw. Skin stays in a desaturated warm grey range, barely tinted. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf09_pasaportes_recibos': {
        'ranura': 'r16',
        'cuadros': 233,
        'que': 'el cajon con los pasaportes',
        'personaje': '',
        'id': '4RtDVW49Aa',
        'semilla': 220595,
        'prompt': 'Close shot of an open desk drawer seen from slightly above, containing three plain passport booklets stacked loosely and a small pile of plain receipt slips beside them. The drawer interior is bare. No hands, no people. Flat even light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no logos, no coat of arms, no emblem — the passport covers and the slips are blank.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf10_puesto_control': {
        'ranura': 'r18',
        'cuadros': 170,
        'que': 'el puesto de control en la via',
        'personaje': '',
        'id': 'WD5fv1bcXe',
        'semilla': 47454,
        'prompt': 'Wide shot of a small roadside migration control post seen straight on, a plain booth with a raised barrier beside an empty road, a bare grey hut behind. Overcast daytime, flat even light. Completely empty: no officers, no uniforms, no people, no vehicles. Ordinary and neutral, not threatening. No flags, no shields, no signage.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no coat of arms, no emblem of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf11_informe_dos_meses': {
        'ranura': 'r19',
        'cuadros': 197,
        'que': 'el informe de los dos meses',
        'personaje': '',
        'id': '4RtDH3h9Aa',
        'semilla': 698280,
        'prompt': 'Three-quarter angled shot of a desk: a MID GREY desktop with a single LIGHT GREY sheet of a migration response lying on it, its content reduced to faint illegible mid grey bars with one short bar near the top isolated from the rest, and a DARK GREY closed folder lying beside it. A DARK GREY wall fills the upper third of the frame behind the desk. Nothing else. No hands, no people. Flat even light. The frame has three clearly separate tonal zones: dark wall and folder, mid grey desktop, light sheet.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no dates, no logos, no coat of arms, no emblem — the content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf12_viajero_documento': {
        'ranura': 'r20',
        'cuadros': 104,
        'que': 'un viajero con su documento',
        'personaje': 'viajero',
        'id': 'rgW3Vzqxtc',
        'semilla': 166847,
        'prompt': 'Medium shot of one of THE FOUR TRAVELLERS, a man of about thirty in plain grey everyday clothes with no colour anywhere, standing against a MID GREY wall and holding out a single plain light grey folded document towards camera at chest height, looking down at it. Composed, matter-of-fact expression. No other person in frame. The document is blank: no printing of any kind on it. The image has a wide tonal range: the wall is mid grey, his clothes are mid to dark grey, only the document is light.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients on the cheek, forehead or jaw, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Skin stays in a desaturated warm grey range, barely tinted. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no stamps, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf13_marta_lejos': {
        'ranura': 'r23',
        'cuadros': 170,
        'que': 'Marta sola y pequena',
        'personaje': 'MARTA',
        'id': '1lYi624r4r',
        'semilla': 183382,
        'prompt': 'Wide shot of MARTA standing alone and small in the middle of a bare grey interior, full figure, arms at her sides, facing camera from a distance. MARTA is a woman of about thirty-five, medium build, dark hair tied back, wearing a plain light grey blouse over plain grey trousers, with a plain institutional yellow scarf knotted at the neck. Composed, withheld expression, not smiling. The room is empty: plain walls, a plain floor, no furniture, no other person in frame.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Faces ARE drawn and expressive but simplified and graphic, with no photographic detail, no skin pores, no individual hair strands, no caricature. Facial surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos. The yellow scarf is a flat uniform area of solid colour with no pattern, no emblem and no marking of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no big round anime eyes, no soft airbrushed skin shading.',
    },
    'kf14_orden_servicio': {
        'ranura': 'r24',
        'cuadros': 182,
        'que': 'la orden de servicio',
        'personaje': '',
        'id': 'xSc21MvjfW',
        'semilla': 424838,
        'prompt': 'Medium close shot, straight on and slightly from above, of a small stack of plain LIGHT GREY printed forms lying on a desk, the top sheet a service order filled with abstract grey bars arranged in three columns standing in for rows of typed entries, with a wider solid grey band across its lower third. The bars and the band are SOLID FLAT GREY and contain absolutely nothing inside them. THE DESK SURFACE IS A PERFECTLY UNIFORM FLAT MID GREY, plain and smooth: not stone, not marble, not granite, not concrete, not wood grain, with no mottling, no speckle, no veining, no blotches and no pattern of any kind. A DARK GREY desk edge and the shadow under the stack anchor the bottom of the frame. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the desk edge and the shadow under the stack, mid grey across the desk surface, light only on the forms. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no signature, no stamp, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf15_conversacion_pantalla': {
        'ranura': 'r26',
        'cuadros': 205,
        'que': 'la conversacion en la pantalla',
        'personaje': '',
        'id': 'lJMGAfkgv9',
        'semilla': 695287,
        'prompt': 'Close shot, straight on, of a plain desktop monitor on a bare grey desk, its screen filled with a long continuous column of faint illegible grey message bars running from top to bottom, suggesting a complete conversation. Nothing else in frame. No hands, no people, no keyboard. Flat even light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no app icons, no logos, no emoji — the screen content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf16_cuaderno_teresa': {
        'ranura': 'r28',
        'cuadros': 201,
        'que': 'el cuaderno de cuentas de Teresa',
        'personaje': '',
        'id': 'lJMGAsjgv9',
        'semilla': 213682,
        'prompt': 'Close overhead shot of a plain ruled accounts notebook lying open on a bare grey worktop, both pages covered in faint illegible grey bars arranged in columns, the last column running on without a closing line. Nothing else in frame. No hands, no people. Flat even light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no figures, no currency symbols, no logos — the content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'kf17_dos_viajeros_se_van': {
        'ranura': 'r30',
        'cuadros': 177,
        'que': 'dos viajeros que se van',
        'personaje': '',
        'id': 'XmgKKm1Bfo',
        'semilla': 572396,
        'prompt': 'Wide shot from behind of TWO TRAVELLERS walking away from camera down an empty road, each carrying a small plain grey backpack, already some distance off. A man and a woman of about thirty in plain grey everyday clothes, no colour anywhere on either of them. No faces visible. Bare grey roadside, overcast flat light, no other person in frame, no vehicles, no signage.\n\nStylized editorial character illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. Skin stays in a desaturated warm grey range, barely tinted. Figures are 8 to 8.5 heads tall. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling, no soft airbrushed skin shading.',
    },
    'cama_calle_medellin': {
        'ranura': 'r01',
        'cuadros': 202,
        'que': 'la calle de Medellin al amanecer',
        'personaje': '',
        'id': '9ZmpYjgNYZ',
        'semilla': 371830,
        'prompt': 'Wide establishing shot of an ordinary street on the edge of Medellín at first light, seen straight on. Modest low rendered buildings with plain frames and plain doors, a narrow pavement, a kerb, hills faintly visible behind. Overcast, flat even light. The street is empty: no people, no vehicles. Ordinary and unremarkable, not sinister, not derelict. No window bars, no grilles, no padlocks.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_sello_sin_fecha': {
        'ranura': 'r07',
        'cuadros': 178,
        'que': 'el sello sin fecha',
        'personaje': '',
        'id': 'aF4gGhwfSh',
        'semilla': 659732,
        'prompt': 'Three-quarter angled shot of a desk corner: a MID GREY desktop with eleven small printed screenshots laid out across it in a loose grid, each one a LIGHT GREY rectangle with faint illegible mid grey bars suggesting lines of a chat conversation, some sitting slightly askew. A DARK GREY desk edge runs along the bottom of the frame and a DARK GREY wall fills the upper third behind the desk. Nothing else. No hands, no people, no device. Flat even light. The frame has three clearly separate tonal zones: dark wall and desk edge, mid grey desktop, light screenshots.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no dates, no logos, no emoji — the marks on the screenshots are abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_mesa_equipo': {
        'ranura': 'r08',
        'cuadros': 237,
        'que': 'la mesa del equipo',
        'personaje': '',
        'id': 'nVqvKA2YQD',
        'semilla': 777749,
        'prompt': 'Overhead shot looking straight down at a DARK GREY institutional meeting table in a bare grey office, with four empty chairs tucked in around it, a closed plain light grey folder and a plain pen set at each place. The table is otherwise bare. The floor around it is mid grey. Completely empty: no people, no hands. Flat even overhead light. The image has a wide tonal range: deep dark greys in the table and the chairs, mid greys in the floor, light greys only in the folders.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no emblem of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_tienda_esquina': {
        'ranura': 'r11',
        'cuadros': 257,
        'que': 'la tienda de la esquina',
        'personaje': '',
        'id': 'u5i7S3TQLD',
        'semilla': 208431,
        'prompt': 'Medium wide shot of the counter of a small neighbourhood corner shop seen from the customer side, plain grey shelving behind holding unlabelled packages, a bare counter with two unlabelled grocery packets on it. Completely empty: no shopkeeper, no customer, no people. Flat even light. No price labels, no packaging text, no notices.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
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
    'cama_visado': {
        'ranura': 'r14',
        'cuadros': 228,
        'que': 'el pasaporte abierto en el visado',
        'personaje': '',
        'id': 'YMbEp4DWeC',
        'semilla': 171596,
        'prompt': 'Close shot, from above and slightly to the side, of a plain LIGHT GREY passport lying open on a desk at its visa page, the booklet occupying the middle of the frame. The visa page carries a plain empty rectangle and a few short abstract grey bars standing in for printed fields: they are SOLID FLAT GREY and contain absolutely nothing inside them. THE DESK SURFACE IS A PERFECTLY UNIFORM FLAT MID GREY, plain and smooth: not stone, not marble, not wood grain, with no mottling, no speckle and no pattern of any kind. A DARK GREY desk edge and the shadow under the booklet anchor the lower part of the frame. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the desk edge and the shadow under the booklet, mid grey across the desk surface, light only on the open pages. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no photograph, no face, no stamp impression, no logos, no coat of arms, no emblem, no national insignia of any country.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_cajon': {
        'ranura': 'r17',
        'cuadros': 101,
        'que': 'el cajon vacio',
        'personaje': '',
        'id': 'eIskC6vdqL',
        'semilla': 869065,
        'prompt': 'Very close shot of one open drawer of a DARK GREY metal filing cabinet, the drawer filling most of the frame, seen straight on and slightly from above. The drawer is pulled fully out and is COMPLETELY EMPTY: nothing inside it, no papers, no folders, no documents, only the plain flat LIGHT GREY empty interior and its dark inner shadow. The dark grey cabinet front and the dark grey drawer face frame the shot on all sides, leaving almost no background visible. No hands, no fingers, no people. Flat even light.\n\nThe frame must have three clearly separate tonal zones: deep dark in the cabinet front and the inner shadow, mid grey across the drawer face, light only on the empty drawer interior. No large area of near-black and no large area of near-white anywhere. NO LARGE EMPTY BACKGROUND SURFACE AT ALL: the cabinet fills the frame edge to edge.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Every surface is a perfectly uniform flat area of solid grey meeting the next at a hard edge, smooth and plain: no mottling, no speckle, no veining, no blotches, no camouflage, no maze pattern, no grain, no noise and no pattern of any kind anywhere in the image. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no labels, no signage, no logos, no emblem.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_sala_reunion': {
        'ranura': 'r21',
        'cuadros': 173,
        'que': 'la sala de reunion vacia',
        'personaje': '',
        'id': '5jG94j2Kxe',
        'semilla': 157984,
        'prompt': 'Wide shot of a plain institutional meeting room seen straight on from one end, a long bare table with empty chairs along both sides, a blank grey wall panel at the far end, plain grey walls. Completely empty: no people, no uniforms. Flat even overhead light. No whiteboard writing, no posters, no flags.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos, no coat of arms, no emblem of any kind.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_telefono_omar': {
        'ranura': 'r25',
        'cuadros': 174,
        'que': 'el telefono de Omar, solo',
        'personaje': '',
        'id': 'N2heC7F6D9',
        'semilla': 321566,
        'prompt': 'Close overhead shot of a plain dark grey mobile phone lying face up and alone on a MID GREY desk, its screen a light grey rectangle with two faint illegible mid grey message bars on it. The phone fills about a third of the frame, with the desk visible around it on all sides. No hands, no people. Flat even light. The image has a wide tonal range: the phone body is deep dark grey, the desk is mid grey, only the screen is light.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: absolutely no legible text, no readable lettering, no numbers, no app icons, no logos, no emoji — the screen content is abstract grey bars only.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_pantalla': {
        'ranura': 'r27',
        'cuadros': 184,
        'que': 'el monitor de lado',
        'personaje': '',
        'id': 'N2hBzcX6D9',
        'semilla': 207172,
        'prompt': 'Wide shot of an empty office desk seen from the side and slightly behind, with a plain DARK GREY computer monitor turned three quarters away from camera so only the edge of its LIGHT GREY screen is visible, its pale light falling on the MID GREY wall beside it. An empty chair is pushed back from the desk. The desk surface is mid grey and bare except for a closed plain notebook. The foreground floor and the near edge of the desk are dark grey. Completely empty: no people, no hands. Flat even light. Ordinary and quiet.\n\nThe frame must have three clearly separate tonal zones: deep dark in the monitor body, the chair and the foreground, mid grey across the wall and the desk, light only on the visible sliver of screen and the patch of wall it lights. No large area of near-black and no large area of near-white anywhere.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients, and every flat area is a perfectly uniform area of solid colour with no grain, no speckle and no noise. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no readable lettering, no numbers, no letters, no words, no icons, no logos, no brand name on the monitor.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
    'cama_carretera_golfo': {
        'ranura': 'r31',
        'cuadros': 153,
        'que': 'la carretera hacia el Golfo',
        'personaje': '',
        'id': 'nVqvvv5YQD',
        'semilla': 64859,
        'prompt': 'Wide shot of an empty two-lane road running away from camera towards the Gulf of Urabá, flat low scrub on both sides and a faint line of sea and sky at the horizon. Overcast daytime, flat even light. Completely empty: no people, no vehicles, no buildings, no signage. Ordinary and quiet, not desolate.\n\nStylized editorial illustration, flat graphic treatment. No ink outline anywhere: forms are built from broad soft tonal planes, never from rendered shading, never from texture or brush marks. Surfaces are built from FLAT tonal planes meeting at hard edges, never from soft airbrushed gradients. The environment is entirely in greys. Flat even light, static camera, perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible text, no lettering, no numbers, no signage, no logos.\n\nNot a photograph, not a 3D render, not painterly. No ink outlines, no multicolour gradients, no paper grain, no brush texture, no childish or cartoon-mascot styling.',
    },
}


def revisar():
    """Integridad del archivo. No juzga los prompts, solo el registro."""
    fallos = []
    if len(PLACAS) != 28:
        fallos.append('hay %d placas, se esperaban 28' % len(PLACAS))
    for campo in ('id', 'ranura'):
        v = [p[campo] for p in PLACAS.values()]
        if len(set(v)) != len(v):
            fallos.append('hay %s repetidos' % campo)
    for n, v in PLACAS.items():
        if 'no legible text' not in v['prompt']:
            fallos.append('%s no pide placa limpia' % n)
        if not v['prompt'].strip().startswith(('Wide', 'Medium', 'Close',
                                               'Overhead', 'Three', 'Very')):
            fallos.append('%s no empieza por el encuadre' % n)
    # las 28 placas mas las tres graficas tienen que dar el bloque de
    # ranuras entero de montar_p3c3.py: N_RANURAS = 6100
    total = sum(v['cuadros'] for v in PLACAS.values()) + sum(GRAFICAS.values())
    if total != 6100:
        fallos.append('los cuadros suman %d y el bloque de ranuras es 6100'
                      % total)
    return fallos


def deuda():
    """Lo que estas placas NO llevaban, y que por eso hubo que arreglar
    despues con piel.py y acentos.py.

    Ninguna de las siete placas con figura pidio la piel con numero: el
    prompt decia 'desaturated warm grey range, barely tinted' y el modelo
    lo leyo como cafe. Medido: tono 0-26, saturacion 0.29-0.33, valor
    0.18-0.38, contra 12-34 / 0.16-0.28 / 0.40-0.71 del Caso 2 aprobado.
    De ahi salio piel.py y de ahi sale CLAUSULAS['piel'].

    En los casos 4 y 5 la clausula va en el prompt y no hace falta la LUT.
    Esta funcion existe para que eso no se olvide.
    """
    return [n for n, v in sorted(PLACAS.items())
            if v['personaje'] and 'saturation no higher' not in v['prompt']]


if __name__ == '__main__':
    for n, v in sorted(PLACAS.items(), key=lambda x: int(x[1]['ranura'][1:])):
        print('%-4s %-28s %-9s %7s  %4d cuadros  %5d car' % (
            v['ranura'], n, v['personaje'] or '-', v['semilla'],
            v['cuadros'], len(v['prompt'])))
    print()
    print('%d placas, %d creditos, %d cuadros horneados' % (
        len(PLACAS), len(PLACAS) * MODELO['creditos'],
        sum(v['cuadros'] for v in PLACAS.values())))
    f = revisar()
    print('REVISION:', 'sin fallos' if not f else '')
    for x in f:
        print('   ', x)
    d = deuda()
    print('SIN CLAUSULA DE PIEL CON NUMERO (%d de %d con figura):' % (
        len(d), sum(1 for v in PLACAS.values() if v['personaje'])))
    print('   ', ', '.join(d) if d else 'ninguna')
