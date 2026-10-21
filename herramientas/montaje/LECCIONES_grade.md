# Lo que el Caso 4 enseñó sobre el grade de la serie

21 de octubre de 2026. Escrito después de romper el mismo set de placas
cuatro veces, y de que la medida de aceptación las diera por buenas las
cuatro.

## El síntoma

Los crudos del Caso 4 salieron del modelo mucho más claros y planos que
los del Caso 3. Medido en percentiles de luma:

```
Caso 3 aprobado, final      23,6 /  85,0 / 201,6
Caso 4 crudo                68,0 / 133,9 / 183,6
objetivo de la serie        23   /  84   / 205
```

Al Caso 3 el grade tenía que estirarlo poco; al Caso 4 le toca estirarlo
casi el doble. Y al estirar aparecía moteado de piedra con manchas de
color en las mesas oscuras, y ruido de arcoíris en el papel: exactamente
lo que todos los prompts de la serie prohíben.

## La causa real, que no era ninguna de mis tres primeras hipótesis

No es el bit depth, ni el tope de dureza, ni dónde está el grano.
**Es dónde se ancla la curva.**

La curva de la serie fija tres puntos — p2→23, p50→84, p98→205 — y eso
supone un histograma repartido. En una toma cenital de papel sobre mesa,
el papel o la mesa ocupan más de la mitad del cuadro con UN SOLO valor,
así que la mediana cae dentro de esa mancha:

```
r01   p2  61   p50  63   p98 113     la mesa es p2 y p50 a la vez
r33   p2  84   p50 209   p98 211     el papel es p50 y p98 a la vez
```

Entonces la curva tiene que llevar dos niveles a sesenta — pendiente ×30
— y lo que estira es el escalonado de la cuantización. Ocho de las 36
placas estaban rotas así, seis de ellas por arriba.

La corrección está en `graduar_serie.anclas`: cuando la mediana queda a
menos de 20 niveles de un extremo, deja de usarse como ancla y los tres
puntos se vuelven un mapa de dos. La pendiente de esas ocho cayó de
24–60 a 1,3–4,4, que es la banda de las que sí salieron bien.

**No hubo que regenerar ninguna placa.**

## Los cuatro errores, que son todos el mismo error

1. **Anular `TOPE_DUREZA` en 28 de 36 placas.** Lo "verifiqué" midiendo
   la planitud sobre el 60 % más plano del cuadro. En una placa con papel
   claro, el 60 % más plano ES EL PAPEL, que aguanta cualquier estirón.
   La mesa oscura —la que se rompe— nunca entró en la medición.

2. **Tramar al cuantizar.** Arregla el redondeo final. Aquí el daño es la
   amplificación, que ocurre antes.

3. **Alisar lo medido como plano y oscuro.** Dejó el papel roto por
   arriba (el grano de r08 subió a 12,51 contra 2,25 de la peor
   aprobada), y al quitarle la restricción de "oscuro" se comió el texto
   de r16.

4. **Dejar la piel fuera con un umbral fijo** (R−B > 12). Se comió la
   mano de r37, que vive entre 4 y 12 porque está en penumbra sobre papel
   claro.

Los cuatro son el mismo error: **medir en la población equivocada.** Un
umbral o una verificación no valen nada si el conjunto sobre el que se
toman no incluye el caso que puede romperse.

## Lo que sí funciona

- **Separar por amplitud, no por sitio** (`suave.quitar_grano`). El grano
  es de uno a tres niveles; el dibujo de esta serie es de veinte o
  cuarenta. No hace falta saber dónde mirar. El umbral se mide en cada
  placa y se escala con la pendiente que le va a caer encima, porque lo
  que hay que acotar es el ruido de SALIDA.

- **La mancha de color va aparte** (`suave.alisar_croma`). El moteado de
  r22 y r25 era cromático y una medida de gris no lo ve. Se alisan las
  dos diferencias de color y se reconstruye el píxel con la luma exacta
  de antes: el dibujo vive en la luma y la luma no se toca.

- **El tinte que mete el propio grade** (`suave.neutralizar_entorno`). La
  curva por canal alinea los tres canales y, si sus percentiles no
  coincidían, corre el entorno hacia un color: r28 salió con el fondo
  verde-azulado en el 40 % del cuadro partiendo de un crudo gris. Se
  resta localmente, no por media global —el papel blanco diluía la
  media— y la piel se deja fuera midiéndola, no con un número.

- **El tope de la piel, relativo al cuadro** (`piel.techo_de`). El tope
  de 1,5 se puso contra un plano en penumbra y era bueno ahí. En una mano
  sobre escritorio claro dejaba la piel cuatro veces más oscura que la
  mesa que la sostiene. Ahora la piel puede subir hasta el p75 de la
  propia imagen: el motivo original del tope —que la cara no brille sobre
  su entorno— queda intacto, porque el techo ES el entorno.

## La regla que queda

**Una placa no se da por buena hasta haberla mirado a 1:1 sobre su zona
más oscura y sobre su zona más clara.** La medida pasó las cuatro
versiones rotas. La medida sirve para encontrar la placa sospechosa entre
treinta y seis; no sirve para firmarla.

Y la banda de aceptación se mide **contra el set aprobado**, no contra
cero. El look de la serie es 0,017 de saturación media y 1,48 de
gradiente en zona oscura, no neutralidad perfecta.

## Medidas de referencia (Caso 3 aprobado, 10 placas)

```
zona oscura, gradiente medio    0,14 a 1,48
zona oscura, croma              0,42 a 4,84  (mediana 0,6)
zona clara, gradiente medio     medio 1,02 · peor 2,25
saturación media                0,017
% de píxeles con tinte azul     1,0 (peor 9,5)
```

Caso 4, las 36 ya terminadas: zona oscura 1,33 · croma 1,24 · zona clara
1,45 · tinte azul 0,1 % · sin ninguna placa fuera de banda por tinte.
