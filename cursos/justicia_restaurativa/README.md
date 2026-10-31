# Justicia restaurativa · PRIORIDAD 1

Carpeta del Drive (de JP Soluciones Digitales):
https://drive.google.com/drive/folders/1Bzc28eFvCSbYng8nxjhLEQ3GOxoH53Rl —
cinco documentos («Casos 1 y 2», «Unidad 1» a «Unidad 4»). Las entregas van a
su subcarpeta **«Videos»**
(https://drive.google.com/drive/folders/1_RSBf53etpkeY264s4_90eYkatBLqgHE),
**solo con el OK de Sebastián**, todas juntas y distinguidas por el nombre.

## Seis videos

| | fuente | palabras | voz | ranuras · placas | pieza |
|---|---|---|---|---|---|
| C1 «Una discusión en un sitio público» | «Casos 1 y 2» → enlace al .pptx «Preguntas sobre Mediación. Curso JR», diapositiva «CASO PLANTEADO» | 170 | Pilar | 9 · 9 | 2344 · 1:37,8 |
| C2 «Fase 1 — La historia» (de lesividad alta) | «Casos 1 y 2», Caso 2 | 505 | Carlos | 29 · 22 | 6268 · 4:21,4 |
| U1 «El encuentro en la carretera» | «Unidad 1» | 143 | Pilar | 10 · 10 | 2339 · 1:37,6 |
| U2 «La situación reflexiva» | «Unidad 2» | 203 | Carlos · Juana | 11 · 7 | 2605 · 1:48,7 |
| U3 «Prosigue la situación reflexiva» | «Unidad 3» | 671 | Carlos · Juana | 32 · 22 | 6571 · 4:34,1 |
| U4 «Culminamos la situación con diversas reflexiones» | «Unidad 4» | 673 | Carlos · Juana | 35 · 24 | 6984 · 4:51,3 |

Sebastián no sabe a qué unidad pertenecen los casos 1 y 2 (quizá a una
introducción): por eso todo va a una sola carpeta «Videos» y se distinguen
por el nombre (`PRIO 1 - JUSTICIA RESTAURATIVA - CASO 1 ...`, `... - UNIDAD 3 ...`).

## Sin preguntas

Sebastián, 30 oct: *«all questions segments must not be part of the video
itself … they will deploy it thru the moodle»*. Sale el segmento entero:
enunciado, opciones, respuesta y la retroalimentación que la explica (en la
U1 eso incluye los comentarios de cada fase y el cierre de la respuesta C;
en la U2, el «RESPUESTA: Falso…»). Dicha en el video, la retroalimentación le
daría la respuesta a la pregunta que Moodle hace después. Queda guardada en
`guion_jr.FUERA_DEL_VIDEO` por si la agencia la quiere.

En la U2 la narración sigue con «Tras contestarle, usted…», que es lo que el
documento escribe: la respuesta ocurre fuera del video, en Moodle.

## Erratas y una alerta de contenido

Corregido lo obvio (regla de la casa): «envanece» → «envanecían» (U2),
«no tiene qué» → «no tiene que» (U3), «Sepulveda» → «Sepúlveda» (C2).

**No corregido, para que lo vea Sebastián:** la U2 dice «Pierre, soldado
francés, estaba frente al pelotón de fusilamiento ruso». En *Guerra y paz*
Pierre Bezújov es ruso y civil, y la mirada que lo salva es con el mariscal
francés Davout. Va verbatim; si el profesor lo corrige, es una toma de voz
(`a03_tolstoi`) y un cartón.

## Voces

ElevenLabs, cuenta de Sebastián, `eleven_multilingual_v2`. Carlos y Pilar,
las de la serie, y **Juana con la voz de Elisa María** (la de los casos del
profe Carlos Humberto): en las unidades 2 a 4 el narrador le habla a «usted,
fiscal», y lo que el fiscal dice o lee en voz alta (Tolstói, Hillman,
Thiebaut, la historia de Rubiano) va en la voz del narrador; Juana dice sus
parlamentos. 97 tomas, todas oídas por Scribe: las únicas diferencias son
cifras que Scribe escribe en dígitos y los nombres dichos a la española
(Van Gog, Jílman, Yung, Tiebó). «doctor(a)» se dice «doctor» (la voz del
fiscal es la de Carlos); el cartón conserva «doctor(a)».

Máster a −19 LUFS, techo −2 dBFS, por la mediana del short-term con voz.
**Nuevo en `armar_jr`:** los parlamentos de menos de un segundo («Ajá…»,
«le dice,») no llenan una ventana de 3 s; se nivelan por el momentary
corrido. Peor salto entre bloques: 0,10 / 0,35 / 0,25 / 0,35 / 0,65 / 0,60
LU. Y las ranuras de menos de 96 cuadros que dejaban esos parlamentos se
funden con la vecina (`fusionar_cortas`).

Rejilla recortada por palabra (`recortar_jr.CORTES`): C1 en «y con
posterioridad» (la ventanilla y el despacho son dos lugares); U1 en «Al
intentar adelantar», «Más adelante» y «La policía llega».

## Sistema visual

El de la serie (biblia P3 / DF / GJ). Lo propio del curso, en `base_jr.py`:

- **U2-U4 son una sola conversación en una sola oficina**, en tres luces:
  mañana, mediodía, tarde. **El fiscal es la cámara** («usted», sin género
  en el documento): se ven sus manos y, sobre el hombro, su espalda.
- **Lo recordado va en otro registro** (contraluz / hero, siluetas): la
  mirada de Tolstói, el hombre cansado de Van Gogh, el jardín de Rubiano,
  Dante y Virgilio.
- **Acento**: Ana (bufanda, C1), Camilo (suéter, C2), Mario (suéter, U1),
  Juana (bufanda, U2-U4).
- **Sin cara**: Juan y su defensor, el legista, los procesados (siluetas),
  el fiscal «usted». La violencia no se dibuja nunca: C1 es el bolso en el
  piso; C2 el andén vacío y dos siluetas quietas; U1 el antes (frente a
  frente, un metro de aire) y el después (vidrios, el resplandor de lejos,
  el casco calcinado). El hombre del jardín no toca al niño en imagen.

## Placas: Seedream 5 Flash

Prueba del mismo prompt de oficina en Pro (100), Lite (50) y **Flash (35)**:
Flash da el mismo estilo (la hoja de Juana y la oficina se sostienen) por un
tercio. 94 placas × 2 candidatas + 6 hojas × 2 + 3 repeticiones.

**Una ranura puede reusar la placa de otra** (`REUSA` en `escenas_jr_*`,
biblia §4: la unidad es la escena, no la placa): 32 de las 126 ranuras
toman la placa de su madre con otra cámara (`encuadre`, `empuje`,
`centro`). `jr_pieza elegir/construir` lo aplican.

Repeticiones (`elegidas_jr.json["_motivos"]`): C2 r23 (uno de los procesados
salía con pelo largo), U3 r32 y U4 r08 (el modelo le copiaba la melena de
Juana a la espalda del fiscal: el token pide ahora «SHORT dark hair cut
close at the neck»).

## Movimiento y detalles

Nueve clips de Kling 3.0 donde el movimiento es real y robusto
(`kling_jr.json`): C1 r07 (los dos se alejan por el corredor), C2 r09 (una
moto cruza), U1 r01 (el carro por la carretera), U1 r09 (el humo), U2 r01
(Juana entra), U3 r08 (el niño corre a la madre, siluetas), U4 r06 (el
café), U4 r32 (las manos en la escalera), U4 r35 (Juana se levanta). Los
nueve salieron a la primera; ninguno se repitió. Dos notas: en U2 r01
Kling metió la mano del fiscal a tomar la taza a los 3,8 s, y
`bajar_mov_jr.py` recorta el crudo a 3,7 s antes del conformado (el retime
al largo de la ranura hace el resto); en U4 r32 las siluetas, después de
tomarse la mano, suben un par de peldaños (el prompt pedía que no), y se
queda porque es exactamente lo que dice el texto. Nueve rampas de luz sin
modelo (`mov_jr.LUZ`).

**Detalles: 15 insertos de 72 cuadros, ninguno con Kling.** Sin gesto no
hay modelo: `detalle_jr.py quieto` le hace a la placa de detalle graduada
la cámara de la casa (empuje lento, vibra 4) y `conformar` lo trata como a
un crudo (la placa va a 2560 porque el riel de `camara` exige ventana ≥
1920/ancho). Lo que se aprendió con las placas de detalle: con «CLOSER
SHOT OF THE SAME SCENE» + la madre como referencia, Seedream devolvía
casi la misma composición de la madre (un salto de eje al cortar), le
copiaba la melena de Juana a la espalda del fiscal (U2 r10) o metía
escudo, bandera y retrato en la pared (U3 r23). La fórmula que sirve, para
la biblia: **«MACRO INSERT ... the reference image gives ONLY the palette,
the light and the flat graphic style: this image is a much tighter
framing of the same desk, not a copy of the reference composition ... NO
head, NO face, NO hair, NO shoulders, NO second person»**. Siete detalles
se rehicieron así (U1 r03 —la primera traía la cara de Diego gritando, y
la decisión equivocada no va en una cara—, U1 r06, U2 r10, U3 r19, U3
r23, U4 r08, U4 r26); U1 r06 se rehizo dos veces porque la segunda era de
noche con faros y la madre es día nublado. Motivos en
`elegidas_jr.json["_motivos"]["_detalles"]`.

## Líneas y revisión interna

`jr_pieza.py <L> montar` arma la línea en `DAE MASTER - CURSOS` (bins
espejo, V1 ranuras, V2 movimiento, V3 detalle, V4 cartones, V6 marca de
agua, V8 lower third; A1 narrador, A4 ambiente, A5 música) y exporta el
`.drt` a `10 TIMELINE SEBASTIAN`. `revisar` rinde a
`D:\DAE\_tmp\jr\revision` (nunca a 05 EXPORTS) y mide:

| | cuadros | LUFS | pico | negros |
|---|---|---|---|---|
| C1 | 2344/2344 | −19,8 | −4,5 | ninguno |
| U1 | 2339/2339 | −20,3 | −4,6 | ninguno |
| C2 | 6268/6268 | −19,4 | −3,9 | ninguno |
| U2 | 2605/2605 | −19,6 | −4,4 | ninguno |
| U3 | 6571/6571 | −19,3 | −3,9 | ninguno |
| U4 | ver `cad_K.log` | | | |

Las hojas `revision_<L>_v1.jpg` (un cuadro a mitad de cada ranura, cada
detalle, cada movimiento y cada rótulo) están en `D:\DAE\_tmp\jr`.

## Revisión de Sebastián, 31 oct · C2

La línea ya la había tocado (un inserto del cerrojo puesto a mano en V3,
cuadro 5138): nada se remonta. Todo entra por `reemplazar_en_sitio_jr`
(mismo nombre, mismo largo, `ReplaceClip`) o por `cirugia_jr.py` (quitar o
poner UN item, o rehacer V4 entera), con retrato antes y después. Lo que
pidió y lo que se hizo:

- **r04**: otro plano de Camilo como presentación, el actual con menos
  tiempo, y el rótulo que faltaba. La ranura es ahora **compuesta**
  (`escenas_jr_c2.COMPUESTAS`): 84 cuadros del plano ancho mientras sale el
  cartón p01, y luego el plano de frente (placa EXTRA `r04b_camilo_de_frente`,
  con la hoja) con el rótulo «Camilo Andrés Ferreira Buitrago · 27 años,
  trabajador independiente.» (`lowerthirds_jr.LOWERS['C2']`, entra en el
  cuadro 96 de la ranura, cuando el cartón ya salió). La primera tirada del
  plano de frente traía el nombre ESCRITO en la imagen —el prompt decía
  «with his name under him»—: nunca describir el rótulo en el prompt.
- **r05**: Ferreira huyendo de la escena, herido, la mano derecha en el lado
  izquierdo del pecho, la cara preocupada, una sombra al fondo del callejón.
  Sin sangre ni arma. Placa nueva (c) con la hoja y la calle vacía anterior
  como referencia; la rampa de luz se rehizo sobre ella.
- **p06**: el perfil completo. Dos cartones nuevos: «Perfil de la víctima.
  Nombre…» y «Edad y ocupación: 27 años, trabajador independiente. Relación
  con los procesados: ninguna; no se conocían antes de los hechos.» (separados
  salían a 16 car/s). V4 se rehízo entera con `cirugia_jr C2 v4`.
- **r12**: primero la radiografía (placa EXTRA `r12a_la_radiografia`, 206
  cuadros, hasta «urgencia») y la venda en «laceración en el brazo».
- **r17, la voz**: «Jairo Ortiz … Cuéllar» con un segundo de pausa y el
  acento en la a. `voz/retomar_jr.py`: pide variantes (la mitad con la
  grafía «Cuéyar», que es lo que el modelo lee bien), las oye con Scribe y
  mide la pausa; la elegida (16,5 s en una ventana de 20,6) entra EN LA MISMA
  VENTANA del master, nivelada al short-term de la toma vieja, y el sobrante
  se reparte en las pausas internas de coma y dos puntos (+0,4 s cada una)
  en vez de dejar cinco segundos de silencio al final. Rejilla y ranuras no
  cambian; los cartones se recalculan por palabra (`cartones_jr.NUM_PAL`:
  «Procesado 1» contra «procesado uno»).
- **2:40**: r19 pasa de la reja vacía a las dos sombras sentadas en la celda
  (`la_celda`, placa nueva con la r08 como referencia); el cerrojo sigue como
  inserto.
- **r25**: fuera el inserto de la carpeta (saltaba del zoom a la placa); la
  ranura lleva ahora un empuje continuo del 14 % (`escenas_jr_c2.CAMARA`).
- **r28**: la placa era negro puro alrededor de la ventana. Placa nueva con
  una cláusula de luz propia («the room is lit by its spill… NO pure black»)
  y graduada **sin techo** (`SIN_TECHO = {28}`): 20/60/200.
- **Dos reglas nuevas en `construir`**, de paso: `nivelar_acento` gira el
  acento a los 42° de la serie cuando una placa se va más de 8° (r04 y 04b
  salían a 54-57°, limón en vez de mostaza) y `piso_negro` le sube el pie a
  16 a la placa que quede con p2 bajo 10 (la r05 nueva traía 5 % del cuadro
  en negro 0).

Créditos: 6 placas Flash (210). Revisión interna: 6268/6268, −19,4 LUFS,
sin negros.

## Créditos de Magnific

| | créditos |
|---|---|
| prueba de modelos (Pro / Flash / Lite) | 185 |
| hojas de personaje (6 × 2, Flash) | 420 |
| placas (94 × 2, Flash) | 6.580 |
| repeticiones (3 × 2) | 210 |
| Kling 3.0, 9 clips (6 + 6 + 4 + 5 + 5 + 6 + 5 + 5 + 5 s a 90/s) | 4.230 |
| placas de detalle (15 + 8 rehechas, Flash, 1 candidata) | 805 |
| revisión del C2, 31 oct (6 placas) | 210 |
| **total del curso** | **12.640** |

Contra los ~22.000 de Gerencia judicial (tres videos) es la mitad por
video: Flash en vez de Pro para las placas, una candidata por detalle,
nada de Kling en los detalles, y las rampas de luz sin modelo.

## Herramientas

Las de Gerencia judicial con sufijo `_jr`, más `rejilla/cruce_jr.py` (la
rejilla cruzada con Scribe, para el storyboard y los cortes por palabra).
Ver `cursos/gerencia_judicial/README.md` para lo que hace cada una.

## Dónde está cada cosa

```
E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\
  00 DOCUMENTOS FUENTE\   00 PERSONAJES\   (6 hojas + _crudos)
  CASO 1 - Una discusion en un sitio publico\     (las diez carpetas)
  CASO 2 - Fase 1 La historia\
  UNIDAD 1 - El encuentro en la carretera\
  UNIDAD 2 - La situacion reflexiva\
  UNIDAD 3 - Prosigue la situacion reflexiva\
  UNIDAD 4 - Culminamos la situacion\
```

Bins espejo en `DAE MASTER - CURSOS` › PRIORIDAD 1 › CURSO - JUSTICIA
RESTAURATIVA. Al lado, en PRIORIDAD 1, sigue «PROFE CARLOS HUMBERTO», que no
se toca.
