# Terminaciones anticipadas · videos de profe a cámara

Pedido de Sebastián (17 nov 2026), después del inventario de SRPA, Ley 1826 y Terminaciones
anticipadas: «empieza con lo que falta del material que tenemos pero no se lo hemos producido,
cada uno excelentemente hecho siguiendo todos los protocolos, de pe a pa, los dejas subidos y
actualizas el inventario». De este curso había dos grabaciones sin producir: el inicio y el
cierre del curso.

El formato es el de los profes de Derechos humanos, Enfoque diferencial y Bienes: intro FGN,
cartón de título con el nombre del curso y el de la pieza, el profe con cartones de caja, listas
de AE y lower third, cartón de cierre y outro. Base común: `base_ta_profe.py`.

## Profe

**Juan David Peña Gómez.** Lo dice en el inicio: «elaborado por Víctor Hugo Ospina Vargas y
quien les habla, Juan David Peña Gómez». El documento de introducción del curso lo presenta como
investigador académico de la Universidad Nacional de Colombia. Lower third: «Coautor del curso.
Investigador académico de la Universidad Nacional de Colombia».

## Fuentes

Drive del curso → `VIDEOS` (de JP, 14 nov). Grabaciones de Teams: 1280×720, H.264 Constrained
Baseline, 30 fps parejos, BT.601, AAC estéreo a 44,1 kHz, con el fondo virtual del edificio y el
panel DAE/Fiscalía.

| archivo en Drive | id | qué es | copia de trabajo (`01 VIDEO`) |
|---|---|---|---|
| `terminaciones_anticipadas_inicio_curso.mp4` | `1YmOIgt9Qo49ayMXJm804QYeZWTUWjRDn` | inicio del curso, 8:03,9 (14.517 cuadros) | `ta_inicio_curso_fuente.mp4` |
| `terminaciones_anticipadas_cierre_curso.mp4` | `1AA096BLK_v7yd9aE3qISuidZvfX5M0nh` | cierre del curso, 7:52,3 (14.168 cuadros) | `ta_cierre_curso_fuente.mp4` |

Las dos están leídas al guion y de corrido: sin tomas repetidas ni pausas de más de 2 s. Van
enteras. En el cierre se traba una vez (358,5 s: «analizar qué, qué elementos deben te-- ser
tenidos en cuenta»): se deja, y encima va la lista de lo que piden las actividades.

Transcripción: Scribe sobre WAV mono a 16 kHz (1.128 y 1.086 palabras). Los JSON y los WAV
están en `D:\DAE\_tmp\sr_ta\` (`tai.*`, `tac.*`).

El inicio y el cierre de las unidades 1 a 4 llegaron el 17 nov: ver «Unidades 1 a 4» al final.

## Ventana y columna

1067×600 desde (0, 20), ×1,8. El profe está muy cerca de la cámara y corrido a la derecha.
- Medido con una muestra cada 2 s (fondo = mediana): el borde izquierdo de la cabeza va de x 389
  (p5) a 472 (p50) de la fuente en el inicio, y de 333 (p5) a 504 (p50) en el cierre.
- La columna de cartones y listas es de 470 (`MAXW`): la caja termina en x=640. El lower third
  lleva el nombre a 40 px y el cargo a 440 de ancho.
- `D:\DAE\_tmp\sr_ta\zona.py` mide, a 2 muestras por segundo, cuánto de la caja de cartones
  (x 86–660, y 250–690 de salida) ocupa la persona. En los dos videos, nunca más del 1,5 %.
- Con la columna en 470 las listas van sin título y con cuatro filas como mucho, de dos
  renglones (unos 34 caracteres). En las enumeraciones de cinco, dos términos van en una fila o
  queda fuera uno; las cinco respuestas del final del cierre van en dos listas seguidas.

Simulación (`profe_sim.py`): `D:\DAE\_tmp\sr_ta\tai\sim\` y `…\tac\sim\`.

## Dónde

E: no tiene espacio (6 GB libres). El árbol va en
`D:\DAE MASTER\CURSO 4 - Curso Terminaciones Anticipadas\`:
- `INICIO DEL CURSO\` y `CIERRE DEL CURSO\`, con las subcarpetas de la serie;
- `00 MOTION GRAPHICS\TA_profe_mg.aep` (copia de `SRPA_mg.aep`) y sus `iconos`.

En la carpeta del curso de E: queda un `LEER`. Los másters de 32 Mb/s están en
`D:\DAE\_masters_archivo\CURSO 4 - Curso Terminaciones Anticipadas\`. Bins de Resolve:
`CURSO 4 - TERMINACIONES ANTICIPADAS` › `INICIO DEL CURSO - PROFE` y `CIERRE DEL CURSO - PROFE`.

## Entregas

Drive: curso → `CONTENIDOS › CASOS › VIDEOS FINALIZADOS`
(`1H2oIsmE55wwaNYyynoZrmhJK9WXN4k_V`), en dos carpetas nuevas con los nombres que usa SRPA.

| pieza | plan | línea | entrega | carpeta de Drive | id |
|---|---|---|---|---|---|
| Inicio del curso | `plan_tai` | `TA - CURSO - INICIO` | `terminacionesanticipadas - CURSO - INICIO-v1.mp4` | «presentación del curso» (`1dqizTlzjp-e6SG-Rk3Fh2PWo6Er7LUrc`) | `1siDui1Y0dgTTmrSjBwUz3S5vFQ81PkhY` |
| Cierre del curso | `plan_tac` | `TA - CURSO - CIERRE` | `terminacionesanticipadas - CURSO - CIERRE-v1.mp4` | «cierre del curso» (`1wh6BBlNa6E5SvGW7rru6Hjro4ibWgLAD`) | `19cQoztfV4fbPVjKYZQOuqZsqaERcdl4K` |

| entrega | cuadros | sonido | pico | PSNR medio / mínimo | peso |
|---|---|---|---|---|---|
| inicio | 12.419 = línea | −16,1 LUFS | −2,9 dBTP | 50,7 / 45,0 dB | 245 MB |
| cierre | 12.141 = línea | −16,1 LUFS | −3,0 dBTP | 50,7 / 45,2 dB | 242 MB |

Las dos se subieron con copia exclusiva (`profe_subida.py`) y se verificaron byte a byte contra
una copia de servidor (`verificar_drive.py`).

## Cómo se hizo (cadena genérica de profe)

Desde estas piezas la cadena no depende del curso (`herramientas/montaje/`):

    python profe_cadena.py plan_tai [componer titulo cartones mg]
    python profe_sim.py plan_tai [nombre=a-b] [nombre@t]
    python profe_entrega.py <log de la cadena | -> plan_tai
    python ..\entrega\profe_subida.py plan_tai

Los logs van a `<P.TMP>` (`D:\DAE\_tmp\sr_ta\tai\`): `cadena.log`, `sim\sim.log`, `entrega.log`,
`subida.log`.

## Unidades 1 a 4: inicio y cierre (17 nov 2026, entrega provisional)

Sebastián: «vamos a dejarlos por favor con versión provisional, queriendo decir: solo hagamos
intro y outro, placas de entrada y salida y títulos del profe por ahora, para que salgan más
rápido». Ocho videos con intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo
va sin gráficos.

**Fuentes.** Drive del curso → `VIDEOS` › «VIDEOS UNIDADES» (`1Cg7mvB8pLSoFVS43ao_kNxgTjL8tf7kE`,
de JP, 17 nov). Copia de trabajo en `UNIDAD n\<INICIO|CIERRE>\01 VIDEO\ta_u<n>_<pieza>_fuente.mp4`.
- Son otra grabación que las del curso: **1920×1080**, H.264 Constrained Baseline, 30 fps
  parejos, AAC estéreo a 48 kHz (−17,5 a −18,0 LUFS), sin etiquetas de color.
- **BT.709**, medido con los colores del panel DAE/Fiscalía contra el compuesto del inicio del
  curso (ver `base_ta_profe`).
- Una sola toma cada una, leída de corrido: sin cortes ni pausas de más de 2,6 s. Entran de medio
  segundo antes de la primera palabra a 0,8 s después de la última. Los tropiezos sueltos se
  dejan («funcio-, fu--» al final del cierre de la U1, «nes--» al final del inicio de la U4).
- Transcripción (Scribe, WAV a 16 kHz): JSON y WAV en `D:\DAE\_tmp\ta_u\stt\`.

**Nombres de las unidades** (cartón de título): del formato de diseño del curso (FGN-AP01-F-204,
«07_09_2026 Definitivo DISEÑO CURSO_TERMINACIONES ANTICIPADAS», `1g8GxE5ZjdCM1xAXowHrxgBPJkC-tIs66`):
1. Archivo de la indagación; 2. La preclusión en el proceso penal; 3. Aplicación del principio de
oportunidad; 4. Preacuerdos y negociaciones en el sistema penal.

**Ventana: el cuadro entero.** El profe está muy cerca de la cámara (el borde izquierdo de la
cabeza, entre x 376 y 524 de 1920; el tope, entre y 40 y 92) y tapa parte del logo de la Fiscalía
del panel: está así en la fuente. El lower third va con las medidas del curso y queda sobre la
plaza y el hombro; se miró en un cuadro antes de rendir (`D:\DAE\_tmp\ta_u\sim_lt_u1i.jpg`).
**Para la versión con gráficos hay que decidir antes dónde van**: la columna de cartones (x 86–640)
le cae en la cara.

**Entregas** (Drive: `VIDEOS FINALIZADOS` › «unidad 1» `1PbxRVMi7bjWl6XqL9kqjcDoQLBhaC7NJ`,
«unidad 2» `17__DYHiWGyTazAbPycbw0raJTYGe9Zl4`, «unidad 3» `1b_rT09Wjw1UkYhEFUUmly3QPB4VpF_LX` y
«unidad 4» `150cl_kFtK1Cm8BTTl-TB6rOrtRwJOMGJ`; las de las unidades 2 y 3 se crearon ese día).

| pieza | plan | línea | entrega | largo | cuadros = línea | LUFS · pico | PSNR medio / mín. | bytes | Drive |
|---|---|---|---|---|---|---|---|---|---|
| U1 inicio | `plan_tau1i` | `TA - U1 - INICIO` | `terminacionesanticipadas - U1 - INICIO-v1.mp4` | 7:26 | 10.690 | −16,1 · −2,9 | 51,3 / 45,0 | 190.972.710 | `1kPSTfF0DZnkQgmvj5dowjv2Z4ivPfJcQ` |
| U1 cierre | `plan_tau1c` | `TA - U1 - CIERRE` | `… - U1 - CIERRE-v1.mp4` | 6:32 | 9.402 | −16,1 · −3,0 | 51,7 / 45,0 | 160.322.930 | `1ObJ2lq2vHkvvlSbpvMX5ZaE6qBXmOSZB` |
| U2 inicio | `plan_tau2i` | `TA - U2 - INICIO` | `… - U2 - INICIO-v1.mp4` | 8:06 | 11.649 | −16,1 · −3,0 | 51,4 / 45,1 | 212.094.701 | `1qA0dZLWjsbVBhvStLhFgRd5Jk2aymHLn` |
| U2 cierre | `plan_tau2c` | `TA - U2 - CIERRE` | `… - U2 - CIERRE-v1.mp4` | 6:33 | 9.419 | −16,1 · −2,9 | 51,3 / 45,1 | 165.583.769 | `18xtcNVG0CcQmMoZxP0-iBkhTgPpcFPUw` |
| U3 inicio | `plan_tau3i` | `TA - U3 - INICIO` | `… - U3 - INICIO-v1.mp4` | 7:25 | 10.665 | −16,1 · −2,9 | 51,3 / 45,1 | 197.999.037 | `1_vJs94ayibrXa8E9pgSvAPgYX-SEWRm-` |
| U3 cierre | `plan_tau3c` | `TA - U3 - CIERRE` | `… - U3 - CIERRE-v1.mp4` | 6:39 | 9.573 | −16,1 · −3,0 | 51,5 / 45,1 | 171.605.325 | `1-O3cIkxZaoFQJqsZ3R8qwNm13t7FmeuU` |
| U4 inicio | `plan_tau4i` | `TA - U4 - INICIO` | `… - U4 - INICIO-v1.mp4` | 8:22 | 12.037 | −16,1 · −3,0 | 51,2 / 45,1 | 215.259.279 | `1qF9Dffu3Qc9YOm6ERYIlmzEn9K-okLHt` |
| U4 cierre | `plan_tau4c` | `TA - U4 - CIERRE` | `… - U4 - CIERRE-v1.mp4` | 7:37 | 10.945 | −16,1 · −2,9 | 51,5 / 45,1 | 194.684.039 | `1Gv33bEn4L4vlpQBSVE1yWrlq-1BzOzM_` |

Todas: H.264 High L4.0, 1920×1080, Rec.709, 23,976; AAC 48 kHz estéreo copiado del máster. Subidas
con copia exclusiva y comparadas byte a byte contra una copia de servidor (ocho «OK»).

**Preset de x264.** Las dos de la unidad 1 salieron con `slow`, el de la receta. Las otras seis,
con `medium` (`PRESET_ENTREGA` en el plan, que lee `mp4_entrega`): mismo CRF 18 y mismo formato,
PSNR igual (51,3–51,5 dB) y archivos de tamaño parecido. Es por la máquina (i7 de cuatro núcleos):
con `slow` cada video tardó 26 a 30 minutos compitiendo con los compuestos; con `medium`, 9 a 12,5.
La v2 con gráficos vuelve a `slow` quitando esa línea del plan.

**Cómo se hizo la tanda** (`D:\DAE\_tmp\ta_u\`): `prep_tau.py` (traer, medir, hoja de cuadros y
Scribe, cuatro por proceso), `lote_cadena.py` (componer, título y lower third, tres a la vez, sin
After Effects), `lote_entrega.py` (línea y máster de a uno, porque Resolve rinde de a uno; la
entrega x264, la hoja de revisión y la copia a Drive, dos a la vez) y `prioridad.py` (los ffmpeg
por debajo de lo normal para que Resolve tenga procesador: el máster pasó de 7 minutos a 1–2).
De la primera medida a la última entrega en Drive, 1 h 35 min (17:47 a 19:22), con las ocho ya verificadas.

**Dónde.** `D:\DAE MASTER\CURSO 4 - Curso Terminaciones Anticipadas\UNIDAD n\<INICIO|CIERRE>\`,
con las subcarpetas de la serie. Másters de 32 Mb/s en
`D:\DAE\_masters_archivo\CURSO 4 - Curso Terminaciones Anticipadas\UNIDAD n\<pieza>\`. Bins de
Resolve: `CURSO 4 - TERMINACIONES ANTICIPADAS` › `UNIDAD n - INICIO - PROFE` y `UNIDAD n - CIERRE -
PROFE`. Hojas de revisión: `D:\DAE\_tmp\sr_ta\tau<n><i|c>\hoja_rev_1.jpg`.

**Para la v2 con gráficos:** agregar los ítems al plan, quitar `PRESET_ENTREGA`, poner
`VERSION = 2` y correr cartones, listas, línea y entrega sobre el mismo compuesto.
