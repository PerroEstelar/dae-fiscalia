# -*- coding: utf-8 -*-
r"""UNIDAD 1 «El encuentro en la carretera» · diez ranuras · pieza 2339.

LO QUE SE OYE ENCIMA (recortar_jr.py: u02, u04 y u12 partidos donde arranca
la accion nueva; los titulos de fase quedaron fundidos con su frase)
    r01 179  Inicio: el encuentro en la carretera. Un hombre adinerado,
             Diego, conduce su Audi por una carretera solitaria.
    r02 139  Al intentar adelantar a un viejo automovil, el otro conductor
             (Mario) lo bloquea.
    r03 201  Escalada: el orgullo entra en juego. Alterado, Diego logra
             adelantar a Mario y lo insulta, siguiendo su camino.
    r04  89  Mas adelante, Diego sufre un pinchazo y se detiene.
    r05 139  Mario aparece... y reconoce al hombre que lo insulto. Hay
             ofensas mutuas.
    r06 226  Confrontacion directa. Ambos conductores se enfrentan
             fisicamente. Explosion: punto sin retorno.
    r07 184  La violencia escala rapidamente: destruyen los vehiculos, se
             golpean brutalmente, se hieren gravemente.
    r08 286  En un momento extremo, uno intenta matar al otro con el auto y
             terminan atrapados en una lucha salvaje dentro del vehiculo.
             Desenlace: destruccion mutua.
    r09  96  El auto se incendia y los dos conductores mueren dentro de el.
    r10 150  La policia llega tras el incendio del vehiculo. Encuentran el
             auto completamente calcinado.

UNA CARRETERA, UN DIA ENTERO
    De la manana (r01) a la tarde (r05, r06), al crepusculo (r07, r08), a la
    noche (r09) y al amanecer siguiente (r10). La luz cuenta la escalada.

LA VIOLENCIA NO SE DIBUJA
    r06 es el antes: dos hombres frente a frente a un metro, sin tocarse.
    r07 es el despues sobre los carros: vidrio en el asfalto, una puerta
    hundida, un espejo en el piso, nadie en cuadro. r08 es el carro
    atravesado en la via con las puertas abiertas y las luces encendidas,
    visto de lejos, sin nadie visible. r09 es un resplandor y una columna
    de humo al fondo de la carretera, de noche. r10 es el casco calcinado
    al amanecer, con un carro blanco sin marcas detras y dos figuras de
    espaldas, lejos. Ningun golpe, ningun cuerpo, ningun arma.

QUIEN LLEVA CARA
    Diego (r03) y Mario (r05, r06). Los dos de fabula; Mario lleva el
    acento (el sueter): es «el otro» de la carretera.
"""

R = {}

R[1] = (179, 'dia', (), False, False, 'carretera', '''
Wide shot of a lonely two-lane road in the Colombian Andes in the morning,
the camera at standing height on the shoulder, perfectly level, looking
along the road as it curves away along the mountainside.

On the road, coming toward the camera and still some distance away,
%(audi)s, alone on the asphalt, small in the frame. The green slope rises
on the right, the valley falls away on the left under low cloud, a few
bare fence posts along the shoulder. Grey morning light from one side; the
asphalt carries a faint sheen. Nothing else moves on the road. No sign, no
lettering, no number plate.
''')

R[2] = (139, 'dia', (), False, False, 'carretera', '''
Medium-wide shot on the same mountain road, the camera low at bumper
height on the centre line, perfectly level, looking along the road from
BEHIND two cars.

Nearer the camera, %(viejo)s, in the right lane. Just ahead of its left
rear corner, %(audi)s has pulled out into the left lane to overtake and is
level with the old car's rear door; and the old car has drifted LEFT toward
the centre line, closing the gap, its left wheels on the line. The two cars
are a hand's width apart. Both drivers are only shapes through the rear
windows. The road curves ahead with the valley on the left. No number
plates, no badges, no lettering.

What the camera asserts: one car is not letting the other past.
''')

R[3] = (201, 'dia', ('diego',), None, False, 'carretera', '''
Medium shot inside the dark sedan, the camera on the passenger seat at
seated eye level, perfectly level, looking across at the driver.

%(diego)s drives with his left hand on the wheel at the top; his right arm
is raised with the hand open, palm out, toward the driver's window beside
him, in the middle of a shout: his head turned toward that window, his
mouth open, his brows down, the cords of his neck showing. Through the
driver's window, out of focus and close, the pale flank of the old car
being left behind. Through the windscreen the road ahead, bright. Plain
dark grey interior with no logo on the wheel, no screen, no lettering.

What the camera asserts: he is past, and he is still shouting.
''')

R[4] = (89, 'dia', ('diego',), None, False, 'carretera', '''
Wide shot of the dark sedan stopped on the gravel shoulder of the mountain
road, its rear right tyre flat, the car very slightly tilted, the camera at
standing height across the road, perfectly level.

%(diego)s crouches by the flat tyre, seen from BEHIND and small, his jacket
pulled tight across his back, one hand on the tyre; his face is not
visible. The road is empty in both directions. Midday light, flat and grey;
the slope rises behind the car. No number plate, no badge.
''')

R[5] = (139, 'dia', ('diego', 'mario'), None, False, 'carretera', '''
Wide shot on the same shoulder, the camera at standing height on the road
behind the two cars, perfectly level.

The old light grey sedan has stopped on the shoulder ten metres behind the
dark sedan with its driver's door open. %(mario)s stands beside the open
door, one hand still on its top edge, facing forward along the shoulder
toward the dark sedan; %(diego)s has stood up beside his flat tyre and
turned to face back. The two men are ten metres apart, each facing the
other, each with his free hand at his side. Neither has taken a step. Their
faces are small in the frame. Afternoon light from the side, the shadows of
the cars long on the gravel.
''')

R[6] = (226, 'contraluz', ('diego', 'mario'), None, False, 'carretera', '''
Medium shot of two men facing each other on the gravel shoulder of the
mountain road, the camera at chest height to one side, perfectly level, so
that both are in PROFILE, one on the left and one on the right, a metre of
air between their faces. Behind them, the pale sky over the valley is the
only bright thing in the picture; the men read as dark planes with the
light along their edges.

On the left, %(diego)s: his weight forward on the front foot, his chin
pushed out, his jaw set, his mouth closed hard, both hands at his sides
closed into fists. On the right, %(mario)s: his weight back, his chin
level, his mouth a closed straight line, his hands open at his sides,
fingers spread. Neither touches the other; the metre of air stays empty.
No speed lines, no motion blur.

What the camera asserts: the last moment in which nothing has happened.
''')

R[7] = (184, 'contraluz', (), False, False, 'carretera', '''
Medium-wide shot of the two cars on the shoulder at dusk, the camera at
knee height on the asphalt, perfectly level, the fading sky over the valley
the only bright thing in the picture.

The old light grey sedan nearest: its windscreen a web of cracks with a
hole in it, its driver's door hanging open, its side mirror lying on the
asphalt in the foreground in a scatter of small pieces of glass. Beyond it,
the dark sedan with its rear door caved in and its rear window gone, one
headlight on. NOBODY in the picture: no figure, no shadow of a person,
nothing on the ground but the mirror and the glass. The gravel and the
asphalt read as dark planes.
''')

R[8] = (286, 'hero', (), False, False, 'carretera', '''
Wide shot of the mountain road at night from far down the road, the camera
at standing height on the centre line, perfectly level.

Two hundred metres away, the dark sedan stands SKEWED across both lanes,
its headlights on and pointing off into the slope, both front doors open:
the headlights are the one weak light source in the picture, and the beams
lay a long grey plane across the asphalt toward the camera. The old car is
a dark shape behind it on the shoulder. Nobody is visible: no figure in
the beams, no figure in the car, only the open doors and the light. The
slopes and the valley dissolve into near-black.
''')

R[9] = (96, 'hero', (), False, False, 'carretera', '''
Wide shot of the mountain road at night from very far down the road, the
camera at standing height on the shoulder, perfectly level.

At the far end of the road, where it curves, a low pale grey-white glow -the only light in the
picture- rises from the
asphalt behind the curve, and a wide soft column of smoke climbs from it
into the night sky, lit from below. The road between the camera and the
glow is a long dark plane with a faint sheen. Nothing else is visible: no
car, no figure. The glow is rendered as light, without any coloured flame
drawn.
''')

R[10] = (150, 'dia', (), False, False, 'carretera', '''
Wide shot of the mountain road at dawn, grey and still, the camera at
standing height on the shoulder, perfectly level.

In the middle of the road the burnt-out shell of a sedan: no glass, no
paint, every surface a flat dull dark grey, the roof sagging, the tyres
gone, sitting on its rims in a wide black stain on the asphalt. Twenty
metres behind it a plain white car with a plain unlit light bar on its roof
and NO marking, NO lettering, NO emblem of any kind, its doors open. Two
figures in plain dark jackets stand near the shell, seen entirely from
BEHIND, far and small, still. Low cloud on the ridges; the first grey light
from the valley side.
''')

NOMBRE = {1: 'la_carretera', 2: 'el_bloqueo', 3: 'el_insulto', 4: 'el_pinchazo',
          5: 'mario_aparece', 6: 'frente_a_frente', 7: 'los_carros',
          8: 'atravesado', 9: 'el_resplandor', 10: 'calcinado'}

REUSA = {}

CON_PERSONA = {3, 4, 5, 6, 10}
SILUETAS = set()
CARTONES = {1, 3, 6, 8, 10}
CENITALES = set()
SOLO_MANOS = set()
SIN_CARA = {4, 10}
TOPE_SIN_GENTE = 3
PIEZA = 2339
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {3: ['diego'], 4: ['diego'], 5: ['diego', 'mario'], 6: ['diego', 'mario']}

DET = {
 (3, 'la_mano_en_el_volante'): dict(cuadros=72, entra=110, registro='dia',
     personas=('diego',),
     escena='Close shot of a man\'s left hand gripping the top of a plain dark '
            'grey steering wheel, the cuff of a dark charcoal jacket and an '
            'expensive plain wristwatch with no legible dial at the wrist, '
            'the bright road out of focus through the windscreen beyond.',
     gesto='The fingers tighten on the wheel until the knuckles stand out, '
           'and hold. The wheel does not turn. Nothing else moves.'),
 (6, 'las_manos_de_mario'): dict(cuadros=72, entra=120, registro='contraluz',
     personas=('mario',),
     escena='Close shot of a man\'s two hands hanging open at his sides '
            'against the plain grey canvas of a work jacket, fingers spread, '
            'the pale sky behind, the hands reading as dark planes with light '
            'on their edges.',
     gesto='The fingers close slowly into loose fists and open again. '
           'Nothing else moves.'),
}

BROLL = {
 'la_curva': ('dia', 'Wide shot of an empty curve of a two-lane mountain road '
              'in the Colombian Andes, low cloud on the ridges, nobody on it.'),
}

# 31 oct, revision de Sebastian: r04 y r05 salieron fotograficas (roca con
# textura, carro de foto): se rehacen con la r02 y la r06 -la misma carretera,
# ya aprobadas- como referencia de dibujo. Y la r08 se parte en tres: el carro
# atravesado, la pelea DENTRO del carro (sobre el hombro, cara que forcejea,
# sin sangre ni arma) y el carro ardiendo antes del resplandor lejano de r09.
# clave -> (nombre, registro, gente, acento, silueta, lugar, texto, hojas)
EXTRA = {
 '08b': ('la_lucha', 'hero', ('diego', 'mario'), None, False, 'carretera', '''
Medium-close shot INSIDE the dark sedan at night, the camera low in the back
seat looking forward between the two front seats, perfectly level.

Over the near shoulder of %(mario)s -his back and the collar of his plain
grey canvas jacket large and soft in the right foreground, his face not
visible- we see %(diego)s in the driver's seat turned toward him, caught in
the middle of a struggle: his face lit from below by the dashboard and the
headlight glow coming back off the slope through the windscreen, teeth
clenched, brows drawn, eyes on the other man; his right hand grips the
other man's jacket at the shoulder and his left forearm is raised between
them. Mario's near arm pushes against Diego's chest. It is a shove and a
grip, two men locked together in a space too small for it: NO weapon, NO
blood, NO wound, no broken glass in the frame. The arm in motion may carry
a slight motion blur; the faces and the car interior are sharp. Through the
windscreen beyond them, out of focus, the pale plane of the headlights on
the asphalt and the black of the slope.

What the camera asserts: «atrapados en una lucha salvaje dentro del
vehiculo», and nothing more explicit than that.
''', ['diego', 'mario']),
 '08c': ('el_incendio', 'hero', (), False, False, 'carretera', '''
Medium-wide shot of the dark sedan at night, skewed across the road exactly
as in the previous wide shot, the camera at standing height on the asphalt
forty metres away, perfectly level.

The car is burning: broad pale grey-white planes of fire rise from the
engine bay and out of the open front doors, rendered as LIGHT -soft flat
shapes with no drawn tongues of coloured flame- and a wide dark column of
smoke climbs from it into the night, lit grey from below. The fire is now
the only light source: it lays a bright plane on the asphalt around the car
and a soft glow on the slope behind it; the headlights are off. The old
light grey car is a dark shape behind it on the shoulder, untouched. NOBODY
is visible: no figure in the car, no figure on the road, no shadow of a
person. The valley dissolves into near-black.

What the camera asserts: the end of it, from a distance, as light and smoke.
''', []),
}

# ranura -> [(placa, cuadros), ...]; la ultima toma lo que falte.
#   r08: el carro atravesado hasta «con el auto» (96), la pelea dentro del
#   carro en «terminan atrapados en una lucha salvaje dentro del vehiculo»
#   (110) y el incendio desde «Desenlace» hasta el corte a r09 (80).
COMPUESTAS = {
 8: [(8, 96), ('08b', 110), ('08c', None)],
}


MOV = {
 1: 'kling: el carro oscuro avanza por la carretera hacia la camara',
 2: 'kling: el carro viejo se cierra sobre la linea; el oscuro frena',
 8: 'luz: la noche se cierra sobre los tres planos (sin modelo); ver COMPUESTAS',
 9: 'kling: el humo sube; el resplandor late',
 10: 'luz: amanece (sube el cielo, sin modelo)',
}

LOWER_THIRD = {3: 'Diego', 5: 'Mario'}


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
    if len(CENITALES) > 3:
        fallos.append('%d cenitales' % len(CENITALES))
    return fallos, tot, mejor
