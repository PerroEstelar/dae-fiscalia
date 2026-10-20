# PRIORIDAD 03 · Caso 2 — personajes, gramática de color y lo que no se dibuja

Mismo sistema de la serie: **soft-volume editorial vector** con rostro, el
bloque de estilo del Caso 1 sin cambios, y los acentos fijados después con
`acentos.py`. Lo que cambia es a quién le toca color, y por qué.

## La regla de la serie, aplicada a un caso donde casi nada está establecido

El Caso 1 preguntaba quién responde. Este pregunta **cómo se trata a quien
todavía no sabemos qué es**, y el documento lo dice en su primera línea: la
información es la del primer contacto, nada está judicialmente demostrado, y
que el inmueble sea un lugar de trata es una hipótesis.

La regla de color de la serie —**el acento marca lo que el enunciado da por
establecido, nunca lo que el derecho concluye**— aquí deja casi todo en gris,
que es exactamente lo correcto.

| color | quién | qué da por establecido el enunciado |
|---|---|---|
| azul `#08539F`, prenda completa | Saúl, Darío | Saúl administra el taller; Darío trabaja para él y recibe parte de los pagos |
| amarillo `#FCC50E`, un detalle | Patricia, la tía | intervinieron —los mensajes existen, la tía recibe parte de la remuneración—; qué significa su intervención es lo que se discute |
| sin acento | Mara, Samuel, Elisa, las dos personas que conservan documentos | sobre su condición es que se pregunta |

**El amarillo de Patricia es la única decisión discutible de esta hoja, y hay
que decirla en voz alta.** Marcarla puede leerse como ponerla del otro lado,
que es justo lo que la opción b) de la votación niega. Va igual, por la misma
razón que en el Caso 1: sus mensajes **están**, eso es lo establecido, y lo que
se vota es qué significan. Si a Sebastián le parece que inclina la votación, se
quita y va en gris; es un cambio de media hora.

## Los tokens, literales para el prompt

| token | descripción |
|---|---|
| **Saúl** | a man of about fifty, lean, medium height, short greying dark hair, wearing a plain institutional blue shirt with the sleeves rolled up over dark grey trousers and grey shoes |
| **Darío** | a man of about forty, stocky, short, short dark hair, wearing a plain institutional blue jacket over a plain grey t-shirt, grey trousers and grey shoes |
| **Mara** | a woman of twenty-six, tall, slim, long dark hair worn loose, wearing a plain light grey long-sleeved blouse, plain grey trousers and grey flat shoes, ordinary everyday clothing, nothing tight and nothing revealing, no colour anywhere |
| **Samuel** | a man of thirty-five, medium build, medium height, short dark hair and a close-trimmed beard, wearing a plain mid-grey work shirt over grey trousers and grey shoes, no colour anywhere |
| **Elisa** | a girl of seventeen, slim, short, dark hair in a single braid, a plain light grey t-shirt, plain grey jeans and grey trainers, dressed in ordinary everyday clothes exactly like the others, no colour anywhere |
| **Patricia** | a woman of thirty-two, medium build, medium height, dark hair tied back, a plain mid-grey blouse over plain grey trousers and grey shoes, with a plain institutional yellow scarf knotted at the neck (en la hoja lleva una liga amarilla; en el primer plano se cambió por el pañuelo, ver abajo) |
| **la tía** | a woman of about fifty, heavy build, short, dark hair cut short, a plain mid-grey cardigan over a plain light grey blouse and a grey skirt, with a plain institutional yellow handbag |
| **las dos** | two workers of about thirty in plain grey work clothes, no colour anywhere, always at a distance and never in close-up |

### Mara

Se dibuja **exactamente como cualquier otra mujer del sistema**. Nada en el
dibujo la marca: ni la silueta, ni la ropa, ni un rasgo puesto ahí para que se
note. El caso lo dice con palabras —«mujer trans venezolana de veintiséis
años»— y la imagen no lo subraya, porque subrayarlo sería hacer con el dibujo
justo lo que el funcionario del caso propone hacer con el nombre.

Y por eso mismo el token no lleva la palabra: un prompt que la incluya produce
caricatura. La identidad va en la locución y en el cartón, que es donde el
participante la necesita.

### Elisa, diecisiete años

Mismo trato que Yeimi en el Caso 1: ropa corriente, postura corriente, misma
ficha que los adultos, nunca sola en un plano que sugiera nada. El sistema sin
fotorrealismo es lo que hace viable que aparezca.

### La hija de Patricia no se dibuja

Tiene cuatro años. No hay forma de representarla que aporte algo al ejercicio
y sí varias de que reste. Va nombrada en locución y nada más.

## Lo que no se ilustra, en ningún plano

- **Ningún hecho.** Ni la amenaza de divulgar imágenes, ni el ofrecimiento a
  Elisa, ni una retención, ni una jornada de catorce horas en acto. El pasaje
  duro va a entorno vacío o a primer plano de expresión, más el término en
  pantalla.
- **Ningún candado, ninguna reja, ningún cerrojo.** El documento dice
  literalmente «no hay candados», y es un dato del caso: dibujar un encierro
  contestaría la pregunta. Es la misma corrección que costó el plano de las
  nueve del C5U3.
- Nada de ropa ajustada o reveladora, ninguna postura sugerente, en ninguna
  figura.

## Los cuatro estados, aplicados

| persona | estado | por qué |
|---|---|---|
| Saúl, la tía | Resuelta | cada uno decide y lo decide sin conflicto |
| Mara, Elisa, Patricia | Guardada | las tres piden algo y las tres se reservan algo |
| Samuel | **de frente** | mira al interlocutor y responde; la excepción de esta pieza |
| Darío | Distante | habla por otro y aparta la mirada del que traduce |

**La excepción de Samuel es el plano que sostiene su bloque.** La tentación es
dibujarlo apartado, y sería exactamente el error que el caso denuncia: el
problema no es que Samuel no se comunique, es que el equipo no lo escucha.
Entonces Samuel mira de frente, y el que aparta la mirada es Darío.


## Dos hallazgos de la producción de este caso

**La planitud se gana en el prompt de la PLACA, no en el de la hoja.** La hoja
de Mara y Samuel salió con los estudios de cabeza más modelados de la cuenta
—la barba con degradado, la mejilla suave— y la repetí pidiendo planos duros y
pasando la propia hoja como referencia. Salió **peor**: más suave todavía. La
referencia tira hacia lo que ya había. Volví a la primera y endurecí el prompt
de las catorce placas, que es donde sí funciona: las placas finales están
planas aunque la hoja no lo esté del todo. Costó cien créditos aprenderlo.

**Un acento pequeño junto a la cara se deforma.** La liga amarilla de Patricia,
en primer plano, salió como un disco pegado a la oreja —parecía un arete, no
una liga—. En plano entero funciona; en primer plano no hay sitio para un
detalle pequeño. Se cambió por un pañuelo anudado al cuello, que es una banda
limpia en la parte baja del cuadro y se lee como prenda. La regla que queda:
**para un primer plano, el acento va en una prenda del torso, nunca en el
pelo ni cerca de la oreja.**

## Saúl: estaba ausente a propósito, y ahora aparece en sombra

La primera versión de esta hoja decía que **Saúl no aparece en ningún plano**:
es el que todos nombran y nadie muestra, su responsabilidad es justamente lo
que el caso NO da por establecido, y dibujarlo lo convertiría en el culpable
de la pieza antes de que el participante decida nada.

**Sebastián lo revisó y pidió lo contrario**, con razón: el video lo nombra
una y otra vez y nunca enseña nada, y eso no se lee como una decisión, se lee
como un hueco. La regla cambia, pero no se cae:

> **Saúl aparece, y su cara nunca se aclara.**

En todos sus planos la cabeza va en sombra plana, sin facciones dentro del
contorno: de espaldas, de perfil, de tres cuartos por detrás, o sentado de
espaldas a la puerta. El perfil puede leerse como borde; dentro no hay nada
que mirar. Así el participante sabe quién administra el taller sin que el
dibujo le entregue un rostro al que culpar.

Los ángulos están en `P3C2_hoja5_Saul.png` —cinco estudios: de frente, de
perfil, de espaldas, sentado al escritorio y tres cuartos por detrás—, y su
primera aparición es `br15_saul_oficina`, visto a través de la puerta de su
oficina desde el taller.

**El azul sigue siendo correcto sobre él.** El acento marca lo establecido, y
que Saúl administra el taller es lo que el enunciado da por establecido; Darío
lo lleva por lo mismo. Mostrarlo no le añade ninguna afirmación que la hoja
no hiciera ya con el color.

### Lo que esto deja dicho para los casos que vienen

Un personaje que la locución nombra mucho **necesita cuerpo en pantalla**,
aunque el caso no quiera atribuirle nada. La forma de no atribuir no es
esconderlo —esconderlo se nota— sino **mostrarlo sin rostro**.
