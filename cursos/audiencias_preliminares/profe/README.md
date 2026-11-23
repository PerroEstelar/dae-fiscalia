# Audiencias preliminares y medidas de aseguramiento · videos de profe (20 nov 2026)

Curso «Audiencias preliminares y medidas de aseguramiento» (Prioridad 1). Profe: **John Zuluaga Taborda**, autor del
curso (la ficha pone «Zuluaga John» en 1.5; el nombre completo es el del rótulo de Teams de la grabación). **Entrega
provisional**: intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos.

## El pedido

Sebastián (20 nov): «ok ahora vamos a hacer lo mismo con estos», la carpeta de Drive «Videos Curso Virtual FGN-UNAL»
(`1qXcS3F8bXq-yXtIz88b5U291yEfGwI37`, dentro de VIDEOS del curso). «Lo mismo» es lo de Desaparición forzada: transcribir,
cotejar con el documento del curso, cortar lo que haga falta, gráfica provisional, subtítulos, inventarios y enlaces.

## Las fuentes

Ocho grabaciones de Teams, la introducción y la recapitulación de cada unidad: 1280×720, 25 fps, ~880 kb/s, BT.601,
AAC estéreo. Fondo virtual con el edificio de la DAE y el panel DAE/Fiscalía; rótulo de Teams con el nombre abajo a la
izquierda (x 0–180, y 684–717), que queda fuera de la ventana (1200×675 desde (40, 0), ×1,6). Ya vienen editadas:
arrancan con 2 a 3,8 s de silencio digital y tres terminan pegadas a la última palabra.

| plan | pieza | fuente | tramo (s) | dura | 
|---|---|---|---|---|
| `plan_apu1i` | U1 inicio | `Unidad 1 - Introducción.mp4` (3:15,7) | 3,33–192,34 | 3:09,0 |
| `plan_apu1c` | U1 cierre | `Unidad 1 - Recapitulación.mp4` (7:01,6) | 3,29–420,24 | 6:57,0 |
| `plan_apu2i` | U2 inicio | `Unidad 2 - Introducción.mp4` (2:25,3) | 1,57–145,28 (final) | 2:23,7 |
| `plan_apu2c` | U2 cierre | `Unidad 2 - Recapitulación.mp4` (9:15,3) | 1,45–555,28 (final) | 9:13,8 |
| `plan_apu3i` | U3 inicio | `Unidad 3 - Introducción.mp4` (3:36,4) | 2,75–214,20 | 3:31,5 |
| `plan_apu3c` | U3 cierre | `Unidad 3 - Recapitulación.mp4` (11:00,5) | 2,67–659,66 | 10:57,0 |
| `plan_apu4i` | U4 inicio | `Unidad 4 - Introducción.mp4` (2:34,6) | 2,33–154,56 (final) | 2:32,2 |
| `plan_apu4c` | U4 cierre | `Unidad 4 - Recapitulación.mp4` (10:16,3) | 3,01–615,95 | 10:12,9 |

**Sin cortes adentro.** Las transcripciones (Scribe sobre cada fuente, `D:\DAE\_tmp\ap_p\stt\`) no tienen tomas
repetidas, frases dichas dos veces ni pausas de más de 2 s; los tropiezos sueltos («función— fusiona», «la re— su
restricción») se quedan en el video y salen del subtítulo. Bordes: 0,45 s antes de la primera palabra y 0,7 s después
de la última (o el final del archivo).

## Lo que pide el documento y lo que hay

La ficha («Vaciado_Curso…», `1TdXDfJV_j9MM45JcnWqbp4vvJjO2Ddz9`, y una por unidad) pide:

- **Video de presentación del curso** (2.1): **no está en la carpeta.**
- Por unidad, el video de la introducción (3.2) y el de la actividad de acompañamiento dirigido (3.8, «una síntesis de
  los principales temas abordados en la unidad»): son las ocho grabaciones. Van como `INICIO` y `CIERRE`.
- El cierre del curso (4.1) es un mensaje escrito, sin video.

## Nombres

- Curso: 1.1 de la ficha. Cartón: «Audiencias preliminares y / medidas de aseguramiento».
- Unidades: 3.1 de cada ficha. **La de la unidad 4 repite la de la 3** («Audiencias para la autorización y control de
  técnicas de investigación») en la ficha general y en la de la unidad; el cartón lleva el de la lista de contenidos del
  curso (2.x): «Intervención argumentada en audiencias preliminares y ejercicio integrador».
- Otras cosas de la ficha que no cuadran (no tocan los videos): la introducción dice «durante cinco unidades» y son
  cuatro; los criterios de certificación (4.3) hablan de «trata, tráfico y explotación sexual», que es de otro curso.

## Cómo se arma

- `base_ap_profe.py` y los 8 planes; `lote/cadena_ap.py` (compuesto, título y lower third, tres a la vez) y
  `lote/entrega_gpu.py` (línea de Resolve y entrega por la placa NVIDIA, ~5 Mb/s, fuera de receta), en `D:\DAE\_tmp\ap_p\`.
- 25 fps → la línea va a 23,976: el compuesto se escribe a 23,976 (`FPS_COMPUESTO`), los tramos se cuentan a 25.
- Árbol: `D:\DAE MASTER\PRIORIDAD 1\CURSO - AUDIENCIAS PRELIMINARES Y MEDIDAS DE ASEGURAMIENTO\VIDEOS PROFE\UNIDAD n\
  INICIO|CIERRE`, fuentes en `00 FUENTES`. Bins: `PRIORIDAD 1 / CURSO - AUDIENCIAS PRELIMINARES Y MEDIDAS DE
  ASEGURAMIENTO / VIDEOS PROFE / UNIDAD n - …`.
- Drive: VIDEOS del curso › **VIDEOS FINALIZADOS** (`1r2AepvLVei0eHFf47Kh-YePDPowoTuvF`), creada para esto, al lado de
  «Videos Curso Virtual FGN-UNAL».

## Entregas

Las 8, el 20 de noviembre entre las 00:16 y las 00:29 (hora de Colombia), en **VIDEOS FINALIZADOS**
(`1r2AepvLVei0eHFf47Kh-YePDPowoTuvF`), cada una con su `.srt` al lado (y en `05 EXPORTS` junto al video). En total
53,5 minutos. Render por la placa NVIDIA desde Resolve, ~5,4 Mb/s (fuera de receta, como en Desaparición forzada).
Sonido medido en cada entrega: −16,1 a −16,2 LUFS, pico −2,9 a −3,0.

| video | MB | id en Drive | `.srt` |
|---|---|---|---|
| `audienciaspreliminares - U1 - INICIO-v1.mp4` | 142 | `1udMohMW6kNE7kMo7kb7vOse3er7up3pI` | `1nsnNitZPLuzbTGOVYzL13iETNgZIdYeT` |
| `audienciaspreliminares - U1 - CIERRE-v1.mp4` | 289 | `1ATj4JTVoE4GIyg-Dg-IUs8Dwq6Rz2UD1` | `1gYpQvBsTmOCHmWAhFNx-QiIB2AqhNoZA` |
| `audienciaspreliminares - U2 - INICIO-v1.mp4` | 113 | `1NILsuLPmiTuughnPHyaH_DpVfkKediOu` | `1hlFmWZxcUAJjZGlYDZ7V6hQv0U_kfu7c` |
| `audienciaspreliminares - U2 - CIERRE-v1.mp4` | 376 | `1n8-CshwBvuTBjlbnkU6Usrtd7T9wN2Mj` | `1VZP9fpM7KGx8yEZFryTeDZbU1V05Pt-M` |
| `audienciaspreliminares - U3 - INICIO-v1.mp4` | 157 | `1xytsV4cg59tIehWnBAHMxlX_JMXYIabF` | `1k3X9IIBJ3nV-dWPMTQdEBPVaTsjOhduU` |
| `audienciaspreliminares - U3 - CIERRE-v1.mp4` | 442 | `1O166514apJpjak4dfI1N_Ihf4EvjgNFT` | `1XOPFVyACbNFSc2rJ8o8ZvvnA9GzlUdCU` |
| `audienciaspreliminares - U4 - INICIO-v1.mp4` | 119 | `1U59NaaBNEn5tifpV27i1WDaceqCDTVgh` | `1YOeJ8MF-p5UX5lsxkVP4chCcMz-e62Cj` |
| `audienciaspreliminares - U4 - CIERRE-v1.mp4` | 414 | `1k6-Q6-7D63ZCGmafCc9oUHHHrNiwEjib` | `1p0tKIGygVi0_NP3_rYHYyCfbKOwMeBPU` |

- **Verificadas contra el disco**: cada entrega se copió en `_verif ap 20nov`, se bajó por Drive para escritorio y se
  comparó con la de `05 EXPORTS` (`herramientas/entrega/verificar_drive.py`, `D:\DAE\_tmp\ap_p\verif.log`: 8 «OK»).
  Después el video pasó a VIDEOS FINALIZADOS y la copia de verificación a la papelera.
- Hojas de revisión (`<TMP>/hoja_rev_1.jpg`) miradas en las 8: intro, cartón de título, rótulo «John Zuluaga Taborda /
  Autor del curso», cartón de cierre y outro. El rótulo de Teams de la grabación queda fuera de la ventana.
- Las copias de trabajo de las fuentes quedaron en `_MA subidas › _bajadas AP 20nov` (`166c5pWMWWins5VFEFJcB-3vuCuwIz9pb`);
  las originales siguen en «Videos Curso Virtual FGN-UNAL».
- Subtítulos: `../subtitulos/README.md`.

## Inicio y cierre del curso (23 nov 2026)

Sebastián: «llegaron el inicio y cierre que nos faltaban de ese curso». Están en la carpeta del profe «Videos Curso
Virtual FGN-UNAL» (`1EwIMnNW2Ales4pjaBhsvh3uq6G2Efb-f`, la misma que tiene las ocho de las unidades): `Apertura de
curso.mp4` (5:34,8) y `Cierre de curso.mp4` (5:59,8), el mismo formato de Teams (1280×720, 25 fps, BT.601). Copias de
trabajo en `_bajadas AP 20nov`; en disco, en `00 FUENTES`.

| plan | pieza | tramo (s) | entrega | dura | id en Drive | `.srt` |
|---|---|---|---|---|---|---|
| `plan_apci` | inicio del curso | 5,55–331,74 | `audienciaspreliminares - CURSO - INICIO-v1.mp4` (230 MB) | 6:00 | `18ggELQo92OD3CvJr93PaasxfUEYn0Fi5` | `1QU07kSUNuVWexEJY5ekUiFgH6SyFwArs` |
| `plan_apcc` | cierre del curso | 3,13–356,28 | `audienciaspreliminares - CURSO - CIERRE-v1.mp4` (248 MB) | 6:27 | `15uJ6HGC98vYvJxwv_o5uXd6xEqkso94B` | `1S7jfP61A9cnjDtbtVfbUgj2lWnaXbWyz` |

- `armar_curso` en `base_ap_profe.py`; carpetas `VIDEOS PROFE/CURSO/INICIO|CIERRE`, bin `… / VIDEOS PROFE / CURSO - INICIO|CIERRE`.
  Cartón de título: el nombre del curso y «Inicio del curso» o «Cierre del curso».
- Sin cortes. El inicio es el «Video de presentación» (2.1) que faltaba; el cierre la ficha lo da como mensaje escrito
  (4.1) y el profe lo grabó. En el cierre el tropiezo «Audiencias preliminares… d— y medidas» (0:27–0:35 del video,
  con 1,6 s de pausa) se queda.
- Entregas por la placa NVIDIA (pedido 5000 kb/s, real ~5,36 Mb/s), −16,1 LUFS, pico −3,0. Hojas de revisión miradas.
  Verificadas byte a byte con una copia de servidor en `_verif ap 23nov` (`D:\DAE\_tmp\ap_p\verif_curso.log`: 2 «OK»;
  la carpeta, a la papelera). En VIDEOS FINALIZADOS con su `.srt` al lado, y el `.srt` también en `05 EXPORTS`.
- `lote/cadena_ap.py` acepta ahora los planes por argumento (antes creaba las carpetas solo de los ocho de `PLANES`).
