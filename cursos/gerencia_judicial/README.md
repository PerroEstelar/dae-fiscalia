# Gerencia judicial · PRIORIDAD 2

Documento del Drive: «Gerencia judicial - Casos varios»
(https://docs.google.com/document/d/1kZrQeecvuwx4Jj9h_7PDxAZFMtCGakATgyvjp_W-7QE/edit),
en la carpeta «PRIORIDAD 2 - GERENCIA JUDICIAL» del Drive. Las entregas van a
su subcarpeta «Videos» (https://drive.google.com/drive/folders/1hUGpHHn9iHFbTFtslGhYya6H5MF6vKGo),
**solo con el OK de Sebastián**. El texto completo, con los cuatro comentarios
de la agencia marcados, está en `fuentes/Gerencia_judicial_Casos_varios.md`.

## Lo que trae el documento y lo que va a video

Tres temas —Primer, Tercer y Cuarto; el Segundo no viene— y cada uno abre con
un **caso introductorio**. Lo demás (pregunta que guía el tema, conceptos
clave, el caso real de Triple A, las decisiones i–vi) va a Moodle.

| | lo marcado por JP | palabras | voz | pieza |
|---|---|---|---|---|
| T1 «El despacho de los 2.000 casos» | «Solo esto en video»: el párrafo del caso | 59 | Pilar | 1176 cuadros · 0:49,0 |
| T3 «Aceptar o negociar» | «Video»: los cuatro párrafos de la hipótesis | 206 | Carlos | 2872 · 1:59,8 |
| T4 «Dos situaciones al comenzar la semana» | «Video» sobre toda la hipótesis (+ uno anidado sobre las dos situaciones) | 401 | Pilar; las dos citas, Carlos | 4877 · 3:23,4 |

**Tres videos, no cuatro** (Sebastián, 29 oct: «hagamos tres videos
entonces»). El comentario anidado del T4 se puso 14 s ANTES que el grande:
primero marcaron las dos situaciones y después ampliaron la marca para que
entrara el encuadre de la coordinación. Si alguna vez se quiere partir, el
corte natural está en «La primera ocurre dentro del equipo».

Los títulos de carpeta son de trabajo. En pantalla, el cartón de entrada dice
«Gerencia judicial · Primer tema» y el título del tema **tal como lo escribe
el documento** (en el Cuarto, hasta los dos puntos).

## Voces

ElevenLabs, cuenta de Sebastián, `eleven_multilingual_v2`, los ajustes de
`elevenlabs.py`. 23 tomas, todas oídas por Scribe (`stt_gj.py`) contra el
texto pedido: ninguna palabra de más ni de menos, ningún tartamudeo (las
únicas diferencias son cifras que Scribe escribe en dígitos). Máster a
−19 LUFS, techo −2 dBFS; los bloques se nivelan por la **mediana del
short-term con voz** (no por integrado) porque en el T4 hablan dos voces:
peor salto entre bloques 0,0 / 0,8 / 0,2 LU.

**Rejilla recortada por palabra** (`rejilla/recortar_gj.py`): la automática
cortaba «en el estricto | orden en que llegan», «previsto en el artículo |
349» y «el nuevo aplicativo | utilizado». Se recortó en el silencio entre
palabras, con los tiempos de Scribe. La automática quedó en `_descartes`.

## Sistema visual

El de la serie (biblia P3 / Desaparición Forzada), sin una coma de más:
rostros dibujados y simplificados, piel gris cálido, tres registros de luz,
superficie lisa, el acento como prenda mostaza mate, cartones verbatim.

- **Acento**: T1 la corbata del fiscal; T3 el suéter del fiscal; T4 la
  servidora (cárdigan) y la joven (manta), las dos personas sobre las que
  trata el enfoque diferencial.
- **Sin cara**: el equipo del T1 (atiende «en el estricto orden»), el
  procesado y los directivos (T3), el coordinador que responde y el
  investigador (T4). La **joven** no lleva cara en ningún plano: aparece una
  vez, de lejos y de espaldas, en su territorio. La agresión no se dibuja ni
  en silueta; el presunto responsable no aparece nunca; los testigos van a
  contraluz.
- **El hecho debatido no se ilustra** (T3): las órdenes y los contratos son
  elementos probatorios sobre la mesa del fiscal, nunca alguien firmándolos.
- **Hojas de personaje** (Seedream 5 Pro, en `00 PERSONAJES`): fiscal T1,
  fiscal T3, coordinadora, servidora. Entran como referencia en cada placa
  donde aparece la persona.

## Placas

Seedream 5 Pro, 2k, 16:9, dos candidatas por ranura con la hoja como
referencia: 36 ranuras. Elegidas en `herramientas/prompts/elegidas_gj.json`.
Tres cenitales salieron como **hoja de historieta** (dos o tres viñetas) en
las dos candidatas —T1 r04, T3 r03, T3 r10—: se repitieron con una cláusula
de imagen única (`UNA_IMAGEN` en `prompts_gj.py`, ahora en todo cenital).

Descartes que no fueron gusto: T1 r03 a (el papel pasaba entre los dos
asistentes, no desde la fila); T3 r04 b (vineta con tres obreros); T3 r07 a
(la mano tocaba una carpeta: el plano es que no toca ninguna); T4 r09 b (al
coordinador se le veía el perfil); T4 r16 b (el carro estaba dentro del río);
T4 r18 a y T4 r19 a (al investigador se le veía la cara); T4 r20 b (el
testigo sonreía, con cara).

## Limpieza de color

La de las situaciones (bandas frías ×0,08, amarillo suelto ×0,15 sin acento,
todo ×0,15 sin gente ni acento) **más los topes de piel** que en las
situaciones solo tenían los insertos: rosado/rojo ≤ 0,20 siempre y banda
cálida ≤ 0,22 sin acento. Las manos del T1 salieron rosadas después del
grade sin eso.

## Movimiento (V2) y detalles (V3)

Kling 3.0, 1080p, 16:9; cuadro inicial = la placa **graduada** de la ranura
(JPEG 2560 subido con `subir_gj.py`), la cláusula QUIETO al final del prompt
y un negativo por plano. `mov_gj.py kling` recorta al 88 %, limpia el color
cuadro a cuadro, retima al largo de la ranura y funde 12 cuadros de entrada
contra la ranura horneada. Prompts y descartes en `prompts/kling_gj.json`.

- **Con modelo** (8): T1 r01, r03 · T3 r02, r11 · T4 r01, r06, r13, r16.
- **Solo luz, sin modelo** (3): T3 r04 (el cielo baja un tono), T3 r08 (de
  noche), T4 r20 (los testigos a contraluz).
- **Descartes de Kling** (crudos en `_tmp/gj/mov/crudos/_descartes`):
  T1 r01 v1 — el fiscal sonreía (cuadros 32-56) y la cara se volvía 3D;
  T1 r03 v1 — el del equipo volteaba y mostraba la cara, y la hoja pasaba
  entre los dos asistentes (el mismo error de la candidata a);
  T4 r01 v1 — la cara de la coordinadora se volvía ansiosa (cejas arriba,
  boca abierta, arrugas). **Lección**: en un plano con cara, Kling sonríe,
  alza las cejas y abre la boca si el prompt deja la expresión libre o dice
  «about to speak». El prompt fija la expresión (neutral, labios quietos,
  cejas quietas) y el negativo nombra sonrisa, cejas, boca abierta, arrugas.
  Y si la cara no debe verse, el movimiento se pide **lejos** de esa persona
  (en T1 r03 ahora se mueve solo la fila).

**Detalles** (Seedream 5 Pro con la madre graduada de referencia; gesto en
Kling de 3-4 s; `detalle_gj.py placas` y `conformar`): T1 r04 el sello ·
T3 r01 la página · T3 r06 la pluma · T4 r05 el bastón · T4 r06 el teclado ·
T4 r18 la palma. Elegidas y motivos en `elegidas_gj.json["_detalles"]`.
El grade le devolvió el rosado a la mano del sello (1,34 %): `detalle_gj`
ahora vuelve a limpiar después del grade, como `construir`. La pluma v1 se
descartó (desde el cuadro 30 la mano se cerraba en puño y agarraba la pluma
como puñal); la v2 pide el mismo agarre y que solo suba la punta. Del
teclado se usan los cuadros 0-66 (`CORTE`): después la mano de abajo se
salía del teclado. Los retimes 97 → 84 daban 83 cuadros: `tpad` clona el
último y `-frames:v` corta al largo exacto.

Para mirar: `montaje/hoja_mov_gj.py` (ranura | 0 | 12 | medio | último por
clip) y `montaje/tira_gj.py` (tira de cuadros con recorte, para las caras).

## Herramientas

| | |
|---|---|
| `voz/textos/guion_gj.py` | guion verbatim + tts por bloque, temas, títulos |
| `voz/textos/rutas_gj.py` | el árbol |
| `voz/lanzar_voz_gj.py` | pide las voces |
| `voz/stt_gj.py` | Scribe contra el texto pedido |
| `voz/armar_gj.py` | máster, rejilla y ranuras |
| `rejilla/recortar_gj.py` | cortes internos por palabra |
| `prompts/base_gj.py` | reparto y lugares sobre `base_df_v1` |
| `prompts/escenas_gj_t1/t3/t4.py` | una placa por ranura + DET + MOV + rótulo |
| `prompts/personajes_gj.py` | hojas de personaje |
| `prompts/prompts_gj.py` | arma todo y escribe el storyboard .md de cada tema |
| `prompts/bajar_placas_gj.py` · `subir_gj.py` | Magnific ida y vuelta |
| `prompts/elegidas_gj.json` | candidata por ranura |
| `montaje/gj_pieza.py` | elegir · construir · blancos · musica · montar · revisar · exportar · entregas · verificar |
| `montaje/mov_gj.py` · `detalle_gj.py` | V2 movimiento · V3 detalle |
| `montaje/hoja_mov_gj.py` · `tira_gj.py` | hojas para mirar movimiento, detalles y caras |
| `montaje/hoja_linea_gj.py` | la hoja de `revisar` compuesta desde la media, sin render |
| `montaje/revision_ffmpeg_gj.py` | la línea entera compuesta con ffmpeg (V1-V8, voz, música, intro): cuadros, negros, loudness, hoja; revisión cuando Resolve no rinde |
| `cartones/cartones_gj.py` | cartones a mano; el tiempo sale de Scribe |
| `cartones/lowerthirds_gj.py` | un rótulo por caso, en la r01 |

## Dónde está cada cosa

```
E:\DAE MASTER\PRIORIDAD 2\CURSO - GERENCIA JUDICIAL\
  00 DOCUMENTOS FUENTE\   el .docx del Drive y el texto con comentarios
  00 PERSONAJES\          4 hojas (+ _crudos con las 8 candidatas)
  TEMA 1 - El despacho de los 2000 casos\        las diez carpetas de siempre
  TEMA 3 - Aceptar o negociar\
  TEMA 4 - Dos situaciones al comenzar la semana\
```

Los mismos bins en Resolve (`DAE MASTER - CURSOS`): PRIORIDAD 2 › CURSO -
GERENCIA JUDICIAL › TEMA n. La línea de cada tema va en su
`10 TIMELINE SEBASTIAN`, con su `.drt` en la carpeta del mismo nombre.

## Decisiones de la segunda pasada (29 oct, tarde)

Sebastián: «you make the decisions… I will check and approve everything at
the end». Lo que decidí, y por qué:

- **El acento del T4 se lleva al de la serie.** Medido en las placas
  graduadas: suéter del T3 41-47°, saturación ~0,5; DF 45°. El cárdigan de la
  servidora y la manta de la joven salieron a 31-34° (naranja) y hasta 0,78.
  `gj_pieza.ACENTO = {'T4': (+7 PIL ≈ 10°, ×0,9)}` después del grade, cuadro a
  cuadro en `mov_gj` y en la saturación de los detalles (el tono del detalle
  ya se iguala a la madre). Quedó: r05 32,5° → 40,9°, r06 31,1 → 40,9,
  r07 33,9 → 43,8 (0,78 → 0,70), r09 35,3 → 45,2.
- **T3 r01: el detalle de la página ya no pisa el rótulo.** El rótulo
  «Fiscal delegado» ocupa los cuadros 14-134 de la ranura; el detalle entraba
  en el 100. Ahora entra en el 140 y dura 58 (se usan los cuadros 0-63 del
  crudo: la hoja cae hacia el 40 y después la mano está quieta).
- **El último cartón de cada tema ya no entra al cierre.** Se estiraba hasta
  90 cuadros después de la voz y se metía ~28 cuadros en el cartón blanco de
  cierre. Puede sostenerse sobre el respiro, nunca pasarlo
  (`cartones_gj.calcula`). Cambian T1 p02 (181 → 153), T3 p07 (219 → 192),
  T4 p17 (149 → 122); se requemaron solo esos tres.
- Se quedan como están: T1 r03 en 94 cuadros (cortado por palabra), los
  cartones del T4 al 70 % (es lo que la voz dice; p14 lee a 17,5 car/s pero
  es verbatim de lo que se oye), el piso de 96 de la rejilla.
- **El render de revisión con vigía**: si el porcentaje no se mueve en 240 s
  se para (`_tmp/gj/cadena_revisar.py`); la primera vez Resolve se colgó en
  0 % y hubo que reiniciarlo.

## Revisión de Sebastián (29-30 oct)

T1 y T3 aprobados (con ajustes suyos a mano en Resolve: no se tocan). En el
T4, **r06 y r07** no funcionaban: el texto habla de una servidora ciega a la
que el aplicativo nuevo no le sirve con el lector de pantalla, y en las placas
ella miraba la pantalla y leía. Rehechas sin remontar su línea:

- **r06** (placa c): cámara delante de ella, el monitor a un lado del cuadro,
  la cara vuelta lejos de él y hacia abajo, la mano apretando el audífono, la
  otra quieta en el teclado: el lector se quedó callado. La primera tirada ya
  decía «her eyes not on the screen» y el modelo la puso de perfil mirando el
  monitor: lo que funcionó fue la composición (cámara de frente, monitor al
  costado) y «she is blind and she works by ear».
- **Movimiento r06**: el primer Kling la hacía girar hacia la pantalla al
  bajar la mano al teclado (descartado). El bueno: cuadro inicial y final la
  misma placa, ella sigue escuchando con la mano en el audífono y teclea con
  la otra; nunca mira el monitor.
- **Detalle r06**: el teclado a dos manos ya no casaba (ahora tiene una mano
  en el audífono). Pasa a `la_escucha`: la mano en el audífono, los ojos bajos
  (cuadros 0-53 del crudo: después los ojos subían hacia el monitor).
  Mismo largo y misma entrada; el clip de la línea se reapuntó con
  `ReplaceClip` al archivo nuevo.
- **r07** (placa e): en la planta, todos miran su pantalla menos ella, que
  escucha con la cabeza baja y el bastón plegado en el escritorio. Las dos
  primeras tiradas (c, d) le pusieron DOS audífonos —uno puesto y otro al
  cuello, porque la hoja de personaje lo trae al cuello—: se repitió con la
  r06 nueva como referencia y «ONE headset, ON HER EARS; NOTHING around her
  neck».
- **Acento**: para las placas nuevas el giro se mide (objetivo 42°,
  saturación ≤ 0,55: `ACENTO_AUTO` en `gj_pieza`), porque ya no traían el
  naranja de la primera tirada.
- **En sitio** (`montaje/reemplazar_en_sitio_gj.py`): los cuatro medios se
  releyeron con `ReplaceClip`; retrato de los 58 clips de su línea antes y
  después: misma pista, entrada, salida y desplazamiento en todos; solo cambió
  el nombre del archivo del detalle.

## Estado (29 oct, cierre)

- Las tres líneas **remontadas** con las decisiones de la segunda pasada
  (largos exactos 1176 / 2872 / 4877, ninguna capa faltante, `.drt`). Las
  anteriores quedaron en el proyecto como «(anterior)».
- **Resolve volvió a rendir después de reiniciar el computador** (los tres
  cuelgues en 0 % eran del estado de la máquina: ni el códec ni la línea).
  Revisión interna de Resolve en `D:\DAE\_tmp\gj\revision\GJ_<T>_v1_REVISION_INTERNA.mp4`:

  | | cuadros | negros | integrado | pico | render |
  |---|---|---|---|---|---|
  | T1 | 1176 / 1176 | ninguno | −21,0 LUFS | −5,0 dBFS | 9 s |
  | T3 | 2872 / 2872 | ninguno | −19,9 LUFS | −4,1 dBFS | 18 s |
  | T4 | 4877 / 4877 | ninguno | −19,3 LUFS | −4,3 dBFS | 30 s |

- El render de Resolve es exacto al cuadro (el detalle de T3 r01, medido
  contra su archivo, cae en el cuadro que dice el plan). El armado de
  `revision_ffmpeg_gj.py` coincide en loudness y largo pero va ~1 cuadro
  tarde en las capas: queda solo como respaldo si Resolve vuelve a colgarse.
- **Sin exportar y sin subir a Drive**: va con el OK de Sebastián.
