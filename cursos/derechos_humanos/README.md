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
