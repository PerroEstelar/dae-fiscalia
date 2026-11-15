# M1 · Video 1 — prompts de hojas de personaje y keyshots (v1)

Para Magnific (Seedream/Flux, lo que use la cuenta). Estilo: el de la serie de la Fiscalía
(ilustración editorial plana, planos tonales amplios, sin contorno de tinta), **pero a color**,
con rojo y amarillo de la marca como acentos que dirigen la mirada (`emb/CLAUDE.md`).
Ancla de estilo: subir una placa aprobada de la Fiscalía como referencia `style` (Sebastián
elige cuál: la de Enfoque diferencial o Ley 1826 es la más cercana). Formato 16:9 a 2560×1440.

## Bloques comunes

```
STYLE: stylized editorial illustration, flat graphic treatment, no ink outline anywhere:
forms built from broad soft tonal planes, never rendered shading, texture or brush marks.
Large surfaces smooth; a smooth gradient of light is allowed. Natural, gently muted full
colour — real Bogotá colours: brick, concrete, overcast sky, green hills — never grey-only.
Faces simplified and graphic: clear eyes with iris and highlight, brow, simple nose and mouth,
flat tonal planes with hard edges, warm natural skin in the person's real tone, no caricature.
Figures 8 to 8.5 heads tall, Colombian features carried by structure and hair.
Perfectly level camera, no dutch tilt, no fisheye, no lens flare, no bokeh discs.

COLOUR RULE: the brand red (#DF1F15) and brand yellow (#FFC400) appear ONLY on the one element
named in the shot; everything else avoids saturated red and yellow — no red cars, no yellow
signs, no red awnings, no orange light.

SETTING — Bogotá: two and three storey houses in exposed clay brick and plain rendered concrete,
flat roofs, metal grilles on ground-floor windows, concrete poles with bundles of black cables,
raised concrete pavement of square slabs, small motorcycles, the green eastern hills (cerros
orientales) hazy behind the rooftops, soft overcast Andean daylight.

CLEAN PLATE: no legible text, letters or numbers anywhere, no logo, emblem, badge, flag, seal or
coat of arms — not on clothes, not on the train, not on construction fences; any sign is a
plain flat panel with no marks.

NEGATIVE: photograph, 3D render, painterly brush, ink outline, anime eyes, airbrushed skin,
text, letters, numbers, logo, watermark, golden hour, sunset, orange sky, neon, lens flare,
bokeh, England, European architecture, pitched tiled roofs, chimneys.
```

## Hojas de personaje (una imagen por personaje, fondo liso claro)

Cada hoja: «character sheet on a plain light warm-grey background: the same person shown five
times in a row — front, three-quarter, profile, full body front, and a close-up with a calm
neutral expression — identical clothes, hair and proportions in every view». + STYLE + CLEAN.

| id | personaje | descripción para el prompt |
|---|---|---|
| hp01 | la servidora de la EMB | Colombian woman about 35, medium-brown skin, dark hair tied back, plain **brand-red** waist jacket with no marks over a white shirt, dark trousers, flat shoes, holding a closed grey folder |
| hp02 | la comerciante | Colombian woman about 50, light-brown skin, short curly dark hair with some grey, plain **brand-yellow** apron with no marks over a dark-blue sweater |
| hp03 | la persona cuidadora | Colombian woman about 40, dark-brown skin, braids gathered at the nape, olive-green rain jacket, a cloth bag on the shoulder |
| hp04 | el adulto mayor | Colombian man about 75, fair weathered skin, white moustache, grey wool ruana over a brown jacket, flat cap, wooden walking cane |
| hp05 | la usuaria de silla de ruedas | Colombian woman about 30, Afro-Colombian, short natural hair, denim jacket, manual wheelchair with plain dark frame |
| hp06 | el ingeniero del equipo técnico | Colombian man about 45, medium skin, short beard, plain white hard hat with no marks, plain high-visibility vest in **lime green** (not yellow) with two plain grey reflective bands, rolled plan under the arm |
| hp07 | la residente | Colombian woman about 25, light skin, long straight dark hair, grey hoodie, small backpack |
| hp08 | el vecino crítico | Colombian man about 60, medium-brown skin, grey hair combed back, glasses, dark corduroy jacket, holding his own sheaf of papers |

## Keyshots del video 1

Se piden **con las hojas como referencia `character`** y el ancla como `style`.

**p01 · La convocatoria que no llegó** (B1, lección 1.1.1)
Eye-level medium-wide shot at the door of a small Bogotá community hall (salón comunal) in late
morning. Outside on the pavement, the elderly man (hp04) and an elderly woman stand side by side;
she holds a mobile phone with its screen dark, held low, both of them looking at the closed
glass door, not at the camera. Through the door, inside, rows of white plastic chairs, almost all
empty. The ONLY brand-yellow element is the soft warm light spilling from the open door onto the
two of them. Brick wall, metal grille on the window, overcast sky. Camera at chest height, slightly
to the side, so the empty chairs and the two people read in the same frame.

**p02 · Una misma barrera, distinta para cada quien** (B3)
Low eye-level shot (camera at wheelchair height) on a raised concrete pavement beside a
construction fence of plain grey panels. The woman in the wheelchair (hp05) stops in front of a
high kerb where the pedestrian detour drops to the street; behind her, the caregiver (hp03) walks
arm in arm with the elderly man (hp04) and his cane. Nobody looks at the camera. The ONLY
brand-yellow element is a band of light along the edge of the high kerb. Far behind, above the
rooftops, the grey concrete viaduct of the metro under construction, out of focus as painted
soft shapes.

**p03 · El cierre peatonal** (B4 y B6)
Eye-level wide shot of a commercial street with a temporary pedestrian closure: plain grey
construction panels and plastic barriers. In front of a small corner shop with a roll-down
shutter half open: the shopkeeper (hp02, yellow apron — the only yellow) and a second shopkeeper
talk with the engineer (hp06); the engineer points at the barrier with an open hand. A little to
the left the young resident (hp07) points down a side street. On the right, the critical
neighbour (hp08) stands with arms crossed, his papers pressed to his chest. The red EMB servant
does NOT appear in this shot. Everyone is mid-conversation, mouths half open, nobody shouting,
nobody looks at the camera. Composition leaves three clear groups for on-screen labels.

## Planos de ambiente (reusables en todo el curso)

**a01 · El viaducto** — wide establishing shot of a broad Bogotá avenue with the elevated
concrete viaduct of the metro crossing the frame on tall columns; a six-car **brand-red**
passenger train on the viaduct (the only red), plain with no marks; below, buses, pedestrians,
brick buildings, the green eastern hills behind under a soft overcast sky. Referencias reales de
la Línea 1 como `image` (estructura, no copiar ninguna estación concreta).

**a02 · La estación** — three-quarter view of an elevated station with a curved roof over the
platform, seen from the street below; commuters going up the stairs; the train's red nose just
entering; no signage, no text.

## Movimiento (Kling, después)

Siguiendo la casa: todo movimiento llega a destino, nada «a punto de». p01: la luz de la puerta
respira, la mujer baja el teléfono y lo guarda en el bolsillo. p02: la silla avanza un palmo y se
detiene en el borde. p03: conversación en sitio, el ingeniero abre la mano y la baja. a01: el tren
cruza el cuadro completo y sale.
