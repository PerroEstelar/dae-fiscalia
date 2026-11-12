# Introducción al curso (Delitos ambientales)

Pedido de Sebastián (12 nov 2026): el video de presentación del curso con la
docente de las introducciones de unidad, «con la misma línea», como video de
profe a cámara. Lleva:

- intro y outro;
- cartones de inicio y de salida;
- lower third;
- cartones de apoyo;
- gráficos de After Effects.

Nada puede quedar recortado: ni la marca de agua, ni los textos, ni los clips.

## El material

- **Fuente:** Drive, carpeta del curso → `VIDEOS`, archivo
  `ambiental_inicio_curso.mp4`.
  - Es una grabación de Teams de 3:47,6, 1280×720 a 30 fps.
  - El fondo virtual es el aéreo DAE/Fiscalía, con el logo arriba a la
    izquierda.
  - Para bajarlo se hizo una copia en `_MA subidas` (Mi unidad), que Drive
    sincroniza, y de ahí se copió a disco.
- **Quién habla:** la docente de las introducciones de unidad.
  - Ella dice «Mi nombre es Diana Carolina Flórez Bayona». El lower third dice
    «Diana Carolina Florez Vallona», como el de la U1, que Sebastián confirmó el
    10 nov.
  - Debajo del nombre va lo que ella dice de sí misma: doctora en Derecho,
    magíster en Administración Pública y especialista en Derecho Constitucional.
- **Transcripción:** Scribe, palabra por palabra (`D:\DAE\_tmp\ma\ic\stt_full.json`).
  - Con el mp3 a 44,1 kHz Scribe devolvió basura: 141 «palabras» en chino, ruso
    e inglés.
  - Con un WAV mono a 16 kHz salió bien: 430 palabras, `language_probability` 1,0.
  - Si una transcripción sale rara, mirar `language_probability` y el número de
    palabras antes de usarla.
- **Disco:** `E:\DAE MASTER\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\INTRODUCCION AL CURSO\`,
  con las carpetas 01 VIDEO, 02 CARTONES, 03 VOCES, 05 EXPORTS, 09 MOTION
  GRAPHICS y 10 TIMELINE SEBASTIAN. En Resolve, los mismos bins.
- **Línea:** `MA - CURSO - INTRODUCCION`. Su `.drt` está en `10 TIMELINE SEBASTIAN`.

## Cómo se hizo (`plan_ic.py`, `herramientas/montaje/ic_pieza.py`, `ic_linea.py`)

Es el procedimiento de los videos de profes (`te_pieza`, `te_linea`), con el plan
de este video.

- **Ventana:** 1143×643 desde (0, 30), escalada a 1920×1080 en Rec.709. Así queda:
  - ella a la derecha, con la cabeza desde x≈810–860;
  - la caja de cartones (x 62–790) libre;
  - el logo del fondo virtual entero (x 59–832, y 20–188).
- **Audio:** el v2 de los profes.
  - Cadena: paso alto a 80 Hz, −2 dB en 250 Hz, +3 dB en 3 kHz, compresor 3:1.
  - Después, loudnorm a −16 LUFS con techo de −3 dBTP.
  - El original venía en −27,2 LUFS.
- **Gráficos.** Son 15 en total:
  - el lower third;
  - 10 cartones de caja verbatim: la bienvenida con el nombre del curso, el
    propósito, «Cinco unidades», una por unidad, la invitación y la despedida;
  - 4 listas de After Effects en `MA_intros_mg.aep`, comps `IC_*`: la
    experiencia, la U2 («Con especial atención a»), la U3 y el recorrido.

  Antes de rendir se midió la cima de cada uno:
  - Dos cartones (el propósito y la invitación) se salían de la caja con título.
    Quedaron como una sola frase en mediana.
  - Las listas, con los rótulos enteros, llegaban hasta la y=94. Quedaron con las
    palabras de ella recortadas, y la más alta llega a la y=259.
- **Cartón de título:** se hizo con `titulo_dema` sobre u1v2, con el subtítulo
  «Introducción al curso». El cartón de entrada y el de salida son el mismo
  archivo, y la marca APRENDE CON LA DAE entra entera.
- **Línea:** todo va a 1:1 (zoom 1, pan 0). Ni el cierre ni el outro llevan el
  1,16 / 145 de la plantilla.
  - Cada ítem está en el cuadro y con la duración del plan.
  - El último cartón termina en el 5861 y el clip en el 5866.

## Entrega

- **Disco:** `05 EXPORTS/delitosambientales - CURSO - INTRODUCCION-v1.mov`.
  - Formato: H.264 High, 1920×1080, 23,976.
  - Son 6.275 cuadros, los mismos que la línea, y pesa 189 MB.
  - El audio mide −16,1 LUFS, con pico −2,9 dBTP. No hizo falta el limitador.
  - No hay cuadros negros. Los dos silencios son los cartones de título, como en
    las introducciones.
- **Drive:** curso → `VIDEOS/VIDEOS UNIDADES/videos exportados`, junto a las
  introducciones de unidad.
