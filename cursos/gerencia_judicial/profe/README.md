# Gerencia judicial · videos de profe

## Bienvenida al curso e inicio y cierre de las unidades 1 a 4 (27 nov 2026) — entrega provisional

Pedido de Sebastián (27 nov): procesar «de pe a pa», con gráfica provisional, los videos nuevos del profe hablando a
cámara, quitarles el fondo y poner el de siempre, editar y componer entre tomas si hace falta, subirlos y actualizar lo
que haya que actualizar. Profe: **Jairo Ignacio Acosta Aristizábal**. Fuente: tres grabaciones de cámara web en
`E:\DAE MASTER\PRIORIDAD 2\CURSO - GERENCIA JUDICIAL\VIDEOS PROFE` (detalle en `base_gj_profe.py`).

| pieza | entrega · id | `.srt` | largo | edición |
|---|---|---|---|---|
| Bienvenida al curso | `gerenciajudicial - CURSO - INICIO-v1.mp4` · `121L40NbEIwaQbC12s7BVrA-tHlJ39fIQ` | `1iBskDxHWB7K1KcfwPspxUdGQQfOBvoTu` | 24:23,1 · 35.080 cuadros | 18 cortes (rótulos leídos y arranques en falso); 16 tramos en plano cerrado |
| Inicio de la U1 | `gerenciajudicial - U1 - INICIO-v1.mp4` · `185yvKV7YF9xytSxPPgP_O_1EPO0JvLwY` | `1QXaXVhVEvl4QfZ13BwG59Kjx6ZzOGMZ2` | 3:07,7 · 4.500 cuadros | **compuesto entre dos tomas**; 1 tramo cerrado |
| Cierre de la U1 | `gerenciajudicial - U1 - CIERRE-v1.mp4` · `16pzyM1-1nZDD3A1ulRkeeGVPlMnZF4OQ` | `1bkgwM8C5HXBmy9mfRpxyQYd7rxuYMnO7` | 3:04,7 · 4.428 cuadros | sin cortes |
| Inicio de la U2 | `gerenciajudicial - U2 - INICIO-v1.mp4` · `1nJKFxnZCLkVHMYt8hftCyaglMxvOs7VQ` | `1QqMVFR6VMSuF4YxqcrQBngfbsx4Q2Ya0` | 2:57,7 · 4.261 cuadros | 1 corte |
| Cierre de la U2 | `gerenciajudicial - U2 - CIERRE-v1.mp4` · `1Wk3f2WGv4egjDA_qCjc4rN0wKFsSo9UC` | `1Dru7nNT_kVFnkFbAw4_yWHdNtlxp2bRY` | 2:54,0 · 4.172 cuadros | 2 cortes |
| Inicio de la U3 | `gerenciajudicial - U3 - INICIO-v1.mp4` · `16ktFMTqh43D0h4oq1fiOiRxv6quG3Qn5` | `1i5m6r7f7W7SRJjYq41nUjEIqif7bvajC` | 3:13,1 · 4.630 cuadros | 1 corte |
| Cierre de la U3 | `gerenciajudicial - U3 - CIERRE-v1.mp4` · `1TnmHEUIDFrtEfAkTKp1itjjYSYMCyLa0` | `1kqic0zlkpj18Y-2iWJ0u9IXswLqQnNya` | 2:59,5 · 4.304 cuadros | 3 cortes |
| Inicio de la U4 | `gerenciajudicial - U4 - INICIO-v1.mp4` · `1jXSa-IOZPv1ylh-d4V5gIo2NcMirKczD` | `1XtWTc6kL-48knVqGjOgSJO4nIAMVpjbE` | 2:57,1 · 4.246 cuadros | 1 corte |
| Cierre de la U4 | `gerenciajudicial - U4 - CIERRE-v1.mp4` · `1uij0YH7iMHZNZ54Ob27uU6AtuHs8Xr8r` | `1TQG3k75AKey_g9g2jNIdGP3xwPQzzIy6` | 2:55,0 · 4.196 cuadros | 2 cortes |

Total: 48,5 minutos, 699 subtítulos. Carpeta de Drive: VIDEOS FINALIZADOS
(https://drive.google.com/drive/folders/1Is3yRM6apr3Q6G9bhDFRghKy8B82YQuZ); cada `.srt` al lado de su video (ver
`../subtitulos/`). Las nueve verificadas en Drive byte a byte (`herramientas/entrega/verificar_drive.py`: 9 OK).

- **Gráfica provisional:** intro, cartón de título («Gerencia judicial» + «Unidad n. <nombre>» o «Introducción al curso»),
  rótulo de nombre (8 s), cartón de cierre y outro. El cuerpo va sin gráficos.
- **Fondo:** el profe va recortado (Robust Video Matting) sobre `FONDO 4 V2`, al 85 % y centrado en x=1220.
- **Cortes:** los rótulos que el profe lee en voz alta y los arranques en falso con silencio a los dos lados; cada corte
  cambia a plano cerrado hasta la pausa siguiente. Cada corte está medido y contado en su plan (`plan_gj*.py`).
- **Video:** H.264 High L4.0, 1920×1080, 23,976, Rec.709, x264 CRF 18 `medium` (3,7–4,2 Mb/s). **Audio:** AAC 320 kb/s,
  48 kHz estéreo, −16,1 a −16,3 LUFS, pico −2,5 a −2,9 dBTP (limitador sobremuestreado a 192 kHz).
- **Sin el render de Resolve.** El render de Resolve quedó en 0 % («cuMemAlloc failed 801» en su log: la placa no le da
  memoria; reiniciar Resolve no alcanzó, en octubre lo arregló reiniciar el computador). `lote/entrega_ffmpeg.py` arma
  igual la línea en Resolve (`ic_linea_externa.py`) y después la **lee** (cada item, su pista, su lugar y su recorte de
  fuente) y la compone con ffmpeg: cuadros de la entrega = cuadros de la línea en las nueve.
- **Líneas de Resolve** (proyecto «DAE MASTER - CURSOS»): `GJ - CURSO - INICIO` y `GJ - U1..U4 - INICIO|CIERRE`, con su `.drt`
  en `10 TIMELINE SEBASTIAN` de cada pieza.

### Avisos para Sebastián

- **No hay cierre del curso** en las grabaciones; el cierre de la U4 dice «Les espero en el video de cierre del curso».
- La **bienvenida dura 24:23** (la ficha pide hasta 8 min para el video de presentación): se entrega completa.
- **Para revisar el contenido:** en la bienvenida (16:17) dice «Esta sensación es un problema de esfuerzo, es un problema
  de método» (falta el «no»; en el inicio de la U3 lo dice bien) y «discreción funcional» por «dirección funcional»
  (18:45). En el cierre de la U3 (1:10) presenta «Mejoraremos la investigación de delitos complejos» como «un buen objetivo
  en clave de Drucker» y en seguida dice lo que le falta («Precisa qué, cuándo, en qué plazo…»). Los subtítulos de los dos
  primeros van corregidos; el video, como lo dijo.
- **Rótulo:** «Autor experto del curso. Jurista; fue juez de la República y procurador delegado en lo penal». La ficha de
  presentación (1 nov) lo nombra autor; el formato de diseño del 7 sep pone a Diana Carolina Flórez como autora experta y
  a él como coautor. Si va «coautor», es un rótulo nuevo por video.
- Tropiezos sin silencio donde cortar quedan en el video (lista en cada plan) y salen del subtítulo.
- Las copias de paso de `_MA subidas` (9 MP4 y 9 `.srt`) no se pueden mover con el conector: se copiaron a VIDEOS
  FINALIZADOS y las de paso se pueden mandar a la papelera.

### Archivos

- `base_gj_profe.py` (lo común y todas las decisiones) y un `plan_gj*.py` por pieza (`gjci`, `gju1i` … `gju4c`).
- `lote/`: `extraer.py` (saca cada pieza de VIDEO 3 a su `_fuente.mp4`), `cortes.py` (mide cada corte), `planes.py`,
  `recorta_lote*.py` y `pegar_partes.py` (el recorte, en cuatro procesos; la bienvenida en cuatro partes que después se
  pegan sin recodificar), `lote_cadena.py` y `orquesta.py` (compuesto, título y cartones), `entrega_ffmpeg.py` (línea +
  MP4 + revisión), `subtitular.py`, `qa_grilla.py`. `entrega_gpu.py` (render por Resolve) quedó sin usar por la falla de
  la placa; `lanza_entrega.py` contaba mal los procesos y no se usa.
- Disco: `E:\DAE MASTER\PRIORIDAD 2\CURSO - GERENCIA JUDICIAL\VIDEOS PROFE\<CURSO|UNIDAD n>\<INICIO|CIERRE>\`
  (`01 VIDEO` recortado y compuesto, `02 CARTONES`, `05 EXPORTS` con el MP4 y el `.srt`, `10 TIMELINE SEBASTIAN`).
  Temporales en `D:\DAE\_tmp\gj_p\`.
