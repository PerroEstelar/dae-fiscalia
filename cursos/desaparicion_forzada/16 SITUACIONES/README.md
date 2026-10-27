# 16 situaciones · curso de Desaparición Forzada

Documento del Drive: «16 situaciones» (carpeta *PRIORIDAD 3 - Investigación
Judicial y Forense de la Desaparición Forzada*). Fuera del caso integrador,
dentro del mismo curso.

## Lo que trae el documento

Se llama «16 situaciones» pero trae **once**, de la A a la K. Cada una es un
**contexto** (el caso) y una **consigna para el participante** (preguntas,
opciones, retroalimentación, plantillas). La consigna **no va en ninguna
pieza**: la agencia la marcó en el propio documento, comentario por
comentario, con «No incluir esto en el video» (A–E) y «No incluir esto en la
IMAGEN» (F–K). Va a Moodle.

## Video o imagen

| | palabras | va en | título de trabajo | voz |
|---|---|---|---|---|
| A | 268 | video | La última llamada | Carlos |
| B | 243 | video | La nota sobre la cama | Pilar |
| C | 233 | video | El plazo de 24 horas | Carlos |
| D | 255 | video | La creciente de La Miel | Pilar |
| E | 272 | video | El camión hacia El Vergel | Carlos |
| F | 77 | imagen | El primer contacto | — |
| G | 86 | video (y su imagen) | La vocera | Pilar |
| H | 103 | imagen | Dos mujeres, dos impactos | — |
| I | 70 | imagen | La minuta | — |
| J | 57 | imagen | Las piezas del expediente | — |
| K | 56 | imagen | El informe integral | — |

Entre la E (272) y la H (103) no hay nada: son dos poblaciones. La marca de la
agencia y el largo del texto dicen lo mismo.

La **G** la marcó la agencia como imagen y pasó a video el 27 de octubre por
pedido de Sebastián: es la única de las imágenes con secuencia (la vocera, las
18:00, el teléfono, la Fiscalía). La forma de imagen se conserva en
`IMAGENES/SITUACION G`.

## Los seis videos, medidos

| | ranuras | pieza | duración | cartones | V2 mov. | V3 detalle | rótulo | línea en Resolve |
|---|---|---|---|---|---|---|---|---|
| A | 13 | 3366 | 2:20,4 | 7 | 3 | 3 | 1 | `SIT A LA ULTIMA LLAMADA v2` |
| B | 12 | 2880 | 2:00,1 | 6 | 2 | 3 | 1 | `SIT B LA NOTA SOBRE LA CAMA v2` |
| C | 11 | 3000 | 2:05,1 | 7 | 2 | 3 | 1 | `SIT C EL PLAZO DE 24 HORAS v2` |
| D | 12 | 3137 | 2:10,8 | 8 | 3 | 3 | 1 | `SIT D LA CRECIENTE DE LA MIEL` |
| E | 13 | 3151 | 2:11,4 | 6 | 3 | 3 | 1 | `SIT E EL CAMION HACIA EL VERGEL` |
| G | 5 | 1565 | 1:05,3 | 3 | 3 | 2 | 1 | `SIT G LA VOCERA` |

**Estado (27 oct, noche): las seis líneas completas en su bin de Resolve, SIN
exportar** (así lo pidió Sebastián: revisa en la línea y después se exporta).
Las A, B y C v1 siguen en Resolve y su v1 en `05 EXPORTS`, intactas. Cada
línea tiene su `.drt` en `10 TIMELINE SEBASTIAN`. La revisión interna se rindió
a `D:\DAE\_tmp\sit\revision\SIT_<X>_v<n>_REVISION_INTERNA.mp4` (no es
entrega) y sobre ese archivo se midió: cuadros = pieza, negros, loudness y una
hoja con un cuadro de cada ranura, de cada movimiento, de cada detalle y del
rótulo.

### Pistas

- **V1 VIDEO** intro · entrada · ranuras · respiro · cierre · outro.
- **V2 MOVIMIENTO** (`mov_sit.py`). Kling 3.0 desde la placa graduada (cuadro
  inicial, sin cuadro final), recortado al 88 % como la ranura, limpieza de
  bandas por cuadro, retime al largo, 12 cuadros de entrada contra la ranura
  horneada. **Sin fundido de salida** (nuevo): el clip cubre la ranura entera y
  sale en el corte; el fundido de salida hacía reaparecer como fantasma lo que
  cruzaba (la camioneta de A r03, el camión de C r05). Donde lo único que cambia
  es la luz, rampa sin modelo: `cielo` (A r05, E r07, G r03), `pantalla` (G r04,
  el teléfono se apaga) y `faros` (A r09: Kling movía a las tres personas, los
  faros que se van son luz).
- **V3 DETALLE** (`detalle_sit.py`). Placa Seedream con la madre graduada de
  referencia → limpieza de la madre + piel igualada → grade de la madre → Kling
  4 s desde esa placa con un solo gesto → conformado: cuadro 0 contra la placa,
  bandas, piel por el factor del cuadro 0, topes de piel (rosado ≤ 0,20; sin
  acento, banda cálida ≤ 0,22), **acento girado al tono de la madre** (A r10: la
  madre naranja, el detalle mostaza), retime. Dos crudos se cortan antes de que
  entre una segunda mano (B r05, G r03). Entra en `entra` de su ranura madre.
- **V4 CARTONES** los de siempre (verbatim, un tamaño).
- **V6 MARCA DE AGUA** al abrir y al cerrar el cuerpo.
- **V8 LOWER THIRD** (`lowerthirds_sit.py`): uno por pieza, en la r01 —la única
  ranura sin cartón en las seis—, nombre + edad + oficio tal como lo dice la voz.
  120 cuadros, entra a los 14.

### Correcciones de esta ronda que también tocan lo ya hecho

- **A r09 tenía un cian** que le ponía el grade de contraluz (frío p90 0,02 →
  0,07, se veía en la ropa clara). `construir` ahora repasa la limpieza de
  bandas DESPUÉS del grade cuando queda frío; A r09 se rehorneó. Medido en las
  70 placas: ninguna otra pasa de 1,5 % de píxeles fríos.
- **Láminas: el grade sube la saturación** (J: yemas 0,15 → 0,27, rosadas). El
  tope de rojos se pasa ahora sobre la graduada; las seis láminas se rehicieron
  (las anteriores en `_descartes`).
- **Apagón** a media construcción de D y E: `sit_pieza.py X construir=5,6,…`
  rehace solo las ranuras que faltaban; la ranura cortada quedó en
  `_descartes` con el motivo.

### Para que Sebastián mire

- Voces de A–E y G sin escuchar por mí (siglas deletreadas).
- A r10: Rosa Elena camina alejándose del edificio. C r02 sedán / r03 cabina de
  camioneta: continuidad del vehículo de Fernando.
- B: la piel de Julián es más cálida que la del resto (decisión DF de no
  pasarle piel); B r05 tiene 2,6 % de píxeles rosados.
- G: Mariana se ve menor de 16 en algunas placas.
- E r01 detalle: la vaca del detalle es gris medio, la de la madre blanca.
- Los rótulos de la r01 de B, C, D y E pasan por encima del corte al detalle
  (la r01 es la única ranura limpia y el detalle de oficio vive ahí).

## Dónde está cada cosa

```
UNIDAD DESAPARICION FORZADA/16 SITUACIONES/
  00 FUENTE/        el documento exportado del Drive
  _PERSONAJES/      15 hojas de personaje (corregidas) + _crudos + ids
  VIDEOS/SITUACION A..E/   las diez carpetas del caso integrador
  IMAGENES/SITUACION F..K/ 01 PLANOS · 02 LAMINA · 05 EXPORTS · 06 GUION Y PROMPTS
```

El mismo árbol existe como bins en `DAE MASTER - CURSOS`, bajo
PRIORIDAD 03 › CURSO … › UNIDAD DESAPARICION FORZADA › 16 SITUACIONES.

## Herramientas

| | |
|---|---|
| `herramientas/voz/textos/guion_sit.py` | guion verbatim + tts, por bloque; textos de las láminas |
| `herramientas/voz/textos/rutas_sit.py` | el árbol |
| `herramientas/voz/lanzar_voz_sit.py` | pide las voces (Carlos / Pilar) |
| `herramientas/voz/armar_sit.py` | máster −19 LUFS, rejilla y ranuras |
| `herramientas/prompts/base_sit.py` | reparto nuevo sobre `base_df_v1` |
| `herramientas/prompts/escenas_sit_[a-e].py` | una placa por ranura + DET + BROLL + MOV |
| `herramientas/prompts/imagenes_sit.py` | dos angulaciones por imagen |
| `herramientas/prompts/personajes_sit.py` | hojas de personaje |
| `herramientas/prompts/prompts_sit.py` | arma todo y escribe el storyboard .md de cada situación |
| `herramientas/cartones/cartones_sit.py` | cartones escogidos a mano, tiempos y verbatim por máquina |
| `herramientas/cartones/lamina_sit.py` | la lámina de las imágenes |
| `herramientas/prompts/bajar_placas_sit.py` | baja las candidatas y arma la hoja de contacto |
| `herramientas/prompts/elegidas_sit.json` | qué candidata va en cada ranura |
| `herramientas/montaje/sit_pieza.py` | elegir · construir[=n,…] · blancos · musica · montar · revisar · exportar · entregas · verificar (`v=2` antes de los pasos) |
| `herramientas/montaje/detalle_sit.py` | placas · conformar de los insertos V3 |
| `herramientas/montaje/mov_sit.py` | kling · luz de la pista V2 |
| `herramientas/montaje/cadena.py` | corre pasos en orden, cada uno a su log |
| `herramientas/cartones/lowerthirds_sit.py` | los seis rótulos |
| `herramientas/cartones/imagen_sit.py` | candidata → limpieza → grade → tope de rojos → lámina → 05 EXPORTS |
| `herramientas/prompts/imagenes_sit_creativas.py` | las ideas de las láminas (doble exposición, cenital, espalda con espalda…) |
| `herramientas/prompts/subir_sit.py` · `bajar_crudos_sit.py` | subir placas a Magnific · bajar crudos de Kling |

## Las cinco imágenes (y la G en imagen)

En `IMAGENES/SITUACION X/05 EXPORTS`: `SIT_X_lamina.png/.jpg` (ilustración +
contexto verbatim) y `SIT_X_ilustracion.png` sola. Ideas: F doble exposición
(el camino dentro de la silueta de Rosa Elena), G cenital de la cuadrícula de
exhumación, H Rosa Elena y Mariana espalda con espalda, I la minuta escrita
frente a las manos de la madre (el funcionario sin rostro), J los ocho
documentos en orden sobre la mesa, K cuatro manos que juntan las carpetas en
cruz.

## Lo que falta

- La revisión de Sebastián de las seis líneas y las seis láminas.
- Con su OK: exportar (`sit_pieza.py X v=2 exportar entregas verificar`) y subir.
