# Delitos informáticos · videos de profe de Humberto Suárez Gómez (24 nov 2026)

Las diez grabaciones del guion del curso: presentación y cierre del curso, y la introducción y el cierre de cada una
de las cuatro unidades. Profe: **Humberto Suárez Gómez**, coautor del curso. **Entrega provisional**: intro, cartón de
título, rótulo, cartón de cierre y outro; el cuerpo va sin gráficos. Base: `base_hs_profe.py`.

## El pedido

Sebastián (24 nov): «we just got delitos informáticos, estilo de gráfica provisional, profe hablando a cámara (…) no
entiendo por qué hay U3 y U4 si ya los había hecho, por favor revisa la documentación de este curso y averigua por qué,
pero igual procesa todo este batch, lo mismo que ya sabemos hacer; me recomendaron que mejorara los niveles y
ecualización de estos videos». Carpeta del pedido: `1r5rcMiIs8Pw6RbO438B2BYAqXchAXFst`.

Decisiones de Sebastián (24 nov):
- **Rótulo:** «Humberto Suárez Gómez», cargo «Coautor del curso».
- **Lo de Yefrin se deja:** «dejar ambos». Estos van en otra carpeta y con otro nombre (`… - SUAREZ`).

## Por qué vuelven a estar la U3 y la U4

El curso tiene dos autores en la ficha («1.5 Autor: Garavito Yefrin, Suárez Gómez Humberto», en el vaciado general y
en los cuatro de unidad). La ficha dice que «el equipo autor reúne esas dos experiencias», la del fiscal y la del
ingeniero, y que «sus integrantes acompañarán al participante en videos». Por unidad pide dos videos: «Video unidad N»
(la introducción, con su guion) y «Video de cierre de la unidad». Además pide la presentación del curso.

- **Lo del 22 nov** (`../profe/`) eran cinco videos que el ingeniero **Yefrin Garavito** editó por su cuenta, con sus
  cartones y su placa: bienvenida, intermedio y cierre de la U3 y la U4. Los «intermedios» no están en la ficha. Su
  bienvenida de la U3 es una versión suya del guion de la ficha.
- **Lo de hoy** son los diez videos de la ficha completa: el guion de cada unidad, leído por el otro coautor.

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
| `plan_dxci` | presentación del curso | «su--» (vuelve su-- sobre su decisión) |
| `plan_dxcc` | cierre del curso | — |
| `plan_dxu1i` / `plan_dxu1c` | U1 inicio / cierre | cierre: «a--» (pasamos a-- de comprender) |
| `plan_dxu2i` / `plan_dxu2c` | U2 inicio / cierre | inicio: sale «Listo.»; cierre: «instrusión-- la», «ileti--» |
| `plan_dxu3i` / `plan_dxu3c` | U3 inicio / cierre | — |
| `plan_dxu4i` / `plan_dxu4c` | U4 inicio / cierre | cierre: dos intentos fallidos y «Voy a pulir» (71,3–127,0 s), «ye--» |

## Cómo se arma

- **Ventana:** el cuadro entero (1280×720 desde 0, 0), subido a 1080. `MATRIZ_FUENTE` bt709, y se compone a
  10000/333 (`FPS_COMPUESTO`).
- **Rótulo:** abajo a la izquierda, a 1,5 s del arranque, con «Humberto / Suárez Gómez» y «Coautor del curso».
- **Lote:**
  - `lote/cadena_hs.py`: compuesto, cartón de título y rótulo, tres a la vez;
  - `lote/entrega_gpu.py`: línea de Resolve, entrega por la placa NVIDIA (~5 Mb/s, como en Derecho de petición),
    hoja de revisión y copia a `_MA subidas`.

  La carpeta de trabajo es `D:\DAE\_tmp\di2\`.
- **Árbol:** `E:\DAE MASTER\PRIORIDAD 03\CURSO DELITOS INFORMATICOS - VIDEOS PROFE HS\<CURSO|UNIDAD n>\<INICIO|CIERRE>`.
- **Líneas:** `DI HS - …`.
- **Entregas:** `delitosinformaticos - <CURSO|Un> - <INICIO|CIERRE> - SUAREZ-v1.mp4`.

## Entregas

(en proceso)
