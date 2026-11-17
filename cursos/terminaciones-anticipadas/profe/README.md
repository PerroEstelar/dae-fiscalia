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

Todavía **no hay grabación** del inicio y del cierre de las unidades 1 a 4 (8 videos).

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
