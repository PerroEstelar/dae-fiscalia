# -*- coding: utf-8 -*-
r"""Clausulas y reparto del curso «Justicia restaurativa» (PRIORIDAD 1).

EL SISTEMA ES EL DE LA SERIE, SIN UNA COMA DE MAS
    El de Gerencia judicial, que es el del P3 y de Desaparicion Forzada:
    rostros dibujados y simplificados, piel gris calida, los tres registros
    de luz, superficie lisa, el acento como PRENDA mate, la escena como
    unidad, cartones verbatim. Todo lo que no es reparto se importa de
    `base_df_v1` tal cual; los lugares de oficina, ciudad y sala vienen de
    `base_gj`.

SEIS PIEZAS, TRES MUNDOS
    C1 y C2 son casos: la ciudad, el hospital, la Fiscalia, la sala.
    U1 es una fabula en una carretera de montana, de dia a noche.
    U2, U3 y U4 son UNA SOLA CONVERSACION en UNA SOLA OFICINA, en tres
    tiempos: la manana (U2), el mediodia (U3) y la tarde que cae (U4).
    «Usted sigue en su oficina, Juana tambien». La misma mesa, la misma
    ventana, la misma silla; lo que cambia es la luz y lo que hay sobre la
    mesa (el vaso de agua, el celular, el libro, el cafe).

EL FISCAL DE LAS UNIDADES ES «USTED»: LA CAMARA
    El documento le habla al fiscal en segunda persona y lo deja sin
    genero («doctor(a)»). Entonces el fiscal no se dibuja de frente nunca:
    es el punto de vista. Juana esta del otro lado del escritorio, mirando
    a la camara o un poco a un lado de ella; del fiscal se ven las manos
    -sirviendo el cafe, abriendo el libro, sosteniendo el celular- y, en los
    planos sobre el hombro, la espalda y la nuca. Nadie decide mal en estas
    piezas, pero igual: lo que el fiscal piensa esta en la voz, y su cara es
    la del que mira.

LO QUE SE RECUERDA SE VE EN OTRO REGISTRO
    La conversacion va en `dia` (oficina institucional). Lo que el fiscal
    recuerda o lee -la mirada de Tolstoi, el dibujo de Van Gogh, el jardin
    de Rubiano, Dante y Virgilio- va en `contraluz` o en `hero`: es otro
    tiempo y otro lugar, y la luz lo dice sin un solo rotulo.

EL COLOR, PIEZA POR PIEZA
    C1  Ana Perez, la victima: una bufanda. La pregunta del caso es si la
        mediacion la revictimiza; ella es el centro.
    C2  Camilo Ferreira, la victima: el sueter con que se recupera. Los
        procesados y la acusacion van en gris.
    U1  Mario, el del automovil viejo: un sueter bajo la chaqueta. Es «el
        otro» a quien no se reconoce al principio de la fabula; Diego, el del
        carro caro, en gris oscuro.
    U2-U4  Juana: una bufanda tejida. Es quien pregunta y quien decide si
        su primo va o no.

QUIEN NO LLEVA CARA, Y POR QUE
    C1  Juan Rodriguez, el que golpea: la agresion no se dibuja y su cara
        tampoco; es la espalda al salir de la audiencia, junto a su
        defensor, tambien sin cara. El medico legista: manos y bata.
    C2  Los dos procesados: siluetas y espaldas. La amiga y los duenos de
        la tienda, pequenos y de lejos. El defensor y quien lee el
        expediente: manos.
    U1  Diego y Mario SI llevan cara -son personajes de fabula- pero la
        violencia no se dibuja nunca: se ve el antes (los dos carros
        detenidos, los dos hombres frente a frente a distancia) y el
        despues (el vidrio en el asfalto, el carro ardiendo de lejos, el
        carro calcinado al amanecer). Ningun golpe, ningun cuerpo.
    U2-U4  El fiscal: es la camara (ver arriba). Los personajes de lo
        recordado -los dos hombres de la mirada, el hombre cansado, la
        madre y el nino, el hombre del jardin, Dante y Virgilio- van a
        contraluz o en silueta: son figuras de un recuerdo, no retratos.
        El hombre del jardin NUNCA toca al nino en imagen; el nino no se
        dibuja llevado por nadie.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_df_v1 as B                          # noqa: E402
from base_df_v1 import (PIEL, ROSTRO, PLANOS, REGISTRO, CAMARA, LIMPIA,  # noqa
                        SIN_ROLES, SILUETA, ESTILO, FIGURA, LUGAR, ACENTO, NEG)
from base_gj import OFICINA, CIUDAD, SALA       # noqa: E402

# ------------------------------------------------------------------ lugar
HOSPITAL = ('The setting is an ordinary Colombian public hospital: plain '
            'painted corridor walls with a darker band along the lower half, '
            'plain tiled floor, simple metal benches, swing doors with small '
            'plain windows, fluorescent ceiling light. Nothing lavish, nothing '
            'north-american, no cross, no logo, no lettering anywhere.')

CARRETERA = ('The setting is a lonely two-lane mountain road in the Colombian '
             'Andes: plain grey asphalt with a faded centre line, no traffic, '
             'green steep slopes on one side falling away to a deep valley on '
             'the other, low cloud on the far ridges, a few bare fence posts, '
             'no buildings, no signs, no billboards, no lettering anywhere. '
             'Nothing picturesque, no postcard framing.')

BARRIO = ('The setting is an ordinary residential street in Bogota at night: '
          'two and three storey houses built flush to the pavement in exposed '
          'clay brick and plain rendered concrete, flat concrete roofs, plain '
          'metal grilles on every ground-floor window, square concrete utility '
          'poles with bundles of black cable, a raised concrete kerb, a '
          'corner shop with a roll-down metal shutter. No lettering, no shop '
          'sign, no logo anywhere.')

JARDIN = ('The setting is a quiet residential street of single-storey houses '
          'in a Colombian town, each with a small front garden: a patch of '
          'plain lawn, a low painted wall with a simple metal gate, a plain '
          'rendered facade behind. Nothing lavish, nothing north-american, no '
          'picket fence, no lettering anywhere.')

CELDA = ('The setting is a plain institutional detention corridor: painted '
         'masonry, a long barred metal gate, a bench bolted to the wall, '
         'light from a high small window. No lettering, no number, no emblem, '
         'no uniform.')

RECUERDO = ('The setting is bare and unplaced: an empty space with a plain '
            'ground plane and nothing that says a country or a period. No '
            'lettering anywhere.')

LUGARES = {'oficina': OFICINA, 'ciudad': CIUDAD, 'sala': SALA,
           'hospital': HOSPITAL, 'carretera': CARRETERA, 'barrio': BARRIO,
           'jardin': JARDIN, 'celda': CELDA, 'recuerdo': RECUERDO}

# ------------------------------------------------------------------ reparto
CUERPO = {
 # ---- C1
 'ana': ('ANA PEREZ, a mestiza Colombian woman of about thirty-four, medium '
         'build, dark hair pulled back in a low bun, in a plain mid-grey '
         'cardigan over a plain light grey blouse, plain grey trousers, and '
         'a plain matte mustard-yellow knitted scarf wrapped once around her '
         'neck with both ends hanging down the front'),
 'juan': ('JUAN RODRIGUEZ, a young Colombian man of about twenty-four, lean, '
          'short dark hair, in a plain dark grey hooded jacket and plain grey '
          'trousers, seen only from BEHIND or from the side with his face '
          'turned away'),
 'defensor1': ('HIS DEFENCE LAWYER, a man of about fifty, in a plain mid-grey '
               'suit with a plain grey tie, a plain grey folder under his arm, '
               'seen only from behind or with his face turned away'),
 'fiscal1': ('THE LOCAL PROSECUTOR, a mestiza Colombian woman of about forty, '
             'medium build, dark hair cut to the jaw, in a plain charcoal grey '
             'blazer over a plain light grey blouse and plain grey trousers'),
 'legista': ('THE FORENSIC PHYSICIAN, seen only as a pair of hands and the '
             'sleeves of a plain light grey coat, no face in frame'),
 # ---- C2
 'camilo': ('CAMILO FERREIRA, a mestizo Colombian man of about twenty-seven, '
            'lean, short dark curly hair, a short dark beard, in a plain matte '
            'mustard-yellow crew-neck sweater over a plain light grey '
            'T-shirt, plain grey trousers; his right forearm is wrapped in a '
            'plain light grey bandage'),
 'procesados': ('THE TWO ACCUSED MEN, one of about twenty-one, slight, and '
                'one of about thirty-nine, heavy-set, both in plain grey '
                'everyday clothes, seen only as SILHOUETTES or from BEHIND, '
                'never a face'),
 'amiga': ('A YOUNG WOMAN, a friend of his, of about twenty-five, in plain '
           'grey clothes, small in the frame and far away, her face not '
           'readable'),
 'defensor2': ('THE DEFENCE LAWYER, a woman of about forty-five in a plain '
               'mid-grey suit, seen only from behind or as hands and a folder'),
 'fiscal2': ('THE PROSECUTOR WHO READS THE FILE, seen only as hands and the '
             'sleeves of a plain charcoal grey jacket, no face in frame'),
 # ---- U1
 'diego': ('DIEGO, a Colombian man of about forty-five, well-fed, short dark '
           'hair combed back, clean-shaven, in a plain dark charcoal grey '
           'suit jacket over a plain dark grey shirt open at the collar, '
           'plain dark trousers and polished dark shoes, an expensive plain '
           'wristwatch with no legible dial'),
 'mario': ('MARIO, a Colombian man of about fifty-two, wiry, grey stubble, '
           'thinning grey hair, in a plain grey canvas work jacket open over a '
           'plain matte mustard-yellow crew-neck sweater, plain grey work '
           'trousers and worn grey boots'),
 'audi': ('a large dark charcoal grey luxury sedan, low and wide, with clean '
          'straight lines, dark tinted windows and plain dark wheels, with NO '
          'badge, NO logo, NO lettering and NO number plate'),
 'viejo': ('an old boxy light grey sedan from the nineteen-eighties, faded '
           'paint, a dented rear fender, mismatched hubcaps, with NO badge, NO '
           'logo, NO lettering and NO number plate'),
 # ---- U2-U4
 'juana': ('JUANA, a mestiza Colombian woman of about forty-eight, medium '
           'build, dark wavy hair to the shoulders with a few grey strands, '
           'in a plain mid-grey wool coat open over a plain light grey '
           'blouse, plain grey trousers, and a plain matte mustard-yellow '
           'knitted scarf wrapped once around her neck with both ends '
           'hanging down the front; she keeps a plain grey handbag on her lap '
           'or at her feet'),
 'fiscal': ('THE PROSECUTOR -«usted»-, never seen from the front: only the '
            'back of a head of SHORT dark hair cut close at the neck, well '
            'above the collar, never long and never a bob, a plain charcoal '
            'grey jacket over the shoulders, and a pair of hands with plain '
            'light grey shirt cuffs, no ring, no watch'),
}

VIDA = {
 'ana': ('She works and lives in the same neighbourhood where it happened. '
         'She said no to talking with him twice, and means it.'),
 'juan': ('He is twenty-four and has never been inside a court before this '
          'week.'),
 'fiscal1': ('Twelve years in the local prosecution office. She reads the '
             'whole file before she decides anything, and keeps a plain grey '
             'pen on the folder she is working on.'),
 'camilo': ('He works for himself, odd jobs, and has not worked since the '
            'surgery. He keeps his right arm still and close to his body.'),
 'diego': ('He is used to arriving first. He drives with one hand on the '
           'wheel and the other on the gear lever.'),
 'mario': ('He has driven the same car for twenty years and knows every '
           'noise it makes. He drives with both hands on the wheel.'),
 'juana': ('She came in on her lunch break from work to ask for her cousin, '
           'who cannot come himself. She listens with her whole body, leaning '
           'a little forward, and does not pretend to agree when she does '
           'not.'),
 'fiscal': ('Years of hearing people in this chair. Listens before answering. '
            'Keeps a plain grey notebook, a plain white cup and, today, a '
            'book on the desk.'),
}

# Quien lleva acento.
CON_ACENTO = {'ana', 'camilo', 'mario', 'juana'}

# Quien NO se dibuja nunca con rostro.
SIN_ROSTRO = {'juan', 'defensor1', 'legista', 'procesados', 'amiga',
              'defensor2', 'fiscal2', 'fiscal'}

TOKENS = CUERPO


def arma(escena, registro='dia', personas=(), con_acento=None,
         con_lugar=True, con_rostro=True, lugar='oficina', silueta=False,
         exterior=None):
    """Arma el prompt final. `con_acento=None` lo decide el reparto: lleva
    acento si en el plano hay alguien de CON_ACENTO. `lugar` es una de las
    llaves de LUGARES. `exterior` se acepta por compatibilidad y no hace nada."""
    if con_acento is None:
        con_acento = any(p in CON_ACENTO for p in personas)
    p = [escena.strip()]
    if personas:
        vidas = [VIDA[x] for x in personas if x in VIDA]
        if vidas:
            p.append('WHO THESE PEOPLE ARE. ' + ' '.join(vidas))
    p.append(REGISTRO[registro])
    p.append(PLANOS)
    if silueta:
        p.append(ESTILO + FIGURA)
        p.append(SILUETA)
    else:
        con_cara = con_rostro and any(x not in SIN_ROSTRO for x in personas)
        p.append(ESTILO + (ROSTRO if con_cara else '')
                 + (PIEL + ' ' if personas else '') + FIGURA)
    p.append(CAMARA)
    if con_acento:
        p.append(ACENTO)
    if con_lugar:
        p.append(LUGARES[lugar])
    p.append(LIMPIA)
    p.append(SIN_ROLES)
    p.append(NEG)
    return '\n\n'.join(x.strip() for x in p if x and x.strip())
