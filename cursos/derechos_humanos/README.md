# Derechos humanos aplicados a la función judicial · PRIORIDAD 2

Carpeta del Drive: https://drive.google.com/drive/folders/1rRgeOZ2lEWinTMDhOrk7Y3w8zG_58ALC —
cinco documentos, uno por unidad. Las entregas van a su subcarpeta «Videos»
**solo con el OK de Sebastián**.

## Cinco videos

| | título | ranuras | pieza (cuadros) |
|---|---|---|---|
| U1 | Llega la noticia | 13 | 3316 |
| U2 | La defensa invoca un tratado | 25 | 4822 |
| U3 | Dos versiones de la misma entrevista | 27 | 5343 |
| U4 | La medida de aseguramiento | 40 | 8529 |
| U5 | La decisión integral y el giro | 13 | 3504 |

Árbol: `E:\DAE MASTER\PRIORIDAD 2\CURSO - DERECHOS HUMANOS APLICADOS A LA FUNCION JUDICIAL\`
(00 DOCUMENTOS FUENTE, 00 PERSONAJES, UNIDAD 1..5 con las diez carpetas de la
serie). Bins iguales en el proyecto de Resolve `DAE MASTER - CURSOS`.

## Sin preguntas

Sebastián, 31 oct: ninguno de los videos lleva secciones de preguntas ni
respuestas. Lo que el documento pone como pregunta va a Moodle
(`guion_dh.FUERA_DEL_VIDEO`). Las instrucciones que quedan en la voz
(«registre su primera decisión», «márquelo cuando lo escuche», «Anote en su
bitácora…», la decisión integral de la U5) son el lugar de la pausa del H5P.

## Voces

ElevenLabs, cuenta de Sebastián, `eleven_multilingual_v2`. Carlos narra;
Carmen = Elisa María, Andrés = Leo, Entrevistador = Johan, Sandra y la
abogada Salgado = Milena (nunca hablan las dos en el mismo video), Quintero =
Pilar, Julián = Alejandro, Juez = Horacio. Los bloques `_tel` llevan filtro
telefónico (`armar_dh.TELEFONO`). La U4 cierra con un bloque `SILENCIO` («La
otra silla»): `aislar_silencio` lo corta en ranuras propias, sin voz.

## Reparto y lugares (todo en Colombia)

Hojas de personaje de Seedream 5 Flash para los nueve que tienen cara
(`personajes_dh.py`); Acosta solo de espaldas; presos, vecinos y colegas sin
rostro. El acento mostaza es SOLO el cárdigan de Carmen Elisa. Lugares:
pueblo andino con su plaza y mercado, la emisora comunitaria y su cabina, la
recepción de denuncias, la oficina abierta, la sala de entrevistas, el
despacho de la fiscal Quintero (en tres luces: mañana, tarde, anochecer), la
oficina de la defensa, la sala de audiencias y el pabellón.

## PIEL (31 oct, Sebastián lo vio en vivo)

Siete de las nueve hojas salieron con la piel durazno-rosada (mediana de
saturación 0,22-0,30, hasta 11 % de rosado) y las placas aprobadas entraban
como referencia **crudas**: la piel se copiaba y subía de plano en plano
(U2/U4/U5 a mediana 0,25, 3-8 % de rosado). Arreglo, ya en las
herramientas:

- `prompts/hojas_ref_dh.py`: hoja → limpieza de placa + `piel_ref` →
  `00 PERSONAJES\_piel_ref` (la original no se toca). Esas son las hojas de
  referencia (`prompts_dh.HOJA_ID`; las crudas en `HOJA_ID_CRUDA`).
- `prompts/piel_ref.py`: banda de piel (tono PIL 0-18 y el lado magenta) a
  s ≤ 0,15, tono hacia 25°. `subir_dh.py` lo aplica a toda referencia; un
  cuadro inicial de Kling sube tal cual (`"tipo": "kling"`).
- Las referencias de lugar son placas **graduadas** (`gen/placa_id.json`).
- Cláusulas: `base_dh.PIEL_DH` (todas las complexiones en la misma escala de
  gris, sin durazno, rubor, labios rojos ni sombras naranjas),
  `prompts_dh.REF_PIEL` (la placa de referencia es el techo de la piel) y la
  frase de la hoja en `HOJA(S)_REF` y `REFERENCIA`.

Resultado: candidatas nuevas a mediana 0,09-0,17 y ~0 % de rosado. Las placas
de antes quedan ≤ 0,20 y sin rosado por `elegir` (limpia) y `construir`
(grade); se miden todas las `_grade` antes de montar.

## Encuadre: lecciones del curso

- Con un ancla de dos personas como referencia de lugar, los primeros planos
  salen como plano de dos y con la persona duplicada: el primer plano lleva
  de referencia un primer plano aprobado del mismo cuarto y el texto dice
  «ALONE in the frame… appears ONCE».
- Acosta salió de perfil dos veces (U4 r22): la referencia es una placa
  aprobada de él de espaldas (U4 r16) y el texto dice «only the back of his
  head».
- «numbered list» trae números: «ONLY plain flat grey bars… no numerals».
- U4 r23 y r34 son copias de U2 r13 b y U2 r22 a (`COPIA`).

## Cartones y rótulos

`cartones_dh.ELEGIDOS`, escogidos a mano, VERBATIM (U1 9 · U2 13 · U3 11 ·
U4 23 · U5 7): los datos, los tres caminos y los cuatro pasos del análisis de
convencionalidad (U2), las cuatro marcas (U3), las tres cargas, los cuatro
hechos y las tres decisiones del juez (U4), el epílogo mudo de la U4 (entra
por proporción). Rótulo y cartón nunca comparten ranura (medido con Scribe):
los rótulos van en `lowerthirds_dh.LOWERS`.

## Movimiento

Kling 3.0 (`kling-30`, 1080p, cuadro inicial = placa graduada) solo para
acción real: U1 r01, r02, r13 · U2 r01 · U3 r01, r09, r25 · U5 r08, r13, y
el detalle de la moto en la U1 r05 (`prompts/kling_dh.json`). Fuera en la revisión: U3 r02 (ver abajo) y U4 r40
(Kling disolvió la fila del pabellón); las dos ranuras quedan con la cámara
de la casa. Quien solo habla (U2 r13, r21; U4
r06, r24, r28) queda con la cámara de la casa: Kling deforma las caras al
hablar. Los detalles (`DET`, V3) van con `detalle_dh quieto` (placa de
detalle graduada con empuje lento), con la piel igualada a la madre.

## Revisión propia antes de entregar (31 oct, noche)

- **Rótulos contra cartones:** el primer montaje dejó rótulos debajo de
  cartones que venían de la ranura anterior (el último cartón de un bloque se
  estira). Se midió con los tiempos quemados (`D:\DAE\_tmp\dh\cartones_dh.json`) y se
  movieron: Carmen U1 r03 +40, Andrés U1 r08 +67 con 96 cuadros
  (`LOWERS` acepta `'cuadros'`), Quintero U4 → r21, Salgado U4 r24 +52,
  Sandra U5 r02 +74; fuera Salgado en la U2 y la apoderada en la U4. Datos de
  rótulo sin punto final, todos.
- **U2, Gelman:** el cartón empezaba en «Que es tarea…»; ahora «Control de
  convencionalidad, que es tarea de cualquier autoridad pública (Gelman vs.
  Uruguay, 2011, párr. 239).»
- **U1 r13:** Kling escribió «COMMUNITY RADIO» en la caja de luz (la placa la
  tiene lisa). `montaje/parche_caja_dh.py` la rellena cuadro a cuadro con el
  fondo del letrero (rectángulo fijo 918-1043 × 639-680).
- **U3 r02:** el clip de Kling hacía que el entrevistador mirara a Carmen al
  señalar la silla (la escena pide lo contrario): fuera; la ranura queda con
  la cámara de la casa.
- **U5, cielo:** el atardecer en la ventana quedaba salmón. `dh_pieza.CIELO`
  apaga la banda cálida/rosada en lo claro (v > 150, rampa de 40) a s ≤ 0,05
  y lleva su tono a 28° (gris cálido, la misma regla de la piel) en la placa
  graduada, en Kling (`mov_dh`) y en los detalles. Con s ≤ 0,10 (primer
  intento) la hoja seguía mostrando las nubes rosadas.
- Se dejan como están: cuatro cartones a 17-19 car/s que dicen lo mismo que
  la voz en ese momento (U2 «Camino C», «¿Cómo se motiva…», U3 «Cuatro…», «La
  diferencia…»): darles más tiempo obligaría a montarlos sobre el bloque
  siguiente.

## Primera revisión de Sebastián en la línea (31 oct, noche)

- **U1 r05, 00:58:** «anatomically incorrect, weird positioning of the hands;
  we should portray the scene with character being followed by a bike».
  Lo roto era el detalle V3 (el teléfono en dos manos, los dedos cruzando la
  pantalla). En su lugar, con la frase «el martes una moto me siguió desde la
  emisora hasta mi casa» (V3 1313-1397, el mismo sitio y largo): Carmen camina
  por una calle del pueblo y una moto la sigue despacio, el motociclista con
  casco cerrado de visor oscuro, sin placa. Placa de Seedream con la hoja de
  Carmen y la calle de la emisora (U1 r02) como lugar; Kling 3.0, 84 primeros
  cuadros sin retime (`detalle_dh.CORTE`). Kling hizo un travelling hacia
  atrás con ella (la regla es cámara quieta): se deja porque es lo que cuenta
  la escena. `prompts_dh.video` acepta detalles de OTRO lugar ('ref', 'hojas',
  'lugar').
- Se probó rehacer la placa de la r05 con una mano: salió casi igual y la
  aprobada ya tiene los dos antebrazos con su puño. Se quedó la aprobada (la
  ranura volvió a ser idéntica, diferencia 0).
- Cambio en la línea con `reemplazar_en_sitio_dh.py` (nuevo=>>viejo): retrato
  idéntico antes y después, 41 clips; nada de lo que Sebastián movió se tocó.
- Revisados los otros nueve detalles del curso (manos): ninguno roto.

## Entregas

Carpeta «Videos» del Drive (creada el 31 oct dentro de «PRIORIDAD 2 - DDHH
APLICADOS A LA FUNCIÓN JUDICIAL»): `1Oa_NdV5Uwl6IgMccYY-BO38RofKr7iAk`.
Nombre: `PRIO 2 - DERECHOS HUMANOS - UNIDAD <n> <TÍTULO>.mp4`. Camino:
`dh_pieza <L> exportar entregas verificar` → `G:\My Drive\_DH subidas` (md5
igual) → sincroniza → `update_file(parentId=Videos)`.

- U1 (31 oct): 3316 cuadros, −20,0 LUFS, pico −3,6, 38 MB.

## Revisión de Sebastián de la U2 (31 oct, noche)

Todo entra en SU línea sin remontar: `reemplazar_en_sitio_dh` (nuevo=>>viejo,
siempre a un archivo de NOMBRE distinto: Resolve guarda lo decodificado y un
reemplazo con el mismo nombre puede no llegar al render) y `cirugia_dh`
(poner un item, con retrato antes/después; devuelve a Sebastián a la línea y
la página en que estaba).

- **Cenital entre r01 y r02:** inserto V3 en los últimos 96 cuadros de la r01
  (`DET (1, 'el_despacho_desde_arriba')`, placa con las dos hojas y la r01
  de lugar, cámara de la casa).
- **r02 con el fondo de la r01:** era imposible (la vemos de frente). Ahora la
  cámara mira a la pared de la ventana (referencia de lugar: la r18). La r05
  tenía el mismo problema y se rehizo igual.
- **r04 («¿quién es ella?»):** Quintero coteja el escrito con los registros
  telefónicos del expediente (lo que dice la voz). Salgado se presenta con su
  rótulo en la r14 (cuadros 2-72, antes del cartón).
- **r07, r12, r21, r22 con movimiento** (Kling): la bandeja; Julián cuelga el
  teléfono (placa nueva, la r12 ya no es el cajón); Quintero y el juez
  parpadean, asienten, mueven un poco las manos (10 s, boca cerrada). La
  primera r21 hizo un empuje de cámara y metió una espalda por el borde: se
  rehízo con «locked-off», sin figura en primer plano.
- **r09, la voz del juez:** −20,1 LUFS contra −18,7 de Carlos. +2 dB solo en su
  bloque (59,1-66,5 s del narrador, rampas en el silencio): −18,1, pico −3,0.
- **Rótulo de Carmen Elisa en la r13** (no aparece antes en la U2).
- **2:58 (b18, cartón p13):** Sebastián (1 nov): «Ni rechazo reflejo… ni
  retirada refleja» se leía como verbos. Ahora, voz y cartón: «Ni el rechazo
  automático (camino A) ni la retirada automática (camino B): el camino C es
  el del análisis.» Toma nueva de Carlos (`retomar_dh candidatos`, la 2 de 4,
  6,26 s de habla, `atempo` 1,03), puesta a mano en el narrador: empieza 0,6
  s antes (163,075 s) y la b19 se corre 0,47 s (la cola del archivo tenía
  sitio). Mismo largo de archivo, −19,2 LUFS como la b17. Rejilla, crudo y
  stt al día. Cartón `DH_U2_p13_carton_v2.mov`, 197 cuadros como en su línea.
- **Música:** Sebastián recortaba a mano la cama para que no pisara el intro.
  Ahora `cama_musica` calla antes de `abre` (intro − 23 cuadros, como la dejó
  él en la U2) y termina de salir en el primer cuadro del outro. U3-U5
  rehechas y releídas en su línea; la U1 (entregada) y la U2 (recortada por
  él) no se tocan. Regla en la biblia (§10).

## U3: la voz del entrevistador (1 nov)

Sebastián: «the voice of the interviewer in DH U3 is weird, can you clean it
up?». Medido: las cuatro tomas de Johan (c02, c04, c06, c08) tenían la voz
ronca y con ruido (relación armónico/ruido 1,7 dB contra 7-8 de Carmen y
Sandra; pausas a −51/−65 dB contra −88). Arreglo sin mover un cuadro:
**voz a voz** (`elevenlabs.py transformar`, modelo
`eleven_multilingual_sts_v2`) de cada toma a **Jerome** —misma actuación,
mismas pausas, mismo largo—, puesta en su ventana con `retomar_dh poner
--sin-repartir`. Se probaron Iván, Alexander y Horacio: Jerome salió el más
limpio. `remove_background_noise` va APAGADO: con él se comía el arranque de
las palabras («Porque» → «que»). Scribe oye las cuatro igual que las de Johan.
Resultado: relación armónico/ruido 4,0-4,7 dB, pausas −68/−84 dB, c04 +1,6 dB
para quedar como las otras (−19,8 LUFS). En su línea: `DH_U3_NARRADOR_v3.wav`
(ReplaceClip, retrato idéntico, 55 clips).

**Revertido el mismo día.** Sebastián: «now it sounds worse, mucho golpe de
viento en el micrófono… quiero que realces la voz, no que la dañes». Jerome
fuera; vuelven las cuatro tomas de **Johan** tal cual (crudos, stt y
`habla_master` de la rejilla restaurados) y sobre el master original solo
dentro de las cuatro ventanas (±60 ms): EQ **+2 dB a 280 Hz, Q 1** (presencia
en medios bajos) y ganancia por bloque para quedar **~+1,5 dB** sobre como
estaba, con techo −17,8 LUFS (`herramientas/voz/realce_entrevistador_u3.py`). Medido, antes →
después: c02 −20,0 → −18,4, c04 −19,8 → −18,3, c06 −19,2 → −17,9,
c08 −18,7 → −17,9 LUFS; picos ≤ −2,9 dBFS, sin limitador. Fuera de las
ventanas el master es bit a bit el original; mismo largo (9 394 531
muestras). En su línea: `DH_U3_NARRADOR_v4.wav`. Lección: a la voz de un
personaje que ya está aprobado se la realza (EQ, nivel); cambiarla de voz es
otra decisión y se pregunta. Si el master de la U3 se vuelve a armar con
`retomar_dh`, hay que volver a correr el realce.

## U3 apretada y con más animación (1 nov)

Sebastián: «we need to shorten some of the narration gaps… it sounds
glitchy, also make the other characters besides the main narrator talk a bit
faster, it's like they are dragging the video, also we need every other clip
where they talk to have mouth movement, not necessarily sync… en general
necesita más animación, deja los otros cambios que hice».

**La voz** (`herramientas/voz/apretar_dh.py`, plan en
`D:\DAE\_tmp\dh\u3_apretado\`: `mapa_u3.py`, `final_u3.py`). Sobre el master
v4 (con el realce del entrevistador), con la envolvente a −48 dB:
- huecos entre bloques: 0,45 s entre personajes, 1,0 s cuando entra o sale el
  narrador, 0,65-0,9 entre bloques de Carlos; los que pesan quedan algo más
  largos (c09 «…Nada» 0,85; «Tómese su tiempo» 1,3; c10 1,15). Un hueco que se
  acorta conserva sus dos orillas (la cola de la frase y el aire antes de la
  siguiente) y pierde el medio: todos los cortes caen en silencio.
- pausas internas: las de los personajes de 0,40 s o más quedan en 0,34; las
  de Carlos de 0,55 o más, en 0,45 (eran los «…» del guion, hasta 1 s).
- tempo (`atempo`, no cambia el tono): Sandra 1,12; Carmen y el
  Entrevistador 1,08; Carlos igual.
- 195,7 s → 156,65 s (huecos −22,8 s, pausas −8,5, habla −7,9). Nivel y
  timbre intactos: −18,8 LUFS integrado, pico −3,0; el pico de diferencia
  entre muestras es la «T» de «Tres» que ya estaba en el original (no hay
  clics nuevos). `atempo` deja unos ms por bloque: el mapa se corrigió con
  los arranques medidos en el master armado (deriva final 0,1 s).
- `03 VOCES`: `DH_U3_NARRADOR.wav` y `_v5`, rejilla, ranuras y los 25 stt
  pasados por el mapa; los de antes en `_descartes` con
  `__antes_de_apretar_<hora>`. Ojo: `retomar_dh` sobre la U3 rearma desde
  los crudos sin apretar; si hace falta una toma nueva, se pone a mano y se
  vuelve a apretar ese bloque.

**La línea** (`herramientas/montaje/apretar_linea_dh.py`), hecha desde la
SUYA, item por item, con el mismo mapa: 5295 → 4358 cuadros (3:41 → 3:02).
Sus cambios siguen: sin el respiro final, cartón p03 con su recorte (termina
antes del corte a la r11), la cama terminando donde empieza el outro. Su
línea quedó como «… (antes de apretar)»; nada se borró del pool.
- V1: ranuras simples cortadas (`apretar_ranuras_dh.py`, el horneado es sin
  empuje); las compuestas (r09, r10, r13, r18) rehorneadas con el corte
  pasado por el mapa (151 «Dos», 75 «Ahora vea», 67 «Tómese», 91 «Nada»).
- V3: detalles cortados (las manos 50, los ojos 53).
- V4: los 11 cartones requemados al largo nuevo (`cartones_apretados_dh.py`,
  `_ap<cuadros>.mov`), entrando en la misma palabra; si el mapa los dejaba
  más densos se les devolvió su largo de antes mientras cupiera (p04 17,1,
  p05 20,2 y p10 19,0 car/s: no caben más, el siguiente entra detrás).
- V6/V8: marca de agua y rótulo de Sandra con su largo, corridos.
- A5: cama rehecha con la rejilla nueva (`abre`/`cierra`).

**Kling 3.0** (boca sin sincronía: «habla genérica», nunca abierta del
todo): r04, r06, r14, r15, r16, r17, r20, r22, r23 con boca; r05 (él habla de
espaldas, ella se endereza), r07 (el lapicero), r24 (la tarjeta pasa de mano)
y r26 (la oficina al fondo). Más los tres de antes reconformados (r01, r09,
r25). r06 y r20 (REUSA al 0,7) salen del cuadro 0 de la ranura y se
conforman sin recorte (`KLING_DESDE_RANURA`). Descartes: r03 dos veces (él
toma la carpeta; luego la cámara se corre), r16 y r20 una vez (guiño y
sonrisa con dientes; el cuerpo se mecía). r08 y r19 no llevan: el detalle de
V3 los tapa casi enteros. Créditos: 9.000 (quedan 18.850).
