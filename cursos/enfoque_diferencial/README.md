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

El único «negro» de cada uno es el último cuadro del respiro (C1 194,44 s;
C2 239,57 s), el fundido horneado. C3–C5 esperan su revisión.

## Estado

Ver el documento del proyecto `claude/ED_Enfoque_Diferencial_03_noviembre.md`.
