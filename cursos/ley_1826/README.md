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

## Pase previo a la revisión de Sebastián (3 nov, noche) — v2 de las cinco líneas

Antes de que revisara los videos, se midió qué ajusta él a mano en las líneas
que aprueba y qué pide cambiar después de revisar (docs del proyecto de las
rondas de P3, C5, TA, DF/16 situaciones, GJ, JR y DH), y se aplicó lo que ese
historial dice sin esperar la ronda. Líneas nuevas `… v2` (la v1 en
`_ARCHIVO versiones anteriores`), `.drt` v2 en `10 TIMELINE SEBASTIAN`,
revisión interna en `D:\DAE\_tmp\lp\revision\LP_<K>_v2_REVISION_INTERNA.mp4`.

Lo que él deja a mano, medido (16 líneas aprobadas):

| ajuste suyo | líneas | qué se hizo aquí |
|---|---|---|
| fundido a negro al final del respiro, antes del cartón de cierre (SIT B/C/D/E/G, DH U2) o desde negro en un cambio de escena (DH U1/U5, GJ T4) | 9 | `lp_pieza.respiro`: los últimos 16 cuadros del respiro funden a negro, horneado (luma ~95 → 21) |
| recortar la cama para que no pise intro/outro («always») | 5 + regla en la biblia | ya venía: `abre` 159 / `cierra` = primer cuadro del outro |
| quitar el respiro o recortar el último cartón (SIT A/B, DH U3/U5) | 4 | `cartones_lp.calcula`: el último cartón termina con el cuerpo, el respiro queda limpio (antes se estiraba sobre él, como en las situaciones) |
| apagar/mover capas de movimiento o detalle, partir clips | 7 | las capas siguen en V2/V3, apagables; los 4 Kling nuevos revisados cuadro a cuadro |

Lo que pide después de revisar (~95 pedidos en 13 rondas), y lo que se hizo:

| categoría | pedidos | aquí |
|---|---|---|
| la placa no muestra lo que la voz dice / falta quien se nombra / rasgo equivocado | ~22 | las 41 ranuras cruzadas con la frase que se oye encima (`cruce_lp.json`): sin faltas; U4 C2 r09 y U4 C3 r04 ya se habían corregido |
| cartones: faltan, primera mitad «vacía», redacción, dígitos | ~14 | U2 C1: 27 s sin cartón entre el 1224 y el 1868 → vuelve «debido a una caída atípica…» (a04); U2 C2: vuelve «Durante los últimos tres años…» cortado donde empieza la ranura del rótulo (303-470). Rótulo y cartón siguen sin convivir: ahora el cartón se corta, no se descarta |
| cuadros vacíos / falta gente a media acción / insertos de detalle | ~12 | insertos nuevos: U4 C1 r05 la solicitud en la mano (84 cuadros, entra 70), U4 C2 r07 las tres firmas (84, entra 110; la ranura más larga, 299, cenital sin gente) |
| defectos de movimiento (manos, cámara que empuja, figura que sale) | ~12 | los 11 clips existentes revisados en tira de 8 cuadros: ninguno con defecto |
| más animación / boca en los planos de habla | ~6 | 4 Kling más (560 cr): U4 C1 r06 el defensor habla y baja la hoja; U2 C2 r11 la fiscal habla ante el juez; U2 C1 r08 el vigilante habla y el investigador escribe; U4 C2 r09 el defensor se levanta y objeta. 15 clips en 41 ranuras |
| placas repetidas / monotonía | ~9 | U4 C1 r01 y r03 son el mismo escritorio (OTS y cerrado): se dejan, son dos momentos |
| color / piel / estilo | ~10 | sin cambios; piel 0 % rosado en las placas graduadas |
| audio / voz | ~8 | huecos entre bloques 1,0-1,6 s (narrador solo): se dejan |
| rótulos | ~4 | sin cambios |

Créditos: 2.701 → 2.071 (2 placas de detalle 70 + 4 Kling 560). Quedan por
encima de los 2.000 de reserva.

Para mirar en su revisión: el inserto de las firmas (U4 C2) trae el moteado
del papel blanco que deja el grade; el defensor de U4 C2 r09 se levanta y
queda de perfil señalando con el índice (todo el clip es la ranura, 122
cuadros); la mano del inserto de U4 C1 salió gris neutro (la madre, gris
cálido 0,098).

## Revisión de Sebastián · U2 C1 (3 nov, noche) — sobre SU línea v2, sin remontar

Pedido: «r01 el supervisor se ve raro, encuadrado tan a la derecha que no
parece intencional; a los 23 s la narración parte el nombre (Mario Alberto…
Gómez Parra) y debe leerse como uno; el vigilante de r08 se parece demasiado
al supervisor; mientras el presupuesto esté apretado, solo stills con cámara
horneada; conservar los cortes que él hizo».

- **r01**: placa nueva (candidata c, 2 tiradas, 70 cr): el supervisor es el
  sujeto, en el tercio izquierdo, del muslo para arriba, mirando calle abajo
  hacia los vehículos; la vieja (ancla de lugar) como referencia. Cámara de
  la casa; su clip de Kling (el paso desde la esquina) fuera de la línea y a
  `MOVIMIENTO/_descartes`. El respiro sale de la r01 nueva.
- **r08**: `base_lp.vigilante` es otro hombre (28 años, flaco, afeitado,
  pelo al ras, camisa azul grisácea) y la placa se pidió con la r08 vieja de
  referencia (mismo cuarto, mismo encuadre, solo cambia él). Candidata b
  (2 tiradas, 70 cr). Su clip de Kling también fuera.
- **La voz** (medido en el STT: 0,50 s de silencio entre «Alberto» y
  «Gómez», 0,32 entre «Eliécer» y «Benavides»): cirugía sobre el master, sin
  volver a pedir la voz. Se quitan 0,32 s y 0,15 s de esos huecos (quedan
  ~0,10) y se devuelven como silencio después de «Parra,» (+0,22) y al final
  del bloque a01 (+0,25): mismo número de muestras, la rejilla no se mueve,
  «contratista» sigue cayendo en el corte a la r02. `LP_U2C1_NARRADOR_v2.wav`
  releído con `ReplaceClip`; el STT del bloque remapeado. El cartón p02 ya
  traía «Mario Alberto Gómez Parra» en un solo renglón (el que se parte es
  «Pedro Antonio Morales / Rincón»: cabe en 3 renglones solo partiéndolo).
- Todo en su línea con `cirugia_lp U2C1 v=2 relink/quitar` y
  `reemplazar_en_sitio_lp`: retrato idéntico salvo los dos ítems de V2 que
  salen. `.drt` reexportado (el anterior en `_descartes`). Créditos: 1.511 →
  1.371.

## Revisión de Sebastián · U4 C2 r09 (3 nov, noche) — y una regla nueva de la biblia

Pedido: «no hagas tan tembloroso el arranque de los clips, se ve siniestro,
como si el video fallara; no revises los clips pasados pero pon la regla en la
biblia: las transiciones entre clips no pueden tener ese movimiento de cámara
fantasmal, arrastrado, a saltos; y este clip de la r09 se ve de otro estilo
que el resto porque es demasiado realista: cámbialo por un still del mismo
hombre en nuestro estilo gráfico, gesticulando. El caso de análisis 1 está
bien por ahora. No exportes nada hasta que yo lo diga».

- **La causa del arranque tembloroso** no era Kling sino el conformado:
  `mov_lp.kling` fundía el clip 12 cuadros (`MEZCLA`) contra la ranura
  horneada de V1, y esa ranura se mueve (zoom + pulso de `camara.py`)
  mientras el clip no. Dos imágenes desfasadas durante medio segundo. Desde
  ahora `MEZCLA = 0` en `mov_lp` y `mov_ed`: el clip se escribe tal cual y
  entra en corte seco (cubre la ranura entera desde el cuadro 0; el corte
  anterior ya es un corte). Lo ya conformado no se rehace, como pidió. La
  regla está en la biblia (§8) y en `CLAUDE.md`.
- **r09**: su clip (`LP_U4C2_r09_la_oposicion_mov_v122.mp4`) fuera de SU
  línea v2 con `cirugia_lp U4C2 v=2 quitar V2 …` (retrato idéntico salvo ese
  ítem) y a `MOVIMIENTO/_descartes/…__demasiado_realista_*.mp4`. Queda la
  placa horneada que ya estaba debajo: el defensor de pie, la mano abierta,
  gesticulando, con la cámara de la casa. Sin gastar créditos (siguen en
  1.371). `9` fuera de `MOV` en `escenas_lp_u4c2.py`; `retirado` en
  `kling_lp.json`. `.drt` reexportado (el anterior en `_descartes`).
- U4 C1 queda como está. Nada exportado.

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
