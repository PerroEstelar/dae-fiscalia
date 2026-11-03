# -*- coding: utf-8 -*-
r"""Cláusulas, lugares y reparto del curso «Enfoque diferencial en la
práctica del fiscal» (PRIORIDAD 2).

EL SISTEMA ES EL DE LA SERIE
    Estilo de `base_df_v1` en su versión corta (la de Ley 1826, que salió
    bien con Seedream 5 Flash): rostros dibujados y simplificados, piel gris
    cálida, tres registros de luz, superficie lisa, el acento como PRENDA
    mate. Lo propio de este curso es el MUNDO -cinco ciudades distintas- y el
    REPARTO.

EL ENCARGO (Sebastián, 3 nov): «make it cinematic, feel like a movie,
different camera angles, same characters, consistency, mid action stills,
several complementary shots of the same scene». Biblia §4: la unidad es la
ESCENA (lugar + quién + hora + qué pasa) filmada desde varias angulaciones
-general, medio, primer plano, detalle-; §6: cada persona con vida y un
objeto suyo que vuelve; §12: el detalle.

LO QUE NO SE DIBUJA NUNCA (la regla de toda la serie)
    Ningún golpe, ninguna agresión en acto, ningún arma, ninguna herida,
    ningún cuerpo. Los agresores y quien amenaza: SILUETA. La niña de
    Putumayo NO se dibuja: está su camino, sus botas, su morral. Ningún
    uniforme, insignia, placa, escudo ni bandera: los policías van con
    chaqueta oscura lisa. Ningún texto legible. Ninguna decisión equivocada
    cae sobre una cara (biblia §3): el coronel de C2, el fiscal de turno de
    C3 y el funcionario de C5 van de espaldas, sobre el hombro o en manos;
    el fiscal Molano (C1) y el fiscal de C4 sí tienen cara, y el cartón de su
    error no cae sobre su rostro.

EL ACENTO (un solo color saturado por composición, una PRENDA mate)
    C1 Yolanda · su cárdigan mostaza
    C2 Jairo · la CAMISA MOSTAZA que compró para su cumpleaños: la que queda
       sobre la silla y que nadie recoge. Vivo, él lleva gris.
    C3 sin acento (la pieza es la noche del aeropuerto)
    C4 la madre · su blusa mostaza
    C5 Valentina · su abrigo mostaza
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
from base_df_v1 import (PIEL, ROSTRO, PLANOS, REGISTRO, CAMARA, LIMPIA,  # noqa
                        SIN_ROLES, SILUETA, ESTILO, FIGURA, ACENTO, NEG)
from base_gj import SALA as _SALA_GJ           # noqa: E402

COLOMBIA = ('This is Colombia, and the architecture, the streets, the cars '
            'and the people must say so; never Europe, never the United States.')

# ------------------------------------------------------------------ lugares
# ---- comunes
DESPACHO = ('The setting is the office of a prosecutor in a Colombian city: a '
            'plain grey desk with an ordinary computer screen and a desk '
            'telephone, metal shelving full of cardboard case folders, two plain '
            'visitor chairs, a window with a plain blind, and a plain round wall '
            'clock with hands and NO numerals. No logo, no seal, no flag, no '
            'portrait, no diploma on the wall, no lettering anywhere.')
SALA = (_SALA_GJ + ' The layout: the judge sits at the centre behind a plain '
        'desk on a low plain platform; the prosecution table on one side, the '
        'defence table on the other, and a few rows of plain public benches at '
        'the back. A plain microphone on a short stand on each table.')
PASILLO = ('The setting is the long plain corridor of a Colombian courthouse: '
           'plain painted walls, a row of plain wooden benches, closed plain '
           'doors, tall windows at the far end with flat daylight. No sign, no '
           'notice board, no lettering anywhere.')

# ---- C1 · Édgar Molano (una ciudad andina, sin nombre)
UNIDAD_VICTIMAS = ('The setting is a small quiet interview room of a victims '
                   'attention unit in a Colombian prosecution office: a plain '
                   'round table with two plain chairs, a box of tissues, a jug '
                   'of water and two glasses, a low plain shelf, soft painted '
                   'walls, one window with a plain blind. No poster, no logo, '
                   'no lettering anywhere.')
BARRIO_ANDINO = ('The setting is a working-class residential barrio of an '
                 'Andean Colombian city: two and three storey houses built '
                 'flush to the pavement in exposed clay brick and plain '
                 'rendered concrete, FLAT concrete roofs, plain metal grilles '
                 'on the windows and doors, square concrete utility poles with '
                 'bundles of black cable, a raised concrete kerb, small parked '
                 'cars, green mountains behind the rooftops. Never pitched '
                 'roofs, never front gardens. No sign, no lettering anywhere.')
CASA_YOLANDA = ('The setting is the inside of a modest family home in a '
                'Colombian barrio: plain painted masonry walls, a plain tiled '
                'floor, a small living room with a plain sofa and a plain '
                'wooden table, a window with a plain grille and a thin curtain, '
                'a few potted plants on the sill. Ordinary, tidy, warm. No '
                'picture with a face, no calendar, no lettering anywhere.')
PSICOLOGIA = ('The setting is a forensic psychology room: two plain armchairs '
              'facing each other at an angle, a low plain table with a jug of '
              'water and a plain notepad, a box of plain wooden toys and '
              'drawing paper on a shelf, soft painted walls, one window with a '
              'plain blind. Calm and bare. No poster, no logo, no lettering.')

# ---- C2 · Jairo (una ciudad intermedia del Caribe colombiano)
CARIBE = ('The setting is a street of an intermediate city of the Colombian '
          'Caribbean coast in hard tropical light: one and two storey houses '
          'with plain rendered walls painted in pale washed tones (all of them '
          'nearly grey here), wide front porches with plain metal grilles and '
          'plain rocking chairs, big almond trees casting deep round shadows, '
          'a plain concrete pavement, square concrete utility poles with '
          'cables, a few motorcycles. Flat roofs and fibre-cement roofs, never '
          'tiled European roofs. No sign, no lettering anywhere.')
CASA_JAIRO = ('The setting is the inside of a professor\'s modest house in a '
              'Caribbean Colombian city: plain painted walls, a plain tiled '
              'floor of large pale tiles, tall plain shelves full of books with '
              'blank spines, a ceiling fan, a few woven hand-made objects from '
              'the Pacific coast on a shelf, louvred plain windows with hard '
              'light coming through the slats. No poster, no picture with a '
              'face, no lettering on any book or object.')
HABITACION = ('The setting is a plain bedroom in that house: a made bed with a '
              'plain pale cover, one plain wooden chair, a plain wardrobe, a '
              'ceiling fan, louvred plain windows with light through the '
              'slats, a pale tiled floor. No picture, no lettering anywhere.')
AULA = ('The setting is an ordinary university classroom in a Colombian '
        'Caribbean city: rows of plain student desks, a plain whiteboard with '
        'only plain grey marks and no letters, tall windows with louvres and '
        'hard daylight, a ceiling fan. No poster, no logo, no lettering.')
RUEDA_PRENSA = ('The setting is the forecourt of a police headquarters in a '
                'Caribbean Colombian city in hard daylight: a plain lectern '
                'with a bunch of plain microphones, plain cameras on tripods, '
                'reporters holding plain recorders, a plain concrete facade. '
                'No flag, no shield, no emblem, no badge, no logo on any '
                'microphone, no lettering anywhere.')
FUNDACION = ('The setting is the small rented office of a grassroots human '
             'rights foundation: plain painted walls, a long plain table with '
             'mismatched plain chairs, stacks of paper and plain folders, a '
             'plain laptop, a plain cloth banner rolled up in a corner with no '
             'letters on it, a ceiling fan. No poster, no flag, no logo, no '
             'lettering anywhere.')
ARCHIVO = ('The setting is a judicial archive: tall plain metal shelving full '
           'of old cardboard case folders tied with plain string, a plain '
           'table, dust in a slanting band of light from a high window. No '
           'label, no number, no lettering anywhere.')

# ---- C3 · Wilmer (el aeropuerto de una capital de departamento)
AEROPUERTO = ('The setting is a small regional airport of a Colombian '
              'departmental capital at night: a plain concrete apron under '
              'flat sodium-free white floodlights, one mid-size plain white '
              'passenger jet with NO livery, NO logo and NO lettering, a plain '
              'boarding stair, a low plain terminal building with large dark '
              'windows, dark hills beyond. No sign, no lettering anywhere.')
CABINA = ('The setting is the inside of the cabin of a plain passenger jet '
          'with no livery: rows of plain grey seats, the narrow aisle, the '
          'overhead bins closed, small round windows black with night, the '
          'cabin lights on. No sign, no lettering, no logo, no seat numbers.')
ESTACION_AEROPUERTO = ('The setting is the small plain police post inside a '
                       'regional airport at night: a plain counter, a plain '
                       'desk with an ordinary computer screen, two plain metal '
                       'benches against a wall, a glass door onto the empty '
                       'terminal hall, flat fluorescent light. No flag, no '
                       'shield, no badge, no poster, no lettering anywhere.')
TERMINAL = ('The setting is the departures hall of a small regional Colombian '
            'airport at night, nearly empty: plain rows of seats, a plain '
            'polished floor reflecting the lights, large dark windows onto the '
            'apron. No sign, no screen with text, no logo, no lettering.')
ENTREVISTA_PRENSA = ('The setting is a plain street outside a modest house in '
                     'a Colombian city in daylight, where a small local news '
                     'crew -one plain camera on a tripod, one plain handheld '
                     'microphone with no logo- records an interview. No '
                     'lettering anywhere.')

# ---- C4 · Putumayo (resguardo cerca de Puerto Guzmán)
RESGUARDO = ('The setting is an indigenous reserve in the Amazonian foothills '
             'of Putumayo, Colombia, near the town of Puerto Guzman: dense '
             'tropical forest, a red-earth path between tall plantains and '
             'chontaduro palms, scattered wooden houses raised on short posts '
             'with plain corrugated zinc roofs, a wide brown river glimpsed '
             'between trees, low cloud on the green hills. Humid, quiet. No '
             'sign, no lettering anywhere.')
CASA_TAITA = ('The setting is a wooden house of the reserve raised on short '
              'posts, plain plank walls, a plain zinc roof, a wooden porch '
              'with a plain hammock, and leaning in the corner by the door a '
              'tall carved wooden staff of authority with plain coloured '
              'ribbons hanging from its top. No lettering anywhere.')
CABILDO = ('The setting is the community house of the cabildo: a large open '
           'wooden building with a high thatched palm roof on wooden posts, '
           'plain wooden benches in a circle, a packed-earth floor, the forest '
           'visible all around through the open sides. No flag, no emblem, no '
           'lettering anywhere.')
FISCALIA_PUEBLO = ('The setting is the small Fiscalía office of a river town '
                   'in Putumayo: a one-storey building of plain rendered '
                   'concrete with a zinc roof, inside a plain desk with an '
                   'ordinary computer screen, a plain standing fan, metal '
                   'shelving with cardboard folders, a window onto a hot street '
                   'with motorcycles. No logo, no seal, no flag, no lettering.')
MESA_TECNICA = ('The setting is a plain meeting room of a regional government '
                'building in Mocoa: a long plain table with eight plain chairs, '
                'plain folders and glasses of water, a plain projector screen '
                'that is blank, a window onto green hills. No logo, no flag, '
                'no seal, no lettering anywhere.')

# ---- C5 · Valentina (una ciudad colombiana, de noche y de día)
CALLE_NOCHE = ('The setting is a residential street of a Colombian city at '
               'night: two and three storey brick and concrete houses with '
               'plain metal grilles, one white street lamp, parked small cars, '
               'square concrete utility poles with cables, the pavement wet. '
               'No sign, no lettering anywhere.')
FISCALIA_FACHADA = ('The setting is the entrance of a Colombian prosecution '
                    'office building in a city in the morning: a plain modern '
                    'concrete facade of four storeys, a plain glass door, a few '
                    'concrete steps, people coming and going. No logo, no '
                    'seal, no flag, no sign, no lettering anywhere.')
RECEPCION = ('The setting is the reception hall of a Colombian prosecution '
             'office: a long plain reception counter with a low pane of plain '
             'glass, a plain computer screen behind it, rows of plain plastic '
             'waiting chairs where several ordinary people sit waiting their '
             'turn, flat fluorescent light. No logo, no seal, no turn-number '
             'display, no poster, no lettering anywhere.')
ESCRITORIO_DENUNCIA = ('The setting is a plain desk in a reception office where '
                       'complaints are taken: an ordinary computer screen, a '
                       'printed one-page form of plain grey bars, a plain pen, a plain stamp, a partition of plain '
                       'grey panels. No logo, no lettering anywhere.')

APARTAMENTO = ('The setting is a small rented apartment in a Colombian city at '
               'night: plain painted walls, a plain wooden table with two '
               'chairs, a plain lamp, a window with a plain metal grille '
               'looking onto the street lamps outside. Tidy, quiet. No '
               'picture with a face, no lettering anywhere.')

SALA_NOCHE = SALA + (' It is a late-night session: the high windows are black '
                     'and the room is lit by plain ceiling lamps.')

LUGARES = {
 'apartamento': APARTAMENTO, 'sala_noche': SALA_NOCHE,
 'despacho': DESPACHO, 'sala': SALA, 'pasillo': PASILLO,
 'unidad_victimas': UNIDAD_VICTIMAS, 'barrio_andino': BARRIO_ANDINO,
 'casa_yolanda': CASA_YOLANDA, 'psicologia': PSICOLOGIA,
 'caribe': CARIBE, 'casa_jairo': CASA_JAIRO, 'habitacion': HABITACION,
 'aula': AULA, 'rueda_prensa': RUEDA_PRENSA, 'fundacion': FUNDACION,
 'archivo': ARCHIVO,
 'aeropuerto': AEROPUERTO, 'cabina': CABINA,
 'estacion_aeropuerto': ESTACION_AEROPUERTO, 'terminal': TERMINAL,
 'entrevista_prensa': ENTREVISTA_PRENSA,
 'resguardo': RESGUARDO, 'casa_taita': CASA_TAITA, 'cabildo': CABILDO,
 'fiscalia_pueblo': FISCALIA_PUEBLO, 'mesa_tecnica': MESA_TECNICA,
 'calle_noche': CALLE_NOCHE, 'fiscalia_fachada': FISCALIA_FACHADA,
 'recepcion': RECEPCION, 'escritorio_denuncia': ESCRITORIO_DENUNCIA,
 'ninguno': '',
}

# ------------------------------------------------------------------ reparto
CUERPO = {
 # ---- C1
 'molano': ('EDGAR MOLANO, the prosecutor, a Colombian man of about fifty, '
            'medium build, short dark hair greying at the temples, a neat '
            'short grey-flecked moustache, plain dark-rimmed reading glasses, '
            'in a plain navy-grey suit, a plain white shirt and a plain dark '
            'tie'),
 'yolanda': ('YOLANDA, a Colombian woman of twenty-nine, slight build, a round '
             'gentle face, straight dark hair in a low ponytail with a plain '
             'clip, in a plain grey long-sleeved blouse and plain dark '
             'trousers, and a plain matte mustard-yellow knitted cardigan worn '
             'OPEN over the blouse, hanging straight down the front on both '
             'sides'),
 'mama_yolanda': ('YOLANDA\'S MOTHER, a Colombian woman of about sixty, short '
                  'grey hair, reading glasses on a cord, in a plain grey '
                  'knitted jumper and a plain dark skirt'),
 'vecino': ('THE ACCUSED NEIGHBOUR, a man of about forty-five, seen ONLY AS A '
            'SOLID DARK SILHOUETTE: no face, no features, no skin tone'),
 'defensora': ('THE DEFENCE LAWYER, a Colombian woman of about forty-five, '
               'straight black hair in a neat low bun, in a plain black '
               'trouser suit over a plain white-grey blouse'),
 'juez': ('THE JUDGE, a Colombian man of about sixty, white hair combed back, '
          'a short trimmed white beard, in a plain dark grey suit and plain '
          'grey tie; no gown, no robe, no sash'),
 'psicologa': ('THE FORENSIC PSYCHOLOGIST, a Colombian woman of about forty, '
               'curly dark hair tied up, in a plain light grey cardigan over a '
               'plain white blouse, holding a plain notepad'),
 # ---- C2
 'jairo': ('JAIRO MONTERO SALAS, a university professor of Venezuelan origin, '
           'a man of about forty-five, lean, short black hair greying, a '
           'neatly trimmed short beard, round tortoiseshell glasses, in a '
           'plain light grey linen shirt with the sleeves rolled up and plain '
           'dark trousers'),
 'mauricio': ('MAURICIO REYES, Jairo\'s partner of more than eight years, a '
              'Colombian man of about forty-five, stocky, short wavy dark '
              'hair, clean-shaven, in a plain dark grey polo shirt'),
 'coronel': ('THE POLICE COLONEL, a heavy-set man in a plain dark suit, seen '
             'ONLY FROM BEHIND or over the shoulder: no face is ever visible; '
             'an ordinary civilian suit of completely plain smooth fabric with nothing sewn, pinned or printed on it anywhere'),
 'policias': ('SEVERAL POLICEMEN, bareheaded, in plain dark jackets and dark '
              'trousers of completely plain smooth fabric with nothing sewn, pinned or printed on it anywhere, small in the frame, '
              'their faces not readable'),
 'fiscal_c2': ('A PROSECUTOR in a plain charcoal jacket, seen ONLY FROM BEHIND, '
               'over the shoulder, or as hands at a desk: his face is never '
               'visible'),
 'activista': ('THE ACTIVIST, a Caribbean Colombian woman of about forty, one '
               'of the founders of the foundation, short natural curly hair, large '
               'plain hoop earrings, in a plain dark grey blouse'),
 'activistas': ('FOUR OR FIVE ACTIVISTS of different ages and builds in plain '
                'everyday clothes in shades of grey'),
 'estudiantes': ('A FEW UNIVERSITY STUDENTS seen from behind at their desks, '
                 'small in the frame'),
 # ---- C3
 'wilmer': ('WILMER, a patrolman, an Afro-Colombian man of about thirty, tall '
            'and broad-shouldered, very short black hair, clean-shaven, a calm '
            'steady face, in a plain dark navy field jacket and dark trousers '
            'of completely plain smooth fabric with nothing sewn, pinned or printed on it anywhere'),
 'companero': ('HIS PARTNER, a Colombian patrolman of about forty, short dark '
               'hair, a dark moustache, in the same dark navy field jacket '
               'of completely plain smooth fabric with nothing sewn, pinned or printed on it anywhere'),
 'agresores': ('TWO DRUNK PASSENGERS, men in plain light shirts, seen ONLY AS '
               'DARK SHAPES FROM BEHIND or in shadow: their faces are never '
               'readable'),
 'pasajeros': ('ORDINARY PASSENGERS in their seats, in plain clothes in shades '
               'of grey, several holding up their mobile phones to film, the '
               'screens lit with plain grey light and nothing legible on them'),
 'azafata': ('A FLIGHT ATTENDANT, a Colombian woman of about thirty-five, dark '
             'hair in a neat bun, in a plain dark grey uniform dress with no '
             'logo, no wings and no badge'),
 'fiscal_c3': ('THE PROSECUTOR ON DUTY, a man in a plain grey jacket, seen '
               'ONLY FROM BEHIND, over the shoulder, or as hands at a desk: his '
               'face is never visible'),
 'fiscal_revision': ('THE REVIEWING PROSECUTOR, a Colombian woman of about fifty, '
                     'short straight grey-streaked hair, plain thin-framed '
                     'glasses, in a plain charcoal blazer over a plain light '
                     'grey blouse'),
 'wilmer_civil': ('WILMER, the same patrolman, an Afro-Colombian man of about '
                  'thirty, tall and broad-shouldered, very short black hair, '
                  'clean-shaven, now off duty in a plain light grey shirt'),
 'periodista': ('A LOCAL REPORTER, a Colombian woman of about thirty, holding '
                'a plain handheld microphone with no logo, seen in '
                'three-quarter back view'),
 'jueza': ('THE JUDGE, a Colombian woman of about fifty-five, short dark '
           'hair, in a plain dark grey suit; no gown, no robe, no sash'),
 'reporteros': ('SEVERAL REPORTERS crowded together, seen from behind or as '
                'outstretched arms and hands holding plain microphones and '
                'plain recorders with no logo: their faces are not readable'),
 'mano': ('AN ANONYMOUS HAND of an ordinary adult, with its wrist and the cuff '
          'of a plain grey sleeve; no face anywhere'),
 # ---- C4
 'madre': ('THE MOTHER, an indigenous woman of the Amazonian foothills of '
           'Putumayo, about thirty-five, slim and strong, long straight black '
           'hair tied back, a few plain strings of small seed beads around her '
           'neck, in a plain matte mustard-yellow cotton blouse with short '
           'sleeves and a plain dark skirt, rubber boots'),
 'taita': ('HIPOLITO JACANAMIJOY, the Taita, seen ONLY AS A SOLID DARK '
           'SILHOUETTE: no face, no features, no skin tone; a tall carved '
           'wooden staff of authority in one hand'),
 'cabildantes': ('FIVE OR SIX AUTHORITIES OF THE CABILDO, indigenous men and '
                 'women of different ages from Putumayo, in plain everyday '
                 'clothes in shades of grey, some with plain strings of seed '
                 'beads around the neck'),
 'fiscal_c4': ('THE PROSECUTOR, a Colombian man of about thirty-eight, slim, '
               'short black hair, clean-shaven, in a plain light grey shirt '
               'with the sleeves rolled to the elbow and plain dark trousers, '
               'no jacket in the heat'),
 'colegas': ('TWO OR THREE COLLEAGUE PROSECUTORS in plain shirts, one woman and '
             'two men'),
 'funcionarios': ('SIX OR SEVEN OFFICIALS of different institutions around a '
                  'table, men and women in plain shirts and blouses in shades '
                  'of grey'),
 # ---- C5
 'valentina': ('VALENTINA, a trans woman of twenty-nine, slim, long dark wavy '
               'hair to below the shoulders, a calm composed face with defined '
               'brows, small plain earrings, in a plain grey high-neck blouse '
               'and plain dark trousers, and a plain matte mustard-yellow wool '
               'coat worn OPEN, hanging straight down the front on both sides'),
 'funcionario': ('THE RECEPTION OFFICIAL, a Colombian man of about fifty, '
                 'balding, in a plain pale grey shirt and a plain dark tie, seen '
                 'ONLY FROM BEHIND, over the shoulder, or as hands at the desk: '
                 'his face is never visible'),
 'expareja': ('A MAN seen ONLY AS A SOLID DARK SILHOUETTE far away under a '
              'street lamp: no face, no features'),
 'turno': ('SEVERAL ORDINARY PEOPLE waiting their turn in plain plastic '
           'chairs, in plain everyday clothes in shades of grey'),
}

VIDA = {
 'molano': ('A prosecutor of a unit for victims of sexual violence: '
            'methodical, he reads the file with his glasses on the tip of his '
            'nose and takes them off when he has to decide.'),
 'yolanda': ('She lives with her mother in the barrio. She speaks slowly and '
             'clearly, holds her own hands when she is nervous, and keeps a '
             'small plain notebook in her cardigan pocket.'),
 'mama_yolanda': ('Her mother and her support network.'),
 'defensora': ('A defence lawyer, serene and technical.'),
 'psicologa': ('A forensic psychologist who listens more than she writes.'),
 'jairo': ('A university professor and a well-known human rights defender, '
           'warm and outspoken; he always has a book or a folder under one '
           'arm.'),
 'mauricio': ('His partner of more than eight years; after the crime he keeps '
              'Jairo\'s house keys in his hand.'),
 'activista': ('She is one of the activists who created the foundation after Jairo\'s murder.'),
 'wilmer': ('Six years in the National Police; calm, patient, he speaks low '
            'and keeps his hands open.'),
 'companero': ('His partner on that night\'s shift.'),
 'azafata': ('A flight attendant who called the police.'),
 'fiscal_revision': ('The prosecutor who reviewed the case and named it.'),
 'madre': ('She walks the red-earth path every day; she carries her daughter\'s '
           'small school backpack when she goes to ask for justice.'),
 'fiscal_c4': ('A prosecutor of a small river-town office, unsure and '
               'conscientious; he rubs his forehead when he does not know.'),
 'valentina': ('She works and lives on her own; she is composed and direct, '
               'and she holds her identity card firmly in her hand.'),
}

# La prenda de acento de cada quien (biblia §6: una PRENDA, mate).
PRENDA = {
 'yolanda': 'her knitted cardigan',
 'jairo_camisa': 'the folded shirt',
 'madre': 'her cotton blouse',
 'valentina': 'her wool coat',
}
CON_ACENTO = {'yolanda', 'madre', 'valentina'}
SIN_ROSTRO = {'vecino', 'coronel', 'policias', 'fiscal_c2', 'estudiantes',
              'agresores', 'pasajeros', 'fiscal_c3', 'periodista', 'taita',
              'funcionario', 'expareja', 'turno', 'activistas', 'colegas',
              'funcionarios', 'cabildantes', 'reporteros', 'mano'}

# C3 es de noche y casi todo pasa bajo luz de techo (cabina, puesto de
# policia, terminal): el registro 'dia' habla de luz de dia; ahi se dice
# luz blanca de techo, con la misma estructura de valores (biblia §7: el
# registro es la estructura, no la hora).
NOCHE_INTERIOR = {'cabina', 'estacion_aeropuerto', 'terminal', 'sala_noche'}
REGISTRO = dict(REGISTRO)
REGISTRO['dia_noche'] = REGISTRO['dia'].replace(
    'ordinary daylight', 'ordinary flat white light from the ceiling lamps, '
    'night outside the windows,')

TOKENS = CUERPO

CORTO = True
C_ESTILO = ('STYLE: stylized editorial illustration, flat graphic treatment, no '
            'ink outline anywhere: forms built from broad soft tonal planes, '
            'never rendered shading, texture or brush marks. Large surfaces '
            'smooth, no material texture, no wood grain, no noise; a smooth '
            'gradient of light is allowed. ')
C_ROSTRO = ('Faces are drawn simplified and graphic: clear eyes with brow, '
            'simple nose and mouth, flat tonal planes with hard edges, no '
            'photographic detail, no caricature. ')
C_PIEL = ('Skin is a desaturated warm GREY, the same grey scale for every '
          'complexion -lighter or darker grey-, barely more coloured than a '
          'grey shirt: never pink, peach, tan or brown, no blush, no red lips. ')
C_FIGURA = ('Figures 8 to 8.5 heads tall, Colombian features carried by '
            'structure and hair. The environment is almost fully desaturated '
            'greys. Perfectly level camera, no dutch tilt, no fisheye, no lens '
            'flare, no bokeh discs.')
C_ACENTO = ('The ONLY saturated colour in the whole image is the muted MATTE '
            'mustard of %s (woven cloth, no glow, it goes into shadow with the '
            'cloth, never bright chrome or neon yellow); everything else is '
            'grey.')
C_LIMPIA = ('Clean plate: no legible text, letters or numbers anywhere, no '
            'logo, emblem, badge, insignia, flag, seal or coat of arms; any '
            'writing on paper or screens is plain flat grey bars.')
C_NEG = ('Not a photograph, not a 3D render, not painterly, no ink outlines, '
         'no anime eyes, no airbrushed skin, no motion blur. Nothing violent is '
         'shown: no blow, no weapon, no wound, no blood, no body.')
C_SILUETA = ('The people marked as silhouettes or seen only from behind never '
             'show a readable face.')


def arma(escena, registro='dia', personas=(), con_acento=None,
         con_lugar=True, con_rostro=True, lugar='despacho', silueta=False,
         exterior=None, prenda=None):
    """Arma el prompt final (la forma corta de `base_lp.arma`)."""
    quien = [p for p in personas if p in CON_ACENTO]
    if isinstance(con_acento, str):          # la prenda va en la ranura
        prenda, con_acento = con_acento, True
    if con_acento is None:
        con_acento = bool(quien) or bool(prenda)
    p = [escena.strip()]
    if personas:
        vidas = [VIDA[x] for x in personas if x in VIDA]
        if vidas:
            p.append('WHO THESE PEOPLE ARE. ' + ' '.join(vidas))
    p.append(REGISTRO['dia_noche'] if (registro == 'dia' and lugar in NOCHE_INTERIOR)
             else REGISTRO[registro])
    con_cara = con_rostro and any(x not in SIN_ROSTRO for x in personas)
    p.append(C_ESTILO + (C_ROSTRO if con_cara else '')
             + (C_PIEL if personas else '') + C_FIGURA)
    if silueta or any(x in SIN_ROSTRO for x in personas):
        p.append(C_SILUETA)
    if con_acento:
        cual = prenda or (PRENDA[quien[0]] if quien else 'the garment')
        p.append(C_ACENTO % cual)
    if con_lugar and LUGARES.get(lugar):
        p.append(LUGARES[lugar] + ' ' + COLOMBIA)
    p.append(C_LIMPIA)
    p.append(C_NEG)
    return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())
