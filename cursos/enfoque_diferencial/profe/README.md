# Enfoque diferencial · videos de profe (Camilo Borrero García, 15 nov 2026)

Pedido de Sebastián (15 nov): «hacer lo mismo para todos los videos en esta carpeta, profe
hablando a cámara de pe a pa». La carpeta es «Videos enfoques diferenciales», del profe
(`caborrerog@unal.edu.co`, Drive `1dTALmfoD-P3cyiIoO39tg-0-3rTOy7mJ`): 12 grabaciones, 2 h 12 min.

Es el formato de las introducciones de Delitos ambientales:
- intro y outro FGN;
- cartón de título con el nombre del curso arriba y el video abajo;
- lower third del profe;
- cartones de caja verbatim y listas de After Effects;
- audio v2 de los profes;
- entrega MP4 con la receta del 23 oct.

Herramientas: `ic_pieza`, `ic_linea_externa`, `mp4_entrega` e `ic_revision`, con
`DAE_PLAN=plan_ed…`. La base común es `base_ed_profe.py`; hay un plan por video.

## Los 12 videos

| plan | video | fuente | tramo (cuadros de la fuente) | gráficos | cobertura |
|---|---|---|---|---|---|
| `plan_ed00` | Presentación del curso | `ed_00_presentacion_general` (1:52) | 28–3266 | 8 | 68 % |
| `plan_ed1p` | Unidad 1 · presentación | `ed_u1_presentacion` (0:47) | 54–1355 | 3 | 75 % |
| `plan_ed1c` | Unidad 1 · contenido «Igualdad y diferencia» | `ed_u1_contenido` (22:11) | 50–39876 | 79 | 63 % |
| `plan_ed2p` | Unidad 2 · presentación | `ed_u2_presentacion` (0:44) | 14–1262 | 3 | 65 % |
| `plan_ed2c` | Unidad 2 · contenido «Sujetos de especial protección constitucional» | `ed_u2_contenido` (21:44) | 14–39013 | 65 | 63 % |
| `plan_ed3p` | Unidad 3 · presentación | `ed_u3_presentacion` (0:52) | 38–1496 | 4 | 72 % |
| `plan_ed3c` | Unidad 3 · contenido «Enfoques diferenciales y derechos especiales» | `ed_u3_contenido` (26:18) | 18–47240 | 80 | 62 % |
| `plan_ed4p` | Unidad 4 · presentación | `ed_u4_presentacion` (0:43) | 51–1210 | 4 | 79 % |
| `plan_ed4c` | Unidad 4 · contenido «Etnicidad» | `ed_u4_contenido` (25:53) | 54–46519 | 72 | 62 % |
| `plan_ed5p` | Unidad 5 · presentación | `ed_u5_presentacion` (0:46) | 35–1168 | 4 | 79 % |
| `plan_ed5c` | Unidad 5 · contenido «El enfoque de género» | `ed_u5_contenido` (27:56) | 17–50160 | 80 | 62 % |
| `plan_ed99` | Conclusiones del curso | `ed_99_conclusiones` (2:06) | 7–3623 | 8 | 70 % |

Cada tramo va de 0,7 s antes de la primera palabra a 0,8 s después de la última. Al final
de cada grabación el profe se acerca a la cámara para cortarla, y eso queda afuera.

Las presentaciones de unidad quedan por encima del 70 %. Son de 40 s, con tres frases y un
lower third de 6 s, y cada frase es un punto del curso.

## La fuente

Grabaciones de teléfono:
- HEVC Rec.709, codificadas a 1080×1920 con rotación, así que se ven en 1920×1080;
- audio AAC **mono**;
- fondo virtual del edificio de la Universidad Nacional, con el panel DAE/Fiscalía arriba
  (x 190–890, y 78–235).

Dos cosas que cambian el procedimiento:

- **La cadencia no es pareja.** Declaran 30 fps, pero cada tanto traen un cuadro de 35 ms: el
  contenido de la U5 tiene 50.246 cuadros en 1675,74 s, 26 menos que 30 × duración.
  - Cortar por número de cuadro (`trim=start_frame`) corría el final del video casi un
    segundo respecto del audio.
  - El plan pone `POR_TIEMPO = True` y `ic_pieza._trim` corta por tiempo en la rejilla de
    30. La base de tiempo es 1/600, así que f/30 cae exacto en un tick.
  - Medido: el compuesto sale con un cuadro de más como mucho, y el audio queda del mismo
    largo.
- **El audio es mono.** `ic_pieza.base_audio` arma el dual-mono ANTES de medir y normalizar
  cuando la fuente tiene un canal. Medido: −16,0 LUFS y −3,0 dBTP en los 12. Las fuentes
  venían entre −30 y −33 LUFS.

Las fuentes se leyeron de una copia en `G:\My Drive\_MA subidas\_ED profes` (8,2 GB, en
streaming de Drive), no copiadas a disco.

## Ventana, columna y lower third

**Ventana 1440×810 desde (0, 40), ×1,33.** Es la misma para los 12 videos.
- Se probó con la caja dibujada en 8 cuadros de cada video (`caja_ed.py`).
- La cabeza del profe queda desde x≈810 de salida.
- El panel entra entero.
- Abajo solo se corta pecho.

**La columna de cartones y listas es de 560** (`MAXW`). El pelo largo baja por la izquierda
hasta los hombros.
- Se midió la cima de los 410 gráficos (≥ 250) y se simularon sobre cuadros del compuesto.
- Las listas de cuatro filas no llevan título.
- La enumeración de la presentación del curso (nueve poblaciones en 17 s) va en tres listas
  de tres. Cada última fila queda 4 s o más.

**El lower third lleva el nombre a 40 px y el cargo a 440 de ancho**, en tres renglones.
Termina en x≈590.

**El fondo virtual trae un marco fino** a la izquierda:
- una línea vertical en x≈157 de salida;
- un «DAE» vertical en x≈95–115.

No se puede dejar afuera: correr la ventana 120 px pone la cabeza en x≈650, encima de la
columna. Queda como parte del fondo institucional, y la barra amarilla de los cartones pasa
por encima del «DAE».

## Los textos

Salen de la transcripción de Scribe (WAV mono a 16 kHz), sin muletillas y verbatim.

Correcciones de la transcripción:
- «mancos» (no «bancos»);
- «altisonante»;
- «indebido privilegio»;
- el apartheid «campeó».

Lo que el profe nombra de oído va con su forma escrita:
- C-586 de 2016;
- Ley 581 de 2000;
- SU-020 de 2022;
- T-254 de 1994;
- artículo 104A;
- Ley 1761 de 2015;
- Sisma Mujer.

Tres cosas que dice y el cartón no repite:
- llama «artículo 49» al que enumera los derechos de los niños (es el 44): el cartón dice
  «La Constitución»;
- la Ley 70 es de 1993 (él dice 1992): va sin año;
- la «T302 de 2025» va como «una sentencia reciente».

Herramientas de texto (scratchpad del 15 nov, no en el repo): `gen_plan.py` pasa un plan con
tiempos por frase (`A('frase')`, `Z('frase')`, `W('frase')`) a números contra el JSON de Scribe,
y `ajusta.py` recorta a tiempo de lectura (10 car/s) y quita solapes.

## Dónde quedó

- **Disco:** `D:\DAE MASTER\PRIORIDAD 2\CURSO - ENFOQUE DIFERENCIAL\VIDEOS PROFE\`.
  - E: no tenía espacio (8 GB libres); hay un `LEER` en el mismo sitio de E:.
  - Carpetas por video: `00 PRESENTACION DEL CURSO`, `UNIDAD n\PRESENTACION`,
    `UNIDAD n\CONTENIDO` y `99 CONCLUSIONES`.
  - Dentro de cada una: 01 VIDEO, 02 CARTONES, 05 EXPORTS, 09 MOTION GRAPHICS y
    10 TIMELINE SEBASTIAN (con el `.drt`).
- **After Effects:** `E:\DAE MASTER\PRIORIDAD 2\CURSO - ENFOQUE DIFERENCIAL\00 MOTION GRAPHICS\ED_profe_mg.aep`,
  con las comps `ED00_*`, `ED1P_*`, `ED1C_*`… Es una copia de `MA_intros_mg.aep` con las
  comps nuevas.
- **Resolve:** bins `PRIORIDAD 2 / CURSO - ENFOQUE DIFERENCIAL / VIDEOS PROFE / …`; líneas
  `ED - CURSO - PRESENTACION`, `ED - U1 - PRESENTACION` … `ED - CURSO - CONCLUSIONES`.
- **Máster de paso** (decisión de Sebastián, 15 nov): el máster de 32 Mb/s se rinde en
  `D:\DAE\_tmp\ed_profes\master`, se usa para la entrega, se verifica y va a la papelera de
  Windows. En `05 EXPORTS\_master` queda un `LEER` que lo dice.

## Entregas (15 nov 2026)

Drive: carpeta VIDEOS del curso →
[VIDEOS PROFE - Camilo Borrero García](https://drive.google.com/drive/folders/1LNFO7X0A15EnIifpRpEycKcGW1LIqYLA)
(`1LNFO7X0A15EnIifpRpEycKcGW1LIqYLA`). Los 12 archivos están juntos y el tamaño de cada uno
se comprobó contra el disco.

| entrega | largo | cuadros = línea | LUFS · pico | PSNR | MiB | Drive |
|---|---|---|---|---|---|---|
| `enfoquediferencial - CURSO - PRESENTACION-v1.mp4` | 2:22 | 3.406 | −16,3 · −3,0 | 49,8 | 74 | `1lSvKUu6o8Wg_uV__Zr2XOcypOjpFvbZg` |
| `… - U1 - PRESENTACION-v1.mp4` | 1:17 | 1.857 | −16,6 · −3,0 | 50,4 | 36 | `1EUmd6gAbBTfiPgwGDyFfuW8GY6BEaBuU` |
| `… - U1 - CONTENIDO-v1.mp4` | 22:42 | 32.647 | −16,0 · −2,3 | 49,4 | 773 | `13gvB9TLcKEme07XxgfjDag5c5jE2gE2Y` |
| `… - U2 - PRESENTACION-v1.mp4` | 1:16 | 1.815 | −16,5 · −3,0 | 50,3 | 37 | `1wsYqIRFtpnShTdlxRfjC8gSlKaFQ8erF` |
| `… - U2 - CONTENIDO-v1.mp4` | 22:14 | 31.986 | −16,0 · −2,8 | 49,0 | 830 | `1gNVmlOlWn1jxplYcP2GDzD67_R9IFTul` |
| `… - U3 - PRESENTACION-v1.mp4` | 1:23 | 1.983 | −16,5 · −3,0 | 50,2 | 40 | `1xZAwjK8GO_aMcts5xNRIs76h4uoxg9xz` |
| `… - U3 - CONTENIDO-v1.mp4` | 26:48 | 38.558 | −16,0 · −2,8 | 48,4 | 1.175 | `1rTn58-92E7RYSyGVtAC681tQe4XNuDod` |
| `… - U4 - PRESENTACION-v1.mp4` | 1:13 | 1.744 | −16,6 · −3,0 | 50,7 | 32 | `1uk3vRgrQRy3QMVjFe6Hz6A2DoW1mBgNk` |
| `… - U4 - CONTENIDO-v1.mp4` | 26:23 | 37.952 | −16,0 · −2,0 | 49,4 | 906 | `1ff2KuM-qABxpZuO9jinr16Pvtz6aCtIZ` |
| `… - U5 - PRESENTACION-v1.mp4` | 1:12 | 1.723 | −16,5 · −3,0 | 50,6 | 32 | `1ocq9p5tTdy98OdJlN6xClXh0RoNvCtgu` |
| `… - U5 - CONTENIDO-v1.mp4` | 28:26 | 40.892 | −16,0 · −2,2 | 48,9 | 1.131 | `12nFMusviNbgCg_h_6R8v5QoRKfticxFB` |
| `enfoquediferencial - CURSO - CONCLUSIONES-v1.mp4` | 2:35 | 3.708 | −16,2 · −3,0 | 49,7 | 87 | `1chY2F2Rl_E_WjQXb4tD7KHGPEdCAabZM` |

Todas son H.264 High L4.0, 1920×1080, Rec.709 y 23,976, con audio AAC 48 kHz estéreo. El
audio sale copiado del máster.

Las hojas de revisión (`D:\DAE\_tmp\ed_profes\<fuente>\hoja_rev_1.jpg`) tienen un cuadro por
gráfico, más intro, título, cierre y outro.

Las copias de las fuentes en `G:\My Drive\_MA subidas\_ED profes` se mandaron a la papelera de
Drive. Los originales siguen en la carpeta del profe.

**Lo que hubo que rehacer:** `mg_armar` del contenido de la U1 se cortó dos veces porque aftr no
respondió a tiempo («batch timed out after 30000ms»). Fue con After Effects cargado: aerender,
Resolve y x264 corrían a la vez. Con la máquina libre, la misma comp se arma en 7 s.
- AE terminó igual la primera comp después del timeout. Su render anterior quedó en
  `09 MOTION GRAPHICS\_descartes`, con un `LEER`.
- Se rearmaron y se rindieron las 15 listas.
