# -*- coding: utf-8 -*-
r"""EL PLAN DE MOVIMIENTO del caso Miriam y Mariana: veinte ranuras.

LA REGLA DE SELECCION, QUE ES DE SEBASTIAN
    «haz algunOS MOTIONS MAS DONDE VEAS QUE NO PASA NADA Y QUE N HAYAN
    PERSONAS O MANOS».

    Asi que entran las ranuras SIN GENTE Y SIN MANOS, y solo esas. En un
    plano con una cara o una mano el modelo de video inventa un gesto, y un
    gesto inventado en un caso de desaparicion forzada es exactamente lo que
    la biblia prohibe. Veinte de cincuenta y siete cumplen.

LA ANCLA CONTRA LA DEFORMACION
    «monta la linea de tiempo y en otro canal motion usando key inicla y
    final, pide que no distorsione nada».

    La MISMA placa graduada va de cuadro inicial Y de cuadro final. El clip
    sale y vuelve al mismo sitio, asi que:
      - no hay deriva: lo que se mueve tiene que regresar,
      - la entrada y la salida del clip en la linea son invisibles, porque el
        primer y el ultimo cuadro de V2 son el cuadro de V1,
      - y la pista se prende y se apaga sin que nada salte.

    El clip cubre la ranura COMPLETA, no un pedazo: asi V2 es un reemplazo
    limpio de V1 y la comparacion A/B es honesta.

LOS ELEMENTOS SUELTOS
    «PUEDES AGREGAR COSAS SUTILES COMO PASA UN AVION, PASA UN PERRO, NO SE
    COSAS ASI RANDOM PARA DARLE UINA SENACION MAS DE ANIMACION».

    Solo en EXTERIORES, y solo lejos: un perro que cruza al fondo de la
    cuadra, un avion alto, un pajaro. En los planos de mesa -documentos,
    carpetas, la bandeja- no entra nada nuevo al cuadro: ahi lo unico que
    se mueve es la luz y una corriente de aire. Un papel de prueba con algo
    nuevo encima deja de ser una prueba.

EL MODELO
    Kling 3.0 a 1080p, 90 creditos por segundo, hasta quince segundos, con
    cuadro inicial y final. Kling 4.0 existe y tambien los soporta, pero
    cuesta 280 por segundo -tres veces- y aqui no hay nada que justifique
    el salto: lo que pedimos es una brisa, no una coreografia.
"""

# El bloque que va al final de CADA prompt de movimiento.
#
# TRES PRUEBAS SOBRE LA MISMA RANURA, Y LO QUE DIJO CADA UNA
#     Todas sobre C1 r03 «la casa cerrada», midiendo la diferencia media
#     entre cuadros repartidos del clip.
#
#     1. Cuadro inicial Y final, con la clausula dura
#        -«No object appears and no object disappears»-:
#        ancla perfecta (primer vs ultimo cuadro: 0,68 niveles) y CERO
#        movimiento (0,2-0,3 entre cuadros). El perro no aparecio nunca.
#        La clausula prohibia exactamente lo que Sebastian pidio.
#
#     2. Cuadro inicial Y final, con la clausula acotada a lo que ya esta
#        en el cuadro: ancla perfecta (0,58) y SIGUE SIN MOVERSE (0,2-0,4).
#        O sea que no era la clausula: es el ancla. Entre A y A el camino
#        mas corto es quedarse en A, y el modelo se queda.
#
#     3. SOLO cuadro inicial: el perro cruza, el polvo se ve, hay pieza.
#        Y aparecio el problema de verdad: LA VENTANA SE CONVIRTIO EN UNA
#        CORTINA que crece hasta colgar fuera del muro. Yo habia pedido
#        «the thin curtain behind the window stirs» y en la placa no hay
#        ninguna cortina, asi que el modelo la fabrico sacandola de la
#        ventana.
#
# LA REGLA QUE SALE DE AHI
#     El movimiento se pide SOLO de dos clases de cosa:
#       a) algo que YA ESTA en la placa y puede moverse sin dejar de ser lo
#          que es -pasto, una cuerda, la esquina de un papel, la luz-;
#       b) algo pequeno y claramente aparte que CRUZA y se va -un perro,
#          un pajaro, la luz de un avion, una hoja seca-.
#     Nunca algo que haya que HACER CRECER de un objeto solido que ya esta:
#     pedirle a una ventana que tenga cortina es pedirle que se deforme.
#
# LA SEGUNDA LECCION, MIRANDO LOS VEINTE CLIPS
#     Trece salieron bien a la primera. Los siete que no, fallaron casi
#     todos por lo mismo: YO LE PEDI AL PAPEL QUE SE MOVIERA.
#
#     «one corner lifts slightly in a draught and settles» devuelve una
#     hoja que se levanta entera y queda vertical (C3 r09), dos hojas que
#     aletean y cambian de sitio (C5 r02), un cartel que se tuerce (C2
#     r04). El papel es demasiado facil de animar: cualquier permiso se
#     convierte en un aleteo, y en un plano de prueba documental una hoja
#     que se mueve sola deja de ser una prueba.
#
#     Entonces en los planos de mesa y de documento NO SE MUEVE EL PAPEL.
#     Se mueve la luz, y nada mas. Un documento inmovil mientras la luz
#     cruza es ademas mas exacto para lo que el plano afirma.
#
#     Los otros tres: la ventana encendida se apagaba (C1 r12), una hoja
#     seca llegaba hasta el telefono y parecia un pajaro (C2 r06), las
#     alturas de los picos del perfil cambiaban (C5 r09) y una SOMBRA DE
#     PERSONA cruzaba el tablero (C5 r11). Los cuatro se cierran nombrando
#     lo que tiene que quedarse quieto.
#
# Y EL ANCLA DE SALIDA SE RESUELVE EN EL MONTAJE, NO EN EL MODELO
#     Sin cuadro final el ultimo cuadro ya no es la placa. No importa: el
#     clip va en V2 ENCIMA de la placa horneada de V1, con disolvencia de
#     doce cuadros a la entrada y a la salida. V1 asoma por debajo en los
#     dos bordes y no hay salto, venga el clip como venga. Es la misma
#     razon por la que el movimiento va en pista aparte: para que un clip
#     flojo nunca pueda tumbar la pieza.
QUIETO = (
    'The camera DOES NOT MOVE: no pan, no tilt, no zoom, no dolly, no '
    'handheld drift, no parallax. '
    'EVERYTHING ALREADY STANDING IN THIS FRAME -every wall, door, window, '
    'surface, object and piece of ground- keeps its exact shape, size, '
    'position and identity from the first frame to the last. None of it '
    'morphs, warps, stretches, melts, ripples, grows, shrinks or slides '
    'across the frame. NOTHING NEW GROWS OUT OF ANY OBJECT ALREADY IN THE '
    'PICTURE: no cloth, no curtain, no smoke, no flag and no shape of any '
    'kind unfolds, hangs, spills or emerges from a wall, a window, a door, '
    'an opening or any other solid thing. '
    'THE MOVEMENT DESCRIBED ABOVE IS THE ONLY MOVEMENT, and it IS clearly '
    'visible: it really happens on screen, unhurried and small in the frame, '
    'and apart from it nothing else enters or leaves. '
    'No text, no number, no letter, no logo and no marking appears anywhere '
    'at any point. No face, no hand and no human figure enters the frame at '
    'any point, AND NO SHADOW OF A PERSON falls into the frame or moves '
    'across any surface in it. '
    'The style, the grey palette and the flat graphic treatment stay exactly '
    'as in the given frame for the whole clip.')

# Disolvencia de entrada y de salida del clip de V2 sobre la placa de V1.
MEZCLA = 12

# (capitulo, ranura): (cuadros, movimiento)
MOV = {
 (1, 2): (158,
    'Her two hands work at the griddle in a small, slow, ordinary rhythm: the '
    'right hand slides one flat arepa a few centimetres across the griddle and '
    'presses it lightly, the left hand rests on the counter and stays there. '
    'No steam and no smoke rises from the griddle. HER HEAD, FACE, '
    'EYES AND EXPRESSION DO NOT CHANGE: no blink, no turn, no smile, no '
    'change of gaze. Her body stays exactly where it is.'),
 (1, 6): (168,
    'A thin, low drift of dust moves slowly along the ground of the street '
    'from left to right, close to the pavement, and fades. High above the far '
    'bright end of the street a bank of cloud moves slowly across, and as it '
    'passes the light at the far end softens slightly and then returns. THE '
    'THREE DARK FIGURES DO NOT MOVE AT ALL: not a step, not a turn, not a '
    'gesture, no limb shifts; they stay exactly as they are, flat dark shapes '
    'with no features.'),
 (1, 10): (120,
    'High above, a single small aircraft light crosses the dark sky very '
    'slowly from left to right and leaves the frame. The weak scatter of '
    'windows at the edge of town flickers once and stays lit. The small far '
    'figure on the road keeps walking away at the same slow steady pace, '
    'upright, no detail visible, and does not grow or shrink noticeably. '
    'Nothing else moves and nothing appears on the road.'),
 (1, 3): (145,
    'A few specks of dust drift slowly across the bright doorway. A DOG walks '
    'across the lit doorway, left to right, and out of the picture: small, '
    'unhurried, a dark shape against the light. The closed door, the window '
    'and the walls do not move and nothing hangs from them.'),
 (1, 8): (108,
    'The light on the open cash box shifts slightly and comes back. The tipped-'
    'back lid does not move. The box stays empty: no coin, no note, no object '
    'appears in any compartment.'),
 (1, 12): (196,
    'The light in the one lit window dims very slightly and comes back, as if someone had crossed the room far away: IT NEVER GOES OUT and the window stays clearly lit for the whole clip. A MOTH crosses the lit rectangle once. Down at the far end of the street a DOG walks slowly across and out of frame, very small. Every other window stays dark, the street stays empty, and the window openings stay exactly as they are: nothing hangs out of any of them.'),
 (1, 17): (118,
    'The tied-down awnings of the three closed stalls lift and fall slightly in '
    'the dawn wind. The dawn light grows a little and settles. A bird crosses '
    'high above the row of facades. The stalls stay closed and the tipped stools '
    'do not move.'),
 (2, 4): (151,
    'The light across the post and the taped sheet shifts slowly, as if a cloud were passing, and comes back. THE PAPER ITSELF DOES NOT MOVE AT ALL: no sheet, page, card, form or document lifts, flutters, curls, flaps, turns, slides or changes its position or angle by any amount. Only the light moves. The sheet stays taped flat against the post at exactly the same angle, the same size and the same place, and the grey rectangle and the grey bars on it never change.'),
 (2, 6): (254,
    'The pool of lamplight on the pavement wavers very slightly, as if the lamp above were swinging a little, and comes back. NOTHING CROSSES THE PAVEMENT: no leaf, no paper, no bird, no animal and no object of any kind enters the frame or passes near the phone. The phone does not move, is not touched, does not slide and its screen stays completely black.'),
 (2, 9): (136,
    'The light across both sheets shifts very slowly and comes back. One corner '
    'of each sheet lifts slightly in a draught and settles. The two forms stay '
    'where they are, stay the same size as each other and nothing is written on '
    'them.'),
 (3, 4): (214,
    'The light along the corridor floor shifts slowly and comes back. One of the '
    'loose sheets lifts at the corner in a draught and settles again without '
    'sliding away. The box does not move and no further sheet comes out of it.'),
 (3, 7): (179,
    'The light across the table shifts very slowly and comes back, so the clean '
    'bands of empty table between the three folders brighten and darken '
    'together. The three folders stay closed, stay squared up and stay exactly '
    'where they are.'),
 (3, 9): (146,
    'The weak light on the table top wavers very slightly and comes back, so the shadows under the two folders shift a little. THE PAPER ITSELF DOES NOT MOVE AT ALL: no sheet, page, card, form or document lifts, flutters, curls, flaps, turns, slides or changes its position or angle by any amount. Only the light moves. The open folder stays open at exactly the same angle, its exposed page stays flat, and the closed folder stays closed.'),
 (4, 5): (117,
    'The daylight across the table and the two chairs shifts slowly, as if a '
    'cloud were passing outside, and comes back. A faint draught moves through '
    'the open doorway. The chairs do not move, the jug and the glasses do not '
    'move, and nobody comes through the door.'),
 (5, 2): (233,
    'The light across both documents shifts very slowly and comes back, so the shadow of the upper sheet moves a little across the lower one. THE PAPER ITSELF DOES NOT MOVE AT ALL: no sheet, page, card, form or document lifts, flutters, curls, flaps, turns, slides or changes its position or angle by any amount. Only the light moves. The two sheets stay overlapped exactly as they are, at the same angle and in the same place, and no mark and no number appears on either.'),
 (5, 3): (157,
    'The scrub and the dry grass along the road move in a light night wind. The '
    'weak light at the horizon flickers once. High in the dark sky a single '
    'aircraft light crosses the frame, very small and very slow. The truck stays '
    'parked with its doors closed and its lights off: it does not move, nothing '
    'is loaded onto it and nobody approaches it.'),
 (5, 5): (158,
    'The plain tape between the stakes and the string of the grid vibrate '
    'slightly in the wind. The daylight across the ground shifts and comes back. '
    'A bird crosses high above the open country behind. The earth inside the grid '
    'stays bare and undisturbed: nothing is dug, nothing is uncovered and nothing '
    'appears in any square.'),
 (5, 7): (197,
    'The light across the tray shifts slowly and comes back, so the shadow of the '
    'rim moves a little across the sifted earth. A faint breeze stirs the very '
    'surface of the earth without disturbing the raked layer. The tray stays '
    'empty: no object, no fragment and nothing else appears in it, and the scale '
    'rule does not move.'),
 (5, 9): (199,
    'The light on the bench shifts a little and comes back. THE READOUT ON THE SCREEN DOES NOT CHANGE AT ALL: every peak keeps its exact height, its exact width and its exact place, the number of peaks stays the same, the spacing stays the same, the baseline stays flat and still, and no label, number or colour appears. The screen does not flicker and does not go dark.'),
 (5, 11): (150,
    'The light across the board shifts slowly and comes back, so the small shadows cast BY THE CARDS THEMSELVES move a little. THE PAPER ITSELF DOES NOT MOVE AT ALL: no sheet, page, card, form or document lifts, flutters, curls, flaps, turns, slides or changes its position or angle by any amount. Only the light moves. Every card stays exactly where it is, at the same angle, no line is added or removed, and nothing is written on any card.'),
 (5, 12): (177,
    'The grass and the line of fencing move in a light wind and the plain tape '
    'around each of the three marked patches vibrates slightly. The dusk light '
    'at the horizon dims very slowly and comes back. A bird crosses the far sky. '
    'The three patches stay marked and undisturbed and nothing and nobody moves '
    'on the property.'),
}

FPS = 23.976
MODELO = 'kling-30'
CUADRO_FINAL = False   # ver el encabezado de QUIETO: el ancla congela el clip
RESOLUCION = '1080p'
PROPORCION = '16:9'
CREDITOS_POR_SEGUNDO = 90


def segundos(cuadros):
    """Kling cobra por segundo entero, asi que el clip cubre la ranura
    completa redondeando hacia arriba. Un cuadro de sobra se recorta en la
    linea; un cuadro de menos deja un hueco."""
    import math
    s = int(math.ceil(cuadros / FPS))
    return max(3, min(15, s))


def prompt(cap, ran):
    return MOV[(cap, ran)][1].strip() + '\n\n' + QUIETO


def plan():
    filas = []
    for (cap, ran), (cuad, _) in sorted(MOV.items()):
        s = segundos(cuad)
        filas.append((cap, ran, cuad, s, s * CREDITOS_POR_SEGUNDO))
    return filas


if __name__ == '__main__':
    print('%-4s %-5s %7s %6s %9s' % ('cap', 'ran', 'cuadros', 'seg', 'creditos'))
    tc = ts = 0
    for cap, ran, cuad, s, cr in plan():
        print('%-4d r%02d   %7d %6d %9d' % (cap, ran, cuad, s, cr))
        tc += cr
        ts += s
    print('')
    print('%d clips - %d s - %d creditos' % (len(MOV), ts, tc))
    for (cap, ran) in sorted(MOV):
        p = prompt(cap, ran)
        assert len(p) <= 2500, (cap, ran, len(p))
    print('todos los prompts caben en el limite de 2500 caracteres de Kling')
