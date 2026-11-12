# Delitos contra el medio ambiente: introducciones de unidad (MA)

> La **introducción al curso** (la presentación del curso con la misma docente,
> 12 nov 2026) está en `introduccion_curso/`: línea `MA - CURSO - INTRODUCCION`,
> export `delitosambientales - CURSO - INTRODUCCION-v1.mov`.

Son cinco videos. En cada uno, la docente (Diana Carolina) presenta su unidad a
cámara. Las líneas están en Resolve: proyecto `DAE MASTER - CURSOS`, bin
`CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/UNIDAD n`, con el nombre
`MA - Un - INTRODUCCION`.

## El molde: la U1 como la dejó Sebastián (10 nov 2026)

Sebastián pidió que la U2 a la U5 «queden todo como el video de introducción que
ya hicimos para la unidad 1». La U1 queda así:

| Pista | Contenido |
|---|---|
| V1 | Intro FGN 0–194, clip de la unidad desde el 409, cartón de título de cierre al final del clip (zoom 1,16, pan 145) y outro FGN (el mismo clip del intro, zoom 1,16, pan 145) |
| V2 `CARTONES` | Cartón de título `carton titulo ambientales unv3.mp4` 194–409, y encima los cartones de caja (cartones_v3: barra amarilla, texto blanco Montserrat a la izquierda) |
| V3 `MOTION GRAPHICS` | En la U1 está vacía. De la U2 a la U5 lleva las composiciones de After Effects |
| V4/V5 | Lower third «Diana Carolina Florez Vallona» 413–569 (Text+ y Text) |
| A1 | Audio del intro, del clip y del outro. No lleva música ni marca de agua |

El 10 de noviembre el intro y el outro de la U1 estaban *offline*: los ítems de la
línea habían perdido su MediaPoolItem. Se reenlazaron desde el clip del pool y se
repusieron el zoom y el pan del outro. Antes se guardó un respaldo, la línea
`ZZ respaldo antes de reenlazar intro - MA - U1 - INTRODUCCION`.

## U2–U5

- **Plan** (`plan_intros.py`): todos los cuadros son de línea, porque el clip
  empieza en el 409. Los textos salen de la transcripción palabra por palabra
  de cada clip (Scribe, `UNIDAD n/03 VOCES/stt`). Se corrigieron la puntuación
  y las mayúsculas, y no se agregó nada que ella no diga. Lo que hay en
  pantalla cubre entre el 61 % y el 66 % del clip. Los cartones de lecciones
  y actividades van verbatim.
- **Cartones de caja**: `herramientas/cartones/cartones_ma.py` dibuja los ítems
  `carton`. Salen en `UNIDAD n/02 CARTONES/v3/MA_Un_<clave>.mov` (qtrle con
  alfa, 23,976).
- **Cartón de título** `carton titulo ambientales u{1..5}v3.mp4`. Lo pidió
  Sebastián el 10 nov: el nombre del curso va en minúscula salvo la primera palabra,
  «Investigación y judicialización de delitos contra el medio ambiente y los
  recursos naturales». El subtítulo «Introducción Unidad n» no cambia.
  - Del cartón original `u1v2` no hay proyecto fuente en disco. Por eso
    `herramientas/cartones/titulo_ma_v3.py` lo rehace sobre sus propios cuadros:
    conserva el fondo, la barra, la marca y el subtítulo de cada `unv2` (el dígito
    viene de `titulo_ma.py`), borra la zona del título y lo vuelve a escribir.
  - El título reescrito va palabra por palabra, con la animación medida en el
    original. Fuente: Montserrat Bold 68, color (11, 54, 78), una máscara por
    línea.
  - Entrada: una palabra cada 4,5 cuadros, con la curva 41/25/16/10…
  - Salida: sube y sale por arriba, una palabra cada 1/3 de cuadro.
  - En el pool se cambió con `ReplaceClip` al archivo nuevo, así que los ítems
    conservan su sitio y su zoom y pan.
- **Motion graphics** (`herramientas/motion/mg_ma.py`): se hacen en After
  Effects a través de aftr (REST `127.0.0.1:8787`). El proyecto es
  `00 MOTION GRAPHICS/MA_intros_mg.aep`, con una composición
  `MA_Un_<clave>` por ítem. Se rinden con aerender («High Quality with Alpha»,
  ProRes 4444 premultiplicado) a `UNIDAD n/02 CARTONES/mg/`. Siguen el
  lenguaje de los cartones: la misma barra, la misma tipografía, la misma
  sombra y la misma zona (la parte de arriba nunca pasa del y=250). Hay dos
  tipos:
  - `mg_lista`: un título y filas de ícono + rótulo. Cada fila entra con un
    pop del ícono en el cuadro en que ella nombra la cosa (macrocriminalidad,
    procedimientos, participación, reparación, mecanismos de terminación).
  - `mg_act`: la tarjeta de cada actividad, con el ícono a la izquierda de
    «Actividad n» (en pop), el título en negrita y el cuerpo.
  - Los íconos son blancos de línea, hechos en Magnific (nano-banana-2-flash).
    Están en `00 MOTION GRAPHICS/iconos`, 512 px RGBA, y sus hojas en
    `iconos/hojas`.
- **Montaje** (`herramientas/montaje/ma_intros.py`, dentro de `run_inline`):
  `construir(u)` duplica la U1 (y con eso hereda el lower third), le cambia
  V1/V2/V3/A1 por lo de la unidad y deja la línea en su bin. La línea vieja de
  cada unidad pasa a llamarse «… (primera pasada)». `importar(u)` sube el
  cartón de título y los cartones a `UNIDAD n/02 CARTONES`, y los MG a
  `UNIDAD n/05 MOTION GRAPHICS` (con *Alpha mode* Premultiplied).

En `AppendToTimeline`, el `endFrame` del outro es 194 y no 193. Con 193 la
línea queda corta por un cuadro, como pasó en la primera corrida de la U2.

Apellido del lower third: «Florez Vallona», como en la U1. Lo confirmó Sebastián
el 10 de noviembre, aunque en los clips suena «Bayona». Las cinco líneas lo
heredan de la U1.

## Entrega (10 nov 2026)

Las exportó con el mismo formato que la U1 que había entregado Sebastián
(`delitosambientales - U1 - INTRODUCCION-v2.mov`). Después del cambio de nombre
del curso se volvieron a exportar las cinco como **U1 v3 y U2–U5 v2**. En Drive
se mandaron a la papelera las versiones anteriores (U1 v1 y v2, U2–U5 v1), para
que no se confundan con las nuevas:

- QuickTime H.264 High, 1920×1080, 23,976 fps, tope de 6.000 kb/s, AAC 48 kHz estéreo.
- Archivos `UNIDAD n/05 EXPORTS/delitosambientales - Un - INTRODUCCION-v1.mov`.
- Subidas a Drive: carpeta del curso → `VIDEOS` → `VIDEOS UNIDADES` → `videos exportados`,
  donde ya estaban la v1 y la v2 de la U1.

| | cuadros | sonoridad | pico |
|---|---|---|---|
| U2 | 8370 | −19,1 LUFS | −1,1 dBTP |
| U3 | 8010 | −19,5 LUFS | −1,4 dBTP |
| U4 | 9072 | −19,0 LUFS | −0,6 dBTP |
| U5 | 8386 | −19,1 LUFS | −0,7 dBTP |

**Los clips de la docente no llegan todos al mismo nivel.** Medidos en crudo:

| | sonoridad | pico |
|---|---|---|
| U1 | −19,0 LUFS | −0,8 dBTP |
| U2 | −17,2 LUFS | +0,7 dBTP |
| U3 | −21,1 LUFS | −2,7 dBTP |
| U4 | −18,9 LUFS | −0,8 dBTP |
| U5 | −17,2 LUFS | +0,3 dBTP |

La U1 se entregó sin tocar el nivel. Para que las otras quedaran como ella, se hizo
una copia del clip con ganancia fija:

- U2: −1,8 dB.
- U3: +1,7 dB. No llega a +2,1 para no pasar de −1 dBTP.
- U5: −1,8 dB.

Las copias se llaman `Introduccion_delitos_ambientales_unidad-n_nivel19.mp4` y
tienen el video copiado tal cual y la misma duración. Reemplazaron al clip en V1/A1
de las líneas nuevas, en el cuadro 409 y con el mismo final. La U4 quedó como
venía. Los primeros renders de U2, U3 y U5 con el nivel crudo están en
`05 EXPORTS/_descartes`. El de la U2, que llegó a copiarse a la carpeta de subida,
está en `D:/DAE/_tmp/ma/_descartes`.

