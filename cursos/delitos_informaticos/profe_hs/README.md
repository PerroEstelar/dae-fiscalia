# Delitos informáticos · videos de profe, grabaciones del 24 nov 2026

Las diez grabaciones del guion del curso: presentación y cierre del curso, y la introducción y el cierre de cada una
de las cuatro unidades. Profe: coautor del curso, **nombre sin confirmar** (ver abajo). **Entrega provisional**: intro, cartón de título,
cartón de cierre y outro, sin rótulo; el cuerpo va sin gráficos. Base: `base_hs_profe.py`.

## El pedido

Sebastián (24 nov): «we just got delitos informáticos, estilo de gráfica provisional, profe hablando a cámara (…) no
entiendo por qué hay U3 y U4 si ya los había hecho, por favor revisa la documentación de este curso y averigua por qué,
pero igual procesa todo este batch, lo mismo que ya sabemos hacer; me recomendaron que mejorara los niveles y
ecualización de estos videos». Carpeta del pedido: `1r5rcMiIs8Pw6RbO438B2BYAqXchAXFst`.

Decisiones de Sebastián (24 nov):
- **Sin rótulo.** Primero respondió «Humberto Suárez Gómez», «Coautor del curso», y la primera entrega salió con ese
  rótulo. Después: «por ahora no le pongamos rótulo al profesor porque no está confirmado» quién es. Desde la v2 (v3 en
  la presentación del curso y el cierre de la U1) va sin rótulo, y el nombre de los archivos lleva «24NOV» (por la
  carpeta de las grabaciones) en vez del apellido. Las líneas («DI HS») y esta carpeta (`profe_hs`) quedaron con el
  nombre de antes; si se confirma, `ROTULO_CONFIRMADO = True` en la base devuelve el rótulo.
- **Lo de Yefrin se deja:** «dejar ambos». Estos van en otra carpeta y con otro nombre (`… - 24NOV`).

## Por qué vuelven a estar la U3 y la U4

El curso tiene dos autores en la ficha («1.5 Autor: Garavito Yefrin, Suárez Gómez Humberto», en el vaciado general y
en los cuatro de unidad). La ficha dice que «el equipo autor reúne esas dos experiencias», la del fiscal y la del
ingeniero, y que «sus integrantes acompañarán al participante en videos». Por unidad pide dos videos: «Video unidad N»
(la introducción, con su guion) y «Video de cierre de la unidad». Además pide la presentación del curso.

- **Lo del 22 nov** (`../profe/`) eran cinco videos que el ingeniero **Yefrin Garavito** editó por su cuenta, con sus
  cartones y su placa: bienvenida, intermedio y cierre de la U3 y la U4. Los «intermedios» no están en la ficha. Su
  bienvenida de la U3 es una versión suya del guion de la ficha.
- **Lo de hoy** son los diez videos de la ficha completa: el guion de cada unidad, leído por otro coautor (el nombre
  falta confirmarlo).

O sea, no es un error de envío: son dos juegos distintos. La U3 y la U4 tienen ahora dos introducciones y dos cierres
(uno de cada profe). Cuál va en el aula lo decide la DAE.

## Lo que llegó

`E:\DAE MASTER\CURSO DELITOS INFORMATICOS\GRABACIONES 24 NOV\`. Son diez exports ProRes 422 HQ:
- 1280×720, 10000/333 ≈ 30,03 cuadros/s, 10 bits, BT.709;
- audio PCM float mono a 48 kHz;
- entre 2,6 y 3,6 min cada uno.

Se copiaron del Drive del pedido a «Mi unidad» con una copia de servidor y se leyeron desde G:; la copia de Drive se
mandó a la papelera. El profe está al centro, sobre el fondo del campus, con el panel DAE/Fiscalía arriba a la
izquierda, que es parte del fondo. Ya vienen editadas.

## El audio (lo nuevo de este lote)

Medido en 2 min de cada grabación (`herramientas/audio/voz_analisis.py`, resultado en `voz_hs.json`):
- **Nivel:** −38 a −42 LUFS.
- **Piso de ruido:** −53 a −60 dBFS, a unos 19–22 dB de la voz.
- **Espectro**, contra la voz media de referencia (Byrne 1994):
  - +5 a +9 dB entre 125 y 630 Hz;
  - −7 dB en 1 kHz;
  - −5 a −16 dB arriba de 2,5 kHz.

  Es una voz apagada y con mucho cuerpo.

Cada plan lleva su `AUDIO_CADENA`, que va antes del dual-mono y antes del loudnorm de siempre en dos pasadas
(`I=-16:TP=-3:LRA=7`):
1. paso alto de 90 Hz;
2. ganancia previa a −20 LUFS;
3. `firequalizer` con el 70 % de la diferencia con la referencia, suavizada, con topes de −8 y +7 dB y nada sobre
   12,5 kHz;
4. `afftdn` suave (nr 6);
5. expansor (`agate` 2:1);
6. compresor de picos;
7. de-esser suave;
8. limitador.

Comparada con la cadena de siempre sobre los mismos 2 min:
- El desvío espectral frente a la referencia baja de 8–9 dB (original) y ~7 dB (cadena de siempre) a 3–3,6 dB.
- El piso en las pausas queda 2 a 9 dB más abajo.

Dos variantes se descartaron:
- `afftdn` fuerte antes de la curva se comía los agudos.
- `anlmdn` también se los comía.

## Cortes

Los bordes van 0,45 s antes de la primera palabra y 0,7 s después de la última. Los cortes internos caen en silencio,
medido en RMS de 10 ms, y llevan 6 cuadros de mezcla. El detalle está en cada plan.

| plan | pieza | cortes |
|---|---|---|
| `plan_dxci` | presentación del curso | «de Buda-» (el Convenio de Buda- de Budapest) y «su--» (vuelve su-- sobre su decisión) |
| `plan_dxcc` | cierre del curso | — |
| `plan_dxu1i` / `plan_dxu1c` | U1 inicio / cierre | cierre: «a--» (pasamos a-- de comprender) |
| `plan_dxu2i` / `plan_dxu2c` | U2 inicio / cierre | inicio: sale «Listo.»; cierre: «instrusión-- la», «ileti--» |
| `plan_dxu3i` / `plan_dxu3c` | U3 inicio / cierre | — |
| `plan_dxu4i` / `plan_dxu4c` | U4 inicio / cierre | cierre: dos intentos fallidos y «Voy a pulir» (71,3–127,0 s), «ye--» |

## Cómo se arma

- **Ventana:** el cuadro entero (1280×720 desde 0, 0), subido a 1080. `MATRIZ_FUENTE` bt709, y se compone a
  10000/333 (`FPS_COMPUESTO`).
- **Rótulo:** ninguno mientras el nombre no esté confirmado (la v1 lo llevaba abajo a la izquierda, a 1,5 s del arranque).
- **Lote:**
  - `lote/cadena_hs.py`: compuesto, cartón de título y rótulo, tres a la vez;
  - `lote/entrega_gpu.py`: línea de Resolve, entrega por la placa NVIDIA (~5 Mb/s, como en Derecho de petición),
    hoja de revisión y copia a `_MA subidas`.

  La carpeta de trabajo es `D:\DAE\_tmp\di2\`.
- **Árbol:** `E:\DAE MASTER\PRIORIDAD 03\CURSO DELITOS INFORMATICOS - VIDEOS PROFE HS\<CURSO|UNIDAD n>\<INICIO|CIERRE>`.
- **Líneas:** `DI HS - …`.
- **Entregas:** `delitosinformaticos - <CURSO|Un> - <INICIO|CIERRE> - 24NOV-vN.mp4` (la v1 decía `- SUAREZ-v1`).

## Entregas (24 nov 2026)

Carpeta: Delitos Informáticos › [VIDEOS PROFE - GRABACIONES 24 NOV](https://drive.google.com/drive/folders/1HX0c6ozxiOugKsaD9W2ktS5WUQlFuM0L)
(`1HX0c6ozxiOugKsaD9W2ktS5WUQlFuM0L`), cada video con su `.srt`; copia del `.srt` junto al video en `05 EXPORTS`.

| pieza | video | dura | .srt |
|---|---|---|---|
| presentación del curso | [CURSO - INICIO - 24NOV-v3](https://drive.google.com/file/d/14LKKfPPtGXVcmXOyop5gDmlGlIJGJKlY/view) | 4:06 | [64](https://drive.google.com/file/d/18G5NtweUcJ7MZsAltKdraE3dSkYdCQFG/view) |
| U1 inicio | [U1 - INICIO - 24NOV-v2](https://drive.google.com/file/d/1ArB0gFz3a_DeXxNhuONmgC-l9UzQ3IN_/view) | 3:29 | [53](https://drive.google.com/file/d/1w6D_oAa6It55-CPvsa83LhkU7CqYKi1y/view) |
| U1 cierre | [U1 - CIERRE - 24NOV-v3](https://drive.google.com/file/d/11mtWBl1EBjMh5IqGrJWiPDKhj9FfqMug/view) | 3:08 | [50](https://drive.google.com/file/d/1FqHeDfFn9KweD-OmoFSfI5HZqfYie-2e/view) |
| U2 inicio | [U2 - INICIO - 24NOV-v2](https://drive.google.com/file/d/1_AsEEx0fQiKb49PIRIofn1ABT9FK6s35/view) | 3:15 | [52](https://drive.google.com/file/d/1MbOldgSlIgqbJTGaLqj-Vipx1cyaqDc1/view) |
| U2 cierre | [U2 - CIERRE - 24NOV-v2](https://drive.google.com/file/d/1Ht_6ynKz6pNr44TzN9NMOKCC8iEz8r5a/view) | 3:23 | [53](https://drive.google.com/file/d/15Cb1QXobfLGDot1x0OxraAi8iwKkqeCB/view) |
| U3 inicio | [U3 - INICIO - 24NOV-v2](https://drive.google.com/file/d/14b7cX9nxp9tclqSkaY8iN4efFWrMYrVp/view) | 3:18 | [47](https://drive.google.com/file/d/17EizzPQeRt219vyhnwMnntVZSz1k6duh/view) |
| U3 cierre | [U3 - CIERRE - 24NOV-v2](https://drive.google.com/file/d/1agqYjGKfoL6ob7n8RaKHR0hKwPTkN0EK/view) | 3:28 | [51](https://drive.google.com/file/d/1_wPn_qWgPzdIUu-qWD8dUJdGBVTYTlHo/view) |
| U4 inicio | [U4 - INICIO - 24NOV-v2](https://drive.google.com/file/d/1-0Tp4LUXd6JO_Mxm-tVhxX73wW6s4HQ5/view) | 3:26 | [51](https://drive.google.com/file/d/1fnEFQKs7uW0r4jolKfg-vAEPI1qBr64v/view) |
| U4 cierre | [U4 - CIERRE - 24NOV-v2](https://drive.google.com/file/d/1OBsckuPnS0pc9_V4qrEcqEGPh32CeTOp/view) | 3:07 | [48](https://drive.google.com/file/d/1PCTyP55QnErMHpeoGC2LqwG3-4b-lFEq/view) |
| cierre del curso | [CURSO - CIERRE - 24NOV-v2](https://drive.google.com/file/d/1Y2JrDFhPAorHRZWWWZiX1wT0OdmrlX_X/view) | 3:14 | [46](https://drive.google.com/file/d/1YPsZCtkkPi3PZh-K40ocD7DeL11HknVk/view) |

- Render NVIDIA desde Resolve (~5,3 Mb/s), −16,1 a −16,2 LUFS, picos de −2,3 a −3,8 dBTP. Las diez se verificaron byte a
  byte contra lo que guarda Drive (copia de servidor a `_MA subidas`, que después fue a la papelera).
- Versiones anteriores, en [`_anteriores`](https://drive.google.com/drive/folders/1Kt4txMzQ1yW-OlP9CK6RKZzjm7EwGa4a) y en
  `05 EXPORTS\_anteriores`: las v1 con rótulo y «SUAREZ», y las v2 de la presentación y del cierre de la U1 (v1 → v2:
  sale «de Buda-»; el corte de la U1 se llevaba el «-mos» de «pasamos»: lo cazó Scribe al hacer los subtítulos).
- **El conector de Drive ya no puede mover lo que sube Drive para escritorio** (24 nov: «The caller does not have
  permission to move this file», `canMoveItemWithinDrive: false` aunque el dueño es Sebastián). Se hizo así: copia de
  servidor a la carpeta final; los originales de paso se movieron en G: a la carpeta de verificación y esa carpeta,
  creada por el conector, se mandó a la papelera con todo adentro.
