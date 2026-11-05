# Estándares interamericanos · graves violaciones a los derechos humanos · PRIORIDAD 3

Carpeta del Drive: `1c7fmrN1YeM2uYtn1-6ThuNgRX5fOZLBa` («PRIORIDAD 3 -
Estandares Interamericanos Graves violaciones VF»), un solo documento:
«Estándares Interamericanos - Actividades de aprendizaje»
(`1er8p3nu7Ut2d97i0XsJV92v8mR516YiHlVV9o5yJOnE`). Entregas en `VIDEOS`
(`1j6v4nenqFDAL2RNu3x15nZzWxObP7q7Y`) e `IMAGENES`
(`1UEghYotTn4q86O8TotyDspDDBLolXsZC`), **solo con el OK de Sebastián**.

Árbol: `E:\DAE MASTER\PRIORIDAD 03\CURSO - ESTANDARES INTERAMERICANOS\`
(00 DOCUMENTOS FUENTE, 00 PERSONAJES, VIDEOS\SITUACION 0n - … con las diez
carpetas de la serie, IMAGENES\SITUACION 0n - … con las cuatro de las láminas,
IMAGENES\IMAGENES ENTREGA). Bins iguales en `DAE MASTER - CURSOS` dentro de
«PRIORIDAD 03». Rutas en `herramientas/voz/textos/rutas_ei.py`; metadatos y
textos en `guion_ei.py`.

PRIORIDAD 0X / X: medido el 5 nov, en disco y en el pool solo existe
«PRIORIDAD 03» (los casos P3 y Desaparición forzada). El curso entra ahí: crear
«PRIORIDAD 3» abriría el par y obligaría a mover y reenlazar toda la serie P3.

## Lo que pidió Sebastián (5 nov)

- Las situaciones con comentario «Video» o «Imagen» se hacen así. Las que no
  tenían comentario, «dependiendo de la longitud del caso: si vale la pena para
  video, video; si no, ilustración».
- Sin preguntas ni respuestas (van en otra parte de la virtualización). La
  consigna tampoco, como en «16 situaciones».
- Todo en Colombia, en el estilo de la serie, cinematográfico; más clips con
  movimiento: techo de ~800 créditos de Magnific por video.
- Magnific con la **cuenta nueva** (jpcolombia3, Pro, 300.000 créditos): se
  conecta cerrando sesión del conector de Magnific en Claude e iniciándola con
  la cuenta nueva; no hace falta API. Las creaciones de la cuenta vieja no se
  ven desde la nueva: las anclas de estilo (placas aprobadas de Ley 1826 y
  Enfoque diferencial) y una hoja de ED se subieron de disco
  (`prompts/placa_id_ei.json`, `EI_ANCLA_*`, `EI_ESTILO_HOJA_*`).

## Separación (palabras de la situación, sin consigna)

| clave | actividad | tipo | por qué |
|---|---|---|---|
| S01 | AA1 ¿Quién responde por una violación de derechos humanos? | video | comentario (121 palabras) |
| S02 | AA2 ¿Cómo se organiza la protección internacional…? | lámina | comentario (38) |
| S03 | AA3 ¿Qué fuente internacional necesito consultar? | lámina | comentario (30) |
| S04 | AA4 ¿Cómo utilizaría una fuente internacional…? | video | comentario (86) |
| S05 | AA4 ¿Cómo utilizaría la jurisprudencia interamericana…? | lámina | comentario (51) |
| S06 | Actividad inicial · la muerte de dos jóvenes | video | sin comentario, 108 palabras |
| S07 | Actividad · la fosa clandestina | video | sin comentario, 87 |
| S08 | Actividad · bajo custodia policial | video | sin comentario, 78 |
| S09 | AA1 ¿Es suficiente abrir una investigación penal? | lámina | sin comentario, 63 |
| S10 | AA2 ¿Qué examina la Corte Interamericana…? (La Rochela) | lámina | comentario (61 + lectura) |
| S11 | AA3 ¿Qué decide y qué ordena la Corte Interamericana? | lámina | comentario (72) |

Las tres actividades sin número aparecen dos veces en el documento (copia):
cuentan una vez.

## Cinco videos

| | narra | ranuras | cuadros de narración | acento |
|---|---|---|---|---|
| S01 El líder comunitario | Carlos | 12 | 1235 | la ruana del líder |
| S04 Las fuentes | Pilar | 10 | 1021 | la bufanda en la bolsa de evidencia |
| S06 La muerte de dos jóvenes | Carlos | 9 | 1088 | la chaqueta en la percha |
| S07 La fosa clandestina | Pilar | 9 | 973 | el saco hallado |
| S08 Bajo custodia policial | Carlos | 7 | 880 | el buzo devuelto |

Las ranuras parten los bloques de la rejilla en la palabra donde cambia la
idea (tiempos de Scribe): 2 planos por bloque donde el bloque pasa de ~6 s.
Sin rótulos: nadie tiene nombre en el documento. Cartones: un trozo verbatim
por bloque (`cartones/cartones_ei.py`), 69-74 % del cuerpo. Dos arreglos de
lectura: en el S04 las dos convenciones van en un solo cartón que cruza la
frontera de bloque (sola, «la Convención Americana…» quedaba en 54 cuadros) y
el S06 p04 («Un testigo afirma…») entra 36 cuadros tarde (`DESPLAZA`) para que
el p03 baje de 20,8 a 14,5 car/s.

### Movimiento (Kling 2.5, 720p, 5 s, 140 cr)

Cinco clips por video sobre la placa graduada (`prompts/kling_ei.json`,
ledger de ids en el doc del proyecto):

| | clips | descartes | créditos |
|---|---|---|---|
| S01 | r01 r05 r08 r10 r11 | r08 (la familia caminaba y Kling siguió con la cámara) | 840 |
| S04 | r01 r06 r08 r09 r10 | — | 700 |
| S06 | r01 r04 r06 r07 r09 | r04 (la placa traía dos sombreros) | 840 |
| S07 | r02 r04 r06 r08 r09 | — | 700 |
| S08 | r01 r02 r03 r05 r07 | — | 700 |

Ventanas (`hasta`, en `bajar_mov_ei`): una ranura más corta que el crudo se
recorta a su largo para ir a velocidad nativa (acelerar un Kling se nota), y
se cortan las colas malas: S01 r05 3,3 s (los investigadores vuelven al
inicio), S04 r08 2,5 s (la cabeza toca el borde; `ABRE`), S07 r04 2,5 s (el
que lleva la maleta se esconde detrás de la antropóloga y desaparece), S07 r09
3,7 s (al final mira a cámara).

Subida de cuadros iniciales: JPEG 2048 hecho en la máquina, `stage` a la nube
y PUT con curl desde ahí (desde Windows uno de cinco dio SSL EOF).

### Placas rehechas en la revisión (35 cr cada tirada, referencia «mismo»)

- S01 r08-r12: la oficina de la organización traía una bandera con escudo en
  el rincón (r08 la propagó como referencia de lugar a r09-r12). Pared lisa.
- S06 r07: la caja de luz con radiografías mostraba costillas. Pared lisa.
- S06 r09: «last light over the hills» dio un cielo rosado. Gris neutro.
- S06 r04: el padre tenía sombrero puesto y otro en las manos. Cabeza
  descubierta, un sombrero.
- S07 r05: «earth on its folds» dejó manchas que se leían como agujeros en el
  saco. Saco entero, polvo claro en un pliegue.

## Seis láminas

Ilustración tipo afiche (`prompts/imagenes_ei.py`, dos ideas por lámina) y
panel azul con el texto verbatim de la situación en párrafos
(`cartones/lamina_ei.py`): rótulo = el subtítulo del documento («SITUACIÓN DE
APRENDIZAJE», «SITUACIÓN INICIAL», «SITUACIÓN»). S10 lleva la lectura de La
Rochela (párrafos 178 y 179) como cita sangrada en cuerpo menor; S11 las
tres determinaciones con la etiqueta en negrita. S03 pasó el panel a la
izquierda (a la derecha tapaba a la servidora en la escalera); la marca lleva
sombra solo cuando el fondo bajo ella es claro (S03, S09).

## Lo que no se dibuja

Ninguna desaparición, detención, agresión, masacre ni muerte; ningún arma,
cuerpo, resto ni hueso (la fosa es carpa, cuerda y lona). Ningún hecho
debatido: ni el enfrentamiento del informe militar ni la subida al vehículo
(S06), ni lo que muestra el video (S08: una mancha gris). Los militares no se
dibujan (camiones lejos, una manga verde oliva lisa); los patrulleros de S08
van de espaldas con el uniforme de la Policía Nacional; la fuente de S07 sin
cara.

## Revisión de Sebastián y entrega (5 nov, noche)

Retocó las líneas (lo único medible por API: en S04 acortó el cartón p01 de
115 a 88 cuadros; nada más cambió de sitio ni de archivo) y dejó un marcador:

- **S04, cuadro 813** (r06 la convención): «the pamphlet or booklet looks off,
  doesn't make sense how it opens». La placa tenía el libro de canto contra la
  cámara con las hojas saliendo por arriba, y el Kling lo hojeaba así. Placa
  nueva por encima del hombro, el libro abierto de frente en las dos manos
  (candidata f; la opción del libro sobre el escritorio se descartó porque la
  r05 ya es eso y quedaban dos planos iguales seguidos). Kling nuevo: pasa una
  página y sigue leyendo. Ranura y movimiento reescritos en su sitio y
  releídos en SU línea con `cirugia_ei S04 relink` (sin remontar).
  105 cr de placas + 140 de Kling.

Exportados con la receta Fiscalía (`ei_pieza <S> exportar entregas
verificar`): `05 EXPORTS\EI_<S>_v1.mp4` + copia 720p.

Drive, con las subcarpetas de disco: `VIDEOS\SITUACION 0n - …\` y
`IMAGENES\SITUACION 0n - …\`, cada archivo con su nombre de entrega
(`PRIO 3 - ESTANDARES INTERAMERICANOS - SITUACION 0n …`). Ids de las carpetas
en el doc del proyecto.

| entrega | cuadros | MB | LUFS · pico | negros |
|---|---|---|---|---|
| S01 | 1885 | 26 | −20,0 · −4,2 | el último del respiro |
| S04 | 1671 | 22 | −20,1 · −4,5 | el del respiro + su fundido desde negro en 472 (r02→r03) |
| S06 | 1738 | 24 | −20,2 · −4,3 | el último del respiro |
| S07 | 1623 | 24 | −20,2 · −4,7 | el último del respiro |
| S08 | 1530 | 20 | −20,4 · −4,1 | el último del respiro |

Las 6 láminas, las PNG de `IMAGENES ENTREGA` (S03 y S09 en su versión
corregida). Todo comprobado por tamaño contra el disco.
