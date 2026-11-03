# -*- coding: utf-8 -*-
r"""Cláusulas, lugares y reparto del curso «Ley 1826 de 2017: procedimiento
penal especial abreviado y acusador privado» (PRIORIDAD 1).

EL SISTEMA ES EL DE LA SERIE, SIN UNA COMA DE MÁS
    Lo de estilo se importa de `base_df_v1` tal cual, como en Derechos
    humanos (rostros dibujados y simplificados, piel gris cálida, tres
    registros de luz, superficie lisa, el acento como PRENDA mate). La sala
    viene de `base_gj`. Lo propio de este curso es el MUNDO y el REPARTO.

LO QUE NO SE DIBUJA NUNCA (la regla de toda la serie)
    Ningún golpe, ninguna agresión, ningún arma en una mano, ninguna herida.
    El agresor y quien amenaza entran como SILUETA (regla del 27 oct). Los
    servidores que deciden mal -el asistente que redacta mal, el fiscal que
    cita a conciliación lo que no es querellable, el fiscal que lleva el
    audio de la mediación al juicio- no llevan cara: manos, espalda, sobre
    el hombro. El procesado se presume inocente: de espaldas o sin rasgos.
    Ningún texto legible, ninguna marca (tampoco «Kombucha Valle» en una
    etiqueta: la etiqueta es un rectángulo liso), ninguna placa de carro
    legible, ningún escudo ni bandera.

EL ACENTO
    Un solo color saturado por composición: la prenda mostaza mate de la
    víctima (María T.C. en la U1, María Elena en la U2, la ciudadana de la
    U4 C3). Donde no hay víctima en cuadro no hay acento.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
from base_df_v1 import (PIEL, ROSTRO, PLANOS, REGISTRO, CAMARA, LIMPIA,  # noqa
                        SIN_ROLES, SILUETA, ESTILO, FIGURA, ACENTO, NEG)
from base_gj import SALA as _SALA_GJ           # noqa: E402

PIEL_LP = ('Every person here, whatever their complexion, has skin drawn in '
           'the SAME grey scale: lighter or darker GREY with only a faint warm '
           'tint, barely more coloured than a grey shirt. No peach, no tan, no '
           'olive, no pink cheeks, no rosy nose or ears, no red lips, no blush '
           'and no orange or red in the shadows of the face and hands.')

# ------------------------------------------------------------------ lugar
BARRIO = ('The setting is a working-class residential barrio of a Colombian '
          'city: two and three storey houses built flush to the pavement in '
          'exposed clay brick and plain rendered concrete, FLAT concrete roofs '
          'with short steel bars standing up from an unfinished top floor, a '
          'plain metal security grille on every ground-floor window and door, '
          'square concrete utility poles with thick bundles of black cable, a '
          'raised concrete kerb, and hazy mountains behind the rooftops. Never '
          'pitched roofs, never chimneys, never front gardens. No shop sign, '
          'no lettering anywhere.')

CASA = ('The setting is the inside of a modest rented home in a Colombian '
        'city barrio: plain painted masonry walls, a plain tiled floor, a small '
        'living-dining room with a plain table and four plain chairs, a narrow '
        'kitchen counter, a plain wooden door with an ordinary lock, a window '
        'with a plain metal grille and a thin curtain. Ordinary, tidy, nothing '
        'lavish. No picture, no calendar, no lettering anywhere.')

DESPACHO = ('The setting is the office of a prosecutor in a Colombian city: a '
            'plain grey desk with an ordinary computer screen and a desk '
            'telephone, metal shelving full of cardboard case folders, two plain '
            'visitor chairs, a window with a plain blind, and a plain round wall '
            'clock with hands and NO numerals. No logo, no seal, no flag, no '
            'portrait, no diploma on the wall, no lettering anywhere.')

OFICINA = ('The setting is a busy open-plan office of a Colombian prosecution '
           'office: rows of plain grey desks, ordinary computer screens, '
           'stacks of cardboard case folders, plain metal shelving, plain '
           'office chairs, flat fluorescent tube light. No logo, no seal, no '
           'flag, no poster, no lettering anywhere.')

SALA = (_SALA_GJ + ' The layout: the judge sits at the centre behind a plain '
        'desk on a low plain platform; the prosecution table on one side, the '
        'defence table on the other, and a few rows of plain public benches at '
        'the back. A plain microphone on a short stand on each table.')

CONSULTORIO = ('The setting is a small plain forensic medical examination room: '
               'a plain examination couch with a paper sheet, a plain desk with '
               'a computer screen, a small plain cabinet, plain painted walls, '
               'a window with a plain blind. Clean and bare. No poster, no '
               'chart, no logo, no lettering anywhere.')

BODEGAS = ('The setting is a street in the industrial district of Cali, '
           'Colombia, in hot flat daylight: long low warehouses with plain '
           'corrugated metal roll-up doors, plain rendered concrete walls, a '
           'wide cracked concrete road, square concrete utility poles with '
           'bundles of black cable, a few tall palms far away and green hills '
           'hazy in the distance. No sign, no logo, no lettering anywhere.')

SALA_MEDIACION = ('The setting is a small plain mediation room: one round plain '
                  'table with three plain chairs around it, a jug of water and '
                  'plain glasses, plain painted walls, a window with a plain '
                  'blind. Calm, neutral, nobody at the head of the table. No '
                  'logo, no poster, no lettering anywhere.')

LADERA = ('The setting is a hillside barrio of Medellín, Colombia: dense '
          'stacked houses of exposed clay brick and plain rendered concrete '
          'climbing the steep slope, flat concrete roofs, narrow concrete '
          'stairways between them, tangled cables on concrete poles, and the '
          'wide valley of the city below under a pale sky. No sign, no '
          'lettering anywhere.')

OFICINA_EMPRESA = ('The setting is the small plain office of a zone supervisor in a '
                   'beverage distribution company in Cali: a plain desk with an '
                   'ordinary computer screen, a plain metal filing cabinet, '
                   'stacked plain cardboard crates against a wall, a window with a '
                   'plain blind onto the warehouse yard. No logo, no brand, no '
                   'poster, no lettering anywhere.')

SALA_ENTREVISTAS = ('The setting is a small plain interview room of a judicial '
                    'police office: a plain table, two plain chairs facing each '
                    'other, a plain notebook and pen, plain painted walls, one '
                    'window with a plain blind. No logo, no seal, no poster, no '
                    'lettering anywhere.')

VENTANILLA = ('The setting is the filing counter of a Colombian prosecution '
              'office: a plain counter with a pane of plain glass and a low '
              'opening in it, an official behind it at a grey desk, stacks of '
              'plain folders, fluorescent tube light. No logo, no seal, no '
              'flag, no poster, no lettering anywhere.')

CALLE_BOGOTA = ('The setting is a street of Bogota, Colombia, on a grey overcast '
                'day: three and four storey buildings of exposed red-brown clay '
                'brick with plain windows, a plain concrete pavement, square '
                'concrete utility poles with cables, small cars, and the steep '
                'green eastern hills rising behind the rooftops under low cloud. '
                'No sign, no logo, no lettering anywhere.')

CRUCE = ('The setting is an ordinary street crossing in a Colombian city on an '
         'overcast day: plain rendered concrete buildings of two and three '
         'storeys, a plain asphalt road with faded white lines, square concrete '
         'utility poles with cables, a plain traffic light on a pole. No sign, no '
         'logo, no lettering, no number plate characters anywhere.')

LUGARES = {'barrio': BARRIO, 'casa': CASA, 'despacho': DESPACHO,
           'oficina': OFICINA, 'sala': SALA, 'consultorio': CONSULTORIO,
           'bodegas': BODEGAS, 'mediacion': SALA_MEDIACION, 'ladera': LADERA,
           'oficina_empresa': OFICINA_EMPRESA, 'sala_entrevistas': SALA_ENTREVISTAS,
           'ventanilla': VENTANILLA, 'calle_bogota': CALLE_BOGOTA, 'cruce': CRUCE,
           'ninguno': ''}

# ------------------------------------------------------------------ reparto
CUERPO = {
 # ---- U1 (láminas): el mismo expediente en los cinco casos
 'maria': ('MARIA T.C., a mestiza Colombian woman of about thirty, slim, '
           'straight black hair to the shoulders, in a plain light grey '
           'long-sleeved blouse and plain dark grey trousers, and a plain '
           'matte mustard-yellow knitted scarf wrapped once around her neck, '
           'its ends hanging down the front'),
 'jose': ('JOSE A.C., a man of about thirty-five, broad-shouldered, seen ONLY '
          'AS A SOLID DARK SILHOUETTE: no face, no features, no skin tone'),
 'asistente': ('A PROSECUTOR\'S ASSISTANT, a young Colombian man in a plain '
               'light grey shirt, seen ONLY FROM BEHIND or as hands and '
               'forearms at a desk, his face never visible'),
 'defensora': ('A DEFENCE LAWYER, a Colombian woman of about forty-five, '
               'straight black hair in a neat low bun, in a plain black '
               'trouser suit over a plain white-grey blouse'),
 'perito': ('A FORENSIC DOCTOR, a Colombian man of about fifty, short grey '
            'hair, in a plain white coat over a plain grey shirt'),
 # ---- U3 (láminas)
 'apoderado': ('THE VICTIMS\' LAWYER, a Colombian man of about forty, short '
               'black hair, neat short beard, in a plain dark grey suit and '
               'plain grey tie, holding a slim plain folder'),
 'inversionistas': ('FIFTEEN ORDINARY COLOMBIAN PEOPLE of different ages, in '
                    'plain everyday clothes in shades of grey, small in the '
                    'frame'),
 'comerciante': ('A SHOP OWNER, a Colombian woman of about fifty, short '
                 'curly dark hair, in a plain grey work apron over a plain dark '
                 'blouse'),
 'acusador': ('THE PRIVATE ACCUSER, a lawyer, seen ONLY AS A SOLID DARK '
              'SILHOUETTE in a suit: no face, no features'),
 # ---- U2 C1 (Cali)
 'supervisor': ('JORGE ELIECER BENAVIDES, the zone supervisor, a Colombian man '
                'of about forty-five, stocky, short black hair greying at the '
                'temples, a short black moustache, in a plain light grey '
                'short-sleeved work shirt and plain dark grey trousers, a plain '
                'dark lanyard with a blank card'),
 'contratista': ('MARIO ALBERTO, the contractor, a Colombian man of about '
                 'thirty-five in a plain dark grey polo shirt and jeans, seen '
                 'ONLY FROM BEHIND or in three-quarter back view, his face '
                 'never readable'),
 'transportador': ('PEDRO ANTONIO, the former driver, a Colombian man of about '
                   'fifty in a plain grey cap and a plain charcoal T-shirt, '
                   'seen ONLY FROM BEHIND or in three-quarter back view, his '
                   'face never readable'),
 'vigilante': ('A SECURITY GUARD of the company, a Colombian man of about fifty, '
               'short grey hair, a plain grey work shirt with no badge, no patch '
               'and no lettering'),
 'investigador': ('A JUDICIAL POLICE INVESTIGATOR seen ONLY FROM BEHIND, over the '
                  'shoulder, in a plain dark jacket, his face never visible'),
 # ---- U2 C2 (Medellín)
 'mariaelena': ('MARIA ELENA GUTIERREZ RIOS, a mestiza Colombian woman of '
                'about forty, medium build, wavy dark hair tied back, in a '
                'plain grey blouse and plain dark trousers, and a plain matte '
                'mustard-yellow knitted cardigan worn OPEN over the blouse, '
                'hanging straight down the front on both sides'),
 'carloseduardo': ('CARLOS EDUARDO, the accused, seen ONLY AS A SOLID DARK '
                   'SILHOUETTE: no face, no features, no skin tone'),
 'armados': ('TWO OR THREE MEN seen ONLY AS DARK SILHOUETTES far away, no '
             'faces, no weapon visible'),
 'fiscal_mujer': ('THE PROSECUTOR, a Colombian woman of about forty-eight, '
                  'dark hair cut to the jaw, plain thin-framed glasses, in a '
                  'plain charcoal grey blazer over a plain light grey blouse'),
 'juez': ('THE JUDGE OF GUARANTEES, a Colombian man of about sixty, white hair '
          'combed back, a short trimmed white beard, in a plain dark grey suit '
          'and plain grey tie; no gown, no robe, no sash'),
 'defensor': ('THE DEFENCE LAWYER, a Colombian man of about fifty, bald with '
              'grey at the sides, plain dark-rimmed glasses, in a plain navy-'
              'grey suit and plain grey tie'),
 # ---- U4
 'fiscal_sin_cara': ('THE PROSECUTOR, a Colombian man in a plain charcoal '
                     'jacket over a plain light grey shirt, seen ONLY FROM '
                     'BEHIND, over the shoulder, or as hands at a desk: his '
                     'face is never visible'),
 'indiciado': ('THE ACCUSED, a Colombian man of about thirty-five, in a plain '
               'grey hooded jacket, seen ONLY FROM BEHIND or in three-quarter '
               'back view, his face never readable'),
 'mediador': ('THE MEDIATOR, a Colombian man of about fifty-five, short grey '
              'hair, a neat grey beard, plain round glasses, in a plain soft grey '
              'cardigan over a plain light shirt'),
 'lesionado': ('THE INJURED PERSON, a Colombian man of about forty, short '
               'black hair, his left forearm in a plain grey sling, in a plain '
               'grey shirt'),
 'conductor': ('THE DRIVER, the accused, a Colombian man of about thirty, seen '
               'ONLY FROM BEHIND or in three-quarter back view, his face never '
               'readable, in a plain dark grey jacket'),
 'ciudadana': ('THE CITIZEN, a mestiza Colombian woman of about twenty-eight, '
               'slim, long dark hair in a low ponytail, in a plain grey blouse '
               'and plain dark jeans, and a plain matte mustard-yellow knitted '
               'cardigan worn OPEN over the blouse'),
 'estudiante': ('A YOUNG LAW-CLINIC LAWYER from a university, a Colombian man '
                'of about twenty-four, short curly black hair, clean-shaven, in '
                'a plain light grey shirt buttoned to the collar and a plain '
                'dark grey sweater, carrying a plain grey folder'),
}

VIDA = {
 'maria': ('She lives in a small rented home in barrio Prado Alto. She keeps '
           'her own counsel; her hands do the talking.'),
 'defensora': ('A defence lawyer, serene and technical, who keeps a slim '
               'black folder closed in front of her until she needs it.'),
 'supervisor': ('He has followed his distribution zone for months. He records '
                'with his mobile phone held flat in both hands.'),
 'mariaelena': ('She has lived for three years under threat in her own home. '
                'She holds her plain handbag close and keeps her back to the '
                'wall.'),
 'fiscal_mujer': ('A prosecutor who acts fast: the protection measure, the '
                  'transfer, the request to the judge.'),
 'mediador': ('A mediator of the judicial district: he listens with his hands '
              'flat on the table and never takes sides.'),
 'ciudadana': ('She came to the prosecutor\'s office to withdraw her complaint. '
               'She keeps her eyes on her own hands.'),
 'estudiante': ('A young lawyer from a university law clinic, careful and a '
                'little nervous, who speaks for her.'),
}

CON_ACENTO = {'maria', 'mariaelena', 'ciudadana'}
SIN_ROSTRO = {'investigador', 'jose', 'asistente', 'acusador', 'contratista', 'transportador',
              'carloseduardo', 'armados', 'fiscal_sin_cara', 'indiciado',
              'conductor', 'inversionistas'}

TOKENS = CUERPO


# 3 nov: la version CORTA de las clausulas de la serie (la de las laminas,
# que salio bien con Seedream 5 Flash): las mismas reglas en un tercio del
# texto. `arma` la usa cuando CORTO es True.
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
          'complexion, barely more coloured than a grey shirt: never pink, '
          'peach, tan or brown, no blush, no red lips. ')
C_FIGURA = ('Figures 8 to 8.5 heads tall, Colombian features carried by '
            'structure and hair. The environment is almost fully desaturated '
            'greys. Perfectly level camera, no dutch tilt, no fisheye, no lens '
            'flare, no bokeh discs.')
C_ACENTO = ('The ONLY saturated colour in the whole image is the muted MATTE '
            'mustard of her knitted garment (woven cloth, no glow, it goes into '
            'shadow with the garment, never bright chrome or neon yellow); '
            'everything else is grey.')
C_LIMPIA = ('Clean plate: no legible text, letters or numbers anywhere, no '
            'logo, emblem, badge, flag, seal or coat of arms; any writing on '
            'paper or screens is plain flat grey bars.')
C_NEG = ('Not a photograph, not a 3D render, not painterly, no ink outlines, '
         'no anime eyes, no airbrushed skin, no motion blur. Nothing violent is '
         'shown: no blow, no weapon in a hand, no wound, no blood.')
C_SILUETA = ('The people marked as silhouettes are SOLID DARK SHAPES with no '
             'facial features of any kind.')


def arma(escena, registro='dia', personas=(), con_acento=None,
         con_lugar=True, con_rostro=True, lugar='despacho', silueta=False,
         exterior=None):
    """Arma el prompt final (la forma de `base_dh.arma`)."""
    if con_acento is None:
        con_acento = any(p in CON_ACENTO for p in personas)
    if CORTO:
        p = [escena.strip()]
        if personas:
            vidas = [VIDA[x] for x in personas if x in VIDA]
            if vidas:
                p.append('WHO THESE PEOPLE ARE. ' + ' '.join(vidas))
        p.append(REGISTRO[registro])
        con_cara = con_rostro and any(x not in SIN_ROSTRO for x in personas)
        p.append(C_ESTILO + (C_ROSTRO if con_cara else '')
                 + (C_PIEL if personas else '') + C_FIGURA)
        if silueta or any(x in SIN_ROSTRO for x in personas):
            p.append(C_SILUETA if silueta else '')
        if con_acento:
            p.append(C_ACENTO)
        if con_lugar and LUGARES.get(lugar):
            p.append(LUGARES[lugar])
        p.append(C_LIMPIA)
        p.append(C_NEG)
        return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())
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
                 + (PIEL + ' ' + PIEL_LP + ' ' if personas else '') + FIGURA)
    p.append(CAMARA)
    if con_acento:
        p.append(ACENTO)
    if con_lugar and LUGARES.get(lugar):
        p.append(LUGARES[lugar])
    p.append(LIMPIA)
    p.append(SIN_ROLES)
    p.append(NEG)
    return '\n\n'.join(x.strip() for x in p if x and x.strip())
