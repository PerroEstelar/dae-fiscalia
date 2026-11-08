# Delitos contra el medio ambiente · piezas de Sebastián · PRIORIDAD 3

Curso: «Investigación y judicialización de delitos contra el medio ambiente y
los recursos naturales». Documento maestro (PDF del curso, con las notas de
virtualización repartidas por resaltado): Drive `1HOT5p71fNf2kfg93Q-NnQZMMdYRHv0Xa`.
Carpeta del curso en Drive: `1l9Kyx9IbpAwYmXBGI_tLDMI1wRKzVsnn`; entregas en
`VIDEOS` (`1ti3YDj4-u4i7lGVzo65js9TlhZWKHdTh`), **solo con el OK de Sebastián**.

Árbol: el curso ya existía en disco con las introducciones de unidad (el
profesor en cuadro). Las piezas nuevas entran en su unidad:
`E:\DAE MASTER\CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\UNIDAD n\VIDEO 0n - …`
con las diez carpetas de la serie (09 MOTION GRAPHICS en vez de 09 A LA VOZ).
Rutas en `herramientas/voz/textos/rutas_da.py`; metadatos, bloques de voz y
fuentes de las cifras en `guion_da.py`.

## Lo que es nuestro (7 nov)

Los resaltados «Video sebastián / Sebas / Sebastian» del PDF son seis:

| clave | unidad | pieza | guion |
|---|---|---|---|
| V01 | U1 L1 | Video introductorio: problemática ambiental y criminalidad | nuestro |
| V02 | U3 L1 | Video explicativo: Plan de priorización de la FGN (Direccionamiento Estratégico 2024-2028) | nuestro |
| V03 | U3 L3 | Video interactivo: técnicas especiales de investigación | nuestro |
| V04 | U4 L1 | El río y la fábrica: midiendo el daño para reparar | del caso escrito |
| V05 | U4 L2 | Operación «Raíces Profundas» | del caso escrito |
| V06 | U4 L5 | El caso Francisco | del libreto |

Lo de Esteban (interactivos, mapas, infografías) y «Esto lo hago yo» no es
nuestro. Sebastián pidió ver el V01 terminado antes de seguir con los demás.

## La dirección de arte del curso

`prompts/base_da.py`. El tema es el territorio, así que el entorno NO va en
grises puros como en el resto de la serie: bosque verde gris apagado, agua
limpia gris verdosa oscura, agua minada ocre-gris, cielo gris neutro. El único
saturado es la **mostaza mate de la maquinaria y del oro** (la retro, el motor
de la draga, el oro en la batea y en la balanza). Gente a media acción, piel
gris cálida, nadie armado a la vista, nada violento, ningún texto ni bandera.
Desde el aire, el bosque se dibuja en masas simplificadas (`C_AEREO`): sin
eso Seedream entrega fotos de dron.

Tres cosas del pipeline que cambian contra EI (`montaje/da_pieza.py`):

- `limpia` ACOTA el verde (s ≤ 0,20) y el ocre (s ≤ 0,26 sin acento) en vez
  de apagarlos; el frío de verdad sigue ×0,08.
- `graduar_da`: la curva de la serie sacada de la luma y aplicada igual a los
  tres canales, sin `neutralizar_entorno` (que llevaba el bosque a gris).
- Registros nuevos: `aire` (se gradúa como día) y `contra_ext` (contraluz de
  exterior: el `contraluz` de la serie habla de puertas y pasillos).

## V01 · Problemática ambiental y criminalidad

Narra Carlos. 13 bloques, 166,5 s de voz, 34 ranuras cortadas por la voz
(Scribe palabra por palabra), pieza de 4642 cuadros. Progresión: la selva
intacta → el río (draga, mercurio, pescador) → la tierra (retro, pozos) → el
bosque (tala, quema, potrero) → los seis motores → el dinero → los grupos
armados → el lavado → la intervención y su límite → la fiscal → subir por la
cadena → el río limpio.

Cifras (literales en el gráfico, en letras en la voz):

- Gobierno nacional y UNODC, EVOA 2025: 118.410 ha con evidencias de
  explotación de oro de aluvión; 75 % ilícita; 85,6 % de los municipios con
  EVOA con presencia de al menos un grupo armado.
- IDEAM, deforestación 2025: 119.483 ha; ~65 % en la Amazonía.

**V5 MOTION GRAPHICS** (`graficas/mg_da.py`, qtrle con alfa, cada elemento
entra con su palabra en Scribe): aluvión (r07), IDEAM con el mapa de los
departamentos amazónicos (r12, es un esquema de la región), los seis motores
(r13-r18, uno por placa), municipios (r23) y la cadena (r33). Los cartones
(`cartones/cartones_da.py`, 11, verbatim) no pisan un gráfico.

**V2 MOVIMIENTO**: Kling 2.5 720p 5 s desde la placa graduada en 27 ranuras
(`escenas_da_v01.KLING`); sin clip las ranuras bajo gráficos y las que valen
por quietas (pozos, la máquina sola).

Placas: 34, Seedream 5 Flash 2k; ids en `prompts/placa_id_da.json`, elegidas
en `prompts/elegidas_da.json`. Rehechas: r01 (salía foto de dron), r21 (los
hombres miraban a cámara), r24 (multitud no pedida), r28 (banderines en la
lancha).

**Estado:** aprobado por Sebastián y entregado (`05 EXPORTS\DA_V01_v1.mp4`,
Drive `1Xmf3jdG_bM6knGa6rbITPOAE34IO9G4p`).

## V02–V06 (7 nov)

| | narra | ranuras | gráficos (V5) | cartones | Kling |
|---|---|---|---|---|---|
| V02 Plan de priorización | Pilar | 26 · 4627 c | pilares, niveles, enfoques, programa, art. 6, consecuencias | 11 | 16 + 3 prestados del V01 |
| V03 Técnicas especiales | Carlos | 24 · 4455 c | control del juez + nueve rótulos-enlace (arts. 233, 235, 236, 239–244) | 10 | 19 |
| V04 El río y la fábrica | Pilar | 18 · 3549 c | lesión, −30 % de oxígeno, plan de reparación, medir | 9 | 12 |
| V05 Raíces Profundas | Carlos | 23 · 4002 c | las cuatro preguntas y las dos firmas | 11 | 18 |
| V06 El caso Francisco | Pilar | 26 · 4889 c | los ocho pasos del libreto (rompecabezas, preguntas, balanza) | 12 | 16 |

Kling: `escenas_da_v0N.KLING`; los cuadros iniciales son las placas graduadas
en JPEG 2048 (`prompts/kling_jpg_da.py`) subidas desde la nube. Sin clip las
ranuras bajo el panel de un gráfico; en V03 los rótulos no llevan panel, así
que sí llevan clip las ranuras donde lo marcado no se mueve (la pantalla, el
paquete, el portátil, la orden), y no las que marcan algo que el clip
movería (el empresario que camina, el lanchero, la lancha).

Lo medido en la tanda (de 66 clips):

- **El papel no se anima.** V02 r02 y r15 hojeaban la carpeta: el crudo entra
  desde que la carpeta ya está abierta (`desde` en `bajar_mov_da`). El clip
  cubre la ranura entera en corte seco, así que no tiene que arrancar en la placa.
- **Kling suma humo donde hay paisaje quieto**: la mina abandonada del V04 r05
  (queda placa con cámara), la bodega del V03 r10 (poco, se deja), la lona del
  V03 r01 que se volvía humo (entra desde 3,2 s).
- **Un brazo que señala a lo lejos suelta algo del dedo** (V04 r08: una nube
  blanca). Rehecho con «gira la cabeza y dice unas palabras».
- **«Camina hasta el borde del muelle» la metió al río** (V02 r25). Rehecho con
  «cada uno se queda donde está» y la caja que pasa de mano en mano.
- Mirar a cámara al final del gesto (V03 r11, V04 r07, r09): se corta antes.

**Estado (7 nov, 16:00):** las cinco líneas montadas en `DAE MASTER - CURSOS`
con su `.drt` en `10 TIMELINE SEBASTIAN`, revisión interna pasada (cuadros =
pieza, el único negro es el fundido del respiro, −19,1 a −19,4 LUFS). Sin
exportar: esperan que Sebastián las vea.

- **El respiro ya no es siempre la r01** (`escenas.RESPIRO`): V04 cierra en el
  río limpio (r18), V05 en las firmas (r23), V06 en el Amazonas (r26). La r01
  del V06 es la tala con motosierra y quedaba como última imagen después de
  «protección del Amazonas».
- **Un medio reemplazado en su sitio no llega al render**: Resolve siguió
  sirviendo el respiro viejo con el archivo nuevo en disco. Se copia con nombre
  nuevo (`DA_V06_respiro_r26_v48.mp4`, `DA_V02_r24_..._mov_v77b.mp4`) y se
  hace `ReplaceClip` sobre el ítem del pool; el render siguiente ya lo trae.

**V02 entregado (7 nov, 16:35).** Sebastián marcó el r05: el mapa de Colombia
de la pizarra no era el país. La placa se pidió con la pizarra en blanco (la
r05 como referencia) y el mapa se dibujó encima con los departamentos de
Natural Earth (`graficas/mapa_pizarra_da.py`, candidata `m`), multiplicado
sobre la franja de sol de la placa. Export `05 EXPORTS\DA_V02_v1.mp4` (4627 c,
−19,3 LUFS, md5 `dde992bd…`), en Drive en `VIDEO 02 - Plan de priorizacion de
la FGN`. Mientras exportaba, D: quedó en 0 GB: el render salió sin `moov`.
Se movieron a `E:\DAE MASTER\_tmp_movido_de_D\da` las revisiones internas y
los másters de este curso (8,9 GB libres después).

**V03 entregado (7 nov, 19:55).** Exportado como lo dejó Sebastián: la cama
pasó a una pista nueva (A6) corrida 349 cuadros, así que la línea mide 4804;
se entrega la pieza hasta el último cuadro del outro (4455). Medido: bajo la
voz la música sigue en −32,9 dB de mediana (con la cama en su sitio era igual),
y suena a −28 dB bajo el outro hasta el corte. Un fundido desde negro suyo en
el cuadro 741 (entrada del control del juez). `05 EXPORTS\DA_V03_v1.mp4`
(−19,0 LUFS, md5 `670860df…`), en Drive en `VIDEO 03 - Tecnicas especiales de
investigacion`.

**V04 entregado (7 nov, noche)** tal como lo dejó Sebastián (partió el gráfico
del oxígeno en tres en la V5). `05 EXPORTS\DA_V04_v1.mp4` (3549 c, −19,3 LUFS,
md5 `f94dde50…`), en Drive en `VIDEO 04 - El rio y la fabrica`.
