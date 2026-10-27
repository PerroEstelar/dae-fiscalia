# -*- coding: utf-8 -*-
r"""LOS PLANOS DE DETALLE del caso Miriam y Mariana.

LA LEY, QUE ES DE SEBASTIAN (27 de octubre)
    "i really like detail shots, it makes everything feel so much more alive
    (...) always think of it in cinematic and photographic terms, ask
    yourself: is this cinematic enough? do I need to double check online
    references? can this shot be complemented by another of details? or
    maybe a different camera angle?"

    Y la razon tecnica, que es suya y es correcta: "these detail shots might
    be easier to ask for motion and fit it without breaking the illusion,
    because it won't involve big bodies doing certain specific things in
    harmony with other things during long seconds". Un ojo que ajusta la
    pupila o una mano que aprieta una carpeta son un solo gesto en un solo
    objeto: el modelo de video no tiene que coordinar nada.

QUE ES UN DETALLE AQUI
    Un inserto de 3 a 4 segundos DENTRO de la ranura madre, que no cambia ni
    un cuadro del largo de la pieza ni de los cortes de Sebastian: va en la
    pista V3 DETALLE, debajo de los cartones, encima de la placa. Se apaga y
    la pieza queda como estaba.

    Se genera CON LA PLACA MADRE GRADUADA COMO REFERENCIA de imagen, para que
    sea indistinguible de ella: mismo personaje, misma ropa, misma luz del
    mismo lado, misma paleta, mismo estilo. Lo que se le pide al video es un
    solo gesto pequeno y lo demas quieto.

DONDE ENTRA
    Nunca en los primeros 40-60 cuadros de la ranura -la placa madre tiene
    que establecerse primero- y nunca pisando el lower third de la ranura.
    Nunca cruza un corte.

  (capitulo, ranura, nombre): dict(
      cuadros   largo del inserto
      entra     cuadro de la ranura en el que entra
      registro  el de la placa madre
      personas  tokens de CUERPO que entran
      acento    si la prenda de acento esta en cuadro
      escena    el prompt de la placa, con %(token)s
      gesto     el unico movimiento que se le pide al video)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

REFERENCIA = (
    'THIS IMAGE IS A DETAIL INSERT CUT FROM THE SAME SCENE AS THE REFERENCE '
    'IMAGE: the same person, the same clothing, the same light arriving from '
    'the same side, the same grey palette and exactly the same flat graphic '
    'illustration style, so that it cuts together with the reference '
    'seamlessly. It is a much tighter framing of one part of that scene, not '
    'a new scene.')

DET = {
 (2, 1, 'manos_carpeta'): dict(cuadros=96, entra=140, registro='dia',
    personas=('rosaelena',), acento=True, escena="""
EXTREME CLOSE-UP: the two hands of %(rosaelena)s pressing the plain plastic
document folder flat against her chest, the hands and the folder filling the
frame. Only the hands, the folder and the grey blouse behind them are in the
picture, and a fold of the mustard-yellow shawl enters at one edge. The
fingers are held together over the edges of the folder, the thumbs clearly
visible, the knuckles slightly raised as if holding on. No face. Same
daylight from the same side as the reference; the plain rendered wall behind
is out of focus.
""", gesto=(
    'Her fingers tighten very slightly on the folder and ease again, once, '
    'slowly; the thumbs press a little into its edge. The folder does not '
    'bend, slide or change shape. Nothing else moves.')),

 (2, 2, 'ojos_mariana'): dict(cuadros=96, entra=150, registro='dia',
    personas=('mariana',), acento=False, escena="""
EXTREME CLOSE-UP of the eyes of %(mariana)s: the frame cut from just above
the eyebrows to just below the lower lids, the two eyes filling the width of
the frame, seen straight on at her eye level. The same face as the reference
in the same flat graphic style: eyes clearly defined with the brow, dark
irises, plain round pupils, no photographic detail, no individual lashes, no
glare. The expression is the one in the reference -RESOLVED, level, looking
forward- not wide, not narrowed, not wet. Same daylight from the same side:
one side of the face a lighter plane, the other in shadow. No other feature
of the face in frame.
""", gesto=(
    'Her pupils contract slightly, as if adjusting to the light, and her gaze '
    'shifts a little to one side and comes back to the camera, unhurried; '
    'she blinks once, slowly. The eyebrows do not rise, the head does not '
    'move, and the eyes do not water.')),

 (2, 5, 'mano_telefono'): dict(cuadros=96, entra=100, registro='contraluz',
    personas=('mariana',), acento=True, escena="""
EXTREME CLOSE-UP of the hand of %(mariana)s hanging at her side holding the
plain grey mobile phone, seen from behind and a little below, the hand and
the phone filling the frame, the mustard-yellow band at her cuff just above
the hand. The phone's screen faces outward and is completely black and
blank: no icon, no light, no reflection. Beyond the hand the bright open
doorway of the police substation fills the background out of focus, so the
hand and the phone read mostly as a dark shape with a clean edge of light
down one side, exactly as in the reference. No face and no other part of
her in frame.
""", gesto=(
    'Her thumb moves slowly once across the edge of the phone and settles, '
    'and the fingers close a little more around it. The screen stays '
    'completely black the whole time and the doorway light behind does not '
    'change. Nothing else moves.')),

 (2, 8, 'ojos_fiscal'): dict(cuadros=90, entra=50, registro='dia',
    personas=('fiscal',), acento=False, escena="""
EXTREME CLOSE-UP of the eyes of %(fiscal)s: the frame cut from just above the
eyebrows to just below the lower lids, the eyes turned slightly down toward
the folder below the frame, seen at her eye level. The same face as the
reference in the same flat graphic style: eyes clearly defined with the brow,
dark irises, plain round pupils, no photographic detail, no individual
lashes, no glare. The expression is plain ordinary attention. Same window
light from the same side as the reference. No other feature of the face in
frame.
""", gesto=(
    'Her eyes move slowly along a line of reading from one side to the other '
    'and drop to the next line; she blinks once. The eyebrows do not rise and '
    'the head does not move.')),

 (2, 10, 'mano_auricular'): dict(cuadros=96, entra=60, registro='dia',
    personas=(), acento=False, escena="""
EXTREME CLOSE-UP of a hand holding a plain grey telephone handset against an
ear, seen from the side: the hand, the handset, and only the ear and the
edge of the jaw are in frame -no eyes, no mouth-. The fingers are held
together around the handset, the thumb clearly visible, the hand at a
natural angle so it reads as a hand with thickness and knuckles. The skin is
a desaturated warm grey, hue around 25 degrees and saturation no higher than
0.20, never pink and never brown. The handset is a plain object with no
button, no light and no marking. Same plain office and the same daylight
from the window on the same side as the reference, the bare wall out of
focus behind.
""", gesto=(
    'The hand adjusts its grip on the handset very slightly, once, and the '
    'handset settles a little closer to the ear. Nothing else moves.')),

 (3, 3, 'manos_caja'): dict(cuadros=90, entra=50, registro='dia',
    personas=('asistente',), acento=False, escena='''
EXTREME CLOSE-UP of the two hands of %(asistente)s under the base of the
plain grey document box he is carrying, the box filling the upper half of the
frame and the hands the middle: the fingers held together under its base,
taking its weight, the thumbs up its sides clearly visible, the knuckles
slightly raised. No face and no other part of him in frame. The corridor
shelving is a soft out-of-focus plane behind. The box is plain: no label, no
lettering, no number anywhere. Same daylight from the same side as the
reference.
''', gesto=(
    'His fingers shift once under the base of the box, re-taking the weight, '
    'and settle. The box stays level and closed, nothing slides out of it, '
    'and nothing else moves.')),

 (3, 5, 'ojos_fiscal_umbral'): dict(cuadros=96, entra=150, registro='contraluz',
    personas=('fiscal',), acento=False, escena='''
EXTREME CLOSE-UP of the eyes of %(fiscal)s standing in the doorway: the frame
cut from just above the eyebrows to just below the lower lids, the two eyes
filling the width of the frame, seen straight on at her eye level. The same
face as the reference in the same flat graphic style: eyes clearly defined
with the brow, dark irises, plain round pupils, no photographic detail, no
individual lashes, no glare. The corridor light behind her puts ONE CLEAN
CONTINUOUS EDGE of light down one side of the face; the other side is in
shadow; nothing crosses the face. The expression is level and surveying:
RESOLVED, not wide, not narrowed, not wet. No other feature of the face in
frame.
''', gesto=(
    'Her gaze travels slowly across the room from one side to the other and '
    'holds; she blinks once, slowly. The eyebrows do not rise, the head does '
    'not move, and the edge of light on her face does not change.')),

 (3, 6, 'mano_carpeta'): dict(cuadros=96, entra=60, registro='dia',
    personas=('fiscal',), acento=False, escena='''
EXTREME CLOSE-UP of the hand of %(fiscal)s resting on her plain grey closed
folder, which lies on the meeting table SLIGHTLY ASKEW to the table edge, the
folder and the hand filling the frame and the table edge running along the
bottom. The hand rests flat on the folder, the fingers held together, the
thumb clearly visible, seen at a natural angle so it reads as a hand with
thickness and knuckles. A sliver of her dark grey jacket sleeve enters at one
edge. No face. The folder is plain: no label, no lettering, no number. Same
daylight from the same side as the reference, the table top otherwise bare.
''', gesto=(
    'Her hand slides the folder a few centimetres until it lies squared with '
    'the edge of the table, and settles flat on it. The folder stays closed, '
    'nothing comes out of it, and nothing else moves.')),

 (3, 8, 'dos_manos_documento'): dict(cuadros=90, entra=50, registro='dia',
    personas=('fiscal', 'analista'), acento=False, escena='''
EXTREME CLOSE-UP, slightly from above, of the single document lying flat on
the table with TWO RESTING HANDS near it, one entering from each side of the
frame: the hand of %(fiscal)s from one side and the hand of %(analista)s from
the other, each resting on the table beside the document, the fingers held
together and the thumbs clearly visible, each at its natural size and seen at
a natural angle so it reads as a hand with thickness and knuckles. Neither
hand is on the paper and neither is pointing. The document carries plain flat
grey bars with no readable character anywhere. NO FACE in the frame. Same
daylight from the same side as the reference.
''', gesto=(
    'The fingers of one hand rise a little and settle again on the table '
    'beside the document, once, slowly. The document does not move, the grey '
    'bars on it do not change, and nothing else moves.')),
}

# Kling 3.0 cobra por segundo entero; el inserto se conforma al largo exacto.
MODELO = 'kling-30'
RESOLUCION = '1080p'
FPS = 23.976


def segundos(cuadros):
    import math
    return max(3, min(15, int(math.ceil(cuadros / FPS))))


def prompt_placa(cap, ran, nom):
    from base_df_v1 import arma, TOKENS
    d = DET[(cap, ran, nom)]
    esc = d['escena'] % TOKENS if '%(' in d['escena'] else d['escena']
    p = arma(esc, registro=d['registro'], personas=d['personas'],
             con_acento=d['acento'], con_lugar=False, con_rostro=True,
             exterior=False, silueta=False)
    return p + '\n\n' + REFERENCIA


def prompt_video(cap, ran, nom):
    from movimiento_df import QUIETO
    return DET[(cap, ran, nom)]['gesto'] + '\n\n' + QUIETO


def archivo(cap, ran, nom):
    return 'DF_C%d_r%02d_%s_det' % (cap, ran, nom)


if __name__ == '__main__':
    for k in sorted(DET):
        print(archivo(*k), DET[k]['cuadros'], 'entra', DET[k]['entra'],
              segundos(DET[k]['cuadros']), 's',
              len(prompt_placa(*k)), len(prompt_video(*k)))
