# Caso 02 · movimiento

## Qué se pidió

Cuatro loops a Magnific, Kling 2.5, 720p, 10 s, desde el cuadro inicial de cada
plano ya elegido. 280 créditos cada uno, 1 120 en total — y 280 más por un error
mío que se explica abajo.

| plano | loop | qué hace |
|---|---|---|
| KF03 | `TA02_KF03_bodega_loop10s.mp4` | la mujer acomoda una caja en la bodega, los demás trabajan al fondo |
| KF04 | `TA02_KF04_abogado_propone_loop10s.mp4` | el abogado habla, sostiene la palma abierta, nunca sonríe |
| KF05 | `TA02_KF05_andres_escucha_loop10s.mp4` | Andrés escucha con las manos entrelazadas |
| BR03 | `TA02_BR03_cajas_loop10s.mp4` | travelling lento entre estibas, una figura se aleja |

## El error del KF05

Pedí el primer KF05 con el identificador `rgAtLGTxtc`, que es la **variante B del
KF04**, no la del KF05. Salió el abogado otra vez. El identificador correcto era
`CqOTQ2uEEy`; el loop bueno quedó en `yiek2LTPW9`. 280 créditos perdidos.

La lección queda escrita: antes de mandar a generar, confirmar que el
identificador corresponde al plano y no solamente a la variante.

## Cómo se ajustó cada loop a su ranura

Los loops salen a 1280×720, 241 cuadros, 24/1. La línea va a 1920×1080 y
24000/1001. Dos caminos, y el criterio importa:

- **Ranura más corta que el loop** → se toma una **ventana a velocidad nativa**.
  Acelerar un Kling se nota mucho más que frenarlo: los gestos quedan nerviosos.
- **Ranura más larga que el loop** → `setpts` con `k = n × 1.001 / 241`. El
  1.001 es el paso de 24 a 23.976; sin él se pierde un cuadro al final.

Todo se escala a 1920×1080 con lanczos en el encode, no en la línea, para que
Resolve no reescale cuadro a cuadro.

| archivo | cuadros | cómo |
|---|---|---|
| `TA02_KF03_bodega_mov314f.mp4` | 314 | setpts, 1.303× más lento |
| `TA02_KF02_entrega_mov152.mp4` | 152 | ventana nativa (pase anterior) |
| `TA02_BR03_cajas_mov264f.mp4` | 264 | setpts, 1.095× más lento |
| `TA02_KF04_abogado_propone_mov200f.mp4` | 200 | ventana nativa desde 0 |
| `TA02_KF05_andres_escucha_mov165f.mp4` | 165 | ventana nativa **desde el cuadro 40** |
| `TA02_BR03_cajas_mov91f.mp4` | 91 | ventana nativa desde 0 |
| `TA02_KF05_andres_escucha_mov172f.mp4` | 172 | ventana nativa **desde el cuadro 69** |

### Por qué el KF05 no arranca en cero

En el primer segundo y medio del loop, el acompañante que está de pie sale de
cuadro. Es el comportamiento conocido de Kling a 10 s: resuelve la situación
entera. Una figura que se va justo al entrar el plano distrae y además contradice
la narración, que en ese punto dice que Andrés ofrece. Entrando en el cuadro 40
el plano empieza con Andrés ya solo, escuchando.

El KF05 aparece dos veces en la línea. La segunda entra en el cuadro 69 del mismo
loop para que no se lea como una repetición literal.

## El re-corte del KF04

En la versión sin movimiento, el KF04 ocupaba una sola ranura de 365 cuadros
(1286 → 1651). Era demasiado para un plano fijo del abogado y no dejaba ver a
Andrés recibiendo la propuesta. Se partió en dos:

- KF04 · el abogado propone · 1286 → 1486 (200 cuadros)
- KF05 · Andrés escucha · 1486 → 1651 (165 cuadros)

El total de la línea no cambia: 3 385 cuadros, 2:21.

## La línea con movimiento

`TA CASO 02 - doble beneficio y reintegro MOV`, duplicada de la línea verbatim y
con siete ranuras de V1 reemplazadas. Todo lo demás —cartones de preguntas en V2,
marca de agua en V4, audio de intro y outro en A1, cama de música en A5— queda
exactamente igual, que es la razón de duplicar en vez de rearmar.

Sin huecos en V1. El hueco de A1 entre el intro y el outro es el esperado: ahí no
va audio de video.

A2, A3 y A4 siguen vacías, esperando las voces.
