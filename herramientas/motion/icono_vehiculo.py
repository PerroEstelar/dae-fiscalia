# -*- coding: utf-8 -*-
"""Ícono `vehiculo` para las listas de AE (Bienes en el proceso penal, 14 nov 2026).

Los juegos de íconos de SRPA y de Delitos ambientales no traían ningún vehículo, y
los de `00 ICONOS` del curso 5 tienen otro trazo (más fino). Este se dibuja en el
estilo de SRPA: línea blanca sobre transparente, trazo redondeado de ~22 px en un
lienzo de 512, supermuestreado ×4.

    python icono_vehiculo.py "E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/00 MOTION GRAPHICS/iconos/vehiculo.png"
"""
from PIL import Image, ImageDraw
import os
import sys
S = 4                      # supermuestreo
N = 512 * S
T = 22 * S                 # grosor del trazo
im = Image.new('RGBA', (N, N), (0, 0, 0, 0))
d = ImageDraw.Draw(im)
W = (255, 255, 255, 255)
def P(x, y): return (x * S, y * S)
def linea(pts):
    pts = [P(*p) for p in pts]
    d.line(pts, fill=W, width=T, joint='curve')
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0] - T / 2, p[1] - T / 2, p[0] + T / 2, p[1] + T / 2], fill=W)
# carrocería: base, frente, capó, parabrisas, techo, luneta, baúl, trasera
cuerpo = [(120, 352), (62, 352), (50, 336), (50, 290), (66, 262), (150, 246), (200, 176), (226, 162),
          (340, 162), (366, 176), (408, 246), (446, 256), (462, 280), (462, 336), (450, 352), (392, 352)]
linea(cuerpo)
linea([(184, 352), (328, 352)])
# ventanas
linea([(220, 236), (236, 196), (276, 196), (276, 236), (220, 236)])
linea([(306, 236), (306, 196), (338, 196), (362, 236), (306, 236)])
# ruedas
for cx in (152, 360):
    r = 46
    d.ellipse([P(cx - r, 352 - r), P(cx + r, 352 + r)], outline=W, width=T)
    d.ellipse([P(cx - 10, 342), P(cx + 10, 362)], fill=W)
# faro y manija
linea([(452, 290), (436, 290)])
linea([(64, 292), (78, 292)])
im = im.resize((512, 512), Image.LANCZOS)
dst = sys.argv[1] if len(sys.argv) > 1 else 'vehiculo.png'
if os.path.dirname(dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
im.save(dst)
print(dst)
