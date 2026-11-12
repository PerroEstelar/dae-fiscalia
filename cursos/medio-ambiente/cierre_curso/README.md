# Cierre del curso (Delitos ambientales)

Pedido de Sebastián (12 nov 2026): el cierre del curso, con la misma docente y
el mismo método que la introducción al curso (`../introduccion_curso`).

Lleva:

- intro y outro;
- los cartones de inicio y de salida;
- el lower third;
- cartones de apoyo;
- gráficos de After Effects.

Nada puede quedar recortado. Va en las carpetas que le corresponden, en disco
y en Drive.

## El material

- **Fuente:** Drive, carpeta del curso → `VIDEOS`, archivo
  `ambiental_cierre_curso.mp4`.
  - Es una grabación de Teams de 2:52,6, 1280×720 a 30 fps.
  - Tiene el mismo fondo virtual que la introducción.
  - Se bajó por `_MA subidas` (una copia en Mi unidad que Drive sincroniza). Esa
    copia se mandó después a la papelera.
- **Quién habla:** «Soy Diana Carolina Flórez Bayona». El lower third dice
  «Diana Carolina Florez Vallona», como la U1 y la introducción, con la misma
  línea de títulos debajo.
- **Transcripción:** Scribe sobre un WAV a 16 kHz. Son 320 palabras y una sola
  voz (`D:\DAE\_tmp\ma\cc\stt_full.json`).
- **Disco:** `E:\DAE MASTER\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\CIERRE DEL CURSO\`,
  con las mismas carpetas que la introducción y los mismos bins en Resolve.
- **Línea:** `MA - CURSO - CIERRE`. Su `.drt` está en `10 TIMELINE SEBASTIAN`.

## Cómo se hizo

Son las herramientas de la introducción con `DAE_PLAN=plan_cc` (`plan_cc.py`):

- `ic_pieza componer · titulo · cartones · mg_armar · mg_render`;
- `ic_linea construir · drt`;
- `ic_mp4`, para la entrega;
- `ic_revision`.

**Imagen y sonido:**

- **Ventana:** 1143×643 desde (0, 30). Ella está más cerca de la cámara que en
  la introducción. Aun así, la cabeza empieza en x≈825–885 y la caja termina
  en el 790.
- **Audio:** el v2 de los profes.
  - El original venía en −27,1 LUFS.
  - El compuesto queda en −16,0 LUFS, con pico −3,0 dBTP.

**Gráficos.** Son 12 en total:

- el lower third;
- 7 cartones de caja verbatim:
  - «Quiero felicitarlos…»;
  - las perspectivas;
  - la mirada integral;
  - los servidores;
  - la protección del medio ambiente;
  - los éxitos;
  - «Muchas gracias»;
- 4 listas de After Effects:
  - «En las cinco unidades»;
  - «También analizamos»;
  - «También es necesario»;
  - «Esperamos que les puedan».

**Ajustes medidos antes de rendir:**

- El primer cartón, con el nombre del curso debajo, iba a 20 car/s. Quedó
  solo la frase, y el nombre del curso ya está en los cartones de título.
- Los rótulos de las listas son sus palabras recortadas hasta que la cima
  quedó en 259 o más.
- La cobertura es del 70 %. Por eso quedaron fuera tres frases:
  - «Esto considerando…»;
  - «No basta con identificar…»;
  - el agradecimiento.
- Se corrigió «contribuyen» por «contribuyan».

**Cartón de título:** «Cierre del curso», con `titulo_dema` sobre u1v2. La
marca APRENDE CON LA DAE entra entera.

**Línea:** todo va a 1:1.

- Cada ítem está en el cuadro y con la duración del plan.
- El último cartón termina en el 4542, y el clip en el 4546.

## Entrega (MP4, receta del 23 oct, `ic_mp4`)

- **Archivo:** `05 EXPORTS/delitosambientales - CURSO - CIERRE-v1.mp4`.
  - Formato: H.264 High L4.0, 1920×1080, 23,976, bt709.
  - Son 4.955 cuadros, los mismos que la línea, y pesa 152 MB.
  - El máster de 802 MB está en `05 EXPORTS/_master`.
- **Sonido:** −16,1 LUFS, pico −2,3 dBTP.
- **Calidad:** PSNR contra el máster de 48,6 dB de media y 43,5 de mínimo.
- **Negros y silencios:** sin cuadros negros. Los dos silencios son los cartones
  de título.
- **Revisión:** en la hoja ningún texto pisa la cara.
  - En las zonas más apretadas, el texto termina en x≈773 y la oreja empieza en
    x≈807.
- **Drive:** curso → `VIDEOS/VIDEOS UNIDADES/videos exportados`, junto a la
  introducción al curso y las introducciones de unidad.
