# Enfoque diferencial en la práctica del fiscal · PRIORIDAD 2

Carpeta del Drive: `1gp1dof3SncgICHNNiuEW3HHBYxdSCZDJ` («PRIORIDAD 2 -
ENFOQUE DIFERENCIAL EN LA PRÁCTICA DEL FISCAL»). Los cinco casos no son de
ninguna unidad: van en `VIDEOS` (`1qKmKVuwmNGKaTLbzgtm2pc5-uqf98k9u`). Las
entregas suben **solo con el OK de Sebastián**.

Árbol: `E:\DAE MASTER\PRIORIDAD 2\CURSO - ENFOQUE DIFERENCIAL\` (00 DOCUMENTOS
FUENTE, 00 PERSONAJES, VIDEOS\CASO 1..5 con las diez carpetas de la serie).
Bins iguales en `DAE MASTER - CURSOS`, vecino de Gerencia judicial y Derechos
humanos dentro de «PRIORIDAD 2». Rutas en `herramientas/voz/textos/rutas_ed.py`;
metadatos y textos en `guion_ed.py`.

PRIORIDAD 0X / X (Sebastián, 3 nov): si conviven «PRIORIDAD 2» y «PRIORIDAD
02» se funden en la de un dígito. Medido en disco y en el pool: no hay ningún
par duplicado (solo «PRIORIDAD 03», sin «3»), así que no se tocó nada.

## Lo que pidió Sebastián (3 nov)

- El guion empieza DESPUÉS del subtítulo «Fase de experiencia concreta» (ese
  subtítulo no va en el video). Verbatim.
- «De pe a pa», cinematográfico, como película: varios ángulos, los mismos
  personajes, consistencia, planos a media acción, varios planos
  complementarios de la misma escena.
- Reservar ~2.000 créditos de Magnific para cambios.

## Cinco videos

| | narra | ranuras | cuadros de narración | acento | rótulo |
|---|---|---|---|---|---|
| C1 Édgar Molano | Carlos | 23 | 4314 | cárdigan de Yolanda | Molano (r01) |
| C2 Jairo Montero Salas | Pilar | 31 | 5396 | la camisa del cumpleaños | Jairo (r01), Mauricio (r22) |
| C3 El patrullero Wilmer | Carlos (+ Andrés: la frase de Wilmer) | 25 | 4697 | sin acento | Wilmer (r01) |
| C4 La niña del resguardo de Putumayo | Pilar | 19 | 3772 | blusa de la madre | — |
| C5 La denuncia de Valentina | Pilar (+ Julián: el funcionario) | 20 | 3531 | abrigo de Valentina | Valentina (r02) |

Receta de la serie (`montaje/ed_pieza.py`): voz → rejilla → cruce → escenas →
placas → `elegir` → `construir` → detalles → Kling → cartones → rótulos →
blancos → música → `montar` → `revisar`. Geometría: intro 182 · entrada 119 ·
ranuras · respiro 48 · cierre 119 · outro 182.

## Puesta en escena (biblia P3)

Cada caso es una película corta: lugares con placa ancla (primera tanda, con
una placa aprobada de Ley 1826 como referencia de ESTILO) y el resto de los
planos pedidos con su ancla como referencia de LUGAR o del MISMO plano.
`prompts/escenas_ed_c1..c5.py` traen, por ranura, lo que se oye encima, quién
lleva cara y por qué, las rimas y los insertos.

Lo que no se dibuja nunca: el crimen de Jairo (ni cuerpo ni arma: el estante
con el hueco y la silla con la camisa), los golpes a Wilmer (la mano en el
antebrazo, los celulares en alto), la niña de Putumayo (su camino, su morral),
el abuso (la puerta cerrada). Agresores y quien amenaza: silueta o de
espaldas. Ninguna decisión equivocada cae sobre una cara: el coronel, el fiscal
de turno, el fiscal de la hipótesis «pasional» y el funcionario de la
recepción van de espaldas o en manos.

Rimas: la carpeta delgada (C1 r06) y la gruesa (r23); la sala de psicología
vacía (C1 r07) y ocupada (r21); las dos mecedoras (C2 r22) y la mecedora vacía
(r31); el formato con una casilla (C3 r15) y con tres (r23); el Taita en su
porche al principio y al final (C4 r02, r19); la única casilla (C5 r13) y la
mano que escribe en ella (r15).

## Placas y créditos

Seedream 5 Flash 2k 16:9 (35 créditos). 118 ranuras: 115 placas + 3 que
reusan otra con cámara distinta (C1 r18←r10, C2 r12←r09, C5 r08←r07), y 9
insertos de detalle. Cinco tandas; 19 placas rehechas por defectos medidos en
la hoja de contacto (una persona dos veces, texto legible —«NO» en las
chaquetas salió de escribir «NO badge» en mayúsculas—, caras de agresores,
insignias, la camisa ignorada con parche). Elegidas en
`prompts/elegidas_ed.json`; identificadores en `prompts/placa_id_ed.json`.

Lección de esta tanda: **una prohibición en mayúsculas dentro de la ropa de un
personaje se dibuja como texto** («NO badge, NO patch» → parches que dicen
NO). La ropa se describe en positivo: «de tela completamente lisa, sin nada
cosido, prendido ni impreso».

## Cartones

`cartones/cartones_ed.py`, verbatim, densidad 49–62 %. Los insultos (C2, C3)
los dice la voz y no se escriben; el hecho de violencia sexual del C4 tampoco.

## Pase previo a la revisión de Sebastián (3 nov, noche) — v2 de las cinco líneas

El mismo pase que en Ley 1826 (ver `cursos/ley_1826/README.md`: lo que él
ajusta a mano en las líneas que aprueba y lo que pide después de revisar), con
la reserva de créditos en 1.500. Líneas nuevas `… v2`, la v1 en
`_ARCHIVO versiones anteriores` (bin y disco), revisión interna en
`D:\DAE\_tmp\ed\revision\ED_<K>_v2_REVISION_INTERNA.mp4`.

- **Respiro con fundido a negro** horneado (`ed_pieza.respiro`, 16 cuadros).
- **El último cartón termina con el cuerpo**; el respiro queda limpio
  (`cartones_ed.calcula`). Un cartón que pise una ranura con rótulo se corta
  donde ella empieza (no pasaba en ninguno).
- **Huecos de más de 400 cuadros sin cartón**, medidos: C2 914–1567, C3
  1022–1519 y 2233–2807, C4 777–1289, C5 521–1107 (la primera mitad del C3
  iba al 35 %). Entran: C2 «Una mañana de finales de agosto,» y «Su cuerpo fue
  hallado al día siguiente, coincidiendo con la fecha de su cumpleaños»; C3
  «Los dos hombres se negaron y, ante la insistencia de Wilmer, se resistieron
  físicamente» y «Los dos agresores fueron capturados por agresión a servidor
  público,»; C4 «Jacanamijoy, aprovechando su posición de autoridad y la
  confianza que esta le confería ante la familia y la comunidad,»; C5 «En la
  recepción, el funcionario le solicitó su documento de identidad.» y «le
  preguntó en voz alta, frente a otras personas que esperaban de turno». Los
  golpes, el abuso y los insultos siguen sin escribirse.
- **Las cuatro caminatas hacia cámara** (C1 r01, C3 r04, C5 r01, C5 r18): el
  clip conformado terminaba con la cabeza cortada por arriba (Kling acerca al
  personaje y el recorte al 88 % lo adelanta). Ahora el encuadre se abre del
  0,88 al 1,00 a lo largo del clip (`mov_ed.ABRE`, smoothstep: un retroceso
  de cámara suave) y la ventana útil es más larga (48 / 96 / 84 / 78 cuadros
  desde `_enteros`; en C5 r18 Kling vuelve transparente a Valentina desde el
  82): la cabeza queda en cuadro y el estirado baja (C3 r04 de 3,0× a 2,6×;
  C5 r01 de 3,2× a 2,7×; C5 r18 1,8×; C1 r01 2,5×).
- **Kling ×4 (560 cr), boca en planos de habla:** C1 r11 la defensora
  argumenta; C3 r19 Wilmer ante el reportero; C4 r13 el fiscal entre los dos
  colegas; C5 r05 Valentina responde. 16 clips en 118 ranuras.
- Créditos: 2.071 → 1.511.

## Revisión de Sebastián · C3 El patrullero Wilmer (4 nov) — en SU línea v2, sin remontar

Pedido: «ningún personaje de la Policía Nacional se ve como un patrullero
colombiano por el uniforme, sobre todo en los planos del incidente en el
aeropuerto (búscalos de referencia); hay clips con negros demasiado duros,
todo debería ser más grisáceo; la r09 no da la idea de la policía sacando a
la gente del aeropuerto; la r11 debería ser un cenital de la misma escena; en
el 1:39 agrega un inserto con una variación de ángulo». Presupuesto apretado:
solo stills y la cámara de la casa.

- **El uniforme.** Referencia: el uniforme de servicio urbano de la Policía
  Nacional (verde oliva) con el chaleco reflectivo verde-amarillo de dos
  franjas grises y la gorra verde. El uniforme azul se presentó en 2021 como
  piloto en diez ciudades (El Heraldo, policia.gov.co, RTVC); las fuentes
  consultadas no confirman que haya reemplazado al verde, y la imagen que se
  reconoce del patrullero es la del verde con el chaleco: esa se usó. `base_ed.UNIFORME_POLICIA` (párrafo entero que
  `arma` agrega cuando hay un patrullero) y `UNIFORME_CORTO` dentro del token
  de Wilmer y de su compañero. Sin letras («POLICÍA» de la espalda),
  insignia, escudo, bandera, placa ni arma, como siempre. Hoja nueva de
  Wilmer (la vieja como referencia de cara; la anterior en
  `00 PERSONAJES/_descartes`).
- **Re-vestidas sobre la misma placa** (REF 'mismo': mismo plano, misma gente,
  misma luz, solo cambia la ropa; una tirada cada una, candidata `p`): r01,
  r02, r04, r05, r06, r10, r12, r13, r24, r25. **Nuevas:** r09 (los dos
  patrulleros escoltan a los dos pasajeros hacia la puerta de salida, luz de
  techo, los pasajeros con la cabeza baja y la cara fuera), r11 (picado
  cenital de la misma escena). Detalles: el brazo de la r11 re-vestido (la
  primera tirada agarraba a otro policía: descartada, segunda tirada con la
  r09 de referencia) y el **contraplano** nuevo en la r12 (desde detrás del
  banco, Wilmer de frente escribiendo el informe), V3 2339-2435 — el 1:39 es el
  cuadro 2374. Los tres, quietos con la cámara de la casa.
- **El color del uniforme.** La limpieza de la serie apagaba el verde
  (x0,08) y el amarillo suelto (x0,15): el uniforme habría salido gris. En
  `escenas.CHALECO` la limpieza deja el verde-amarillo del chaleco a
  s ≤ 0,55 y el verde oliva a s ≤ 0,30 (`ed_pieza.topes_chaleco`; también en
  `detalle_ed` y `hojas_ref_ed`). El chaleco no es acento: no se gira a la
  mostaza. En la revisión interna el chaleco de r02 y r10 salió blanco-gris:
  graduadas sin techo, el grade les dejó un frío de 0,37-0,39 y la relimpieza
  se llevó el chaleco. Ahora `construir` le devuelve tono y saturación de la
  limpia (`reinyectar_acento` en la banda 34-62) y lo vuelve a acotar.
- **Los negros.** Medido sobre su línea: las placas de noche de la terminal
  tenían p50 18-31 y 53-70 % del cuadro bajo 30 (r02, r08-r11; el detalle del
  brazo 75 %). Dos cosas: SIN_TECHO para las de noche (el registro les sube el
  medio tono) y a TODO el C3 una curva suave que levanta la sombra
  (`ed_pieza.gris`, `GRIS = (30, 130)`: 0 → 30, 20 → 42, 45 → 58, 90 → 93,
  blancos intactos). Las 25 ranuras y el respiro rehorneados; el Kling de la
  r19 y el detalle de la r22, que se quedan, llevan la misma curva en ffmpeg
  (`gris_vf`, mismo archivo, `ReplaceClip`).
- **Fuera de su línea** los Kling de r04, r09 y r24 (mostraban la chaqueta
  vieja; `MOVIMIENTO/_descartes`): esas ranuras quedan con la placa nueva y la
  cámara de la casa. Todo con `cirugia_ed C3 v=2 relink / quitar / poner`;
  nada más cambió en la línea. `.drt` reexportado.
- Créditos: 1.336 → **776** (16 stills × 35: la hoja, 12 placas, 2 detalles
  y la tirada descartada del brazo).

## Revisión de Sebastián · C4 La niña del resguardo de Putumayo (4 nov) — marcadores en SU línea v2, sin remontar

Nueve marcadores en la línea general (no en los clips), cada uno con su
instrucción. Presupuesto apretado: solo stills y la cámara de la casa.

| marcador | ranura | pedido | lo que se hizo |
|---|---|---|---|
| 415 (0:17) | r01 | presentar a la niña: hoja de personaje, meterla en el lugar, rótulo | hoja `nina` (Yaneth: niña indígena de unos diez años, trenza, camiseta gris clara, falda gris, botas de caucho, el morral gris); r01 'mismo' con ella caminando hacia cámara por el camino, la casa atrás; rótulo «Yaneth Payaguaje · Niña de la comunidad» en V8 409-529 (la voz dice su nombre en 396-422) |
| 590 (0:24) | r02 | «Taita se pronuncia con tilde en la primera a» | en d02 ElevenLabs dijo «taíta» (STT: «tahita»); toma nueva con «Táita» y SOLO la palabra injertada en el máster (`voz/taita_c4.py`): bordes por energía, RMS igualado (−19,3 → −19,4 dB), fundidos de 12 ms en el silencio, mismas 7.551.604 muestras. STT del tramo nuevo: «Taita». d06 y d16 ya decían «Taita». Resolve tiene abierto el WAV y Windows no deja reescribirlo: va como `ED_C4_NARRADOR_v2.wav` y entra con `cirugia_ed cambiar` (ReplaceClip) |
| 849 (0:35) | r03 | otro ángulo, que no se parezca a la anterior | picado general del resguardo desde la ladera (el camino, las casas, la casa del cabildo, el río), de día; antes era el interior oscuro de la casa mirando a la puerta |
| 1121 (0:46) | r04 | muy oscura, negros demasiado negros | `GRIS = (30, 130)` en todo el C4 y SIN_TECHO en r04 y r19 (medido en su línea: p2/p50 13/16 y 15/17) |
| 3198 (2:13) | r15 detalle | dos planos seguidos de manos levantadas se ve raro: el mismo plano con la gente solo presente | inserto nuevo `la_mesa` (REF 'mismo' del anterior: misma mesa, nadie levanta la mano), quieto, V3 3145-3235 |
| 3466 (2:24) | r17 | la niña | 'mismo': de la mano de su madre en la orilla; fuera el Kling de la madre sola (`MOVIMIENTO/_descartes`) |
| 3550 (2:28) | r18 | la niña | 'mismo': sentada al lado de su madre en el escalón, el morral en sus piernas |
| 3836 (2:39) | r19 | muy oscura + la niña | 'mismo': las dos de espaldas, de la mano, mirando la casa; el Taita lejos en su porche. Grade sin techo + curva gris |
| 3979 (2:45) | r19 | inserto de apoyo: contrapicado, figura en sombra del Taita | detalle `el_contrapicado` V3 3979-4073 (hasta el corte al respiro), quieto. Primera tirada recortada al 70 %: al borde derecho había una mujer de mostaza junto a otra casa |

- **La niña se dibuja desde hoy** (antes la regla del curso era no dibujarla):
  pedido explícito de Sebastián, personaje ficticio. Va como una niña común en
  un momento cotidiano, vestida de escuela, con dignidad (`base_ed.C_NINA`,
  y la regla de 8 cabezas dice que ella es una niña de unas seis). Nunca en la
  casa del Taita ni cerca de él; el abuso sigue sin imagen.
- **El cartón p01** («En un resguardo indígena cercano a Puerto Guzmán,
  Putumayo,») se corta donde entra el rótulo: 236 → 106 cuadros. Va con
  otro nombre (`cartones_ed.RENOMBRA`): el pool cachea la duración. La
  ventana que un cartón no puede pisar es ahora la del rótulo en pantalla
  (entra .. entra + cuadros), no la ranura entera. Los otros trece cartones,
  comprobados idénticos a su línea.
- **El respiro se queda** (la r01 vacía, `RESPIRO_FIJO`): la r01 cambió y el
  respiro de su línea es el camino sin nadie.
- **Kling** de r10 y r13, que se quedan: la misma curva gris en ffmpeg.
- **La curva gris, medida** (p2/p50 antes → después): días 22-23/83-86 →
  43/87-89; contraluz r02 y r09 19-20/60 → 41/69; r04 16/36 → 39/52 y r19
  15/32 → 38/49 (sin techo); nada bajo 30 en ninguna de las 19.
- Cirugía (`cad_c4_rev.py`): 21 relink (19 ranuras + 2 Kling), 3 quitar
  (Kling r17, inserto de las manos, p01), 4 poner (la mesa, el contrapicado,
  p01 cortado, rótulo) y 1 cambiar (la voz). `cirugia_ed retrato`: la línea
  y el plan coinciden, nada más cambió; largo 4422. `.drt` reexportado (el
  anterior a `_descartes`).
- Revisión interna (`D:\DAE\_tmp\ed\revision\ED_C4_v2_REVISION_INTERNA.mp4`):
  4422/4422 cuadros, −19,3 LUFS, pico −4,0; único negro el último cuadro del
  respiro (171,84 s).
- Créditos: 776 → **426** (10 stills × 35: la hoja en dos tiradas, cinco
  placas, dos detalles y la segunda tirada del contrapicado, que no se usó).

## Entregas

Con su OK, caso por caso. `ed_pieza <L> v=2 exportar entregas verificar` sobre
SU línea v2 tal como la dejó (máster H.264 NVIDIA 32 Mbps en
`D:\DAE\_tmp\ed\render`, MP4 receta Fiscalía x264 crf 18 + copia 720p en
`05 EXPORTS`); el `.drt` de `10 TIMELINE SEBASTIAN` se reexporta después del
export (el anterior a `_descartes`). Camino al Drive: copia con el nombre de
entrega (`guion_ed.ENTREGA`) a `G:\My Drive\_ED subidas` (md5 igual), Drive la
sincroniza, `update_file(parentId=VIDEOS)`.

| | archivo en `05 EXPORTS` | cuadros | LUFS · pico | MB | Drive `VIDEOS` |
|---|---|---|---|---|---|
| C1 Édgar Molano (4 nov, «you are good to export and upload») | `ED_C1_v1.mp4` | 4964/4964 | −19,2 · −4,1 | 55 | `PRIO 2 - ENFOQUE DIFERENCIAL - CASO 1 EDGAR MOLANO.mp4` · `1E5jbysh98ZfEXY_n0Nuh3-4XGbd86-a6` |
| C2 Jairo Montero Salas (4 nov, «export and upload ed c2») | `ED_C2_v1.mp4` | 6046/6046 | −19,1 · −4,1 | 83 | `PRIO 2 - ENFOQUE DIFERENCIAL - CASO 2 JAIRO MONTERO SALAS.mp4` · `1BZUppd4nYSmb_06Ps86qqYYFDxJXD1-h` |
| C3 El patrullero Wilmer (4 nov, tras su revisión: «export and upload that one too») | `ED_C3_v1.mp4` | 5347/5347 | −19,2 · −3,5 | 54 | `PRIO 2 - ENFOQUE DIFERENCIAL - CASO 3 EL PATRULLERO WILMER.mp4` · `13nUHnPO0K35pLLYFIoGPl59IUxAdVcBo` |

El único «negro» de cada uno es el último cuadro del respiro (C1 194,44 s;
C2 239,57 s; C3 210,42 s), el fundido horneado. C4: revisión aplicada el 4 nov, espera su OK para exportar. C5 espera su revisión.

## Estado

Ver el documento del proyecto `claude/ED_Enfoque_Diferencial_03_noviembre.md`.
