# Justicia restaurativa en la práctica del fiscal · videos de profe

## Cierre del curso (18 nov 2026) — entrega provisional

Pedido de Sebastián (18 nov, 08:55): «por favor continúa con justicia restaurativa [carpeta VIDEOS del curso]; creo que
por ahora el único es el cierre del curso». En la carpeta (`1s-ZDIhTCPriybRjIIzSYx1GIqkcmgZvy`) había un solo archivo:
«Justica restuaraativa-  Cierre curso.mp4» (`1dGNePRbK98Td0Q45F07m7tKQzZkp1IRv`, 567 MB).

| | |
|---|---|
| entrega | `justiciarestaurativa - CURSO - CIERRE-v1.mp4` · `1yldH5QJQxz7UTnLpyoZBuN8MyjzIy9Pl` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - CURSO - CIERRE-v1.srt` · `1xuKv_o5UkvBMXuwx_PspTtD8NtTSbvi2` (ver `../subtitulos/`) |
| largo | 44:49,6 · 64.487 cuadros (= línea) · 1.800.362.042 bytes |
| video | H.264 Main L4.0, 1920×1080, 23,976, Rec.709, 5,16 Mb/s (placa NVIDIA, directo de Resolve) |
| audio | AAC 48 kHz estéreo · −16,0 LUFS · pico −2,6 dBTP |
| línea de Resolve | `JR - CURSO - CIERRE` (bin PRIORIDAD 1 › CURSO - JUSTICIA RESTAURATIVA) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\CIERRE DEL CURSO\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas` y comparación por bloques de 1 MiB, `verificar_drive.py`).

**Qué es «provisional»** (lo mismo que las clases de SRPA y las unidades de Bienes): intro, cartón de título, rótulos de
nombre, cartón de cierre y outro; el cuerpo va sin cartones ni gráficos. Y sale directo de Resolve por la placa NVIDIA,
sin máster de 32 Mb/s (pesaría ~10 GB y E: tenía 5). Si Sebastián quiere gráficos, sale una `-v2` sobre el mismo
compuesto.

### La fuente

- 1920×1080, 30 fps, 80.225 cuadros (44:34), BT.601, pico −1,3 dBFS. El mismo editor que las de Bienes: **trae pegados
  una intro (cuadros 0–277) y un outro (desde el 79949; el 79947 y el 79948 son blancos)**. Entra del 280 al 79947.
- **Dos coautores en videollamada**, cada uno en un mosaico de 936×528 sobre un lienzo blanco (izquierda x 7–942,
  derecha x 982–1916, los dos en y 290–817). Va el cuadro entero, sin ventana.
- Habla Víctor de 0:09,6 a 5:35; Martín de 5:37,7 a 23:09; cierra Víctor de 23:11 a 44:24.
- **Sin reinicios** (se leyó la transcripción buscando «repito», «perdón», «volver a empezar», frases repetidas y
  pausas). Hablan sin leer y hay tropiezos; no se cortó nada.

### Nombres y rótulos: de la ficha, no inferidos

Ficha «Prioridad 1 - Presentacion Vaciado_ Justicia Restaurativa en la Práctica del Fiscal.docx»
(`1bQcllAcXC6Ka9i76T3Ep4ZLYv1o1YY2y`): nombre del curso «Justicia restaurativa en la práctica del fiscal»; «Víctor Hugo
Ospina Vargas, profesor de pregrado y posgrado de la Universidad Nacional, y Martín Posada Martínez, investigador
académico». En el video se presentan ellos mismos (Scribe oye «Espina»).

- Izquierda: «Víctor Hugo Ospina Vargas · Coautor del curso. Profesor de pregrado y posgrado de la Universidad Nacional
  de Colombia». Derecha: «Martín Posada Martínez · Coautor del curso. Investigador académico».
- **Van debajo de cada mosaico, sobre el blanco, en tinta azul (22, 58, 79) y sin sombra.** El rótulo blanco con sombra
  de la serie no se lee sobre el lienzo, y dentro del mosaico taparía a la persona. `cartones_srpa.lower_third` acepta
  un tercer elemento con opciones: `x`, `top`, `ancho`, `tinta` (con `tinta` no dibuja sombra).
- Tres rótulos: Víctor 11,0–18,5 s de la fuente, Martín 19,2–26,7 y Martín otra vez 338,6–346,6, cuando toma la palabra.
- Se revisaron compuestos sobre un cuadro de la fuente antes de armar la línea: caja de (40, 851) a (829, 994) y de
  (1015, 852) a (1656, 962); no tocan los mosaicos (terminan en y 817) ni salen del cuadro.

### Cómo se hizo

```
profe_cadena.py plan_jrcc componer titulo cartones      # 09:14 a 09:35 (el compuesto, 19 min)
lote/entrega_gpu.py                                     # 12:14 a 12:20: línea, calibración, render (271 s), copia a G:
```

- `base_jr_profe.py`: raíz, bin, nombre del curso en dos renglones, 30 fps de fuente, `AUDIO_META I=-16:TP=-3:LRA=7`,
  los dos rótulos y `armar(...)`. `plan_jrcc.py`: el tramo y los tres rótulos.
- `lote/entrega_gpu.py` es el de Trata con dos cambios: **rinde en `%TEMP%\dae_rindiendo` (C:) y mueve la entrega a
  `05 EXPORTS` al final**, porque E: no tenía sitio para el render y el compuesto a la vez; y acepta el caudal ya
  calibrado como argumento. Pidió 5000 kb/s y salió a 5355.
- `profe_cadena.py` se negaba a empezar («SIN ESPACIO EN E:»): calculaba 0,35 GB por minuto, pensando en una pieza con
  gráficos y máster. Si todos los ítems del plan son rótulos, calcula 0,06 GB por minuto (mínimo 1 GB).
- Entre las 09:35 y las 12:13 no pasó nada: la sesión se cortó con el compuesto ya hecho. No se perdió trabajo.

## Inicio del curso (18 nov 2026, noche) — entrega provisional

Sebastián: «haz el video de inicio de justicia restaurativa de pe a pa, gráfica provisional, subido, verificado,
actualizados documentos, carpetas, etc.». Fuente: «Justica restuaraativa-  inicio curso.mp4»
(`1GOxoYu5V3zS3XvNvsLddTvv8AElk73B4`, 275 MB), en la misma carpeta que el cierre.

| | |
|---|---|
| entrega | `justiciarestaurativa - CURSO - INICIO-v1.mp4` · `19Pk8Lty8weGy3My29opsjl8xSCVCXsjI` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - CURSO - INICIO-v1.srt` · `1Nqgjpci4dQcnyEYvNhej21bFk0poNlRU` (254; ver `../subtitulos/`) |
| medidas | 20:01,9 · 28.816 cuadros = línea · 803.106.062 bytes · H.264 a 5,35 Mb/s · −16,0 LUFS, −2,8 dBTP |
| línea | `JR - CURSO - INICIO` (proyecto `DAE MASTER - CURSOS`) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\INICIO DEL CURSO\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas/_verif jr inicio 18nov` y `verificar_drive.py`: «OK»).

- **La fuente** es como la del cierre: 1920×1080, 30 fps, 36.485 cuadros (20:16), BT.601, los dos coautores en dos
  mosaicos sobre blanco, con intro (0–277) y outro (desde el 36208; 36206 y 36207 blancos) pegados. Entra del 280 al 36206.
- Habla Víctor de 0:10 a 7:47, Martín de 7:49 a 12:49 y cierra Víctor de 12:52 a 20:06.
- **Un corte de 29,8 s** (cuadros 4392 a 5285 de la fuente): Víctor se enreda y lo pide él («ahí, ahí, pequeño corte…
  perdón») y retoma la frase. Queda «…al caso penal, al caso concreto. | Se encuentran en su despacho de fiscales…». Es
  un corte directo: con dos mosaicos no hay plano cerrado que lo disimule. `plan_jrci.py` lleva `TRAMOS` con los dos
  tramos y su propio `cuadro()` que descuenta el corte.
- Rótulos: los mismos del cierre (Víctor 11,0–18,5 s, Martín 19,2–26,7 y Martín otra vez en 469,6–477,6, cuando toma
  la palabra). Cartón de título: «Inicio del curso».
- **Cómo se hizo:** `profe_cadena.py plan_jrci componer titulo cartones` (compuesto en 11,5 min) y `lote/entrega_gpu.py`
  (línea, calibración y render en 3 min; pidió 5000 kb/s y salió a 5346).
- **Resolve estaba en «Untitled Project»** y la línea falló (`carpeta_pool`: `NoneType`). Se abrió
  `DAE MASTER - CURSOS` con `LoadProject` (tarda más de un minuto: el puente corta, pero el proyecto queda abierto) y se
  relanzó la entrega.

## Inicio de la unidad 1 (18 nov 2026, noche) — entrega provisional

Sebastián: «ok ahora prosigue con unidad 1 inicio justicia restaurativa». Fuente: «…Unidad 1 inicio»
(`1dqkWwz5aokHQV2ECPAvmvXv8aYCI9FFI`, 151 MB).

| | |
|---|---|
| entrega | `justiciarestaurativa - U1 - INICIO-v1.mp4` · `1JlmaJV6PewDbHkVAFL4f6hb0_RS5ZCBx` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - U1 - INICIO-v1.srt` · `1fizXTPPfcUv5NdtZ5dGWexytohLJHZcQ` (112; ver `../subtitulos/`) |
| medidas | 8:25,4 · 12.117 cuadros = línea · 338.918.974 bytes · H.264 a 5,37 Mb/s · −16,1 LUFS, −2,6 dBTP |
| línea | `JR - U1 - INICIO` (proyecto `DAE MASTER - CURSOS`) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\UNIDAD 1\INICIO\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas/_verif jr u1 inicio 18nov` y `verificar_drive.py`: «OK»).

- **La fuente** dura 20:03,9 (36.117 cuadros, 30 fps, BT.601) pero **solo los primeros 8 minutos tienen contenido**:
  intro pegada (0–277), la conversación (278–14418), dos cuadros blancos, el outro y después negro hasta el final.
  Entra del 280 al 14419. Sin reinicios ni pausas largas: no se corta nada.
- **Tres mosaicos sobre blanco**, no dos: Martín arriba a la izquierda, un tercer profesor arriba a la derecha y Víctor
  abajo al centro. Habla Víctor (0:09,5–1:02), el tercer profesor (1:02,5–4:32,6), Martín (4:34,9–6:03,4) y cierra
  Víctor (6:05,9–8:00).
- **El tercer profesor no está en la ficha del curso.** Víctor lo presenta de palabra; se le preguntó a Sebastián y
  dijo «Jhonatan Sandoval, sin cargo»: el rótulo lleva solo el nombre, con esa grafía.
- **Nombre de la unidad** (cartón de título), del PDF del curso (`1WjbL40IW0mgYWmEGia8TMAwaj2082s56`, 3.1): «Unidad 1.
  Bases conceptuales y marco jurídico de la justicia restaurativa».
- **Rótulos:** con tres mosaicos el blanco libre queda abajo a los lados, y un nombre en un renglón se metía en el
  mosaico de abajo (empieza en x 509) o se salía por la derecha. Van en dos renglones y con `ancho=430`: Víctor en
  (24, 770), Martín en (24, 575), Jhonatan en (1440, 575); cada uno sale cuando esa persona empieza a hablar (11,0,
  63,3 y 275,9 s de la fuente). Se midieron las cajas en el alfa del `.mov` y se miraron sobre el compuesto antes de
  rendir: ninguna toca un mosaico ni el borde.
- **Cómo se hizo:** `prep_fuente.py` (copia, sonda y STT de la fuente), `profe_cadena.py plan_jru1i componer titulo
  cartones` (compuesto en 4,5 min) y `lote/entrega_gpu.py` (línea, calibración y render en 1,5 min; pidió 5000 kb/s y
  salió a 5365).
- Para ver un `.mov` qtrle con alfa sobre el compuesto en ffmpeg: `[1:v]select=eq(n\,90),format=rgba` y
  `overlay=format=rgb`. Con `-ss` en la entrada del `.mov` el cuadro salía vacío y la hoja no mostraba el rótulo.

## Cierre de la unidad 1 (18 nov 2026, noche) — entrega provisional

Sebastián: «ahora continúa con u1 justicia restaurativa cierre». Fuente: «Justica restuaraativa-  Unidad 1 cierre.mp4»
(`1n-OFMmvE1RjNZL4HWB1yWu41y6wLcjc0`, 179 MB), en la carpeta VIDEOS del curso.

| | |
|---|---|
| entrega | `justiciarestaurativa - U1 - CIERRE-v1.mp4` · `1_6-hPWglkRAzrpuxvrRTC_epsNMx_buu` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - U1 - CIERRE-v1.srt` · `1uz2jOdRPKn5Ebi7ubVVFZ_JzLH9SgYiM` (138; ver `../subtitulos/`) |
| medidas | 10:06,5 · 14.541 cuadros = línea · 406.021.636 bytes · H.264 a 5,36 Mb/s · −16,1 LUFS, −2,9 dBTP |
| línea | `JR - U1 - CIERRE` (proyecto `DAE MASTER - CURSOS`) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\UNIDAD 1\CIERRE\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas/_verif jr u1 cierre 18nov` y `verificar_drive.py`: «OK»).

- **La fuente:** 1920×1080, 30 fps, 18.835 cuadros (10:27,9), BT.601. Trae la intro pegada (0–277) y **no trae outro**:
  la conversación llega al último cuadro (brillo medido en todos los cuadros). Entra del 280 al 18835.
- Los mismos tres mosaicos y los mismos rótulos del inicio de la unidad (`plan_jru1c` los importa de `plan_jru1i`).
  Víctor abre (0:11,5–1:33,7), responde Jhonatan (1:33,8–4:17,5), después Martín (5:04,5–8:18,5) y cierra Víctor
  (8:21,2–10:27,3). Rótulos en 13,0, 94,6 y 305,5 s de la fuente.
- **Un corte de 46,1 s** (cuadros 7742 a 9126 de la fuente): Martín arranca, se traba («ahí me tosté, espérense»),
  pregunta fuera de la grabación cómo referirse a quienes cursan, Víctor le contesta y Martín vuelve a empezar («Vale.
  Pues al final, al finalizar esta unidad…»). Sale todo, «Vale.» incluido. Es un corte directo. La transcripción de
  la entrega lo confirma: «…por medio del modelo penal. Pues al final, al finalizar esta unidad…».
- **Cómo se hizo:** `prep_fuente.py` (ahora recibe la carpeta de paso de Drive como quinto argumento), brillo de todos
  los cuadros (`signalstats` a 160×90, 28 s), `profe_cadena.py plan_jru1c componer titulo cartones` (compuesto en 6
  min) y `lote/entrega_gpu.py` (línea, calibración y render en 1,5 min; pidió 5000 kb/s y salió a 5356).
- **Sitio en E:.** Quedaban 0,73 GB. Las grabaciones originales del cierre y del inicio del curso (567 y 275 MB) se
  movieron a `D:\DAE\_masters_archivo\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\<pieza>\fuente\` (copia, md5 igual
  y recién entonces fuera de E:), con un `LEER - la fuente esta en D.txt` en cada `01 VIDEO`. Las líneas usan el
  compuesto, no la fuente. Después de esta entrega: E: 0,76 GB, D: 0,81 GB.
