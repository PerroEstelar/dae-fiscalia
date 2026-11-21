# Tráfico de migrantes y trata de personas — videos de profe (17–18 nov 2026, entrega provisional)

Pedido de Sebastián del 17 nov (22:14): los once videos de la carpeta `VIDEOS` del curso «Investigación y
judicialización de los delitos de tráfico de migrantes y trata de personas» (Drive
`1Xslh4RCzyn52FeFF_I1OynZ3oqowWgmv`), «gráfica provisional pero completos»: intro, cartón de título, lower
third, cartón de cierre y outro; el cuerpo, sin gráficos.

Son: bienvenida y cierre general del curso; introducción, retroalimentación de la evaluación y cierre de las
unidades 1, 2 y 3.

## Las fuentes

- **Ocho son un avatar** de José María Peláez Mejía («Soy José María Peláez Mejía, autor experto de este
  curso»), vertical (1080×1920, 25 fps), sobre una biblioteca generada. La introducción de la U1 viene
  vertical dentro de un cuadro de 1920×1080 (la imagen ocupa las columnas 656–1263). El audio termina 0,8 s
  antes que la imagen.
- **Los tres cierres de unidad** (`.webm`, 1280×720, cadencia variable, Opus mono) los presenta una mujer con
  el fondo virtual de la DAE. No dice su nombre.

## Decisiones

- **El avatar se recorta y va sobre el fondo de la DAE.** Sebastián: «recortar el personaje y usar el fondo de
  las imágenes que ya hemos usado, específicamente las que están los logos hacia la izquierda y que no tenga
  el logo Aprende con la DAE… iguales al resto de videos de profe hablando a cámara». Sin marca de agua dentro
  del contenido.
  - Fondo: `FONDO 4 V2.png` (vista aérea, logos arriba a la izquierda), de su carpeta de Drive «FONDOS SIN
    APRENDE CON LA DAE» (`1VFuiOQiV12FpQ1oRKp90oz0Boef8QtwJ`); copia en `00 FONDOS`.
  - Recorte: `herramientas/video/recorta_persona.py` (Robust Video Matting, resnet50, por la placa de video).
    Cada plan lleva `RECORTE = dict(y=…, x=…, lado=…)`: el cuadrado de la fuente que se lleva a 1080×1080. La
    persona queda centrada en x=1250. Junto al recortado se guarda el mate (`…_recortado_mate.mp4`).
  - Lo primero que se armó (recorte cuadrado sobre el mismo cuadro desenfocado) se descartó sin entregar nada.
- **Cartón de título:** el nombre del curso en tres renglones y debajo «Introducción al curso», «Cierre del
  curso», «Unidad n. Introducción», «Unidad n. Retroalimentación de la evaluación», «Unidad n. Cierre». Los
  nombres de las unidades (97 a 157 caracteres) no entran junto al nombre del curso.
- **Lower third del avatar** (1,9–9,9 s, columna angosta `LT = (44, 560)`): «José María Peláez Mejía · Autor
  experto del curso. Magistrado de la Sala Penal del Tribunal Superior del Distrito Judicial de Cúcuta».
- **Lower third de los cierres: pendiente.** Se le preguntó a Sebastián si la presentadora es Mariana Lisbeth
  Rodríguez Muñoz (investigadora auxiliar; la nombra el avatar en la bienvenida). Hasta que confirme, los tres
  van sin rótulo de nombre (`PROFE_CIERRES = None` en `base_tr_profe.py`). Agregarlo es rendir el lower third,
  rearmar la línea y una entrega nueva (`-v2`).
- **Entrega directa de Resolve por la placa NVIDIA** (H.264, unos 5 Mb/s, AAC), sin máster de 32 Mb/s: no
  había disco. Es la vía de los cierres de Bienes, fuera de receta; se le dijo a Sebastián.

## Dónde está cada cosa

- `base_tr_profe.py` (decisiones y medidas), `plan_trci.py`, `plan_trcc.py`, `plan_tru<n><i|r|c>.py`.
- Disco: `D:\DAE MASTER\PRIORIDAD 03\VIDEOS PROFE\<CURSO|UNIDAD n>\<INICIO|RETROALIMENTACION|CIERRE>`
  (`01 VIDEO`: fuente, recortado, mate y compuesto; `05 EXPORTS`: la entrega). Bins `PRIORIDAD 03 / VIDEOS
  PROFE / …`; líneas `TRATA - CURSO - INICIO|CIERRE` y `TRATA - Un - INICIO|RETROALIMENTACION|CIERRE`.
- `lote/`: los guiones del lote tal como corrieron en `D:\DAE\_tmp\tr_p\`.
  - `recorta_lote.py`: lee `recortes.txt` y recorta dos a la vez; cuenta los cuadros contra la fuente y pasa
    cada plan a `cola.txt`.
  - `lote_cadena.py`: compuesto, título y cartones de cada plan de `cola.txt`.
  - `entrega_gpu.py`: espera el compuesto, rinde el lower third, arma la línea, rinde la entrega por la placa,
    cuenta cuadros, mide el sonido (y lo rehace si el AAC de Resolve salió roto), copia a la carpeta de paso
    de Drive si hay cupo y saca la hoja de revisión.
  - `verif_tr.py`: compara cada entrega de la carpeta de paso con la local, byte a byte (directo si no está
    en la caché de Drive, o contra una copia de servidor). `rev_entrega.py`: esa verificación más una hoja de
    seis cuadros de la entrega. `pico_scan.py`: busca muestras fuera de escala en el audio. `estado.py`: el
    resumen. `prioridad.py`: baja la prioridad de los ffmpeg.

## Entregas

Drive: VIDEOS › **VIDEOS FINALIZADOS** (`1A3rlk8CCzw0cRq2sFEAZ_H6plaFMkq_l`).

| entrega | dura | cuadros | sonido (LUFS / dBTP) | Drive |
|---|---|---|---|---|
| `traficoytrata - CURSO - INICIO-v1.mp4` | 1:51 | 2.668 | −16,3 / −1,9 | `1ufvfsj_qZnj96u6F6HxNjGwD2vsijCMh` |
| `traficoytrata - CURSO - CIERRE-v1.mp4` | 6:56 | 9.973 | −16,1 / −2,4 | `1zF18nhsYvVZSUnNtG0AaT0dqYbyZuk0P` |
| `traficoytrata - U4 - INICIO-v1.mp4` | 7:09 | 10.293 | −16,1 / −2,2 | `1E2tHeTl9LwuLEj4oAG8oiZfj7T1ynjiH` |
| `traficoytrata - U4 - RETROALIMENTACION-v1.mp4` | 7:06 | 10.223 | −16,1 / −3,0 | `1kOWsiScXS6AdhpLaGrK-jIZL08PRuTpF` |
| `traficoytrata - U4 - CIERRE-v1.mp4` | 8:14 | 11.838 | −16,0 / −3,0 | `10m4z4jj5lk_HZxyARvKyfH9JbdwSdYcV` |
| `traficoytrata - U5 - INICIO-v1.mp4` | 7:03 | 10.136 | −16,1 / −2,8 | `1WFdglgcsK6Nw0wGbSqngWqSd6hmLs5jq` |
| `traficoytrata - U5 - RETROALIMENTACION-v1.mp4` | 7:04 | 10.168 | −16,1 / −2,5 | `1Sd7Xrzh5RSEujHSXp3p07hgqlnyvQlr_` |
| `traficoytrata - U5 - CIERRE-v1.mp4` | 8:14 | 11.834 | −16,1 / −2,5 | `1OejCIBOfI3nYujLpB5u_08ffzQMxiRrS` |
| `traficoytrata - U1 - INICIO-v1.mp4` | 7:11 | 10.341 | −16,1 / −2,7 | `1yF-RWTVTa0egLD7qSXdYij14EjARpR9i` |
| `traficoytrata - U1 - RETROALIMENTACION-v1.mp4` | 7:34 | 10.887 | −16,1 / −3,0 | `1GAY9p7Oo1zFLBR8iYzxnUYb4Kp9lbnjP` |
| `traficoytrata - U1 - CIERRE-v1.mp4` | 8:03 | 11.576 | −16,0 / −3,0 | `1hzwVeVFfooew1iCfVD5ZfwWi7MjrC29G` |
| `traficoytrata - U2 - INICIO-v1.mp4` | 7:13 | 10.375 | −16,1 / −2,9 | `1PJu_LRq825XwcR9nhC-WFWnD4jNQUFl-` |
| `traficoytrata - U2 - RETROALIMENTACION-v1.mp4` | 7:03 | 10.135 | −16,1 / −2,8 | `1wz2dE0wGsGELHnJe9wzY6S6z02MHBAuO` |
| `traficoytrata - U2 - CIERRE-v1.mp4` | 7:56 | 11.424 | −16,1 / −2,4 | `1xgWmQ0ISBBmVaQOvoc6FOhhCQ8ZC_4j9` |
| `traficoytrata - U3 - INICIO-v1.mp4` | 7:14 | 10.398 | −16,1 / −3,0 | `1CEYfmwMg6H9W24Y26_4fTZvP_htCs9WD` |
| `traficoytrata - U3 - RETROALIMENTACION-v1.mp4` | 7:09 | 10.286 | −16,1 / −2,9 | `104Y49E1KDRrj11rPA1Byg8of-NhZTYvr` |
| `traficoytrata - U3 - CIERRE-v1.mp4` | 7:59 | 11.482 | −16,1 / −3,0 | `1_c70j9pMBeBIGqyws85AJrvmCOKyqZp-` |

Las once de las unidades 1 a 3 y el curso son 76 min de video. Las once se compararon byte a byte con lo que guarda Drive antes de moverlas a la
carpeta final (cuatro leídas del servidor sin copia y siete con copia de servidor; ver «Verificar una entrega
en Drive» en CLAUDE.md), y en ninguna hay muestras de audio fuera de escala (`pico_scan.py`).

Tiempos de la noche: fuentes en disco a las 22:20; recorte de los ocho avatares de 23:11 a 01:27 (dos a la
vez); primera entrega buena 23:23 y última 01:34.

**El cierre de la U1 lleva el audio rehecho.** El AAC que codificó Resolve traía dos tramos de 20 ms fuera de
escala (dos chasquidos); se rindió de nuevo con audio PCM y el AAC lo hizo ffmpeg. `entrega_gpu.py` lo detecta
y lo hace solo. Los renders rotos quedaron en `UNIDAD 1\CIERRE\05 EXPORTS\_rindiendo` y `_descartes`.

**Subtítulos (20 nov 2026):** los once `.srt` están al lado de cada video en VIDEOS FINALIZADOS y en `05 EXPORTS`;
ver `../subtitulos/README.md`. Al transcribir las entregas apareció que **los cierres de las unidades 2 y 3 terminan a
mitad de frase** («…descartar la hipó…» y «…la comunicación clara de…»): así terminan las grabaciones de la presentadora
(la fuente sigue un par de segundos sin voz), no es un corte de la edición.

## Unidades 4 y 5 (21 nov 2026)

Sebastián: «tenemos estos videos de más para procesar, en gráfica provisional y de manera completamente veloz… inicio,
retroalimentación y cierre de las unidades 4 y 5 de investigación y judicialización… en los casos de video que haya que
reemplazar el fondo, hazlo como lo hemos hecho antes». Fuentes en `E:\DAE MASTER\CURSO INVESTIGACION Y JUDCIALIZACION\
UNIDAD 4|5\` (los dos zip que están en la carpeta VIDEOS del curso en Drive, descomprimidos): las mismas tres clases que
en las unidades 1 a 3, y el mismo tratamiento.

- **Introducción y retroalimentación:** el avatar de José María Peláez (1080×1920, 25 fps, de 389 a 396 s), recortado
  sobre `FONDO 4 V2.png` con `RECORTE` de y=215 a 230 (hoja de cuadros contra el de la U3: mismo encuadre,
  `D:\DAE\_tmp\tr_p\u45\hoja_recortes.jpg`). Sin cortes: de medio segundo antes de la primera palabra al final.
- **Cierres:** la presentadora de los cierres de las unidades 1 a 3, sin tomas repetidas ni tropiezos, y esta vez **las
  dos grabaciones terminan la frase**. Sin rótulo de nombre (sigue pendiente confirmarlo), como los otros tres.
- El AAC de Resolve volvió a salir roto en el cierre de la U4 (pico +63 dB); `entrega_gpu.py` lo rindió de nuevo con PCM
  y el AAC de ffmpeg, sin intervención.
- **Ritmo:** el recorte va a 4,9 cuadros/s cada uno con dos a la vez y la máquina libre, pero baja a 1,7–3,0 mientras
  corren dos compuestos (y bajó a 2,9 con `prep_tr2.py` midiendo cuadro a cuadro, que se paró: para estas fuentes basta
  la transcripción, `D:\DAE\_tmp\tr_p\stt_rapido.py`). Los cierres, que no se recortan, salieron primero.
- Lotes en `D:\DAE\_tmp\tr_p\` (los de la tanda anterior quedaron como `*_u123`); verificación y subtítulos en
  `D:\DAE\_tmp\tr_s45\` (`verif_loop.py`, `stt_loop.py`).

## Pendiente

- **Rótulo de nombre en los cinco cierres** (ver arriba): falta que Sebastián confirme el nombre y el cargo.
- **Manos cortadas:** cuando el avatar abre las manos, el borde de la fuente vertical las corta, y sobre el
  fondo ancho se ve el corte recto por un instante. Es de la fuente.
- **Disco:** D: quedó con 2,6 GB libres. Del árbol de este curso (19 GB) sobran, cuando Sebastián lo decida:
  `_rindiendo` (1,75 GB: cuatro renders rotos iguales y el `.mov` con PCM) y `_descartes` (0,7 GB: la primera
  versión, descartada). Las fuentes (5,2 GB) son copias de las de Drive.
- Para la versión con gráficos hay que medir la caja de cartones contra el avatar (está centrado en x=1250
  y los hombros se abren hacia la izquierda abajo): no se midió.
