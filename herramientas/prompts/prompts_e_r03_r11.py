# -*- coding: utf-8 -*-
r"""E r03 y r11, 28 oct (Sebastian):
  r03  «doesn't look like a bike»: la moto venia de frente, chica y al centro,
       justo bajo el texto del carton p01; no se leia. Ahora de perfil, grande,
       en la mitad derecha, fuera del bloque de texto.
  r11  el V3 animado del sello se queda; la placa de abajo pasa a un
       over-the-shoulder del fiscal de turno en su despacho, con los mismos
       dos testigos de r08 al otro lado del escritorio. El fiscal sigue SIN
       ROSTRO (decide mal): nuca, hombro, chaqueta gris oscura (como r12).
Escribe D:\DAE\_tmp\sit\prompts_e_28oct.json con los dos prompts armados.
"""
import json
import sys
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_sit as S

ESTILO_PRIMERO = ('STYLE FIRST: a flat graphic illustration in EXACTLY the drawing style of '
                  'the reference images: simplified clean shapes, flat tones with soft '
                  'gradients of light, near-monochrome greys, the same line and the same '
                  'finish. It is a drawing, never a photograph and never photorealistic.')

R03 = '''
Wide shot of the same rural road in front of the same old roadside inn as in
the reference images, the low sun directly behind the scene, the camera at
standing eye level and perfectly level. The inn with its plain covered
terrace stands on the LEFT side of the frame; the road runs across the frame.

On the RIGHT HALF of the frame a PLAIN MOTORCYCLE stands stopped on the road,
seen EXACTLY SIDE-ON, IN FULL PROFILE, so that it reads at first glance as a
motorcycle: two round spoked wheels clearly apart from each other, the fuel
tank, the seat, the handlebar, the round headlight and the exhaust pipe all
clear in outline against the bright sky and the bright road. It is big in the
frame, about a third of the frame wide, its wheels on the ground in the lower
part of the frame, the front wheel pointing toward the right edge.

TWO STANDING SILHOUETTES stand beside the motorcycle, one behind its rear
wheel and one by its handlebar, still, seen as solid dark shapes against the
bright sky. They are only shapes: no faces, no features, nothing in their
hands.

The left half of the frame and the middle of the frame stay quiet: road,
terrace, sky. No other figure is in the frame.

Everything nearer the camera reads as silhouette and edge.
'''

R11 = '''
Over-the-shoulder medium shot inside a small plain office, the camera just
behind and to the left of a man seated at his desk, at his eye level and
perfectly level.

In the LEFT FOREGROUND, filling the left third of the frame, the BACK OF THE
HEAD AND THE LEFT SHOULDER of a man of about fifty in a plain dark grey
jacket, with short dark hair, seen ONLY FROM BEHIND, slightly out of the
light. NO PART OF HIS FACE is visible: no profile, no cheek, no nose, no eye.

Across the plain desk from him, in the middle ground on the RIGHT, sit TWO
WITNESSES, the same two people as in the reference image of the roadside:
a man of about forty with thick wavy dark hair, clean-shaven, in a plain grey
short-sleeved shirt, and beside him a woman of about thirty-five with dark
hair pulled into a low ponytail, in a plain light grey short-sleeved blouse,
a plain cloth bag held on her lap. They lean slightly forward toward the
desk, URGENT AND WORRIED, telling what they saw: his open hand rests on the
edge of the desk, the fingers held together and the thumb clearly visible;
her hands hold the bag.

On the desk between them lies a plain closed grey cardboard folder and a
plain rubber stamp. Nothing on the desk carries any letter or number.

Behind the witnesses, a plain wall and a plain window lets in ordinary
daylight from one dominant direction.
'''


def arma(esc, **k):
    return ESTILO_PRIMERO + '\n\n' + S.arma(esc, **k)


out = {
    'SIT_E_r03_la_moto': arma(R03, registro='contraluz', personas=(), con_acento=False,
                              exterior=True, silueta=True),
    'SIT_E_r11_el_sello': arma(R11, registro='dia', personas=('testigos', 'fiscalturno'),
                               con_acento=False, exterior=False),
}
json.dump(out, open(r'D:\DAE\_tmp\sit\prompts_e_28oct.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
for k, v in out.items():
    print('=====', k, len(v))
    print(v)
