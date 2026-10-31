# -*- coding: utf-8 -*-
r"""Clausulas, lugares y reparto del curso «Derechos humanos aplicados a la
funcion judicial» (PRIORIDAD 2) · cinco videos.

EL SISTEMA ES EL DE LA SERIE, SIN UNA COMA DE MAS
    Biblia P3 + Gerencia judicial + Justicia restaurativa: rostros dibujados
    y simplificados, piel gris calida, tres registros de luz, superficie
    lisa, el acento como PRENDA mate, la escena como unidad, cartones
    verbatim. Lo de estilo se importa de `base_df_v1` tal cual; la sala y la
    oficina vienen de `base_gj`. Lo propio de este curso es el MUNDO y el
    REPARTO.

UN SOLO EXPEDIENTE, UN SOLO PUEBLO
    Todo pasa en un municipio de la cordillera, en Colombia: la plaza, el
    mercado, la emisora comunitaria con su antena en la terraza, la
    seccional de la Fiscalia (la ventanilla de denuncias, la oficina
    abierta, la sala de entrevistas, el despacho de la fiscal Quintero), la
    sala de audiencias y, en el epilogo de la U4, el pabellon. Los lugares
    se disenan una vez y vuelven: lo que cambia es la luz y quien esta.
        U1  la plaza y el mercado al amanecer, la emisora por fuera, la
            ventanilla de recepcion; cierre en la emisora con la luz de
            «al aire» encendida.
        U2  el despacho de Quintero (Julian entrega el escrito); la sala de
            audiencias del camino A y del C; la emisora por dentro.
        U3  primera version en la oficina abierta (luz fria, gente que pasa);
            segunda version en la sala de entrevistas (puerta cerrada, una
            ventana, dos sillas en angulo, sin escritorio entre ellas).
        U4  la sala de audiencias; la emisora por fuera al empezar; el
            epilogo en el corredor y el pabellon, solo siluetas.
        U5  el despacho de Quintero al final de la tarde, el mismo de la U2.

LO QUE EL DOCUMENTO PIDE EN COLOR, TRADUCIDO
    La U3 pide que la segunda version pase «del gris al azul con acentos
    verdes». Eso es otro sistema visual. Se traduce a la luz de la serie:
    la primera version es luz cenital de tubo, plana y fria, con desorden y
    gente detras; la segunda es luz de una sola ventana, suave, con el
    cuarto ordenado y vacio. El cambio se ve sin cambiar de paleta.

EL ACENTO ES DE CARMEN ELISA, Y DE NADIE MAS
    Un cardigan tejido mostaza mate, abierto, que cuelga recto por los dos
    lados. Es la victima y la vocera: el unico color del curso es el de ella.
    Donde no esta (casi toda la U4, la U5 entera, donde solo se oye su voz
    por telefono) no hay acento: la ausencia tambien se ve.

QUIEN LLEVA CARA, Y POR QUE (biblia §3: el error nunca se imprime encima
de una cara)
    Con cara: Carmen Elisa, Andres, Sandra, Quintero, Julian, la abogada
    Salgado, el juez, la apoderada de la victima. Hacen su trabajo.
    El ENTREVISTADOR 1 (U3) lleva cara pero NUNCA en primer plano y nunca
    es el sujeto del plano mientras comete una de las cuatro fallas: esas
    se cuentan con sus manos (el boligrafo sobre la pantalla, el celular que
    se ilumina), con su espalda en el plano sobre el hombro y con la cara de
    Carmen Elisa que las recibe. En el general esta lejos, mirando el
    monitor y no a ella, que es justo lo que el guion cuenta.
    En la U2 los caminos A y B (las respuestas equivocadas del despacho) se
    cuentan con papeles y manos, nunca sobre la cara de Quintero.
    WILMER ACOSTA no lleva cara: se presume inocente, y el curso lo dice
    con todas las letras en el epilogo. Se ve de espaldas o de tres cuartos
    de espalda, sentado junto a su defensora, la cabeza un poco baja; nunca
    un primer plano. Igual que los procesados de Justicia restaurativa.
    El pabellon del epilogo: siluetas, sin rostros, sin hacinamiento
    espectacularizado (el guion lo pide asi).
    Lo que no se dibuja nunca: las amenazas, el panfleto legible, la moto
    siguiendola, la captura, el arma en una mano. El antes y el despues si.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_df_v1 as B                          # noqa: E402
from base_df_v1 import (PIEL, ROSTRO, PLANOS, REGISTRO, CAMARA, LIMPIA,  # noqa
                        SIN_ROLES, SILUETA, ESTILO, FIGURA, LUGAR, ACENTO, NEG)
from base_gj import SALA as _SALA_GJ           # noqa: E402

# 31 oct (Sebastian, en vivo): «la saturacion de la piel va subiendo». Siete
# de nueve hojas de personaje y las placas de la sala salieron durazno-rosadas
# (mediana 0,25, tono 15 grados). La regla de siempre -PIEL- se queda; esto la
# dice para TODOS los complexiones y nombra lo que Seedream mete solo.
PIEL_DH = ('Every person here, whatever their complexion, has skin drawn in '
           'the SAME grey scale: lighter or darker GREY with only a faint warm '
           'tint, barely more coloured than a grey shirt. No peach, no tan, no '
           'olive, no pink cheeks, no rosy nose or ears, no red lips, no blush '
           'and no orange or red in the shadows of the face and hands.')

# ------------------------------------------------------------------ lugar
PUEBLO = ('The setting is a small town in the Colombian Andes: a square plaza '
          'with a few old trees and plain benches, ordinary two-storey houses '
          'in plain rendered and painted masonry with simple wooden balconies '
          'and low-pitched clay tile roofs, plain wooden doors and shutters, '
          'a narrow concrete pavement, square concrete utility poles with '
          'bundles of cable, and green steep mountain slopes rising close '
          'behind the roofs under low cloud. Nothing picturesque, no postcard '
          'framing, no church tower, no cross, no shop sign, no lettering '
          'anywhere.')

MERCADO = ('The setting is the open-air municipal market of a small Andean '
           'Colombian town at first light: rows of simple wooden stalls under '
           'plain canvas awnings on metal poles, plastic crates of potatoes, '
           'plantains and oranges, sacks of grain, a few people setting up, '
           'the houses of the plaza behind and the mountains beyond. No shop '
           'sign, no price card, no brand on any crate or sack, no lettering '
           'anywhere.')

EMISORA = ('The setting is the community radio station of a small Andean '
           'Colombian town: a plain two-storey corner house in rendered and '
           'painted masonry with a flat concrete roof terrace, a tall thin '
           'open-lattice metal antenna mast rising from the terrace with '
           'thin guy wires, a plain wooden street door, and above the door a '
           'small plain rectangular lamp box of frosted glass that lights '
           'when the station is on the air. The lamp box is blank: no '
           'lettering, no logo, no symbol on it or anywhere on the house.')

CABINA = ('The setting is the small broadcast booth of a community radio '
          'station: a plain desk with a broadcast microphone on a jointed arm, '
          'a small mixing desk with plain unmarked sliders, a pair of '
          'headphones, a plain computer screen, plain smooth grey acoustic '
          'panels on the walls, a window onto the street, a small blank '
          'frosted lamp box above the door. No lettering, no logo, no poster, '
          'no sticker anywhere.')

RECEPCION = ('The setting is the complaints reception of a small-town '
             'Colombian prosecution office: a plain counter with a pane of '
             'plain glass and a low opening in it, an official seated behind '
             'it at a grey desk with an ordinary computer screen and keyboard, '
             'a plain metal chair on the public side, a row of plain plastic '
             'waiting chairs along a painted wall, fluorescent tube light. '
             'Nothing lavish, no logo, no seal, no flag, no poster, no '
             'lettering anywhere.')

OFICINA_ABIERTA = ('The setting is a crowded open-plan office of a Colombian '
                   'prosecution office: rows of plain grey desks pushed '
                   'together, ordinary computer screens, tall uneven stacks of '
                   'cardboard case folders, plain metal shelving, plain '
                   'office chairs, colleagues passing or working in the '
                   'background, flat cold fluorescent tube light from the '
                   'ceiling. No logo, no seal, no flag, no poster, no '
                   'lettering anywhere.')

SALA_ENTREVISTAS = ('The setting is a small quiet interview room with its door '
                    'closed: plain painted walls, ONE window with a plain '
                    'half-lowered blind, a small plain table against the wall '
                    'and TWO plain upholstered chairs set at an angle to each '
                    'other with NO desk between them, a plain box of tissues '
                    'and a glass of water on the table. Calm and uncluttered. '
                    'No logo, no seal, no poster, no lettering anywhere.')

DESPACHO = ('The setting is the office of a prosecutor in a small-town '
            'Colombian prosecution office: a plain grey desk with an ordinary '
            'computer screen and a desk telephone, metal shelving full of '
            'cardboard case folders, a small plain meeting table with four '
            'plain chairs, a wide window behind the desk looking out over clay '
            'tile roofs to green mountain slopes, and a plain round wall clock '
            'with hands and NO numerals. No logo, no seal, no flag, no '
            'portrait, no diploma on the wall, no lettering anywhere.')

SALA = (_SALA_GJ + ' The layout: the judge sits at the centre behind a plain '
        'desk on a low plain platform; the prosecution table on one side, the '
        'defence table on the other, a third small table for the victim\'s '
        'legal representative, and a few rows of plain public benches at the '
        'back. A plain microphone on a short stand on each table.')

OFICINA_DEFENSA = ('The setting is the small private office of a defence lawyer '
                   'in a Colombian town: a plain dark desk with a closed laptop '
                   'and a desk lamp, a wall of plain shelves with rows of thick '
                   'law books whose spines are blank, a window with a plain '
                   'half-closed blind, one plain visitor chair. Orderly and '
                   'quiet. No diploma, no portrait, no logo, no lettering '
                   'anywhere, no title on any spine.')

PABELLON = ('The setting is a Colombian prison: a long plain institutional '
            'corridor of painted masonry, a heavy barred gate, and beyond it a '
            'crowded communal cell block suggested in depth: thin mattresses '
            'on the floor along the walls, clothes hung on lines, a queue of '
            'people waiting at a single wall telephone, light from high small '
            'barred windows. No lettering, no number, no emblem, no uniform.')

LUGARES = {'pueblo': PUEBLO, 'mercado': MERCADO, 'emisora': EMISORA,
           'cabina': CABINA, 'recepcion': RECEPCION,
           'oficina_abierta': OFICINA_ABIERTA,
           'sala_entrevistas': SALA_ENTREVISTAS, 'despacho': DESPACHO,
           'sala': SALA, 'pabellon': PABELLON,
           'oficina_defensa': OFICINA_DEFENSA}

# ------------------------------------------------------------------ reparto
# biblia §6: el token lleva quien es, su ropa y SU OBJETO; el estado lo
# declara la escena, nunca el token.
CUERPO = {
 'carmen': ('CARMEN ELISA ROJAS, a mestiza Colombian woman of about '
            'thirty-eight, slim, black straight hair tied back in a low '
            'ponytail, small plain stud earrings, in a plain mid-grey blouse, '
            'plain dark grey trousers and flat dark shoes, and a plain matte '
            'mustard-yellow knitted cardigan with long sleeves worn OPEN over '
            'the blouse, hanging straight down the front on both sides'),
 'andres': ('ANDRES PENA, a mestizo Colombian man of about thirty-two, '
            'medium build, short black hair, clean-shaven, thin dark '
            'rectangular glasses, in a plain light grey shirt with the sleeves '
            'rolled to the forearm and plain dark grey trousers'),
 'entrevistador': ('THE FIRST INTERVIEWER, a Colombian man of about '
                   'fifty-five, heavy-set, receding grey hair, a short grey '
                   'moustache, in a plain pale grey short-sleeved shirt with a '
                   'plain dark tie pulled loose at the collar'),
 'sandra': ('SANDRA IBANEZ, an Afro-Colombian woman of about thirty-six, '
            'medium build, short natural black hair cropped close, in a plain '
            'dark charcoal jacket over a plain light grey round-neck top and '
            'plain dark trousers'),
 'quintero': ('PROSECUTOR MARINA QUINTERO, a mestiza Colombian woman of about '
              'fifty-two, dark hair streaked with grey cut to the jaw, plain '
              'thin-framed reading glasses, in a plain charcoal grey blazer '
              'over a plain light grey blouse and plain dark grey trousers'),
 'julian': ('JULIAN MORA, a Colombian man of about twenty-seven, tall and '
            'lanky, short dark curly hair, clean-shaven, in a plain light '
            'grey shirt buttoned to the collar under a plain dark grey '
            'knitted sleeveless vest, plain dark trousers'),
 'salgado': ('DEFENCE LAWYER SALGADO, a Colombian woman of about forty-five, '
             'straight black hair pulled into a neat low bun, in a plain '
             'black trouser suit over a plain white-grey blouse'),
 'juez': ('THE JUDGE, a Colombian man of about sixty, white hair combed back, '
          'a short trimmed white beard, plain reading glasses, in a plain dark '
          'grey suit with a plain grey tie; no gown, no robe, no sash'),
 'apoderada': ('THE VICTIM\'S LEGAL REPRESENTATIVE, a mestiza Colombian woman '
               'of about forty, shoulder-length curly dark hair, in a plain '
               'dark grey suit jacket over a plain light grey blouse'),
 'acosta': ('WILMER ACOSTA, the accused, a Colombian man of about thirty, '
            'short black hair cut close, in a plain dark grey zip jacket over '
            'a plain grey T-shirt, seen ONLY FROM BEHIND or in three-quarter '
            'back view with his face turned away, his face never readable'),
 'presos': ('INMATES, seen ONLY AS SILHOUETTES and small figures in depth, '
            'never a face'),
 'vecinos': ('A FEW TOWNSPEOPLE going about their morning, small in the frame '
             'and far away, their faces not readable'),
 'colegas': ('COLLEAGUES in the background, small and out of focus, their '
             'faces not readable'),
}

VIDA = {
 'carmen': ('She has read the local news on the community radio for years and '
            'speaks for the municipal victims\' committee. She always carries '
            'a clear plastic document folder with the copy of her complaint '
            'inside.'),
 'andres': ('He takes in the complaints at the reception window and assigns '
            'them. He types fast and looks up at the person while he listens.'),
 'entrevistador': ('Thirty years behind the same kind of desk. His mobile '
                   'phone lies face up next to the keyboard.'),
 'sandra': ('A judicial police investigator. She prepares every interview by '
            'reading the file first, and keeps a plain dark notebook and a '
            'plain pen.'),
 'quintero': ('The prosecutor in charge of the case. She reads with her '
              'reading glasses low on her nose and keeps the whole case file '
              'within reach, a thick stack held with a black binder clip.'),
 'julian': ('Her assistant. He brings the papers in, reads them out standing, '
            'and keeps a pencil behind his ear.'),
 'salgado': ('A defence lawyer, serene and technical. Keeps a slim black '
             'folder closed in front of her until she needs it.'),
 'juez': ('A judge of guarantees. He listens with his hands joined on the '
          'desk and takes his glasses off to speak.'),
 'apoderada': ('She represents the victim at the hearing and takes notes in a '
               'plain grey notepad.'),
}

# Quien lleva acento.
CON_ACENTO = {'carmen'}

# Quien NO se dibuja nunca con rostro.
SIN_ROSTRO = {'acosta', 'presos', 'vecinos', 'colegas'}

TOKENS = CUERPO


def arma(escena, registro='dia', personas=(), con_acento=None,
         con_lugar=True, con_rostro=True, lugar='despacho', silueta=False,
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
                 + (PIEL + ' ' + PIEL_DH + ' ' if personas else '') + FIGURA)
    p.append(CAMARA)
    if con_acento:
        p.append(ACENTO)
    if con_lugar:
        p.append(LUGARES[lugar])
    p.append(LIMPIA)
    p.append(SIN_ROLES)
    p.append(NEG)
    return '\n\n'.join(x.strip() for x in p if x and x.strip())
