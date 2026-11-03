# Enfoque diferencial en la práctica del fiscal · PRIORIDAD 2

Carpeta del Drive: `1gp1dof3SncgICHNNiuEW3HHBYxdSCZDJ` («PRIORIDAD 2 -
ENFOQUE DIFERENCIAL EN LA PRÁCTICA DEL FISCAL»). Los cinco casos no son de
ninguna unidad: van en `VIDEOS` (`1qKmKVuwmNGKaTLbzgtm2pc5-uqf98k9u`). Las
entregas suben **solo con el OK de Sebastián**.

Árbol: `E:\DAE MASTER\PRIORIDAD 2\CURSO - ENFOQUE DIFERENCIAL\` (00 DOCUMENTOS
FUENTE, 00 PERSONAJES, VIDEOS\CASO 1..5 con las diez carpetas de la serie).
Bins iguales en `DAE MASTER - CURSOS`, vecino de Gerencia judicial y Derechos
humanos dentro de «PRIORIDAD 2». Rutas en `herramientas/voz/textos/rutas_ed.py`;
metadatos y textos en `guion_ed.py`.

PRIORIDAD 0X / X (Sebastián, 3 nov): si conviven «PRIORIDAD 2» y «PRIORIDAD
02» se funden en la de un dígito. Medido en disco y en el pool: no hay ningún
par duplicado (solo «PRIORIDAD 03», sin «3»), así que no se tocó nada.

## Lo que pidió Sebastián (3 nov)

- El guion empieza DESPUÉS del subtítulo «Fase de experiencia concreta» (ese
  subtítulo no va en el video). Verbatim.
- «De pe a pa», cinematográfico, como película: varios ángulos, los mismos
  personajes, consistencia, planos a media acción, varios planos
  complementarios de la misma escena.
- Reservar ~2.000 créditos de Magnific para cambios.

## Cinco videos

| | narra | ranuras | cuadros de narración | acento | rótulo |
|---|---|---|---|---|---|
| C1 Édgar Molano | Carlos | 23 | 4314 | cárdigan de Yolanda | Molano (r01) |
| C2 Jairo Montero Salas | Pilar | 31 | 5396 | la camisa del cumpleaños | Jairo (r01), Mauricio (r22) |
| C3 El patrullero Wilmer | Carlos (+ Andrés: la frase de Wilmer) | 25 | 4697 | sin acento | Wilmer (r01) |
| C4 La niña del resguardo de Putumayo | Pilar | 19 | 3772 | blusa de la madre | — |
| C5 La denuncia de Valentina | Pilar (+ Julián: el funcionario) | 20 | 3531 | abrigo de Valentina | Valentina (r02) |

Receta de la serie (`montaje/ed_pieza.py`): voz → rejilla → cruce → escenas →
placas → `elegir` → `construir` → detalles → Kling → cartones → rótulos →
blancos → música → `montar` → `revisar`. Geometría: intro 182 · entrada 119 ·
ranuras · respiro 48 · cierre 119 · outro 182.

## Puesta en escena (biblia P3)

Cada caso es una película corta: lugares con placa ancla (primera tanda, con
una placa aprobada de Ley 1826 como referencia de ESTILO) y el resto de los
planos pedidos con su ancla como referencia de LUGAR o del MISMO plano.
`prompts/escenas_ed_c1..c5.py` traen, por ranura, lo que se oye encima, quién
lleva cara y por qué, las rimas y los insertos.

Lo que no se dibuja nunca: el crimen de Jairo (ni cuerpo ni arma: el estante
con el hueco y la silla con la camisa), los golpes a Wilmer (la mano en el
antebrazo, los celulares en alto), la niña de Putumayo (su camino, su morral),
el abuso (la puerta cerrada). Agresores y quien amenaza: silueta o de
espaldas. Ninguna decisión equivocada cae sobre una cara: el coronel, el fiscal
de turno, el fiscal de la hipótesis «pasional» y el funcionario de la
recepción van de espaldas o en manos.

Rimas: la carpeta delgada (C1 r06) y la gruesa (r23); la sala de psicología
vacía (C1 r07) y ocupada (r21); las dos mecedoras (C2 r22) y la mecedora vacía
(r31); el formato con una casilla (C3 r15) y con tres (r23); el Taita en su
porche al principio y al final (C4 r02, r19); la única casilla (C5 r13) y la
mano que escribe en ella (r15).

## Placas y créditos

Seedream 5 Flash 2k 16:9 (35 créditos). 118 ranuras: 115 placas + 3 que
reusan otra con cámara distinta (C1 r18←r10, C2 r12←r09, C5 r08←r07), y 9
insertos de detalle. Cinco tandas; 19 placas rehechas por defectos medidos en
la hoja de contacto (una persona dos veces, texto legible —«NO» en las
chaquetas salió de escribir «NO badge» en mayúsculas—, caras de agresores,
insignias, la camisa ignorada con parche). Elegidas en
`prompts/elegidas_ed.json`; identificadores en `prompts/placa_id_ed.json`.

Lección de esta tanda: **una prohibición en mayúsculas dentro de la ropa de un
personaje se dibuja como texto** («NO badge, NO patch» → parches que dicen
NO). La ropa se describe en positivo: «de tela completamente lisa, sin nada
cosido, prendido ni impreso».

## Cartones

`cartones/cartones_ed.py`, verbatim, densidad 49–62 %. Los insultos (C2, C3)
los dice la voz y no se escriben; el hecho de violencia sexual del C4 tampoco.

## Estado

Ver el documento del proyecto `claude/ED_Enfoque_Diferencial_03_noviembre.md`.
