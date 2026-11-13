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
