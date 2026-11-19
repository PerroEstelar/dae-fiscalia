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

## Inicio de la unidad 2 (18 nov 2026, noche) — entrega provisional

Sebastián: «ok continúa con justicia restaurativa u2 inicio». Fuente: «Justica restaurativa-  Unidad 2 inicio.mp4»
(`15uZ6c_QyxX5PCDsW2ekmAdh75fs9z-Rz`, 228 MB), en la carpeta VIDEOS del curso.

| | |
|---|---|
| entrega | `justiciarestaurativa - U2 - INICIO-v1.mp4` · `1oF-F75AhpIso3nc81vQByMsdiXUn9m-1` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - U2 - INICIO-v1.srt` · `1RposWITC6uS9HXLojBBGYQnqCROA22Fo` (279; ver `../subtitulos/`) |
| medidas | 20:29,1 · 29.469 cuadros = línea · 819.179.661 bytes · H.264 a 5,33 Mb/s · −16,0 LUFS, −2,5 dBTP |
| línea | `JR - U2 - INICIO` (proyecto `DAE MASTER - CURSOS`) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\UNIDAD 2\INICIO\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas/_verif jr u2 inicio 18nov` y `verificar_drive.py`: «OK»).

- **La fuente:** 1920×1080, 30 fps, 36.408 cuadros (20:13,6), BT.601, con intro (0–277) y outro (desde el 36132; 36130 y
  36131 blancos) pegados. Entra del 280 al 36130. Brillo medido en todos los cuadros: parejo en 188.
- **Dos mosaicos**, como el inicio y el cierre del curso: Víctor a la izquierda (x 38–940) y Jhonatan Sandoval, el
  profesor invitado, a la derecha (x 980–1880), en y 286–794. Víctor presenta (0:14,5–3:27,9), Jhonatan explica el
  enfoque restaurativo (3:29,0–11:21,9) y Víctor recorre las lecciones y cierra (11:24,0–20:02,1). **Sin cortes.**
- **Nombre de la unidad** (PDF del curso): «Unidad 2. Aplicación jurídica de la justicia restaurativa en el proceso penal».
- **Rótulos:** los de dos mosaicos de la base. Víctor en 15,5 s; Jhonatan (nombre solo, `x=1015`) en 31,5 s, cuando
  Víctor lo nombra, y otra vez en 210,0 s, cuando toma la palabra.
- **Cómo se hizo:** `prep_fuente.py`, `profe_cadena.py plan_jru2i componer titulo cartones` (compuesto en 9,5 min; los
  primeros 2,5 son la medida de sonoridad, sin archivo a la vista) y `lote/entrega_gpu.py` (render en 2,2 min; pidió
  5000 kb/s y salió a 5332).
- **Sitio en E:.** D: también estaba lleno (0,8 GB), así que tres grabaciones originales de piezas ya entregadas pasaron
  a **C:** (`C:\DAE_masters_archivo\<misma ruta>\fuente\`, md5 verificado, `LEER - la fuente esta en C.txt` en su
  `01 VIDEO`): las del inicio y el cierre de la U1 de este curso y la del cierre del curso de Bienes (961 MB en total).
  Después de esta entrega: E: 0,37 GB, D: 0,80 GB, C: 12,4 GB.

## Inicio de la unidad 3 (18 nov 2026, noche) — entrega provisional

Sebastián: «continuemos con el inicio de u3, con gráfica provisional, pero revísalo muy bien todo y actualiza todo lo
que haya que actualizar». Fuente: «Justicia restaurativa -  Unidad 3 Inicio.mp4» (`15z_Xy-8qQWaRgp0vTAQnjsMYyNX-vROT`,
403 MB, del 17 nov).

| | |
|---|---|
| entrega | `justiciarestaurativa - U3 - INICIO-v1.mp4` · `1-dyCgrfpuy71YMJUDFdtCCHK_a-Dj72j` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - U3 - INICIO-v1.srt` · `1Hm3rmSlqAMgw0wQ8FsDPCHngOL9cKnTc` (163; ver `../subtitulos/`) |
| medidas | 11:48,1 · 16.977 cuadros = línea · 474.728.502 bytes · H.264 Main a 5,36 Mb/s, BT.709 · −16,1 LUFS, −3,0 dBTP |
| línea | `JR - U3 - INICIO` (proyecto `DAE MASTER - CURSOS`) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\UNIDAD 3\INICIO\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas/_verif jr u3 inicio 18nov` y `verificar_drive.py`: «OK»).

### La fuente no es como las otras

Es la grabación **sin pasar por el editor** (las otras cuatro traían intro y outro pegados y venían etiquetadas BT.601):

- **Sin intro ni outro.** La conversación va del primer cuadro al último (20.842 cuadros, 11:34,8; brillo medido en
  todos; hoja de un cuadro cada 20 s). Entra del cuadro 45 al 20700. Al final quedan fuera 3,5 s de silencio y un
  «Listo, profe» de alguien, ya fuera de la toma.
- **Sin etiqueta de color, y en BT.709.** Se midieron el rojo, el azul y el amarillo del logo de la Fiscalía del
  mosaico de Víctor contra la fuente del cierre de la U1: leída como 709 coincide (rojo 233/66/62 contra 234/65/65);
  leída como 601 el rojo cae a 217/57/71. El plan lleva `MATRIZ_FUENTE = 'bt709'`. Sin eso el video habría salido con
  los rojos apagados.
- **Una raya negra en el borde de arriba** (fila 0 en negro, fila 1 en gris, de lado a lado). `PREFILTRO` pinta esas
  dos filas del blanco del lienzo (`drawbox … color=0xFEFEFE`, que da Y 234, el del lienzo). Ver abajo: **la traen
  también cuatro entregas anteriores**.

### Qué se hizo

- Tres mosaicos, con los mismos bordes que la U1 (medidos). Víctor presenta (0:02,6–1:23,1), habla Jhonatan
  (1:23,9–5:23,3), después Martín (5:26,5–7:44,0) y cierra Víctor (7:46,5–11:29,3). Scribe confunde los hablantes (le
  da a Martín la etiqueta de Víctor): quién habla sale de lo que dicen y de la imagen.
- **Un corte de 14,5 s** (cuadros 18762 a 19197): Víctor se enreda y lo pide («…hemos visto en esto, eh, un, una,
  una, eh… un corte, por favor. Eh, hemos visto en esto, hemos visto en esto una gran motivación»). Queda «…a la
  justicia restaurativa | hemos visto en esto una gran motivación…». Los dos bordes caen en silencio medido (RMS de
  20 ms); la pausa que queda es de 0,36 s (la original, 0,34).
- Se deja «Si me permites, Martín, ¿comienzo yo?» (Jhonatan, al tomar la palabra): es parte de la conversación.
- Título: «Unidad 3. Implementación de la justicia restaurativa» (igual en las dos partes del PDF donde aparece).
- Rótulos: los de tres mosaicos, en 4,0, 84,8 y 327,5 s de la fuente.

### Revisión de la entrega (más larga que las anteriores)

- Contenedor: H.264 Main L4.0, 1920×1080, 23,976, BT.709 etiquetado, AAC 48 kHz estéreo; 16.977 cuadros = línea.
- **Imagen y sonido en su sitio, antes y después del corte.** Sonido: la transcripción de la entrega da cada palabra a
  ±0,1 s de donde debe caer. Imagen: cinco cuadros de la entrega (y cuatro del compuesto) comparados con la fuente por
  diferencia media en la zona de la cara; el mínimo cae en el cuadro esperado o en el de al lado (la cámara repite
  cuadros de a pares).
- Sin cuadros negros (`blackdetect`); filas de arriba en blanco en el título, el cuerpo (antes y después del corte) y
  el cierre; hoja de un cuadro cada 20 s de toda la entrega; tiras de cuadros seguidos en la entrada del cuerpo, el
  corte y la salida; cartón de título y los tres rótulos mirados sobre el compuesto.
- −16,1 LUFS, −3,0 dBTP. Los silencios son los de la serie (cartón de título y cartón de cierre) y dos cambios de
  hablante.

### Lo que la revisión encontró en las entregas anteriores

1. **Raya negra arriba en cuatro videos ya entregados.** La traen las grabaciones del inicio del curso, del inicio y
   el cierre de la U1 y del inicio de la U2 (no la del cierre del curso), y pasó a las entregas: fila 0 en negro y
   fila 1 en gris durante el cuerpo, de lado a lado; en el título y en el cierre no está, así que aparece y desaparece
   en los cortes. Arreglo: `PREFILTRO` en el plan, `ic_pieza reimagen` (rehace la imagen y conserva el audio) y una
   `-v2`. **Pendiente de que Sebastián decida** si salen las cuatro `-v2`.
2. **El nombre de la unidad 1 aparece de dos formas en el PDF del curso.** En la estructura (2.1 y 2.4):
   «Fundamentos, principios y ejes de la justicia restaurativa». En «3.1 Nombre de la unidad No. 1»: «Bases
   conceptuales y marco jurídico de la justicia restaurativa», que es el que llevan los dos cartones de título de la
   U1. Las unidades 2, 3 y 4 se llaman igual en los dos sitios. **Pendiente de confirmar** cuál quiere la DAE.

### Cómo se hizo

`prep_fuente.py`, brillo de todos los cuadros y hoja de la fuente; `profe_cadena.py plan_jru3i componer titulo
cartones` (7 min); `lote/entrega_gpu.py` (render en 1,5 min; pidió 5000 kb/s y salió a 5364). Antes de componer se
probó el filtro en un cuadro por el mismo camino (`ic_pieza.escala`): filas de arriba en 234 y el rojo sin moverse.

**Sitio en E:.** Ocho grabaciones originales más pasaron a `C:\DAE_masters_archivo\` (3,04 GB: Delitos ambientales
U3 L5 y U4 L1; SRPA presentación y cierre del curso, U3 desarrollo y cierre, U5 cierre; Derechos humanos cierre de la
U5). Antes se comprobó, recorriendo los 5.880 clips del media pool, que ninguno apunta a esos archivos, y que cada
uno tiene su compuesto al lado. Después de esta entrega: E: 2,2 GB, D: 0,8 GB, C: 8,7 GB.

## Cierre de la unidad 4 (19 nov 2026) — entrega provisional

Sebastián: «sigamos con el cierre de u4 justicia restaurativa mientras tanto». Fuente: «Justica restuaraativa-
Unidad 4 cierre.mp4» (`1G4PPvI-l50lDGY0ffUOr0Rushskq8MSt`, 191 MB, del 19 nov). El inicio de la U4 había llegado solo
en audio (`.m4a`) y quedó esperando el `.mp4`.

| | |
|---|---|
| entrega | `justiciarestaurativa - U4 - CIERRE-v1.mp4` · `1LT26NnbHAPWaZ5YtB1YJx0ZLn4P2vjf5` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - U4 - CIERRE-v1.srt` · `1Biajmt8kUdwHFIUg5ZcxrfNdfkG4qXwV` (159; ver `../subtitulos/`) |
| medidas | 11:36,3 · 16.693 cuadros = línea · 467.267.915 bytes · H.264 Main a 5,37 Mb/s, BT.709 · −16,1 LUFS, pico −2,4 dBFS |
| línea | `JR - U4 - CIERRE` (proyecto `DAE MASTER - CURSOS`) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\UNIDAD 4\CIERRE\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas/_verif jr u4 cierre` y `verificar_drive.py`: «OK jru4c
467267915»).

- **Fuente** (`plan_jru4c.py`): 1920×1080, 30 fps, 20.144 cuadros (11:11,5), BT.601 etiquetada. Trae la intro pegada
  (0–277) y no trae outro. Tres mosaicos con los bordes de la unidad 1. Entra del cuadro 280 al 20144, **sin cortes**:
  no hay reinicios ni pedidos de corte.
- **La raya negra de arriba** (fila 0 en negro, fila 1 en gris) también viene en esta fuente. Sale con `PREFILTRO`,
  como en el inicio de la U3. En la entrega las filas 0–3 miden 249–250 contra 251 del lienzo (tres cuadros).
- **Nombre de la unidad:** «Plan de justicia restaurativa» (PDF del curso, 2.4).
- **Lower thirds:** Víctor (0:11,5 de la fuente), Jhonatan (2:02,6) y Martín (5:40,9), los de tres mosaicos.
- **Termina sin despedida:** la última frase de Víctor acaba en «…culminar este curso» y hay 0,4 s de silencio hasta
  el final del archivo. Así llegó.
- **Revisión de la entrega:** ocho cuadros (intro, título, los tres rótulos, cuerpo, cierre y outro); sin cuadros
  negros (`blackdetect`); los silencios de más de 2 s son la intro, dos cambios de quien habla, una pausa de Martín y
  el cierre; primera palabra a 17,86 s contra 10,12 s en la fuente (desfase esperado 7,725 s).
- **Cadena:** `prep_fuente.py`, `prep2_jru4c.py` (brillo de todos los cuadros, bordes y mosaicos medidos con PIL,
  turnos de la transcripción), `profe_cadena.py plan_jru4c componer titulo cartones` (componer 454 s) y
  `lote/entrega_gpu.py` (render en 83 s; pidió 5000 kb/s y salió a 5369).
- **Sitio en E:.** Quedaban 2,2 GB. `E:\DAE MASTER\_archivo_tmp` (20,4 GB, 46 archivos, ningún clip del pool) pasó con
  `robocopy /MOVE` a `D:\DAE\_movido_de_E\_archivo_tmp` (0 fallos; nota `LEER` en `E:\DAE MASTER`). Después de esta
  entrega: E: 23 GB, D: 111 GB, C: 6,9 GB.

## Inicio de la unidad 4 (19 nov 2026) — entrega provisional

Sebastián: «ahora volvamos a intentar con justicia restaurativa u4 inicio, ya está con video». Fuente: «Justica
restuaraativa-  Unidad 4 inicio.mp4» (`1q_czi8j8AMRGgv9CZThThXnz67JBiBiE`, 163 MB). El primer enlace había sido el
audio suelto de la misma grabación (`.m4a`); lo que se preparó con él quedó apartado en `D:\DAE\_tmp\jr_p\jru4i_audio`.

| | |
|---|---|
| entrega | `justiciarestaurativa - U4 - INICIO-v1.mp4` · `1eWsux3bkLCb8VP0heqWEI_gHjasLME6r` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - U4 - INICIO-v1.srt` · `1pZkIdR6X3ANEJA8iz45E7mrnYfD3OVse` (124; ver `../subtitulos/`) |
| medidas | 9:16,2 · 13.336 cuadros = línea · 372.504.470 bytes · H.264 Main a 5,36 Mb/s, BT.709 · −16,1 LUFS, pico −2,3 dBFS |
| línea | `JR - U4 - INICIO` (proyecto `DAE MASTER - CURSOS`) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\UNIDAD 4\INICIO\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas/_verif jr u4 inicio` y `verificar_drive.py`: «OK jru4i
372504470»).

- **Fuente** (`plan_jru4i.py`): 1920×1080, 30 fps, 16.330 cuadros (9:04,4), BT.601 etiquetada. Trae pegados la intro
  (0–277) y el outro (desde el 16054). Tres mosaicos con los bordes de la unidad 1. Entra del cuadro 300 al 15964.
- **La raya negra de arriba** viene también; sale con `PREFILTRO`.
- **El final:** Víctor termina «…afronten de la mejor manera esta última unidad.» y arranca una frase que la
  grabación deja cortada («Es un—»). Ese arranque no entra: el tramo termina 0,25 s después de «unidad.», en silencio
  medido. En la entrega la última palabra es «unidad.» (539,14 s) y sigue el cartón de cierre.
- **Dos empalmes del editor de la grabación**, los dos en el silencio entre la pregunta de Víctor y la respuesta de
  Jhonatan: una disolvencia de cinco cuadros en 111,97 s y un corte seco en 112,87 s (los tres mosaicos saltan a la
  vez). En la entrega caen hacia 1:59. Se dejan.
- **Lower thirds:** Víctor (0:12,9 de la fuente), Jhonatan (1:54,1) y Martín (5:11,6).
- **Revisión de la entrega:** ocho cuadros (intro, título, los tres rótulos, después del empalme, final del cuerpo y
  cierre); sin cuadros negros; los silencios de más de 2 s son la intro, un cambio de quien habla y el cierre; primera
  palabra a 18,50 s contra 11,44 s en la fuente (desfase esperado 7,059 s).
- **Cadena:** `prep_fuente.py`, `prep2_jru4i.py`, `dif_u4.py` (diferencia entre cuadros de toda la fuente: así salieron
  los empalmes), `profe_cadena.py plan_jru4i componer titulo cartones` (componer 321 s) y `lote/entrega_gpu.py` (render
  en 71 s).

### Lo que la misma medida encontró en el cierre de la U4, ya entregado

`dif_u4.py` se corrió también sobre la fuente del cierre: trae **dos cortes secos del editor de la grabación**, en
48,6 s y en 120,8 s (los tres mosaicos saltan a la vez; diferencia de 7 a 12 a tamaño completo), los dos en pausas. En
378,3 s y 386,4 s salta solo el mosaico de Martín (su cámara). Nada de eso se puede disimular con tres mosaicos; queda
como llegó.

