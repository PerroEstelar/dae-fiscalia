# Caso 02 · La línea de tiempo armada

Línea **`TA CASO 02 - doble beneficio y reintegro`**, en el proyecto
`DAE MASTER - CURSOS`, dentro de la carpeta del caso.
23,976 fps · 1920 × 1080 · inicio 01:00:00:00 (frame absoluto 86400).
**4899 frames · 3:24**, sin un solo hueco en V1.

Los frames de abajo son relativos al inicio de la línea.

## Las pistas

```
V2 · CARTONES   los seis cartones alfa con tinte
V1 · PLANOS     intro, cartones de entrada/pausa/cierre, los once planos, outro
A1 · VOZ        los cinco bloques de locución
```

## El orden de los planos — por qué este y no el de la v2

El reparto anterior dividía cada bloque en partes iguales. Este está cortado
contra los silencios reales de la locución, medidos con `silencedetect` sobre
los cinco WAV. **Ningún corte parte una palabra**, y cada plano cae donde la voz
dice lo que el plano muestra. Eso cambió tres cosas:

- **El bloque 1 cambió de orden.** Queda `BR02 corredor → KF01 oficina →
  KF03 bodega → KF02 la entrega → BR01 expediente → BR03 cajas`. La bodega entra
  en «el suministro de equipos médicos» y el sobre entra en «Andrés le entregó a
  Carlos ciento veinte millones», que es donde tenían que estar. Antes el sobre
  caía doce segundos antes de que se mencionara la plata.
  *(Este orden está en la hoja de montaje; en la línea armada el bloque 1 va con
  los planos KF01–KF03 en el reparto de abajo, que es el que se montó.)*
- **El KF 06 se partió del KF 07 en otro punto**: el gráfico se queda con toda
  la aritmética del 349, incluida la frase del cincuenta por ciento, y el KF 07
  entra en «no es un requisito de trámite».
- **El KF 08 se alargó** hasta cubrir «el fiscal verifica las condiciones
  patrimoniales antes de sentarse a negociar, no durante», que es exactamente lo
  que muestra el plano. El KF 09 quedó corto y solo para «no puede convertirse en
  moneda de cambio».

## V1 · los planos

| Entra | Sale | Frames | Qué |
|---|---|---|---|
| 0 | 222 | 222 | Intro institucional `FGN_intro_version7.mp4` |
| 222 | 341 | 119 | **Cartón de entrada** |
| 341 | 668 | 327 | KF 01 · la oficina de contratación |
| 668 | 968 | 300 | KF 02 · la entrega |
| 968 | 1248 | 280 | KF 03 · la bodega |
| 1248 | 1438 | 190 | KF 04 · el abogado propone |
| 1438 | 1622 | 184 | KF 05 · Andrés escucha |
| 1622 | 2278 | 656 | **KF 06 · el gráfico del artículo 349** |
| 2278 | 2673 | 395 | KF 07 · el código abierto |
| 2673 | 3188 | 515 | KF 08 · antes de sentarse |
| 3188 | 3340 | 152 | KF 09 · la carpeta cerrada |
| 3340 | 3484 | 144 | **Cartón de pausa** |
| 3484 | 4178 | 694 | KF 10 · el facilitador |
| 4178 | 4661 | 483 | KF 11 · el acta sin firmar |
| 4661 | 4780 | 119 | **Cartón de cierre** |
| 4780 | 4899 | 119 | Outro institucional |

El outro está a 30 fps y Resolve lo conforma solo a 119 frames. No hay que
tocarle el rango de origen: pedirle uno es lo que rompe los clips de otra
velocidad.

## V2 · los cartones alfa

Seis en 3:24 — uno cada 34 segundos, que es el ritmo al que un cartón subraya
sin volverse ruido. Cada uno cae donde la voz está diciendo eso.

| Entra | Sale | Frames | Sobre | Dice |
|---|---|---|---|---|
| 836 | 968 | 132 | KF 02 | **Ciento veinte millones** · Lo que Andrés le entregó a Carlos a cambio de la intervención. |
| 1078 | 1238 | 160 | KF 03 | **Cuatrocientos millones** · El incremento patrimonial ilícito que obtuvo la empresa contratista. |
| 1471 | 1622 | 151 | KF 05 | **La propuesta de la defensa** · Cien millones ahora. Los trescientos restantes, en un plazo de cinco años. |
| 2298 | 2598 | 300 | KF 07 | **No es un requisito de trámite** · Impide que la justicia premial beneficie a quien no hizo esfuerzos suficientes para restablecer el patrimonio afectado. |
| 3054 | 3168 | 114 | KF 08 | **Antes, no durante.** *(suelta)* |
| 3188 | 3340 | 152 | KF 09 | **No es moneda de cambio** · El reintegro patrimonial es una condición que no puede convertirse en moneda de cambio. |

Los dos últimos son del profesor casi literal. Tres de los seis salen y entran
con el corte del plano, que es como se comportan los de la serie JEP.

**Lo que dejé sin cartón a propósito:** todo el bloque del facilitador. Mira a
cámara y hace cuatro preguntas; un cartón encima de una cara que pregunta
compite con la cara. Y el acta sin firmar: la ausencia es la pregunta, y un
texto la contesta.

## A1 · la voz

| Entra | Sale | Frames | Archivo |
|---|---|---|---|
| 359 | 1230 | 871 | `TA02_NARRADOR_B1.wav` |
| 1272 | 1598 | 326 | `TA02_DEFENSA.wav` |
| 1640 | 2655 | 1015 | `TA02_NARRADOR_B2.wav` |
| 2691 | 3322 | 631 | `TA02_NARRADOR_B3.wav` |
| 3502 | 4643 | 1141 | `TA02_FACILITADOR.wav` |

Cada bloque entra 18 frames después del inicio de su tramo y sale antes del
corte siguiente. El diálogo de la defensa lleva 24 de aire a cada lado, para
que se lea como escena y no como narración.

---

## Los cartones · la retícula medida

La retícula no se heredó de un documento: se midió sobre
`A_carton_pausa1.mov` y `A_carton_cierre.mov` del Caso A del profe Edwin, y el
cartón de entrada sobre `U1-PROFE EDWIN - CASO A - carton de caso.mp4`. El
generador es `herramientas/cartones/cartones_ta.py`.

```
barra    #FCB500 · 28 px de ancho · borde izquierdo en x=176
texto    Montserrat · x=249 · ancho máximo 1250
centro   óptico del bloque en y=583
tinte    #03398B al 46 % (alpha 117) sobre todo el cuadro
blanco   fondo #FCFCFC · texto azul noche #07224B
marca    APRENDE CON LA DAE · 408 px de ancho · en (1351, 131) · al 10 %
tamaños  antetítulo SemiBold 30 · título Bold 54 · cuerpo Medium 44 · suelta Bold 72
```

**Ojo con la escala.** La nota vieja de la serie JEP decía barra de 14 px en
x=175. Eso es de otra escala. Medida sobre los cartones de Edwin —que es la
serie con la que se alinean estos videos— la barra son **28 px en x=176**, y el
texto arranca en **x=249**. Si un cartón de esta serie se ve flaco, es que se
hizo con la retícula vieja.

### El movimiento

El mismo de la v3 de medio ambiente, que ya pasó revisión:

- la barra crece desde arriba en 10 f con `easeOutCubic`;
- el texto entra desde el frame 6, línea por línea, subiendo 14 px en 14 f,
  escalonado 3 f;
- salida en 10 f bajando 8 px, escalonada 2 f, y la barra se retrae en los
  últimos 10 f;
- el tinte entra en 12 f y sale en 10 f.

### Los tres cartones de cuadro completo

- **Entrada** (119 f, opaco): antetítulo `CASO 02` y título
  `El doble beneficio y el reintegro`, sobre blanco, con la marca de agua.
- **Pausa** (144 f, opaco): `El reintegro no se negocia. Se verifica.` sobre el
  KF 09 con el tinte azul, igual que los cartones de pausa de Edwin.
- **Cierre** (119 f, opaco): `¿Hasta dónde puede negociar el fiscal?`

### El KF 06 — el gráfico del 349

Se armó con el mismo generador, no en After Effects. Placa limpia, misma
familia tipográfica, 656 frames, con cuatro entradas escalonadas:

1. la barra entera — el incremento patrimonial de cuatrocientos millones;
2. la porción ofrecida — cien millones, una cuarta parte;
3. el remanente — trescientos millones en cinco años;
4. **la marca del cincuenta por ciento**, que entra medio segundo *después* de
   que la voz dice la cifra, no mientras la dice. Ese desfase es lo que la hace
   leerse como conclusión y no como subtítulo.

Si se prefiere hacerlo en After Effects, el archivo actual sirve de guía de
tiempos y de posición.

---

## Bajar de Magnific sin intermediarios

`herramientas/magnific/bajar_de_magnific.py`.

El contenedor en la nube donde corre Claude **no alcanza el CDN de Magnific**:
`pikaso.cdnpk.net` le responde 403 al proxy de salida. La máquina de Sebastián
sí lo alcanza. Entonces Claude arma un manifiesto JSON y lo corre acá con
`script_plugin run_inline`, que es un Python completo sobre esta máquina y ve
E: y D:.

El script baja, verifica que lo bajado sea de verdad un PNG o un MOV y no una
página de error, respalda lo que iba a pisar, y —si el manifiesto trae
`carpeta_pool`— importa al media pool del proyecto abierto.

Las URL de Magnific llevan token con vencimiento: si una responde 403 o 410 hay
que volver a pedirla con `creations_wait`, no reintentar.

---

## Lo que queda

- Los **prompts de movimiento**, ahora sí contra la imagen real.
- Revisar en pantalla el KF 06: es el único elemento de la pieza que no salió ni
  de Magnific ni del profesor.
- Confirmar con la DAE si el cartón de pausa de esta serie lleva pregunta con
  opciones, como los de Edwin, o enunciado, como quedó.
