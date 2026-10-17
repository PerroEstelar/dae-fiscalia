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

## Recortar el loop sale gratis y hay que hacerlo por defecto

En el Caso 04, tres de los ocho loops se fueron de rango: dos levantaban una
hoja a mitad del clip y el tercero empezaba a sonreir hacia el cuadro 60.
Ninguno se volvio a pedir. Se recortan a la ventana util con
`ffmpeg -i loop.mp4 -frames:v N util.mp4` y la ranura se completa con
`loop_congela`. Tres loops salvados, cero creditos.

Conviene revisar la tira de cinco cuadros ANTES de cortar, siempre, y asumir
que de cada ocho loops dos o tres van a necesitar recorte. No es un fallo del
prompt: es que Kling, con diez segundos por delante, inventa algo.

## La rejilla sale de la proporción de caracteres, no de contar silencios

`silencedetect` da los tramos de voz, pero el locutor no hace una pausa en cada
frase: un tramo puede llevar tres frases y una frase puede partirse en dos
tramos. Lo que sí se cumple con precisión es que **el tiempo hablado es
proporcional a los caracteres**. Medido en las ocho piezas: 1,2 a 1,4 cuadros
por carácter, y constante dentro de una misma locución.

`herramientas/rejilla/calzar.py` acumula caracteres y acumula cuadros hablados y
corta cada frase donde coinciden. Devuelve «esta frase va del cuadro A al B», y
de ahí salen a la vez la rejilla de planos y la de cartones. Con 4.811 cuadros
de narración —el Caso 03— hacerlo a ojo no es viable.

Lo único que hay que corregir a mano es la primera frase: el mapa la hace
empezar dentro del «Veamos un ejemplo…», y hay que empujarla al arranque del
tramo siguiente.

## Densidad de cartones: 60–70 % en las piezas largas

En el Caso 07 (59 s de narración) se cubrió el 86 % del tiempo y queda demasiado
lleno: la imagen no respira nunca. En el 03 y el 05, que son de tres y cuatro
minutos, se bajó a 60–65 % y ahí funciona. La regla: un cartón por cada momento
que el profesor subraya, no un cartón por frase.

## El modo `loop` estira, y en un plano que solo respira eso no se nota

`ajustar_planos.py` en modo `loop` hace `setpts` cuando la ranura es más larga
que el clip. Con el movimiento que pide esta serie —respiración y poco más—
estirar 2x es invisible. Eso cambia la economía: la ventana útil de un loop
puede ser de 100 cuadros y aun así servir para una ranura de 240. No hay que
regenerar por falta de metraje.

## Cuándo sí hay que volver a pedir el loop

Recortar resuelve casi todo. Las dos excepciones medidas:
- **Aparece un objeto nuevo** que no estaba en la placa (unas gafas flotando en
  el borde superior del KF03 del Caso 05, desde el cuadro 60).
- **Se borra gente** (el KF12 del Caso 03: a los cinco segundos sale humo de la
  mano y al final no queda nadie en el cuadro).
En los dos casos la ventana útil quedaba por debajo de 60 cuadros, y ahí sí sale
más barato pagar los 280 créditos que inventarse el plano.

El prompt que lo arregló dice lo prohibido por su nombre y por su sitio: «NO new
object of any kind ever appears anywhere in the image — not at the top edge, not
at the sides, not on the desk. No glasses, no pen, no cup».

## Trampas de la API de Resolve encontradas en esta tanda

- `project.ExportTimeline` **no existe**. Es `timeline.Export(ruta, resolve.EXPORT_DRT)`.
- `mp.CreateEmptyTimeline(nombre)` + `SetStartTimecode('01:00:00:00')` + `AddTrack`
  da la línea canónica desde cero, y es el camino bueno cuando no hay nada hecho
  a mano que preservar.
- **No se puede insertar una pista en medio.** Si la línea vieja tiene trabajo de
  Fusion en V3/V4 —como el lower third del Caso 07— hay que duplicarla y parchear
  dentro, y los CARTONES terminan en V6 en vez de V3. Se documenta en el LEER y
  listo: es peor borrarle el trabajo.
- Al reimportar con nombres repetidos, filtrar el pool por `File Path`: después
  de archivar una versión vieja quedan dos ítems con el mismo nombre y
  `pool.setdefault` se queda con el equivocado.

## Dos cosas del puente

- `device_commit_files` solo acepta rutas bajo `/mnt/user-data/outputs/`. Un
  archivo del directorio de trabajo hay que copiarlo ahí primero.
- El contenedor **no puede descargar de `pikaso.cdnpk.net`** (el proxy devuelve
  403). Todo lo que sale de Magnific se baja con `urllib` corriendo en la máquina
  de Sebastian, que además es donde tiene que quedar.
- Las voces nuevas salen con el nombre del texto (`TA0x_NARRACION.mp3`) y la
  serie las llama `NARRADOR`. Renombrar antes de importar.

## La vacilación del loop está al principio, no al final

Hasta aquí la regla era «lo que alucina es la cola: se recorta el final». El
Caso 08 mostró la mitad que faltaba. **Cuando la placa tiene una mano a punto de
alcanzar algo, el modelo vacila al principio**: se queda congelado en el gesto
de alcanzar y después la mano va y viene. Se lee como falso al instante. Hacia
el cuadro 60 o 70 el movimiento ya se asentó y se vuelve consistente.

Lo encontró Sebastian comparando dos ventanas del mismo loop. El KF06 del Caso
08 sale dos veces: `TA08_KF06_v149` con `inicio: 0` —vacila— y
`TA08_KF06_v171` con `inicio: 70` —«acts way better», en sus palabras—. Su
arreglo fue quedarse con la ventana buena y estirarla.

Dos consecuencias, una por etapa:

- **En el montaje.** Si el plano tiene una mano acercándose a un objeto, la
  ventana útil empieza en 60–70, no en 0: `"inicio": 60` en el manifiesto, y se
  estira para llenar la ranura. Como el movimiento es solo respiración, estirar
  no se nota. La regla vieja —recortar la cola— sigue valiendo; ahora hay que
  recortar por los dos lados.

- **En el prompt.** No se pone a nadie **a punto de** tocar algo. O la mano ya
  está apoyada sobre el objeto, o está claramente lejos de él. El «a punto de»
  es exactamente la pose que el modelo intenta completar y después deshace.

  Esto matiza el movimiento 3 del método de prompts, «el gesto único a media
  acción». La media acción vale para el fotograma fijo, pero si ese plano se va
  a animar, la media acción tiene que ser una que **no pida completarse**: un
  peso apoyado, una mirada, una tela a medio caer, un pie que todavía no
  aterriza. Una mano en camino hacia un objeto sí pide completarse, y el modelo
  la completa y la devuelve.

El mismo mecanismo explica el KF04 del Caso 09 —un niño a media zancada— y el
KF11 del Caso 05, donde cuatro manos quedaban cortas de dos objetos. Es la misma
pose, en manos y en piernas.

## El puente a Google Drive

La carpeta de entregas vive en el Drive de `adminproyectos@jpsolucionesdigitales.com`
y está compartida con Sebastian, así que **Drive para escritorio no la
sincroniza**: solo sincroniza «Mi unidad» y las unidades compartidas.

El camino que sí funciona, y que no necesita que él haga nada:

1. Se copia el render a una carpeta dentro de `G:\My Drive\`, que sí sincroniza.
2. Drive lo sube solo. Se espera buscándolo por título con el conector.
3. Se mueve con `update_file(fileId, parentId=<carpeta de la unidad>)`. El
   archivo sigue siendo de Sebastian, igual que cuando él los arrastra, y
   desaparece solo de la carpeta local porque ya no está en «Mi unidad».

El conector de Drive **no sirve para subir** estos archivos: `create_file` solo
recibe el contenido incrustado en la llamada y los renders pesan de 50 a 190 MB.

## Los ajustes de render de la serie

QuickTime `.mov`, H.264 **High**, 1920×1080, 23,976, tope de **6.000 kb/s** de
video, audio AAC 48 kHz estéreo. Medidos sobre los exports que hizo él a mano.

```python
pr.LoadRenderPreset('H.264 Master')
pr.SetCurrentRenderFormatAndCodec('mov', 'H264')
pr.SetRenderSettings({
    'TargetDir': destino, 'CustomName': nombre,
    'FormatWidth': 1920, 'FormatHeight': 1080, 'FrameRate': 23.976,
    'VideoQuality': 6000,        # tope en kb/s, el codificador va en VBR debajo
    'EncodingProfile': 'High',   # sin esta clave sale Main
    'AudioCodec': 'aac', 'AudioSampleRate': 48000,
    'ExportVideo': True, 'ExportAudio': True, 'SelectAllFrames': True,
})
```

Dos cosas que hubo que medir, porque no están documentadas:

- **Sin `EncodingProfile: 'High'` sale perfil Main.** El preset «H.264 Master»
  no lo fija y la clave no da error si falta: simplemente baja el perfil. El
  primer render del Caso 08 salió Main y hubo que repetirlo.
- **`VideoQuality` es un tope, no un caudal fijo.** Probado con dos renders de
  241 cuadros de la misma línea: con 6000 el archivo salió a 3,13 Mb/s y con
  20000 a 8,12 Mb/s. O sea que el codificador va en VBR por debajo del tope. Los
  exports de Sebastian marcan 6.000.578 b/s clavados, que es CBR de la interfaz;
  el render por API da el mismo techo con archivos más chicos y sin pérdida
  visible. El Caso 08 completo: 2.032 cuadros, 84,757 s, 38,3 MB a 3,6 Mb/s.

Nombre de archivo: `TA - U1 - CASO 08 - V1.mov` — `TA - U{unidad} - CASO {NN} - V{n}`.

## El guion de entrega

`herramientas/entrega/exportar_y_subir.py` junta las tres cosas: renderiza con
los ajustes de arriba, verifica el archivo con ffprobe contra el patrón de la
serie (códec, perfil, tamaño, cadencia, audio y número de cuadros contra el
largo de la línea) y solo entonces lo copia a la carpeta de paso del Drive. Si
la verificación falla no sube nada.

`entregar(resolve, timeline, unidad, caso, destino)` devuelve el informe. Lo
único que queda por fuera es el `update_file` que mueve el archivo a la carpeta
compartida, porque eso va por el conector y no por la máquina.

Borrar el archivo anterior antes de renderizar: si el render falla a medias,
ffprobe mide el viejo y todo parece bien.

## Medir la vacilación: cómo se hace y qué NO es

La primera versión del detector promediaba el cuadro entero y daba «limpio»
sobre el propio KF06 del Caso 08, que es el caso conocido. El defecto es
**local** —una mano, un brazo— y en un promedio de 1920×1080 desaparece.

`herramientas/montaje/vacilacion.py` mide por bloques: parte el cuadro en una
rejilla de 8×6, busca el bloque que más se aleja del cuadro 0 en los primeros
45 cuadros, y mira **su** curva. La firma, medida sobre el KF06:

```
cuadro   0   5  10  15  20  25  30  40  60  90 120
dist   0.0 10.0 24.4 26.5 24.4 17.8 16.6 16.5 18.9 17.2 17.0
         \________ sube ________/\__ se deshace __/\___ se queda abajo ___/
```

Sube a 26,5 en quince cuadros, se deshace un 37 % y después se queda plana cien
cuadros. Lo último es lo que la separa de un loop cíclico, que también sube y
baja pero **vuelve** al mismo sitio. Umbrales: pico ≥ 12, caída ≥ 25 %, y que no
regrese al 85 % del pico en los 70 cuadros siguientes.

**Tres cosas que el detector marca y no son el defecto.** Hay que mirar las
tiras de contacto antes de cortar nada:

- **Una cara que habla.** La boca se abre y se cierra: sube y vuelve. El KF10
  del Caso 05 es Laura hablando, y marcó 82 %.
- **Gente que cruza el fondo.** Entran y salen del bloque. El KF01 del Caso 09.
- **Una mano que está congelada en TODOS los cuadros.** Ahí el problema está en
  la placa, no en la ventana: mover el `inicio` no arregla nada. El KF02 del
  Caso 05 tiene una mano en primer plano tendida hacia la carpeta que nunca la
  toma, en los 241 cuadros.

De 38 loops de los casos 02, 03, 05 y 09, uno solo tenía el defecto de verdad:
el **KF07 del Caso 05**, la mano que se acerca a la hoja. Se recortó la ventana
50-148 (`TA05_KF07_util2.mp4`): empieza con la mano ya apoyada, desliza la hoja
y se retira al montón. Un gesto entero, sin el titubeo de la entrada.

La conclusión es la que vale para la próxima: **no se adivina por el texto del
prompt qué plano vacila.** Los cuatro que yo había señalado leyendo las
descripciones —KF10 del 03, KF08 y KF11 del 05, KF02 del 09— salieron limpios.
Se mide y se mira.

## El encuadre es colombiano, y hay que decirlo en el prompt

La serie es para la Dirección de Altos Estudios de la Fiscalía General de la
Nación y la ve público colombiano. Si el prompt dice solo «a grey street of low
buildings», Seedream rellena el hueco con un pueblo inglés: casas pareadas de
ladrillo con techo a dos aguas, chimeneas, setos, antejardines, adoquines.
Pasó con el KF03 y el KF04 del Caso 09 y lo cazó Sebastian de inmediato.

El bloque que sí funciona, para pegar en cualquier exterior:

> SETTING — this is a residential street in a Colombian city, and the
> architecture must say so unmistakably. Two and three storey houses built flush
> to the pavement with no front gardens and no hedges, in exposed clay brick and
> plain rendered concrete, with FLAT concrete roofs — never pitched roofs, never
> tiled roofs, never chimneys. Several houses have an unfinished top floor with
> short steel reinforcing bars standing up from the concrete slab. Every
> ground-floor window and door has a plain metal security grille. One corner shop
> with a roll-down metal shutter. Square concrete utility poles along the kerb
> carrying thick untidy bundles of black cables, with a street lamp on a bracket.
> The pavement is a raised concrete kerb with plain square concrete slabs. Small
> motorcycles parked up on the pavement. The parked cars are small hatchbacks and
> compact sedans. At the far end of the street, hazy mountains behind the rooftops.

Y al negativo: `no England, no English village, no British terraced houses, no
pebbledash, no pitched slate roof, no chimney stack, no sash windows, no front
garden, no hedge, no stone cottage, no cobblestones, no European number plates`.

Las señas que hacen el trabajo son seis: **ladrillo a la vista, cubierta plana
con varillas, rejas en todas las ventanas, poste de concreto con el nudo de
cables, andén elevado de losas, y motos parqueadas en el andén.** Con esas seis
la calle se lee de inmediato; sin ellas, el modelo se va a Inglaterra.

Un efecto secundario que hay que vigilar: el ladrillo sube el croma. El KF03
colombiano midió 0,070 de croma y +0,070 de calidez, contra un máximo de 0,056
en el resto del caso. Se baja en el grado, pero hay que medirlo.

**No todo estaba mal.** El KF01 y el KF02 del mismo caso, que no se tocaron,
salieron en una calle latinoamericana neutra y funcionan. El problema aparece
cuando el prompt deja el entorno sin describir.

---

## Kling no sostiene la cámara quieta en interiores con perspectiva (Caso 5A, oct 2026)

Medido, no supuesto. Tres planos del Caso 5A se mandaron a Kling con la misma
instrucción de cámara bloqueada, repetida hasta el ridículo en el prompt y en el
negativo ("locked-off tripod", "the framing at the last frame must be identical
to the framing at the first frame", "camera push in", "parallax", etc.):

| plano | composición | modelo | resultado |
|---|---|---|---|
| n15 hall de atención | frontal, plana, sin fuga marcada | kling-30 13 s | **cámara quieta**, estilo intacto, la figura lejana camina como se pidió |
| n16 sala de audiencias | perspectiva central, fuga profunda | kling-30 12 s | deriva lenta de empuje y retroceso; aceptable, no bloqueada |
| n07 apertura, plano alto | tres cuartos, fuga fuerte, mesa en diagonal | kling-30 10 s | **deriva clara** de encuadre y las caras se ablandan y oscurecen |
| n07, segundo intento | igual | kling-25 10 s | **la misma deriva**; no es cosa del modelo |

La regla que sale de ahí, y que vale para pedir movimiento en el resto de la serie:

> Kling sostiene el encuadre cuando la composición es frontal y plana. Cuando el
> plano tiene profundidad implícita —punto de fuga, mesa en diagonal, piso que se
> aleja— el modelo quiere mover la cámara y la mueve, se le pida o no. En esos
> planos no se pide movimiento generado: se hornea la cámara con el modo `camara`
> de `ajustar_planos.py`, que sí obedece.

El segundo intento costó 650 créditos y sirvió para descartar que fuera el modelo.
Queda escrito para no volver a pagarlo.

## El modo `camara` de ajustar_planos.py

Para los planos que no llevan video generado. El plano se genera a 2560 de ancho y
la línea es de 1920: ese 33% que sobra es el riel de la cámara, y la ventana nunca
baja de 1920 px de fuente, así que nunca se amplía un pixel.

Zoom lento (`encuadre` + `empuje`) más vibración de pulso de unos 2 px de salida,
armada con tres senos de frecuencias sin razón entera para que no se repita a la
vista. La vibración además resuelve el escalón de `zoompan`: los recortes se
redondean a entero y un paneo lento sin vibración salta cada cuatro o cinco
cuadros; con la vibración encima, x e y cambian en todos los cuadros y el escalón
se disuelve. Por eso la vibración no es un adorno, es parte del mecanismo.

Cuando un mismo plano cae en dos ranuras, se le cambia `encuadre`, el signo de
`empuje`, el `centro` y la `fase`: el mismo plano lee como otro plano.

---

## Por qué un pulso de cámara horneado se siente tieso (Caso 5A, oct 2026)

Sebastián vio el primer corte del 5A y dijo que la vibración se sentía rígida.
Medido, la causa no era el dibujo del movimiento sino la cuantización.

`zoompan` redondea la posición del recorte a entero. Sobre un plano de 2560 que
termina en una línea de 1920, **un pixel de fuente son 0.85 px de salida**. El
pulso viejo eran tres senos con la energía en 0.37, 0.61 y 1.27 Hz y 2 px de
excursión: el desplazamiento entre cuadro y cuadro daba 0.2 a 0.3 px, por debajo
del escalón. Resultado: la imagen se queda quieta cuatro cuadros y salta uno. Eso
no se lee como temblor, se lee como mecanismo.

Las dos correcciones, y las dos hacen falta:

1. **Una banda alta de verdad.** Tres bandas por eje: deriva 0.05–0.16 Hz (peso
   0.46), meceo 0.40–0.95 Hz (0.20), temblor 2.0–3.6 Hz (0.34). La banda alta es
   la que se olvida y es la que hace que cada cuadro sea distinto del anterior.
   Medido sobre seis ranuras: con el temblor en 0.34 se mueve más de medio pixel
   el 79% de los cuadros; con el temblor en 0.18, el 45%. Ese 45% es lo que se
   siente tieso.
2. **El plano se sube a x2 antes del recorte** y se cachea en `_x2/`. Un pixel de
   fuente pasa a ser 0.43 px de salida y el escalón desaparece. `zoompan` saca a
   2880x1620 y después un `scale` lanczos a 1920, para que el reescalado bueno
   quede al final.

Tercera cosa, menor pero real: **la señal se normaliza por su excursión real en la
ranura, no por la suma teórica de los pesos.** Con componentes lentas, una ranura
de cuatro segundos no alcanza a recorrer su máximo; sin normalizar, el pulso sale
a un tercio de lo pedido y las ranuras cortas quedan más quietas que las largas
sin que nadie lo haya decidido.

La lección general: **antes de rediseñar la forma de un movimiento, medir si el
movimiento llega a cruzar el pixel.** Un movimiento correcto por debajo de la
resolución del render se ve peor que uno tosco por encima de ella.

---

## Prohibir movimiento congela el plano (Caso 5A, oct 2026)

Corrección a la sección anterior. Yo había escrito que Kling deriva la cámara en
interiores con fuga, y lo había concluido mirando tiras de contactos. **Está mal.**

La prueba: restar el cuadro 3 contra los cuadros 40, 90, 140, 190 y 236 del clip
de la apertura. La resta sale negra — paredes, ventana, mesa, sillas y sombras
idénticas píxel a píxel. La cámara nunca se movió. Lo que yo leí como deriva era
mío.

Lo que sí pasaba, medido como porcentaje de píxeles que cambian en todo el clip:

| clip | prompt | se mueve |
|---|---|---|
| hall de atención | una acción concreta en positivo | **14.5%** |
| apertura | lleno de prohibiciones | 3.8% |
| sala de audiencias | lleno de prohibiciones | 0.5% |
| la misma apertura, prompt reescrito | pauta de acciones | **10.0%** |
| el mismo archivo, "camina todo el pasillo" | acción grande | **47.6%** |

Mis prompts decían «locked-off», «nobody reaches for anything», «hands stay
exactly where they are», «at most one slow blink», más veinte términos negativos.
El modelo obedeció y congeló la imagen. No era el modelo ni el `cameraMotion`.

> **Al modelo se le dice qué pasa, no qué no pasa.** El prompt de movimiento es
> una pauta de acciones concretas con destino: «levanta la hoja, la lee, la baja y
> la deja sobre la mesa», «camina todo el pasillo hacia la cámara y sale de
> cuadro». Los negativos se reservan para el estilo —textura, contornos, cambio de
> paleta, caras que se deforman— y nunca para apagar movimiento. La cámara queda
> quieta igual: basta «tripod shot, the camera stays where it is» una vez.

La regla que sí sobrevive, y que resuelve el defecto original del Caso 05 (manos
que se acercan a algo y se quedan colgadas): **todo movimiento llega a destino.**
Se escribe en positivo, al final del prompt: «every movement travels all the way
and arrives; nothing stops halfway», y cada acción se redacta con su final — la
hoja se levanta, se lee *y se deja*; la mano agarra *y se lleva* el lapicero.

Lo que no conviene pedirle: **una mano sola entrando a cuadro**. En el plano
cenital del expediente salió flotando y con los dedos mal, que es literalmente el
defecto que Sebastián marcó en el 05 («es solo una mano, sin cuerpo»). Ese plano
se quedó como imagen fija con el modo `camara`.

Costos de referencia, 1080p: Kling 3.0 son 90 créditos por segundo; Seedance 2.0
Fast 720p son 235; Seedance 2.5 Pro 1080p son 790. Kling alcanza de sobra cuando
el prompt está bien escrito.

## Las tildes no son un detalle de codificacion

En el U5C1 escribi los textos de los cartones en ASCII puro -«Votacion»,
«dieciseis», «Si», sin signo de apertura- por la costumbre de esquivar
problemas de codificacion al pasar texto entre la maquina y el contenedor. Se
renderizaron asi y llegaron a la linea de tiempo asi. El render nunca tuvo el
problema: `cartones_ta.py` lleva tildes desde el caso 01 -«Andrés»,
«intervención», «años»- y las fuentes Montserrat las traen todas.

**La regla.** El texto que se ve o se oye es castellano institucional de la
Fiscalia y se escribe completo: tildes, ñ, ¿ y ¡. No hay ningun archivo de
esta serie que se escriba sin tildes -ni los cartones ni el texto de TTS-. Si
algo falla al cruzar el puente, se arregla la codificacion, no el castellano.

## El repartidor de lineas: saltos explicitos y sangria francesa

`partir()` hacia `texto.split()`, que se come los saltos de linea. Las tres
opciones de una votacion -a), b), c)- salian corridas como un parrafo unico y
se leian como una sola frase larga.

Ahora `partir()` corta en cada `\n` del texto y, si un parrafo abre con una
marca de lista (`a)`, `b)`, `1.`, `-`), sangra las lineas de continuacion el
ancho de esa marca. Devuelve pares `(linea, sangria)` y la sangria viaja como
quinto campo de cada linea hasta el `d.text()`. Un texto sin `\n` y sin marca
de lista se reparte exactamente igual que antes.

## Cartones de pausa: son transparentes, necesitan lecho

Los cartones de narracion y de pausa se renderizan con alfa y con su propio
tinte (`con_tinte=True`). **No son pantallas completas**: si se ponen en V1
sobre nada, el fondo sale negro. Van en V3 y debajo tiene que seguir corriendo
un plano.

Para el U5C1 eso significo hornear una ranura mas -la 28- de 384 cuadros desde
la misma placa del plano final, con el retroceso de camara continuado
(`encuadre` 0,78, `empuje` -0,03, `fase` 22,0 donde la 27 terminaba en 0,82 /
-0,055 / 15,6). El lecho corre 3878-4262 y encima van la votacion y la tarea
del foro. Es la misma forma que tiene el bloque de preguntas del caso 5A, donde
el plano final se sostiene bajo los tres cartones.

## Donde ponen las pausas y donde no

La primera reparticion metia la votacion entre las ranuras 24 y 25, y para eso
habia partido la locucion en `_a` y `_b`. Partia tambien la enumeracion: los
cartones «Uno» y «Dos» quedaban antes de la votacion y «Tres» despues. Los dos
cartones de pausa van al final, despues de la locucion completa, que es como
quedo la serie. La locucion entra entera y sin cortar.

## El numero que mide «entrecortado» son los cambios de direccion

En el caso 5A el pulso se sentia tieso y le meti una banda de 2 a 3,6 Hz. En el
U5C1, Sebastian dijo que ahora se veia entrecortado, y tenia razon. Medido sobre
la misma ranura:

    cambios de direccion por segundo   4,1
    desplazamiento por cuadro          0,34 px de media, 1,22 de pico

Una camara en mano de verdad hace **alrededor de un cambio de direccion por
segundo**. La amplitud no es el numero que importa: se puede bajar el pulso a la
mitad y sigue viendose entrecortado si la senal cambia de signo cuatro veces por
segundo. Lo que el ojo lee como temblor de camara es la frecuencia, no el
tamano.

**Y una banda rapida con poco peso igual manda en la derivada.** A 1,2 Hz cada
unidad de amplitud mueve diez veces mas por cuadro que a 0,12 Hz: bajarle el
peso no la arregla, hay que quitarla.

## La banda rapida era un parche de un problema que no era de la senal

La habia puesto porque sin ella el movimiento quedaba en 0,09 px por cuadro y se
congelaba. Pero eso no era culpa del pulso: `zoompan` redondea el recorte a
pixel entero de la fuente, y sobre la placa x2 un pixel de fuente son 0,44 px de
salida. Todo lo mas lento que eso se queda quieto varios cuadros y despues
salta.

La salida no era elegir entre tieso y entrecortado: era quitarle el escalon al
recorte. `herramientas/montaje/camara.py` hace el recorte con
`PIL.Image.resize(box=...)`, que acepta coordenadas con decimales y filtra en
Lanczos. Sin escalon, el pulso vuelve a ser lento:

    cambios de direccion por segundo   0,4 a 1,2
    desplazamiento por cuadro          0,04 px de media, 0,12 de pico
    cuadros congelados                 ninguno

Y de paso la imagen quedo 4% mas nitida (laplaciano medio 4,56 contra 4,39),
porque ahora es **un solo remuestreo y no dos**: ya no hace falta la placa x2.

El pulso ahora es ruido blanco filtrado -dos bandas, 0,12 y 0,40 Hz, tres polos
cada una, pesos 0,70 y 0,30-, no una pila de senos: no tiene periodo que el ojo
pueda agarrar. `vibra` por defecto bajo de 6,0 a 5,0 px.

**La leccion general.** Cuando un movimiento se ve mal, medir primero si el
problema esta en la senal o en el muestreo. En el 5A diagnostique la senal y
puse un parche; el defecto estaba un piso mas abajo, y el parche se volvio el
defecto siguiente.

## AppendToTimeline: `endFrame` es EXCLUSIVO. Y una comprobacion que no sirve

Arme la linea del U5C1 pasando `endFrame: duracion-1`. `endFrame` es exclusivo,
asi que cada clip entro **un cuadro corto**. Como ademas iba un `recordFrame`
explicito por clip, el cuadro que faltaba no corrio el montaje: dejo un hueco.
**Treinta y un cuadros negros, uno entre cada par de clips.** Los vio Sebastian,
no yo.

Medido en la linea:

    intro          duracion 193   el archivo tiene 194
    r01            duracion 174   el archivo tiene 175
    ...y asi los 32

Comprobado aparte, con dos apendizados del mismo clip de 175 cuadros:
`endFrame 174` da 174, `endFrame 175` da 175. **Va la duracion entera.**

**Lo grave no es el off-by-one, es la verificacion.** Despues de armar corri un
chequeo de huecos que decia «problemas: ninguno». Lo decia porque calculaba el
final de cada clip con `GetEnd()` y lo comparaba con el arranque del siguiente,
y `GetEnd()` devuelve el ultimo cuadro del clip tal como quedo puesto. Si el
clip entro corto, su final tambien esta corrido, y los dos numeros cuadran con
el hueco en medio. **La comprobacion estaba hecha con la misma creencia que el
error, asi que lo confirmo en vez de encontrarlo.**

**La regla.** Una linea de tiempo se verifica contra algo que no salio de la
misma aritmetica que la armo: la duracion de cada clip contra el numero de
cuadros del archivo en disco, medido con ffprobe, y la suma contra el total
previsto. Si los dos lados del chequeo vienen de mi, el chequeo no es un
chequeo.

    V1 32 clips | suma 4575 | fin 4575
    contra los archivos en disco: todo cuadra

**Y un detalle del append:** un clip con video y audio **no entra en V1 cuando
`recordFrame` es el primer cuadro de la linea** — solo aterriza su audio, y el
video se va al final o se pierde. Con `mediaType: 1` entra bien. El audio del
bumper se pone aparte, con `mediaType: 2`.

## Dos numeros separan «se ve distinto» de «hay que rehacerlo»

Sebastian dijo que el KF01 estaba «muy lejos en estilo» del plano hero. Medido
sobre las placas bajadas a 640x360, en gris:

    estructura de valores   p2 / p50 / p98 del histograma, y que porcentaje
                            cae bajo 60 y sobre 200
    dureza de borde         media del FIND_EDGES de PIL

    kf08_noche (hero)   23 / 45 / 181   69,3% bajo 60   0,0% sobre 200   5,63
    kf01_avenida        79 /199 / 241    0,2% bajo 60  48,7% sobre 200  15,67

Tres veces la energia de borde y ni un uno por ciento de la imagen por debajo de
60. El resto del conjunto vive entre 4,5 y 7,2 de dureza: los que se salen son
kf01 (15,67), kf02_grupo (14,88), kf02b_banda (13,81) y kf07_archivo (13,55).

**Las dos cosas se arreglan distinto y conviene saber cual es cual antes de
gastar.** Probe una correccion de color sobre el KF01 -curva que baja la clave,
contraste, un pelo de desenfoque-:

    kf01 original   79 /199 / 241    0,2% bajo 60   dureza 15,67
    kf01 gradeado   20 /164 / 221   11,5% bajo 60   dureza 15,94

La estructura de valores se arregla sola con la curva. **La dureza de borde no se
movio.** Eso es lo que hace que una placa se lea como render 3D y no como cuadro
pintado, y no hay grade que lo quite: hay que regenerar.

**La regla.** Antes de pedir una placa de nuevo, medir las dos cosas. Si solo esta
mal el histograma, es una correccion de color y es gratis. Si esta dura, es
generacion.

**Y el ancla de estilo es por caso, no por serie.** El ancla vieja es un cuadro
del video de referencia del Caso 6. Para el U5C1 el plano que manda es el
`kf08_noche`: se sube como creacion y se usa como referencia de estilo. Pedir
«mismo estilo» con palabras no acerca ni la mitad de lo que acerca la imagen.

## El puente puede decir «escrito» y dejar los bytes viejos

Cambie el carton de titulo y mande el .py al repo por `device_commit_files`. La
respuesta dijo escrito y la fecha del archivo era de hace un minuto, **pero el
contenido era el anterior**. El archivo que estaba en el contenedor si tenia el
cambio -mismo md5 que el original editado-, asi que lo viejo salio del puente,
no de mi copia.

**Para un archivo de texto no hay que cruzar el puente.** Se edita en la maquina
con `run_inline`, leyendo el archivo y reemplazando el fragmento ahi mismo. Es
mas rapido, no deja dos copias y no se puede quedar pegado.

**Y si algo si tuvo que cruzar, se verifica leyendolo del otro lado**, no por lo
que devuelve la llamada. El commit de git lo delato de casualidad -dijo «nothing
to commit»- y sin eso el repo se habria quedado con el fuente viejo mientras los
.mov si tenian el cambio.

## El still en pista aparte: como se prueba un cambio de factura sin romper nada

Cuando una placa esta renderizada en 3D y no hay creditos para rehacerla, el
arreglo que si funciona es **quitarle el movimiento generado y dejarla quieta
con la camara de la casa**. El movimiento de Kling conserva la factura de su
placa -medido: la placa marca 15,67 de dureza y sus cuadros 14,9 a 15,4- asi que
un still del clip no cambia el estilo. Lo que cambia es que, en movimiento, la
geometria del render se delata; quieta, se lee mas como ilustracion.

El tono si se arregla, y con la curva sola:

    kf01 original   p2 79  p50 199  <60  0,2%  >200 48,7%
    kf01 con tono   p2 45  p50 168  <60  5,0%  >200 18,2%

**Sin suavizado y sin bandas.** Esa es la leccion del intento anterior: la
cuantizacion bajaba la dureza a 6,33 -dentro del rango del conjunto- y dejaba
manchones en las paredes, el cielo hecho amebas y la gente de la acera borrada.
El numero mejoraba y el cuadro empeoraba. **Una sola metrica no sabe si la
suavidad vino de pintar o de embarrar.**

**Y va en pista aparte.** Los stills se ponen en la V4 tapando exactamente los
clips de la V1 -mismo cuadro de entrada, misma duracion, verificado contra los
archivos-, con la pista renombrada para que se entienda. Apagar la V4 devuelve
la version anterior sin tocar nada. Un cambio de factura es una decision de
Sebastian, no mia, y asi la puede tomar mirando en vez de discutiendo.

**Nota de verificacion:** el PNG que cruzo el puente llego con otro md5 que el
del contenedor. No estaba corrupto: era recompresion. **Un archivo de imagen se
verifica por su contenido -las mismas metricas a los dos lados-, no por el
hash.**

## Hay pistas que no son camas, y se nota en el RMS

La pista del Curso 5 no da la vuelta, y no es cuestion de buscar mejor el punto
de corte. El RMS por segundo lo dice de una: **-16 dB al empezar, -7 en el
cuerpo, -34 en el ultimo compas.** Es una pieza compuesta, con intro y cierre.
El final no se parece al principio porque nunca se penso para eso, asi que
ninguna costura de vuelta completa pasa de 0,50 de correlacion por mas que uno
la busque.

**La salida es repetir solo el cuerpo.** Costura interna: salir del cuerpo y
volver al cuerpo. La cabeza de la pista entra una vez, el tramo parejo del medio
se repite, y la cola cierra con el final real. **La pieza entra con la entrada
de la musica y termina con su cadencia, no con un fundido.** En esta pista:
corta en 87,50 y retoma en 54,62, bucle de 32,9 s, correlacion 0,525.

**El final cae siempre en el ultimo cuadro.** La primera version rellenaba con
silencio cuando la cama quedaba corta -5 s en la prueba- y eso tiraba a la
basura justo el final que se estaba tratando de conservar. Ahora el sobrante o
el faltante se ajusta en el BUCLE y la cola es intocable.

**Como se comprueba que las costuras no suenan:** contar saltos de muestra a
muestra por encima de la media mas doce sigmas, y mirar donde caen. En la cama
armada salieron 1810, todos en el mismo sitio que los 1476 de la pista original
-un elemento percusivo desde 43,6 s, que el bucle repite- y **cero en los siete
empalmes**. Si hubiera un clic de costura, apareceria ahi.

`herramientas/musica/costura.py` mira el perfil de RMS, decide solo si la pista
es cama o pieza, y busca la costura que corresponda.

## Alternar locutores: el integrado no mide lo que el oido sigue

El Curso 5 alterna voz femenina y masculina. Las dos salieron de ElevenLabs con
el mismo ajuste y **los bloques de Carlos quedaron entre 6 y 10 LU por debajo de
los de Pilar** -el de los giros en -31,5 contra -20,6 del cierre-. Eso no es un
matiz: es mas del doble de sonoridad percibida, y cada cambio de voz se oiria
como un bajon.

**No se arregla igualando LUFS integrados.** El integrado promedia toda la pista,
silencios incluidos, y castiga al bloque que calla mas: dos bloques con el mismo
integrado pueden sonar distinto y al reves. Lo que el oido sigue es el nivel
DURANTE el habla.

**Lo que si funciona:** la MEDIANA del short-term -ventana de 3 s, paso de 0,1 s-
contando solo las ventanas con voz, descartando las que estan mas de 20 LU bajo
el pico. Se iguala eso a -19 LUFS y despues **se mide el salto entre bloques
consecutivos**, que es la comprobacion que de verdad importa:

    peor salto 0,06 LU   (por debajo de 1,0 LU no se percibe)

Verificado despues con ebur128 en la maquina de Sebastian, que es un medidor
distinto del mio: los nueve bloques entre -18,3 y -19,2, dispersion 0,90 LU.

**Y la ventana manda sobre el umbral.** El primer detector de pausas devolvio
cero silencios en una locucion que tiene veintiuno: usaba la ventana de 3 s del
short-term, y una pausa de 0,8 s no alcanza a bajar esa ventana. Para encontrar
PAUSAS hace falta una ventana del orden de la pausa: RMS de 50 ms.

## La suma de voz y musica se pasa, aunque las dos esten en su sitio

Voz a -19 LUFS con pico -1,5 dBTP mas la cama a -33 bajo voz: **la suma cruda da
+1,54 dBFS.** Cada una cumple su especificacion por separado y juntas revientan.
Hacen falta 2,5 dB de aire, que es el paso de masterizacion, no un error de la
voz. Medido en la mezcla de prueba: con -2,5 dB el pico queda en -0,96 dBFS.

Es lo mismo que quedo pendiente en el U5C1, donde el master salio a -0,5 dBTP
contra un techo de -1,0. Mejor dejarlo resuelto desde el principio que
descubrirlo al final.
