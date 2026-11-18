# Bienes en el proceso penal (Curso 5): inicio y cierre del curso

Pedido de Sebastián del 14 nov 2026. Son dos videos de profe a cámara, con todo
el procedimiento:
- intro y outro;
- cartones de entrada y salida con el nombre del curso;
- lower thirds con el nombre y el recorrido del profe;
- cartones de apoyo y gráficos de AE;
- audio revisado, nada recortado, y todo en sus carpetas, en el disco y en la nube.

El profe es **Sergio Andrés López Zamora**, autor del curso. Es la primera vez que
se hacen videos suyos en este formato.

| clave | fuente (Drive, `VIDEOS UNIDADES`) | dura | plan |
|---|---|---|---|
| bi | `bienes_iniciocurso.mp4` | 6:21 | `introduccion_curso/plan_bi.py` |
| bc | `bienes_cierre_curso.mp4` | 43:18 (43:12 con el corte) | `cierre_curso/plan_bc.py` |

Las dos fuentes son grabaciones de Teams de 1280×720 a 30 fps, con el fondo virtual
del edificio y el panel DAE/Fiscalía.

## Disco y Resolve

- **Disco:** `E:\DAE MASTER\CURSO 5 - Bienes en el proceso penal\`, en
  `INTRODUCCION AL CURSO\` y `CIERRE DEL CURSO\`. Cada uno tiene:
  - `01 VIDEO`: la fuente y el compuesto;
  - `02 CARTONES`: el título, los cartones y los lower thirds;
  - `05 EXPORTS`: la entrega y `_master`;
  - `09 MOTION GRAPHICS`;
  - `10 TIMELINE SEBASTIAN`: el `.drt`.
- **AE:** `00 MOTION GRAPHICS\BIENES_intros_mg.aep`, con las comps `BI2_*` (inicio)
  y `BC_*` (cierre), y su carpeta `iconos`. Las `BI_*` son de la ventana descartada.
- **Resolve:** bins `C5 BIENES EN EL PROCESO PENAL / INTRODUCCION AL CURSO` y
  `… / CIERRE DEL CURSO`.
  - Líneas: `BIENES - CURSO - INTRODUCCION` y `BIENES - CURSO - CIERRE`.
  - La línea «… INTRODUCCION (ventana 1143, descartada)» es la primera versión.
- **Másteres y descartes pesados:** `D:\DAE\_masters_archivo\CURSO 5 - Bienes en
  el proceso penal\`. En E: quedan los `LEER` que dicen dónde están.

## Herramientas

Son las de las introducciones de curso (`ic_pieza`, `ic_linea`, `ic_revision`), con
`DAE_PLAN=plan_bi` o `plan_bc`, más `mp4_entrega`. Hubo que agregarles cuatro
cosas.

1. **Otro curso.** El cartón de título se rehace con `titulo_srpa.rendir_fijo` y
   `CURSO_LINEAS`. El proyecto de AE y los íconos van por plan (`AEP`, `ICONOS`).
2. **Cortes con su propia ventana.** `TRAMOS` en el plan y `ic_pieza.tramos_vf`.
   - En el cierre hay un arranque en falso en 41:33: se quitan 6,3 s.
   - El comienzo de la frase repetida va en plano cerrado (1024×576 desde
     (96, 40)) durante 4,7 s. Termina antes de que el profe baje la cabeza.
   - `cuadro` pasa los tiempos de la fuente a la línea, descontando el corte.
   - `ic_pieza.py reimagen` rehace solo la imagen cuando cambia una ventana.
3. **Columna angosta y lower third chico** (`MAXW`, `LT` en el plan,
   `ic_pieza.ajustes`). Hizo falta en la introducción: ver abajo.
4. **Renglones equilibrados** (`herramientas/cartones/balanceo.py`). Los cartones
   no dejan una palabra sola abajo.
5. **Líneas largas** (`ic_linea_externa.py`). `run_inline` corta a los 58 s; la
   línea del cierre tiene 122 clips.

Además:
- `icono_vehiculo.py` dibuja el ícono del vehículo en el estilo de los de SRPA.
- `mp4_entrega.py` acepta un cuarto argumento para mandar el máster a otra
  carpeta. El del cierre (~10 GB) va a `D:\DAE\_masters_archivo\…`.

## Encuadre

Se midió con `perfil.py`:
- se toma un cuadro cada 2,5 s y el fondo es la mediana;
- por fila se busca el borde izquierdo de la persona, y se leen p2, p10 y p50.

- **Cierre:** el profe está a la derecha. La ventana estándar 1143×643 desde
  (0, 40) deja la cabeza desde x≈805 (p2), los hombros bajo la caja y el panel
  entero.
  - El lower third lleva el nombre a 44 px y el cargo a 560 de ancho. Con el
    estándar, «Penal» le tocaba el mentón cuando se inclina a la izquierda.
- **Introducción:** el profe está centrado, cerca de la cámara, y a ratos se
  inclina hacia ella. Se probaron tres ventanas.
  1. 960×540 (×2): dejaba libre la caja, pero cortaba la cara por la boca.
  2. 1143×643 desde (0, 40) (×1,68), la estándar: termina en y=683 de la fuente.
     Se entregó una v1 así. En la hoja de revisión el mentón se salía del cuadro
     cuando se inclina (5:59). Quedó en `_descartes`.
  3. **1198×674 desde (0, 46) (×1,60)**, la que quedó: llega al borde inferior
     de la fuente, así que el mentón entra siempre. El panel entra entero.
  - La cara empieza en x≈630–700 de salida. Por eso la columna de texto se
    angosta a 470 px (hasta x≈640).
  - El lower third lleva el nombre a 40 px y el cargo a 520 de ancho, para que
    «Zamora» no pise la mandíbula. Se simuló sobre nueve cuadros antes de rendir.
  - Los archivos de esta composición llevan el prefijo `BI2_`.

## Textos

Salen de la transcripción de Scribe (WAV a 16 kHz, una voz), sin muletillas.
- Se corrigieron los errores de transcripción: votar → adoptar, editarse →
  evitarse, FEAD/FEAP → FEAB, dirigencia → diligencia, bona fe → buena fe.
- En 23:03 dice «adquirido ilícitamente, pero utilizado como instrumento». Es
  «lícitamente», por el contraste con la causal de origen.
- Las listas se midieron antes de armar (cima ≥ 250), con las mismas fuentes y
  el mismo `maquetar`.
- La cobertura de gráficos es de ~70 % en la introducción y ~62 % en el cierre.
- La última fila de cada lista queda al menos 4 s en pantalla.

## Revisión

Cada entrega se revisó con la hoja de `ic_revision` (un cuadro por gráfico, más
intro, título, cierre y outro) y con cuadros a tamaño completo de los lower
thirds, las listas, los cartones más altos y el corte.

Lo que la revisión encontró y se rehízo antes de entregar:

| qué se vio | dónde | qué se hizo |
|---|---|---|
| el mentón se salía del cuadro al inclinarse | inicio, 5:59 | ventana hasta el borde inferior de la fuente |
| primer renglón de dos palabras | inicio y cierre | `balanceo` con mínimos cuadrados; 18 cartones del cierre rendidos de nuevo |
| la última fila de una lista duraba 2 s | 3 listas del inicio, 5 del cierre | listas más largas |
| el mentón se salía del plano cerrado | cierre, 41:42 | plano cerrado más corto |
| «Penal» tocaba el mentón | cierre, primer lower third | cargo en tres renglones |

Las versiones descartadas no se borraron: están en `_descartes`, en cada
carpeta o en `D:\DAE\_masters_archivo`.

## Entrega (14 nov 2026)

MP4 con la receta de `Entrega_MP4_Fiscalia_Receta.md` (`mp4_entrega.py`): máster
H.264 NVIDIA a 32 Mb/s y entrega x264 CRF 18, High L4.0, Rec.709, AAC 48 kHz
estéreo con el audio copiado del máster.

| | inicio | cierre |
|---|---|---|
| archivo (`05 EXPORTS`) | `bienes - CURSO - INTRODUCCION-v1.mp4` | `bienes - CURSO - CIERRE-v1.mp4` |
| largo | 6:55 (9.957 cuadros = línea) | 43:46 (62.951 cuadros = línea) |
| peso | 255 MB | 1.517 MB |
| sonoridad / pico | −16,1 LUFS / −2,4 dBTP | −16,0 LUFS / −3,0 dBTP |
| PSNR contra el máster (medio / mínimo) | 49,4 / 43,8 dB | 49,8 / 44,1 dB |
| gráficos | 2 lower thirds, 11 cartones, 8 listas | 2 lower thirds, 83 cartones, 27 listas, 5 tarjetas |
| máster | `D:\DAE\_masters_archivo\…\INTRODUCCION AL CURSO` (1,4 GB; movido desde E: el 16 nov, con un `LEER` en `05 EXPORTS\_master`) | `D:\DAE\_masters_archivo\…\CIERRE DEL CURSO` (7,6 GB) |

- **Estructura de las dos:** intro (194 cuadros), cartón de título «Bienes en el
  proceso penal / Introducción al curso» o «… / Cierre del curso» (215), el
  clip, el mismo cartón de cierre y el outro (194).
- **Audio:** el de los profes, v2: ecualizado, comprimido y a −16 LUFS con techo
  en −3 dBTP. Las fuentes venían a −26,6 y −27,1 LUFS.
- **Drive:** carpeta `VIDEOS` del curso (`12Wwl_Vq9CCJVTPN7Y7g7JH0j3b9cDiAT`), en
  dos carpetas nuevas:
  - `Inicio del curso` (`1dyVsM9n4SkDRWIwzj4YGvsjNly4OW2qw`);
  - `Cierre del curso` (`13q_woiBdN6fQlOvThAGXzUtvGJ8YxTey`).
  - Subieron por `G:\My Drive\_MA subidas` y se movieron con `update_file`. Las
    copias de las fuentes que quedaban ahí se mandaron a la papelera.
- **Línea para Sebastián:** `10 TIMELINE SEBASTIAN\BIENES - CURSO - INTRODUCCION.drt`
  y `… - CIERRE.drt`, con V1 video, V2 cartones, V3 motion graphics (alfa
  premultiplicado) y V4 lower third.

## Unidades 1 a 4: inicio y cierre (17 nov 2026, entrega provisional)

Pedido de Sebastián del 17 nov: los ocho videos de unidad de la carpeta `VIDEOS UNIDADES` de Drive
(`1s9P1jkAOz0CBJs_gfUdVWGdplWxfc2H_`), «con el estilo provisional de gráfica»: intro, cartón de
título, lower third, cartón de cierre y outro; el cuerpo, sin gráficos. Todo está en
`unidades/` (`base_bi_unidades.py`, que explica las decisiones, y `plan_biu1i.py` … `plan_biu4c.py`).

- **Las fuentes traen una intro y un outro pegados** (cuadros 0–277 y los últimos 278; el cierre de
  la U4 no trae outro). Se sacan: cada plan toma solo el tramo del profe.
- 1920×1080, 30 fps, **BT.601**. Ventana: el cuadro entero.
- **Lower third en columna angosta** (nombre en dos renglones, `LT = (44, 345)`, `LT_TOP = 740`): el
  profe ocupa el centro de abajo y con las medidas del curso el nombre le cruzaba la cara.
- Unidad 4: el cartón dice «…extinción del derecho **de** dominio» (el documento de diseño dice
  «del dominio»; avisado a Sebastián).
- Árbol en `D:\DAE MASTER\CURSO 5 - Bienes en el proceso penal\UNIDAD n\INICIO|CIERRE` (E: no tiene
  espacio); bins `C5 BIENES EN EL PROCESO PENAL / UNIDAD n - INICIO|CIERRE - PROFE`; líneas
  `BIENES - Un - INICIO|CIERRE`.

| entrega | dura | cuadros | codificación | Drive (VIDEOS › «Unidad n») |
|---|---|---|---|---|
| `bienes - U1 - INICIO-v1.mp4` | 7:18 | 10.500 | x264 CRF 18 `medium` | `1Bty6BeHEuvTknRSG0ONuvIR5D1ff8w8v` |
| `bienes - U1 - CIERRE-v1.mp4` | 26:44 | 38.452 | NVIDIA por Resolve, 5 Mb/s | `19g0PdRImQYkmIoUWE_mNLghFLJkeefSD` |
| `bienes - U2 - INICIO-v1.mp4` | 7:48 | 11.227 | x264 CRF 18 `medium` | `11HNJc7D_Z4yV3K1Br_rZM9VE992Ft74s` |
| `bienes - U2 - CIERRE-v1.mp4` | 23:11 | 33.344 | NVIDIA por Resolve, 5 Mb/s | `1Y8ddCUJ0baMJouuNAWi-9nExoaukMdhC` |
| `bienes - U3 - INICIO-v1.mp4` | 6:00 | 8.630 | x264 CRF 18 `medium` | `1k_F5fUCLQ1BG0KmceRm8gP_gxL28NjmS` |
| `bienes - U3 - CIERRE-v1.mp4` | 20:14 | 29.112 | NVIDIA por Resolve, 5 Mb/s | `1IcoyHxfDiODsPRk3gpfR1df3crSboUhS` |
| `bienes - U4 - INICIO-v1.mp4` | 5:39 | 8.133 | x264 CRF 18 `medium` | `1iJCb829twfhq3gcayJ0dktnn2VJ_9_-1` |
| `bienes - U4 - CIERRE-v1.mp4` | 23:50 | 34.294 | NVIDIA por Resolve, 5 Mb/s | `1QkTDnBeKrzIc2TODrkvfnRuxn03gJj_O` |

Las ocho se compararon byte a byte con la copia de servidor de Drive. Sonido: −16,0 a −16,1 LUFS,
picos de −2,0 a −3,0 dBTP.

**Los cierres salieron por la vía urgente** (`unidades/lote/urgente.py`): a las 21:20 Sebastián pidió
tener todo antes de las 22:00 y con x264 el último cierre salía a las 23:15. Se rindieron directo de
Resolve con H.264 NVIDIA; el último quedó en Drive a las 21:45. Si se piden con la receta, salen de
los másters de 32 Mb/s (`D:\DAE\_masters_archivo\CURSO 5 - Bienes en el proceso penal\UNIDAD n\CIERRE`)
como `-v2`.

`unidades/lote/` guarda los guiones del lote tal como corrieron en `D:\DAE\_tmp\bi_u\`: `lote_cadena.py`
(compuestos, tres a la vez, con cola), `lote_entrega.py` (línea, máster y entrega), `prioridad.py`,
`verif_biu.py`, `sim_todos.py` (el lower third sobre dos cuadros de cada fuente) y `urgente.py`.

**Para la versión con gráficos** hay que decidir antes dónde va la columna de cartones: el profe está
chico, abajo al centro, y no hay recorte que lo acerque dejando entero el panel DAE/Fiscalía.
