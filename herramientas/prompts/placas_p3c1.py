# -*- coding: utf-8 -*-
"""Las 21 placas del PRIORIDAD 03 Caso 1, con el prompt literal de cada una.

ESTRUCTURA DE CADA PROMPT
    bloque de estilo (version con rostro)  +  token literal de la persona  +
    la escena  +  el negativo.

EL ENDURECIMIENTO QUE ENTRA AQUI
    El primer plano de la prueba (kf07) salio con degradado suave en la mejilla
    donde la hoja de personaje tiene planos planos. Es el corrimiento hacia lo
    pictorico que costo el Caso 05 de TA. Por eso el bloque de estilo de las
    placas lleva una frase que la hoja no llevaba:

        Facial surfaces are built from FLAT tonal planes meeting at hard edges

LO QUE NO SE ILUSTRA, Y POR QUE SALE DE LA LISTA
    Ninguna placa muestra un encuentro, una agresion, una retencion ni una
    amenaza en acto. Los pasajes duros del guion (b4, b7, b9, b11) van a
    entorno vacio, a primer plano de expresion, o a carton. Es decision de
    cliente heredada de la biblia SRPA.

LA REFERENCIA DE IMAGEN
    Con rostro, el token escrito ya no basta para la consistencia. Cada placa
    donde aparece una persona pasa ADEMAS su hoja aprobada como referencia.
    Las placas de entorno no llevan referencia: la hoja solo les meteria
    figuras que no van.
"""

ESTILO = (
 'Stylized editorial character illustration, flat graphic treatment. No ink '
 'outline anywhere: forms are built from broad soft tonal planes, never from '
 'rendered shading, never from texture or brush marks. Faces ARE drawn and '
 'expressive, but simplified and graphic: clearly defined eyes with brow, a '
 'simple nose and a simple mouth, readable at a glance, with no photographic '
 'detail, no skin pores, no individual hair strands, no caricature and no '
 'exaggerated proportions. Facial surfaces are built from FLAT tonal planes '
 'meeting at hard edges, never from soft airbrushed gradients on the cheek, '
 'forehead or jaw. Skin stays in a desaturated warm grey range for every '
 'figure, barely tinted, never a saturated skin tone. Colombian features, '
 'varied from one person to the next, carried by facial structure, hair and '
 'silhouette rather than by skin colour. Figures are 8 to 8.5 heads tall. '
 'The environment is entirely in greys. Flat even light, static camera, '
 'perfectly level, no tilt, no vignette, no lens flare. Clean plate: no '
 'legible text, no lettering, no numbers, no signage, no logos.')

NEGATIVO = (
 'Not a photograph, not a 3D render, not painterly. No ink outlines, no '
 'multicolour gradients, no paper grain, no brush texture, no childish or '
 'cartoon-mascot styling, no big round anime eyes, no exaggerated features, '
 'no soft airbrushed skin shading.')

TOKEN = {
 'cristina': 'a woman of about thirty-five, slim build, medium height, dark hair pulled back into a low ponytail, wearing a plain institutional blue jacket buttoned to the neck over plain grey trousers and plain grey shoes',
 'victor':   'a man of about forty-five, heavy build, broad shoulders, tall, short dark hair, wearing a plain institutional blue shirt worn loose over dark grey trousers and grey shoes',
 'camilo':   'a man of about thirty-eight, medium build, medium height, short dark hair, wearing a plain grey jacket over a plain grey t-shirt, plain grey trousers and grey shoes, with a plain institutional yellow cap',
 'diana':    'a woman of about thirty, medium build, dark hair loose to the shoulder, wearing a plain light grey blouse and a plain mid-grey knee-length skirt with grey flat shoes, with a plain institutional yellow lanyard around her neck',
 'daniela':  'a woman of twenty-three, slim, medium height, dark hair gathered at the back, plain light grey short-sleeved blouse, plain grey jeans, grey trainers, no colour anywhere',
 'paula':    'a woman of twenty-nine, medium build, dark hair cut short to the jaw, plain mid-grey open jacket over a plain light grey t-shirt, dark grey trousers, grey ankle boots, no colour anywhere',
 'elena':    'a woman of thirty-five, slim, dark hair in a low bun, a plain mid-grey knee-length work tunic over plain grey trousers, flat grey shoes, no colour anywhere',
 'juliana':  'a woman of nineteen, slim, short, long dark hair worn loose, a plain light grey knitted cardigan over a plain grey top, grey jeans, grey trainers, no colour anywhere',
 'yeimi':    'a girl of seventeen, slim, short, dark hair in a high ponytail, a plain light grey t-shirt, plain grey jeans, grey trainers and a plain grey school backpack, dressed in ordinary everyday clothes exactly like the others, no colour anywhere',
}

# hoja aprobada que va como referencia de imagen
HOJA = {'cristina': 'VX1YBnNMMU', 'victor': 'VX1YBnNMMU',
        'camilo': '1lnqgqpr4r', 'diana': '1lnqgqpr4r',
        'daniela': 'gOMruObSXO', 'paula': 'gOMruObSXO', 'elena': 'gOMruObSXO',
        'juliana': 'MBrWocmDCm', 'yeimi': 'MBrWocmDCm'}

ACENTO = {'cristina': 'azul', 'victor': 'azul',
          'camilo': 'amarillo', 'diana': 'amarillo'}

# (nombre, bloque, [personas], escena)
PLACAS = [
 ('kf01_fachada', 'b1', [],
  'Wide establishing shot of the plain street facade of a modest three-storey '
  'lodging house in a Colombian city, seen straight on from across the street. '
  'Rendered windows with plain frames, a single plain door, bare rendered '
  'walls, a narrow pavement and a kerb. Overcast daytime, flat even light. '
  'The street is empty: no people, no vehicles. Ordinary and unremarkable, '
  'not sinister, not derelict. No window bars, no grilles, no padlocks.'),

 ('kf03_cristina_telefono', 'b2', ['cristina'],
  'Medium shot, waist up, of CRISTINA seated at a plain table in a bare grey '
  'interior, holding a mobile phone in both hands at chest height and looking '
  'down at its blank screen. Composed, decided expression. The phone screen is '
  'blank grey, with nothing on it. No other person in frame.'),

 ('kf04_victor_recepcion', 'b2', ['victor'],
  'Medium shot of VICTOR standing behind a plain reception counter in a bare '
  'grey lobby, both forearms resting on the counter top, facing camera. '
  'Composed, decided expression. The counter is empty except for a plain '
  'closed ledger. No other person in frame.'),

 ('kf05_pasillo', 'b3', [],
  'Interior corridor of a modest lodging house seen straight down its length, '
  'plain closed doors evenly spaced along both walls, bare rendered walls, a '
  'plain floor, flat even overhead light. Completely empty: no people. '
  'Ordinary and neutral, not threatening. No padlocks, no bars, no bolts, no '
  'numbers on the doors.'),

 ('kf06_terminal', 'b4', ['daniela'],
  'Wide shot of DANIELA standing alone in the concourse of an intercity bus '
  'terminal, full figure, a single small holdall at her feet, one hand holding '
  'the strap of a shoulder bag. Guarded, withheld posture: shoulders slightly '
  'drawn in, head level. Bare grey concourse behind her with plain columns and '
  'empty benches, no other person in frame, no signage.'),

 ('kf08_tienda', 'b5', ['daniela'],
  'Medium wide shot of DANIELA standing at the counter of a small '
  'neighbourhood grocery shop, seen from the side, a plain cloth bag in one '
  'hand and two unlabelled grocery packets on the counter. Guarded, withheld '
  'posture. Plain grey shelving behind the counter holding unlabelled '
  'packages. No shopkeeper, no other person in frame, no price labels, no '
  'packaging text.'),

 ('kf09_camilo_carro', 'b5', ['camilo'],
  'Wide shot of CAMILO standing beside a plain four-door grey sedan parked at '
  'the kerb outside a bus terminal, full figure, one hand resting on the roof '
  'of the car, body turned three-quarters to camera, his gaze directed away '
  'from the lens. Overcast daytime. No passenger, no other person in frame, '
  'no number plate.'),

 ('kf10_paula_llega', 'b6', ['paula'],
  'Wide shot of PAULA arriving on a plain city pavement, full figure, walking '
  'with a small wheeled suitcase held by the handle beside her, her own '
  'shoulder bag across her body. Upright, resolved, unhurried posture, head '
  'up. Bare rendered wall and kerb behind her, no other person in frame.'),

 ('kf11_paula_cu', 'b6', ['paula'],
  'Close-up of PAULA, head and shoulders, facing camera three-quarters on. '
  'Resolved, composed expression: level gaze, mouth relaxed and closed, brow '
  'untroubled. Plain flat grey background with no detail. Flat frontal light.'),

 ('kf12_elena_limpieza', 'b7', ['elena'],
  'Wide shot of ELENA standing in a bare grey corridor with a mop in one hand '
  'and a plain bucket on the floor beside her, full figure, having stopped '
  'mid-task, arms hanging. Emptied, spent posture: shoulders dropped, head '
  'slightly lowered. Nobody else in frame.'),

 ('kf13_elena_cu', 'b7', ['elena'],
  'Close-up of ELENA, head and shoulders, facing camera almost straight on. '
  'Emptied expression: gaze unfocused and directed slightly past the lens, '
  'mouth closed and slack, eyelids heavy with exhaustion, no tears, no drama. '
  'Plain flat grey background with no detail. Flat frontal light.'),

 ('kf14_cuaderno', 'b7', [],
  'Overhead shot, perfectly level, of a plain open notebook lying on a bare '
  'grey table, a simple pen resting across the right-hand page, nothing else '
  'on the table. Both pages are completely blank: no writing, no ruled lines, '
  'no figures, no numbers. Flat even light. No hands, no people.'),

 ('kf15_cristina_lejos', 'b8', ['cristina'],
  'Wide shot of a bare grey room with a plain curtainless window, CRISTINA '
  'standing small in the far right of the frame beside the window, full '
  'figure, turned away towards the glass, hands at her sides. Most of the '
  'frame is empty wall and floor. She is distant and uninvolved, and no one '
  'else is in the room. No window bars, no grilles.'),

 ('kf16_carro_noche', 'b9', [],
  'Wide shot of a plain four-door grey sedan parked on an empty residential '
  'street at night, seen three-quarters from the front, headlights off, '
  'windows dark and unreadable. A single streetlamp gives flat cool light; '
  'bare rendered walls behind. Completely empty: no people, no figures inside '
  'the car. No number plate, no signage.'),

 ('kf17_camilo_cu', 'b9', ['camilo'],
  'Close-up of CAMILO, head and shoulders, his body towards camera but his '
  'face turned away to the side so his gaze leaves the frame. Distant, '
  'withdrawn expression: mouth closed, brow flat, no appeal to the viewer. '
  'Plain flat grey background with no detail. Flat frontal light.'),

 ('kf18_daniela_ventanilla', 'b9', ['daniela'],
  'Medium shot from outside a plain grey sedan, level with the rear side '
  'window, DANIELA seated inside and seen through the glass, head and '
  'shoulders, looking out and slightly past the camera. Guarded, withheld '
  'expression, mouth closed. The glass is clear with no reflection clutter. '
  'The car is stationary; nobody else is visible.'),

 ('kf19_agencia_diana', 'b10', ['diana'],
  'Medium shot of DIANA standing behind the plain counter of a small travel '
  'agency, facing camera, one hand resting on a closed plain folder on the '
  'counter. Composed, matter-of-fact expression. Bare grey wall behind her '
  'with a single empty plain frame. No customer, no other person in frame, '
  'no posters, no text.'),

 ('kf20_juliana_llega', 'b10', ['juliana'],
  'Wide shot of JULIANA standing on a plain city pavement just arrived, full '
  'figure, a small backpack held in front of her in both hands. Distant, '
  'uncertain posture: weight on one foot, head slightly turned, gaze away '
  'from the lens. Bare rendered wall and kerb behind her, nobody else in '
  'frame.'),

 ('kf21_yeimi_llega', 'b11', ['yeimi'],
  'Wide shot of YEIMI standing on a plain city pavement, full figure, her '
  'school backpack on both shoulders, arms at her sides. Ordinary everyday '
  'clothing, ordinary upright standing posture, nothing suggestive. Distant '
  'expression, gaze directed away from the lens. Bare rendered wall and kerb '
  'behind her, nobody else in frame.'),

 ('kf22_yeimi_cu', 'b11', ['yeimi'],
  'Close-up of YEIMI, head and shoulders, facing camera three-quarters on, '
  'wearing a plain light grey t-shirt. Distant, evasive expression: gaze '
  'directed down and away from the lens, mouth closed, brow flat. Entirely '
  'neutral and ordinary, nothing suggestive. Plain flat grey background with '
  'no detail. Flat frontal light.'),
]


def prompt(nombre):
    for n, b, gente, escena in PLACAS:
        if n != nombre:
            continue
        partes = [ESTILO]
        for p in gente:
            partes.append('%s is %s.' % (p.upper(), TOKEN[p]))
        partes.append(escena)
        partes.append(NEGATIVO)
        return ' '.join(partes)
    raise KeyError(nombre)


def refs(nombre):
    for n, b, gente, escena in PLACAS:
        if n == nombre:
            return [HOJA[p] for p in dict.fromkeys(gente)]
    raise KeyError(nombre)


if __name__ == '__main__':
    print('%-26s %-5s %-22s %-10s %s' % ('placa', 'bloq', 'personas', 'acento', 'largo'))
    for n, b, gente, escena in PLACAS:
        ac = ','.join(sorted({ACENTO[p] for p in gente if p in ACENTO})) or '-'
        print('%-26s %-5s %-22s %-10s %d' % (n, b, ','.join(gente) or '(entorno)', ac, len(prompt(n))))
    print('\n%d placas  ·  %d con persona  ·  %d de entorno'
          % (len(PLACAS), sum(1 for p in PLACAS if p[2]), sum(1 for p in PLACAS if not p[2])))
