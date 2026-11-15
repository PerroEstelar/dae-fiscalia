# Unidad 4, lección 1: justicia restaurativa (Delitos ambientales)

Pedido de Sebastián del 15 nov 2026:

> «tenemos este otro video con otra profe hablando a cámara, necesito todo el
> proceso que ya conoces muy bien de profe hablando a cámara, de pe a pa con todos
> los requerimientos».

Lleva lo de siempre:
- intro y outro FGN;
- cartones de título de entrada y salida con el nombre del curso y el subtítulo
  «Unidad 4. Lección 1»;
- lower thirds con el nombre y el cargo de la profe;
- cartones de apoyo y gráficos de AE;
- audio revisado, nada recortado, todo en sus carpetas en el disco y en Drive.

## El material

- **Fuente:** Drive, curso → `VIDEOS/ambiental_unidad4_leccion1` (sin extensión
  en el título). Es una grabación de 27:36, 1280×720 a 30 fps, con el fondo
  virtual del edificio y el panel DAE/Fiscalía. El audio llega con el pico en
  +0,7 dBTP.
- **La profe:** «Soy Daniela Escallón, fiscal delegada ante la Unidad Nacional de
  Justicia Restaurativa de la Fiscalía General de la Nación». No dice su formación,
  así que el lower third lleva el cargo. Es la primera vez que sale en la serie.
- **El título de la lección** (`plan_intros.UNIDADES[4]`): «Justicia restaurativa
  en el marco del proceso penal colombiano. En los delitos contra el medio ambiente
  y los recursos naturales».
- **Dos bloques en un archivo:**
  1. 0:00–15:37. El caso de Tito: un campesino de 59 años, malacatero en una mina
     ilegal de carbón en Boyacá. Las víctimas son la CAR y Acerías Paz del Río.
     Principio de oportunidad, causal 7: la suspensión del procedimiento a prueba.
     La reparación pasa de 500 a 800 árboles, más unas cartillas para su comunidad
     hechas con la DEMA.
  2. 15:38–27:36. La Unidad Nacional de Justicia Restaurativa:
     - la crea la Resolución 0211 de 2025;
     - sus tres finalidades;
     - mediación y conciliación (art. 521 del CPP), principio de oportunidad y
       preacuerdo;
     - las víctimas institucionales;
     - discrecionalidad y máxima contundencia.

## Disco, Resolve y AE

- **Disco:** `E:\DAE MASTER\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\UNIDAD 4\LECCION 1\`,
  con 01 VIDEO, 02 CARTONES, 03 VOCES, 05 EXPORTS, 09 MOTION GRAPHICS y
  10 TIMELINE SEBASTIAN.
- **Resolve:** bin `CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE / UNIDAD 4 / LECCION 1`,
  línea `MA - U4 - LECCION 1`.
- **AE:** comps `U4L1_*` en `00 MOTION GRAPHICS\MA_intros_mg.aep`.
- **Herramientas:** las de los videos de profes (`ic_pieza`, `ic_linea_externa`,
  `ic_revision`, `mp4_entrega`) con `DAE_PLAN=plan_u4l1`. Desde esta lección las
  `ic_*` buscan el plan recorriendo `cursos/`, así que un plan nuevo no necesita
  tocar las herramientas.

## Encuadre

La profe está muy cerca de la cámara. Se midió con `perfil.py` sobre 663 cuadros:
- la cima de la cabeza está en y≈70 (p2), 86 (p10) y 116 (p50) de la fuente, y en
  algún cuadro llega a 49;
- el borde izquierdo, a la altura de la caja: p10 530–568, p2 480–548. Cuando se
  inclina, el pelo llega a x≈420.

Lo que quedó:
- **Ventana 1143×643 desde (0, 0)**, ×1,68. La estándar empieza en y=40 y dejaba
  la coronilla a 15 px del borde; desde y=0 quedan 80 px. Abajo solo corta pecho y
  el panel DAE/Fiscalía entra entero.
- **Columna de 560 px** (`MAXW`; la estándar es 615). Con 615 el texto le pisaba
  el pelo cuando se inclina (simulado sobre nueve cuadros).
- **Lower third** con el nombre a 48 px y el cargo a 460 de ancho (`LT`), para que
  no llegue al saco blanco.
- Antes de componer se revisaron 16 cuadros con la caja dibujada. Lo único que
  entra en la caja es una mano cuando gesticula (24:40), un momento.

## La transición de cubo de la fuente

Entre los dos bloques, la fuente trae horneada una transición de cubo 3D de medio
segundo (937,65–938,20). En ella el panel DAE/Fiscalía se deforma y sale de
cuadro.
- Se cambió por un corte seco: desde 937,63 se ve quieto el primer cuadro limpio
  del bloque 2 (938,20), y en 938,20 sigue el video.
- El audio no se toca. En ese medio segundo se oye la pausa y el arranque de
  «Hola de nuevo».
- Va en el plan como `CONGELA = [(937.65, 938.20)]`, y `ic_pieza.tramos_vf` lo
  resuelve. Los bordes se llevan a la rejilla de la fuente: el de entrada hacia
  atrás y el de salida hacia adelante, para no dejar ni un cuadro deformado.
- El bloque 2 lleva su propio lower third, porque ella se vuelve a presentar.

## Textos

Salen de Scribe (WAV a 16 kHz, una voz), sin muletillas.
- «resolución dos once de dos mil veinticinco» → Resolución 0211 de 2025 (está en
  el SIDN de la Rama Judicial).
- «artículo cinco veintiuno» → art. 521 del CPP.
- «DEMMA» → DEMA, como en el resto del curso.

Densidad:
- se armó un cartón o una lista por cada momento que ella subraya;
- después se recortó cada uno a lo que tarda en leerse (10 car/s más 2,5 s) para
  dejar la cobertura en ~63 %;
- la última fila de cada lista queda al menos 6 s;
- todo cabe en la caja con cima ≥ 268. Cinco piezas que se salían se acortaron
  antes de rendir: la lista de los árboles, «Para un plan efectivo», la segunda
  finalidad, «Ya no es una responsabilidad objetiva» y «Un poco más allá».

## Revisión

- **Hoja de `ic_revision`:** un cuadro por gráfico, más intro, título, cierre y
  outro.
- **Cuadros a tamaño completo:**
  - los dos lower thirds;
  - la lista más alta (m11);
  - el cartón más alto del bloque 1;
  - la profe inclinada (14:53);
  - el empalme de los dos bloques.

  En el empalme, una tira de 24 cuadros (937,4–938,2) muestra el bloque 1 limpio
  y después el cuadro quieto del bloque 2, sin un solo cuadro del cubo.
- Nada se sale de la caja y nada queda recortado: ni el panel, ni la marca de los
  cartones de título, ni el outro.
- Lo único que se cruza con un texto es la mano de la profe cuando gesticula. Pasa
  en las listas «Para un plan efectivo» (20:16) y la de 24:32, y en «También cuando
  hay juicio». La mano pasa por debajo del texto, que se sigue leyendo.

## Entrega (15 nov 2026)

MP4 con la receta de `Entrega_MP4_Fiscalia_Receta.md` (`mp4_entrega.py`):
- máster H.264 NVIDIA a 32 Mb/s;
- entrega x264 CRF 18, High L4.0, Rec.709, AAC 48 kHz estéreo con el audio copiado
  del máster.

| | |
|---|---|
| archivo (`05 EXPORTS`) | `delitosambientales - U4 - LECCION 1-v1.mp4` |
| largo | 28:11 (40.535 cuadros = línea) |
| peso | 1.005 MB |
| sonoridad / pico | −16,0 LUFS / −3,0 dBTP |
| PSNR contra el máster (medio / mínimo) | 49,6 / 45,0 dB |
| gráficos | 2 lower thirds, 56 cartones, 11 listas, 3 tarjetas |
| máster | `D:\DAE\_masters_archivo\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\UNIDAD 4\LECCION 1` (6,4 GB); en `05 EXPORTS\_master` queda el `LEER` |

- **Estructura:**
  1. intro (194 cuadros);
  2. cartón de título «Investigación y judicialización de delitos contra el medio
     ambiente y los recursos naturales / Unidad 4. Lección 1» (215);
  3. el clip;
  4. el mismo cartón de cierre;
  5. el outro (194).
- **Audio:** el de los profes, v2: ecualizado, comprimido y a −16 LUFS con techo en
  −3 dBTP.
- **Línea para Sebastián:** `10 TIMELINE SEBASTIAN\MA - U4 - LECCION 1.drt`.
  - V1: video.
  - V2: título y cartones.
  - V3: motion graphics, con alfa premultiplicado.
  - V4: lower thirds.
- **Drive:** curso → `VIDEOS/VIDEOS UNIDADES/videos exportados/UNIDAD 4 - LECCIÓN
  1 - Justicia restaurativa` (`1973M2cTX9faj2KPkfbUx0Yh9tlAerfGj`).
  - Subió por `G:\My Drive\_MA subidas` y se movió con `update_file`.
  - La copia de la fuente que quedaba en `_MA subidas` se mandó a la papelera.
