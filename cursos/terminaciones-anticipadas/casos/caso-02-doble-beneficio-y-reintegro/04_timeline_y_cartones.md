# Caso 02 · La línea de tiempo armada

Línea **`TA CASO 02 - doble beneficio y reintegro`**, en el proyecto
`DAE MASTER - CURSOS`, dentro de la carpeta del caso.
23,976 fps · 1920 × 1080 · inicio 01:00:00:00 (frame absoluto 86400).
**4946 frames · 3:26**, sin un solo hueco en V1.

Los frames de abajo son relativos al inicio de la línea.

## Las pistas — las de la plantilla, no otras

Esta línea sigue la estructura de `TA - CASO 01 - PLANTILLA`. Quien abra
cualquier caso de la serie encuentra lo mismo en el mismo lugar.

```
V1 VIDEO            intro, cartones de cuadro completo, los once planos, outro
V2 CARTONES         los seis cartones alfa con tinte
V3 APOYO / B-ROLL   libre
V4 MARCA DE AGUA    APRENDE CON LA DAE sobre el cuerpo
V5 EFECTOS          libre
V6 LOWER THIRD      libre
V7 LOWER THIRD 2    libre

A1 VIDEO            el audio del intro y del outro
A2 NARRADOR         los tres bloques del narrador
A3 FACILITADOR      el bloque del facilitador
A4 DIALOGO          el abogado defensor
A5 MUSICA           vacía — falta elegir la pieza
```

## El intro y el outro son el mismo archivo

`FGN_intro_version7.mp4` dura 222 frames en disco pero **la serie lo usa
recortado a 194**, origen 0..193, y el mismo clip va al principio y al final.
Eso es lo que hacen `MA - U1 - INTRODUCCION` y la plantilla del Caso 01.

**Y trae audio** — estéreo AAC a 48 kHz —, que va en **A1 · VIDEO**, en los dos
extremos. Un plano de video apendizado con `mediaType: 1` entra mudo: hay que
apendizar el mismo clip otra vez con `mediaType: 2` sobre la pista de audio.

El `.mp4` de criptoactivos que está en la carpeta OUTRO **no tiene pista de
audio** (`Audio Ch = 0`) y no es el outro de esta serie.

## El orden de los planos — por qué este

Está cortado contra los silencios reales de la locución, medidos con
`silencedetect` sobre los cinco WAV. **Ningún corte parte una palabra**, y cada
plano cae donde la voz dice lo que el plano muestra. Dos consecuencias:

- **El KF 06 se queda con toda la aritmética del 349**, incluida la frase del
  cincuenta por ciento, y el KF 07 entra en «no es un requisito de trámite».
- **El KF 08 se alargó** hasta cubrir «el fiscal verifica las condiciones
  patrimoniales antes de sentarse a negociar, no durante», que es exactamente lo
  que muestra el plano. El KF 09 quedó corto y solo para «no puede convertirse
  en moneda de cambio».

## V1 · VIDEO

| Entra | Sale | Frames | Qué |
|---|---|---|---|
| 0 | 194 | 194 | Intro institucional |
| 194 | 313 | 119 | **Cartón de entrada** |
| 313 | 640 | 327 | KF 01 · la oficina de contratación |
| 640 | 940 | 300 | KF 02 · la entrega |
| 940 | 1220 | 280 | KF 03 · la bodega |
| 1220 | 1410 | 190 | KF 04 · el abogado propone |
| 1410 | 1594 | 184 | KF 05 · Andrés escucha |
| 1594 | 2250 | 656 | **KF 06 · el gráfico del artículo 349** |
| 2250 | 2645 | 395 | KF 07 · el código abierto |
| 2645 | 3160 | 515 | KF 08 · antes de sentarse |
| 3160 | 3312 | 152 | KF 09 · la carpeta cerrada |
| 3312 | 3456 | 144 | **Cartón de pausa** |
| 3456 | 4150 | 694 | KF 10 · el facilitador |
| 4150 | 4633 | 483 | KF 11 · el acta sin firmar |
| 4633 | 4752 | 119 | **Cartón de cierre** |
| 4752 | 4946 | 194 | Outro — el mismo intro |

## V2 · CARTONES

Seis en 3:26 — uno cada 34 segundos, que es el ritmo al que un cartón subraya
sin volverse ruido. Cada uno cae donde la voz está diciendo eso.

| Entra | Sale | Frames | Sobre | Dice |
|---|---|---|---|---|
| 808 | 940 | 132 | KF 02 | **Ciento veinte millones** · Lo que Andrés le entregó a Carlos a cambio de la intervención. |
| 1050 | 1210 | 160 | KF 03 | **Cuatrocientos millones** · El incremento patrimonial ilícito que obtuvo la empresa contratista. |
| 1443 | 1594 | 151 | KF 05 | **La propuesta de la defensa** · Cien millones ahora. Los trescientos restantes, en un plazo de cinco años. |
| 2270 | 2570 | 300 | KF 07 | **No es un requisito de trámite** · Impide que la justicia premial beneficie a quien no hizo esfuerzos suficientes para restablecer el patrimonio afectado. |
| 3026 | 3140 | 114 | KF 08 | **Antes, no durante.** *(suelta)* |
| 3160 | 3312 | 152 | KF 09 | **No es moneda de cambio** · El reintegro patrimonial es una condición que no puede convertirse en moneda de cambio. |

Los dos últimos son del profesor casi literal. Tres de los seis salen y entran
con el corte del plano, que es como se comportan los de la serie JEP.

**Lo que dejé sin cartón a propósito:** todo el bloque del facilitador. Mira a
cámara y hace cuatro preguntas; un cartón encima de una cara que pregunta
compite con la cara. Y el acta sin firmar: la ausencia es la pregunta, y un
texto la contesta.

## V4 · MARCA DE AGUA

`MARCA_DE_AGUA_DAE_100s.mov` dura 2400 frames y el cuerpo son 4320, así que van
dos instancias: **313 → 2713** y **2713 → 4633**. La marca es estática, así que
la costura no se ve. Entra con el cartón de entrada y sale con el de cierre,
igual que en la plantilla.

## El audio

| Pista | Entra | Sale | Frames | Archivo |
|---|---|---|---|---|
| A1 VIDEO | 0 | 194 | 194 | intro |
| A2 NARRADOR | 331 | 1202 | 871 | `TA02_NARRADOR_B1.wav` |
| A4 DIALOGO | 1244 | 1570 | 326 | `TA02_DEFENSA.wav` |
| A2 NARRADOR | 1612 | 2627 | 1015 | `TA02_NARRADOR_B2.wav` |
| A2 NARRADOR | 2663 | 3294 | 631 | `TA02_NARRADOR_B3.wav` |
| A3 FACILITADOR | 3474 | 4615 | 1141 | `TA02_FACILITADOR.wav` |
| A1 VIDEO | 4752 | 4946 | 194 | outro |

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
texto arranca en **x=249**.

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

- **A5 · MUSICA está vacía.** Falta elegir la pieza y montarla a −32 dB bajo la
  voz y −26 en los huecos, que es el nivel de la serie.
- Los **prompts de movimiento**, ahora sí contra la imagen real.
- Confirmar con la DAE si el cartón de pausa de esta serie lleva pregunta con
  opciones, como los de Edwin, o enunciado, como quedó.
