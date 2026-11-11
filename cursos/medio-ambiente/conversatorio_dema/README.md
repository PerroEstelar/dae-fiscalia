# Conversatorio «Articulación DEMA y DECOC» (Unidad 1)

En el video conversan dos fiscales en pantalla dividida, grabados por Teams:

- a la izquierda, **Ana María Díaz González** (DEMA);
- a la derecha, **Camilo Andrés González López** (DECOC).

Dura 19:20. La introducción de la Unidad 1 lo anuncia como «un conversatorio
institucional con la DEMA». Lo pidió Sebastián el 11 nov 2026: «incluir intro,
outro, las frases más destacadas, los lower thirds presentando a los dos
interlocutores… que queden como los otros videos de la profe de delitos
ambientales».

- Fuente: Drive, carpeta del curso → `VIDEOS/VIDEOS UNIDADES`, archivo
  `Video articulación DEMA y DECOC`. Pesa 145 MB y es 1280×720 a 30 fps.
- Disco: `UNIDAD 1/CONVERSATORIO - Articulacion DEMA y DECOC/`, con las carpetas
  01 VIDEO, 02 CARTONES, 03 VOCES, 05 EXPORTS, 09 MOTION GRAPHICS y
  10 TIMELINE SEBASTIAN, y los mismos bins en Resolve.
- Línea: `MA - U1 - CONVERSATORIO DEMA Y DECOC`, en `10 TIMELINE SEBASTIAN`.

## La composición

La grabación son dos mosaicos de 640×360 lado a lado, con franjas negras arriba
y abajo y los rótulos de Teams al pie. `herramientas/montaje/dema_composicion.py`
la rehace en 1920×1080:

- Fondo **azul institucional #002048, plano y sin degradé**. Es el «noche»
  medido en el intro FGN. Sebastián ya había rechazado un azul que no era el
  institucional y con degradé.
- La franja de los dos mosaicos a 1,5× en y=140.
- Abajo queda una banda de 400 px (y 680–1080) para los gráficos. Así no se
  tapa ninguna cara y se van los rótulos de Teams.

Se probó antes un fondo con la misma imagen desenfocada y quedaba sucio: las
camisas aparecían como manchas.

**Audio.** Medido sobre los tramos de cada uno en Scribe con diarización, Ana
estaba en −14,8 LUFS y Camilo en −16,8. Cada turno lleva su ganancia (−4,2 y
−2,2 dB) para dejar a los dos en −19, como las introducciones. El cambio cae en
el silencio entre turnos.

## Los gráficos (`plan_dema.py`)

Todo va en la banda de abajo, **debajo de quien habla**: a la izquierda desde
x=86 y a la derecha desde x=1046. El ancho máximo es 720 y el bloque se ancla
arriba en y=725. Los textos son verbatim de la transcripción
(`03 VOCES/stt/DEMA_DECOC_stt.json`), sin muletillas. Hay 47 ítems y ocupan
513 de 1.160 s.

- **Lower thirds** (`cartones_dema.py`), como el de «Diana Carolina Florez
  Vallona» en la U1:
  - Barra (227, 214, 49), nombre en Montserrat Bold y barrido de izquierda a
    derecha, a la entrada y a la salida.
  - Debajo, la dirección de cada uno, con el nombre oficial:
    - Ana: Dirección Especializada para los Delitos contra los Recursos
      Naturales y el Medio Ambiente (DEMA), la de la Ley 2111 de 2021.
    - Camilo: Dirección Especializada contra las Organizaciones Criminales
      (DECOC), la de la Resolución 0730 de 2022.
  - En el audio no se dicen los cargos. Las siglas salen del título del
    archivo, y Camilo habla de «la dirección de medio ambiente a la que
    perteneces». **Confirmar con Sebastián.**
  - Cada uno sale dos veces: al empezar a hablar y a mitad del video.
- **Cartones de caja** (`cartones_dema.py`): los de cartones_v3 y cartones_ma,
  con el mismo dibujo y la misma animación.
- **Motion graphics** (`herramientas/motion/mg_dema.py`), en After Effects por
  aftr. Están en el mismo AEP que las introducciones, con composiciones
  `DEMA_<clave>`, y se rinden con aerender a `09 MOTION GRAPHICS`.
  - Los cuatro frentes de la macrocriminalidad ambiental y los tres ejes de la
    articulación van como tarjetas con ícono.
  - Tres listas tienen íconos que entran con la palabra: lo que impone la
    organización, para qué talan y qué pruebas técnicas necesitan.
  - Los íconos nuevos son de Magnific y quedaron en `iconos/hojas/hoja_D.png`:
    casa_lote, madera_fauna, satelite, matraz, finanzas, bidon, oro, vaca y
    excavadora.
- **Cartón de título** (`herramientas/cartones/titulo_dema.py`): el de las
  introducciones, con el nombre correcto del curso y la animación medida. El
  subtítulo se reescribe con la misma curva y dice «Conversatorio: articulación
  DEMA y DECOC».

La palabra que Scribe transcribió «Convertimiento» (minuto 5) se puso como
«Vertimiento» en el cartón c08.

## Revisión y entrega (11 nov 2026)

- **Render de revisión** (`D:/DAE/_tmp/ma/dema/REV_DEMA.mp4`):
  - 28.622 cuadros, la línea entera, con audio a −19,1 LUFS y pico de
    −3,8 dBTP.
  - La hoja de contacto toma un cuadro a mitad de cada uno de los 47 ítems,
    más el intro, el título, el cierre y el outro. En todos se ve el gráfico
    donde va.
  - El primer render quedó cortado (sin `moov`) cuando se cayó el puente con
    el computador. Está en `_tmp/ma/_descartes`.
- **Cargos de los lower thirds:** Sebastián los dejó como están.
- **Entrega:** `05 EXPORTS/delitosambientales - U1 - CONVERSATORIO DEMA y
  DECOC-v1.mov`, con el mismo formato que las introducciones: mov H.264
  High, tope de 6.000 kb/s y AAC 48 kHz.
- **Drive:** curso → `VIDEOS/VIDEOS UNIDADES/videos exportados/CONVERSATORIO -
  Articulación DEMA y DECOC`.
