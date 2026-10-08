# CLAUDE.md

Memoria de trabajo de este repositorio. Léela entera antes de hacer nada: contiene decisiones ya
tomadas, medidas reales y trampas técnicas que costaron horas de descubrir. **Nada de lo que está
acá es una suposición; todo salió de medir.**

---

## Quién y qué

**Sebastián** (Joan Sebastián Realpe Rojas) produce la serie audiovisual de la **Dirección de Altos
Estudios de la Fiscalía General de la Nación, Colombia**. Monta en DaVinci Resolve, genera los
planos con IA, y hace los gráficos en After Effects.

Son piezas de formación para fiscales: estudios de caso de tres a nueve minutos, narradas, con
planos ilustrados, cartones de texto y voz sintetizada en ElevenLabs.

### Cómo trabaja, y cómo hay que trabajar con él

- **Medir, no asumir.** Cada vez que se estimó algo a ojo —duraciones, posiciones, niveles— salió
  mal. Cada número de este archivo salió de leer el archivo real, la línea de tiempo real o el
  render real. Si hace falta un dato, se va y se mide.
- **Verificar el resultado, no el comando.** Después de cada mutación en Resolve, leer de vuelta.
  La API dice que sí y hace otra cosa más seguido de lo que parece.
- **Él edita entre llamadas.** Mueve clips, apaga pistas, escala cartones a mano. Nunca confiar en
  un número de frame anotado hace diez minutos: releer la línea de tiempo y anclarse a los clips de
  voz, no a posiciones recordadas.
- **Nada se borra.** Si algo sobra, va a una carpeta `_descartes`. Él decide.
- **Se responde en español**, en su registro. Él escribe mezclando inglés y español; la respuesta
  va en español rioplatense-neutro, directa, sin relleno.

---

## Los cuatro cursos

| | curso | estado |
|---|---|---|
| 1 | **SRPA** — Sistema de Responsabilidad Penal para Adolescentes | terminado. Profes Edwin (casos A y B), Carlos Humberto (casos 5 y 6), Hugo Ascencio (caso Ipanema) |
| 2 | **Delitos contra el medio ambiente** — 5 unidades | introducciones en montaje. La U1 tiene 17 cartones colocados |
| 3 | **Bernardo JEP** — 5 videos | videos 2, 3 y 4 terminados |
| 4 | **Terminaciones Anticipadas** — 8 casos elegidos | en guion. El caso 02 tiene preproducción completa |

### Dónde vive cada cosa

```
E:\DAE MASTER\          el máster. Un curso por carpeta, unidad/caso adentro,
                        y dentro de cada uno: 01 PLANOS · 02 CARTONES · 03 VOCES ·
                        04 B-ROLL · 05 EXPORTS · 06 GUION Y STORYBOARD · 07 MUSICA
E:\DAE MASTER\00 COMUNES\   intro, outro, marca de agua, cartones alfa de referencia, música
E:\DAE MASTER\_PROYECTO RESOLVE\   el .drp exportado
D:\DAE  ·  D:\FISCALIA  los originales de trabajo (respaldados en E:\...\respaldo de d)
D:\DAE\_repo            este repositorio
```

Proyecto de Resolve activo: **`DAE MASTER - CURSOS`**. El viejo se llama `DAE` y sigue existiendo
con el trabajo de JEP; no se toca.

**Qué entra al repo y qué no.** Todo lo que sea **solo texto** —guiones, bloques de voz, prompts,
rejillas, scripts, decisiones, selecciones— se empuja a GitHub de una, sin preguntar y sin esperar
a que termine la tarea. Regla fijada por Sebastian. Las imágenes, los audios y los renders se
quedan en `E:\DAE MASTER` y se referencian por ruta desde el documento que los usa: un PNG de
2560 x 1440 pesa ~8 MB y git no es el lugar para eso.

Estructura por serie: `cursos/<curso>/README.md` con el indice y el estado, `fuentes/` con el
material del profesor, y `casos/<caso>/` con `00_preproduccion.md`, `01_guion_y_prompts.md`,
`02_seleccion_keyframes.md`.

---

## El formato de las piezas

**23,976 fps · 1920 × 1080 · DaVinci YRGB · Rec.709 (Scene) · scaleToFit.**

Estructura fija, en frames relativos al inicio de la línea de tiempo:

| | qué | duración |
|---|---|---|
| 0 | intro institucional (`FGN_intro_version7.mp4`) | **194 f** |
| 194 | cartón de caso / de título | **119 f** |
| 313 | el cuerpo | variable |
| fin | cartón de cierre | 119 f |
| | outro institucional | 194 f |

Los cartones de pausa dentro del cuerpo son de **144 f** (6 s).

### Duración

**La locución va a 150 palabras por minuto.** Medido contra el narrador real del caso A. La fórmula
vieja de 142 subestimaba, y el multiplicador 1,22 sobreestimaba un 20 %.

Para estimar una pieza terminada: `palabras ÷ 150 × 60 × 1,10 + 30 s`. El 1,10 son las pausas
internas (medido en JEP: 6,60 sílabas/s hablando contra 6,07 overall); los 30 s son intro, cartón
de entrada y cierre.

Cuidado con una trampa: estimar sobre el **texto crudo del guion del profesor** da un número muy
bajo, porque un guion de producción siempre lo desarrolla. El caso 02 pasó de 150 palabras crudas
a 274 escritas — de 1:33 estimados a 2:21 reales.

### Pistas

Nombres fijos. Vídeo: `VIDEO · CARTONES · APOYO / B-ROLL · MARCA DE AGUA · EFECTOS · LOWER THIRD ·
LOWER THIRD 2`. Audio: `VIDEO · NARRADOR · FACILITADOR (mono) · DIALOGO · MUSICA`.

**El facilitador va en su propia pista aunque sea la misma voz y el mismo archivo** que el
narrador: dramáticamente es otro personaje —el único que mira al lente— y así se le puede dar su
propia mezcla, un poco más cerca y con sala más seca, sin tocar la narración.

---

## Los cartones

Hay **dos rejillas conviviendo**, por pedido distinto de cada área. No mezclarlas.

### Rejilla A — serie JEP y casos SRPA (con tinte)

Barra `#FEB900`, 14 px, borde izquierdo **x=175** · texto Montserrat blanco desde **x=243** ·
centro óptico **y=590** · ancho máximo **1330** · sangría 62 · aire de barra 64.
Título Bold 58 · cuerpo Medium 48 · frase suelta Bold 64.
Tinte `#03398B` al **46 %** (alfa 117/255), que es la fórmula medida del render del video 3:
`out = img × 0,539 + (1,3 / 26,2 / 63,8)`.
Fundidos planos de 12 f de entrada y 10 f de salida.

### Rejilla B — introducciones de medio ambiente (en caja, sin tinte)

La DAE marcó un recuadro: el texto vive dentro de **x 62–790, y 250–720**. Medido además contra la
locutora en cuadro: ella ocupa de x≈790 a la derecha entre y 240 y 720, y por debajo de y 720 el
hombro se abre hacia la izquierda.

Barra 14 px en **x=86** · texto desde **x=170** · ancho máximo **615** · el bloque se ancla **abajo
en y=690 y crece hacia arriba**, para que los cartones cortos queden lejos de su cara.
Antetítulo Medium 29 · título Bold 46 · cuerpo Medium 37 · frase suelta Bold 54.

**Sin tinte.** La legibilidad la resuelven tres sombras bajo el texto y bajo la barra:

| capa | difuminado | opacidad | desplazamiento |
|---|---|---|---|
| núcleo | 3 px | 85 % | — |
| ambiental | 22 px | 70 % | — |
| contacto | 7 px | 70 % | 0, +4 |

Sin contorno ni borde duro: sobre cielo claro y sobre edificio se sostiene igual.

**Animación.** La barra crece desde arriba en 10 f con desaceleración cúbica. El texto entra desde
el frame 6, línea por línea: cada una sube 14 px mientras aparece en 14 f, escalonada 3 f. A la
salida se van en el mismo orden —10 f cada una, subiendo 8 px, escalonadas 2 f— y la barra se
retrae hacia arriba en los últimos 10 f.

El generador es `herramientas/cartones/cartones_v3.py`. Rinde cuadro a cuadro con Pillow y
canaliza a ffmpeg. Necesita Montserrat instalada y ffmpeg en el PATH.

### Códec

**QuickTime Animation (qtrle, `-pix_fmt argb`).** PNG-in-MOV **falla** la decodificación a
resolución completa de Resolve al exportar. No usarlo.

---

## Audio

- Voz: **−19 LUFS**, techo **−1,0 dBTP**, **estéreo dual-mono** 48 kHz.
- Música bajo voz: **−32 dB**; en los huecos **−26 dB**. Ataque 0,25 s · relevo 0,70 s ·
  retención 0,30 s.
- **La trampa del √2.** `ffmpeg -ac 1` sobre un archivo estéreo suma los canales con factor √2,
  o sea **+3,01 dB**. Medir siempre con `mean(L,R)` o por canal.
- **Un clip mono en una línea estéreo suena sólo por la izquierda.** La solución es entregar
  dual-mono, no el Stereo Fixer.
- En ElevenLabs las cifras van **en letras**: «ciento veinte millones», no «$120 millones». Los
  sintetizadores leen los símbolos de forma impredecible y en español latino suelen agregar
  moneda equivocada. Los números van a los cartones, no a la voz.

---

## Las trampas de la API de Resolve

Todas descubiertas rompiendo cosas. Respetarlas.

- **`move_clips` y `duplicate_clips` reinterpretan los rangos de origen entre frame rates.** Un
  clip de 30 fps pasó de 117 a 93 frames; un clip con retime perdió el retime. **No usarlos para
  nada que no sea 23,976 a 1:1.**
- `move_clips` **no mueve audio** y **recorta** los items cuyo destino pisa a un vecino que todavía
  no se movió. Hay que pasar los ids en orden, de derecha a izquierda cuando se mueve a la derecha.
- **El método bueno para reposicionar:** borrar el item y volver a añadirlo en su posición exacta
  con el rango de origen completo. Es lo que funciona.
- `delete_clips(ripple=True)` **rippleó A1 pero no V1**: desincroniza imagen y sonido. No usar.
- `insert_generator` sí hace un ripple de verdad y conserva retimes, transiciones, compound clips y
  glows — pero está **fijo en 120 frames** y `timelineDefaultStillDuration` **no es escribible**.
  Y **no ripplea V3 ni V4**: los cartones hay que reposicionarlos a mano después.
- **Un still no se puede estirar por API.** `AppendToTimeline` ignora `endFrame` para imágenes fijas
  y usa la duración por defecto, 24 f. `SetClipProperty` sobre Duration/Frames/End devuelve False.
  La solución fue rendir la marca de agua como **clip de video con alfa** y repetirlo.
- **El media pool cachea la duración del archivo.** Si se sobrescribe un archivo en su sitio, queda
  la duración vieja. Hay que guardar con **nombre nuevo** y reimportar.
- `get_property` devuelve `null`; `GetTrackEnabled` y `GetEndTimecode` no existen en esta build;
  la API de keyframes lanza `'NoneType' object is not callable`. `get_transform` sí funciona.
- `endFrame` en `AppendToTimeline` es **exclusivo**: `endFrame: 194` da 194 frames desde 0.
- **`script_plugin run_inline` da un shell de Python completo en la máquina de Sebastián.** Es la
  herramienta más potente de todas: llega a E: y a D:, mueve archivos, corre git. Las herramientas
  de dispositivo no alcanzan E:.
- La transcripción de Resolve funciona bien: `folder.transcribe_audio(background=True)` → sondear
  `job_status` → `timeline.subtitle_generation_probe({allow_generate: true})` → leer los items de
  la pista de subtítulos. `CreateSubtitlesFromAudio` directo devuelve False.

---

## Reglas duras de contenido

- **No se inventa derecho.** Si la lección del profesor no enuncia una regla, el guion no la
  afirma. Las preguntas del documento cargan la tesis; el narrador narra hechos. Los profesores
  son difíciles de localizar y la institución exige apegarse a lo escrito por ellos.
- **No se inventa lo que el expediente no dice.** Ni precariedad, ni conflicto, ni emoción no
  atribuida. Verificar la geografía real antes de describir un entorno.
- **Ningún texto legible en las imágenes.** Ni placas, ni marcas, ni escudos, ni banderas, ni
  membretes, ni firmas. Todo lo institucional entra en After Effects.
- **Placa limpia siempre.** El texto, la barra amarilla y el tinte son capas de DaVinci; nunca se
  le piden a la imagen generada. Todo prompt lo declara y todo negativo lo bloquea.
- La paleta: entorno **enteramente en grises**, 80/20, un solo saturado por composición. Un matiz
  por personaje. Ladrillo siempre desaturado. Luz **neutra siempre** — ninguna hora dorada, ningún
  cielo naranja, ningún sodio, ningún azul lunar. Sin god rays, sin destellos, sin cámara inclinada.
- Piel cálida y natural, rostros completos con iris, pupila y brillo. Lo que va en grises es el
  entorno y el reparto anónimo, no la gente.

---

## La regla verbatim, en concreto

«Apegarse al material escrito por los profesores» significa, medido contra el Caso 02 donde me fui:

- **Lo literal es la LOCUCIÓN, no la imagen.** No se inventan parlamentos: si el profesor narra en
  tercera persona —«la defensa manifiesta su interés»— eso NO se convierte en un abogado hablando
  en primera persona. Pero **a quien el narrador nombra hay que verlo**: si dice «el fiscal», hay
  un fiscal en cuadro, con cara, el mismo en toda la pieza. Dibujar al abogado está bien; ponerlo
  a hablar, no.
- **Un personaje que el texto no nombra no existe**, ni hablando ni en imagen. El «facilitador» del
  Caso 02 fue invención mía: las preguntas las hace «el o la fiscal», que sí está nombrada.
- **Si el texto dice que algo no se puede identificar, no se dibuja.** Los dos del hurto del Caso 06
  van sin cara porque el caso existe por eso.
- **No se trae doctrina de otra lección al ejemplo.** El texto expositivo de la lección sirve para
  entender, no para meterle párrafos al caso.
- **Si la pieza queda más corta, mejor.** La duración no es un objetivo.

La forma de cada caso de Terminaciones Anticipadas es la que el profesor ya escribió:

```
1 - «Veamos un ejemplo...»
2 - La narración, literal, una sola voz de narrador sobre los planos
3 - Las preguntas del guion, literales, en cartón sostenido con música
```

Las preguntas NO las dice un personaje a cámara: el profesor las escribió como lista, y una lista
dicha mirando al lente son preguntas que nadie escuchó.

## Música

Se reusa la de la serie — hay trece pistas repartidas entre `E:\DAE MASTER`, `D:\DAE` y
`D:\FISCALIA`. La cama se arma con `herramientas/musica/cama_musica.py`, que entrega un MP3 320
a 48 kHz con **el ducking ya horneado**, porque la API de este build no deja escribir niveles ni
keyframes de audio. El clip entra a A5 con la ganancia en cero.

```
voz       −19 LUFS
música    −32 LUFS bajo la narración  (13 dB por debajo de la voz)
música    −26 LUFS en los huecos y bajo el bloque de preguntas
```

Se normaliza a −26 y se bajan 6 dB donde hay voz, con rampas de 1 s. El bloque de preguntas no se
duckea. La cama entra con el cartón de entrada y sale con el de cierre.

**Hay que rehacerla cuando cambien las voces**: el ducking se calcula contra tramos concretos, así
que si la locución se mueve, la música baja donde no habla nadie.

## Voces

Las voces las pide Sebastián desde SU cuenta de ElevenLabs, con sus propias voces. El catálogo de
Magnific no sirve: casi no tiene colombianas y las que tiene no suenan al acento que la DAE pide.
**Acento latino neutro** — ni español, ni argentino, ni mexicano. En el registro de conectores no hay
MCP de TTS de ElevenLabs (el único es de agentes de voz).

Yo entrego los bloques de texto, él genera, y yo masterizo, nombro, ubico e importo.

**Masterización: `loudnorm` en UNA pasada estima mal** — pedí −19 LUFS y salió −16. Hay que hacer
las dos pasadas (medir primero, aplicar con los valores medidos después). Destino: −19 LUFS,
−1,0 dBTP, dual-mono estéreo, 48 kHz. Un MP3 mono a 44,1 kHz suena solo por el canal izquierdo.

## Kling: completa el gesto, y resuelve la situación

Dos tandas medidas (Caso 02 y Caso 06, Kling 2.5 a 720p desde keyframe de entrada):

**A 5 s completa el gesto.** Si en cuadro hay dos manos y un objeto, alguien lo agarra, por más
que el negativo lo prohiba tres veces.

**A 10 s resuelve la situación entera.** No sostiene un estado durante diez segundos: las figuras
salen del cuadro y el local queda vacío, la reja baja sola aunque se diga tres veces que no se
mueve, y el que firma levanta el bolígrafo y **sonríe a cámara**. De seis loops de 10 s, tres
sirvieron enteros, dos sirvieron recortando el primer tercio y uno se descartó.

**Entonces: pedir 5 s por defecto**, y para un hueco más largo estirar el loop con `setpts` en
vez de pedir más segundos — en un plano casi quieto un 20 % de ralentí no se ve, y una acción
que se completa sí.

**Los planos cuyo sentido es que algo NO pasa no van a Kling** — el sobre que nadie tiene, la mano
plana sobre la carpeta cerrada, las cuatro carpetas con el hueco, el mapa sin marcas. Esos se
quedan quietos con un push lentísimo hecho en Resolve, que además no cuesta créditos.

Lo que sí funciona: una acción que se completa sola (una página que termina de voltear), una
figura quieta que respira y sostiene la mirada, una calle que vive mientras el objeto del plano
se queda inmóvil, y alguien que cruza y sale de cuadro.

**Ajustar el loop al hueco antes de montarlo.** Se re-encodea con `setpts=<n/orig>*PTS,fps=...` y
`-frames:v <n>`, así el clip entra con el número exacto de frames y no hay que retimarlo en
Resolve, donde la API no ayuda. Ojo: los loops salen a **1280x720** y suben a 1080 en la línea,
mientras los sostenidos son 2560x1440.

### Lo medido antes

Medido con tres pruebas del Caso 02 (Kling 2.5, 720p, 5 y 10 s): si en cuadro hay dos manos y un
objeto, el modelo hace que alguien lo agarre, por más que el negativo lo prohiba tres veces.

**Los planos cuyo sentido es un gesto que NO se completa no van a Kling** — el sobre que nadie
tiene, la mano plana sobre la carpeta cerrada. Esos se quedan quietos con un push lentísimo hecho
en Resolve, que además no cuesta créditos. Lo que sí funciona: una acción que se completa sola
(una página que termina de voltear) y una figura quieta que respira y sostiene la mirada.

Costos medidos (video_generate, desde keyframe de entrada): Kling 2.5 720p 5 s = **140 créditos**,
10 s = 280, 1080p 5 s = 325. Es de lejos el más barato del catálogo; el siguiente es MiniMax H3 Max
Turbo a 200 y de ahí salta a 1050.

## El método de prompts hero

Está completo en el proyecto de claude.ai (`Metodo_Prompts_Hero_DAE.md`). El resumen operativo:

Antes de escribir un prompt, en este orden: **releer qué dice el expediente y qué se estaría
inventando · encontrar el gesto · buscar la referencia fotográfica y leer su geometría · decidir
dónde se para la cámara y qué afirma eso · darle a cada persona una acción y una dirección de
mirada distintas · escribir el bloque · escribir el negativo contra los fallos de ese plano.**

Lo que más importa:

- **La posición de la cámara es el argumento.** Si la respuesta a «¿qué afirma la cámara por estar
  parada ahí?» es «para que se vea bien», el plano todavía no existe.
- **El gesto único antes que la cara.** Una escena se sostiene sobre un objeto en una posición en
  un instante. El plano canónico es el mostrador del Caso 5: *el papel devuelto sobre el laminado,
  y ninguna de las dos lo tiene*. Ese medio segundo es el «no» completo.
- **La emoción va en las manos.** Las caras salen genéricas; las manos no.
- **Media acción, nunca el pico.** Boca abierta a media palabra, pie de atrás todavía levantado.
  Congelado, no borroso: el movimiento lo dan las poses, no las estelas.
- **Bloquear las dos versiones opuestas del cliché.** Ni cruel ni bondadosa. Ni heroica ni rota.
- **Una instrucción de cámara o de foco se repite dentro del párrafo del plano.** El bloque de
  estilo no basta.
- **Un objeto crítico se describe por sus efectos, no por su nombre.** «Una silla pequeña» no
  produjo una silla pequeña; «claramente construida para un niño, el espaldar llegando sólo a la
  altura de la mesa» sí.
- Desenfoque **pintado, no fotográfico**: forma simplificada y borde suave, nunca discos de bokeh.

---

## Cartones: la retícula de verdad

Medida sobre los cartones del profe Edwin (`A_carton_pausa1.mov`, `A_carton_cierre.mov`,
`U1-PROFE EDWIN - CASO A - carton de caso.mp4`), que es la escala de la serie de Terminaciones
Anticipadas:

```
barra    #FCB500 - 28 px de ancho - borde izquierdo en x=176
texto    Montserrat - x=249 - ancho máximo 1250
centro   óptico del bloque en y=583
tinte    #03398B al 46 % (alpha 117) sobre todo el cuadro
blanco   fondo #FCFCFC - texto azul noche #07224B
marca    APRENDE CON LA DAE - 408 px de ancho - en (1351, 131) - al 10 %
tamaños  antetítulo SemiBold 30 - título Bold 54 - cuerpo Medium 44 - suelta Bold 72
```

La nota vieja de la serie JEP decía barra de 14 px en x=175: esa es otra escala. Si un cartón de
Terminaciones Anticipadas se ve flaco, se hizo con la retícula vieja.
Generador: `herramientas/cartones/cartones_ta.py`.

## Bajar de Magnific

**Trampa del verificador (ya corregida):** `bajar_de_magnific.py` revisaba la extensión del archivo
temporal `.parcial` en vez de la del destino, y rechazaba absolutamente todo con «no tiene el
encabezado del formato que dice la extensión». Si vuelve a fallar en bloque, mirar ahí primero.

### Cómo funciona

El contenedor en la nube **no alcanza** `pikaso.cdnpk.net`: el proxy de salida responde 403. La
máquina de Sebastián sí. Entonces se arma un manifiesto JSON y se corre
`herramientas/magnific/bajar_de_magnific.py` con `script_plugin run_inline`, que es un Python
completo sobre esa máquina y ve E: y D:. Las URL llevan token con vencimiento: ante un 403 o 410
hay que volver a pedir la URL con `creations_wait`, no reintentar.

## Dos trampas más de la API, medidas

- **`endFrame` en `AppendToTimeline` es exclusivo.** Para un clip de N frames se pasa
  `endFrame = N`, no `N-1`. Con `N-1` todo queda un frame corto y la línea se llena de huecos de
  un frame que no se ven en el timeline pero sí en el render.
- **Al outro no se le pasa rango de origen.** Está a 30 fps; apendizado sin `startFrame`/`endFrame`
  Resolve lo conforma solo (150 f a 30 -> 119 f a 23,976). Pedirle un rango es lo que rompe los
  clips de otra velocidad.
- Hay una carpeta del pool que se llama ` 00 COMUNES` **con espacio adelante**: comparar nombres
  de carpeta con `.strip().upper()`.

## Intro y outro: son el mismo archivo, y traen audio

`FGN_intro_version7.mp4` dura 222 frames en disco, pero la serie lo usa **recortado a 194**,
origen 0..193, y el **mismo clip va al principio y al final**. Así están `MA - U1 - INTRODUCCION`
y `TA - CASO 01 - PLANTILLA`.

**Trae audio** (estéreo AAC 48 kHz) y va en **A1 · VIDEO**, en los dos extremos. Un clip
apendizado con `mediaType: 1` entra **mudo**: hay que apendizar el mismo clip otra vez con
`mediaType: 2` sobre la pista de audio. Es el error fácil de cometer y el que Sebastián nota.

El `.mp4` de criptoactivos que está en la carpeta OUTRO **no tiene pista de audio**
(`Audio Ch = 0`) y no es el outro de la serie.

## La estructura de pistas de la serie

Sale de `TA - CASO 01 - PLANTILLA`. Toda línea nueva de Terminaciones Anticipadas se arma así,
no con nombres propios:

```
V1 VIDEO   V2 CARTONES   V3 APOYO / B-ROLL   V4 MARCA DE AGUA
V5 EFECTOS V6 LOWER THIRD V7 LOWER THIRD 2
A1 VIDEO   A2 NARRADOR   A3 FACILITADOR   A4 DIALOGO   A5 MUSICA
```

La marca de agua (`MARCA_DE_AGUA_DAE_100s.mov`, 2400 f) va en V4 desde el cartón de entrada
hasta el de cierre; si el cuerpo pasa de 2400 f se ponen dos instancias, que no se nota la
costura porque la marca es estática. La música va en A5.

## Planos como `.mov`, no como `.png`

Por la limitación de los stills descrita arriba, los planos van como **sostenidos `.mov` de
dieciséis segundos**, generados con ffmpeg a **2560 × 1440** — la línea es 1080, así que sobra un
33 % de margen para los empujes de cámara — y se colocan con rango de origen. Los PNG originales
no se tocan: siguen siendo la fuente para Magnific cuando toque animar.

---

## Estado al día de hoy

- **Medio ambiente U1**: 17 cartones v3 colocados en `MA - U1 - INTRODUCCION`, a zoom 1.0 y pan 0
  (el tamaño está horneado en los archivos). Sin marca de agua: ese video ya tiene bastantes logos.
  Pendiente: replicar en U2–U5, que todavía tienen el montaje de la primera pasada.
- **Terminaciones Anticipadas**: ocho casos elegidos, cinco de la Unidad 4 y tres de la Unidad 1.
  El caso 02 tiene guion, bloques de voz, rejilla, cartones y desglose de los ocho planos.
  Siguiente paso: referencias fotográficas de los KF 02, 04 y 07, y después los prompts.
- **Plantilla**: `TA - CASO 01 - PLANTILLA` en el proyecto de Resolve, con intro, cartón de
  entrada, marca de agua, música y las doce pistas nombradas.

### Dos cosas abiertas

1. **¿Esta serie lleva tinte azul en los cartones?** Los casos de Edwin sí; medio ambiente pidió
   sin tinte y en caja fija. Son dos criterios conviviendo y hay que confirmar cuál aplica.
2. **La voz del abogado defensor.** Si es nueva en ElevenLabs hay que reservarla: la defensa
   aparece en casi todos los casos de Terminaciones Anticipadas.

## Mayusculas sostenidas: nunca

Ni versalitas ni mayusculas sostenidas en ningun carton de la serie. La unica
excepcion es la marca de agua APRENDE CON LA DAE, y ahi las mayusculas son parte
del logotipo. El generador no llama `.upper()` en ninguna parte y asi debe quedar.
El carton de entrada es `Caso:` arriba (SemiBold 30) y el nombre entre comillas
angulares abajo (Bold 54). Ver `identidad_cartones.md`.

## ffmpeg en esta maquina

No esta en el PATH del subproceso que abre `run_inline`. Esta en:

    C:\Users\call_\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin

Siempre invocar ffmpeg y ffprobe por ruta completa desde `run_inline`.

## El puente corta a los 60 s

`script_plugin run_inline` acepta un `timeout` grande, pero el puente al equipo
responde "did not respond within 60s" y se pierde la respuesta. El script sigue
corriendo y termina bien: antes de repetirlo hay que mirar el disco y `tasklist`,
porque relanzarlo encima de un ffmpeg vivo es lo que dejo medios corruptos en el
Caso 06. Partir los trabajos largos en pasos de menos de un minuto.

## Ajustar un loop de Kling a su ranura

Los loops salen 1280x720, 241 cuadros, 24/1. La serie va a 1920x1080 y 24000/1001.

- Ranura mas corta que el loop: ventana a velocidad nativa. Acelerar un Kling se
  nota mucho mas que frenarlo.
- Ranura mas larga: `setpts` con `k = n * 1.001 / 241`. El 1.001 es el paso de 24
  a 23.976; sin el se pierde un cuadro.
- Escalar a 1920x1080 con lanczos en el encode, no en la linea.
- Revisar el arranque del loop antes de cortar: a 10 s Kling resuelve la situacion
  entera y suele sacar figuras de cuadro en los primeros segundos. Si eso pasa, se
  entra despues (en el KF05 del Caso 02, desde el cuadro 40).

## Identificadores de Magnific

Confirmar que el identificador corresponde al PLANO y no solo a la variante antes
de mandar a generar. Pedir el KF05 con el id de la variante B del KF04 costo 280
creditos y un plano equivocado.

## El outro NO se conforma solo

Estaba mal escrito aqui. `FGN_intro_version7.mp4` dura 222 cuadros en disco.
Si se agrega sin startFrame/endFrame entra con sus 222, no conformado a 194.
La serie lo usa SIEMPRE recortado: `startFrame 0, endFrame 194`, tanto en el
intro como en el outro, y en video y en audio por separado.

## Nombrar un objeto critico no basta, hay que medirlo

El KF05 del Caso 08 pedia "su rostro legible" y salio un plano general con el
hombre al fondo. Lo que si funciono fue describirlo por efectos y por comparacion
de tamano: "la grabacion tiene zoom fuerte, la cabeza ocupa un tercio del alto de
la pantalla, es mas grande que el dedo que se acerca desde abajo, las cejas y las
comisuras se ven una por una". Es la regla 9 del metodo de prompts, y cuesta 100
creditos cada vez que se olvida.

## La formula de duracion estima la narracion, no la pieza

`palabras / 142 * 60 + 26 s` no cuenta el bloque de preguntas, que en esta serie
es tiempo de pantalla real. El Caso 08 da 57 s por formula y quedo en 1:35. Para
estimar de verdad: narracion por formula, mas el bloque de preguntas calculado
aparte a 142 palabras por minuto con aire.

## Medio punto menos de color en el entorno

Dicho por Sebastian sobre el Caso 08: la composicion grafica mejoro, y la mezcla
de colores alrededor esta bien, pero el ENTORNO necesita medio punto menos de
saturacion. No la piel, no el acento de color del personaje: el entorno.

En el prompt se escribe como "environment almost fully desaturated, only the
faintest trace of colour left in the greys, close to neutral grey but not quite
monochrome", en vez del "entirely desaturated greys" que se venia usando. La piel
sigue calida y natural y el unico saturado por composicion no cambia.

## Cartones de narracion

La primera mitad de cada pieza tambien lleva cartones de tinte azul, no solo el
bloque de preguntas. Tres por video, de 91 a 142 cuadros, en V2, puestos donde la
narracion dice el dato. Menos que en el bloque de preguntas, pero algunos.
El texto es literal del guion del profesor: nombres, cifras y frases suyas. Un
carton que inventa una sintesis ya no es el texto del profesor.
Generador: `herramientas/cartones/cartones_narracion.py`.

## El bug de los -16 NO era loudnorm

Estaba mal escrito aqui y hay que corregirlo. Pedir -19 y obtener -16 no era
porque loudnorm estimara mal en una pasada. Era el ORDEN del master: se
normalizaba y DESPUES se convertia a estereo dual-mono, y duplicar un canal mono
en L y R suma 3 dB a la medida EBU R128. Exactamente los 3 dB que faltaban.

Orden correcto:
  1. aresample a 48000
  2. pan=stereo|c0=c0|c1=c0   (se arma el dual-mono)
  3. y SOLO ENTONCES medir y normalizar

Con ese orden una sola pasada ya daria bien; se dejan las dos por seguridad.

## La rejilla sale de la voz, no de la formula

La formula sirve para presupuestar, no para montar. El procedimiento real:

1. Generar la voz.
2. `silencedetect` sobre cada pista (noise=-34dB, d=0.30).
3. Separar las pausas de parrafo de las intra-frase CONTRASTANDO cada candidata
   contra el conteo de caracteres de su frase, a ~1.55 cuadros por caracter. Las
   que cuadran son fronteras; el resto son comas.
4. Re-renderizar cada carton de pregunta a la duracion medida de SU pregunta.
5. Re-ajustar cada plano a su ranura nueva.
6. Volver a hornear la cama de musica contra los tramos medidos.

Entre el bloque de narracion y el de preguntas van 36 cuadros de respiro, y el
ultimo plano del tramo se extiende sobre ellos para que V1 no tenga corte.

## ajustar_planos.py y el modo loop_congela

`herramientas/montaje/ajustar_planos.py` tiene tres modos: hold, loop (ventana a
velocidad nativa, el default) y **loop_congela**: el loop entero a velocidad
nativa y despues su ultimo cuadro quieto hasta completar la ranura. Es para
cuando la ranura es mas larga que el loop Y EL GESTO YA TERMINO; arrastrar el
movimiento a 1.7x se ve mucho peor que dejarlo reposar.

## A3 en estas tres lineas es PREGUNTAS

La plantilla de la serie llama A3 "FACILITADOR". En las lineas "a la voz" se
renombro a PREGUNTAS, que es lo que lleva. A4 sigue vacia.

## El orden nuevo: la voz va PRIMERO

Desde el Caso 07 el caso se construye asi, y en este orden:

1. Escribir los dos textos de voz (narracion y preguntas) desde el guion.
2. Generarlos en ElevenLabs y masterizarlos.
3. Medir los silencios y derivar la rejilla: cuantos planos, cuanto dura cada
   uno, cuanto dura cada carton de pregunta.
4. SOLO ENTONCES pedir las imagenes, ya sabiendo la duracion de cada ranura.
5. Loops, cartones a la duracion medida, musica, linea.

Asi no hay que re-renderizar nada: antes se hacia al reves y toco rehacer 22
cartones y 38 planos de los tres primeros casos.

## Un negativo generico no basta contra la sonrisa ni contra el bokeh

El KF08 del Caso 07 salio sonriendo a camara y con discos de bokeh, con las dos
cosas ya bloqueadas en el negativo. Lo que si funciono fue decirlo en POSITIVO
dentro del parrafo del plano: "su boca es una linea recta, ni una sonrisa leve,
las comisuras no suben" y "no hay discos de bokeh, ni orbes, ni circulos de
desenfoque, ni en las esquinas ni en ningun lado". Es la regla 8 otra vez: lo
que importa se repite donde importa.

## El pool tenia dos arboles con numeracion distinta

Dentro de `CURSO 4 - TERMINACIONES ANTICIPADAS` convivian un arbol viejo
`UNIDAD 4 / LECCION 4.x / CASO 01..09`, con la numeracion del documento del
profesor, y un arbol plano `CASO 01..08` con la numeracion definitiva de la
seleccion de ocho. Las timelines terminadas estaban en el viejo, dentro de un
«CASO 01» que no es el caso 01. Si el usuario dice que no encuentra una timeline
o que abre la equivocada, lo primero es mirar si hay dos arboles, no asumir que
se perdio.

Ahora: las ocho carpetas de caso viven bajo `UNIDAD 1 - ARCHIVO DE LA
INDAGACION` (06, 07, 08) o `UNIDAD 4 - PREACUERDOS Y NEGOCIACIONES` (01 a 05),
en disco y en el pool, con el mismo nombre en los dos lados. El numero del caso
no cambia al entrar en su unidad.

## La timeline definitiva de cada caso va en `09 TIMELINE SEBASTIAN`

Una carpeta por caso, con una sola timeline dentro: la buena. En disco la misma
carpeta lleva el `.drt` exportado y un `LEER - esta es la buena.txt`. Cualquier
version anterior va a `_ARCHIVO versiones sin voz` con ese prefijo en el nombre.
Renombrar con prefijo no basta cuando los nombres se parecen; lo que resuelve es
que haya un solo sitio donde buscar.

## `Folder.SetName` existe pero no se puede llamar

En Studio 20.0.0b.47, `hasattr(folder, 'SetName')` da True y llamarlo lanza
`TypeError: 'NoneType' object is not callable`. No hay forma de renombrar una
carpeta del pool por API. Para apartar una carpeta hay que crear la nueva y
`MoveFolders([vieja], nueva)`. `MoveFolders` y `MoveClips` si funcionan.

## Mover carpetas en disco rompe los enlaces, y `RelinkClips` los arregla

`mp.RelinkClips(clips, ruta_de_carpeta)` busca **recursivamente** dentro de la
ruta que se le pasa, asi que basta darle la raiz del caso: encuentra los
`01 PLANOS`, `07 MOVIMIENTO` y demas por su cuenta. Una llamada por caso, 240
clips en cuatro llamadas, 0 sin resolver. Verificar despues recorriendo las
timelines con `GetMediaPoolItem().GetClipProperty('File Path')` y
`os.path.exists`, no fiarse del True que devuelve.

## Kling no deja a nadie quieto si la toma dura diez segundos

El KF06 y el KF09 del Caso 01 son la misma camara de seguridad y tenian que
mostrar, uno, a un hombre identificable y, el otro, a una figura que se ve pero
no se identifica. Las dos veces Kling resolvio la situacion: en el A el hombre
camina y termina de espaldas hacia el cuadro 120; en el B la figura se va del
pasillo y la pantalla queda vacia, igual que el escenario 3. Se repitieron con
«no camina, se queda exactamente donde esta, del mismo tamaño del primer cuadro
al ultimo, nunca de espaldas» escrito tres veces, y volvio a hacer lo mismo.

La salida no fue un tercer intento: fue dejarlos como **still**. Una grabacion de
camara de seguridad congelada se lee bien, y el plano que si tiene loop en esa
serie de tres es casi estatico de todos modos, asi que los tres monitores se leen
igual. Antes de gastar un tercer loop de 280 creditos en un plano donde la
persona tiene que quedarse quieta, considerar el hold.

## El ducking se calcula solo contra la narracion

En la cama del Caso 01 se pasaron a `cama_musica.py` los DOS tramos de voz
-narracion y preguntas- como tramos a agachar, y el bloque de preguntas salio en
-31 LUFS cuando tiene que estar en -26. La serie agacha la musica bajo la
narracion y la deja arriba bajo las preguntas. En el JSON va un solo tramo.
Verificar siempre por regiones, nunca por el integrado.

## El plano gemelo se pide con el primero como referencia

Cuando dos planos tienen que leerse como el mismo sitio en dos momentos -el KF03
y el KF15 del Caso 01, o las tres camaras de seguridad- el segundo NO se pide con
un prompt nuevo. Se pide con el primero en `references` tipo `image` y un prompt
que empieza diciendo que se conserven camara, encuadre, muebles, luz y personajes,
y que solo cambia tal cosa. Con prompt nuevo salen dos bodegas distintas.

## Mirada y gesto se bloquean en positivo, dentro del parrafo del plano

Dos fallos del Caso 01, los dos contra cosas que el negativo ya prohibia. El KF01
miraba a camara pese a «nobody looks at the camera»; lo que sirvio fue describir
la mirada por sus efectos: «la cabeza inclinada unos veinte grados, las pupilas
abajo en los ojos, se ve casi todo el parpado superior, la linea de la mirada cae
dentro de la caja». El KF14 salio caricatura de chismoso pese a tenerlo prohibido;
sirvio «la espalda recta, la cintura sin doblar, las dos manos colgando a los
lados, la boca apenas abierta, la separacion entre los labios no mas gruesa que un
lapiz». Es la regla 9 aplicada a las personas, no solo a los objetos.

## El carton tiene que estar completo mientras se dicen las palabras

Era el fallo mas repetido de la serie y estaba en la animacion. El texto tardaba
35 cuadros en terminar de entrar -arranque en el 6, 14 de fundido, escalonado 3
por linea- y empezaba a irse 20 cuadros antes del final, tambien escalonado. Como
cada carton dura exactamente lo que dura su frase, se comia segundo y medio por
delante y casi uno por detras: el texto se iba mientras todavia se oian las
ultimas palabras.

Ahora: entrada en 15 cuadros (arranque 2, fundido 8, escalon 1) y salida de 7 sin
escalonar. Y sobre todo, **el carton se renderiza con `tramo + CABEZA + COLA` y
se coloca CABEZA cuadros ANTES de que empiece la frase** (15 y 7). Asi las dos
animaciones caen fuera de las palabras. Verificado midiendo la opacidad cuadro a
cuadro: completo del 14 al 150 en un carton de 157.

## El tinte va aparte, no viaja con cada carton

Al crecer, los cartones del bloque de preguntas se solapan 22 cuadros. Si cada
uno trae su propio tinte al 46 %, en el solape se apilan dos capas y el azul
salta a **71 %**: un parpadeo oscuro entre pregunta y pregunta, ocho veces por
pieza. Medido: 0,459 -> 0,707 de alfa.

La solucion es un panel de tinte sostenido -`render_tinte()`- que entra una vez,
dura todo el bloque y sale una vez, con los cartones de texto SIN tinte encima.
Los de narracion van sueltos y si conservan el suyo.

Mapa de pistas nuevo de la serie:
    V1 VIDEO · V2 TINTE · V3 CARTONES · V4 CARTONES 2
    V5 MARCA DE AGUA · V6 EFECTOS · V7 LOWER THIRD
El texto necesita dos pistas porque se solapa. El tinte va DEBAJO del texto.

## El escalon de volumen no era la voz

Sebastian oyo un salto brusco entre la voz del narrador y la de las preguntas.
Medidas las diez pistas por ventanas de 8 s -este build de ffmpeg no imprime el
short-term por cuadro, hay que medir el integrado por ventanas- las dos voces de
cada caso quedan dentro de 1 LU. El salto era la cama: -31,6 bajo la narracion y
-26,0 bajo las preguntas, 5,6 dB de subida en el cuadro donde cambia de locutor.
La voz no se mueve pero pierde ese aire de golpe.

El bloque de preguntas se habia pensado sin voz y entro como «hueco». Ahora
`cama_musica.py` acepta una profundidad por tramo: -6 dB bajo narracion, -3 bajo
preguntas, 0 en los huecos.

## Un plano de detalle sale mas barato que repetir un loop

Idea de Sebastian y queda como metodo. Cuando Kling arruina el final de un loop
-una figura que se va, algo que se cierra solo- en vez de pedir el loop otra vez
por 280 creditos se corta a un plano de detalle del mismo sitio: una imagen de
100 y, si se quiere, un loop corto. Ademas suma, porque el detalle agrega
material en vez de reemplazarlo. El Caso 06 estrena el BR04 de la vitrina
abierta, que tapa los 60 cuadros donde el KF01 pierde a la figura.

## Un still tambien pide movimiento

Los planos que quedaron como `_hold` se notan muertos al lado de los que tienen
loop. Cuando se pidan los loops de un caso, se piden TODOS los planos, incluidos
los que uno daria por estaticos.

## `timeline.SetName()` si funciona

Al reves que `folder.SetName()`, que existe pero no se puede llamar. Para dejar
sitio a una version nueva con el mismo nombre, se renombra la vieja y listo.

## Correccion: alargar el carton y solaparlo NO sirve

Quedo escrito mas arriba que los cartones se renderizan con margen y se solapan
22 cuadros en dos pistas. Se probo y esta mal: el carton que sale se queda a
opacidad plena durante 15 de los 22 cuadros del solape, asi que durante medio
segundo se ven DOS textos completos encima del otro. Un texto sobre otro no se
lee como disolvencia, se lee como error, y Sebastian lo vio de inmediato.

Lo correcto: los cartones van PEGADOS, uno por pista, cada uno exactamente lo
que dura su frase, y lo que se acorta es la animacion. Con entrada de 11 cuadros
y salida de 5 quedan 16 cuadros muertos por carton -medio segundo escaso- contra
los 55 de la version original. Cero solape.

La leccion general: cuando dos elementos del mismo tipo tienen que turnarse en
el mismo sitio de la pantalla y no hay hueco entre ellos, no se busca espacio
alargandolos; se acorta la transicion.

Lo que si se queda del intento anterior es separar el tinte: ese arreglo es
independiente y resuelve un problema real.

## Un video se siente hueco cuando la primera mitad no tiene cartones

El Caso 01 tenia tres cartones de narracion y los tres caian en la segunda
mitad: los primeros cincuenta segundos iban sin un solo carton. Sebastian lo
describio como «vacio» y tenia razon. Subieron a nueve, cinco de ellos en la
primera mitad, y el hecho se va fijando en pantalla a medida que se cuenta.

Regla: en la narracion, un carton cada 300 o 400 cuadros, con texto literal del
guion -nombres, cifras, la frase que define el giro-. Tres por pieza es poco.

## Un plano de 267 cuadros donde no pasa nada se parte

No se arregla pidiendo mas movimiento: se corta y entra un plano de detalle del
mismo sitio. El KF02 del Caso 01 paso de 267 a 159 cuadros y los 108 restantes
se los lleva la franja de luz en el piso.

## Kling alucina objetos y levanta manos cuando le sobran segundos

En el KF04 del Caso 01 la mano se despegaba de la mesa y aparecian unas gafas y
un lapiz que no estaban en la imagen; en el KF10 la puerta se abria sola al
final. En los dos la ventana util eran los primeros segundos.

El remedio no es volver a pedir el loop: se recorta a la ventana buena con
ffmpeg -un `-frames:v N` y listo- y se completa la ranura con `loop_congela`.
Sale gratis y es mas predecible que una segunda tirada.

## Describir las manos en el prompt, no solo la accion

El KF04 original traia una manga sin mano delante de la mano principal. Lo que
lo arreglo fue decirlo como cuenta: «hay exactamente UN brazo en el cuadro»,
«no hay manga ni tela que no tenga una mano visible». Lo mismo con los papeles:
«todo el papel esta plano sobre la mesa, nada flota».

## Si un concepto no se lee, el problema es el encuadre, no el prompt

El KF10 pedia «varios empleados autorizados» y se habia resuelto con tres manos
convergiendo sobre el lector: ilegible. Con tres personas en fila ante la misma
puerta, cada una a distinta distancia, se entiende en un cuadro. Cuando algo no
se lee, cambiar la puesta en escena antes que afinar el texto.
