# -*- coding: utf-8 -*-
r"""SITUACIÓN 04 · ¿Cómo utilizaría una fuente internacional en una
investigación penal? · 10 ranuras · 1021 cuadros. Narra Pilar.

LO QUE SE OYE ENCIMA
    r01-r02  la Fiscalía General de la Nación adelanta una investigación | por
             la presunta desaparición forzada de una persona
    r03-r05  durante la revisión jurídica del caso, un servidor identifica |
             que el ordenamiento colombiano cuenta con disposiciones
             constitucionales | y penales relacionadas con la conducta
    r06      también encuentra referencias a la Convención Americana
    r07-r08  a la Convención Interamericana sobre Desaparición Forzada | y a
             diferentes decisiones de la Corte Interamericana
    r09-r10  el servidor debe determinar qué fuentes internacionales pueden
             resultar relevantes | y cómo incorporarlas a su análisis jurídico

QUIÉN LLEVA CARA
    El servidor (hoja). La persona desaparecida no se dibuja: está su
    bufanda mostaza en la bolsa de evidencia, el acento, que vuelve en r02,
    r03, r07 y r10. Los libros y documentos no llevan una letra: el modelo
    los dibuja con lomos y tapas lisas.
"""

R = {}

R[1] = (78, 'dia', ('gente',), None, False, 'fachada_fiscalia', '''
Wide shot of the forecourt of the large prosecution office building in Bogota
in the morning, the camera at standing height, perfectly level. %(gente)s
cross the wide paved forecourt toward the glass entrance. The plain concrete
and glass facade rises several storeys; behind it, the green Andean hills of
the city under a pale sky.
''')

R[2] = (93, 'dia', (), 'bufanda', False, 'despacho_servidor', '''
Close shot at desk height, perfectly level, of a plain manila case folder
lying closed on a plain grey desk; on top of it lies a clear plastic evidence
bag, sealed, with a folded matte mustard knitted scarf inside it and a small
plain white tag with no writing. Soft morning light from a window blind
across the desk. Nobody in the frame, no hand.
''')

R[3] = (106, 'dia', ('servidor',), 'bufanda', False, 'despacho_servidor', '''
Medium shot of %(servidor)s in his small office in the morning, the camera at
standing height, perfectly level. He sits down at his desk and opens the
plain manila case folder with both hands, his eyes already on its first page;
beside the folder lies the sealed clear evidence bag with the folded mustard
knitted scarf inside. Tall shelves of thick law books with blank spines
behind him; light through the plain blind. He appears ONCE.
''')

R[4] = (98, 'dia', ('servidor',), None, False, 'despacho_servidor', '''
Close shot at desk height, perfectly level: his two hands on the desk, one
holding open a thick plain book with a dark blank cover, its pages only plain
grey bars; the other hand lays a small plain grey paper slip between two
pages as a marker, a pencil between his fingers. The cuffs of a plain light
blue-grey shirt rolled to the forearm. Exactly two hands. No face.
''')

R[5] = (85, 'dia', ('servidor',), None, False, 'despacho_servidor', '''
Medium-close shot of %(servidor)s at his desk, frontal three-quarter, the
camera at his seated eye level, perfectly level. Two thick plain books lie
open side by side in front of him; his left index finger rests on a line of
one page while his eyes move to the other book, his pencil in his right hand.
Concentrated, calm. He appears ONCE.
''')

# 5 nov, revision de Sebastian (marcador 813: «the booklet looks off, doesn't
# make sense how it opens»): la placa tenia el libro de canto contra la camara
# con las hojas saliendo por arriba. Placa nueva (candidata f, con la vieja
# como referencia de personaje y lugar): por encima del hombro, el libro
# abierto de frente en las dos manos. No sobre el escritorio: la r05 ya es el
# libro abierto sobre la mesa y quedarian dos planos iguales seguidos.
R[6] = (123, 'dia', ('servidor',), None, False, 'despacho_servidor', '''
Over-the-shoulder shot from just behind the left shoulder of %(servidor)s,
the camera at his shoulder height, perfectly level. His shoulder and the side
of his head fill the left third of the frame, his face in profile, eyes down
on the page. He stands at the bookshelf holding a slim volume open in both
hands at chest height: the two open pages face him and the camera, the spine
runs vertically down the middle between his hands, his two thumbs rest on the
lower corners of the pages, his fingers out of sight behind the plain
blue-grey covers. The pages show only plain grey bars. Behind the book, soft
painted shapes of the shelf of books. Exactly two hands, exactly one book.
''')

R[7] = (103, 'dia', ('servidor',), 'bufanda', False, 'despacho_servidor', '''
Overhead shot looking STRAIGHT DOWN at his plain grey desk, the camera square
to the desk. Laid out in one neat row across the desk: the open manila case
folder with the sealed evidence bag and its folded mustard scarf on it; the
slim blue-grey volume; a stapled document of a few pages, only grey bars; and
a stack of three thick bound volumes with blank covers. From the bottom edge,
his two hands in light blue-grey shirt cuffs set down the third bound volume
on the stack. Nothing else.
''')

R[8] = (89, 'dia', ('servidor',), None, False, 'biblioteca', '''
Wide shot down a long aisle of the legal library, the camera at standing
height at the end of the aisle, perfectly level. Tall shelves on both sides
are filled with thick bound volumes of court decisions, all with blank plain
spines. In the middle ground, %(servidor)s walks along the aisle toward the
camera, caught mid-stride, carrying two thick bound volumes against his
chest. A band of daylight from a high window at the far end. He appears ONCE.
''')

R[9] = (135, 'contraluz', ('servidor',), None, False, 'despacho_servidor', '''
Close-up of %(servidor)s at his desk late in the afternoon, from the chest
up, three-quarter view, the camera at his eye level, perfectly level. He has
taken off his glasses and holds them in his right hand near his chin,
thinking, his eyes on the documents on the desk below the frame. The bright
window behind him; his face in soft shadow. He appears ONCE.
''')

R[10] = (111, 'hero', ('servidor',), 'bufanda', False, 'despacho_servidor', '''
Medium-wide shot of the small office in the evening, the camera at seated
height from the side, perfectly level. %(servidor)s writes at his computer
under the plain desk lamp, in profile, glasses on; at his elbow the sources
stand in one neat stack -the slim blue-grey volume, the stapled document, the
bound volumes- with the case folder and the sealed evidence bag with the
mustard scarf on top. The window behind is dark with the faint lights of the
city. The desk lamp is the main light. He appears ONCE.
''')

NOMBRE = {1: 'la_fiscalia', 2: 'la_bufanda', 3: 'el_servidor',
          4: 'la_constitucion', 5: 'los_codigos', 6: 'la_convencion',
          7: 'las_fuentes', 8: 'la_jurisprudencia', 9: 'determinar',
          10: 'el_analisis'}

CON_PERSONA = set(R) - {2}
SILUETAS = set()
CARTONES = {1, 3, 6, 7, 8, 9}
CENITALES = {7}
SOLO_MANOS = {4, 7}
SIN_CARA = set()
TOPE_SIN_GENTE = 3
TOTAL = 1021
PIEZA = TOTAL + (182 + 119 + 48 + 119 + 182)

HOJAS = {3: ['servidor'], 5: ['servidor'], 6: ['servidor'], 8: ['servidor'],
         9: ['servidor'], 10: ['servidor']}

ANCLAS = {1, 3, 8}

REF_PLACA = {
 1: (['EI_ANCLA_pueblo'], 'estilo', ''),
 3: (['EI_ANCLA_oficina'], 'estilo', ''),
 8: (['EI_ANCLA_pasillo'], 'estilo', ''),
 2: (['EI_S04_r03_el_servidor'], 'lugar', 'It is the SAME desk, the SAME folder and the SAME evidence bag. '),
 4: (['EI_S04_r03_el_servidor'], 'lugar', ''),
 5: (['EI_S04_r03_el_servidor'], 'lugar', 'It is the SAME office and the SAME man. '),
 6: (['EI_S04_r03_el_servidor'], 'lugar', 'It is the SAME office and the SAME man. '),
 7: (['EI_S04_r03_el_servidor'], 'lugar', ''),
 9: (['EI_S04_r03_el_servidor'], 'lugar', 'It is the SAME office and the SAME man. '),
 10: (['EI_S04_r03_el_servidor'], 'lugar', 'It is the SAME office and the SAME man, now in the evening. '),
}

REUSA = {}
DET = {}
BROLL = {}

MOV = {
 1: 'kling: la gente cruza la plazoleta hacia la entrada',
 6: 'kling: saca el volumen del estante y lo mira',
 8: 'kling: camina por el pasillo de la biblioteca con los volúmenes',
 9: 'kling: piensa con las gafas en la mano; baja la mirada',
 10: 'kling: escribe en el computador bajo la lámpara',
}

LOWER_THIRD = {}


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
    if set(LOWER_THIRD) & CARTONES:
        fallos.append('rotulo y carton en la misma ranura')
    for (n, _), d in DET.items():
        if (d['entra'] < 60 and not d.get('abre')) or d['entra'] + d['cuadros'] > R[n][0]:
            fallos.append('detalle r%02d fuera de su ranura' % n)
    return fallos, tot, mejor
