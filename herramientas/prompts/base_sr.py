# -*- coding: utf-8 -*-
r"""Cláusulas, lugares y reparto de los CASOS del curso «Sistema de
responsabilidad penal para adolescentes y justicia restaurativa» (PRIORIDAD 1).

EL SISTEMA ES EL DE LA SERIE
    Las cláusulas cortas de `base_ed` (Ley 1826, Enfoque diferencial,
    Estándares interamericanos), tal cual: rostros dibujados y simplificados,
    piel gris cálida, tres registros de luz, superficie lisa, cámara a nivel,
    placa limpia, entorno casi del todo en grises (la regla de color de
    Sebastián: gris predominante, un solo color, en una prenda o un objeto).

EL MUNDO DE NICO
    San Miguel de los Andes, «municipio del departamento de Cundinamarca»: un
    pueblo andino frío de la sabana y sus bordes (ruanas, gorros de lana,
    chaquetas, montañas con niebla). No existe; se dibuja como los pueblos
    reales de Cundinamarca (la plaza de mercado cubierta de concreto y teja de
    zinc, el puente peatonal metálico sobre la vía que entra al pueblo, casas
    de ladrillo y de bahareque encalado). Después: la Policía, el Centro de
    Internamiento Preventivo, la sala de entrevistas del defensor, el pasillo
    del juzgado y el Centro de Atención Especializada.

EL ACENTO (un solo color saturado por composición, una PRENDA mate)
    Nico · su buzo con capucha MOSTAZA, viejo, desteñido, con los puños
    deshilachados. Es lo único suyo que atraviesa la pieza: bajo el puente,
    en la plaza, en la patrulla, con el defensor, en el CAE. Al final queda
    doblado sobre la cama del aislamiento.

LO QUE NO SE DIBUJA NUNCA (biblia §3 y la regla de toda la serie)
    Ningún golpe, ninguna patada, ninguna agresión en acto, ninguna herida
    abierta, nada de sangre, ningún arma. La agresión se cuenta con lo que la
    rodea: el corro de espaldas, el caldo derramado en el andén, el teléfono
    que graba, el chico en el suelo cubriéndose el rostro (es lo que el
    documento dice que muestra el video), sin nadie golpeándolo en cuadro.
    Los comerciantes que lo persiguen y lo golpean: SILUETA o de espaldas,
    nunca una cara legible. La vendedora que lo ayuda sí tiene cara.
    Ninguna decisión equivocada cae sobre una cara (biblia §3): el consejo del
    defensor va sobre el hombro y en las manos; la orden de raparlo y la de
    aislarlo, en manos, espaldas y la tabla de la funcionaria. Las omisiones
    de los policías, en planos generales y de espaldas.
    Nico es un ADOLESCENTE de 15 años (ficticio): se dibuja con dignidad,
    flaco y cansado pero entero, nada de su cuerpo subrayado, nunca
    caricatura de «niño de la calle»; en la valoración médica se ve vestido,
    descalzo a lo sumo, y las lesiones son una sombra gris en el pómulo.
    Policía: el uniforme de servicio de la Policía Nacional
    (`base_ed.UNIFORME_POLICIA`), sin letras, insignias, escudo ni arma.
    Ningún texto, logo, bandera ni escudo en ninguna parte.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
from base_ed import (REGISTRO as _REGISTRO_ED, C_ESTILO, C_ROSTRO, C_PIEL,  # noqa: E402
                     C_LIMPIA, C_SILUETA, UNIFORME_POLICIA, UNIFORME_CORTO,
                     PASILLO, SALA)

COLOMBIA = ('This is Colombia, a cold Andean town of Cundinamarca, and the '
            'buildings, the streets, the vehicles and the people must say so; '
            'never Europe, never the United States, never an English village.')

C_FIGURA = ('Adults 8 to 8.5 heads tall; the boy is a thin adolescent of '
            'fifteen, about seven and a half heads tall, clearly younger and '
            'slighter than the grown men around him. Colombian features carried '
            'by structure and hair. The environment is almost fully desaturated '
            'greys: only the faintest trace of colour left in the greys, close '
            'to neutral grey but not quite monochrome. Perfectly level camera, '
            'no dutch tilt, no fisheye, no lens flare, no bokeh discs.')

C_ACENTO = ('The ONLY saturated colour in the whole image is the muted MATTE '
            'mustard-yellow of %s (worn, faded woven cotton, no glow, it goes '
            'into shadow with the cloth, never bright chrome or neon yellow); '
            'everything else is grey.')

C_SIN_ACENTO = ('Nothing in the image is saturated: no bright colour anywhere, '
                'no orange, no red, no saturated yellow.')

C_NICO = ('The boy is an ordinary fifteen-year-old drawn with dignity and '
          'restraint: thin and tired but whole, fully dressed, nothing about '
          'his body emphasized, never a caricature of a street child.')

C_NEG = ('Not a photograph, not a 3D render, not painterly, no ink outlines, '
         'no anime eyes, no airbrushed skin, no motion blur. Nothing violent is '
         'shown: no blow, no kick, no raised fist, no weapon, no wound, no '
         'blood.')

# ------------------------------------------------------------------ lugares
PUEBLO = ('The setting is San Miguel de los Andes, a small cold Andean town of '
          'Cundinamarca, Colombia, high on the savanna edge: two-storey houses '
          'of exposed clay brick and of whitewashed adobe with plain wooden '
          'doors and small wooden balconies, some with low-pitched roofs of '
          'faded clay tiles and others with flat concrete roofs with steel bars '
          'sticking up, square concrete utility poles with thick bundles of '
          'black cables, motorcycles parked on the pavement, small buses, green '
          'Andean mountains in grey mist close behind the roofs. No sign, no '
          'brand, no lettering anywhere.')
PUENTE = ('The setting is a pedestrian footbridge over the main road that enters '
          'a small Andean town of Cundinamarca: a plain grey painted steel truss '
          'walkway on concrete pillars, with a long concrete stair at each end; '
          'under the stair and the first span, against the concrete abutment, a '
          'narrow strip of bare earth and weeds sheltered from the rain; beyond, '
          'the road with small buses and motorcycles, brick houses, and two '
          'blocks away the long low corrugated roof of the municipal market; '
          'misty green mountains behind. No sign, no graffiti, no lettering '
          'anywhere.')
CAMBUCHE = ('Under the footbridge stair, his sleeping place: flattened cardboard '
            'boxes laid on the ground as a mattress, two worn grey woollen '
            'blankets, a few folded old clothes used as a pillow, a knotted '
            'plastic bag with his things. Nothing written on the cardboard.')
PLAZA = ('The setting is the covered municipal market (plaza de mercado) of a '
         'small Andean town of Cundinamarca, Colombia: a large open hall with a '
         'high roof of corrugated sheets on plain steel trusses, plain concrete '
         'columns, a worn concrete floor; rows of stalls with plain wooden '
         'counters heaped with potatoes, plantains, onions and fruit in plain '
         'baskets and sacks, bunches of herbs hanging; vendors in plain white '
         'aprons; shoppers in woollen ruanas, wool caps and jackets; through '
         'the wide open entrances the grey street and the misty mountains. No '
         'sign, no price tag, no poster, no brand, no lettering anywhere.')
COMEDOR = ('The setting is the food section (comedores) inside the covered '
           'municipal market of a small Andean town of Cundinamarca: small '
           'open kitchen stalls side by side, each with a counter, big dented '
           'aluminium pots steaming on gas burners, a griddle with arepas, '
           'tamales wrapped in green-grey plantain leaves stacked on a tray, '
           'plain enamel cups, and in front of each stall a long plain wooden '
           'table with plain wooden benches covered with a plain oilcloth; '
           'the high corrugated roof on steel trusses above, concrete columns. '
           'No sign, no menu board, no price, no brand, no lettering anywhere.')
DESAYUNO = ('THE BREAKFAST on the table: a tamal unwrapped on its plantain leaf '
            'on a plain plate, a deep plain bowl of clear rib broth (caldo de '
            'costilla) with a rib bone and potato, and a plain enamel mug of hot '
            'chocolate; a spoon, a small arepa.')
ANDEN = ('The setting is the pavement in front of the municipal market of a '
         'small Andean town of Cundinamarca: a wide worn concrete sidewalk with '
         'a raised kerb, the market\'s wide entrance and concrete columns, '
         'parked motorcycles, a small bus passing, brick houses opposite, misty '
         'mountains. No sign, no lettering anywhere.')
PATRULLA = ('THE PATROL VEHICLE: a plain white double-cab pickup truck of the '
            'Colombian National Police with a plain dark green stripe along its '
            'side and a plain light bar on the cab roof, switched off; nothing '
            'written on it: no word, no number, no emblem.')
CIP = ('The setting is the admission corridor of a centre for the preventive '
       'internment of adolescents in Colombia: a long plain corridor with walls '
       'painted pale grey to shoulder height and white above, a plain steel '
       'door with a small square window, a plain wooden bench, a plain wall '
       'clock with hands and no numerals, fluorescent tube lights. No sign, no '
       'notice, no logo, no lettering anywhere.')
SALA_DEFENSA = ('The setting is a small plain interview room for private '
                'conversations with a defence lawyer: a small plain grey table, '
                'two plain chairs facing each other, bare walls painted pale '
                'grey, a single high window with flat daylight, a plain closed '
                'door. Nothing on the walls, no logo, no lettering anywhere.')
DESPACHO_DEFENSOR = ('The setting is a small crowded office of public defenders '
                     'in a Colombian town: a plain grey desk under tall stacks of '
                     'cardboard case folders tied with string, a plain computer '
                     'screen showing only grey bars, a plain desk telephone, '
                     'metal shelving full of folders, a window with a plain '
                     'blind. No logo, no seal, no flag, no diploma, no lettering '
                     'anywhere.')
CAE_FACHADA = ('The setting is the entrance of a specialised care centre for '
               'adolescents (CAE) on the edge of a Colombian Andean town: a long '
               'plain two-storey institutional building painted pale grey and '
               'white, a high plain perimeter wall, a sliding plain grey steel '
               'gate, a guard booth, a few young trees, misty mountains behind. '
               'No sign, no logo, no flag, no coat of arms, no lettering '
               'anywhere.')
CAE_RECEPCION = ('The setting is the admission office of a specialised care '
                 'centre for adolescents in Colombia: a plain grey desk with a '
                 'plain computer screen showing only grey bars, a plain metal '
                 'chair in front of it, plain walls painted pale grey, a plain '
                 'filing cabinet, a window with a plain blind, a plain wall clock '
                 'with hands and no numerals. No poster, no logo, no lettering '
                 'anywhere.')
ENFERMERIA = ('The setting is the small nursing room of a specialised care '
              'centre for adolescents in Colombia: a plain examination couch '
              'covered with a strip of white paper, a plain white metal cabinet, '
              'a plain grey medical floor scale, a plain sink, a plain '
              'goose-neck examination lamp, plain pale grey walls, a window with '
              'a plain blind. No poster, no chart, no logo, no lettering '
              'anywhere.')
LAVADERO = ('The setting is a plain washroom of a specialised care centre for '
            'adolescents: walls of plain pale grey tiles to shoulder height, a '
            'plain concrete floor with a drain, a row of plain sinks along one '
            'wall, NO mirror anywhere, a single plain plastic chair in the '
            'middle of the floor. No poster, no logo, no lettering anywhere.')
PATIO_CAE = ('The setting is the common room of a specialised care centre for '
             'adolescents in Colombia: plain tables and plastic chairs, plain pale '
             'grey walls, high windows with flat daylight, a table-football game '
             'and a plain shelf with a few board games. No poster, no logo, no '
             'lettering anywhere.')
AISLAMIENTO = ('The setting is a small bare single room of a specialised care '
               'centre for adolescents: a narrow plain concrete bed base with a '
               'thin plain mattress and a plain grey blanket, bare walls painted '
               'pale grey, a single small high window letting in flat daylight, '
               'a plain grey steel door. Nothing on the walls, no lettering '
               'anywhere.')
PASILLO_JUZGADO = PASILLO

LUGARES = {
 'pueblo': PUEBLO, 'puente': PUENTE, 'cambuche': PUENTE + ' ' + CAMBUCHE,
 'plaza': PLAZA, 'comedor': COMEDOR, 'desayuno': COMEDOR + ' ' + DESAYUNO,
 'anden': ANDEN, 'patrulla': ANDEN + ' ' + PATRULLA, 'cip': CIP,
 'sala_defensa': SALA_DEFENSA, 'despacho_defensor': DESPACHO_DEFENSOR,
 'pasillo': PASILLO_JUZGADO, 'cae_fachada': CAE_FACHADA,
 'cae_recepcion': CAE_RECEPCION, 'enfermeria': ENFERMERIA,
 'lavadero': LAVADERO, 'patio_cae': PATIO_CAE, 'aislamiento': AISLAMIENTO,
 'ninguno': '',
}
EXTERIOR = {'pueblo', 'puente', 'cambuche', 'anden', 'patrulla', 'cae_fachada'}

# ------------------------------------------------------------------ reparto
# 7 nov (DA V03 r17, y la lección de ED): un token en MAYÚSCULA pegado a una
# prenda se imprime en la prenda. Los tokens van en minúscula y la ropa se
# describe en positivo.
HUDI = ('a worn, faded matte mustard-yellow hooded sweatshirt (his only warm '
        'garment) with frayed cuffs and a stretched hem, worn closed, the hood '
        'down on his shoulders')
CUERPO = {
 'nico': ('the boy, a Colombian mestizo adolescent of fifteen, thin and small '
          'for his age, a narrow face with high cheekbones and dark tired eyes, '
          'straight black hair grown long and uneven over his ears and '
          'forehead, wearing ' + HUDI + ', worn dark grey tracksuit trousers a '
          'little short at the ankle, and old grey canvas sneakers with split '
          'soles'),
 'nico_rapado': ('the boy, a Colombian mestizo adolescent of fifteen, thin and '
                 'small for his age, a narrow face with high cheekbones and dark '
                 'tired eyes, his head now SHAVED to the scalp, wearing ' + HUDI
                 + ', worn dark grey tracksuit trousers'),
 'vendedora': ('a market cook, a Colombian woman of about fifty-five from the '
               'Andean countryside, sturdy, a round kind face, greying hair in a '
               'low bun under a plain white kerchief, a plain white apron over a '
               'plain grey woollen sweater with the sleeves pushed up'),
 'comerciantes': ('market merchants, grown men in plain white aprons over plain '
                  'dark sweaters and jackets, seen ONLY FROM BEHIND or as dark '
                  'silhouettes against the light: no face is ever readable'),
 'comerciante': ('a market merchant, a grown man in a plain white apron over a '
                 'plain dark sweater, seen ONLY FROM BEHIND or as a dark '
                 'silhouette: his face is never readable'),
 'cliente': ('a Colombian family man of about forty, short black hair, a short '
             'moustache, in a plain grey padded jacket over a plain shirt'),
 'familia': ('his wife, a Colombian woman of about thirty-eight with dark hair '
             'tied back in a plain grey woollen ruana, and their daughter, a '
             'girl of about eight in a plain grey jacket, sitting beside him'),
 'policias': ('two patrolmen of the Colombian National Police in ' + UNIFORME_CORTO
              + ', grown men of about thirty'),
 'policia': ('a patrolman of the Colombian National Police in ' + UNIFORME_CORTO
             + ', a grown man of about thirty'),
 'defensor': ('the public defender, a Colombian man of about fifty-five, '
              'heavy-set, thinning grey-black hair combed back, plain reading '
              'glasses, in a plain grey suit jacket over a plain light grey shirt '
              'with no tie, a thin plain cardboard folder'),
 'funcionaria': ('a staff member of the centre, a Colombian woman of about '
                 'forty-five, dark hair tied back, in a plain light grey cardigan '
                 'over a plain white blouse, a plain clipboard in her hands'),
 'funcionarios': ('two staff members of the centre, a woman in a plain light '
                  'grey cardigan and a man in a plain dark grey polo shirt, seen '
                  'ONLY FROM BEHIND or with their faces turned away'),
 'enfermera': ('the centre\'s nurse, a Colombian woman of about thirty-five, '
               'dark curly hair tied up, in a plain white-grey nurse\'s tunic '
               'and trousers, plain pale blue-grey disposable gloves'),
 'jovenes': ('three other adolescents of the centre, boys of about sixteen in '
             'plain grey sweatshirts, seen from behind or in profile, at a '
             'distance'),
 'transeuntes': ('townspeople in plain woollen ruanas, wool caps and jackets'),
 'escolares': ('schoolchildren of about twelve in plain grey school tracksuits '
               'with plain backpacks, walking in a small group'),
}
# las prendas del acento, para las cláusulas
PRENDA = {'nico': 'his hooded sweatshirt', 'nico_rapado': 'his hooded sweatshirt'}
CON_ACENTO = {'nico', 'nico_rapado'}
SIN_ROSTRO = {'comerciantes', 'comerciante', 'funcionarios', 'jovenes'}
PATRULLEROS = {'policias', 'policia'}

VIDA = {
 'nico': ('He has lived for months under the footbridge near the market; he '
          'has no papers and nobody looks after him; the mustard hooded '
          'sweatshirt and a knotted plastic bag are all he owns.'),
 'nico_rapado': ('He has lived for months under the footbridge; the mustard '
                 'hooded sweatshirt is all he still has of his own.'),
 'vendedora': ('She has cooked breakfasts in the market for thirty years and '
               'sometimes keeps a portion aside for the boy.'),
 'defensor': ('A public defender with far too many cases, always with a thin '
              'folder under his arm and his reading glasses in his hand.'),
 'enfermera': ('She examines every adolescent who arrives and writes it all '
               'down on her clipboard.'),
}

REGISTRO = dict(_REGISTRO_ED)

TOKENS = CUERPO
CORTO = True


def arma(escena, registro='dia', personas=(), acento=None, lugar='ninguno',
         con_rostro=True, fuego=False):
    """El prompt final. `acento`: lo que lleva el mostaza (el buzo de Nico) o
    None: si Nico está en cuadro se pone solo."""
    p = [escena.strip()]
    if acento is None and any(x in CON_ACENTO for x in personas):
        acento = PRENDA[[x for x in personas if x in CON_ACENTO][0]]
    if personas:
        vidas = [VIDA[x] for x in personas if x in VIDA]
        if vidas:
            p.append('WHO THESE PEOPLE ARE. ' + ' '.join(vidas))
    if any(x in PATRULLEROS for x in personas):
        p.append(UNIFORME_POLICIA)
    p.append(REGISTRO[registro])
    con_cara = con_rostro and any(x not in SIN_ROSTRO for x in personas)
    p.append(C_ESTILO + (C_ROSTRO if con_cara else '')
             + (C_PIEL if personas else '') + C_FIGURA)
    if any(x in ('nico', 'nico_rapado') for x in personas):
        p.append(C_NICO)
    if any(x in SIN_ROSTRO for x in personas):
        p.append(C_SILUETA)
    p.append(C_ACENTO % acento if acento else C_SIN_ACENTO)
    if LUGARES.get(lugar):
        p.append(LUGARES[lugar] + ' ' + COLOMBIA)
    p.append(C_LIMPIA)
    p.append(C_NEG)
    return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())
