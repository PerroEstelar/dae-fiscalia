# -*- coding: utf-8 -*-
r"""Cláusulas, lugares y reparto de las piezas de Sebastián del curso «Delitos
contra el medio ambiente» (PRIORIDAD 3).

EL SISTEMA ES EL DE LA SERIE
    Las cláusulas cortas de `base_ed` (Ley 1826, Enfoque diferencial,
    Estándares interamericanos), tal cual: rostros dibujados y simplificados,
    piel gris cálida, tres registros de luz, superficie lisa, cámara a nivel,
    placa limpia. Lo que cambia es el MUNDO -la selva, el río del Pacífico,
    la frontera amazónica, el pueblo minero- y por eso la PALETA.

LA PALETA DE ESTE CURSO (propuesta del 7 nov, a validar con V01)
    El entorno ya no es «casi todo gris»: en un curso sobre el bosque y los
    ríos, el verde y el agua son el tema. Se quedan con un rastro de su color
    -verde gris apagado, nunca exuberante; agua limpia gris verdosa, agua
    removida ocre turbio- y el cielo gris neutro.
    EL ACENTO (el único saturado): el AMARILLO MOSTAZA mate de la maquinaria
    y del oro. El amarillo sigue al dinero: la retroexcavadora, el motor de la
    draga, los granos de oro en la balanza, la máquina nueva que llega en la
    cama baja. Donde no hay negocio, no hay amarillo.

LO QUE NO SE DIBUJA NUNCA (biblia §3)
    Ningún arma, ninguna amenaza ni violencia en acto, ningún herido ni
    cuerpo. Los grupos armados van de espaldas o en silueta, sin arma a la
    vista, sin insignia. Ningún texto, escudo, bandera ni placa. El fuego ya
    pasó: humo gris y tocones quemados, nunca llamas naranjas (romperían el
    acento). Ningún uniforme con letras; la Armada, si aparece, es un bote gris
    sin marcas y figuras pequeñas a lo lejos.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
from base_ed import (REGISTRO as _REGISTRO_ED, DESPACHO, C_ESTILO,  # noqa: E402
                     C_ROSTRO, C_PIEL, C_LIMPIA, C_SILUETA)

COLOMBIA = ('This is Colombia, and the landscape, the boats, the houses and '
            'the people must say so; never Africa, never South-East Asia, '
            'never Europe, never the United States.')

C_FIGURA = ('Figures 8 to 8.5 heads tall, Colombian features carried by '
            'structure and hair. Perfectly level camera with a level horizon, '
            'no dutch tilt, no fisheye, no lens flare, no bokeh discs.')

C_PALETA = ('PALETTE: restrained, close to monochrome. The forest, the grass '
            'and the land keep only a faint trace of their colour: a muted, '
            'desaturated grey-green and earth-grey, never lush, never vivid, '
            'never emerald. Clean river water is a dark grey-green; water '
            'stirred up by mining is a dull opaque ochre-grey. The sky is a '
            'plain neutral grey. No golden hour, no orange or pink sky, no '
            'blue moonlight.')

C_ACENTO = ('The ONLY saturated colour in the whole image is the muted MATTE '
            'mustard-yellow of %s (matte paint, no glow, no shine, it goes into '
            'shadow with the object, never bright chrome or neon yellow); '
            'everything else stays within the restrained palette.')

C_SIN_ACENTO = ('Nothing in the image is saturated: no bright colour anywhere, '
                'no orange, no red, no saturated yellow.')

C_FUEGO = ('Where something has burned, the fire is over: charred grey '
           'stumps and trunks and drifting pale grey smoke, never flames.')

# 7 nov, primera tirada: los aéreos salieron con miles de árboles dibujados
# uno por uno -casi foto-; el dosel se pide como masas.
C_AEREO = ('From the air the forest is drawn as BROAD SIMPLIFIED MASSES of tone: '
           'clusters of rounded crowns merged into soft flat shapes with a few '
           'clear edges, never thousands of individually detailed trees, never '
           'a photograph from a drone.')

C_NEG = ('Not a photograph, not a 3D render, not painterly, no ink outlines, '
         'no anime eyes, no airbrushed skin, no motion blur. Nothing violent is '
         'shown: no weapon of any kind, no blow, no wound, no blood, no body.')

# ------------------------------------------------------------------ lugares
SELVA_AIRE = ('The setting is the Colombian Amazon rainforest seen from high '
              'in the air: an unbroken canopy of rounded tree crowns of many '
              'sizes, a wide river winding through it in slow meanders with '
              'pale sandbanks on the inside of the bends, low white mist '
              'caught between the trees, a plain grey sky. No settlement, no '
              'road, no boat.')
RIO_PACIFICO = ('The setting is a wide river of the Colombian Pacific lowlands '
                '(Choco): the river is broad and slow between banks of dense '
                'low rainforest with tall trees and palms, a plain grey humid '
                'sky. ')
DRAGA = ('THE DREDGE: a floating mining raft anchored in mid-river, built as '
         'a flat deck of rough wooden planks on rows of plastic barrels; a '
         'plain grey plastic tarpaulin stretched as a roof on thin wooden '
         'poles over half of the deck; under the roof a big boxy engine and '
         'pump whose casing is painted MATTE MUSTARD-YELLOW; a thick black '
         'suction hose running from the pump down into the water; at the '
         'back an inclined wooden sluice box lined with dark carpet, where '
         'grey water and sand run back into the river; a few blue-grey plastic '
         'fuel drums, a coil of rope. No flag, no name, no lettering.')
RIBERA = ('The setting is a river village of the Colombian Pacific lowlands: '
          'a row of stilt houses of weathered grey wooden planks with '
          'corrugated zinc roofs standing over the water, narrow plank '
          'walkways, dugout canoes (potrillos) tied to the posts, banana '
          'plants and palms behind, a plain grey humid sky. No church, no sign, '
          'no lettering anywhere.')
MINA_PIT = ('The setting is an open-pit alluvial gold mine carved out of the '
            'lowland rainforest of north-western Colombia: a wasteland of bare '
            'grey-ochre sand mounds and wide stagnant ponds of opaque ochre '
            'water where the forest used to be, felled tree trunks pushed '
            'aside in heaps, and at the edge a tall wall of standing '
            'rainforest. No building, no sign, no lettering.')
RETRO = ('A hydraulic excavator of the ordinary tracked kind, its body, boom '
         'and bucket painted MATTE MUSTARD-YELLOW and streaked with dried mud, '
         'no brand, no number, no lettering anywhere on it')
FRONTERA = ('The setting is the agricultural frontier of the Colombian Amazon '
            '(Caqueta, Guaviare): the edge of the tall rainforest, where the '
            'forest has just been cut. ')
TALA = (FRONTERA + 'A freshly cut clearing: big felled trunks lying '
        'criss-crossed on the ground, cut branches heaped, stumps, the tall '
        'standing forest like a wall behind. No road, no sign, no lettering.')
QUEMA = (FRONTERA + 'A burned clearing: charred grey stumps and blackened fallen '
         'trunks over ashen ground, a few tall dead trees left standing, '
         'pale grey smoke drifting low, the standing forest behind.')
POTRERO = (FRONTERA + 'A new pasture opened in the forest: rough grass with '
           'grey stumps still standing in it, a few lone tall trees left, a '
           'new barbed-wire fence on fresh wooden posts, a herd of white-grey '
           'zebu (Brahman) cattle grazing, and the dark wall of the forest '
           'beyond. No building, no sign.')
VIA = ('The setting is the Colombian Amazon seen from the air: a straight, '
       'freshly opened red-earth track cutting through the rainforest like a '
       'scar, cleared strips opening on both sides of it, the canopy dark and '
       'unbroken beyond. Plain grey sky at the horizon.')
COCA = ('The setting is a small field of coca bushes planted in rows in a '
        'clearing of the Colombian Amazon forest: knee-high leafy shrubs, '
        'stumps between the rows, the forest wall around. No person.')
MADERA = ('The setting is a muddy river landing in the Colombian Amazon: '
          'stacks of freshly sawn wooden planks and squared beams piled on the '
          'bank, a long wooden riverboat loaded with timber tied to a post, '
          'the brown river and the forest behind. No sign, no lettering.')
EMBARCADERO = ('The setting is a bend of a wide river of the Colombian Pacific '
               'lowlands: a small floating wooden landing tied to the bank, a '
               'wooden plank hut on stilts behind it, dense forest all '
               'around, the wide grey-brown river. No flag, no sign, no '
               'lettering anywhere.')
PUEBLO_MINERO = ('The setting is the main street of a mining town of the '
                 'Colombian lowlands (like Caucasia or Quibdo): two-storey '
                 'buildings of plain rendered concrete and brick with metal '
                 'shutters, balconies, tangled black cables on concrete poles, '
                 'motorcycles parked on the pavement, a humid grey sky. No '
                 'sign, no brand, no lettering anywhere.')
COMPRAVENTA = ('The setting is a small gold-buying shop on a mining town '
               'street in Colombia: a narrow room with plain painted walls, a '
               'glass-topped counter, behind it a small electronic precision '
               'scale on a plain mat, a plain ceiling fan, a metal security '
               'grille at the door open to the street. The display of the '
               'scale shows only a plain grey bar, no digits. No sign, no '
               'poster, no lettering anywhere.')
OFICINA_EMPRESA = ('The setting is the office of a commercial company in a '
                   'tall building in a Colombian city: a wide plain glass desk, '
                   'a plain leather chair, a laptop with a plain grey screen, '
                   'a floor-to-ceiling window over the city and the green '
                   'Andean mountains behind it. No logo, no sign, no '
                   'lettering anywhere.')
FINCA = ('The setting is the gate of a cattle ranch carved out of the forest in '
         'the Colombian Amazon: a plain wooden gate (tranquera) in a barbed-wire '
         'fence, a red-earth track, wide pasture with a few white-grey zebu '
         'cattle and lone trees, the forest far behind. No sign, no lettering.')
CARRETERA = ('The setting is a red-earth road in the Colombian Amazon '
             'frontier, puddles in the ruts, the forest on both sides.')
LANCHA = ('A plain grey river patrol boat with no markings, numbers, flags or '
          'lettering anywhere')
DESPACHO_DA = DESPACHO

LUGARES = {
 'selva_aire': SELVA_AIRE, 'rio': RIO_PACIFICO, 'draga': RIO_PACIFICO + DRAGA,
 'ribera': RIBERA, 'mina': MINA_PIT, 'tala': TALA, 'quema': QUEMA,
 'potrero': POTRERO, 'via': VIA, 'coca': COCA, 'madera': MADERA,
 'embarcadero': EMBARCADERO, 'pueblo': PUEBLO_MINERO,
 'compraventa': COMPRAVENTA, 'oficina_empresa': OFICINA_EMPRESA,
 'finca': FINCA, 'carretera': CARRETERA, 'despacho': DESPACHO_DA,
 'ninguno': '',
}
EXTERIOR = {'selva_aire', 'rio', 'draga', 'ribera', 'mina', 'tala', 'quema',
            'potrero', 'via', 'coca', 'madera', 'embarcadero', 'pueblo',
            'finca', 'carretera'}

# ------------------------------------------------------------------ reparto
CUERPO = {
 'minero': ('THE DREDGE WORKER, a Colombian mestizo man of about thirty, '
            'wiry, short black hair, a few days of stubble, in a soaked plain '
            'grey T-shirt, plain dark shorts and tall white rubber boots, a '
            'plain grey cap'),
 'pescador': ('THE FISHERMAN, an Afro-Colombian man of about sixty from a '
              'river village of the Pacific, lean and strong, short grey hair, '
              'a short grey beard, in a faded plain grey shirt and rolled plain '
              'trousers, barefoot'),
 'lavandera': ('A WOMAN of the river village, an Afro-Colombian woman of about '
               'forty, her hair wrapped in a plain grey cloth, in a plain grey '
               'dress'),
 'operador': ('THE EXCAVATOR OPERATOR, a man in a plain grey shirt and cap, '
              'seen small through the glass of the cabin'),
 'motosierrista': ('A CHAINSAW OPERATOR, a Colombian campesino man of about '
                   'thirty-five from the Amazon frontier, broad-shouldered, '
                   'in a sweat-darkened plain grey long-sleeved shirt, plain '
                   'dark trousers tucked into rubber boots, plain grey ear '
                   'defenders around his neck, holding a chainsaw with a plain '
                   'dark grey housing'),
 'vaquero': ('A COWHAND on horseback, small in the frame, in a plain grey shirt '
             'and a plain straw hat'),
 'colono': ('A SETTLER, a campesino man of about fifty in a plain grey shirt '
            'and a plain straw hat, rubber boots'),
 'lanchero': ('A BOATMAN, a man of about forty in a plain grey shirt'),
 'armados': ('THREE MEN of an armed group, seen ONLY FROM BEHIND or as dark '
             'silhouettes: plain dark olive field jackets and trousers, '
             'rubber boots, one with a small handheld radio clipped to his '
             'chest; nothing sewn, pinned or printed on the clothes, and no '
             'weapon visible anywhere'),
 'cobrador': ('A MAN of the armed group, seen ONLY FROM BEHIND: plain dark '
              'olive field jacket, rubber boots, a small plain notebook and a '
              'pencil in his hands; nothing sewn or printed on his clothes, no '
              'weapon visible'),
 'comprador': ('THE GOLD BUYER, a Colombian man of about fifty-five, heavy, '
               'short grey hair, plain reading glasses, in a plain white '
               'short-sleeved shirt'),
 'empresario': ('A BUSINESSMAN in a plain dark grey suit and white shirt, seen '
                'ONLY FROM BEHIND or as hands and sleeves: his face is never '
                'visible'),
 'dueno': ('A MAN in a plain grey polo shirt and a plain cap, seen ONLY FROM '
           'BEHIND or as hands and forearms: his face is never visible'),
 'fiscal': ('THE PROSECUTOR, a Colombian woman of about forty-five, straight '
            'dark hair cut to the jaw, plain thin-framed glasses, in a plain '
            'dark grey blazer over a plain white blouse'),
 'investigador': ('A CRIMINAL INVESTIGATOR of the prosecution service, a '
                  'Colombian man of about thirty-eight, short black hair, a '
                  'short beard, in a plain dark grey field jacket with nothing '
                  'printed on it, plain dark trousers, rubber boots'),
 'tecnica': ('AN ENVIRONMENTAL TECHNICIAN, a Colombian woman of about thirty, '
             'dark hair in a ponytail, in a plain light grey long-sleeved '
             'field shirt, plain blue-grey rubber gloves'),
}

VIDA = {
 'minero': ('He came from the interior to work the dredge; he sleeps on the '
            'deck under the tarpaulin; the black suction hose is his.'),
 'pescador': ('He has fished this river all his life from his own dugout '
              'canoe with a hand-made cast net.'),
 'motosierrista': ('A day labourer paid by the felled tree; the chainsaw is '
                   'not his.'),
 'comprador': ('He weighs other people\'s gold all day behind his glass '
               'counter.'),
 'fiscal': ('A prosecutor of the environmental crimes unit: she reads maps '
            'and satellite images as carefully as case files, a pencil always '
            'in her hand.'),
 'investigador': ('An investigator who documents everything with a plain '
                  'camera and a plain notebook.'),
 'tecnica': ('She takes the water samples herself and labels every bottle by '
             'hand.'),
}

SIN_ROSTRO = {'operador', 'vaquero', 'armados', 'cobrador', 'empresario',
              'dueno', 'lanchero'}

REGISTRO = dict(_REGISTRO_ED)
# contraluz de EXTERIOR: el 'contraluz' de base_ed habla de puertas y pasillos,
# y en un rio o una mina eso no existe (r11, r21, r22, r29).
REGISTRO['contra_ext'] = ('LIGHT: plain overcast daylight coming from BEHIND the '
                          'subject: the brightest plane is the grey sky and the '
                          'far water or land beyond; the people and objects '
                          'nearest the camera are a darker grey and read by '
                          'their shapes and edges, still clearly drawn, never '
                          'black. No sun disc, no glare, no bloom, no lens '
                          'flare, no visible light rays.')
REGISTRO['aire'] = ('LIGHT: a plain overcast sky, soft even daylight, the haze '
                    'of the humid forest softening the distance; a genuinely '
                    'light value and a genuine dark in the frame, the brightest '
                    'value a light grey clearly darker than paper white.')

TOKENS = CUERPO
CORTO = True


def arma(escena, registro='dia', personas=(), acento=None, lugar='ninguno',
         con_rostro=True, fuego=False):
    """El prompt final. `acento`: lo que lleva el amarillo mostaza (la
    maquinaria, el oro) o None para un plano sin ningún saturado."""
    p = [escena.strip()]
    if personas:
        vidas = [VIDA[x] for x in personas if x in VIDA]
        if vidas:
            p.append('WHO THESE PEOPLE ARE. ' + ' '.join(vidas))
    p.append(REGISTRO[registro])
    con_cara = con_rostro and any(x not in SIN_ROSTRO for x in personas)
    p.append(C_ESTILO + (C_ROSTRO if con_cara else '')
             + (C_PIEL if personas else '') + C_FIGURA)
    p.append(C_PALETA)
    if registro == 'aire':
        p.append(C_AEREO)
    if any(x in SIN_ROSTRO for x in personas):
        p.append(C_SILUETA)
    p.append(C_ACENTO % acento if acento else C_SIN_ACENTO)
    if fuego:
        p.append(C_FUEGO)
    if LUGARES.get(lugar):
        p.append(LUGARES[lugar] + ' ' + COLOMBIA)
    p.append(C_LIMPIA)
    p.append(C_NEG)
    return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())
