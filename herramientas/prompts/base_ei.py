# -*- coding: utf-8 -*-
r"""Cláusulas, lugares y reparto del curso «Estándares interamericanos ·
graves violaciones a los derechos humanos» (PRIORIDAD 3).

EL SISTEMA ES EL DE LA SERIE
    Las cláusulas cortas de `base_ed` (las de Ley 1826 y Enfoque diferencial,
    que salieron bien con Seedream 5 Flash), tal cual: rostros dibujados y
    simplificados, piel gris cálida, tres registros de luz, superficie lisa,
    un solo acento como PRENDA mate. Lo propio de este curso es el MUNDO -una
    vereda andina, un pueblo, el monte, una estación de policía, las oficinas
    de la Fiscalía- y el REPARTO.

LO QUE NO SE DIBUJA NUNCA (biblia §3)
    Ninguna desaparición, captura, ataque, agresión ni muerte en acto; ningún
    arma, herida, cuerpo, resto humano ni hueso: la fosa es una carpa, una
    cuadrícula de cuerda y una lona; la «agresión» del video es una mancha
    gris en una pantalla. Ningún hecho DEBATIDO se ilustra: ni el
    enfrentamiento del informe ni la subida al vehículo militar del testigo
    (S06), ni lo que muestra el video de redes (S08). La actuación procesal sí.
    Quien amenaza, la estructura criminal y los agentes de quienes se
    sospecha (los patrulleros de S08) van en silueta, de espaldas o en
    manos. La FUENTE de S07 no lleva cara (está protegida). Ningún texto,
    insignia, escudo, bandera ni placa. Los patrulleros, con el uniforme de
    la Policía Nacional (regla del 4 nov); los militares no se dibujan
    -solo sus camiones, lejos, y una manga verde oliva lisa-.

EL ACENTO (un solo color saturado por composición: la PRENDA de quien falta)
    S01  el líder · su ruana mostaza (después, doblada, en manos de su esposa)
    S04  la persona desaparecida · su bufanda tejida, en la bolsa de evidencia
    S06  uno de los jóvenes · su chaqueta, colgada junto a la puerta de la casa
    S07  una de las personas buscadas · el saco hallado, en la bolsa de evidencia
    S08  la persona que murió bajo custodia · su buzo con capota, devuelto en
         una bolsa transparente
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
from base_ed import (REGISTRO as _REGISTRO_ED, COLOMBIA, DESPACHO, PASILLO,  # noqa
                     FUNDACION, UNIFORME_POLICIA, UNIFORME_CORTO, C_ESTILO,
                     C_ROSTRO, C_PIEL, C_FIGURA, C_ACENTO, C_LIMPIA, C_NEG,
                     C_SILUETA)

# ------------------------------------------------------------------ lugares
# ---- S01 · el líder comunitario (una vereda andina del suroccidente)
VEREDA = ('The setting is a rural hamlet (vereda) in the Andean mountains of '
          'south-western Colombia: a red-earth road, a few one-storey houses '
          'of whitewashed adobe and plain rendered brick with corrugated zinc '
          'roofs, a small plain concrete community hall (caseta comunal) with '
          'a covered porch, plantains and coffee bushes on steep green slopes, '
          'high green mountains with drifting cloud behind. No church, no '
          'sign, no lettering anywhere.')
CASA_LIDER = ('The setting is the inside of a modest rural house in the '
              'Colombian Andes: whitewashed adobe walls, a plain packed-earth '
              'and cement floor, a heavy plain wooden table with plain wooden '
              'chairs, a small window with a wooden shutter, a plain wooden peg '
              'by the door. Ordinary, tidy, poor. No picture with a face, no '
              'calendar, no lettering anywhere.')
PUERTA_NOCHE = ('The setting is the front of a one-storey rural house of the '
                'Colombian Andes at night: whitewashed adobe wall, a plain '
                'wooden door half open, a bare bulb above it, the red-earth '
                'road outside falling into darkness, the dark shapes of the '
                'mountains against a dark grey sky. No sign, no lettering.')
OFICINA_PUEBLO = ('The setting is the plain public office of a small Colombian '
                  'mountain town (the municipal ombudsman\'s office): a plain '
                  'counter of painted wood, a plain desk behind it with an old '
                  'computer screen, metal shelving with cardboard folders, '
                  'plain painted walls, a window onto a sunny small-town '
                  'street. No logo, no seal, no flag, no poster, no lettering '
                  'anywhere.')
ONG = FUNDACION.replace('grassroots human rights foundation',
                        'human rights organization in a Colombian city')

# ---- S04 · el servidor y las fuentes
FACHADA_FISCALIA = ('The setting is the entrance of a large Colombian '
                    'prosecution office building in Bogota in the morning: a '
                    'plain modern facade of grey concrete and glass several '
                    'storeys high, a wide paved forecourt, a few plain trees, '
                    'people in plain office clothes walking in. No logo, no '
                    'seal, no flag, no sign, no lettering anywhere.')
DESPACHO_SERVIDOR = ('The setting is the small office of a legal analyst in a '
                     'Colombian prosecution office: a plain grey desk with an '
                     'ordinary computer screen and a plain desk lamp, tall '
                     'plain bookshelves full of thick law books with blank '
                     'plain spines, a few cardboard case folders, a window '
                     'with a plain blind onto the city. No logo, no seal, no '
                     'flag, no diploma, no lettering on any book or paper.')
BIBLIOTECA = ('The setting is a quiet legal library: long rows of tall plain '
              'shelves filled with thick bound volumes of court decisions, '
              'all with blank plain spines, a plain reading table with a plain '
              'lamp, a high window with a band of daylight. No label, no '
              'number, no lettering anywhere.')

# ---- S06 · los dos jóvenes
MONTANA = ('The setting is a rural zone of the Colombian mountains at dawn: '
           'steep green slopes with patches of forest and pasture, a winding '
           'unpaved road along the valley floor, a river, low mist in the '
           'folds of the hills, a few scattered farmhouses with zinc roofs. '
           'No sign, no lettering anywhere.')
CASA_PUEBLO = ('The setting is a modest family home in a small Colombian town: '
               'a plain front door of painted metal opening straight onto a '
               'narrow concrete street, plain rendered walls, a plain tiled '
               'floor, a small living room with a plain sofa, a row of plain '
               'pegs by the door. Ordinary, tidy. No picture with a face, no '
               'calendar, no lettering anywhere.')
TIENDA = ('The setting is a small roadside shop on a rural road in the '
          'Colombian mountains: an open front with a plain wooden counter, '
          'shelves of plain unbranded goods, a plain plastic table and chairs '
          'outside under a zinc awning, the empty unpaved road running past '
          'into the hills. No brand, no sign, no lettering anywhere.')
MEDICINA_LEGAL = ('The setting is an office of the national forensic medicine '
                  'institute in a Colombian city: a plain desk with an '
                  'ordinary computer screen, a wall-mounted plain light box '
                  'with plain grey films, metal filing cabinets, plain '
                  'painted walls, flat white light. No logo, no seal, no '
                  'chart, no lettering anywhere.')

# ---- S07 · la fosa
CASERIO = ('The setting is a small rural hamlet in the Colombian mountains: '
           'a few one-storey houses of plain brick and wooden planks with '
           'corrugated zinc roofs along an unpaved road, plantains, a fence of '
           'wooden posts, forested hills rising behind. No sign, no lettering '
           'anywhere.')
COCINA = ('The setting is the kitchen of a rural house in the Colombian '
          'mountains at night: a plain wood-fired stove of brick, blackened '
          'pots, plank walls, a plain wooden table with a plain oil lamp, a '
          'small dark window. No lettering anywhere.')
CLARO = ('The setting is a small clearing in the forest of the Colombian '
         'mountains where a forensic search is under way: a plain white '
         'canopy tent, the ground marked out with a grid of plain white string '
         'on small wooden stakes, a plain grey tarpaulin, plain plastic '
         'equipment cases, tall trees all around, flat grey daylight. No '
         'bones, no remains, no body anywhere: only earth, string and '
         'tarpaulin. No label, no number, no lettering anywhere.')
LAB_DIGITAL = ('The setting is a small digital analysis office of the '
               'Colombian prosecution service: a long plain desk with two '
               'ordinary computer screens, a plain keyboard, a plain mobile '
               'phone in a plain stand, a window blind half closed, the cool '
               'light of the screens. Every screen shows only plain grey '
               'rectangles and small grey thumbnail shapes, never letters, '
               'numbers, icons or a readable face. No logo, no lettering.')
EVIDENCIA = ('The setting is an evidence storage room: tall plain metal '
             'shelves with sealed plain cardboard boxes and clear plastic '
             'evidence bags with plain white tags that carry no writing, a '
             'plain steel table, flat white light. No label, no number, no '
             'lettering anywhere.')

# ---- S08 · bajo custodia
ESTACION_NOCHE = ('The setting is the outside of a neighbourhood police '
                  'station in a Colombian city at night: a plain two-storey '
                  'building of rendered concrete with barred plain windows, a '
                  'lit plain doorway, a plain white pickup truck parked in '
                  'front with no markings and no lettering, a white street '
                  'lamp, the pavement wet. No shield, no flag, no sign, no '
                  'lettering anywhere.')
ESTACION_DENTRO = ('The setting is the front desk of a neighbourhood police '
                   'station in a Colombian city: a plain counter, a thick '
                   'plain bound logbook lying open on it, a plain desk behind '
                   'with an old computer screen, plain painted walls, a plain '
                   'metal door to a corridor, flat fluorescent light. No '
                   'shield, no flag, no poster, no lettering anywhere.')

DESPACHO_NOCHE = DESPACHO + (' It is evening: the window is dark and the desk '
                             'lamp is the main light.')

LUGARES = {
 'despacho': DESPACHO, 'despacho_noche': DESPACHO_NOCHE, 'pasillo': PASILLO,
 'vereda': VEREDA, 'casa_lider': CASA_LIDER, 'puerta_noche': PUERTA_NOCHE,
 'oficina_pueblo': OFICINA_PUEBLO, 'ong': ONG,
 'fachada_fiscalia': FACHADA_FISCALIA, 'despacho_servidor': DESPACHO_SERVIDOR,
 'biblioteca': BIBLIOTECA,
 'montana': MONTANA, 'casa_pueblo': CASA_PUEBLO, 'tienda': TIENDA,
 'medicina_legal': MEDICINA_LEGAL,
 'caserio': CASERIO, 'cocina': COCINA, 'claro': CLARO,
 'lab_digital': LAB_DIGITAL, 'evidencia': EVIDENCIA,
 'estacion_noche': ESTACION_NOCHE, 'estacion_dentro': ESTACION_DENTRO,
 'ninguno': '',
}

# ------------------------------------------------------------------ reparto
PATRULLEROS = {'patrulleros', 'patrullero'}

CUERPO = {
 # ---- S01
 'lider': ('THE COMMUNITY LEADER, a Colombian campesino man of about '
           'fifty-five from the Andean mountains, wiry and weathered, short '
           'grey-black hair, a thick grey moustache, deep lines around the '
           'eyes, in a plain grey work shirt and plain dark trousers, rubber '
           'boots, and a plain matte mustard-yellow wool ruana -a square '
           'woollen poncho- worn over his shoulders, hanging straight down the '
           'front and the back'),
 'esposa': ('HIS WIFE, a Colombian campesina woman of about fifty-five, short '
            'and sturdy, long dark hair with grey streaks in a low plait, a '
            'round calm face, in a plain grey long-sleeved blouse, a plain dark '
            'grey cardigan and a plain dark skirt'),
 'hija': ('THEIR DAUGHTER, a Colombian woman of about thirty, slim, straight '
          'black hair to the shoulders, a direct serious face with defined '
          'brows, in a plain light grey blouse and plain dark trousers'),
 'hijo': ('THEIR SON, a Colombian man of about twenty-six, broad-shouldered, '
          'short black hair, a short black beard, in a plain dark grey '
          'work jacket over a plain grey T-shirt'),
 'abogada': ('THE HUMAN RIGHTS LAWYER, a Colombian woman of about forty-five, '
             'short curly dark hair, plain dark-rimmed glasses, in a plain '
             'charcoal blazer over a plain light grey blouse'),
 'fiscal_s01': ('THE PROSECUTOR, a Colombian woman of about forty-five, dark '
                'hair in a neat low bun, in a plain navy-grey jacket over a '
                'plain white blouse'),
 'investigadores': ('TWO INVESTIGATORS of the prosecution service in plain '
                    'dark grey jackets and plain dark trousers, one man and '
                    'one woman, small in the frame, their faces not readable'),
 'vecinos': ('A DOZEN NEIGHBOURS of the hamlet, campesino men and women of '
             'different ages in plain everyday clothes in shades of grey, '
             'some with plain hats, seated on plain plastic chairs'),
 'amenaza': ('TWO MEN ON A MOTORCYCLE, seen ONLY AS SOLID DARK SILHOUETTES far '
             'away in the dark: no face, no features, no skin tone'),
 'funcionaria': ('AN OFFICIAL behind the counter, seen ONLY as hands and a '
                 'plain grey sleeve, or from behind: her face is never '
                 'visible'),
 # ---- S04
 'servidor': ('THE LEGAL ANALYST, a Colombian man of about thirty-five, slim, '
              'short black hair neatly parted, clean-shaven, plain thin-framed '
              'glasses, in a plain light blue-grey shirt with the sleeves '
              'rolled to the forearm and a plain dark grey tie, plain dark '
              'trousers'),
 'gente': ('A FEW PEOPLE in plain office clothes in shades of grey walking, '
           'small in the frame, their faces not readable'),
 # ---- S06
 'fiscal_s06': ('THE PROSECUTOR, a Colombian man of about forty-eight, heavy '
                'build, short dark hair receding at the temples, a short grey '
                'beard, plain reading glasses, in a plain white shirt with the '
                'sleeves rolled up and a plain dark grey tie loosened'),
 'madre_s06': ('THE MOTHER of one of the young men, a Colombian woman of about '
               'fifty from a small town, slight, dark hair pulled back tightly, '
               'a tired lined face, in a plain grey blouse and a plain dark '
               'cardigan'),
 'padre_s06': ('THE FATHER of the other young man, a Colombian campesino of '
               'about sixty, lean, grey stubble, in a plain grey shirt, a plain '
               'straw hat held in his hands'),
 'testigo': ('THE WITNESS, a Colombian campesino shopkeeper of about sixty-five, '
             'thin, white stubble, a plain straw hat, in a plain faded grey '
             'shirt'),
 'investigador': ('AN INVESTIGATOR of the prosecution service, a Colombian man '
                  'of about forty in a plain dark grey jacket, seen from '
                  'behind or over the shoulder, his face not readable, '
                  'holding a plain notebook'),
 'medica': ('THE FORENSIC DOCTOR, a Colombian woman of about fifty, short '
            'straight grey hair, plain rimless glasses, in a plain white lab '
            'coat over a plain grey sweater'),
 'manga_militar': ('A HAND in the plain dark olive-green sleeve of a field '
                   'uniform with nothing sewn, pinned or printed on it: no '
                   'face, no badge'),
 # ---- S07
 'fuente': ('THE SOURCE, a campesino man in a plain grey jacket and a plain '
            'cap, seen ONLY FROM BEHIND or as a dark shape against the lamp: '
            'his face is never visible'),
 'investigadora': ('A FIELD INVESTIGATOR of the prosecution service, a '
                   'Colombian woman of about thirty-five, dark hair in a '
                   'ponytail, in a plain dark grey jacket, holding a plain '
                   'notebook'),
 'forenses': ('A FORENSIC TEAM of four people in plain white protective '
              'coveralls with the hoods up, plain white face masks and plain '
              'blue-grey gloves, kneeling and working; their faces are hidden '
              'by the hoods and masks'),
 'antropologa': ('THE FORENSIC ANTHROPOLOGIST, a Colombian woman of about '
                 'forty in a plain white protective coverall with the hood '
                 'down and the mask lowered, short dark hair, plain blue-grey '
                 'gloves'),
 'analista': ('THE DIGITAL ANALYST, a Colombian man of about thirty, lean, '
              'curly black hair cut short, a thin beard, in a plain dark grey '
              'hooded jacket over a plain grey T-shirt'),
 'fiscal_s07': ('THE PROSECUTOR, a Colombian man of about fifty, tall, '
                'close-cropped grey hair, clean-shaven, in a plain charcoal '
                'suit, a plain white shirt and no tie'),
 # ---- S08
 'madre_s08': ('THE MOTHER of the man who died, a Colombian woman of about '
               'sixty from a working-class barrio, heavy-set, short dyed dark '
               'hair, in a plain dark grey cardigan over a plain grey blouse'),
 'hermana': ('HIS SISTER, a Colombian woman of about thirty-two, slim, long '
             'straight dark hair tied back, small plain earrings, in a plain '
             'grey hooded jacket over a plain dark top'),
 'fiscal_s08': ('THE PROSECUTOR, a Colombian man of about forty, medium build, '
                'short dark hair, a neat short beard, in a plain grey suit, a '
                'plain light grey shirt and a plain dark tie'),
 'patrulleros': ('TWO PATROLMEN in ' + UNIFORME_CORTO + ' seen ONLY FROM '
                 'BEHIND or as hands and sleeves: their faces are never '
                 'visible'),
 'patrullero': ('A PATROLMAN in ' + UNIFORME_CORTO + ' seen ONLY FROM BEHIND '
                'or as hands and sleeves: his face is never visible'),
 'investigadora_s08': ('AN INVESTIGATOR of the prosecution service, a '
                       'Colombian woman of about forty, short dark hair, in a '
                       'plain dark grey jacket'),
 'mano': ('AN ANONYMOUS HAND of an ordinary adult, with its wrist and the cuff '
          'of a plain grey sleeve; no face anywhere'),
}

VIDA = {
 'lider': ('The leader of his hamlet\'s community board for twenty years: he '
           'speaks with his open hand on his chest and listens with his head '
           'tilted; the mustard ruana is always on his shoulders.'),
 'esposa': ('His wife: she keeps every paper of the case in a plain clear '
            'plastic folder that grows thicker with the years.'),
 'hija': ('Their daughter: she asks the questions in the family.'),
 'hijo': ('Their son: he speaks little and firmly, his hands flat on the table.'),
 'abogada': ('A lawyer of a human rights organization: she listens first and '
             'takes notes in a plain notebook.'),
 'fiscal_s01': ('The prosecutor in charge of the investigation.'),
 'servidor': ('A careful legal analyst of the prosecution office: he reads with '
              'a pencil in his hand and marks pages with plain grey slips of '
              'paper.'),
 'fiscal_s06': ('A prosecutor of a regional office: he reads every page twice '
                'and takes his glasses off when something does not fit.'),
 'madre_s06': ('She keeps her son\'s job application -his CV in a plain clear '
               'plastic sleeve- in her bag.'),
 'testigo': ('He has kept the shop by the road for forty years and sees '
             'everyone who passes.'),
 'medica': ('A forensic doctor: precise, quiet, she compares documents side by '
            'side.'),
 'antropologa': ('She leads the excavation and handles every object with both '
                 'hands.'),
 'analista': ('A digital analyst: he works close to the screens, in the dark.'),
 'fiscal_s07': ('The prosecutor in charge: he decides what is collected and how.'),
 'hermana': ('His sister: she found the video and carries it on her phone.'),
 'madre_s08': ('His mother: she holds his returned clothes on her lap.'),
 'fiscal_s08': ('The prosecutor in charge of the case.'),
 'investigadora': ('A field investigator who interviews quietly.'),
 'investigadora_s08': ('An investigator who checks every record.'),
}

# La prenda de acento de cada quien (biblia §6: una PRENDA, mate).
PRENDA = {
 'lider': 'his wool ruana',
 'ruana': 'the folded wool ruana',
 'bufanda': 'the knitted scarf inside the clear evidence bag',
 'chaqueta': 'the jacket hanging on the peg',
 'saco': 'the knitted sweater inside the clear evidence bag',
 'buzo': 'the hooded sweatshirt inside the clear plastic bag',
}
CON_ACENTO = {'lider'}
SIN_ROSTRO = {'investigadores', 'amenaza', 'funcionaria', 'gente', 'investigador',
              'manga_militar', 'fuente', 'forenses', 'patrulleros', 'patrullero',
              'mano', 'vecinos'}

NOCHE_INTERIOR = {'despacho_noche', 'estacion_dentro', 'cocina', 'lab_digital'}
REGISTRO = dict(_REGISTRO_ED)
REGISTRO['dia_noche'] = REGISTRO['dia'].replace(
    'ordinary daylight', 'ordinary flat white light from the ceiling lamps, '
    'night outside the windows,')

TOKENS = CUERPO
CORTO = True


def arma(escena, registro='dia', personas=(), con_acento=None,
         con_lugar=True, con_rostro=True, lugar='despacho', silueta=False,
         exterior=None, prenda=None):
    """Arma el prompt final (la forma corta de `base_ed.arma`)."""
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
    if any(x in PATRULLEROS for x in personas):
        p.append(UNIFORME_POLICIA)
    p.append(REGISTRO['dia_noche'] if (registro == 'dia' and lugar in NOCHE_INTERIOR)
             else REGISTRO[registro])
    con_cara = con_rostro and any(x not in SIN_ROSTRO for x in personas)
    p.append(C_ESTILO + (C_ROSTRO if con_cara else '')
             + (C_PIEL if personas else '') + C_FIGURA)
    if silueta or any(x in SIN_ROSTRO for x in personas):
        p.append(C_SILUETA)
    if con_acento:
        cual = PRENDA.get(prenda, prenda) or (PRENDA[quien[0]] if quien else 'the garment')
        p.append(C_ACENTO % cual)
    if con_lugar and LUGARES.get(lugar):
        p.append(LUGARES[lugar] + ' ' + COLOMBIA)
    p.append(C_LIMPIA)
    p.append(C_NEG)
    return '\n\n'.join(' '.join(x.split()) for x in p if x and x.strip())
