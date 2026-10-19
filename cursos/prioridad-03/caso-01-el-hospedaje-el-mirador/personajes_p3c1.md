# PRIORIDAD 03 · Caso 1 — personajes, bloque de estilo y gramática de color

Lo que va en cada prompt, literal. El sistema es el **soft-volume editorial
vector** de la biblia SRPA, no el pictórico del curso de Bienes: esta serie
tiene personajes, y la hoja de dirección de arte del 12 oct 2026 demuestra que
las formas planas aguantan el movimiento generado y el volumen pintado no.

## El bloque de estilo, para pegar al principio de cada prompt

```
Soft-volume editorial vector illustration. No outline anywhere: not on figures,
not on clothing, not on objects, not on the background. Faces carry no lines at
all — no eyelid, no eyebrow, no nose, no mouth, no eyes: the head is a clean
flat shape and the hair is a separate flat shape around it. Skin is one single
flat neutral grey, identical on every figure. Figures are 8 to 8.5 heads tall.
Volume is suggested only by broad soft tonal planes, never by rendered shading,
never by texture, never by brush marks. Each figure stands on a large
soft-edged elliptical shadow. The environment is entirely in greys — no colour
at all in walls, floor, furniture or props. Flat even light, static camera,
perfectly level, no tilt, no vignette, no lens flare. Clean plate: no legible
text, no lettering, no numbers, no signage, no logos, no emblems, no flags.
```

Y el negativo:

```
Not a photograph, not a 3D render, not painterly. No ink outlines, no facial
features of any kind, no skin tone other than flat grey, no multicolour
gradients, no paper grain, no brush texture, no cartoon or childish styling,
no caricature, no exaggerated proportions.
```

## La gramática de color de esta serie

La biblia SRPA asigna **rojo a la víctima, una sola por caso**. Aquí no se puede:
este caso tiene cuatro mujeres que podrían serlo y una que explícitamente no, y
**decidir eso es la pregunta que el video le hace al participante**. Pintar a
alguien de rojo contesta la votación antes de que vote. Es el mismo error que la
reja de la ventana en el C5U3.

La gramática adaptada marca **lo que el ejercicio da por establecido**, no lo que
el derecho concluye:

| color | quién | por qué |
|---|---|---|
| azul `#08539F`, prenda completa | Cristina, Víctor | el acuerdo lo da por establecido el propio enunciado |
| amarillo `#FCC50E`, un detalle | Camilo, Diana | intervinieron; qué significa su intervención es lo que se discute |
| sin acento, todo gris | Daniela, Paula, Elena, Juliana, Yeimi | el color no decide quién es víctima |

Tiene precedente en la propia biblia: la excepción documentada del Caso 3, donde
los cinco adultos van en gris a propósito. Aprobada por Sebastián el 19 oct 2026.

**El rojo y el neón quedan sin asignar en esta serie.** Si más adelante hace
falta un cuarto nivel, el neón `#E9DF00` está libre.

## Los acentos hay que FIJARLOS después de generar

El modelo acierta el tono institucional y falla la saturación, por la mitad y de
forma sistemática. Medido en las dos primeras hojas:

| | tono medido / objetivo | saturación medida / objetivo |
|---|---|---|
| azul | 211,1 / 210,2 | **0,49 / 0,95** |
| amarillo | 37,6 / 46,1 | **0,48 / 0,94** |

El azul era el azul correcto, lavado. El amarillo además se corría nueve grados
al naranja. **No se arregla regenerando** —es como pinta el modelo, y cuesta
créditos— sino con `herramientas/montaje/acentos.py`, que rota el tono y escala
la saturación solo sobre los píxeles que ya llevan color, sin tocar los grises y
sin tocar el valor, de modo que el modelado suave de la prenda sobrevive.
Resultado: azul a tono 210,3 y saturación 0,93; amarillo a tono 46,0.

Se corre sobre **toda placa que lleve acento**, antes del grade.

## Los nueve tokens

Van literales dentro del prompt de cada plano donde la persona aparezca. No se
describe el rostro nunca —no tiene— y no se menciona tono de piel: es gris plano
para todos, y la etnia solo se sugiere por estructura, peinado y silueta.

| token | descripción para el prompt |
|---|---|
| **Cristina** | a woman of about thirty-five, slim build, medium height, dark hair pulled back into a low ponytail, wearing a plain institutional blue jacket buttoned to the neck over plain grey trousers and plain grey shoes |
| **Víctor** | a man of about forty-five, heavy build, broad shoulders, tall, short dark hair, wearing a plain institutional blue shirt worn loose over dark grey trousers and grey shoes |
| **Camilo** | a man of about thirty-eight, medium build, medium height, short dark hair, wearing a plain grey jacket over a plain grey t-shirt, plain grey trousers and grey shoes, with a plain institutional yellow cap |
| **Diana** | a woman of about thirty, medium build, dark hair loose to the shoulder, wearing a plain light grey blouse and a plain mid-grey knee-length skirt with grey flat shoes, with a plain institutional yellow lanyard around her neck |
| **Daniela** | a woman of twenty-three, slim, medium height, dark hair gathered at the back, plain light grey short-sleeved blouse, plain grey jeans, grey trainers, no colour anywhere |
| **Paula** | a woman of twenty-nine, medium build, dark hair cut short to the jaw, plain mid-grey open jacket over a plain light grey t-shirt, dark grey trousers, grey ankle boots, no colour anywhere |
| **Elena** | a woman of thirty-five, slim, dark hair in a low bun, a plain mid-grey knee-length work tunic over plain grey trousers, flat grey shoes, no colour anywhere |
| **Juliana** | a woman of nineteen, slim, short, long dark hair worn loose, a plain light grey knitted cardigan over a plain grey top, grey jeans, grey trainers, no colour anywhere |
| **Yeimi** | a girl of seventeen, slim, short, dark hair in a high ponytail, a plain light grey t-shirt, plain grey jeans, grey trainers and a plain grey school backpack, dressed in ordinary everyday clothes exactly like the others, no colour anywhere |

### Lo que no se dibuja, en ningún plano

- **Ningún hecho se ilustra.** Es decisión de cliente heredada de la biblia: el
  pasaje duro va a plano de entorno vacío más el término en pantalla. Ninguna
  escena muestra un encuentro sexual, una agresión, una retención física ni una
  amenaza en acto.
- **Yeimi se trata exactamente como las otras ocho.** Ropa corriente, postura
  corriente, misma ficha. La Guía Audiovisual prohíbe imágenes de personas
  menores de edad y es el sistema sin rasgos faciales lo que hace viable que
  aparezca.
- Nada de ropa ajustada o reveladora, ninguna postura sugerente, en ninguna
  figura.

### Los cuatro estados sin rostro, aplicados

La biblia resuelve la expresión sin cara con cabeza, hombros y brazos. En las
hojas todos van en pose neutra, de pie y de frente, porque la hoja sirve para
comparar contexturas. En los planos:

| persona | estado | por qué |
|---|---|---|
| Cristina, Víctor, Diana, Paula | Resuelta | cada uno decide algo y lo decide sin conflicto |
| Daniela | Guardada | la deuda y la amenaza |
| Elena | Vacía | dieciséis horas, sin descanso, diecisiete meses |
| Camilo, Juliana, Yeimi | Distante | Camilo aparta la mirada, Juliana apenas llegó, Yeimi evade la pregunta de su edad |
