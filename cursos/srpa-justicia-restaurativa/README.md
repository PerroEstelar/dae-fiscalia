# Sistema de responsabilidad penal para adolescentes y justicia restaurativa: videos de profes

Prioridad 1. Pedido de Sebastián del 11 nov 2026:

> «necesitamos realizarlos en ese formato, intro, outro, lower thirds, frases más
> relevantes en pantalla, gráfica con aftr… cartón de entrada y de salida con el
> nombre del curso y como subtítulo justo abajo el nombre de la unidad».

El formato es el de las introducciones de Delitos ambientales.

## Los siete videos

La fuente está en Drive, en la carpeta del curso → `VIDEOS/UNIDADES`. Son siete
mp4 de Teams, de 1280×720 a 30 fps, con fondo virtual DAE/Fiscalía. Se miraron y
se transcribieron todos con Scribe (`03 VOCES/stt`) para saber qué es cada uno.

| clave | original | qué es | dura | profe |
|---|---|---|---|---|
| curso | Inicio Curso | presentación del curso | 15:21 | Estanislao Escalante Barreto |
| u1b | Unidad1-presentacion | bienvenida U1 | 8:19* | Estanislao Escalante Barreto |
| u3b | Unidad 3 - presentacion - a | bienvenida U3 | 3:43 | Carlos Humberto Ramírez Romero |
| u3d | Unidad 3 - presentacion - b | desarrollo U3 (una clase completa) | 39:23* | Carlos Humberto Ramírez Romero |
| u3c | Unidad 3 - cierrre | cierre U3 | 11:21 | Carlos Humberto Ramírez Romero |
| u4c | Unidad 4 - cierrre | cierre U4 | 9:01 | Carlos Humberto Ramírez Romero |
| u5c | Unidad 5 - cierrre | cierre U5 | 17:43 | Carlos Humberto Ramírez Romero |

\* Ya con los cortes de abajo.

- La U2 no trae video.
- En disco el curso está en `E:\DAE MASTER\PRIORIDAD 1\CURSO - SRPA Y JUSTICIA
  RESTAURATIVA`: una carpeta por video (`PRESENTACION DEL CURSO`, `UNIDAD n\BIENVENIDA`,
  `UNIDAD 3\DESARROLLO`, `UNIDAD n\CIERRE`), cada una con 01 VIDEO, 02 CARTONES,
  03 VOCES, 05 EXPORTS, 09 MOTION GRAPHICS y 10 TIMELINE SEBASTIAN.
- En Resolve, los mismos bins bajo `CURSO - SRPA Y JUSTICIA RESTAURATIVA`.
- Los nombres de las líneas son `SRPA - U3 - CIERRE`, etc.

**Nombre del curso:** «Sistema de responsabilidad penal para adolescentes y
justicia restaurativa», con mayúscula solo en la primera palabra. Es el mismo
criterio que Sebastián fijó para Delitos ambientales: el sistema de
responsabilidad penal para adolescentes es un nombre genérico, no un título. Los
nombres de las unidades salen de la ficha del curso y siguen la misma regla.

## Composición (`herramientas/montaje/srpa_composicion.py`)

- Se toma una ventana de 1143×643 de la fuente (×1,68) desde x=12. Así el profe
  queda a la derecha, con la cara desde x≈770, y a la izquierda queda libre la
  caja de cartones (x 62–790, y 250–720), como en Delitos ambientales.
- Se va también el filete blanco de 10 px que trae el fondo virtual del edificio.
- En el fondo aéreo (u3b, u3d) la ventana empieza en y=30, porque ahí el profe
  está más abajo y el logo más arriba.
- Rec.709 etiquetado. Audio a −19 LUFS con una ganancia fija medida en el
  original, más un limitador a −1,5 dBFS, porque los originales traen picos sobre 0.
- **Cortes:**
  - **u1b:** a los 4:17 el profe dice «Corta ahí ese último minutico y volvemos
    a empezar». Se quitó de 256,55 a 277,10 s, en las pausas. Lo que sigue va
    acercado (×2,09) hasta la pausa de 303,8 s, para que el salto se lea como
    cambio de plano.
  - **u3d:** termina en «Muchas gracias.». Después venía la charla con el técnico
    («Profe, ¿me escucha?»).

## Gráficos (`plan_srpa.py`)

Los tiempos están en segundos de la fuente, y `srpa.a_salida` descuenta los
cortes. Los textos son verbatim de lo que dice el profe. De la ficha del curso
solo se toman:
- los nombres oficiales de las unidades;
- la grafía de los nombres propios (Manuel Enrique López Betancur, Gabriela
  Rodríguez Beltrán);
- el texto oficial de las reglas de Beijing que el profe lee en la U3.

| tipo | herramienta | dibujo |
|---|---|---|
| cartón de caja | `cartones_srpa.py` (usa `cartones_ma`) | el de las introducciones de Delitos ambientales |
| lower third | `cartones_srpa.py` | el de la U1 de Delitos ambientales (barra amarilla, nombre Bold 48, cargo Medium 27), abajo a la izquierda |
| tarjeta y lista de AE | `herramientas/motion/mg_srpa.py` (usa `mg_ma`), por aftr | el de los motion graphics de Delitos ambientales; la tarjeta y la lista pueden ir sin título |
| cartón de título | `herramientas/cartones/titulo_srpa.py` | el cartón de Delitos ambientales con el nombre del curso en dos líneas y la unidad debajo, en Regular 44, cortada en renglones equilibrados; es uno por unidad y uno del curso |

- Las tarjetas y listas de AE están en `00 MOTION GRAPHICS/SRPA_mg.aep`.
- Los íconos nuevos son 27, en las hojas E, F y G de Magnific
  (`herramientas/motion/iconos_srpa.py`). Además se reusan los de Delitos
  ambientales.

## Línea (`herramientas/montaje/srpa_linea.py`)

El esqueleto es el del conversatorio DEMA y DECOC:
- intro FGN 0–194 y cartón de título 194–409;
- el clip desde el 409;
- el cartón de cierre y el outro, con zoom 1,16 y pan 145;
- las pistas V2 CARTONES, V3 MOTION GRAPHICS y V4 LOWER THIRD.

**Entrega:** `05 EXPORTS/srpa - U3 - CIERRE-v1.mov`, con los ajustes de la serie
(mov H.264 High, tope de 6.000 kb/s, AAC 48 kHz).

## Ronda 2 (11 nov 2026, la tarde)

Sebastián: «los cartones de salida, la marca de agua hacia el final y el outro,
todo está como si se hubiera ampliado… y siento que la voz de los profes está
débil».

- **Cierre y outro a 1:1.** El zoom 1,16 con pan 145 venía de la plantilla
  (`MA - U1 - INTRODUCCION`) y recortaba el título de cierre, la marca APRENDE CON
  LA DAE y el outro FGN. Se dejaron en zoom 1, pan 0 en las siete líneas, y
  `srpa_linea.py` ya no lo aplica.
- **Audio v2** (`herramientas/montaje/srpa_audio.py`). Se rehace desde el
  original con:
  - paso alto a 80 Hz;
  - −2 dB en 250 Hz;
  - +3 dB en 3 kHz;
  - compresor de 3:1 con el umbral en −26 dB;
  - loudnorm en dos pasadas a −16 LUFS, con techo de −1,5 dBTP.

  El LRA bajó de unos 6,5 LU a unos 3. El compuesto v2 lleva el mismo video,
  copiado, y entra en la línea con `ReplaceClip`.
- **Exports v2.** Se revisaron con hojas que incluyen tres cuadros del cierre y
  tres del outro. Se subieron a las mismas carpetas de Drive y los v1 se mandaron
  a la papelera.

## Casos (12 nov 2026)

Además de los videos de profes, el curso tiene casos narrados con la receta de
los cursos de casos: voz de ElevenLabs, placas de Magnific, Kling, cartones
verbatim y listas de After Effects. Van en su unidad, al lado de los videos de
profes.

- **Caso Nico** (U1, principio de culpabilidad): `casos/nico/README.md`.
  Receta: `herramientas/montaje/sr_pieza.py`.

## Inicio y cierre del curso (13 nov 2026)

Sebastián pidió «el video de inicio y cierre de curso srpa», con el formato de
profe a cámara y en la misma línea.

### Inicio

Es el mismo `Inicio Curso.mp4` del 11 nov (mismo archivo, 368.437.056 bytes):
la presentación del curso, que ya estaba hecha. Se había entregado como
`srpa - CURSO - PRESENTACION-v2.mov`. Sebastián eligió reentregarlo en MP4.

- La línea `SRPA - CURSO - PRESENTACION` se revisó antes de rendir:
  - el compuesto v2, sin medios fuera de línea;
  - V1 entera a 1:1;
  - ningún gráfico con zoom.
- Se rindió con `herramientas/montaje/mp4_entrega.py`, que es `ic_mp4` sin plan:
  la línea, la carpeta y el nombre van por argumento. El máster midió −1,4 dBTP,
  así que el audio se copió.

### Cierre (`cc`)

- **Fuente:** Drive, curso → `VIDEOS/UNIDADES/srpa-cierre-curso.mp4`.
  - Formato: 7:25, 1280×720 a 30 fps, AAC 44,1 kHz dual-mono a −18,9 LUFS.
  - Profe: Estanislao Escalante Barreto («les habló en este caso Estanislao
    Escalante»).
  - Transcripción: Scribe sobre WAV a 16 kHz. Son 1.165 palabras, una sola voz.
  - Disco: `CIERRE DEL CURSO\` con las carpetas de siempre.
- **Ventana propia.** El profe está centrado y cerca de la cámara.
  - Se midió en 178 cuadros, con el fondo calculado como la mediana. El borde
    izquierdo de la cabeza va de x 416 (p2) a 470 (p50), y los hombros empiezan
    en y≈460.
  - Con la ventana de los otros videos (1143×643 desde x=12) la cabeza entraba
    en la caja.
  - Va 1024×576 desde (0, 40), ×1,875. La cabeza queda desde x≈810 y los hombros
    bajo y=720.
  - Este fondo no trae el filete blanco. El panel DAE/Fiscalía entra entero.
- **Audio v2** (`srpa_audio.py`): −16,0 LUFS, pico −1,5 dBTP, LRA 2,1.
- **Cartón de título:** «Cierre del curso» (`titulo_srpa.py cc`), en
  `carton titulo srpa cierre curso.mp4`.
- **Gráficos.** Son 27 y cubren el 68 % de la caja:
  - 2 lower thirds;
  - 16 cartones verbatim, a 9–15 car/s, con la cima en 385 o más;
  - 9 tarjetas y listas de AE.
- **Medición antes de rendir.** Las listas se midieron primero. Cuatro se subían
  de la zona:
  - la del segundo lugar, a 236;
  - «Hemos encontrado», a 249;
  - la de justicia restaurativa, a 39;
  - la del hurto de comida, a 204.

  Quedaron entre 259 y 401, sin título o con sus palabras recortadas.
- **AE:** si After Effects no está abierto, se arranca solo `AfterFX.exe` y se
  espera a que cargue. Después se manda `ae_abrir.jsx` con `-r`, y por último
  se levanta el controlador de aftr (`node controller/src/server.js` en
  `C:\Users\call_\aftr`), y el panel se conecta solo.
  - Lanzar `AfterFX.exe -r script` con AE cerrado lo dejó colgado y se cerró
    sin abrir el proyecto.

### Entregas (MP4, receta del 23 oct, `mp4_entrega.py`)

| archivo | cuadros | sonido | pico | PSNR medio / mínimo | peso |
|---|---|---|---|---|---|
| `PRESENTACION DEL CURSO/05 EXPORTS/srpa - CURSO - PRESENTACION-v2.mp4` | 22.903 = línea | −16,0 LUFS | −1,4 dBTP | 49,2 / 44,2 dB | 641 MB |
| `CIERRE DEL CURSO/05 EXPORTS/srpa - CURSO - CIERRE-v1.mp4` | 11.494 = línea | −16,1 LUFS | −1,5 dBTP | 48,6 / 44,2 dB | 390 MB |

- **Audio:** en las dos se copió del máster, porque no pasaba de −1 dBTP.
- **Cierre, hojas de revisión** (`D:\DAE\_tmp\srpa\rev\cc.jpg` y `cc_zoom.png`):
  - En los recortes a tamaño real, el texto termina en x≈773 y la cara empieza
    en x≈840–920.
  - El título «Cierre del curso» y el outro entran enteros.
  - No hay cuadros negros. Los silencios son los dos cartones de título.
- **Cierre, línea:** `SRPA - CURSO - CIERRE`, con su `.drt` en `10 TIMELINE SEBASTIAN`.
- **Drive** (curso → `VIDEOS FINALIZADOS`):
  - el inicio, en «presentación del curso». El `.mov` v2 se mandó a la papelera,
    y en disco quedó en `05 EXPORTS/_descartes`;
  - el cierre, en la carpeta nueva «cierre del curso».
- **`srpa_revision.py`:**
  - lee el MP4 si existe;
  - el último cuadro del outro pasó a +180, porque con un `-ss` en los últimos
    cuadros ffmpeg no devuelve nada;
  - si falta un cuadro, la hoja lo salta.

## Los que llegaron después: cierre de la U1 y unidad 2 (17 nov 2026)

Del inventario de SRPA, Ley 1826 y Terminaciones anticipadas salieron tres piezas de profe con
la grabación en Drive (VIDEOS/UNIDADES) y sin producir. Sebastián: «empieza con lo que falta
del material que tenemos pero no se lo hemos producido, cada uno excelentemente hecho siguiendo
todos los protocolos, de pe a pa, los dejas subidos y actualizas el inventario».

Van por `ic_pieza` con planes en `profe/` (`base_sr_profe.py`), como los profes de Derechos
humanos, y no por `sr_pieza`/`plan_srpa.py`. E: no tiene espacio: el árbol está en
`D:\DAE MASTER\PRIORIDAD 1\CURSO - SRPA Y JUSTICIA RESTAURATIVA\`, con un `LEER` en las carpetas
`UNIDAD 1` y `UNIDAD 2` de E:. El proyecto de AE es el de siempre (`SRPA_mg.aep`, en E:).

### Cierre de la unidad 1 (`plan_sr1c`) — entregado

- **Fuente:** `Unidad 1 - cierre.mp4` (`18Gdlyg_7e0q_6stYaBnG48pSAENnca9A`, subida el 12 nov),
  16:55,7. Estanislao Escalante Barreto, con el fondo y el encuadre del cierre del curso. Copia
  de trabajo: `UNIDAD 1\CIERRE\01 VIDEO\srpa_u1_cierre_fuente.mp4`.
- **La lámina.** Del 5:45 al 13:49 comparte una diapositiva («La visión multidimensional del
  SRPA. Una apuesta para su comprensión») y él queda en una miniatura. Ese tramo va a cuadro
  completo y sin gráficos. Las dos transiciones de Teams se tapan con un cuadro quieto de la
  lámina (`CONGELA`; a la salida, con 'antes'): se ve un corte seco del profe a la lámina y de
  la lámina al profe, y nunca se congela su cara. Los cuadros están en el plan.
- **Ventana:** 1088×612 desde (0, 44), ×1,765, columna de 470.
- **Gráficos:** solo en los dos tramos del profe (0–5:45 y 13:49–16:55): 62 % de ese tiempo.
- **Línea:** `SRPA - U1 - CIERRE`. **Entrega:** `srpa - U1 - CIERRE-v1.mp4`, en Drive →
  `VIDEOS FINALIZADOS` › «unidad 1» (`1mKRysBB50QhE1xAb4cDjaIXQKxXV8Gy7`), id
  `1x_xkiDoDt_XmWAPpUr9Zy1xhC-4fvmaB`. 25.169 cuadros = línea; −16,0 LUFS, −2,9 dBTP; PSNR 50,3 /
  43,8 dB contra el máster; 592 MB. Subida con copia exclusiva y verificada byte a byte.
- **Lower third:** el cargo de Estanislao es largo. Con la columna de 470 se había puesto a 440 de
  ancho y daba cinco renglones: el último se salía del cuadro. Se vio en la simulación. A 560 son
  tres, parejos (`LT = (40, 560)` en el plan), y queda sobre el saco, lejos de la cara.
- **Compuesto v2:** la v1 llevaba la lámina a 1280×720 completo y arriba se veía la raya negra
  de 1 px que Teams deja en y=0. La v2 usa la ventana 1276×718 desde (0, 2); solo se rehízo la
  imagen (`ic_pieza reimagen`). La v1 está en `01 VIDEO\_descartes`.
- Simulación y cortes: `D:\DAE\_tmp\sr_ta\sr1c\sim\` y `corte_entra.jpg`, `corte_sale.jpg`,
  `e_cortes.jpg` (los dos cortes en la entrega).

### Unidad 2: bienvenida y cierre — **en pausa**

Sebastián (17 nov): «lo más probable es que alguien más me va a enviar los videos con el fondo
adecuado, pausemos esos». No se produjo nada. Lo que quedó medido, por si llegan iguales:

- **Fuentes** (subidas el 11 nov): `Unidad 2 - presentacion.mp4`
  (`1qsD7ZqT7FroRDFYu9XUx1T1hZW_egdVv`, 5:00,8), `Unidad 2 - A.mp4`
  (`1ScxZx8j2XjvxNlfPgPCh4JPQjC5PAbHR`, 12:47,1) y `Unidad 2 - B.mp4`
  (`1JyVnQURMPVQLQzbe9mUKU5l18fjVFaFP`, 15:40,1). A y B son el cierre de la unidad, en dos
  partes; se decidió entregarlas como un solo video.
- **Profe sin identificar.** No dice su nombre en ninguna de las tres. Es otro profe (pelo cano,
  bigote, camisa de cuadros), grabado con cámara contra una pared blanca, sin el fondo virtual.
  Sebastián pidió armarlo sin lower third hasta confirmar el nombre.
- **Las dos partes unidas sin recodificar el video:**
  `UNIDAD 2\CIERRE\01 VIDEO\srpa_u2_cierre_A+B_fuente.mov` (D:). El video se copia con el
  demuxer `concat` (`duration 767.133333` para la parte A, que son sus 23.014 cuadros) y el
  audio va en PCM, con el de A recortado a esa misma duración. 51.217 cuadros a 30 fps exactos.
  Verificado con `framemd5`: los cuadros de la costura, del medio y del final son idénticos a
  los de las fuentes.
- **Canto de un tablero** arriba a la izquierda (x 0–49, y 0–326 según la toma). Se borra con
  `PREFILTRO = 'pad=iw+2:ih+2:2:2:color=0xF6F6F3,delogo=x=2:y=2:w=54:h=334,crop=iw-2:ih-2:2:2'`:
  el borde de 2 px del color de la pared hace que `delogo` interpole desde pared y no desde el
  tablero (con `delogo` solo quedaba una raya).
- **Texto azul noche** (`TINTA = (7, 34, 75)`, sin sombra, íconos teñidos con otro prefijo en
  AE): el blanco de la serie no se lee sobre una pared blanca. Está en `ic_pieza.ajustes` y
  `mg_ma`; no se llegó a usar.
- **Ventana pensada:** 1067×600 desde (0, 0), ×1,8, columna de 470.

Transcripciones (Scribe) y medidas: `D:\DAE\_tmp\sr_ta\` (`u2p`, `u2a`, `u2b`).

## Unidad 4: inicio y desarrollo (17 nov 2026)

Sebastián: «llegó U4 SRPA, por favor revísalo en la carpeta del Drive, ahí está el material en
crudo; procésalo con todo nuestro protocolo, súbelo y actualiza el Excel».

En VIDEOS/UNIDADES había dos archivos nuevos del 17 nov:

| archivo en Drive | id | qué es |
|---|---|---|
| `SRPA_unidad_4_inicio_v2.mp4` | `1lDPp4niSdZZ1th82hPZfZOmxcn6S3x02` | 33:33,8 (60.414 cuadros). La bienvenida de la unidad y la clase, pegadas |
| `SRPA_unidad4_inicio_.mp4` | `1wRxW_FCMNuuBMl--NuOG7KD8Ses0z8JB` | 1:57,4 (3.522 cuadros). Solo la bienvenida: son los primeros 3.522 cuadros del otro |

Grabación de Teams, 1280×720, 30 fps parejos, BT.601, AAC estéreo a −13,0 LUFS con picos de
+1,5 dBTP (`componer` la deja en −16 LUFS y −3 dBTP). **Carlos Humberto Ramírez Romero**: el
fondo aéreo, el saco y la corbata son los de la presentación y el desarrollo de la unidad 3 (se
puso un cuadro de cada fuente al lado). No dice su nombre.

**Son dos piezas, como en la unidad 3** (`presentacion - a` y `presentacion - b`). Sebastián lo
confirmó a mitad del trabajo: «continúa con los dos».

- **Inicio** (`plan_sr4b`), cuadros 0–3521: «Queridos discentes, sean ustedes bienvenidos a
  la unidad número cuatro… Vamos adelante con esta unidad». Se subió como BIENVENIDA y Sebastián
  pidió el cambio: «cambia el nombre a inicio, siempre serán inicio y cierre». La entrega, el
  máster y la línea se llaman INICIO; la carpeta y el bin siguen siendo `UNIDAD 4\BIENVENIDA`.
- **Desarrollo** (`plan_sr4d`), cuadros 3570–60389: la clase de las cuatro lecciones («Sean
  ustedes bienvenidos, queridos discentes, a nuestra unidad número cuatro… Finalizamos unidad
  número cuatro»). La ficha no lo pide (pide la presentación y el cierre de cada unidad); vino en
  la misma grabación y se hizo igual, como el desarrollo de la unidad 3.

Copia de trabajo de la fuente: `UNIDAD 4\BIENVENIDA\01 VIDEO\` y `UNIDAD 4\DESARROLLO\01 VIDEO\`
(`srpa_u4_inicio_v2_fuente.mp4`), en D:. La transcripción (Scribe, 4.183 palabras) está en
`03 VOCES\stt_u4_inicio_v2.json`.

### La fuente ya venía montada con tomas

Se midió cuadro a cuadro (`D:\DAE\_tmp\sr_ta\prep_u4.py`): diferencia media contra el cuadro
anterior, diferencia del panel DAE/Fiscalía contra su mediana y fracción de píxeles oscuros.

- **Corte seco en el cuadro 3522** (117,4 s), entre la bienvenida y la clase. El panel cambia de
  nivel contra su mediana (2,5 → 0,8): son dos tomas con el fondo virtual un pelo corrido. Es
  la frontera entre las dos piezas.
- **Un cubo 3D**, cuadros 23181–23210 (772,7–773,7 s), en una pausa. `CONGELA` muestra quieto el
  primer cuadro limpio de después (el 23212).
- **Cuatro cortes secos a mitad de frase** (un pico aislado de la diferencia, con la cabeza en
  otro sitio): cuadros 24199, 48933, 51964 y 60291. Después de cada uno va el **plano cerrado**
  (960×540, ×2,0) hasta la pausa del final de la frase: 5,6 s, 10,2 s, 4,9 s y 3,3 s. Ahí no hay
  gráficos. Los tres primeros van desde (20, 34), con el panel entero; el último, desde
  (140, 146), sin el panel (ver «Compuesto v2»).
- **Un quinto corte**, en el cuadro 29134 (971,13 s), casi no desplaza la imagen (diferencia 3,5
  contra 5,5–8,9 de los otros): se deja.
- El plano cerrado no puede dejar afuera el panel: en dos de los tramos la cabeza llega hasta
  y=148 de la fuente y el panel termina en y=142. Se midió el tope y los bordes de la cabeza en
  cada tramo (`cerrado_u4.py`) antes de elegir la ventana.

Cómo se buscan: un cubo se ve en el panel (sube de 0,4 a 95); un corte seco no mueve el panel,
y hay que buscar picos aislados de la diferencia entre cuadros (un cuadro alto con los diez de
antes y los diez de después bajos). Los escalones chicos del panel (0,1) no son cortes.

### Ventana y columna

1143×643 desde (12, 30), ×1,68: la de la presentación y el desarrollo de la unidad 3. El borde
izquierdo de la cabeza está en x 588 (p50), 521 (p5) y 453 (p1) de la fuente. Con la caja de
cartones en x 86–750 de salida, la persona pasa del 1,5 % de la caja 12,5 s en los 33 minutos
(manos, de a medio segundo): la columna es de **560** (`MAXW = columna(560)`). Lower third con el
nombre a 44 px y el cargo en 2 renglones (`LT = (44, 560)`); el nombre termina en x≈918, sobre
el saco.

### Inicio (`plan_sr4b`) — entregado

- Una sola toma, de corrido: va entera (0–117,4 s). 8 gráficos: lower third, una lista de AE y
  seis cartones (las cuatro lecciones, el acompañamiento docente y la metodología).
- **Línea:** `SRPA - U4 - INICIO`. **Entrega:** `srpa - U4 - INICIO-v1.mp4`, en Drive →
  `VIDEOS FINALIZADOS` › «unidad 4» (`1f5FchtGdFOwvWtYT8xvILlyamEwloNQb`), id
  `18BwbBy2u8kvD8jrlykTBA_ZjfWymFs8x`. 3.632 cuadros = línea; −16,3 LUFS, −3,0 dBTP; PSNR 51,1 /
  45,0 dB contra el máster; 63,9 MB. Subida con copia exclusiva y verificada byte a byte.

### Desarrollo (`plan_sr4d`) — entregado

- 31:34 de clase. 109 gráficos: lower third, 87 cartones y 21 listas de AE; 68 % del tiempo.
  Ningún gráfico cruza un borde de tramo ni cae en un plano cerrado. En 1.399 s el profe abre
  las manos y una pasa 0,7 s por detrás del cartón «Prácticas formales»: se dejó, porque correr
  el cartón lo sacaba de las palabras.
- **Compuesto v2.** El último plano cerrado («Finalizamos unidad número cuatro») iba con la
  ventana de los otros tres y cortaba el mentón: en esa toma el profe está más abajo y al final
  se inclina. Se vio en la tira de 4 cuadros por segundo de la simulación, con el compuesto de
  31 minutos ya hecho. La v2 usa 960×540 desde (140, 146) para ese plano. No se recompuso todo:
  la v1 tiene un cuadro clave justo en el corte (el 56721 del compuesto), así que se
  codificaron solo los 99 cuadros finales con la misma receta y se pegaron a los primeros 56.721
  de la v1 sin recodificar; el audio es el de la v1 (`D:\DAE\_tmp\sr_ta\cola_sr4d.py`).
  Verificado: SPS/PPS iguales, 56.820 cuadros y 1.894,000 s en video y audio, `framemd5` igual a
  la v1 antes del empalme y a la cola suelta después, decodificación completa sin errores. La v1
  está en `01 VIDEO\_descartes`.
- **Compuesto:** −16,0 LUFS, −2,9 dBTP.
- **Línea:** `SRPA - U4 - DESARROLLO`, 46.228 cuadros. **Entrega:** `srpa - U4 - DESARROLLO-v1.mp4`,
  en Drive → `VIDEOS FINALIZADOS` › «unidad 4», id `1hTtylD5IrNH3FtrswmucVNWPTlniGIzW`. 46.228 cuadros = línea (32:08); −16,0 LUFS,
  −2,6 dBTP; PSNR 50,3 / 45,0 dB contra el máster; 936 MB. Subida con copia exclusiva y
  verificada byte a byte.
- Simulación, tiras de los cortes y de los planos cerrados: `D:\DAE\_tmp\sr_ta\sr4d\sim\`,
  `cortes_compuesto.jpg` (los cuatro cortes en el compuesto, cuadro a cuadro) y `cola_v2.jpg`.

### Cómo se hizo más rápido

`profe_cadena` hace los pasos en fila y componer 31 minutos tarda media hora. Se mató solo el
proceso de la cadena cuando `componer` ya escribía el `.parcial` (el hijo sigue y termina solo)
y, mientras tanto, corrieron `cartones_solo.py` (título y cartones) y `mg_solo.py` (After
Effects), los dos en `D:\DAE\_tmp\sr_ta\`. Las 21 listas se armaron en 147 s, sin cortes de
aftr, y se rindieron en 17 minutos.
