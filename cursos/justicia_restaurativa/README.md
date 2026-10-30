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
café), U4 r32 (las manos en la escalera), U4 r35 (Juana se levanta).
Nueve rampas de luz sin modelo (`mov_jr.LUZ`).

## Créditos de Magnific

| | créditos |
|---|---|
| prueba de modelos (Pro / Flash / Lite) | 185 |
| hojas de personaje (6 × 2, Flash) | 420 |
| placas (94 × 2, Flash) | 6.580 |
| repeticiones (3 × 2) | 210 |

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
