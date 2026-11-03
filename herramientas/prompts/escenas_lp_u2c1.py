# -*- coding: utf-8 -*-
r"""UNIDAD 2 · Estudio reverso de caso 1 «Escrito de acusación, flagrancia y
nulidad» · 11 ranuras · pieza 2809. Narra Carlos.

LO QUE SE OYE ENCIMA (cruce_lp.json)
    r01  El 15 de agosto de 2023, en el barrio Industrial de Cali, el
         supervisor de zona Jorge Eliécer Benavides sorprendió a Mario Alberto
         Gómez Parra,
    r02  contratista activo de la distribuidora, y a Pedro Antonio Morales
         Rincón, extransportador
    r03  realizando el transbordo clandestino de 45 botellas ... Kombucha
         Valle desde un vehículo particular,
    r04  placa KTH412, hacia el camión repartidor oficial, placa WXN445
    r05  al inspeccionar los envases ... etiquetas y tapas no correspondían
    r06  venía haciendo seguimiento ... caída atípica en las ventas
    r07  grabó un video de las botellas con su celular
    r08  la investigación sin captura, entrevistas al personal de seguridad,
         informes técnicos
    r09  e investigaciones internas de la empresa en 2023
    r10  el escrito de acusación se radicó bajo las reglas del abreviado,
    r11  Ley 1826 de 2017, el 4 de febrero de 2026

UN LUGAR Y UNA HORA: una calle de bodegas del barrio Industrial de Cali al
mediodía (r01 ANCLA). Los dos procesados se ven de espaldas: se presumen
inocentes y el texto no dice más que el hallazgo. El supervisor lleva cara
(lo nombra el texto). Ninguna etiqueta, tapa ni placa se lee: la etiqueta es
un rectángulo liso y la placa un rectángulo vacío. La fiscalía del final no
tiene nombre: solo manos y el escrito.
"""

R = {}

R[1] = (290, 'dia', ('supervisor',), None, False, 'bodegas', '''
Wide shot of a street of warehouses in the industrial district of Cali at
midday, the camera at standing height on the pavement, perfectly level. In
the foreground on the right, %(supervisor)s has just stopped at the corner of
a warehouse wall, half hidden by it, looking down the street, mid-step, one
hand on the wall. Far down the street, small in the frame, a plain private
hatchback car is parked with its boot open, nose to nose with the rear of a
plain white delivery truck with its roll-up door raised. Hard noon light,
short shadows.
''')

R[2] = (153, 'dia', ('contratista', 'transportador'), None, False, 'bodegas', '''
Medium shot from BEHIND of two men at the open boot of a plain private
hatchback car in a warehouse street, the camera at chest height, perfectly
level. Mid-action: %(transportador)s lifts a plastic crate of glass bottles
out of the boot with both hands; beside him %(contratista)s holds the raised
roll-up door of a plain white delivery truck parked just behind. Both are
seen from behind, their faces turned away and never visible. Hard noon light.
''')

R[3] = (201, 'dia', ('contratista', 'transportador'), None, False, 'bodegas', '''
Close shot at waist height of a plastic crate full of dark glass bottles held
between two pairs of hands, passing from the open boot of a car toward the
open back of a delivery truck. Every bottle carries a plain blank pale label,
a smooth rectangle with nothing on it, and a plain cap. Only hands and
forearms are in the frame: the left pair in a plain charcoal T-shirt sleeve,
the right pair in a plain dark grey polo sleeve. No face. The crate is held
level and firmly. Hard noon light.
''')

R[4] = (287, 'dia', ('supervisor',), None, False, 'bodegas', '''
Over-the-shoulder shot from behind %(supervisor)s, his shoulder and the back of
his head soft and out of focus in the left foreground, the camera at his eye
level, perfectly level. Down the street, in focus: a plain private hatchback
car parked with its boot open right behind a plain white delivery truck with
its roll-up door raised, a crate of bottles between them, and two men from
behind at work. Each vehicle has a plain BLANK number plate, an empty pale
rectangle with no characters. Hard noon light.
''')

R[5] = (234, 'dia', ('supervisor',), None, False, 'bodegas', '''
Medium-close shot of %(supervisor)s from the chest up, frontal, the camera at
his eye level, perfectly level. Mid-action: he holds TWO dark glass bottles
side by side at chest height, one in each hand, comparing their caps and
plain blank labels, his eyes narrowed on the caps, mouth closed. Behind him,
out of focus, the open back of the delivery truck. Hard noon light from one
side. He is ALONE in the frame and appears ONCE.
''')

R[6] = (282, 'contraluz', ('supervisor',), None, False, 'oficina_empresa', '''
Medium shot of %(supervisor)s seated at his office desk in the evening, in
three-quarter view, the camera at seated height, perfectly level. Mid-action:
he leans toward the computer screen, one hand on the mouse, studying a
simple line chart on the screen whose single line falls steadily from left
to right, no numbers, no labels; beside the keyboard, a stack of plain
delivery sheets. The window behind him is the only bright thing, the yard
outside already dim.
''')

R[7] = (101, 'dia', ('supervisor',), None, False, 'bodegas', '''
Close shot over the shoulder of %(supervisor)s of his mobile phone held flat in
both hands at chest height, recording: the phone screen shows a simplified
image of the crate of bottles, and beyond the phone, in soft focus, the same
crate of bottles on the ground at the back of the truck. Only his hands and
the edge of his shoulder are in the frame. Hard noon light.
''')

R[8] = (204, 'dia', ('vigilante', 'investigador'), None, False, 'sala_entrevistas', '''
Medium shot of a judicial police interview at a plain table, the camera at
seated height behind the investigator, perfectly level. Facing the camera,
%(vigilante)s speaks with one hand open on the table; in the near foreground,
%(investigador)s writes in a plain notebook. Window light from one side.
''')

R[9] = (104, 'dia', (), None, False, 'oficina_empresa', '''
Overhead shot looking straight down at a plain desk: a fan of plain internal
company reports with grey bars, a printed photo of two bottle caps side by
side, a plain binder clip, a pen. Nobody in the frame. Daylight from one side
throws soft shadows of the pages.
''')

R[10] = (124, 'dia', ('fiscal_sin_cara',), None, False, 'ventanilla', '''
Close shot at counter height of the filing counter of a prosecution office:
through the low opening in the glass, a hand in a plain charcoal jacket sleeve
slides a thick plain charge sheet, its cover marked only with grey bars,
toward the official on the other side, whose hand rests flat ready to receive
it. Only hands and sleeves; no face. Fluorescent light.
''')

R[11] = (179, 'dia', (), None, False, 'despacho', '''
Medium-wide shot of a prosecutor's office in the morning, nobody in the
frame, the camera at seated height, perfectly level. On the plain grey desk,
the thick charge sheet lies squared in the middle, a plain pen across it; on
the wall, the plain round clock with NO numerals. Soft morning light from the
window lays a clean bright band across the desk and the document.
''')

NOMBRE = {1: 'la_calle_de_bodegas', 2: 'de_espaldas', 3: 'el_transbordo',
          4: 'los_dos_vehiculos', 5: 'las_tapas', 6: 'la_caida_de_ventas',
          7: 'el_video', 8: 'la_entrevista', 9: 'los_informes',
          10: 'la_radicacion', 11: 'el_escrito'}

CON_PERSONA = {1, 2, 3, 4, 5, 6, 7, 8, 10}
SILUETAS = set()
CARTONES = {1, 2, 3, 4, 6, 8, 10, 11}
CENITALES = {9}
SOLO_MANOS = {3, 7, 10}
SIN_CARA = {2}
TOPE_SIN_GENTE = 3
PIEZA = 2809
TOTAL = PIEZA - (182 + 119 + 48 + 119 + 182)

HOJAS = {1: ['supervisor'], 4: ['supervisor'], 5: ['supervisor'],
         6: ['supervisor'], 7: ['supervisor']}

ANCLA = 'LP_U2C1_r01_la_calle_de_bodegas'
REF_PLACA = {1: (['DH_U1_r01_el_mercado'], 'estilo', '')}
for _n in (2, 3, 4, 5, 7):
    REF_PLACA[_n] = ([ANCLA], 'lugar', 'It is the SAME street at the SAME hour. ')
REF_PLACA[6] = ([ANCLA], 'estilo', '')
REF_PLACA[8] = ([ANCLA], 'estilo', '')
REF_PLACA[9] = ([ANCLA], 'estilo', '')
REF_PLACA[10] = ([ANCLA], 'estilo', '')
REF_PLACA[11] = ([ANCLA], 'estilo', '')

REUSA = {}

# 3 nov: el detalle entra en el 70 (era 120). El Kling de la r05 sube las dos
# botellas hasta los ojos entre ~1,7 y 3,0 s del crudo (cuadros ~79-139 de la
# ranura, con el retime x1,93): se ve como binoculos. El detalle lo tapa.
DET = {
 (5, 'las_tapas'): dict(cuadros=72, entra=70,
     registro='dia',
     personas=('supervisor',),
     escena='Extreme close shot of two dark glass bottle necks held side by '
            'side by a man\'s hands, the cuffs of a plain light grey work '
            'shirt: two plain caps of slightly different shape and finish, '
            'and the edges of two plain blank pale labels that do not line up. '
            'Hard noon light.',
     gesto='The hands turn the two bottles slowly a quarter turn, side by side, '
           'and hold them still. Nothing else moves.'),
}

BROLL = {}

MOV = {
 1: 'kling: el supervisor da un paso y se asoma desde la esquina',
 3: 'kling: la caja pasa de unas manos a otras y entra al camion',
 5: 'kling: gira las dos botellas y las compara',
}

LOWER_THIRD = {5: 'Jorge Eliécer Benavides'}


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
