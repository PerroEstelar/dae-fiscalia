# Unidad 3, lección 5: la prueba pericial (Delitos ambientales)

Pedido de Sebastián del 15 nov 2026:

> «preparar este, profe hablando a cámara, Video ambiental: Unidad 3 lección 5. Ya
> tiene intro, pero verifica todos los procesos necesarios, de pe a pa».

## El material

- **Fuente:** Drive, curso → `VIDEOS/HUGO SALAZAR/INTRO Unidad 3 - HUGO ASCENCIO
  SALAZAR - Leccion 5.mov`. No es la grabación cruda: es un montaje de septiembre.
  - 1920×1080 a 23,976, Rec.709, 6:55 (9.949 cuadros).
  - Cuadros 0–193: el intro FGN.
  - Cuadro 194: uno de paso, oscuro.
  - Cuadros 195–9754: el profe. Lleva quemado abajo a la izquierda, todo el tiempo,
    un rótulo azul en mayúsculas, «HUGO ASCENCIO SALAZAR».
  - Desde el 9755: negro y el outro FGN.
  - El audio viene en −21,1 LUFS con pico en −2,9 dBTP.
  - No tenía cartón de título, cartones de apoyo ni gráficos.
- **En disco:** `E:\DAE MASTER\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\UNIDAD 3\LECCION 5\01 VIDEO\ambiental_unidad3_leccion5.mov`.
- **El profe:** «Hola, yo soy Hugo Ascencio Salazar. Soy ingeniero químico de la
  Universidad Nacional de Colombia. Tengo una maestría en Desarrollo Sostenible y
  Medio Ambiente de la Universidad de Manizales». Es profesional investigador del
  Grupo Investigativo contra la Criminalidad Organizada para los delitos contra los
  Recursos Naturales y el Medio Ambiente, en el CTI.
- **La lección** (`plan_intros.UNIDADES[3]`): «La prueba pericial. En materia
  procesal penal frente a los delitos ambientales».
- **Temas:**
  - la función del perito ambiental: identificar, seleccionar, recolectar y valorar
    los EMP y la evidencia física;
  - demostrar el peligro o establecer una infracción administrativa;
  - su aporte, del programa metodológico al juicio oral;
  - el lugar de los hechos: qué, cómo, dónde y para qué recolectar;
  - el orden público en campo;
  - los soportes científicos y la cadena de custodia;
  - el grupo interdisciplinario y el trabajo en equipo;
  - los delitos conexos;
  - la comparación con líneas base.

## Qué se hizo con el montaje viejo

Se usa solo el tramo del profe (`TRAMOS`, cuadros 195–9754), y se rearma todo con lo
de la serie: intro, cartón de título, clip, cartón de cierre y outro. Así no hay
intro doble, y el rótulo quemado se reemplaza por el lower third de la serie.

El rótulo no se tapa: queda fuera de la ventana.

## Encuadre

`perfil2.py` (`D:\DAE\_tmp\ma\u3l5`) es `perfil.py` para una fuente de cualquier
tamaño y con un tramo de tiempo. Se corrió sobre 199 cuadros del tramo, y midió
también el borde derecho. En coordenadas de la fuente:
- cima de la cabeza: mín. 72, p2 79, p50 156;
- borde izquierdo a la altura de la caja: p2 490–550, p10 630–700;
- borde derecho de la cabeza: p98 1270, máx. 1474.

Lo que quedó:
- **Ventana 1472×828 desde (0, 50), ×1,30.**
  - El ancho sale del borde derecho: con menos, la cabeza se sale por la derecha
    cuando él se corre.
  - Abajo termina en y=878, y el rótulo quemado empieza en y≈980.
  - El panel DAE/Fiscalía (y 87–231) entra entero.
- **Columna de 470 px** (`MAXW`). El profe está al centro y empieza en x≈640–720 de
  salida (p2).
- **Lower third** con el nombre a 36 px y el cargo a 420 de ancho, en tres renglones
  (`LT`); termina en x≈559. Al principio él está cerca y la camisa blanca empieza en
  x≈614. Con el nombre a 40 px, el texto blanco tocaba la camisa (simulado sobre
  ocho cuadros).
- `MATRIZ_FUENTE` = bt709: la fuente es un export HD, no una grabación de Teams
  (BT.601).
- `FPS_COMPUESTO` = 23,976: la fuente ya va a esa cadencia, y a 30 se duplicarían
  cuadros.

## Textos

Salen de Scribe (WAV a 16 kHz, una voz), sin muletillas. EMP: elementos materiales
probatorios.

- 14 cartones, 4 listas y 3 tarjetas de AE.
- Todos caben en la caja con cima ≥ 257.
- La última fila de cada lista queda al menos 4 s.
- Cobertura: ~72 % del clip. La pieza es corta y densa: se quitaron cuatro cartones
  que repetían al anterior.

## El cuadro negro del primer compuesto

El compuesto v1 salió con 9.561 cuadros, uno de más, y el último era negro. Era el
primer cuadro del outro viejo:
- 9755/23,976 = 406,8648 s;
- el borde del tramo (406,865, redondeado a tres decimales) quedaba detrás de él.

Los bordes del tramo ahora van a mitad de cuadro (194,5 y 9754,5). El v1 quedó en
`01 VIDEO\_descartes` con un `LEER`.

## Revisión

- **Hoja de `ic_revision`:** un cuadro por gráfico, más intro, título, cierre y outro.
- **Cuadros a tamaño completo:**
  - el lower third, en dos momentos;
  - las cuatro listas;
  - dos tarjetas;
  - el primer cuadro del clip;
  - los cartones de título.
- El clip arranca limpio en el profe, sin el cuadro oscuro de paso, y termina sin
  negro.
- El lower third queda libre de la camisa. Nada se sale de la caja ni queda
  recortado: ni el panel, ni la marca de los cartones de título, ni el outro.

## Entrega (15 nov 2026)

MP4 con la receta de `Entrega_MP4_Fiscalia_Receta.md` (`mp4_entrega.py`): máster
H.264 NVIDIA a 32 Mb/s, y entrega x264 CRF 18, High L4.0, Rec.709, AAC 48 kHz
estéreo con el audio copiado del máster.

| | |
|---|---|
| archivo (`05 EXPORTS`) | `delitosambientales - U3 - LECCION 5-v1.mp4` |
| largo | 7:13 (10.378 cuadros = línea) |
| peso | 205 MB |
| sonoridad / pico | −16,1 LUFS / −2,7 dBTP |
| PSNR contra el máster (medio / mínimo) | 50,9 / 45,0 dB |
| gráficos | 1 lower third, 13 cartones, 4 listas, 3 tarjetas |
| máster | `D:\DAE\_masters_archivo\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\UNIDAD 3\LECCION 5` (1,3 GB); en `05 EXPORTS\_master` queda el `LEER` |

- **Estructura:**
  1. intro (194 cuadros);
  2. cartón de título «Investigación y judicialización de delitos contra el medio
     ambiente y los recursos naturales / Unidad 3. Lección 5» (215);
  3. el clip (9.560 cuadros);
  4. el mismo cartón de cierre;
  5. el outro (194).
- **Audio:** el de los profes v2, a −16 LUFS con techo en −3 dBTP. El montaje viejo
  venía en −21,1.
- **Línea para Sebastián:** `10 TIMELINE SEBASTIAN\MA - U3 - LECCION 5.drt`.
  - V1: video.
  - V2: título y cartones.
  - V3: motion graphics, con alfa premultiplicado.
  - V4: lower third.
- **Drive:** curso → `VIDEOS/VIDEOS UNIDADES/videos exportados/UNIDAD 3 - LECCIÓN 5
  - La prueba pericial` (`1owzhcZV_mOam7wdU9TRYJzqL45cfFb5s`).
  - Subió por `G:\My Drive\_MA subidas` y se movió con `update_file`.
  - La copia de la fuente que había quedado en `_MA subidas` se mandó a la papelera.
  - El montaje de septiembre sigue donde estaba, en `VIDEOS/HUGO SALAZAR`.
