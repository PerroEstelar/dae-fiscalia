# Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado · PRIORIDAD 1

Carpeta del Drive con los cuatro documentos (uno por unidad):
`1T7Lzpllmqh-MtWJyKdPCoLbCt8I5S2vq` («PRIORIDAD 1 - LEY 1826 PROCEDIMIENTO
PENAL ABREVIADO»). Dentro, `IMAGENES` (`1ST5k6iqTFtda-xD1O7fmqDuRy-HQSxUN`:
Unidad 1 `1h6NXHpPnZG0r8VnJoFMRRPQEMzANsmCP`, Unidad 3
`1iUTlTecycCSXiA8R2_9Fvd0oPqYovZ8C`) y `VIDEOS`
(`1NWHxVndq7nZsjQLMFud4u0FvZEmigl_q`: Unidad 2
`1Y_lqs6RKjnaWy9__5zaEV5kmkaz9m05U`, Unidad 4
`1RFogbclwzHYAbl0xK_b3ozGy0xohFsbi`). Las entregas suben **solo con el OK de
Sebastián**.

Árbol: `E:\DAE MASTER\PRIORIDAD 1\CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO\`
(00 DOCUMENTOS FUENTE, 00 PERSONAJES, UNIDAD 1..4). Bins iguales en `DAE
MASTER - CURSOS`. Rutas en `herramientas/voz/textos/rutas_lp.py`; metadatos y
textos en `guion_lp.py`.

## Lo que pidió Sebastián (3 nov)

| unidad | qué | de dónde sale el texto |
|---|---|---|
| U1 | 5 láminas tipo afiche | solo «Síntesis fáctica del caso» |
| U2 | 2 videos de la receta completa | solo los hechos (sin las soluciones) |
| U3 | 3 láminas tipo afiche | solo «Premisa fáctica» |
| U4 | 3 videos muy cortos | los casos de análisis 1-3, verbatim |

Créditos de Magnific al mínimo: «mitad y mitad», unos 6.800 para este curso y
el resto en reserva para el siguiente juego de videos.

## Láminas (U1 y U3)

La composición de las láminas de Desaparición Forzada («16 situaciones»):
ilustración a sangre, panel azul `#004890` al 82 % del lado libre, filete
amarillo, rótulo «CASO DE ESTUDIO N», el texto verbatim y la marca APRENDE CON
LA DAE. Afiche: dos ideas por lámina en `prompts/imagenes_lp.py`, elegida en
`elegidas_lp.json → _laminas` (lado y ancho del panel por lámina). Herramienta:
`cartones/lamina_lp.py` (cursiva con Montserrat-Italic-VF a peso 500 para
«capítulo de hechos» en U1 C2). Salen a `02 LAMINA`, `05 EXPORTS` e
`IMAGENES ENTREGA\<ENTREGA>.png`.

## Cinco videos

| | narra | ranuras | pieza (cuadros) | cama |
|---|---|---|---|---|
| U2 C1 Escrito de acusación, flagrancia y nulidad | Carlos | 11 | 2809 | TA03 |
| U2 C2 Audiencia de prueba anticipada | Pilar | 11 | 2770 | TA03 |
| U4 C1 Caso de análisis 1 | Carlos | 6 | 1879 | TA05 |
| U4 C2 Caso de análisis 2 | Pilar | 9 | 2386 | TA05 |
| U4 C3 Caso de análisis 3 | Carlos | 4 | 1460 | TA05 |

Receta de Derechos humanos (`montaje/lp_pieza.py`): voz → rejilla → cruce →
escenas → placas → `elegir` → `construir` → cartones → rótulos → blancos →
música → `montar` → `revisar`. Geometría: intro 182 · entrada 119 · ranuras ·
respiro 48 · cierre 119 · outro 182.

Cifras en pantalla en dígitos («10 millones de pesos»), en la voz en letras
(`guion_lp.BLOQUES`, campo tts).

## Placas

Seedream 5 Flash, 2k, 16:9, 35 créditos. Las cláusulas de la serie en su
versión corta (`base_lp.CORTO`, la que salió bien en las láminas). Hojas de
personaje en `hoja_id_lp.json` (con `piel_ref`); las placas aprobadas sirven de
referencia de lugar/estilo por su id de creación crudo
(`/home/claude/l1826/placa_id_lp.json` → `elegidas_lp.json → _magnific`).

Quién lleva cara: el fiscal que decide mal va de espaldas o en manos (U4 C1,
U4 C2); el indiciado se presume inocente: de espaldas (U4 C1, U4 C2); Carlos
Eduardo (U2 C2) es silueta y la agresión se cuenta con el DESPUÉS (la cocina
vacía, la silla caída). El acento mostaza es de María Elena (U2 C2) y de la
ciudadana (U4 C3).

Repetidas, y por qué:
- U4 C2 r02 (las partes): el conductor salió de perfil; se rehízo desde detrás
  de las sillas de visita (`_b`).
- U4 C2 r09 (la oposición): la voz dice «El defensor formula oposición» y la
  placa era una defensora. Rehecha con un defensor (`base_lp.defensor2`, otra
  cara que el de la U4 C1), con la placa vieja de lugar.
- U4 C3, inserto de la r04: dos tiradas, las dos con DOS anillos, uno a medio
  sacar (se lee como que ella se quita la argolla: lo contrario del caso).
  Fuera; la r04 queda sola. El primer planteamiento (un teléfono con un
  mensaje) insinuaba cómo llegó la disculpa y el expediente no lo dice.

## Cartones

`cartones/cartones_lp.py → ELEGIDOS`, verbatim, con el tiempo de Scribe.
Primera corrida: 76/69/74/85/75 % del cuerpo y tres fallas de lectura; quedó
en 65/53/74/67/67 % (ver el comentario de ELEGIDOS). Rótulos
(`lowerthirds_lp.LOWERS`): Jorge Eliécer Benavides en U2 C1 r05 y María Elena
Gutiérrez Ríos en U2 C2 r02 (por eso salió el cartón de «tres años… Medellín»).

## Movimiento

Kling 2.5 (`kling-25`, 720p, 5 s, 140 créditos) solo para acción real
(`prompts/kling_lp.json`): U2 C1 r01, r03, r05 · U2 C2 r07, r08 · U4 C1 r01 ·
U4 C2 r05, r08 · U4 C3 r02 y los insertos de U4 C3 (la firma, la carpeta):
11 clips, 1.540 créditos. El resto con la cámara de la casa; el inserto del
teléfono de U2 C2 r09 y el de las tapas de U2 C1 r05 con `detalle_lp quieto`.

Revisados cuadro a cuadro antes de conformar:
- U2 C1 r05: Kling sube las botellas hasta los ojos (se ve como binóculos)
  entre 1,7 y 3,0 s. El inserto de las tapas entra en el 70 (era 120) y lo
  tapa.
- U4 C2 r08: a los 3 s el fiscal baja la grabadora y sale de cuadro; se usa
  hasta 2,9 s (`hasta` en el manifiesto de `bajar_mov_lp`).
- U4 C3, la firma y la carpeta: hasta 2,6 s (después la mano flota o la
  carpeta pierde las hojas).

## Revisión propia (3 nov)

Las cinco líneas montadas en `DAE MASTER - CURSOS` (bins del árbol, `.drt` en
`10 TIMELINE SEBASTIAN`) y rendidas a `D:\DAE\_tmp\lp\revision` (NO es
entrega): cuadros = pieza, sin negros, −19,5 a −20,3 LUFS, pico −4,0 a
−4,5 dBFS.

- U2 C1: el rótulo del supervisor caía sobre el inserto de las tapas (dos
  manos): ahora entra en el 144 de la r05, 90 cuadros, sobre él.
- U4 C2 r09: defensor (ver Placas).

## Timelines en Resolve (3 nov)

Cada pieza del curso tiene su bin `10 TIMELINE SEBASTIAN` con una sola línea
y el `.drt` en la misma carpeta del disco:

- Videos: `LP UNIDAD 2 ESTUDIO REVERSO 1 …`, `LP UNIDAD 2 ESTUDIO REVERSO 2 …`,
  `LP UNIDAD 4 CASO DE ANALISIS 1/2/3` (las «(anterior)» en
  `_ARCHIVO versiones anteriores`).
- Láminas (Sebastián: «no creaste timeline para Sebastián para cada video»;
  las unidades de láminas no tenían ninguna): `LP UNIDAD 1 CASO DE ESTUDIO
  1…5` y `LP UNIDAD 3 CASO DE ESTUDIO 1…3`, una pista `LAMINA` con la lámina
  como clip de 240 cuadros (`LP_<K>_lamina_v240.mp4`, x264 crf 10: un still
  apendizado por API entra de 24 cuadros). La lámina, la ilustración y los
  exports también quedaron importados en sus bins (01 PLANOS, 02 LAMINA,
  05 EXPORTS).
