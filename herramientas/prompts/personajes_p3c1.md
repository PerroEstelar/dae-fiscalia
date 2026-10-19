# PRIORIDAD 03 · Caso 1 — personajes, bloque de estilo y gramática de color

Lo que va en cada prompt, literal. El sistema es el **soft-volume editorial
vector** de la biblia SRPA, no el pictórico del curso de Bienes: esta serie
tiene personajes, y la hoja de dirección de arte del 12 oct 2026 demuestra que
las formas planas aguantan el movimiento generado y el volumen pintado no.

## El rostro vuelve — decisión de Sebastián, 19 oct 2026

La biblia SRPA trae «sin ninguna línea facial» como regla dura heredada de la
Guía Audiovisual, justificada en que las piezas tienen adolescentes. Sebastián
decidió recuperar el rostro para esta serie: son personajes de ficción
estilizados, y con rostro se puede hacer primer plano, que es lo que convierte
una ficha en una historia. Queda como decisión suya y fechada.

Lo que **no** cambia con el rostro:

- Ningún hecho se ilustra.
- Nada sugerente en ninguna figura, ninguna ropa ajustada o reveladora.
- Yeimi se trata exactamente igual que las otras ocho.

**Y una consecuencia técnica que sí cambia el método.** La hoja de dirección de
arte del 12 oct documenta que los rostros dibujados se rompen al animarse —«ojos
grandes y saltones», «un hombre sin cabeza»— porque el modelo repinta el iris en
cada cuadro. La regla que sale de ahí:

> **Los primeros planos van como placa sostenida con empuje de cámara, nunca
> como clip generado. Los dos o tres clips generados de cada pieza se reservan
> para planos sin cara cerca.**

Así se tiene el close-up sin el ojo saltón, y además cuesta cero.

**Medido en la prueba aprobada:** con el rostro dibujado, la piel cayó en
`#B5B0AC`, croma 9, saturación 0,048 — contra el gris piel de la biblia,
`#B7B3AC`, croma 11. Es decir que el sistema sostiene el rostro sin que el tono
de piel haga el trabajo, que es la regla 2 del manifiesto.

## El bloque de estilo, para pegar al principio de cada prompt

```
Stylized editorial character illustration, flat graphic treatment. No ink
outline anywhere: forms are built from broad soft tonal planes, never from
rendered shading, never from texture or brush marks. Faces ARE drawn and
expressive, but simplified and graphic: clearly defined eyes with brow, a
simple nose and a simple mouth, readable at a glance, with no photographic
detail, no skin pores, no individual hair strands, no caricature and no
exaggerated proportions. Skin stays in a desaturated warm grey range for every
figure — barely tinted, never a saturated skin tone. Colombian features, varied
from one person to the next, carried by facial structure, hair and silhouette
rather than by skin colour. Figures are 8 to 8.5 heads tall. The environment is
entirely in greys. Flat even light, static camera, perfectly level, no tilt, no
vignette, no lens flare. Clean plate: no legible text, no lettering, no
numbers, no signage, no logos.
```

Y el negativo:

```
Not a photograph, not a 3D render, not painterly. No ink outlines, no
multicolour gradients, no paper grain, no brush texture, no childish or
cartoon-mascot styling, no big round anime eyes, no exaggerated features.
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

Se corre sobre **toda placa que lleve acento**, antes del grade.\n\nEl sesgo del amarillo esta medido dos veces y es reproducible: **+8,5 y +9,2\ngrados hacia el naranja**, con la saturacion a la mitad. El del azul es solo de\nsaturacion: el tono sale clavado.

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


## Las hojas aprobadas

En `E:\\DAE MASTER\\PRIORIDAD 03\\00 PERSONAJES\\`. Cada una trae figura entera y
estudios de cabeza, y los acentos ya fijados:

| hoja | quiénes |
|---|---|
| `P3_hoja1_Cristina_Victor.png` | Cristina y Víctor, cuatro estudios de cabeza |
| `P3_hoja2_Camilo_Diana.png` | Camilo y Diana, cuatro estudios |
| `P3_hoja3_Daniela_Paula_Elena.png` | las tres, un estudio cada una |
| `P3_hoja4_Juliana_Yeimi.png` | las dos, cuatro estudios |

Las versiones sin rostro quedan archivadas con prefijo `_crudo_`.

**La consistencia entre planos es el riesgo abierto.** Dentro de una hoja los
rostros se sostienen; entre catorce placas distintas es donde se desarma. El
método de la casa es el token escrito repetido literal, pero con rostro eso ya no
basta: hay que pasar además la hoja como referencia de imagen en los planos de
primer plano, y medir si el rostro aguanta antes de generar el set completo.
