# Entrevista «Técnicas especiales de investigación» (Unidad 3)

Pedido de Sebastián (11 nov 2026):

> «crea una carpeta aparte para este, mira el video, comprende sus temáticas,
> reconoce al profesor, agrega intro, placa de entrada, placa de salida, outro,
> lower thirds, textos de apoyo en pantalla y aftrs, también enhance the audio».

## El material

- **Fuente:** Drive, carpeta del curso → `VIDEOS/VIDEOS UNIDADES`, archivo
  `tecnicas_especiales_delitos_ambientales.mp4`. Es una grabación de Teams de
  14:59, 1280×720 a 30 fps, con fondo virtual aéreo. Habla un solo profe.
- **Quién habla:** según la ficha de la Unidad 3, «Entrevista al doctor Jairo
  Porras o CTI: Técnicas especiales de investigación». En el video no dice su
  nombre, pero sí que lleva 32 años en la Fiscalía y que fue 13 años fiscal
  especializado ante la DEMA. El lower third dice «Jairo Porras». **Falta que
  Sebastián lo confirme.**
- **Temas:**
  - la fuente no formal (cardex, seudónimo), que no es prueba per se;
  - las técnicas especiales: interceptación, agente encubierto y entrega
    controlada;
  - escalar con judicializaciones primarias y principios de oportunidad
    condicionados a testimonio;
  - llegar al músculo financiero;
  - el caso del gobernador del Putumayo;
  - «explotación ilícita de yacimiento minero» (art. 332) y no «minería ilegal»,
    con sus dos requisitos (título minero y licenciamiento ambiental);
  - los delitos conexos;
  - la peritación;
  - las fuentes abiertas.
- **Disco:** `UNIDAD 3/ENTREVISTA - Tecnicas especiales de investigacion`, con
  las carpetas 01 VIDEO, 02 CARTONES, 03 VOCES, 05 EXPORTS, 09 MOTION GRAPHICS y
  10 TIMELINE SEBASTIAN, y los mismos bins en Resolve.
- **Línea:** `MA - U3 - ENTREVISTA TECNICAS ESPECIALES`.
- **Drive:** curso → `VIDEOS/VIDEOS UNIDADES/videos exportados/ENTREVISTA -
  Técnicas especiales de investigación`.

## Cómo se hizo (`plan_te.py`, `herramientas/montaje/te_pieza.py`, `te_linea.py`)

Es el procedimiento de los videos de profes del curso SRPA.

- **Ventana:** 1143×643 desde (12, 30). El profe queda a la derecha y la caja de
  cartones a la izquierda.
- **Audio:**
  - paso alto a 80 Hz;
  - −2 dB en 250 Hz;
  - +3 dB en 3 kHz;
  - compresor de 3:1;
  - loudnorm a −16 LUFS.

  El primer export midió +0,3 dBTP después del AAC de Resolve. El audio v2 lleva
  el techo en −3 dBTP y ese export quedó en `05 EXPORTS/_descartes`.
- **Gráficos.** Son 31:
  - 2 lower thirds;
  - 20 cartones de caja verbatim;
  - 9 tarjetas y listas de AE, en `MA_intros_mg.aep`, con comps `TE_*`.
- **Cartón de título:** se hizo con `titulo_dema`, sobre la base u3v2. El
  subtítulo dice «Entrevista: técnicas especiales de investigación».
- **Cierre y outro:** a 1:1.
