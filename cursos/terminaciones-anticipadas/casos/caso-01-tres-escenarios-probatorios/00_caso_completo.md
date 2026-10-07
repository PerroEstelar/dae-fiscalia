# Caso 01 · los tres escenarios probatorios

Unidad 4 · lección 4.2 · 388 palabras. El mismo hecho contado tres veces con tres
estados de la prueba. Es el primero hecho entero con el método de la voz primero
desde el minuto cero, y el primero donde el rótulo de escenario ordena la pieza.

**3 · 5 714 cuadros · 3:58.**

## La rejilla sale de la voz

Carlos narra, Elisa María lee las preguntas. Las dos pistas se midieron con
`silencedetect` antes de pedir una sola imagen.

```
   0 →  194   intro
 194 →  313   cartón de entrada        (119)
 313 → 4110   narración                (3 797)   A2
      +  36   respiro
4146 → 5365   bloque de preguntas      (1 219)   A3
      +  36   respiro
5401 → 5520   cartón de cierre         (119)
5520 → 5714   outro                    (194)
```

Fronteras medidas de la narración: 575 · 894 · 1143 · 1259 · 1998 · 2788 · 3484 ·
3797. Los quince planos caen exactamente en ellas. Fronteras de las preguntas:
137 · 294 · 531 · 916 · 1219.

## Los tres escenarios son el mismo plano tres veces

El hallazgo del caso. Los escenarios 1, 2 y 3 abren con **la misma cámara de
seguridad, el mismo monitor, el mismo pasillo y la misma hora**; lo único que
cambia es lo que se alcanza a ver:

| | plano | lo que muestra |
|---|---|---|
| Escenario 1 | KF06 | se identifica claramente a Alejandro |
| Escenario 2 | KF09 | una figura tapada por el montante, sin rostro |
| Escenario 3 | KF12 | el pasillo vacío |

Las variantes B y C se pidieron **con la A como referencia**, no con un prompt
nuevo. Es lo que hace que se lean como la misma cámara y no como tres bodegas
distintas.

Los tres rótulos van en V2 sobre esos planos: la etiqueta en el antetítulo
—«Escenario 1»— y debajo una frase literal del guion. El rótulo ordena; el
profesor habla.

## Los quince planos

| # | plano | cuadros | gesto |
|---|---|---|---|
| 01 | el depósito | 308 | la mano plana sobre la tapa que todavía no cierra |
| 02 | la madrugada | 267 | la mano en la manija y la franja de luz en el piso |
| 03 | el abogado propone | 319 | la carpeta empujada y la mano encima sin soltarla |
| 04 | el fiscal valora | 249 | la mano abierta en el hueco, sin tocar ninguna pila |
| 05 | tres escenarios | 116 | tres carpetas idénticas en fila, cenital |
| 06 | **cámara A** | 196 | el rostro legible |
| 07 | la tarjeta | 217 | la tarjeta a dos dedos del lector, sin tocarlo |
| 08 | el dinero hallado | 326 | el locker abierto y dos que miran a otro lado |
| 09 | **cámara B** | 187 | la figura tapada por el montante |
| 10 | varios autorizados | 309 | tres manos y tres tarjetas en el mismo lector |
| 11 | el testigo | 294 | la mano en el aire señalando nada |
| 12 | **cámara C** | 191 | el pasillo vacío |
| 13 | nadie lo vio | 171 | cuatro hombres, cuatro direcciones de atención |
| 14 | el que solo oyó decir | 334 | la boca apenas abierta y el otro ya mirando lejos |
| 15 | la misma propuesta | 313 | la misma carpeta, y ahora nadie la toca |

El KF15 es el gemelo del KF03, pedido con el KF03 como referencia: mismo
despacho, misma gente, misma carpeta en el mismo sitio, pero la mano ya no está
encima. La propuesta es «exactamente la misma» y eso se ve, no se dice.

## Lo que hubo que rehacer

**El KF01 miraba a cámara** con los ojos muy abiertos: las dos cosas que el
negativo bloqueaba. El negativo genérico no sirvió; lo que sirvió fue describir
la mirada por sus efectos dentro del párrafo del plano — *«la cabeza inclinada
unos veinte grados, las pupilas abajo en los ojos, se ve casi todo el párpado
superior, la línea de la mirada cae dentro de la caja»*.

**El KF14 era una caricatura de chismoso**: inclinado, la mano junto a la boca,
la boca muy abierta. Otra vez, decirlo en positivo — *«la espalda recta, la
cintura sin doblar, las dos manos colgando a los lados, la boca apenas abierta,
la separación entre los labios no más gruesa que un lápiz»*.

**Los loops del KF06 y del KF09 no se pudieron usar.** Kling resuelve la
situación: en el A el hombre camina y termina de espaldas, en el B la figura se
va del pasillo. Se pidieron dos veces, con «no camina, se queda exactamente donde
está, del mismo tamaño» escrito tres veces en el prompt, y las dos veces hizo lo
mismo. Quedaron como **still**: una grabación de cámara de seguridad congelada se
lee bien así, y el KF12 —que sí tiene loop— es casi estático de todos modos, así
que los tres monitores se leen igual.

**El KF08 cerraba la puerta del locker** sobre la bolsa a mitad del plano. Se
repitió pidiendo que la puerta no se moviera ni un grado, y quedó.

## Los cortes

23 cortes con `ajustar_planos.py`, 0 descuadrados. Los planos de gesto terminado
—el 04, el 08, el 14 y el 15— entraron con `loop_congela` en vez de frenarse: la
ranura es más larga que el loop pero el movimiento ya acabó, así que se deja
reposar en vez de arrastrarlo. Los de movimiento continuo se frenaron entre 1,11×
y 1,33×.

Los ocho planos del bloque de preguntas vuelven por otro punto del loop. La
pregunta 3 —en cuál de los escenarios— trae los **tres monitores seguidos**,
128 + 128 + 129 cuadros: la pregunta se contesta mostrándolos.

## La música

`primalhousemusic-pondering-weak-and-weary-193890.mp3`, de la carpeta del caso 2
del profe Carlos Humberto — cuarta pista distinta, para no repetir ninguna de las
tres anteriores. Entra en el cuadro 81 y termina donde arranca el outro.

Medida por regiones: **−31,5 LUFS** bajo la narración y **−25,3** bajo el bloque
de preguntas.

Primer intento salió mal y vale anotarlo: se pasaron los dos tramos de voz como
tramos a agachar y el bloque de preguntas quedó en −31. **El ducking se calcula
solo contra la narración**; bajo las preguntas la música sube.

## El gasto

21 imágenes (15 planos más 6 variantes y repeticiones) y 18 loops: **6 940
créditos**.
