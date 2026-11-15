# Unidad 3, lección 4: la investigación financiera (Delitos ambientales)

Pedido de Sebastián del 15 nov 2026: «de igual manera ahora con este, ambiental
unidad 3 lección 4». Es el procedimiento completo de profe a cámara:
- intro y outro;
- cartones de título con el nombre del curso y «Unidad 3. Lección 4»;
- lower third;
- cartones de apoyo y gráficos de AE;
- audio revisado, nada recortado, y todo en sus carpetas en el disco y en Drive.

## El material

- **Fuente:** Drive, curso → `VIDEOS/ambiental_unidad3_leccion4.mp4`. Es una
  grabación de Teams de 5:27, 1280×720 a 30 fps, con el fondo virtual del edificio
  y el panel DAE/Fiscalía.
  - Abajo a la izquierda trae quemado el nombre de Teams, «Alba Lucía Solís
    Ramírez».
  - Audio: −17,2 LUFS, pico +0,2 dBTP.
- **La profe:** Alba Lucía Solís Ramírez. Es líder del grupo de análisis de
  investigaciones financieras (GAIF) de la Delegada contra la Criminalidad
  Organizada. Primera vez en la serie.
- **Temas:**
  - la investigación financiera como herramienta en los delitos ambientales;
  - el GAIF, creado por la Resolución 0042 del 5 de mayo de 2026 (como ella lo
    dice);
  - el análisis contable, tributario, financiero, cambiario y societario;
  - comprender la organización antes de investigar sus finanzas;
  - la articulación con la DIACO;
  - las capacidades del GAIF;
  - seguir la ruta del dinero detrás de la afectación ambiental;
  - la metodología de trabajo con el fiscal.

## Lo que traía la grabación

Viene armada con varias tomas. Midiendo cuadro a cuadro el panel aparecieron siete
defectos, y en el audio dos tomas repetidas.

| | dónde (fuente) | qué se hizo |
|---|---|---|
| negro al arranque, sobre «Cordial saludo» | 0:00–0:01 | se empieza en «Mi nombre es»; 5 cuadros quietos tapan el final del negro |
| cubo 3D entre tomas (con silencio digital) | 0:26,6 | el primer cuadro limpio, quieto, sobre el cubo; el audio sigue |
| cubo 3D | 1:04,0 | igual |
| fundido desde negro, con manchas negras del fondo virtual hasta el cuadro 4370 | 2:25,2 | igual, en una pausa, con el cuadro 4372 (el primero sin manchas) |
| toma repetida: «…quiénes aparecen formalmente como propietarios y quién es el verdadero beneficiario, eh, final económico» | 3:43–3:51 | corte a la toma limpia («Quién aparece formalmente…», 3:52,8) |
| cubo 3D y 1,3 s de negro, dentro de otra toma repetida: «Posteriormente, se realiza la recolección… informe técnico de laboratorio» | 4:39–4:53 | se deja el «Posteriormente,» de la primera toma y corte a la segunda («la recolección y procesamiento… decisiones del fiscal») |
| negro al final | 5:27,3 | el clip termina antes |

- Los dos cortes caen en pausas, con fundidos de audio de 15 ms.
- Después de cada corte, hasta el final de la frase, va un plano más cerrado:
  1024×576 desde (96, 40), como en el cierre de Bienes. Así el salto se lee como
  cambio de plano.
- Esos planos se revisaron a 4 cuadros por segundo: la cara y el panel quedan
  enteros. En ellos no va ningún cartón.
- Los bordes de los tramos van a mitad de cuadro.
- `ic_pieza.tramos_vf` ahora admite un congelado al arranque de un tramo.

El clip queda en 5:04: 9.117 cuadros, con audio y video del mismo largo.

**Tres compuestos descartados** (en `01 VIDEO\_descartes`, con un `LEER`):
- **v1, con 5 cuadros de más.** Los congelados se medían en segundos con cuatro
  decimales.
- **v2, con 1 cuadro de más.** `trim=start/end` pasa los segundos a la base de
  tiempo del stream redondeando. Ahora `tramos_vf` corta el video por número de
  cuadro y el audio en los mismos tiempos.
- **v3, con manchas negras.** El congelado del fundido mostraba el cuadro 4366: el
  panel ya estaba limpio, pero el cielo y la cara todavía tenían manchas. Se vio en
  la tira de cuadros de cada corte.

## Encuadre

`perfil2.py` y una hoja de 16 cuadros con la caja dibujada:
- ella está al centro: la cabeza va de x≈615 a 860 de la fuente;
- **ventana estándar 1143×643, desde (0, 30)**:
  - el pelo empieza en x≈907 de salida (p10) y la columna estándar (615) termina en
    785;
  - abajo termina en y=673, antes del nombre quemado (y 683–705), que queda fuera;
  - el panel DAE/Fiscalía entra entero;
- **lower third** con el nombre a 44 px y el cargo a 560 de ancho, en tres
  renglones. Termina en x≈690; la chaqueta empieza en x≈730–750. Se simuló sobre
  siete cuadros.

## Textos

Salen de Scribe (WAV a 16 kHz, una voz), sin muletillas.
- 11 cartones, 8 listas de AE y el lower third.
- Todo cabe en la caja con cima ≥ 257.
- La última fila de cada lista queda al menos 4 s.
- La cobertura es de ~73 %. Es una lección densa y corta: se quitaron tres
  cartones que repetían a una lista o al cartón siguiente.

## Revisión

- **Hoja de `ic_revision`:** un cuadro por gráfico, más intro, título, cierre y outro.
- **Cuadros a tamaño completo:**
  - el lower third;
  - seis listas;
  - el congelado del fundido;
  - los dos planos cerrados;
  - el último cartón;
  - el primer cuadro del clip;
  - el cartón de cierre.
- **Una tira de 12 cuadros alrededor de cada corte y de cada congelado.** Fue la que
  mostró las manchas del v3.
- **El compuesto:** 9.117 cuadros, audio y video del mismo largo.

## Entrega (15 nov 2026)

MP4 con la receta de `Entrega_MP4_Fiscalia_Receta.md` (`mp4_entrega.py`).

| | |
|---|---|
| archivo (`05 EXPORTS`) | `delitosambientales - U3 - LECCION 4-v1.mp4` |
| largo | 5:38 (8.104 cuadros = línea) |
| peso | 177 MB |
| sonoridad / pico | −16,1 LUFS / −2,9 dBTP |
| PSNR contra el máster (medio / mínimo) | 50,5 / 45,0 dB |
| gráficos | 1 lower third, 11 cartones, 8 listas |
| máster | `D:\DAE\_masters_archivo\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\UNIDAD 3\LECCION 4` (1,0 GB); en `05 EXPORTS\_master` queda el `LEER` |

- **Estructura:**
  1. intro;
  2. cartón de título «… / Unidad 3. Lección 4»;
  3. clip (7.286 cuadros);
  4. cartón de cierre;
  5. outro.
- **Línea para Sebastián:** `10 TIMELINE SEBASTIAN\MA - U3 - LECCION 4.drt`.
  - V1: video.
  - V2: título y cartones.
  - V3: motion graphics, premultiplicados.
  - V4: lower third.
- **Drive:** curso → `VIDEOS/VIDEOS UNIDADES/videos exportados/UNIDAD 3 - LECCIÓN 4
  - La investigación financiera` (`138IERkCos3CdTH3SEjUCul6pLJ_sy5pv`).
  - La copia de paso de la fuente en `_MA subidas` está en la papelera.
