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

> **CORRECCIÓN (Sebastián, 12 nov 2026: «¿por qué lo subiste en .mov? Quedamos
> en subir mp4 sin pérdida»).** Lo que se entrega es **MP4**, con la receta de
> `Entrega_MP4_Fiscalia_Receta.md` (proyecto de claude.ai, 23 oct):
> 1. máster de archivo MP4 / H.264 NVIDIA a `VideoQuality` 80000 (~32 Mb/s) con AAC;
> 2. x264 CRF 18, `preset slow`, `tune animation`, High L4.0, keyint 48,
>    `-c:a copy` y `+faststart`.
>
> Ya lo hacen `sr_pieza.exportar` + `entregas` y `herramientas/montaje/ic_mp4.py`.
> El `.mov` de 6.000 kb/s de abajo es el formato de los exports a mano de la U1
> de medio ambiente y de TA. Se copió a los videos de profes (SRPA, entrevista
> TE, conversatorio DEMA, introducciones MA) y **no es la entrega**.

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

## El bin del caso se resuelve con `bins.py`, nunca con `AddSubFolder(raiz, …)`

*19 oct 2026, cuando Sebastián no encontró la línea del Caso 03.*

Los montajes del C5U2 v2, C5U3 y C5U4 hacían `mp.AddSubFolder(raiz, CARPETA)`
y volcaban los ~45 medios **sueltos** en un bin nuevo de la **raíz** del media
pool. La estructura buena del proyecto es:

```
C5 BIENES EN EL PROCESO PENAL > U<n> > CASO <n> >
    RANURAS | CARTONES | VOCES | MUSICA | B-ROLL | COMUNES
```

La línea de tiempo va en la **raíz del caso**, al lado de sus subbins. Al
crear el bin en la raíz del Master, las tres líneas quedaron en bins paralelos
al final de la lista: estaban, pero no donde se buscan.

`herramientas/montaje/bins.py` es lo que hay que usar:

| función | qué hace |
|---|---|
| `carpeta(mp, ruta)` | resuelve y crea el camino anidado, con sus subbins |
| `clasificar(nombre)` | el subbin que le toca a un archivo, por su nombre |
| `importar(mp, ruta, rutas)` | importa cada archivo a su subbin; idempotente; **falla** si algo no entró |
| `clips(mp, ruta)` | los medios del subárbol, salteando los subbins de archivo |
| `archivar(mp, ruta, clips)` | manda una tanda a `_v1 ARCHIVO` dentro del caso |

En el `montar_*.py` son tres líneas:

```python
import bins
CASO_BIN = ['C5 BIENES EN EL PROCESO PENAL', 'U4', 'CASO 04 - los ilustres']

def _carpeta(mp):
    return bins.carpeta(mp, CASO_BIN)

def _clips(mp):
    return bins.clips(mp, CASO_BIN)

def medios(mp):
    bins.importar(mp, CASO_BIN, rutas)
```

Tres cosas que la hoja dejó claras al escribirla:

- **La clasificación es el nombre del archivo**, no una tabla aparte. Una tabla
  se desincroniza; el nombre ya lo imponen los renders. Lo que no clasifica
  **no se esconde**: queda en la raíz del caso con un aviso por consola, para
  que un archivo mal nombrado se vea en el momento.
- **`clips()` saltea los subbins que empiezan por `_`.** Cuando un caso se
  rehace conviven dos juegos de medios con los mismos nombres; sin ese filtro
  una versión vieja le gana a la vigente en el diccionario y el montaje sale
  con el clip equivocado sin avisar.
- **Se chequeó contra los 183 medios de los cuatro casos ya montados**, y el
  chequeo encontró el único caso raro: el C5U1 numeraba los cartones con un
  dígito (`_n5_`) y del C5U2 en adelante van con dos (`_n05_`). La regla acepta
  los dos. Ese es el valor de medir contra lo que ya existe en vez de confiar
  en la convención que uno cree que hay.

El Caso 02 quedó con los dos juegos separados: la v2 en los subbins normales y
los 41 medios de la v1 en `_v1 ARCHIVO`, con las dos líneas de tiempo juntas en
la raíz del caso.

## El grano de un clip generado no es un problema del modelo de vídeo (Caso 3, oct 2026)

Sebastián marcó que los clips de movimiento del Caso 3 tenían «ruido y
texturas muy raras», y lo atribuyó a Veo: *"¿por qué nos cambiamos de
Kling?"*. Antes de cambiar de modelo había que medirlo, y medido dice otra
cosa.

El número es el **gradiente local horizontal medio** sobre el cuadro 0:

| conjunto                      | ruido | dureza de borde |
|-------------------------------|-------|-----------------|
| placas quietas del Caso 3      | 1,33  | 7               |
| clips Veo del Caso 3           | 3,81  | 32              |
| clips Kling del Caso 1         | 7,45  | —               |
| clips Veo del Caso 2           | 9,85  | —               |

O sea: los clips de este caso son **los menos ruidosos de toda la serie**.
Volver a Kling habría empeorado exactamente lo que se quería arreglar. El
repo tiene 25 menciones de Kling y ninguna de Veo, y eso sesgaba la lectura.

Y la dureza de 32 contra 7 **tampoco** era el modelo añadiendo estructura. A
1:1 las formas y los bordes son idénticos; lo que cambia es un moteado fino y
parejo sobre todas las superficies planas. Era grano, y el grano inflaba la
propia métrica de dureza. Primero lo leí al revés y lo dije así; queda
escrito para no repetirlo.

**La herramienta: `herramientas/video/aplanar.py`.** `hqdn3d`, hasta
50:40:60:50, baja el ruido de 9,07 a 7,24 y no alcanza. `nlmeans=s=N:p=7:r=15`
sí llega. Pero **la fuerza no se elige a ojo**: con s=7 fijo el r11 queda en
1,09 contra 1,58 de su placa, o sea *más liso* que el original, que también
está mal. `aplanar.py` prueba s de 3 a 9 sobre el cuadro 0 y se queda con el
que minimiza la distancia relativa a las dos métricas de SU placa. En este
caso salieron valores entre 5,0 y 7,0, distintos por clip.

**La causa del color, aparte:** los clips se habían generado ANTES de que
existiera `piel.py`, así que los personajes en movimiento conservaban la piel
marrón mientras las placas quietas ya estaban corregidas. Medido: clips entre
−11° y +11° de tono, placas entre 24° y 26°. Luis estaba a 36° de su propia
placa. No era el modelo: era el orden en que corrí las herramientas.

## El azul institucional sale del intro oficial, medido (oct 2026)

Sebastián: *"los ae tienen un color de fondo que no es el azul institucional y
un ligero gradiente, eso está muy lejos del branding de la Fiscalía"*. Dos
cosas distintas, y las dos ciertas.

**El pigmento.** Medido sobre `FGN_intro_version7.mp4` —el intro oficial, que
la pieza ya lleva dentro y es por tanto la referencia de marca disponible sin
pedirle nada a nadie—: **#004890** institucional y **#002048** noche. La
plantilla de la casa traía **#03398B**, heredado del Caso A. Está cerca y por
eso aguantó tres cursos, pero no es.

**El gradiente.** No lo dibuja el cartón: es la placa transparentándose. Con
la tinta al 46 % el cuadro compuesto va de (94,119,158) arriba a (18,43,81)
abajo, 76 niveles. Al 88 % bajaría a 17, pero rompería el emparejado con los
Casos 1 y 2 ya aprobados. Se dejó en 46 %.

Regla: **cuando haya duda de marca, medir el intro oficial**, que es el único
activo de la Fiscalía que está en el proyecto. Y cambiar el pigmento SOLO en
el caso que se está rehaciendo —en `cartones_p3c3.py`, no en
`cartones_ta.py`—, porque tocar la plantilla repinta cursos aprobados.

## Los nombres de archivo de placa mienten (Caso 3, oct 2026)

La primera rejilla del Caso 3 se armó leyendo los NOMBRES de los archivos de
placa en vez de abrir las imágenes. `cama_sello_sin_fecha` no es un sello: son
once capturas de pantalla impresas sobre un escritorio. De ahí salieron doce
ranuras mal calzadas y ocho seguidas corridas una casilla entera.

**Antes de montar, siempre:** `silencedetect` sobre el máster de narración,
casar los mp3 de bloque contra el máster por duración con programación
dinámica —no con el método ávido, que se desincroniza en cuanto un bloque
abarca dos segmentos—, y cruzar cada ranura con la frase que se oye encima.
Está en `herramientas/rejilla/cruce.py`. Sin eso no se monta.

Corolario para Magnific: el `thumbnailUrl` es un recorte **cuadrado de
400×400** de un cuadro 16:9. Emparejar contra él dio tres parejas falsas. Se
empareja contra el `previewUrl` a 1024, y contra el `_crudo_*.png`, nunca
contra la placa ya graduada.

## Media acción, y las manos cuando no puede haber caras (Caso 3, oct 2026)

Sebastián, sobre el primer montaje: *"muestra más a los personajes a media
acción a lo largo de TODO el video, no puros cuadros vacíos… ¿qué pasó con los
prompts elaborados de media acción, fotográficos, cinematográficos, planos
sobre el hombro, cenitales, contrapicados?"*.

El número le daba la razón: de 28 placas, **21 eran entorno vacío**. Había
estirado la convención de «cama institucional» a casi toda la pieza en vez de
aplicar el método de prompts hero que está escrito más arriba en este mismo
archivo. Entraron dieciséis placas nuevas.

Donde el caso no permite caras —el equipo, los funcionarios, por la regla SRPA
de «sin personal identificable»— la acción va en las **manos**: la mesa en
cenital con ocho manos y una hoja a media deslizar, el dedo detenido a mitad
de un renglón, la mano que acaba de soltar un documento que nadie recoge. No
es un rodeo a la regla: es el plano canónico del método, y la regla lo empuja
hacia él.

Tres fracasos de prompt que costaron una repetición cada uno, y cómo se
arreglaron:

- **Una banda amarilla por debajo del piso de saturación.** `grade_placas` con
  `forzar` no mueve el tope; el amarillo salía generado a 0,34 y el piso es
  0,45. Se arregla en el prompt, no en el grade: *"THAT YELLOW BAND IS THE
  ONLY SATURATED COLOUR ANYWHERE IN THE WHOLE IMAGE"*.
- **`piel.py` manchó una mano casi gris** (×1,57 de saturación sobre una mano
  clarísima). En placas de solo manos cuya piel ya está en banda, se salta.
- **Teresa con los brazos arriba parecía estornudar.** Se arregla nombrando
  los fracasos, no la pose: *"HER ELBOWS STAY DOWN… she is NOT reaching, NOT
  recoiling, NOT sneezing"*. Es la regla de bloquear las dos versiones
  opuestas del cliché, aplicada al gesto.

## Una prohibición en mayúsculas sobre la ropa se dibuja como texto (Enfoque diferencial, 3 nov 2026)

El patrullero Wilmer y su compañero salieron con parches en la chaqueta que
decían «NO»: el token del personaje decía «with NO badge, NO insignia, NO patch
and NO lettering». Seedream leyó la palabra en mayúsculas pegada a la prenda y
la escribió en la prenda. Lo mismo pasó con un token en mayúsculas al lado de
un formulario: «THE PROSECUTOR ON DUTY» quedó impreso como título del papel.

La regla: **la ropa se describe en positivo** —«de tela completamente lisa, sin
nada cosido, prendido ni impreso en ninguna parte»— y un token en mayúsculas
no va en la misma frase que un papel o una prenda que el modelo pueda rotular.
Las prohibiciones generales siguen en la cláusula de placa limpia, en minúscula.

## Revisar las placas con `creations_read` antes de bajarlas

`mcp__magnific__creations_read` muestra la candidata a 512 px sin bajar nada.
Para tandas chicas (rehechas, detalles) es más rápido que bajar a la máquina,
armar la hoja y subirla al contenedor.

## Lo que Sebastián ajusta a mano, medido, y lo que pide después (Ley 1826, 3 nov 2026)

Antes de su revisión de Ley 1826 se contó, sobre los docs de las rondas
anteriores (P3, C5, TA, DF/16 situaciones, GJ, JR, DH), qué toca él a mano en
las líneas que aprueba y qué pide cambiar. Los dos rankings, en orden:

**A mano, en 16 líneas aprobadas:** (1) fundido a negro al final del respiro,
antes del cartón blanco de cierre —medido en SIT C: luma 66 → 16 en 9 cuadros;
en DH U2, ~20 cuadros—, o desde negro en un cambio de escena: 9 líneas.
(2) Recortar la cama para que no pise el sonido del intro ni del outro: «always»
(ya está en `cama_musica` con `abre`/`cierra`). (3) Quitar el respiro o
recortar el último cartón: 4 líneas. (4) Apagar o mover capas de movimiento y
detalle, partir clips: 7 líneas.

**Lo que pide (~95 pedidos en 13 rondas):** la placa no muestra lo que la voz
dice o falta quien se nombra (~22) · cartones que faltan, primera mitad
«vacía», redacción, dígitos (~14) · cuadros vacíos, gente a media acción,
insertos de detalle (~12) · defectos de movimiento (~12) · color, piel, estilo
(~10) · placas repetidas (~9) · audio y voz (~8) · más animación y boca en los
planos de habla (~6) · rótulos (~4).

Lo que cambió en la receta por eso (`lp_pieza`, `cartones_lp`):

- **El respiro funde a negro** en sus últimos 16 cuadros, horneado en el
  archivo (`lp_pieza.respiro`, paso aparte). `blackdetect` marca un cuadro al
  final del respiro: es el fundido, no un hueco.
- **El último cartón termina con el cuerpo**, no sobre el respiro. Así lo deja
  él en C, D, E, G y en DH U2: cartón fuera en el corte, respiro limpio,
  fundido. La regla vieja de las situaciones («el último cartón se queda
  sobre el respiro lo que tarde en leerse») queda derogada.
- **Rótulo y cartón siguen sin convivir, pero el cartón se corta donde empieza
  la ranura del rótulo** en vez de descartarse entero («Durante los últimos
  tres años…» volvió a la U2 C2 a 10,3 car/s).
- **Un hueco de más de 400 cuadros sin cartón en la narración es un fallo**,
  aunque la placa «ya lo diga»: en la U2 C1 había 27 s sin cartón y volvió
  el de la caída de las ventas.
- Los cuadros de prueba: la hoja de `revisar` muestra el COMPUESTO a mitad de
  cada ítem, así que donde hay un inserto V3 la fila de V1 enseña el inserto,
  no la placa madre. No es una placa repetida.

## Las caminatas hacia cámara: el encuadre se abre, no se recorta (Enfoque diferencial, 3 nov 2026)

Kling, con un personaje que camina hacia la cámara, lo acerca hasta sacarle la
cabeza por arriba; el recorte al 88 % con que se conforma el clip lo adelanta
todavía más. En las cuatro caminatas del curso (C1 r01, C3 r04, C5 r01, C5 r18)
el conformado terminaba con la cabeza cortada, y la salida anterior —cortar
corto y estirar 3×— era peor que el defecto.

Lo que sí funciona, y sale gratis (`mov_ed.ABRE`): el encuadre se abre a lo
largo del clip, del 0,88 de la ranura al 1,00 del crudo, con smoothstep. El
cuadro 0 sigue siendo exacto a la ranura horneada, el final deja la cabeza
dentro, y la ventana útil puede ser un 20–30 % más larga, así que se estira
menos. Se lee como un retroceso de cámara suave, no como un zoom.

Y mirar la cola del crudo antes de fijar la ventana: en C5 r18 Kling vuelve
TRANSPARENTE a Valentina desde el cuadro 82 (se desvanece, no sale de cuadro).
La ventana se corta en el 78.

## La entrada de un clip es un CORTE SECO: ningún fundido contra una placa que se mueve (Ley 1826, 3 nov 2026)

Sebastián, sobre la U4 C2 r09: *«don't make it so shaky at the beginning of
clips, it looks so uncanny, like the video is glitching, doesn't look natural
(…) the transitions between clips cannot have this ghostly dragged choppy
feeling movement of the camera»*. Es regla de la biblia (§8).

La causa estaba en el conformado, no en Kling: el clip entraba con un fundido
de 12 cuadros (`MEZCLA`) contra la ranura horneada que va debajo en V1, y esa
ranura SE MUEVE —el zoom y el pulso de `camara.py`— mientras el Kling no. Doce
cuadros de dos imágenes desfasadas se ven como un arranque tembloroso y
fantasmal. El fundido venía del caso Miriam y Mariana, donde empataba el borde
de salida; aquí el clip cubre la ranura entera desde el cuadro 0 y no hay nada
que empatar: el corte anterior ya es un corte.

`mov_lp.MEZCLA = 0` y `mov_ed.MEZCLA = 0`: el clip se escribe tal cual, sin
`overlay`. Si algún día un clip entra a mitad de ranura, el empate se resuelve
con el cuadro 0 del clip igual a la ranura en ese cuadro (como las caminatas
`ABRE`), nunca mezclando dos imágenes que se mueven distinto. Lo ya conformado
no se rehace (él lo pidió así); la regla rige desde aquí.

Y un clip que se ve «demasiado realista» frente al resto —otro estilo, otra
textura— se retira y queda la placa horneada: la pieza es gráfica plana, y un
clip que se separa del estilo rompe más que lo que aporta su gesto.

## Una mano que se dibuja bien: palma abajo, dedos juntos, pulgar a la vista (Ley 1826, 3 nov 2026)

Sebastián, U4 C3 r03: *«hand its anatomically incorrect»*. La placa pedía «a
young man's hand slides a request across the desk» y el modelo resolvió el
brazo entrando por la esquina superior y la mano de plano HACIA la cámara: en
escorzo, con dos dedos visibles y sin pulgar. Un escorzo de mano es lo más
difícil de dibujar para una persona y también para el modelo.

La pose que sale bien a la primera (35 cr, una tirada): cámara a la altura de
la mesa y DE LADO, la mano entra por un borde lateral, **palma abajo, los
cuatro dedos juntos y planos sobre el objeto, el pulgar visible a un lado**,
el dorso y los nudillos hacia el espectador, y se dice en el prompt («exactly
five fingers of natural length, nothing hidden or bent oddly»). Vale para
cualquier mano sobre una mesa: empujar una hoja, apoyar una carpeta, posar la
mano junto a un teléfono. Lo que no se pide: dedos apuntando a la lente, una
mano que cruza hacia la cámara, dos manos entrelazadas en escorzo.

## El patrullero colombiano lleva su uniforme; la noche es gris, no negra (Enfoque diferencial C3, 4 nov 2026)

Sebastián: *«none of the characters from la Policía Nacional look like
Colombian patrulleros regarding their attire, specially during the incident at
the airport»* y *«clips graded with too much hard black tones, everything's
supposed to be more greyish»*.

- **Uniforme.** La regla vieja («ningún uniforme: chaqueta oscura lisa») dejaba
  a un patrullero que nadie reconocía. Un policía de servicio va con el
  uniforme de la Policía Nacional (`base_ed.UNIFORME_POLICIA`: verde oliva,
  chaleco reflectivo verde-amarillo de dos franjas grises, gorra verde), sin
  letras, insignia, escudo, bandera, placa ni arma. Un token que se inserta a
  mitad de frase lleva la versión corta (`UNIFORME_CORTO`); la descripción
  entera va en su propio párrafo (`arma` la agrega si hay un patrullero): un
  token largo con punto y coma rompe la oración del plano.
- **Re-vestir sin perder el plano**: la placa aprobada como referencia 'mismo'
  («mismo plano, misma gente, misma luz; solo cambia la ropa») + la hoja nueva
  como primera referencia. Diez de diez salieron a la primera.
- **La limpieza de color se come el uniforme**: frío x0,08 y amarillo suelto
  x0,15 dejan el verde y el chaleco grises. Esas ranuras van en
  `escenas.CHALECO` (acota a s ≤ 0,55 el chaleco y ≤ 0,30 el verde, sin girar a
  la mostaza). Y el grade sin techo puede volver a quitárselo (r02, r10 salieron
  con chaleco blanco): `construir` lo devuelve desde la limpia con
  `reinyectar_acento(banda=(34, 62), perdida=0.8)`.
- **Gris, no negro**: `escenas.GRIS = (piso, codo)` levanta la sombra de todo
  el tema con una curva suave (`ed_pieza.gris`; en ffmpeg `gris_vf` para los
  clips que se quedan) y SIN_TECHO para las de noche. Con (30, 130), medido en el C3:
  p2 12-25 → 38-45 y bajo 30 de 3-59 % → 0 % en las 25; la terminal de p50
  20-50 → 57-61; los hero de noche quedan en 45-52.
- **Un detalle de agarre se pide nombrando a quién se agarra**: «la mano
  sostiene el brazo de otro hombre» devolvió la mano de un policía sobre el
  chaleco de otro policía. Funcionó «el pasajero NO es policía: camisa clara,
  sin chaleco».
- Subir referencias desde Windows falló dos veces (SSL EOF en el PUT); desde la
  nube con curl salió a la primera: JPEG en `D:\DAE\_tmp\ed\up`, stage, PUT.

## Una palabra mal dicha se injerta, no se regenera el bloque (Enfoque diferencial C4, 4 nov 2026)

Sebastián: *«Taita se pronuncia con tilde en la primera a»*. ElevenLabs había
dicho «taíta», tres sílabas, en uno solo de los tres bloques (el STT de cada
toma lo delata: oyó «tahita» en d02 y «Taita» en d06 y d16). Regenerar el
bloque entero cambia su largo y corre la rejilla, los cartones y la música de
una línea que él ya tocó.

`herramientas/voz/taita_c4.py` hace la cirugía sobre el máster: toma nueva del
mismo bloque con «Táita» escrito con tilde (la tilde en el TTS fuerza el
acento; el cartón verbatim sigue «Taita»), STT de la toma y del máster, y entre
el final de la palabra anterior y el comienzo de la siguiente se apaga la
vieja y entra la nueva, **con los bordes por energía** (tramos de 10 ms sobre
el umbral; el STT da los bordes con ±30 ms), centrada en su lugar, igualada en
RMS (−19,3 → −19,4 dB) y con fundidos de 12 ms dentro del silencio. El máster
mide exactamente lo mismo (7.551.604 muestras) y el STT del tramo nuevo dice
«Taita».

**Resolve tiene abierto el WAV de la voz y Windows no deja reemplazarlo**
(`PermissionError: Access is denied` en `os.replace`). Los mp4 de las ranuras
sí se reemplazan en su sitio; el audio no. El corregido va con sufijo
(`ED_C4_NARRADOR_v2.wav`, que `ed_pieza.plan` prefiere si existe) y entra a la
línea con `cirugia_ed <L> v=2 cambiar <viejo> <nuevo>` (`ReplaceClip` del
medio del pool con otra ruta: el item de la línea conserva todo lo demás, y el
retrato comprueba que solo cambió el nombre del archivo).

**Y ffmpeg cambió de carpeta**: ya no es `ffmpeg-9.0-full_build` sino
`ffmpeg-9.0.2-full_build` (WinGet lo actualizó). Buscarlo con
`glob(r'C:\Users\call_\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\ffmpeg.exe')`
en vez de escribir la ruta.

## Los golpes de aire se miden bajo 60 Hz y se cortan solo donde están (Enfoque diferencial C5, 4 nov 2026)

Sebastián: *«mucho golpeo de aire en el micrófono»* sobre una pregunta de
Julián (la voz del funcionario). Medido en envolvente de 20 ms: un golpe de
−7 dBFS bajo 80 Hz, **8 dB por encima del habla** (en Pilar, los graves quedan
32 dB bajo el habla). Un paso alto de 100 Hz en todo el bloque lo bajó solo a
8,5 dB bajo el habla. Lo que funcionó (`voz/aire_c5.py`): el paso alto de
100 Hz en los bloques de esa voz y, **solo en los tramos de 10 ms con energía
bajo 60 Hz sobre −40 dBFS** (290 ms en el bloque; la voz normal de un hombre
nunca pasa de −41 ahí), un paso alto de 200 Hz con rampas de 10 ms. Quedó 27 dB
bajo el habla, el resto del máster idéntico. Un detector por «graves cerca del
habla» marcaba 1,4 s de los 2,4: la voz de un hombre tiene graves.

Y **los marcadores se leen en las cinco líneas**, no solo en la que él nombra:
pidió los del C5 y había otro en el C1 ya entregado («missing around this
part»: la placa del vecino había perdido la silueta que la voz nombra).

## Cuenta nueva de Magnific: lo de la vieja no existe (Estándares interamericanos, 5 nov 2026)

El curso se hizo con otra cuenta (jpcolombia3, Pro, 300.000 créditos). Para
cambiarla no hace falta API: se cierra la sesión del conector de Magnific en
Claude y se inicia con la cuenta nueva. Lo que hay que saber después:

- **Los identificadores de la cuenta vieja dan «not found».** Las anclas de
  estilo (placas aprobadas de Ley 1826 y Enfoque diferencial) y la hoja de
  personaje de ED se subieron de disco: `creations_request_upload` → PUT desde
  la máquina → `creations_finalize_upload`. Quedan en `prompts/placa_id_ei.json`
  como `EI_ANCLA_*` y `EI_ESTILO_HOJA_*`.
- **El PUT desde Windows se corta con placas de 2560** («The write operation
  timed out»). `subir_ei.py` las baja a JPEG de 2048 y usa timeout de 300 s, y
  la tanda corre en segundo plano (`cad_subir.py`) porque el puente corta a los
  60 s: de nueve PUT en primer plano llegó uno.

## `AddSubFolder` devuelve None si Resolve está en Deliver

`arbol_ei.py` no creaba ningún bin y no daba error: `AddSubFolder` devolvía
None. `GetCurrentPage()` decía None y Resolve estaba en la página Deliver.
`resolve.OpenPage('edit')` antes de tocar el pool, y salieron los 58 bins.

## Una bandera aparece aunque la placa limpia la prohíba (EI S01 r08, 5 nov 2026)

La oficina de la organización salió con una bandera de asta y escudo en el
rincón, en gris y por eso fácil de pasar por alto en la hoja de contactos. La
cláusula de placa limpia ya decía «no flags». Se arregló con la placa aprobada
como referencia y una sola instrucción en positivo —«el rincón del fondo es una
pared lisa, sin nada delante ni colgado»— (35 cr, dos de dos limpias), y se
rehízo solo esa ranura (`ei_pieza.py S01 elegir construir=8`).
**Revisar a resolución completa los rincones de todo interior institucional**
(oficina, ONG, alcaldía, despacho): es donde el modelo pone la bandera.

## Una placa de referencia propaga sus defectos (EI S01, 5 nov 2026)

La bandera del r08 no se quedó en el r08: esa placa era la referencia de
LUGAR de r09 a r12 («It is the SAME office»), y las cuatro salieron con su
bandera en el mismo rincón. Antes de usar una placa como referencia de lugar o
de estilo, revisarla a resolución completa: un defecto en la madre son cinco
placas que rehacer (fueron 175 cr en vez de 35).

## Palabras del prompt que se vuelven defectos (EI, 5 nov 2026)

Cuatro placas aprobadas en la hoja de contactos que hubo que rehacer al
mirarlas a tamaño de línea, y lo que las causó:

- «The window behind him bright with the **last light** over the hills» →
  cielo rosado de atardecer. Contra la regla de luz neutra; la hora del día no
  se nombra, se dice «plain overcast neutral grey sky».
- «a folded sweater, **earth on its folds**» → manchas oscuras que se leían
  como agujeros en una prenda hallada en una fosa. Se dice «whole and intact,
  a faint dusting of dry pale earth along one fold, no spots, no holes».
- «behind her the plain **light box with plain grey films**» (medicina legal)
  → radiografías con costillas: un cuerpo. En un despacho forense la pared va
  lisa.
- Un personaje que «turns his hat in his hands» y además lleva sombrero → dos
  sombreros. Se dice «bare head, holds his one hat; exactly one hat in the
  image».

Las cuatro se arreglaron con la placa aprobada como referencia `image`
(«keep this exact image… only one thing changes»), 35 cr y dos de dos.

## Kling: entrar caminando mueve la cámara; quedarse en su sitio no (EI S01 r08)

«The family comes in through the open door… follow one step behind» y Kling
siguió a la familia con la cámara: a 1,8 s la abogada ya estaba fuera de
cuadro y a 4,6 s quedaban figuras transparentes. La segunda tirada, con «says
a word of welcome… nods back… all four stay in their places in the doorway»,
salió quieta y con boca. Para un plano de grupo, gesto y habla en sitio; la
caminata, solo con una persona y hacia algo que ya está en cuadro.

## Una ranura más corta que el crudo se recorta, no se acelera

`mov_ei.kling` hace el retime del crudo ENTERO al largo de la ranura: un
crudo de 121 cuadros en una ranura de 83 iba a 1,46x, y una boca que habla
acelerada se nota de inmediato. En `crudos.json` cada clip lleva `hasta` =
(largo + 2) / 24 s cuando la ranura es más corta que el crudo, y así va a
velocidad nativa. Once de 25 en EI. El mismo `hasta` corta las colas malas.

Y la rama normal del conformado podía dejar el clip un cuadro corto (82/83):
ahora repite el último cuadro con `tpad`, igual que la rama de INICIO.

## cartones_ei: no quema nada si hay FALLAS, y dos herramientas nuevas

`cartones_ei.py --quemar` calcula, imprime las FALLAS y **no quema ningún
cartón** si hay una sola (renglones > 3 o menos de 60 cuadros). En EI la
cadena dijo «LISTO» con cero cartones en disco; hay que leer la línea FALLAS.

- Un trozo puede cruzar dos bloques de voz seguidos: `'d03_x+d04_y'` en
  ELEGIDOS (entra con la voz del primero, su bloque termina con el segundo).
  Sirve cuando la voz parte una enumeración que en el documento es una sola.
- `DESPLAZA = {(video, n): cuadros}` hace entrar un cartón tarde cuando el
  anterior se queda sin tiempo de leerse (S06: el anterior pasó de 20,8 a
  14,5 car/s).

## Los cuadros iniciales de Kling se suben desde la nube

Desde Windows, uno de cinco PUT volvió a dar «EOF occurred in violation of
protocol» (ya había pasado en ED). El camino que no falló en 25 subidas: el
JPEG de 2048 se hace en la máquina (`D:\DAE\_tmp\ei\up\kling`), se trae con
`stage` y el PUT va con curl desde el contenedor. Las URL prefirmadas duran
una hora.

## Un libro en la mano se dibuja abierto de frente, no de canto (EI S04 r06, 5 nov 2026)

Sebastián marcó el r06 del S04: *«the booklet looks off, doesn't make sense
how it opens»*. La placa («draws out a slim volume… half out of the shelf»)
había salido con el libro de canto contra la cámara y las hojas asomando por
arriba, y Kling lo hojeó así: un objeto que no se entiende cómo abre. Lo que
salió legible a la primera, con la placa vieja como referencia de personaje y
lugar: **por encima del hombro, el libro abierto de frente en las dos manos,
el lomo vertical en el medio, los pulgares en las esquinas de abajo y los
dedos detrás de las tapas**. Y Kling pasa la página entera sin romper nada.
La otra salida obvia —el libro abierto sobre el escritorio— se descartó por
otra regla: la r05 ya era eso y quedaban dos planos iguales seguidos.

## `cirugia_ei` necesita `reemplazar_en_sitio_ei`

`cirugia_ei.py` importa `reemplazar_en_sitio_ei` (retrato, `items_de`,
`norm`) y el clon del curso no lo traía: se notó recién al primer `relink`.
Es `reemplazar_en_sitio_ed.py` con `ei_pieza`. Al clonar las herramientas de
un curso, clonar también las que importan.

## Una lámina se lee si muestra un momento corriente, no una metáfora (EI S05 y S11, 5 nov 2026)

S05 (dos tomos como monolitos con el equipo diminuto entre ellos) y S11 (un
expediente que pasa entre dos manos sin cuerpo, el palacio de justicia en la
ventana) pasaron la revisión propia y Sebastián las vio «funny». Las que sí
funcionaron (S02, S03, S09) muestran a una o dos personas a escala real
haciendo algo que se reconoce. Las nuevas llevan la cabecera `LEGIBLE` de
`imagenes_ei.py` en vez de `AFICHE`: un momento de trabajo corriente, nada
sobredimensionado, ninguna metáfora visual, «cada mano pertenece a una persona
que se ve». S05: ella lee en voz alta una sentencia y él escucha con la otra
abierta; la bufanda, plegada plana en su bolsa, sobre el expediente. S11: un
colega le entrega la síntesis a la fiscal; la sentencia completa, cerrada, en
el escritorio.

**La marca va arriba en el lado lleno (x > 1530, y < 280 en 1920×1080 con el
panel a la izquierda): ninguna cabeza ahí.** Las dos tiradas buenas tenían a la
persona de pie justo debajo. Se arregló con la placa elegida como referencia
`image` y «change ONLY the framing: the camera pulls back… above the head a
wide band of plain empty wall; the top right corner plain» (35 cr, dos de dos).
`LADO` ya pide esa esquina lisa. `images_expand` no sirve para esto: el modo
por defecto pintó en el margen una interfaz de edición con texto inventado y
`seedream-4-5` no amplió nada (150 cr perdidos).

## Las ranuras sin etiqueta de color se ven más saturadas en Resolve (DA V05, 7 nov 2026)

Sebastián desaturó a mano el arranque del V05 y preguntó qué había pasado con la
desaturación. Había tres causas, y una vale para toda la serie:

- **ffmpeg codifica RGB → yuv420p con la matriz BT.601 y no etiqueta el
  archivo.** Resolve lee un HD sin etiqueta como Rec.709 y le sube un 13–15 %
  la saturación, con un corrimiento leve hacia lo cálido. Verificado sobre la
  revisión del V05: el render coincide con la fuente decodificada como 709
  (diferencia media 0,0005) y no como 601 (0,002). Todas las medidas de
  saturación (`sat_mide`, los grades) decodifican como 601, así que leen un
  14 % por debajo de lo que él ve en la línea.
- **Kling devuelve el clip 1,2–1,9× más saturado que su placa**, y más cálido.
- En la DA, `limpia` acota el verde y el ocre en vez de apagarlos, y la
  apertura de minería salió en 0,08–0,12.

Para un curso nuevo: codificar las ranuras con
`-vf ...,scale=out_color_matrix=bt709:out_range=tv` más
`-colorspace bt709 -color_primaries bt709 -color_trc bt709`, medir
decodificando como 709, e igualar la saturación de cada clip de Kling a la de su
placa en el conformado. **No se cambia a mitad de un curso:** un clip reconformado
saldría un 14 % más gris que sus vecinos.

Su corrección fue un «Saturation, Hue & Lum Mix» en el nodo 1, que en el render
deja ×0,44–0,49. Para replicarla: `CopyGrades` desde uno de sus ítems, en una
versión local nueva (`AddVersion(nombre, 0)`), así su «Version 1» queda
intacta. Se aplicó solo a lo que medía en el rango de lo que él corrigió; lo de
0,046 para abajo se dejó, porque le gustan algunos de los colores que traen los
clips. Y se mide en ventanas sin cartón ni gráfico: los cartones y los paneles
de la DA llevan tinte azul a cuadro completo, y un cuadro a mitad de ranura
mide 0,67 de saturación azul.

## Los ajustes de render son del proyecto: un render sin audio deja mudo al siguiente (DA, 10 nov 2026)

Para medir la desaturación del V05 rendí un tramo de control con
`SetRenderSettings({'ExportAudio': False, ...})`. Esos ajustes quedan guardados
en el proyecto, y `da_pieza.exportar` no fijaba `ExportAudio`: el máster del
V05 y el del V06 salieron **sin pista de audio**. `verificar` no lo notó,
porque el `ebur128` sobre un archivo sin audio no imprime nada y no falla.
Se vio al medir la sonoridad a mano antes de subir; la copia que ya estaba en
`G:\My Drive\_DA subidas` se sacó antes de moverla a la carpeta compartida.

- Todo `exportar` fija **`'ExportVideo': True, 'ExportAudio': True`** de forma
  explícita. Nunca se confía en lo que dejó el render anterior.
- `entregas` se niega a codificar un máster sin audio, y `verificar` imprime
  una línea `audio OK / FALLA`.
- Después de un render de control (sin audio, con MarkIn/MarkOut) se
  devuelven en el acto `ExportAudio: True` y `SelectAllFrames: True`.

Los demás `*_pieza.exportar` (ed, ei, lp, dh, jr, gj, sit) tienen la misma
forma y la misma trampa latente.

## El AAC de Resolve sobrepasa 2,5 dB en los transitorios (entrevista TE, 11 nov 2026)

El compuesto de la entrevista de técnicas especiales llegaba a Resolve con el
techo en −2,9 dBTP y el export salía en −0,4: medido con astats a 192 kHz, el
pico del export cae en otro sitio que el del compuesto. No era la mezcla ni una
capa con audio: **Resolve codifica el AAC a 185 kb/s** y a ese caudal los
transitorios de una voz comprimida sobrepasan unos 2,5 dB.

La salida, sin volver a rendir: `herramientas/montaje/te_limita.py`. El video del
export se copia tal cual (`-c:v copy`) y el audio se rehace con un limitador a
−2,5 dBFS sobremuestreado a 192 kHz, en AAC a 320 kb/s. Quedó en −2,5 dBTP y
−16,3 LUFS, con el mismo número de cuadros y el arranque de los dos streams en 0.
El export crudo va a `_descartes`. Para una pieza de profe hablando, que no
lleva música, dejar el compuesto en −3 dBTP no alcanza: el techo se garantiza
después del export, no antes.

## Caso Nico (SRPA, 12 nov 2026): seis cosas nuevas

- **AE se abre con un script, no con aftr.** aftr no tiene `openProject`. Lo
  que funciona es `AfterFX.exe -r abrir.jsx`, y el jsx abre el proyecto con
  `app.open(f)` **solo si `app.project.dirty` es falso**. Así no aparece
  ningún diálogo de guardar y no se pierde nada de lo que Sebastián tenga
  abierto. Escribe el resultado en un txt. Si el proyecto está sucio, se le
  pide a él.
- **Las listas de aerender salen premultiplicadas.** ProRes 4444 «High Quality
  with Alpha»: leído como alfa directo, el tinte del panel sale navy, al lado
  del azul de los cartones. En Resolve el clip lleva
  `SetClipProperty('Alpha mode', 'Premultiplied')`, y `sr_pieza.construye` lo
  fija.
- **El naranja de la r45 venía de la placa, no de Kling.** Lo había atribuido
  a Kling, y medido después resultó otra cosa: la placa graduada estaba a
  29,6° y el clip a 28°. La causa es la curva GRIS, que va DESPUÉS de
  `nivelar_acento` y le corre el tono al buzo. Así quedaron la r45 a 29,6°, la
  r49 a 31,1° y la r07 y la r42 a 33,9°, contra 35–42° en el resto.
  - `construir` ahora vuelve a nivelar después de GRIS. Las cuatro se
    rehornearon y quedaron entre 39,5° y 40,9°.
  - `mov_sr` igual mide el acento del cuadro 0 contra la placa y gira el clip
    si se va más de 4°. También iguala la saturación media del clip a la de la
    placa (×0,76–1,0).
  - **Antes de culpar a Kling por un color, se mide la placa.**
- **Estirar más de 1,4x se interpola.** La r72, recortada a 3 s (72 cuadros)
  porque después el pelo vuelve a crecer, llena una ranura de 134. Con
  `setpts` + `fps` cada cuadro se repite casi dos veces y el clip tiembla.
  `mov_sr` usa `minterpolate` (mci, aobmc, bidir) cuando estira más de 1,4x:
  la diferencia entre cuadros sale pareja (0,3–2,8) y no queda ninguno
  repetido.
- **Caminata hacia cámara a 10 s: pasan la cámara.** En la r42 (el patrullero
  y Nico) a los 4 s ya habían pasado y el pasillo quedaba vacío. En la r43 el
  defensor da media vuelta a los 3 s. La ventana útil era de 3 s para
  ranuras de 215–262 cuadros, así que se quedaron con la cámara de la casa.
  Una ranura larga de caminata no se resuelve con Kling.
- **Los JPEG de Kling se suben en tanda.** Va así:
  1. `creations_request_upload` con `count` (hasta 100);
  2. PUT con curl desde la nube, leyendo las URL del transcripto
     (`/home/claude/sr/put.py`, sin copiarlas a mano);
  3. un solo `creations_finalize_upload` con `uploads`.

  Son tres llamadas por tanda en vez de tres por imagen.

## Scribe puede devolver basura con un mp3 (introducción al curso DA, 12 nov 2026)

La transcripción del video de presentación del curso volvió con
`language_probability` 1,0 y `language_code` spa, pero eran 141 «palabras» en
chino, ruso e inglés para 3:47 de voz. El audio estaba bien: el espectrograma
era de habla y el ebur128 daba −18,9 LUFS. La entrada era un mp3 mono a
44,1 kHz y 96 kb/s, la misma receta de siempre.

Con el mismo audio en WAV mono a 16 kHz (`pcm_s16le`) salió bien a la primera:
430 palabras.

- **No basta con la probabilidad.** Antes de usar una transcripción se mira el
  número de palabras contra la duración (unas 2 por segundo) y se leen las
  primeras líneas.
- **Para Scribe, WAV a 16 kHz.**

## Pegar intro y outro a un video ajeno: ffmpeg, no Resolve (cierres de unidad DA, 13 nov 2026)

Los cierres de unidad de Delitos ambientales eran videos de diapositivas de
Gemini Notebook a 1280×720 y 24 fps, y solo llevaban nuestra intro y nuestro
outro. `herramientas/montaje/cierres_unidad.py` lo hace en una sola
codificación con la receta de entrega:

- escala a 1080 con lanczos en Rec.709;
- `fps=24000/1001`;
- audio a 48 kHz dual-mono;
- concat con los 194 cuadros del intro en los dos extremos.

Es una generación menos que el máster de Resolve y no hace falta armar líneas.
La verificación es por PSNR del tramo del cierre contra la fuente escalada con
la misma cadena. Dio 53–55 dB.

- **Los videos de Gemini Notebook terminan con una tarjeta de la marca**, de 3 s
  y en silencio. Sebastián la mandó a quitar. `inicio_tarjeta` la encuentra por
  el último corte de escena. Si la última diapositiva es casi blanca, el score
  del corte baja a 0,15, así que el umbral es 0,08 más la comprobación de que
  lo que sigue es la tarjeta quieta.
- **Un cuadro a 23,976 son 2002 muestras a 48 kHz.** Cortando video y audio en
  esas unidades, los dos quedan del mismo largo exacto y el concat no
  desincroniza.
- **Un `-ss` en el último cuadro de un archivo no devuelve nada.** Con `xstack`,
  esa entrada vacía deja a ffmpeg sin salida y con código 0, o colgado. La hoja
  toma `total-12` como último cuadro y escribe con `-update 1`.
- **Antes de rehacer una tanda, se mata todo lo de la anterior.** Hay que pasar
  `taskkill /T` por PID, sacando los PID de
  `wmic … get ProcessId,CommandLine /format:csv`, porque la salida `list` trae
  `\r` y el filtro no encuentra nada. Un proceso colgado de la tanda vieja volvió
  a copiar la U2 a `_MA subidas` después de que Drive la había quitado, y Drive
  la subió como archivo nuevo.

## Un profe centrado necesita su propia ventana (cierre del curso SRPA, 13 nov 2026)

La ventana de los videos de profes (1143×643 desde x=12) supone que el profe ya
está corrido a la derecha. En el cierre del curso de SRPA, Estanislao está
centrado y cerca de la cámara, y con esa ventana la cabeza caía dentro de la caja
de cartones (x 62–790).

- **Se mide antes de elegir.** Se toman 178 cuadros, uno cada 2,5 s, a media
  resolución. El fondo es la mediana por píxel: el profe casi nunca está a la
  izquierda, y ahí la mediana es el fondo virtual. Por cada fila, el borde
  izquierdo de la persona es la primera corrida de 8 píxeles que difiere más de
  60 del fondo. Se leen p2, p10 y p50 por fila.
- **La ventana sale de los números.**
  - La cabeza iba de x 416 (p2) a 470 (p50), y los hombros empezaban en y≈460.
  - Con 1024×576 desde (0, 40), ×1,875, la cabeza queda desde x≈810 (p10) y
    los hombros bajo y=720.
  - El panel DAE/Fiscalía del fondo entra entero.
  - Se puede arrancar en x=0 porque este fondo no trae el filete blanco: hay
    que mirarlo en cada video.
- **Va por tramo:** `srpa.TRAMOS['cc'] = [(0.0, None, (0, 40, 1024, 576))]`. No
  hace falta código nuevo.

## AE cerrado: primero se abre, después el script, después aftr

`AfterFX.exe -r ae_abrir.jsx` con After Effects cerrado escribió la primera línea
del log («existe true sucio false») y el proceso se cerró sin abrir el proyecto.
Lo que funciona:

1. Arrancar `AfterFX.exe` solo y esperar a que cargue: pasa de ~140 MB a ~1 GB.
2. Mandar `-r ae_abrir.jsx`, que abre el `.aep` porque el proyecto sin título no
   está sucio.
3. Levantar el controlador de aftr (`node controller/src/server.js` en
   `C:\Users\call_\aftr`). El panel de AE se conecta solo: el log dice
   «Panel connected».

## La ventana se mide también hacia abajo: el mentón (Bienes, 14 nov 2026)

En la introducción del curso de Bienes el profe está centrado, muy cerca de la
cámara, y a ratos se inclina hacia ella. Se probaron tres ventanas:

1. **960×540 desde (0, 40), ×2.** Era la que pedía el perfil de la cabeza (borde
   izquierdo por fila) para dejar libre la caja de cartones. Cortaba la cara por
   la boca.
2. **1143×643 desde (0, 40), ×1,68, la estándar.** Termina en y=683 de la
   fuente. Se llegó a entregar una v1. En la hoja de revisión, cuando el profe
   se inclina (c10, 5:59), el mentón se salía del cuadro. La fuente no lo
   cortaba: lo cortábamos nosotros.
3. **1198×674 desde (0, 46), ×1,60.** Es la que quedó. Llega hasta y=720, el
   borde inferior de la fuente, así que no corta nada que la fuente no corte.
   El panel DAE/Fiscalía (y 52–157) entra entero, a 10 px del borde superior.

Lo que queda de regla:

- **La ventana no puede cortar por abajo más que la fuente** cuando el profe
  está cerca: `y0 + alto = 720`, con `y0 ≤ 52` para que entre el panel. Eso da
  un alto ≥ 668 y un ancho ≥ 1188.
- **Antes de componer, una prueba con la caja dibujada** en varios cuadros,
  incluidos los momentos en que se inclina. El perfil mide el borde izquierdo,
  no el mentón.
- **Si la caja y la cara no caben, se angosta la columna; no se corta la cara.**
  El plan puede traer:
  - `MAXW`: el ancho del texto de cartones y listas (estándar 615);
  - `LT = (px del nombre, ancho del cargo)`: el lower third (estándar 48 y 900).
  `ic_pieza.ajustes()` los aplica a `cartones_ma`, `mg_ma` y `cartones_srpa`.
  En la introducción de Bienes quedó `MAXW` = 470 y `LT` = (40, 520).
- **Se simula antes de rendir.** Se dibujan el cartón más ancho y el lower third
  sobre nueve cuadros compuestos, con las mismas fuentes
  (`cartones_ma.componer` y los textos del plan).
- **Con la columna angosta las listas de cuatro filas no llevan título.** Cada
  fila entra en dos renglones como mucho: los rótulos son de 386 px, unos 18
  caracteres por renglón.
- **Una entrega descartada no se pisa.** La v1 quedó en `_descartes` (cartones,
  listas, compuesto, entrega, `.drt`), el máster en `D:\DAE\_masters_archivo`,
  y la línea de Resolve renombrada «… (ventana 1143, descartada)». Los archivos
  nuevos llevan otro prefijo (`BI2_`), para que Resolve no confunda los clips.

## Renglones equilibrados en los cartones (`balanceo.py`)

El corte voraz de `componer` deja palabras solas abajo («Conclusión de la unidad
/ 3»). Los títulos en negrita a 46 px tienen unos 22 caracteres por renglón y les
pasa mucho.

`herramientas/cartones/balanceo.py` reparte las palabras en la misma cantidad de
renglones, lo más parejos posible: minimiza la suma de los cuadrados de lo que
cada renglón se aparta del largo medio. Los planes de Bienes lo usan en `cita`,
`c_tit`, `c_ante` y `c_suelta`, con un trozo por renglón y gap 0 entre ellos.
- El alto no cambia, así que la cima medida sigue valiendo.
- Un `\n` en el texto fuerza un párrafo («Medidas cautelares\ncon fines de…»).
- La primera versión minimizaba solo el renglón más largo. Dejaba primeros
  renglones de dos palabras («La adecuada / gestión de los bienes…»). Se vio en
  la hoja de revisión y se cambió; los 18 cartones del cierre que cambiaban se
  rindieron de nuevo.

## Un máster que no entra en E:

El cierre de Bienes dura 43 min: el máster de 32 Mb/s pesa ~10 GB y E: tenía 8 GB.
- `mp4_entrega.py … <carpeta del máster>` lo manda a
  `D:\DAE\_masters_archivo\…` y deja un `LEER` en `05 EXPORTS\_master`.
- Para tener aire se movió `E:\DAE MASTER\_tmp_movido_de_D` (8,9 GB) a
  `D:\DAE\_masters_archivo\` con robocopy `/MOVE`. Quedó un `LEER` en su lugar.
- Los motion graphics en ProRes 4444 pesan ~7 MB/s. Hay que sumarlos antes de
  rendir: en el cierre fueron ~640 s, unos 4,5 GB.

## El plano cerrado de un corte se revisa cuadro a cuadro (cierre de Bienes, 14 nov 2026)

En el cierre de Bienes hay un arranque en falso. Se cortó, y la frase repetida iba
entera en un plano más cerrado (1024×576 desde (96, 40)) para disimular el salto.
En el último segundo de esa frase el profe baja la cabeza, y el mentón se salía del
plano cerrado. En el plano abierto entraba.

- **El plano cerrado tiene menos margen abajo** (termina en y=616 de la fuente) y
  no se puede bajar: el panel DAE/Fiscalía tiene que entrar entero.
- **Se mira todo el tramo, a 4 cuadros por segundo**, antes de dar por bueno el
  corte. Una prueba en un solo cuadro no alcanza.
- **El plano cerrado termina donde el profe todavía está derecho**, en una pausa
  entre palabras. Quedó de 2498,7 a 2503,35: «La adecuada intervención
  patrimonial no consiste simplemente en».
- **`ic_pieza.py reimagen <compuesto anterior>`** rehace solo la imagen con los
  `TRAMOS` nuevos y copia el audio del compuesto anterior. El audio no depende de
  la ventana, y así no se repiten las dos pasadas de loudnorm.
- **Scribe sobre 60 s del compuesto** confirma que el corte quedó limpio: la
  frase sale una sola vez.

## La última fila de una lista queda al menos 4 s

Cuando el profe enumera rápido, la última fila entra cerca del final de la frase.
Si la lista termina con la frase, esa fila dura 2 s y no se lee.

- En los planes de Bienes se midió `fin − entrada de la última fila` en cada
  lista. Las que daban menos de 4 s se alargaron sobre la frase siguiente, y el
  cartón que seguía entra más tarde.
- En el cierre, la lista final (cinco filas en 8 s) se queda hasta «…durante este
  proceso de aprendizaje». El lower third va después, sobre la despedida.
- **Se escapó en el inicio de la U4 de DH** (16 nov 2026): «Solicitud de medida de
  aseguramiento» quedaba 2,9 s y «O se abstiene de pedirla» 1,8 s, con la lista ya saliendo. Se
  vio en los cuadros a tamaño completo de la entrega, no en la medida del plan, que no lo
  miraba. Ahora `ic_pieza.py medir` y `mg_armar` imprimen «ÚLTIMA FILA x s» cuando baja de 4.
  La v2 lleva claves nuevas (`m01b`, `c02b`…) para que Resolve no use la duración vieja en caché.

## Una línea larga se arma con `ic_linea_externa.py`

`run_inline` corta a los 58 s y mata el proceso. Con 30 ítems la importación al
pool ya llega a ese límite; con 117 no termina.

`herramientas/montaje/ic_linea_externa.py` se conecta a Resolve con
`DaVinciResolveScript` y ejecuta `ic_linea.py` igual que `run_inline`, pero
lanzado con `Popen`, sin límite. La línea del cierre de Bienes (122 clips) se
armó en 60 s.

## El lower third también se mide contra la persona (cierre de Bienes, 14 nov 2026)

El lower third estándar (nombre a 48 px, cargo de hasta 900 px de ancho) llega a
x≈1020. En el cierre de Bienes el profe se inclina a la izquierda en los
primeros segundos y «Penal», la última palabra del primer renglón del cargo, le
tocaba el mentón. Se vio en los cuadros a tamaño completo de la primera entrega,
no en la hoja de contactos.

- **Antes de rendir un lower third, simularlo sobre ocho cuadros limpios** del
  compuesto, repartidos en los segundos en que va a estar en pantalla. Un cuadro
  solo no alcanza: el profe se mueve.
- Con `LT = (44, 560)` el cargo va en tres renglones y termina en x≈690; el
  nombre termina en x≈790. Queda libre de la cara y casi libre del saco.
- **Un clip que se rehace con el mismo largo lleva otro nombre** (`lt01_v2`).
  En la línea se borran los dos ítems viejos y se ponen los nuevos en el mismo
  cuadro (`DeleteClips` + `AppendToTimeline`); `revisar` confirma que todo lo
  demás quedó igual.

## Una transición horneada en la fuente se tapa con el cuadro limpio, quieto (DA U4 L1, 15 nov 2026)

La grabación de la U4 L1 trae los dos bloques de la clase en un solo archivo, y
entre ellos una transición de cubo 3D de medio segundo (937,65–938,20) que deforma
el panel DAE/Fiscalía y lo saca de cuadro. Con la ventana puesta se ve como un
error nuestro.

- **No se corta tiempo:** el audio sigue corrido, y en ese medio segundo hay pausa
  y el arranque de la frase siguiente. Lo que se cambia es solo la imagen: sobre
  [a, b) se ve quieto el primer cuadro limpio después de la transición (b).
- En el plan: `CONGELA = [(a, b)]`. `ic_pieza.tramos_vf` parte el tramo en tres
  (antes, el cuadro de b clonado con `tpad`, después) y los concatena. Los bordes
  se llevan a la rejilla de la fuente (`FPS_FUENTE`, 30 por defecto): a hacia
  atrás y b hacia adelante, para que no se cuele ni un cuadro de la transición.
- Se verificó en una prueba sin pérdida (ffv1): los cuadros de la congelada son
  idénticos al de b y el total no cambia.
- **Se busca antes de componer.** En una fuente de más de un bloque, mirar el
  empalme cuadro a cuadro: un salto de escena que no está en el habla es una
  transición del editor de la grabación.

## Una profe muy cerca de la cámara: ventana desde y=0 y columna de 560 (DA U4 L1)

La ventana estándar (1143×643 desde y=40) dejaba la coronilla de la profe a 15 px
del borde. Desde y=0 quedan 80 px, abajo solo se corta pecho y el panel
DAE/Fiscalía entra entero. Pero la cara queda más grande, y cuando ella se inclina
el pelo llega a x≈730 de salida: la columna de cartones bajó a 560 (`MAXW`) y el
cargo del lower third a 460 de ancho (`LT`).

Con la columna en 560 hay que medir cada cartón antes de rendir: cinco se salían
de la caja (cima < 250) y se acortaron. Una lista con título y tres filas de dos
renglones cabe solo si el título va en un renglón (unos 21 caracteres en negrita a
46 px); si no, una de las filas tiene que entrar en un renglón (unos 22 caracteres
a 37 px en los 476 px del rótulo).

## Una fuente que ya es un montaje: se toma el tramo del profe y se rearma (DA U3 L5, 15 nov 2026)

La U3 L5 llegó como un montaje de septiembre: export HD a 23,976 con el intro FGN, el
profe con un rótulo azul en mayúsculas quemado abajo a la izquierda, y el outro. «Ya
tiene intro» no quería decir «ya está»: le faltaban cartón de título, lower third de
la serie, cartones y AE.

- **Se busca dónde empieza y termina el profe** con detección de escena (cortes en
  8,09 y 406,86 s) y luma cuadro a cuadro alrededor: el cuadro 194 era uno de paso
  oscuro, y desde el 9755 venía el negro del outro. El audio se mira en RMS de 20 ms
  para no cortar la última palabra ni meter el sonido del outro.
- **Los bordes del tramo van a mitad de cuadro** (`194,5/FPS`, `9754,5/FPS`).
  `tramos_vf` escribe los tiempos con tres decimales: 9755/23,976 = 406,8648, y un
  borde en 406,865 se llevó el primer cuadro negro. El compuesto v1 salió con un
  cuadro de más y negro al final.
- **El rótulo quemado se deja fuera de la ventana**, no se tapa: la ventana termina
  en y=878 y el rótulo empieza en y≈980.
- **`MATRIZ_FUENTE` y `FPS_COMPUESTO`** en el plan. `srpa_composicion.escala` supone
  una grabación de Teams en BT.601, y `componer` escribe a 30 fps. Para un export HD
  hay que poner bt709 y 24000/1001; si no, se corre el color y se duplican cuadros.
- **`perfil2.py`** (`D:\DAE\_tmp\ma\u3l5`) es `perfil.py` con un tramo de tiempo,
  para cualquier tamaño de fuente y con el borde derecho. El ancho de la ventana
  salió del borde derecho de la cabeza (máx. 1474): con menos, se le corta la cabeza
  cuando se corre. `perfil.py` supone 1280×720 y, sobre el archivo entero, mide
  también el intro.

## Una grabación armada con tomas: transiciones, negros y frases repetidas (DA U3 L4, 15 nov 2026)

La U3 L4 venía editada a partir de varias tomas: cubos 3D entre ellas, un fundido
desde blanco, negros al principio y al final, y dos frases dichas dos veces con la
primera toma sin quitar. La detección de escena (umbral 0,25) solo vio los negros:
los cubos son graduales.

- **Se mide el panel DAE/Fiscalía cuadro a cuadro.** Se toma la diferencia media
  contra su mediana, sobre un recorte de 560×160 bajado a 112×32. Lo normal es 0,6;
  un cubo sube de 14 a 60, y un negro marca 174. Los bordes salen exactos al
  cuadro.
- **Se lee la transcripción buscando frases repetidas**, no solo palabras: una
  oración que vuelve a empezar igual unos segundos después es una toma que quedó.
  Se queda la limpia, y el corte cae en una pausa medida en RMS de 20 ms.
- **Si la toma buena arranca sobre negro**, el comienzo de la frase se toma de la
  toma vieja cuando es igual («Posteriormente,»), y se corta a la buena en la pausa
  siguiente.
- **Después de un corte de toma va el plano cerrado** hasta el final de la frase.
  Se revisa a 4 cuadros por segundo y ahí no va ningún cartón.
- **Un cubo entre bloques se tapa con el cuadro limpio quieto** (`CONGELA`), como
  en la U4 L1. En una pausa no se nota, y no hace falta cortar audio.
- **Lo que se dice sobre negro al arranque no se congela.** Si la imagen arranca
  tarde («Cordial saludo» sobre un segundo de negro), el clip empieza en la
  frase siguiente: un rostro quieto que habla se nota más que un saludo de menos.

## El video se corta por número de cuadro, no por segundos (U3 L4, 15 nov 2026)

`tramos_vf` cortaba con `trim=start=…:end=…` en segundos. Hubo tres errores:
- con cuatro decimales, cada congelado dejaba un cuadro de más cuando el largo
  redondeaba hacia arriba (0,1667 > 5/30);
- con bordes a mitad de cuadro, `trim` pasa los segundos a la base de tiempo del
  stream **redondeando** al más cercano, así que 7166,49 cuadros quedan en 7166;
- en la U4 L1 ya entregada, el congelado de 17 cuadros dejó uno de más (49.697 contra
  49.696 de la fuente). Desde 15:38 el video va un cuadro (33 ms) detrás del audio.

Ahora el video va con `trim=start_frame/end_frame` y el audio se corta en los mismos
tiempos (cuadro/fps). Se verifica con un generador de prueba que cuenta cuadros por
tramo, y con `ffprobe` sobre el compuesto: cuadros esperados = suma de los tramos,
y audio del mismo largo.

**El congelado se elige mirando el cuadro entero, no solo el panel.** En un fundido
desde negro, el panel volvió a su mediana en el cuadro 4366, pero el cielo y la cara
siguieron con manchas negras del fondo virtual hasta el 4370. Lo que lo delató fue
la tira de cuadros de cada corte. Se mide también la fracción de píxeles oscuros de
la mitad de arriba.

## Profe grabado con teléfono: cadencia irregular y audio mono (Enfoque diferencial, 15 nov 2026)

Los 12 videos de Camilo Borrero eran grabaciones de teléfono:
- HEVC a 1080×1920 con rotación;
- audio AAC mono;
- 30 fps declarados, con algún cuadro de 35 ms.

En 28 min eso son 26 cuadros menos que 30 × duración. Tres cosas que cambian:

- **Cortar por número de cuadro corre el video.** `trim=start_frame` cuenta cuadros, y el
  audio se corta en cuadro/30.
  - Con la cadencia irregular, el final del video quedaba casi un segundo después que el del
    audio.
  - `POR_TIEMPO = True` en el plan hace que `ic_pieza._trim` corte por tiempo en la rejilla
    de 30. Con base de tiempo 1/600, f/30 cae exacto en un tick.
  - Se mide el compuesto con ffprobe: cuadros = tramo ±1 y audio del mismo largo.
- **Mono → dual-mono antes de medir** (`ic_pieza.base_audio`, automático si la fuente tiene
  un canal). Si no, en la línea suena solo por la izquierda. Si se duplica después de
  normalizar, la medida sube 3 dB.
- **El perfil de la cabeza no sirve con un profe quieto.** `perfil2/3` toma la mediana por
  píxel como fondo, y si el profe casi no se mueve, la mediana es el profe.
  - Se eligió la ventana con la caja dibujada sobre 8 cuadros de cada video (`caja_ed.py`).
  - Después se simularon el cartón más ancho y el lower third sobre cuadros del compuesto.

## «Esos ya los hicimos»: mirar el archivo antes de saltarlo

Le dijeron a Sebastián que el inicio y el cierre de Enfoque diferencial ya estaban. En otra
carpeta del Drive (PRIORIDAD 2 › Enfoque diferencial › VIDEOS) había dos MP4 de JP:
`enfoque_diferencial_inicio_curso.mp4` y `…_bienes_cierre_curso.mp4`.
- Se copiaron a «Mi unidad», se midieron, se armó una hoja de cuadros y se transcribieron.
- Eran la **misma toma cruda** recortada y bajada a 720p: sin intro, título, lower third ni
  cartones.
- Se hicieron igual.
- Un nombre de archivo no dice si un video está terminado; se abre.

## Máster de paso: la papelera no libera espacio

Con la decisión de Sebastián de no guardar el máster de 32 Mb/s, el máster se manda a la
papelera de Windows después de verificar la entrega:
`Microsoft.VisualBasic.FileIO.FileSystem.DeleteFile(…, 'OnlyErrorDialogs', 'SendToRecycleBin')`.

Pero la papelera ocupa el mismo disco hasta que se vacía, y la de D: tiene un tope de ~25 GB
(`HKCU\…\BitBucket\Volume\{GUID}\MaxCapacity`). Pasado el tope, Windows borra para siempre
los más viejos.
- `ed_entrega` calcula lo que necesita el máster más la entrega y, si D: no alcanza, espera y
  lo dice en el log.
- Nunca vacía la papelera por su cuenta: eso lo decide Sebastián.

## El puente puede escribir el contenido viejo de un archivo de outputs

Ya estaba escrito que `device_commit_files` puede decir «escrito» y dejar los bytes viejos. En
Enfoque diferencial pasó con un `stagedPath` reusado, **incluso hacia un `devicePath` nuevo**:
`ed_entrega.py` editado en `/mnt/user-data/outputs` llegó a la máquina con el contenido de la
primera versión.
- Cada versión de un script que cruza va con **otro nombre** en outputs (`ed_entrega_v2.py`).
- Del otro lado se verifica por md5 o por una cadena que solo tiene la versión nueva, antes de
  lanzarlo.
- Un zip que entra al repo ya lo verifica `aplicar.py`.

## Bytecode viejo al regenerar un plan dentro del mismo segundo

`gen_plan.py` escribe el plan y `ajusta.py` lo reescribe con números del mismo largo en el
mismo segundo. Así, el `.pyc` de `__pycache__` (que se valida por fecha y tamaño) seguía
valiendo y `medir_plan` medía el plan anterior.
- En el contenedor, `PYTHONDONTWRITEBYTECODE=1`.
- Si una medida no cambia después de editar, primero se borra `__pycache__`.

## aftr corta a los 30 s cuando la máquina está cargada (Enfoque diferencial, 15 nov 2026)

El `batch` de una comp de lista suele tardar unos 7 s. Con aerender, un render de Resolve y
x264 corriendo a la vez, el del contenido de la U1 pasó de 30 s y el controlador de aftr
respondió `Command "batch" timed out after 30000ms`. Pasó dos veces.
- El REST (`POST /command`) no deja pedir otro tiempo.
- **AE termina la comp igual**, después del timeout: la primera quedó hecha y `mg_render` la
  rindió.
- `mg_armar` se corta en la primera y las demás no se arman. La línea falla después con
  «FALTA EN DISCO».

Qué hacer:
- `mg_armar` va con la máquina libre, no en paralelo a renders.
- Si se corta, se vuelve a correr: borra y rearma cada comp.
- Lo que se rindió de una comp terminada fuera de tiempo va a `_descartes` y se rinde otra vez.

## Un profe que no dice su nombre (presentación de Derechos humanos, 16 nov 2026)

El profe de la presentación del curso de Derechos humanos no se presenta, y ni la ficha, ni los
documentos de las unidades, ni el paquete de Camtasia de JP dicen quién graba. La ficha lista
tres autores, y uno era Estanislao, el profe de SRPA: con un cuadro de su video al lado se
descartaba. Se transcribieron el principio y el final de dos cierres de unidad del mismo profe
(«les habló…» suele estar ahí): tampoco.

- **Un nombre de lower third no se infiere por descarte.** Se arma todo lo demás y se le
  pregunta a Sebastián. Confirmó a Yefri Yoel Torrado Verjel y pidió de cargo «coautor del curso
  y el nombre del curso».
- Lo que sale de la ficha (el nombre del curso, los nombres cortos de las unidades) sí entra a
  los cartones: lo escribieron los profes.

## After Effects tarda en abrir un proyecto grande: no se relanza el jsx

`AfterFX.exe -r ae_abrir.jsx` con un `.aep` de 28 MB y 363 ítems dejó a AE «Not Responding»
dos minutos, con la barra de «Open Project». aftr no responde mientras tanto (timeout de 30 s).
El jsx tiene abierto su log hasta que `app.open` vuelve, así que el archivo queda vacío.

- Relanzar el jsx encima da un diálogo modal en AE: «Unable to execute script at line 7.
  Permission denied», porque el log todavía está tomado. Hay que cerrarlo a mano.
- Se espera: `tasklist /V` muestra el título de la ventana con el proyecto nuevo cuando
  terminó, y `getProjectInfo` vuelve a responder.

## Si After Effects o Resolve se cerraron a mitad de una cadena (inicio de la U2 de DH, 16 nov 2026)

Entre una pieza y la siguiente, After Effects y Resolve se cerraron (o se reiniciaron). La
cadena no lo sabía y falló en dos sitios con errores que no dicen eso:

- **`mg_armar`: `URLError [WinError 10061] … actively refused it`.** No es el timeout de 30 s:
  es que el controlador de aftr no está escuchando. `tasklist` no mostraba `AfterFX.exe`, y de
  node solo corrían los `mcp.js`, no el `server.js`.
  - Se levanta en el orden de siempre: `AfterFX.exe` solo (hasta ~1 GB); `-r` con el jsx que
    abre el `.aep` (esta vez abrió en segundos); `node controller/src/server.js` en
    `C:\Users\call_\aftr`, con su log, hasta «Panel connected».
  - El primer `getProjectInfo` después de levantar puede dar «Bad JSON from host»; el segundo
    ya responde.
- **La línea: `'NoneType' object has no attribute 'GetSubFolderList'` en `carpeta_pool`.**
  Resolve estaba en un «Untitled Project» vacío (raíz del pool sin carpetas, 0 líneas, página
  None), así que `AddSubFolder` devolvía None. Se cargó `DAE MASTER - CURSOS` con
  `LoadProject` (tarda más de 58 s: `run_inline` corta, pero la carga sigue; se espera
  preguntando `GetCurrentProject().GetName()`). Las líneas ya entregadas seguían ahí.
- **`dh_cadena` no deja seguir a la entrega si el gráfico falla**: escribe «MG FALLO» en vez de
  «LOTE LISTO», y la entrega que espera ese log no arma una línea a medias. Las que quedaron
  esperando se matan por PID (`Get-CimInstance Win32_Process` con `-match`, porque `wmic … csv`
  parte mal las líneas de comando que llevan comas).

## E: se llena en una tanda de profes (inicio de la U4 de DH, 16 nov 2026)

Seis piezas de profe de DH en una tarde y E: quedó en 0,0 GB a mitad de la séptima. Cada pieza
deja en E: entre 1,4 y 2,7 GB: el máster de 32 Mb/s (0,7–1,2 GB), el compuesto, la fuente, los
cartones en qtrle y las listas en ProRes 4444. El fallo no dice «disco»:

- `componer` y `cartones`: ffmpeg «No space left on device» y, en el lower third,
  `OSError: [Errno 22] Invalid argument` al escribir al pipe.
- `mg_armar`: `saveProject` corta a los 30 s de aftr, y After Effects queda con un aviso modal
  «Error with file: …\DH_profe_mg.<pid>.<n>.aep». AE guarda en un temporal: el `.aep` bueno no se
  tocó, y el temporal truncado (126 KB) lo borró AE solo.
- **El aviso tapa el panel de aftr**: hasta cerrarlo, aftr responde «timed out». Ojo al cerrarlo
  con un clic: el centro del visor vacío de AE es el botón «New Composition», y un clic de más
  creó una «Comp 1» (se quitó con `deleteItem`).

Qué se hizo y qué queda:

- Los seis másters de la tanda pasaron a `D:\DAE\_masters_archivo\PRIORIDAD 2\CURSO - DERECHOS
  HUMANOS APLICADOS A LA FUNCION JUDICIAL\<pieza>\` (copia, tamaño igual, recién entonces se
  quita el de E:), con un `LEER - el master esta en D.txt` en cada `_master`. Liberó 5,45 GB.
- `dh_cadena.py` ahora mide E: antes de empezar (pide 3 GB) y corta con «LOTE FALLO» si falla
  `componer`, `titulo` o `cartones`. Antes solo cortaba si fallaba el gráfico, y una entrega
  podía armar la línea con el compuesto a medias.
- Los logs de la corrida fallida quedan como `*_fallo_disco_E.log`.

**Y la medida de 3 GB llega tarde** (cierre de la U5 de DH, 16 nov 2026). `dh_cadena` mide E:
después de esperar la fuente, y la copia de la fuente ya está en E:. Con 3,27 GB libres y una
fuente de 339 MB, cortó con «SIN ESPACIO EN E:». Lo que se mueve sin romper nada:

- **Los másters** de 32 Mb/s (`05 EXPORTS\_master`): nadie los referencia.
- **Las fuentes crudas** (`01 VIDEO\<NN>. Video ….mp4`) de las piezas ya entregadas: la línea de
  Resolve usa el compuesto, y la fuente solo la leen `componer` y `reimagen`. Van a
  `D:\DAE\_masters_archivo\…\<pieza>\fuente\` (`D:\DAE\_tmp\dh_profe\mover_fuentes.py`), con un
  `LEER - la fuente esta en D.txt`. Para recomponer una pieza hay que devolverla a su `01 VIDEO`.
- Los compuestos, cartones y listas **no**: están en las líneas, y moverlos obliga a `RelinkClips`.

**Una tira de cuadros no puede caer dentro de un corte.** `cuadro_de` lanza
`ValueError('… cae en un corte')` para un tiempo que el plan quitó, y la simulación (`dh_sim*.py`)
murió sin escribir la tira del plano cerrado. Las tiras se parten a los dos lados del corte:
`{'antes': (72.0, 73.95), 'cerrado': (74.7, 78.6)}`.

## Una entrega en Drive con el tamaño justo y la cola en ceros (cierre de la U5 de ED, 17 nov 2026)

«Se congela en el minuto 22:34.» El archivo local estaba sano: sin errores de decodificación y
40.892 cuadros. El de Drive tenía **el mismo tamaño** (1.186.766.456 bytes) y, desde el byte
930.086.912 (MiB 887, hacia el 22:16) hasta el final, solo ceros. El reproductor de Drive se
quedaba en el último cuadro bueno. La comprobación «tamaño en Drive = tamaño local» no lo ve.

La causa probable: la copia a `G:\My Drive\_MA subidas\` se hizo con `shutil.copy2`, que crea el
archivo con su tamaño final y lo va llenando, y Drive para escritorio lo leyó y lo subió antes de
que terminara. Es la pieza más grande de la tanda (1,13 GB).

**Cómo se verifica una entrega en Drive** (`herramientas/entrega/verificar_drive.py`):

1. Con el conector, `copy_file` del archivo entregado a una carpeta de «Mi unidad»
   (`_MA subidas/_verif entregas`), con el nombre `<clave>.mp4`. Es una copia en el servidor:
   son los bytes que guarda Drive, los que ve quien abre el enlace.
2. Drive para escritorio la baja a G:, y el script la compara por bloques de 1 MiB con la local.
   El md5 del conector no sirve: `get_file_metadata` no lo da.
3. La carpeta de copias, a la papelera.

Así se verificaron las 23 entregas de profe en Drive (11 de DH, 12 de ED): solo esa estaba mal.

**Cómo se sube** (`herramientas/entrega/subir_exclusivo.py`): `CreateFileW` con
`dwShareMode = 0` sobre un `<nombre>.parcial`, escritura en bloques de 8 MB, `FlushFileBuffers`,
y recién al cerrar `os.replace` al nombre final. Mientras se escribe, nadie lo puede abrir. Eso
evita el caso medido; lo que da la garantía es la verificación de arriba, que se hace en cada
entrega grande antes de pasar el enlace.
`exportar_y_subir.a_paso` ya copia así.

El archivo dañado se reemplaza por uno nuevo: el id cambia y el enlace viejo deja de servir, así
que hay que avisar a quien lo tenga. El dañado va a la papelera.

## Una lámina compartida dentro de un video de profe (cierre de la U1 de SRPA, 17 nov 2026)

En el cierre de la U1 de SRPA el profe comparte una diapositiva durante ocho minutos (5:45–13:49)
y él queda en una miniatura. La grabación de Teams trae un barrido a la entrada y un cubo 3D a
la salida.

- **El tramo de la lámina va a cuadro completo y sin gráficos.** La lámina ya es el gráfico, y es
  blanca: un cartón blanco encima no se lee. Los gráficos van solo en los tramos del profe, y la
  cobertura se cuenta sobre ese tiempo.
- **Las dos transiciones se tapan con la lámina quieta, nunca con la cara.** `CONGELA` acepta un
  tercer elemento: `(a, b, 'antes')` muestra sobre [a, b) el último cuadro ANTES de a (el modo de
  siempre muestra el de b). A la entrada, el tramo de la lámina empieza donde arranca el barrido y
  esos cuadros muestran la lámina ya limpia. A la salida, la lámina se queda quieta hasta que el
  profe está asentado, y él entra en vivo. Una lámina congelada no se nota; una cara congelada
  que habla, sí.
- **Los bordes se miden cuadro a cuadro**, con dos números por cuadro: la diferencia media contra
  el cuadro anterior y contra un cuadro limpio de cada lado (`D:\DAE\_tmp\sr_ta\prep1.py`). La
  transición es donde la primera sube; el lado limpio empieza donde la segunda toca fondo. Después
  del salto al profe la imagen tarda unos 10 cuadros en asentarse: el corte va después.
- **Teams deja una raya negra de 1 px en y=0** cuando comparte pantalla. A cuadro completo queda
  un filete oscuro arriba. La ventana de la lámina es 1276×718 desde (0, 2). Se vio en la tira
  del corte, con el compuesto ya hecho; se rehízo solo la imagen (`ic_pieza reimagen`).
- **Se comprueba en el compuesto**, no en el plan: una tira de 48 cuadros seguidos alrededor de
  cada corte (`ffmpeg … -vf scale=320:180,tile=8x6`).

## Cuánto de la caja ocupa la persona (`zona.py`, 17 nov 2026)

El perfil de la cabeza dice dónde está el borde, pero no cuándo una mano entra en la caja.
`D:\DAE\_tmp\sr_ta\zona.py` toma dos muestras por segundo, resta el fondo (la mediana) y cuenta
los píxeles de persona dentro de la caja de cartones (x 86–660, y 250–690 de salida, llevada a
la fuente con la ventana del plan). Devuelve los tramos en que pasa del 1,5 %. En el cierre de la
U1 de SRPA: 1 s en 17 min (950–951 s, una mano), y ahí no va ningún gráfico.

## Unir dos grabaciones sin recodificar el video (cierre de la U2 de SRPA, 17 nov 2026)

`ic_pieza` trabaja con una sola fuente. Dos partes de la misma cámara se unen así:

- **Video copiado** con el demuxer `concat`, con `duration <cuadros de A / fps>` después de la
  primera entrada. Sin eso el demuxer usa la duración del archivo, que es la del audio (31 ms más
  larga), y la parte B queda corrida respecto de la rejilla de cuadros.
- **Audio en PCM**, con el de A recortado a esa misma duración (`atrim=end=`) y pegado al de B.
- Contenedor `.mov`, que admite H.264 copiado con PCM y conserva la base de tiempo de la fuente.
- **Se verifica con `framemd5`** sobre los cuadros de la costura, del medio y del final, contra las
  fuentes. Tienen que ser idénticos.
- Segundo uso: cierre de la U2 de Derecho de petición (21 nov 2026), dos tomas H.264 Constrained Baseline a 30 cuadros
  (`duration 1782.166667` = 53.465 cuadros / 30). La unida es la `ORIGINAL` del plan y los tiempos de la toma 2 se
  suman a esa duración (`T2` en `plan_dpu2c.py`). Recodificar con NVENC desde ffmpeg no sirve en esta máquina (el
  controlador es más viejo que el que pide ffmpeg); la copia no lo necesita.

## Un canto pegado al borde no se borra con `delogo` solo

`delogo` interpola desde los píxeles que rodean el rectángulo, y pide al menos 1 px de margen. Si
el objeto llega al borde del cuadro (el canto de un tablero en x=0), ese margen ES el objeto y
queda una raya. Con `pad=iw+2:ih+2:2:2:color=<color de la pared>` antes y `crop=iw-2:ih-2:2:2`
después, el margen es pared. En el plan va en `PREFILTRO`, que `ic_pieza.escala` pone antes del
recorte.

## Cadena de profe para cualquier curso (17 nov 2026)

`herramientas/montaje/profe_cadena.py`, `profe_sim.py`, `profe_entrega.py` y
`herramientas/entrega/profe_subida.py` son las de Derechos humanos sin el curso fijo: el plan se
busca en `cursos/` por su nombre y los logs van a `<P.TMP>`. `profe_subida` copia con
`subir_exclusivo`.

- **Los pasos pesados de la pieza siguiente van con prioridad baja**
  (`creationflags=0x00000208 | 0x00004000`): `componer` y `cartones` de la pieza siguiente corren
  mientras la anterior arma en After Effects o rinde en Resolve, y aftr no cortó ni una vez.
  `mg_armar` va siempre con prioridad normal.
- **Un `Z('frase')` del spec toma la primera aparición.** En un video largo la misma frase sale
  varias veces («situación de vulnerabilidad», «el principio pedagógico»): `ajusta.py` avisa con
  «CORTO» y una duración negativa. Se arregla con `'N@frase'`.
- **`git stash -u` + `stash drop` en la nube se lleva lo que no se ha empujado**, carpetas nuevas
  incluidas. Antes de sincronizar, lo nuevo se copia fuera del repo o se empuja.

## El inventario de videos es el archivo de Sebastián

Desde el 17 nov de 2026, cualquier alta o cambio del inventario de SRPA, Ley 1826 y
Terminaciones anticipadas va en **su** hoja de cálculo, «Inventario_videos_17 NOV»
(`178QTUCm6c_LKF7iTm55WfaQp52fyv3xrWtuZgBpvFK0`), con su estructura y su estilo: pestañas
«Resumen» e «Inventario», las diez columnas de siempre y sus textos de estado. La que se generó
con `inventario.py` (`1BR4Zufg0CQMi0ZEfBW4aGYCTfRU45dff6i79tA36YtA`) ya no se toca.

Cómo se edita desde una sesión que no tiene el conector de Google Sheets (17 nov 2026):

- El navegador integrado no tiene la sesión de Google: abre la hoja en «Solo ver». Se edita con
  Claude in Chrome, que usa el Chrome de Sebastián.
- **Ir a una celda:** clic en el cuadro de nombres, escribir `Inventario!G5` y Enter. Después se
  escribe el valor y Enter.
- **El color del estado es formato fijo de la celda**, no formato condicional. Para llevar valor y
  color de la celda de arriba, `Ctrl+D`. Para traerlo de otra fila, `Ctrl+C` en el origen y
  `Ctrl+V` en el destino, **una sola vez por copia**: el segundo `Ctrl+V` pega el portapapeles del
  sistema (cayó en dos celdas un texto ajeno; se corrigió). Después de pegar, esperar un segundo
  antes de escribir encima.
- **Los enlaces** van como `=HYPERLINK("url";"nombre")`.
- **La celda de notas del Resumen (A21) tiene formato por partes** (títulos en rojo). No se
  reescribe: se cambia la frase con Buscar y reemplazar (`Ctrl+H`), que conserva el formato.
- Al final se lee el archivo con Drive (`read_file_content`) para comprobar los valores.

## El lower third se mide con el cargo de ESE profe

`LT = (px del nombre, ancho del cargo)` se había fijado en (40, 440) junto con la columna de 470.
Con un cargo de tres renglones (Terminaciones anticipadas) está bien; con el de Estanislao son
cinco y el último queda fuera del cuadro, porque el lower third arranca en y=870 y cada renglón
baja 37 px. Antes de rendir se cuentan los renglones del cargo con la fuente real: más de tres
no entran. La simulación (`profe_sim.py`) lo muestra en cuatro momentos.

## Un archivo puede traer dos piezas, y cortes secos que no se ven en el panel (U4 de SRPA, 17 nov 2026)

`SRPA_unidad_4_inicio_v2.mp4` se llamaba «inicio» y duraba 33 minutos: eran la bienvenida de la
unidad (1:57) y la clase entera, pegadas. Se supo al leer la transcripción completa, no por el
nombre ni por la hoja de cuadros (el profe, el fondo y la ropa son los mismos de principio a
fin). Quedó en dos piezas, como la unidad 3, que había llegado en dos archivos.

- **Antes de planear, se lee la transcripción entera** buscando dónde el profe vuelve a saludar
  o se despide: ahí cambia la pieza.
- **La frontera entre dos tomas se confirma en el panel DAE/Fiscalía**: su diferencia contra la
  mediana cambia de nivel de una toma a otra (2,5 → 0,8 → 0,4 en este archivo), aunque no haya
  transición.
- **Un corte seco de toma no mueve el panel.** El método del panel (U3 L4) encuentra cubos y
  negros, pero no los cortes secos con que quien editó la grabación quitó pausas. Esos se buscan
  como **picos aislados** de la diferencia entre cuadros: un cuadro por encima de 3,5 con la
  mediana de los diez anteriores y los diez siguientes por debajo de 1,2. Salieron cinco; cuatro
  se ven (diferencia 5,5–8,9) y uno no (3,5). Un gesto de manos da diferencias altas durante
  muchos cuadros seguidos y no pasa el filtro; igual se mira la tira de cada candidato.
- **Después de un corte seco que se ve, plano cerrado hasta el final de la frase**, también
  cuando el corte lo trae la fuente. El salto se lee como cambio de plano.
- **El plano cerrado se elige midiendo la cabeza en ese tramo**, no en el video entero: el tope
  (148–240 de la fuente según la toma), los bordes y dónde queda el mentón. Si la cabeza llega a
  la altura del panel, el plano cerrado tiene que traer el panel entero (acá, 960×540 desde
  (20, 34)); no hay ventana que lo deje afuera sin cortar la cabeza.

## Lo que no depende del compuesto corre mientras se compone (17 nov 2026)

Componer media hora de profe a 1080 tarda unos 30 minutos, y `profe_cadena` hace los pasos en
fila. Los cartones, el cartón de título y las listas de After Effects salen del plan, no del
compuesto. En el desarrollo de la U4 de SRPA se hicieron mientras `componer` seguía:

- `profe_cadena.py <plan> componer titulo cartones` con prioridad baja. Cuando ya está en el
  segundo ffmpeg (el que escribe el `.parcial`), se mata **solo el proceso de la cadena** (los dos
  PID: el lanzador del venv y el python real), no sus hijos: `ic_pieza componer` sigue solo,
  renombra el `.parcial` y termina.
- `D:\DAE\_tmp\sr_ta\cartones_solo.py <plan>` (título y cartones; log `<tmp>\cartones.log`, que
  termina en «CARTONES LISTOS») y `D:\DAE\_tmp\sr_ta\mg_solo.py <plan>` (After Effects; log
  `mg.log`, «MG LISTO»), los dos con prioridad normal. `mg_armar` armó las 21 listas en 147 s,
  sin un solo corte de aftr.
- Si se mata la cadena, el resumen de sonido de `componer` no queda en ningún log: se mide el
  compuesto después (`ebur128=peak=true`) y se cuentan sus cuadros con ffprobe.

## El inventario se edita con el conector de Sheets (17 nov 2026)

Reemplaza la edición por Chrome de la sección anterior. Con el conector de Google Sheets:

- **Una fila que cambia de estado:** `copyPaste` con `PASTE_FORMAT` desde las mismas columnas de
  una fila que ya está en ese estado (trae el relleno verde de «Entregado» y el formato del
  enlace) y después `update_formulas` con los valores. El enlace va como
  `=HYPERLINK("url";"nombre")`, con punto y coma: la hoja está en español.
- **Una fila nueva:** `insert_dimension` con `inheritFromBefore: true` debajo de la fila que se
  le parece, y lo mismo.
- **La nota del Resumen (A21) tiene tramos en rojo.** `update_values` los borra. Va con
  `updateCells`, `fields: "userEnteredValue,textFormatRuns"`: el texto nuevo y los mismos tramos
  con los índices corridos por lo que cambió de largo (se leen antes con `textFormatRuns`).
- Se verifica leyendo de vuelta con `includeGridData` (`formattedValue`, `hyperlink`,
  `backgroundColorStyle`, `textFormatRuns`), no por la respuesta de la escritura.

## Cambiar la ventana de un solo tramo sin recomponer todo (U4 de SRPA, 17 nov 2026)

El último plano cerrado del desarrollo de la U4 (99 cuadros) cortaba el mentón. Se vio en la tira
de 4 cuadros por segundo de la simulación, con el compuesto de 31 minutos ya hecho. `reimagen`
recodifica todo el video: unos 20 minutos. Se rehízo solo ese tramo, en 3:

1. Se mira si el compuesto tiene un **cuadro clave justo en el borde del tramo**
   (`ffprobe -show_entries packet=pts_time,flags`): x264 pone uno en cada cambio de plano, y un
   corte de toma con cambio de ventana lo es. Si no lo hay, no se puede: va `reimagen`.
2. Se codifican solo los cuadros del tramo desde la fuente, con la misma cadena de
   `ic_pieza componer` (`trim=start_frame/end_frame`, recorte, escala a 1080 con la matriz de la
   fuente, `-r 30 -c:v libx264 -crf 16 -preset fast`).
3. Lo anterior al borde se copia de la v1 sin recodificar (`-c:v copy -frames:v N`) y se pega con
   el demuxer `concat` (con `duration N/30` para la primera parte). El audio es el de la v1.
4. **Se verifica todo** (`D:\DAE\_tmp\sr_ta\cola_sr4d.py`): el mismo `extradata_hash` en las dos
   partes (SPS/PPS iguales; si difieren, no se pega), cuadros y duración iguales a la v1,
   `framemd5` igual a la v1 antes del empalme y a la cola suelta después, pts seguidos en el
   empalme, y una decodificación completa sin errores.

Vale para el último tramo o para uno del medio (tres partes). Si cambia la duración de algún
tramo no sirve: el audio de la v1 ya no calza.

**Y la lección de fondo:** la ventana de un plano cerrado se prueba con cuadros de todo el tramo,
incluido el último medio segundo, antes de componer. Acá se midió el tope de la cabeza y los
bordes, pero no el mentón, y el profe se inclina justo al final.

## Los videos de unidad se llaman INICIO y CIERRE (Sebastián, 17 nov 2026)

«Cambia el nombre a inicio, siempre serán inicio y cierre». La bienvenida de la U4 de SRPA se
había subido como `srpa - U4 - BIENVENIDA-v1.mp4`, siguiendo a las de la U1 y la U3, y se
renombró a `srpa - U4 - INICIO-v1.mp4` (el archivo en Drive conserva su id y su enlace; también
el archivo local, el máster y la línea de Resolve, con `timeline.SetName`). De acá en adelante:
`<curso> - U<n> - INICIO` y `<curso> - U<n> - CIERRE`, en el archivo y en la línea; la clase
completa de una unidad, cuando viene, sigue siendo `DESARROLLO`.

## Cortes de toma cuando el panel no los delata, y manos que no son cortes (U5 de SRPA, 17 nov 2026)

En la fuente de la U5 el panel DAE/Fiscalía mide lo mismo en todas las tomas (0,3–0,4 contra su
mediana): no hay escalones que confirmen un cambio de toma, como en la U4. Y el pico aislado de
la diferencia entre cuadros da 41 candidatos en 34 minutos. La mayoría no son cortes:

- **Gestos de manos.** El fondo virtual de Teams recorta mal las manos: aparecen y desaparecen
  de un cuadro al otro, y eso es un pico aislado.
- **Cuadros repetidos.** La grabación trae tramos con cuadros duplicados y después un salto: un
  movimiento rápido de cabeza se ve como un pico con los vecinos en cero.

Lo que los separó (`D:\DAE\_tmp\sr_ta\saltos2_u5.py`): la diferencia media de la **zona de la
persona** (x 200–600, y 60–360 a 640×360) entre el cuadro anterior y el del pico. El movimiento
natural da hasta 8; los cortes de toma claros, de 13 a 24. Entre 9 y 11 hay cortes chicos que
casi no desplazan la imagen: se dejan. Y siempre se miran en una tira (16 cuadros, de 2,5 s
antes a 1,5 s después): la búsqueda de bloque para medir el desplazamiento no sirvió, porque el
fondo quieto domina y da (0, 0) en todos.

Con muchos cortes en una clase:

- Después de cada corte claro, plano cerrado hasta la **pausa siguiente** (3 a 8 s), no hasta el
  final de la frase: hay frases de 40 s.
- La vuelta al plano abierto va en el **cuadro más silencioso de la pausa** (media de 5 cuadros
  del nivel de audio), o **en otro corte** si hay uno a pocos segundos: el cambio de ventana tapa
  también ese.
- La ventana del plano cerrado se elige con el tope de la cabeza de cada tramo
  (`cerrado_u5.py`). Con la cabeza baja (tope en y > 240 de la fuente) no entra la que deja el
  panel adentro: va la de (140, 146), sin el panel, y puede ir en todos.

## Antes de decir que el sonido está corrido, mirar la boca en una pausa de la misma toma

Antes de tres cortes de la U5 se ve al profe levantar el vaso de agua y taparse la boca un
segundo mientras se siguen oyendo palabras. Parecía un desfase de un segundo entre imagen y
sonido, o un corte con el audio y el video en sitios distintos.

No era. Se armó una tira de la boca, todos los cuadros, con el nivel de audio de cada cuadro
escrito encima (`boca2_u5.py`), en una pausa de la misma toma 15 s antes: la boca se cierra
cuando el audio calla y se abre cuando vuelve, al cuadro. En los cuadros del vaso la voz está
10 dB más baja: habla con el vaso delante de la boca.

- La correlación entre el movimiento de la zona de la boca y el nivel de audio (`boca_senal_u5.py`)
  sirve en tomas largas (pico cerca de 0) y **no** en tomas de menos de un minuto: ahí da
  cualquier cosa. La tira en una pausa es lo que decide.
- Scribe estira el final de la última palabra antes de un silencio: sus tiempos no prueban
  dónde termina el habla. El nivel de audio por cuadro, sí.
- Esos cuadros no se pueden quitar sin llevarse palabras. Se dejan, y se dice.

## Entrega provisional de una clase: sin gráficos en el cuerpo (Sebastián, 17 nov 2026)

«Por ahora solo hagamos intro y outro, placas de entrada y salida y títulos del profe,
provisionalmente, porque se trata de entregar rápido». Para una clase larga que hay que entregar
ya:

- El plan lleva en `ITEMS` solo el lower third. Los cortes, los congelados y los planos
  cerrados van igual: son del compuesto y no agregan tiempo.
- La cadena va sin After Effects: `profe_cadena.py <plan> componer titulo cartones`.
- Cuando se pidan los gráficos, se agregan a `ITEMS` y sale una v2 **sobre el mismo compuesto**:
  cartones, listas, línea y entrega, sin volver a componer.
- En el inventario la fila dice que es provisional.

## El nombre de un curso sale de su documento de diseño, no del nombre de la carpeta (Enfoque diferencial, 17 nov 2026)

Sebastián: «todos los videos de Enfoque diferencial el título está mal, deben decir únicamente
Enfoque diferencial; en este momento está apareciendo Enfoque diferencial en la práctica del
fiscal… quiero indagar por qué salió así».

- **De dónde salió.** De la carpeta del curso en Drive, que JP creó el 26 oct como «PRIORIDAD 2 -
  ENFOQUE DIFERENCIAL EN LA PRÁCTICA DEL FISCAL». Copia el nombre de la carpeta vecina,
  «PRIORIDAD 1 - JUSTICIA RESTAURATIVA EN LA PRÁCTICA DEL FISCAL», donde sí es el nombre del
  curso. El 3 nov ese nombre pasó a `guion_ed.CURSO` y a los README, y el 15 nov a
  `base_ed_profe.CURSO_LINEAS`, que es lo que pinta el cartón de título de los 12 videos de profe.
- **Lo que dice el documento.** El formato de diseño del curso (FGN-AP01-F-204,
  `07_09_2026 DISEÑO CURSO_ENFOQUE DIFERENCIAL`, en Drive): «Nombre del curso: ENFOQUE
  DIFERENCIAL».
- **Dónde aparecía.** Solo en el cartón de título de los 12 videos de profe, al principio y en el
  cierre. Los 5 casos animados llevan «Enfoque diferencial · Caso N» (`guion_ed.ANTE`): se miró
  el cartón de entrada y el de cierre de cada entrega.

**La regla.** El texto de un cartón de título se copia del campo «Nombre del curso» del formato
de diseño o de la ficha («1.1 Nombre del curso»), y se anota de dónde salió. El nombre de una
carpeta, de un archivo o de una hoja de seguimiento no es fuente: lo escribe quien organiza, no
quien diseña el curso. Lo mismo vale para los nombres de las unidades y las lecciones.

## Cambiar el cartón de título de entregas ya hechas: `retitular.py` (17 nov 2026)

El título va en dos sitios de la línea de un video de profe, con el mismo archivo: cuadros
194–408 (V2) y los 215 cuadros que siguen al cuerpo (V1). Para cambiarlo en 12 entregas (2 h
12 min de video) no hizo falta volver a rendir ni a codificar el cuerpo
(`herramientas/montaje/retitular.py`):

1. El cartón nuevo se rinde con **otro nombre** (`carton titulo <clave> v2.mp4`; `ic_pieza.py
   titulo`, seis a la vez: 2–4 min cada tanda).
2. En Resolve, `MediaPoolItem.ReplaceClip(ruta nueva)` sobre el medio del cartón viejo: los dos
   ítems de la línea cambian y todo lo demás queda igual (se comprueba el largo y las posiciones).
3. Se rinden en Resolve solo la **cabeza** (del 0 al primer cuadro clave desde el 409) y la
   **cola** (desde el último cuadro clave hasta el arranque del cierre), con `MarkIn`/`MarkOut` y
   los ajustes del máster, y se codifican con la receta de entrega.
4. El **cuerpo se copia** de la entrega vieja sin recodificar y las tres partes se pegan con el
   demuxer `concat` (`-auto_convert 0`); el audio es el de la entrega vieja, tal cual.
5. Se verifica todo: cuadros = línea, SPS/PPS iguales en las tres partes, el cuerpo idéntico
   **paquete a paquete** (`framemd5` en modo copia: tamaño y md5 de cada paquete, sin
   decodificar), pts seguidos y en la rejilla, audio idéntico (md5 de los paquetes),
   decodificación completa sin errores.

Lo que hubo que aprender:

- **Dónde hay cuadro clave.** x264 pone un IDR en el 409 y en el arranque del cierre porque son
  cambios de plano… salvo que caigan a menos de 24 cuadros del IDR anterior (`min-keyint=24`):
  ahí pone un cuadro I que no sirve para cortar. Pasó en 6 de 12, siempre en el arranque del
  cierre (el IDR quedó entre 5 y 16 cuadros antes). El empalme va entonces en el IDR anterior, y
  la parte nueva se lleva esos cuadros del cuerpo, rendidos de la línea.
- **El cuerpo copiado con `-ss` sale corrido un cuadro.** `-ss` tiene que ir un pelo después del
  IDR para que la búsqueda caiga en él, y esos 4 ms se redondean a un cuadro entero: el primer
  cuadro del cuerpo queda con pts negativo y choca con el último de la cabeza («non monotonically
  increasing dts» al decodificar). Se arregla con `-bsf:v setts=pts=PTS-STARTPTS:dts=DTS-STARTPTS`.
- **`concat` mete los SPS/PPS dentro de cada cuadro clave si no se le dice que no.** Por defecto
  (`auto_convert 1`) pasa el video por `h264_mp4toannexb` y cada cuadro clave del cuerpo crece 43
  bytes: se ve igual, pero el archivo ya no tiene la estructura de la entrega original. Con
  `-auto_convert 0` los paquetes salen idénticos. La primera pasada (6 entregas) se rehízo por
  esto; las copias quedaron en `05 EXPORTS\_descartes`.
- **Comparar el cuerpo decodificando es lento** (8 min para un video de 23): se comparan los
  paquetes, que tarda segundos y además habría pillado lo anterior desde el principio.
- **No lanzar un lote mientras se cambia la herramienta.** Un plan arrancó con la versión vieja
  del script un momento antes del `git pull` y falló la verificación: hubo que repetirlo.
- **Los ajustes de render parciales se devuelven en el acto** (`SelectAllFrames: True`), en un
  `finally`.
- La cabeza recodificada no sale idéntica a la vieja ni siquiera en el intro: cambian unos 20
  cuadros antes del título (el control de bitrate mira hacia adelante). No importa: es otra
  codificación de los mismos cuadros.

Sirve para cualquier cambio que toque solo el principio o el final de una entrega (título,
cierre, intro, outro). Si el cambio está en el cuerpo, va `reparchar.py` (la sección que sigue).

## El cartón lleva las palabras del profe, pero bien escritas; y cómo cambiar un cartón ya entregado: `reparchar.py` (17 nov 2026)

Sebastián, con los 12 videos de Enfoque diferencial entregados: «en uno de sus gráficos de texto,
en vez de "unas lentes" que diga "unos lentes", en masculino… revisa los guiones antes de entregar
el paquete entero». El profe dice «unas lentes» y el cartón lo copió.

**La regla de los textos.** «Verbatim» es no inventar ni resumir con otras palabras; no es copiar
lo que al hablar sale torcido. Antes de rendir, cada cartón se lee como texto escrito:

- concordancias y géneros («unos lentes», «dárseles… a los niños»), régimen («sin ningún tipo de»);
- mayúsculas de nombres propios e instituciones («la Constitución») y tildes de voces adaptadas
  («jóker»): la transcripción no las pone;
- **al acortar una enumeración no se le quita el sustantivo a un elemento**: «niños de brazos y
  usuarios con movilidad reducida» había quedado «niños de brazos y movilidad reducida»;
- lo que es elección del profe y no error (un término, «retroprocesos», «capacidades diferentes»)
  se deja y se le avisa a Sebastián en la entrega, en una lista corta.

La revisión se hace sobre **todos** los textos del plan de una vez (se vuelcan con `ast` a un solo
archivo: 410 gráficos de 12 planes se leen en diez minutos), no cartón por cartón cuando alguien
encuentra uno.

**Cómo se cambia un cartón del cuerpo sin rehacer el video** (`herramientas/montaje/reparchar.py`,
el `retitular.py` de los tramos de adentro):

1. En el plan: el texto corregido, `VERSIONES = {clave: 2}` y `VERSION` una más. `ic_pieza.py
   cartones <clave>` rinde «<PREFIJO>_<clave> v2.mov»; el viejo queda en disco.
2. `python reparchar.py <plan> <versión vieja> <versión nueva> <clave>…`: `ReplaceClip` en la
   línea, render de Resolve solo entre los cuadros clave que encierran el cartón (con `keyint=48`
   son 10 a 18 s), x264 con la receta de entrega, y el resto copiado de la entrega vieja.
3. Además de lo que verifica `retitular.py`, compara el tramo nuevo con la entrega vieja cuadro a
   cuadro: **fuera del cartón tiene que dar la misma imagen** (46 dB o más; el umbral es 38). Si
   baja, en la línea cambió algo más que el cartón.

Un video de 28 minutos tarda 2 a 3 minutos (casi todo, la verificación); los cinco, 15 minutos
con la subida. Rendirlos enteros habría sido más de una hora.

- El filtro `psnr` con `-frames:v N` escribe N+1 líneas en el archivo de estadísticas: se toman N.
- El archivo de estadísticas va con nombre relativo y `cwd`, para no escapar «D:» en el filtro.
- Solo cartones y lower thirds. Una lista de After Effects habría que rendirla con otro nombre y
  agregarla al script; las tres dudas que quedaron en listas se dejaron para que Sebastián decida.

## Una tanda de ocho videos de profe: medir primero, ordenar la cola y decir la hora de verdad (Terminaciones anticipadas, 17 nov 2026)

Inicio y cierre de las unidades 1 a 4 (55 minutos de video), en versión provisional. Salieron en
1 h 40 min desde que llegó el pedido; yo había dicho 70 a 80 minutos y hubo que corregir la hora
dos veces.

**Medir antes de copiar el plan de al lado.** Eran del mismo profe y del mismo curso que el inicio
y el cierre del curso, y aun así eran otra grabación: 1920×1080 en vez de 1280×720, BT.709 en vez
de BT.601, el profe mucho más cerca de la cámara.
- **La matriz de color se mide, no se supone.** Con un elemento de color conocido que esté en las
  dos fuentes (el rojo, el azul y el amarillo del panel DAE/Fiscalía): se lee la fuente nueva como
  601 y como 709 y se compara con un compuesto ya entregado. Aquí 709 daba el rojo a 2 niveles del
  de referencia y 601 a 19.
- **Una fuente que repite cuadros no sirve para buscar cortes por el pico aislado**: la
  diferencia entre cuadros alterna ceros y saltos de 5 a 9 todo el tiempo. Se mira el máximo (9,3,
  sin ningún 13) y las pausas de la transcripción.
- **Si el profe ocupa la columna de cartones, se dice en la entrega provisional**, no cuando pidan
  los gráficos.

**La máquina es un i7-4790S de cuatro núcleos.** Tiempos medidos con 1080p:
- compuesto (`ic_pieza componer`, x264 `fast` CRF 16): 13 a 18 min por video de 6 a 8 min, con
  tres a la vez; el cartón de título, 2 min;
- máster de Resolve: 1 a 2 min **si nada le quita el procesador**, 7 min compitiendo con tres ffmpeg;
- entrega x264 `slow`: 26 a 30 min por video, con dos a la vez y los compuestos corriendo;
  `medium`: 9 a 12,5 min, con el mismo PSNR (51,3–51,5 dB) y tamaños parecidos.

**La regla para dar la hora:** con esta máquina, una tanda de N minutos de video 1080p tarda de
reloj unas **1,5 × N** con `medium` y algo más de **2 × N** con `slow`, más 15 minutos de traer,
medir y planear (aquí: 55 min de video, 83 min de cadena con seis en `medium` y dos en `slow`). Se
dice eso al empezar, no «70 minutos» a ojo.

**Cómo se ordena la cola** (`D:\DAE\_tmp\ta_u\`, ver el README de `terminaciones-anticipadas/profe`):
- Resolve rinde de a uno y es el cuello de botella cuando compite: los ffmpeg van **por debajo de
  la prioridad normal** (`prioridad.py`, `SetPriorityClass` 0x4000 cada 15 s a los que aparezcan).
- Los compuestos, tres a la vez; la línea y el máster, en serie apenas está cada compuesto; la
  entrega x264, la hoja y la copia a Drive, dos a la vez apenas está cada máster. Se entrega y se
  manda el enlace **por unidad**, sin esperar a las ocho.
- **Antes de lanzar las ocho líneas se mira un cuadro con el lower third encima** (el cartón se
  rinde aparte en segundos y se compone sobre un cuadro de la fuente): un error ahí se repite ocho
  veces.

**Entrega provisional: `PRESET_ENTREGA = 'medium'` en el plan.** `mp4_entrega` lo lee (el plan
le llega por `DAE_PLAN`); sin esa línea usa `slow`, el de la receta. Solo cambia el preset: CRF 18,
High L4.0, keyint 48, Rec.709 y faststart quedan igual. Se le dice a Sebastián, y la v2 con
gráficos vuelve a `slow`.

**Si el puente con la máquina se cae a mitad de una tanda:** lo que se lanzó con `Popen` sigue
corriendo. Un solo reintento, se sigue con lo que se pueda desde la nube (planes, documentos) y se
vuelve a probar al terminar eso. No se relanza nada a ciegas.


## Cuando hay una hora de entrega: la entrega sale de Resolve por la placa de video (unidades de Bienes, 17 nov 2026)

Los ocho videos de unidad de Bienes (116 min de fuente, cuatro de 5 a 7 min y cuatro de 20 a 26) se
lanzaron a las 19:53 con la cadena de siempre. A las 21:20 Sebastián escribió «please hurry, we need to
have this by before 10 pm»; con x264 `medium` y el compuesto del último todavía al 25 %, el último cierre
salía a las 23:15. Lo que sirvió, en orden:

1. **Mirar dónde está el procesador.** Dos entregas x264 y un compuesto se repartían cuatro núcleos; el
   compuesto del último video, que es el camino largo (compuesto → línea → entrega → subida), avanzaba a
   un cuarto de su velocidad.
2. **Sacar la entrega del procesador.** Resolve rinde H.264 por la placa NVIDIA a unas 8 veces el tiempo
   real: un cierre de 24 min sale en 3 a 4 min. `cursos/bienes-proceso-penal/unidades/lote/urgente.py`
   rinde la línea directo a MP4 con `SetRenderSettings({'VideoQuality': kbps, …})`, le pone `faststart`
   con `-c copy`, cuenta los cuadros contra la línea y copia a Drive.
   - **`VideoQuality` no es la tasa real.** Pedido 16000 dio 13.985 kb/s; pedido 5720 dio 6.058. El guion
     calibra con dos pruebas de 20 s (`MarkIn`/`MarkOut`) y corrige. Los másters, pedidos a 80000, salen a
     unos 20.000 con un profe quieto.
   - **`h264_nvenc` de ffmpeg no abre en este equipo** (GTX 970, controlador 582.28: «Required: 13.1
     Found: 13.0»). No perder tiempo ahí: la placa se usa desde Resolve. `mp4_entrega` acepta el preset
     `nvenc`, pero hoy cae siempre a `veryfast`.
   - Un solo proceso le habla a Resolve. Antes de lanzar el guion urgente se mató `lote_entrega.py` (y las
     entregas x264 a medias, que dejan solo un `.parcial`) y se esperó a que terminara el máster en curso.
3. **Darle el procesador al que falta.** Con las entregas fuera, el compuesto del último pasó de 10 a
   55–85 MB/min y terminó en 18 min en lugar de 70.
4. **Subir pesa:** a 5 Mb/s los cuatro cierres son 3,5 GB; Drive subió cada uno en menos de 2 min.

Resultado: los cuatro cierres en Drive y verificados a las 21:47. Es una entrega **fuera de receta**
(H.264 NVIDIA en vez de x264 CRF 18): se le dijo a Sebastián en el momento y quedó escrito en el README
del curso. Los másters de 32 Mb/s se guardan igual, así que la entrega de receta se puede sacar después.

**Antes de prometer una hora** con videos largos: la regla de 1,5×N minutos (tanda de Terminaciones
anticipadas) vale para videos de 6 a 8 min; con cierres de 20 a 26 min en cola, el último tarda mucho más
porque su compuesto compite con las entregas de los anteriores. Si hay hora de entrega, preguntarla al
empezar y, si es justa, usar la vía de Resolve desde el principio.

**Fuentes que ya traen intro y outro.** Las de unidad de Bienes venían con la intro de la FGN (cuadros
0–277, sin sonido) y un outro pegados, a corte. Se ven en `panel fuera de sitio` del prep (al principio y
al final) y en la hoja de contactos. El plan toma solo el tramo del profe (`armar_unidad(u, pieza, k0,
k1)`), y `k1` no pasa del primer cuadro del outro aunque la última palabra quede a 0,07 s.

**El lower third puede ir en columna angosta**: nombre con salto de renglón en `PROFE`
(`'Sergio Andrés\nLópez Zamora'`), `LT = (px del nombre, ancho del cargo)` y `LT_TOP` (cima; el estándar
es 870). Antes de lanzar una tanda, `sim_todos.py` pone el lower third sobre dos cuadros de cada fuente en
una sola hoja: en Bienes mostró que con las medidas del curso el nombre cruzaba la cara en un video.


## Un avatar se recorta y va sobre el fondo de la DAE (Trata, videos de profe, 17–18 nov 2026)

Ocho de los once videos de profe de Trata son un avatar vertical (1080×1920, 25 fps) sobre una biblioteca
generada. Lo primero que se armó (recorte cuadrado sobre el mismo cuadro desenfocado) no era lo pedido.
Sebastián: «recortar el personaje y usar el fondo de las imágenes que ya hemos usado, específicamente las
que están los logos hacia la izquierda y que no tenga el logo Aprende con la DAE… iguales al resto de
videos de profe hablando a cámara». Sin marca de agua dentro del contenido.

- **Antes de componer una fuente que no es un profe en su fondo de siempre, se pregunta o se muestra un
  cuadro.** Los primeros compuestos se descartaron sin entregar nada.
- **`herramientas/video/recorta_persona.py`**: Robust Video Matting (resnet50, ONNX) por la placa de video
  con `onnxruntime-directml`, que corre en la GTX 970 sin CUDA. Compone la persona sobre el fondo y guarda
  también el mate (`…_mate.mp4`): cambiar de fondo después no obliga a recortar de nuevo. Los modelos están
  en `D:\DAE\_herramientas\matting` (instalación autorizada por Sebastián el 17 nov; no hay ningún otro
  modelo de recorte en el equipo).
- **Medido** (1080×1080, `--ratio 0.4`): 100–120 ms por cuadro; 5,2 cuadros/s uno solo y 4,3–5,0 cada uno
  con dos a la vez (placa al 50–65 %, 3,0–3,6 GB de los 4 GB de memoria con Resolve abierto; un tercero no
  se probó). Por procesador: 545 ms (resnet50) y 252 ms (mobilenetv3). Un video de 6:40 son 31 a 37 min;
  los ocho (71.545 cuadros, 47 min de fuente), de a dos, tardaron 2 h 16. Los bordes del pelo y las manos
  salen limpios; no hizo falta retocar ninguno.
- **Lo que el recorte no arregla:** cuando el avatar abre las manos, el borde de la fuente vertical se las
  corta, y sobre un fondo más ancho ese corte recto se ve. Es de la fuente; se le avisó a Sebastián.
- **Fondo:** `FONDO 4 V2.png` de su carpeta «FONDOS SIN APRENDE CON LA DAE» (el único con los logos a la
  izquierda). La persona va centrada en x=1250 y el lower third de columna angosta (`LT = (44, 560)`) entra
  a la izquierda sin tocarla.
- **`-shortest` corta el video:** el audio del avatar termina 0,8 s antes que la imagen, y con `-shortest`
  el recortado salía con 21 cuadros menos. Sin `-shortest`, y `recorta_lote.py` cuenta los cuadros contra
  la fuente.
- **Un vertical puede venir dentro de un cuadro horizontal** (la introducción de la U1: 1920×1080 con la
  imagen en las columnas 656–1263). Se mira un cuadro de cada fuente antes de fijar `RECORTE`.
- **El lote va por colas** (`cursos/prioridad-03/profe/lote/`): `recortes.txt` → `recorta_lote.py` (dos a
  la vez) → `cola.txt` → `lote_cadena.py` (compuestos) y `entrega_gpu.py` (línea, entrega por la placa y
  copia a Drive). Las colas se pueden alargar con el lote andando, y `estado.py` resume todo en una
  pantalla.

## El AAC de Resolve puede salir con cuadros rotos: un pico sobre 0 dBFS no es «audio fuerte»

El cierre de la U1 de Trata salió de Resolve con `Peak: 51.7` en la línea de sonido del log, y −13,8 LUFS
en vez de −16. Eran dos tramos de 20 ms a +35 y +52 dBFS (280,77 s y 313,77 s): al reproducir, dos
chasquidos a fondo de escala. Lo medido:

- El compuesto estaba limpio (−16,0 LUFS, −3,0 dBTP).
- **Es determinista:** tres renders de la misma línea dieron los mismos dos tramos, con los mismos valores.
  Rendir de nuevo no arregla nada.
- **Es el codificador AAC de Resolve:** el mismo render con audio PCM (`.mov`, `AudioCodec: 'lpcm'`,
  `AudioBitDepth: 24`) salió limpio en esos dos sitios.
- De las diecinueve entregas con AAC de Resolve de esa noche (ocho de Bienes, once de Trata) fue la única
  (`lote/pico_scan.py` busca muestras con |x| > 1 y dice dónde).

Qué hace ahora `entrega_gpu.py`: si el pico medido pasa de 0 dBFS, rinde otra vez a `.mov` con PCM y ffmpeg
copia el video y codifica el AAC (`-map 0:v:0 -map 0:a:0 -c:v copy -c:a aac -b:a 320k -movflags
+faststart`). Quedó en −16,0 LUFS y −3,0 dBTP, con el audio a 0,3 ms del compuesto (correlación cruzada).
Los renders rotos quedan en `05 EXPORTS\_rindiendo` como `.viejo`.

**La línea de sonido del log se lee en cada entrega.** El archivo roto llegó a copiarse a la carpeta de paso
de Drive porque el guion medía el sonido y no lo comparaba con nada. Un pico verdadero por encima de 0 dBFS
es un render roto: el compuesto llega con techo en −3 y el AAC de Resolve sobrepasa a lo sumo 2,5 dB.

## El «libre» de G: no es el cupo de Drive: es el disco C:

Dos veces en la noche se le dijo a Sebastián que su Drive estaba casi lleno (3,6 GB y después 1,4 GB libres
«de 215») y se le pidió vaciar la papelera. La primera vez la vació (más de 41 GB). **Estaba mal leído**: la
segunda vez se comprobó, y la primera casi seguro era lo mismo. Se le corrigió en cuanto se vio.
`shutil.disk_usage('G:/')` da como total el cupo de la cuenta (214,7 GB), pero el libre sigue al disco donde
Drive para escritorio guarda su caché. Pares medidos de C: libre / G: libre, con la papelera sin tocar:
1,45 / 1,38 · 4,6 / 4,40 · 2,63 / 2,50. Es C: menos unos 0,13 GB.

- **El cupo de Drive no se puede leer ni desde G: ni con el conector.** Se ve en drive.google.com (hay que
  tener sesión). Antes de decirle a Sebastián que el Drive está lleno, se comparan G: y C:.
- `entrega_gpu.subir` espera a que haya lugar según G: (o sea, según C:): eso sigue bien, porque la copia a
  la carpeta de paso pasa por la caché de C:. Lo que no entra queda en `pendientes.txt` y se reintenta.
- Lo que sí es cierto de la papelera de Drive: lo que está ahí sigue contando en el cupo y solo él la vacía.
  Las copias de paso van a la papelera al terminar y se le avisa cuánto es.

## Verificar una entrega en Drive: la caché decide el método

La verificación byte a byte vale si lo que se lee de G: viene del servidor y no de la caché local
(`AppData\Local\Google\DriveFS\<cuenta>\content_cache`, un archivo por ítem, con su tamaño exacto).

- La caché guarda los últimos archivos subidos o leídos, según el lugar que haya en C:. Mover un archivo
  fuera de «Mi unidad» no lo saca de la caché enseguida (uno seguía ahí 18 min después).
- **Si el archivo no está en la caché**, se compara directo desde `G:\My Drive\_MA subidas\`: la lectura lo
  baja del servidor (medido: 39–47 MB/s). `lote/verif_tr.py` mira antes que no haya en la caché un archivo
  de ese tamaño; si lo hay, dice «EN CACHE» y no verifica.
- **Si está en la caché**, copia de servidor (`copy_file` a una carpeta de «Mi unidad», mismo nombre) y
  `verif_tr.py copia=<carpeta>`: la copia tiene otro id y nunca estuvo en la caché.
- Siempre **antes** de mover la entrega a la carpeta compartida, que G: no ve.

## C: se llena por el archivo de paginación

Con dos recortes por la placa, Resolve y los ffmpeg a la vez, C: bajó de 6,5 a 1,4 GB libres. No era la
caché de Drive (0,4 GB) ni temporales nuestros: `pagefile.sys` había crecido a 25 GB (`wmic pagefile list`)
porque subió la memoria comprometida. Se mueve solo: al terminar un recorte C: volvió a 4,6 GB y al empezar
el siguiente bajó a 2,6. Lo otro grande de C: es de Sebastián: 13,8 GB de caché de disco de After Effects en
`%TEMP%\Adobe` (se vacía desde AE). En una tanda larga se mira C:, no solo D: y E:.


## Subtítulos de las entregas: se transcribe el video final, y leerlos encuentra defectos del video (18 nov 2026)

Esteban pidió un `.srt` por video, con los tiempos del video final, para montarlos en el aula. El método y el
criterio están en `herramientas/subtitulos/README.md` (`stt_final.py`, `srt_de_stt.py`, `stt_tramo.py`); cada curso
lleva su `subtitulos/manifiesto.json` y `correcciones.json`.

- **Se transcribe el archivo entregado, no la fuente.** La transcripción que se hizo al montar tiene los tiempos de
  la fuente; mapearlos a la línea (intro, cortes, tramos) es justo donde se cuelan los errores. Scribe sobre el
  video final cuesta unos 19 créditos por minuto y los tiempos salen bien por construcción. Sebastián: «con eso
  mantienen la línea de tiempo tal cual la tenemos».
- **Leer la transcripción entera es una revisión del video.** En tres videos de unidad de Terminaciones anticipadas
  entregados el día anterior aparecieron tomas repetidas sin cortar («ah, voy a volver a empezar», «volver a hacer
  ese párrafo»). Al montarlos se había anotado «una sola toma, leída de corrido; hay tropiezos sueltos que se
  dejaron» sin haber leído la transcripción completa de cada uno. **Antes de componer un video de profe se lee su
  transcripción buscando reinicios** («volver a empezar», «otra vez», «perdón», una frase que se repite a los pocos
  segundos, palabras cortadas con `--`): Scribe los marca.
- Un defecto así no se tapa en el subtítulo: el `.srt` sigue al video como está, se avisa, y la corrección es una
  entrega `-v2` con su `.srt` hecho de nuevo.
- **El nombre local de un export a mano puede no ser el de Drive** (`Terminaciones avanzadas - U1 - CASO 06 - V1.mov`
  en disco es `TA - U1 - CASO 06 - V1.mov` en Drive). Se empareja por tamaño en bytes, y el `.srt` lleva el nombre de
  Drive.
- `create_file` del conector de Drive sube un archivo del contenedor por referencia
  (`base64Content: sha256:<hash>:<ruta>`), sin pasar el contenido por la conversación, **solo si la ruta está bajo
  el directorio de trabajo** (`/home/claude/…`); desde `/mnt/user-data/outputs/` dice que no puede. Con
  `disableConversionToGoogleType: true` queda como `.srt` y no como documento.


## Cortar una repetición de una entrega sin reprocesarla: `recortar_entrega.py` (18 nov 2026)

Tres videos de unidad de Terminaciones anticipadas se entregaron con una toma repetida adentro. Sebastián: «haz los
cambios ya», «solo corta esas partes», «para evitar reprocesar todo». `reparchar.py` cambia cartones pero no acorta;
`herramientas/montaje/recortar_entrega.py` usa su mismo método para quitar un tramo:

    python recortar_entrega.py <plan> <versión vieja> <versión nueva> <a> <b> [lt=<clave>] [limpios=<n>]

- Quita los cuadros [a, b) de la línea de la entrega vieja. Copia sin tocar todo lo que queda fuera de los cuadros
  clave que rodean el corte (x264 con `keyint=48` y GOP cerrados) y **codifica solo esos segundos** con la receta de la
  entrega (mismo preset, mismo SPS/PPS: lo verifica). El sonido se rearma entero desde el compuesto (12 ms de fundido
  en el empalme). Medido: 1 min por video; de 10.929 cuadros se codificaron 240, 17 y 261.
- **`lt=<clave>`** para un corte que empieza donde empieza el clip: el lower third de la entrega vieja se va con lo
  cortado, y se vuelve a poner desde su `.mov` a la misma distancia del nuevo arranque.
- **`limpios=<n>`** cuando los primeros cuadros después del corte traen la cola del rótulo viejo: salen del compuesto.
- No toca Resolve: la línea y el compuesto siguen con la toma completa. El plan lo dice en «Versión 2» y lleva
  `CORTE_V2`; sus constantes siguen siendo las de la v1.
- `DAE_TMP_RECORTE=<carpeta>` manda los temporales a otro disco (D: tenía 2,4 GB; cada corte deja unos 400 MB, que
  quedan ahí: nada se borra).

Lo que falló en el camino, y por qué:

- **Con el profe quieto, cuadros vecinos del compuesto dan el mismo PSNR** (51,5 contra 51,4 dB): elegir «el más
  parecido» cuadro por cuadro saltaba hacia atrás. Lo que se ajusta es el paso entero. Medido: **el cuadro k de la
  línea (23,976) muestra el cuadro `piso((k − CLIP0) × 30 / 23,976)` del compuesto (30 c/s)**; con ese paso da 51,9 dB
  sobre 96 cuadros y con un cuarto de cuadro de desfase, 42.
- **Las marcas de color viajan con cada cuadro y le ganan a `-color_primaries`/`-color_trc`.** El compuesto solo
  declara la matriz; al entrar primero en un `concat`, el tramo salió sin primarios ni curva y su SPS ya no era el de
  lo copiado (la herramienta se detuvo ahí). Se fijan con `setparams` en el filtro.
- La prueba con una entrega sintética en el contenedor no vio ninguna de las dos: el profe sintético se movía y su
  compuesto traía todas las marcas. La prueba que vale es la del material real, y la herramienta falla sin escribir la
  entrega nueva.

El `.srt` de una `-v2` se hace transcribiendo el archivo nuevo, no editando el de la `-v1`; después se compara palabra
por palabra con el viejo (tiene que faltar solo lo cortado).


## Subtítulos de profes que hablan sin leer (SRPA, 18 nov 2026)

- Las reglas generales de limpieza están en `srt_de_stt.py` (`numeros`, `tropiezos`, `_tartamudeo`) y se describen en
  `herramientas/subtitulos/README.md`. **Cada regla nueva se prueba contra los `.srt` ya entregados**: tienen que salir
  idénticos, byte a byte (los 22 de Terminaciones anticipadas salen iguales).
- Quitar un «eh» deja una coma colgando («la justicia, restaurativa»): si la muletilla venía entre dos comas, se va
  la de antes, salvo tras un marcador («Así,») o en una lista.
- Scribe a veces pone el punto final varios segundos después de la palabra: el subtítulo no se estira hasta ahí.
- **Una búsqueda en Drive con `fullText` y sin `excludeContentSnippets` devuelve miles de caracteres por archivo.**
  Para comprobar una grafía: `title contains '<archivo>' and fullText contains '<palabra>'` con
  `excludeContentSnippets: true`; si el archivo aparece, la palabra está escrita así.
- Lo que el profe dice mal (un apellido cambiado) queda como lo dijo y se avisa. Una palabra que tres escuchas dan de
  tres maneras no se inventa; si el giro es evidente por el sonido y la frase, se pone y se dice cuál fue.
- **Scribe a veces estira una palabra sobre el silencio de antes** (la primera de un video, 17 s; un «¿Qué» de 8 s en
  medio de una clase): el subtítulo aparece antes de tiempo. `srt_de_stt.cues` no le cree al principio de una palabra
  de más de 3 s. El de la U3 de SRPA se subió de nuevo por esto: **antes de subir, se mira el subtítulo más largo**.
- **Un `diff` de dos `.srt` se pasa por `head`**: si cambia la cantidad de subtítulos, cambian todos los números.
- Los profes que leen (Bienes) dicen «repito» y releen la frase: nueve veces en cuatro videos entregados. Es el mismo
  defecto de Terminaciones anticipadas; la búsqueda de reinicios antes de componer incluye «repito».
- `recortar_entrega.py` solo sirve para entregas x264 (cuadro clave cada 48, GOP cerrados). Las que salieron de Resolve
  por la placa NVIDIA (perfil Main, clave cada 24) no se pueden cortar así: o el corte cae justo en dos cuadros clave, o
  la `-v2` sale del máster con los cortes hechos al codificar.


## Dos personas en videollamada: el rótulo va debajo de cada mosaico, en tinta (JR, cierre del curso, 18 nov 2026)

La fuente del cierre de Justicia restaurativa son dos coautores en mosaicos de 936×528 sobre un lienzo blanco. El
rótulo de la serie (texto blanco con sombra, abajo a la izquierda) no sirve: sobre el blanco no se lee y dentro del
mosaico tapa a la persona.

- `cartones_srpa.lower_third` acepta `(nombre, cargo, opciones)` con `x`, `top`, `ancho` y `tinta`. Con `tinta` el texto
  va en ese color y sin sombra. Cada rótulo va debajo de su mosaico (`x=40` y `x=1015`, `top=852`), en azul (22, 58, 79).
- **Se compone el rótulo sobre un cuadro de la fuente y se mira antes de armar la línea.** Con `ffmpeg overlay` y dos
  `-ss` el rótulo no apareció en la prueba (el archivo estaba bien); con PIL (`alpha_composite` del cuadro del `.mov`
  sobre el cuadro del compuesto) sí. Si la prueba sale vacía, primero se mide la caja del alfa del `.mov`.
- Los nombres salieron de la ficha del curso, y los dos se presentan en el video. Scribe oye «Espina» por «Ospina».
- Una pieza provisional no deja en E: lo que calcula `profe_cadena` para una con gráficos y máster (0,35 GB por minuto):
  con solo rótulos son 0,06. Y el render de Resolve va a `%TEMP%\dae_rindiendo` (C:) y la entrega se mueve a
  `05 EXPORTS` al final, cuando E: no tiene sitio para las dos cosas.

## Subtítulos: «no.» no es «número», y una regla no debe cruzar dos voces (18 nov 2026)

- `srt_de_stt.fin_oracion` tomaba «no.» por abreviatura y pegaba «La respuesta es no.» a la oración siguiente. Estaba
  en seis `.srt` ya entregados, que se subieron de nuevo. **Una lista de abreviaturas se prueba con las palabras
  comunes que se escriben igual.**
- Una regla de `correcciones.json` reparte el tiempo del tramo por letras y le da el hablante de su primera palabra:
  las reglas tocan lo mínimo, y las comillas de una cita dicha por otra voz se ponen palabra por palabra.
- Los casos se cotejan con el documento del profesor con un script que alinea palabras; a ojo se escapan las comillas.
- **Antes de responder «¿hay un caso que se llame X?» se busca el nombre en las transcripciones de las entregas**, no en
  la memoria: «Valentina» no está en ninguno de los 22 videos de Terminaciones anticipadas; es el caso 5 de Enfoque
  diferencial.
- Sebastián, 18 nov: los «repito» de los cierres de Bienes «no importan». No se rehacen.


## Los casos llevan nombre, no número (Sebastián, 18 nov 2026)

«En vez de que se llamen caso con algún número, que tengan el nombre del caso o alguna referencia importante», dentro de
la nomenclatura que ya tienen (curso o prioridad, unidad, versión): `TA - U4 - CASO TRES ESCENARIOS PROBATORIOS - V1`,
no `TA - U4 - CASO 01 - V1`. Vale para toda entrega nueva de un caso.

- El nombre es el del cartón de entrada. Si el documento no le pone nombre, una referencia corta a los hechos, y se le
  dice a Sebastián que la puso Claude.
- **Renombrar en Drive no cambia el id**: los enlaces pasados siguen sirviendo. Se renombra también el `.srt`, que tiene
  que llamarse igual que el video.
- **No se cambia el nombre del que sale la línea de Resolve o el archivo en disco** (`guion_lp.ENTREGA`): el nombre de
  Drive va aparte (`NOMBRE_DRIVE`, o `nombre` en el manifiesto de subtítulos).
- Lo que Sebastián ya renombró a mano se deja como lo puso.
- Para encontrarlos: `title contains 'CASO'` con `owner = 'me'` **y** con `owner != 'me'`; hay entregas subidas con otras
  cuentas suyas. Una búsqueda ancha de Drive devuelve casi mil caracteres por archivo: se acota por carpeta o por título.
- La lista de lo renombrado y de lo que no se tocó: `cursos/NOMBRES_DE_CASOS.md`.


## Dónde va cada caso: la hoja «Casos_ubicación en documentos» (18 nov 2026)

Sebastián pidió un Excel con todos los casos hechos y su lugar en los documentos de los cursos. Es la hoja de Google
`1_Xkp7w3beVXhViua8Ok0Vu3ID0qKU38BfKDzUUqufqM` (copia `.xlsx`: `1m9YER4yQbBRMmpmah-5t09x9Q_xfaQKA`): 94 piezas con
prioridad, curso, unidad, lección o sección, cómo lo llama el documento, página, párrafo, primeras y últimas palabras, y
enlace al documento, al documento de trabajo y a la entrega. **Un caso nuevo se entrega con su fila en esa hoja.** El
método y los guiones están en `herramientas/casos_en_documentos/README.md`. Lo que hay que saber antes de repetirlo:

- **«El documento del curso» es la ficha de la unidad** («Unidad n - Vaciado…», Word) o el PDF fechado del curso (JR,
  SRPA, Bienes, Delitos ambientales). El documento con los casos sueltos que arma la agencia es «el documento de trabajo».
- **`download_file_content` no trae el archivo a la conversación**: lo deja en `tool-results/` y contesta la ruta. Sirve
  para bajar Word y PDF enteros (tope 10 MB) y para exportar un Google Doc a PDF. Lo que pasa de 10 MB:
  `copy_file` a una carpeta propia → `G:\My Drive` → `D:\DAE\_tmp` → `device_stage_files`.
- **La página de un Word es aproximada**: no guarda páginas y usa una fuente que nadie tiene (Ancizar Sans). Se dice así
  en la hoja, y se dan siempre las primeras palabras del caso para buscarlas con Ctrl+F. La de un PDF es exacta.
- **Una búsqueda de Drive con muchos resultados no cuesta contexto** si pasa de unos 75 KB: se guarda en archivo. Las
  medianas (10 a 50 resultados) son las caras; un `or` con una palabra suelta («Ipanema») trae decenas de borradores.
- Cada fila se comprueba releyendo la página anotada (`pdftotext -f P -l P`): título, comienzo y final tienen que estar.

## Antes de armar una línea: que Resolve tenga abierto `DAE MASTER - CURSOS` (18 nov 2026)

La entrega del inicio de Justicia restaurativa falló en `ic_linea_externa` con `carpeta_pool`: `'NoneType' object has
no attribute 'GetSubFolderList'`. Resolve estaba en «Untitled Project» (se había cerrado y el puente lo volvió a
abrir vacío). Antes de lanzar `entrega_gpu.py` se mira `GetCurrentProject().GetName()`; si no es el proyecto, se abre
con `GetProjectManager().LoadProject('DAE MASTER - CURSOS')`. La llamada tarda más de un minuto y el puente corta a los
58 s, pero el proyecto queda abierto: se comprueba con otra llamada (267 líneas, página `edit`) y se relanza.
Volvió a pasar el 21 nov (cierres de la U2 y la U3 de Derecho de petición): la cadena compuso bien y la entrega se cayó
en las dos líneas. Con el proyecto cargado, `entrega_gpu.py` relanzado con la misma `cola.txt` rehízo solo rótulo, línea
y render.

## Videos de profe que no dan la calidad: avatar o restauración (informe del 19 nov 2026)

Sebastián preguntó cómo rehacer con IA los videos de un profe grabados en videollamada (Estándares interamericanos:
cara blanda, halo del fondo virtual). El informe está en el proyecto (`claude/Avatar_parlante_o_restauracion_19_noviembre.md`).
En corto: el equipo (GTX 970 de 4 GB, discos llenos) no corre nada de esto; conviene un avatar desde una imagen nítida
más el audio original antes que restaurar; lo más barato verificado es HeyGen Avatar IV desde foto (~0,80 USD/min) y,
abierto, InfiniteTalk en WaveSpeed (1,80–3,60 USD/min); Magnific sirve para la prueba (VEED Fabric, tope de 300 s,
260 créditos/s a 720p), no para el curso entero. Falta el prototipo de 30 s y la autorización escrita del profesor.

## Tres personas en videollamada: rótulos en dos renglones, y una fuente con 12 minutos de negro (JR, inicio de la U1, 18 nov 2026)

El inicio de la unidad 1 de Justicia restaurativa trae **tres** mosaicos sobre blanco (dos arriba, uno abajo al
centro), y el blanco libre queda solo abajo a los lados, a 500 px de ancho.

- **El rótulo de la serie no entra en un renglón**: el nombre se metía en el mosaico de abajo o se salía del cuadro
  por la derecha. Va con `ancho=430` y el nombre partido con `\n` en el plan (`plan_jru1i.py`). Se mide la caja en el
  alfa del `.mov` y se mira sobre el compuesto antes de rendir.
- **Para mirar un `.mov` qtrle con alfa sobre el compuesto:** `[1:v]select=eq(n\,90),format=rgba[o]` y
  `overlay=format=rgb`. Con `-ss` en la entrada del `.mov`, la hoja salió sin rótulo y parecía que no estaba.
- **La fuente dura 20 min y el contenido 8**: después del outro pegado sigue negro hasta el final. Se mide dónde
  termina el contenido (brillo por cuadro) antes de escribir `k1`; la duración del archivo no dice nada.
- **Un profesor que no está en la ficha:** el rótulo se le preguntó a Sebastián («Jhonatan Sandoval, sin cargo»). Esa
  grafía manda también en los subtítulos, donde Scribe escribe «Jonathan».
- **Dos transcripciones del mismo audio se corrigen entre sí.** La de la fuente y la de la entrega oyeron distinto en
  tres sitios («Mi edad empieza» / «La unidad empieza»); comparar las dos sale gratis, porque la de la fuente ya se
  hizo para planear.

## Un profe que se traba y pregunta algo fuera de la grabación: se corta el tramo entero (JR, cierre de la U1, 18 nov 2026)

En el cierre de la unidad 1, Martín arranca, dice «ahí me tosté, espérense», pregunta cómo llamar a quienes cursan,
Víctor le contesta y Martín vuelve a empezar. Son 46 s que no son del video.

- **Se encuentra leyendo la transcripción por hablante**, no buscando «repito»: es un cambio de hablante corto, fuera
  de tema, entre dos arranques de la misma persona.
- **El corte va de la pausa después de la última palabra buena a la pausa antes del arranque bueno** (aquí, 0,5 s
  después de «penal.» y 0,34 s antes de «Pues»), en cuadros de la fuente, con `TRAMOS` y un `cuadro()` propio en el
  plan. La transcripción de la entrega tiene que leer de corrido en la costura.
- **Una palabra que tres pasadas oyen distinto no se escribe.** Para una tercera escucha, los tramos dudosos van
  juntos en un WAV a 0,85× (`atempo`) y Scribe otra vez; si las tres difieren, el subtítulo deja fuera esa palabra y
  se anota en el README. A velocidad lenta Scribe también puede rellenar («su atención»): sirve para desempatar, no
  para decidir sola.
- **Una fuente del mismo editor puede no traer outro.** La del cierre de la U1 termina en la conversación; la del
  inicio traía outro y 12 min de negro. Se mide el brillo de todos los cuadros (`signalstats` a 160×90 con
  `metadata=print:file=yavg.txt`, corriendo con `cwd` en la carpeta: una ruta con `D:` rompe el filtro).
- **E: sin sitio:** las grabaciones originales de piezas ya entregadas pasan a `D:\DAE\_masters_archivo\…\fuente\`
  con md5 verificado y un `LEER` en su `01 VIDEO` (`D:\DAE\_tmp\jr_p\mover_fuentes_jr.py`). D: quedó en 0,8 GB: el
  próximo alivio tiene que salir de otro lado.

## Con E: y D: llenos, las grabaciones originales van a C: (18 nov 2026)

E: tenía 0,76 GB y D: 0,81 cuando llegó el inicio de la unidad 2 de Justicia restaurativa (20 min: pide 1,2 GB solo
para empezar). En E: hay 5,4 GB de grabaciones originales de piezas ya entregadas (`01 VIDEO`, lo que no es
`_compuesto`); la línea de Resolve no las usa.

- **Destino nuevo: `C:\DAE_masters_archivo\<misma ruta que en E:\DAE MASTER>\fuente\`**, con copia, md5 igual y recién
  entonces fuera de E:, y un `LEER - la fuente esta en C.txt` en el `01 VIDEO` de la pieza
  (`D:\DAE\_tmp\jr_p\prep2_jru2i.py` trae el movimiento). Hoy están ahí las del inicio y el cierre de la U1 de JR y
  la del cierre del curso de Bienes. Las del cierre y el inicio del curso de JR están en `D:\DAE\_masters_archivo`.
- **Para recomponer una pieza** (`componer`, `reimagen`) la grabación vuelve antes a su `01 VIDEO`.
- C: es el disco del sistema (12,4 GB libres de 255) y ahí rinde `entrega_gpu` (`%TEMP%\dae_rindiendo`): no se llena.
  Lo que hace falta es que Sebastián libere E: o D:.
- **`profe_cadena componer` pasa los primeros minutos sin escribir nada**: es la medida de sonoridad (2,5 min para 20
  min de video). El `.parcial` aparece después; no es un cuelgue.

## Revisar a fondo un video de profe: lo que la revisión corta no veía (JR, inicio de la U3, 18 nov 2026)

Sebastián pidió el inicio de la U3 «revisado muy bien». La revisión larga encontró tres cosas, dos de ellas en videos
ya entregados. Desde ahora van en toda pieza de profe:

- **Las filas del borde.** Las grabaciones de videollamada de Justicia restaurativa traen una raya negra arriba, de
  lado a lado: fila 0 en Y 16 y fila 1 en Y 125 sobre un lienzo en Y 234. Pasó a cuatro entregas (inicio del curso,
  inicio y cierre de la U1, inicio de la U2) sin que la hoja de revisión la mostrara: a 333 px de ancho una fila no
  existe. **Se miden las cuatro orillas de la fuente** (mínimo y máximo de las filas 0–3 y 1076–1079 y de las columnas
  0–3 y 1916–1919) **y las filas de arriba de la entrega** en el título, el cuerpo y el cierre. Se arregla en el plan:
  `PREFILTRO = 'drawbox=x=0:y=0:w=iw:h=2:color=0xFEFEFE:t=fill'` (0xFEFEFE da Y 234; `white` da 235).
- **La matriz de color de una fuente sin etiqueta se mide, no se supone.** La grabación sin pasar por el editor viene
  sin `color_space` y en BT.709; las que pasan por el editor llegan etiquetadas `smpte170m`. Se compara un color
  saturado que esté en las dos (el rojo, el azul y el amarillo del logo de la Fiscalía del fondo virtual) leyendo la
  nueva como 601 y como 709 contra una ya conocida. Con la matriz equivocada el rojo pasa de 234 a 217.
- **El nombre de la unidad se busca en todo el documento.** El PDF de Justicia restaurativa llama a la unidad 1
  «Fundamentos, principios y ejes…» en la estructura del curso y «Bases conceptuales y marco jurídico…» en «3.1 Nombre
  de la unidad». Si hay dos, se le dice a Sebastián cuál se puso y cuál es la otra.

Y cómo se comprueba que imagen y sonido siguen juntos después de un corte:

- **Sonido:** la transcripción de la entrega; cada palabra tiene que caer a ±0,1 s de `tiempo de la fuente − lo
  cortado + 409/23,976 − T0`.
- **Imagen:** se compara un cuadro de la entrega con los 13 cuadros de la fuente alrededor del esperado, por
  diferencia media en la **zona de la cara a resolución completa** (300×300). El mínimo es nítido (2,5 contra 8–16).
  Con el mosaico entero reducido a 226 px la curva sale plana y el mínimo no dice nada. Para sacar el cuadro `n`:
  `-ss n/fps − 0,01 -frames:v 1` (un `select=between(t,…)` después de `-ss` no casa nunca: `-ss` pone el tiempo en
  cero, y ffmpeg decodifica el resto del archivo).
- **Una tira de miniaturas no sirve para juzgar un gesto**: a 480 px creí ver unas manos levantadas que no estaban.
  Ante la duda, la zona a resolución completa o el número.

Otras dos cosas de esta pieza:

- **Antes de mover un archivo de `E:\DAE MASTER`, se mira si el media pool lo usa.** Recorrer el pool entero (5.880
  clips, `GetClipProperty('File Path')`) tarda 2,7 s desde `run_inline`; el resultado queda en
  `D:\DAE\_tmp\jr_p\pool_paths.json`.
- **Una cifra que no se oye se pasa varias veces por Scribe** (la frase aislada a 1,0×, 0,9×, 0,8×, 0,7× y 0,6×, más
  las dos pasadas enteras): «treinta y cinco por ciento» salió en cuatro de siete. Se escribe la lectura más repetida y
  **se le dice a Sebastián que es eso y no una certeza**.

## Inventario de videos de profe (18 nov 2026)

Hoja «Videos de profe_inventario y enlaces_18 NOV» (`13wsiWOYCbAxg4IPKHJq4r63uCkDWWaub1YKMP4h_xxM`), en la raíz del
Drive de Sebastián, junto a la de casos: una fila por video de profe con prioridad, curso, unidad, pieza, profesor,
estado, duración y enlaces al video, al `.srt` y a la carpeta. 85 entregados, 935 minutos. Se arma con
`herramientas/inventario_profe/` (ver su README). **Un video de profe nuevo se entrega con su fila en esa hoja**, igual
que un caso nuevo con la suya en la de casos.

## El informe lleva enlaces a las carpetas de Drive (19 nov 2026)

«El informe» es la pestaña Resumen de «Inventario_videos_17 NOV». Sebastián: «no agregaste los enlaces a
carpetas de Drive para ser encontrado fácilmente… en el informe».

- **Cada fila de producción lleva en la columna E una celda «Carpetas en Drive: curso · curso · …»**, con
  un enlace por curso a la carpeta donde quedaron los videos de esa fila. Va en la misma escritura que
  la fila: una producción sin enlaces a carpetas no está informada.
- **La lista «Carpetas en Drive»** (debajo de las filas de producción) lleva una fila por carpeta: curso
  en A y la carpeta enlazada en B. Un curso que entra al informe entra también ahí.
- **Varios enlaces en una celda:** `updateCells` con `userEnteredValue` y `textFormatRuns`; cada enlace
  es un tramo con `format.link.uri`, el azul (0,0667, 0,3333, 0,8) y `underline`, y después un tramo
  con `format: {}` para volver al texto normal. Los índices cuentan unidades UTF-16. Un tramo no puede
  empezar en el final del texto.
- **Un enlace en toda la celda, sin tocar el texto:** `repeatCell` con
  `userEnteredFormat.textFormat.link` y `fields` solo de ese formato.
- **`get_values` no muestra los enlaces.** Devuelve el texto. Para saber si una celda tiene enlace se
  lee con `includeGridData` y el campo `hyperlink` (o `textFormatRuns`). Di por hecho que la columna
  «Archivo en Drive» no tenía enlaces porque solo vi los nombres, y los tenía todos.
- Guion de referencia: `herramientas/inventario_profe/enlaces_informe.py` (arma las peticiones; se
  mandan con el conector de Sheets).

## Espacio en disco: qué se midió y qué se borró (19 nov 2026)

Sebastián pidió qué podía borrar, con D: en 0,8 GB libres. Se midieron C:, D: y E:
(`D:\DAE\_tmp\espacio\escanea.py` y `grupos.py`) y se cruzó con el pool de Resolve (5.886 clips).

- **Ningún clip del proyecto apunta a** `_masters_archivo`, `_tmp`, `_descartes` ni `_archivo_tmp`. Los
  compuestos de `01 VIDEO` sí están en el pool (D: 18,8 GB, E: 14 GB): no se tocan.
- **`D:\DAE\_masters_archivo` se vació el 19 nov, por decisión de Sebastián:** 105 .mp4, 132,2 GB
  (masters de 32 Mb/s, temporales archivados, descartes de Bienes y fuentes crudas). La lista está en
  `D:\DAE\_tmp\espacio\borrado_masters_archivo_19nov.txt`. Los `LEER` que mandaban a esa carpeta
  llevan una línea que lo dice. Un máster se vuelve a rendir desde la línea; una fuente se baja de Drive.
  `C:\DAE_masters_archivo` (fuentes, 4 GB) sigue.
- **Un borrado definitivo se confirma con él antes de hacerlo:** qué se borra, cuántos archivos, cuánto
  pesa y que no se puede deshacer, aunque lo haya pedido con la ruta exacta. La papelera no libera
  espacio (ver «Máster de paso»).
- **`D:\DAE\_tmp` (89 GB, casi todo .mp4) no se borra entera:** adentro están `sr\aplicar.py`,
  `sr\repo_in`, `subs\stt_final.py`, `jr_p\prep_fuente.py`, `jr_p\cola.txt` y `espacio\`. Los
  guiones, json y logs pesan 0,1 GB.
- Lo demás que quedó señalado como borrable, sin tocar: `_descartes` (E: 34,7 GB, D: 13,3 GB), la caché
  de render de Resolve en `D:\doc\project files\CacheClip` (14,3 GB, desactivada), los temporales de
  After Effects en `%LOCALAPPDATA%\Temp\Adobe` (13,7 GB), `E:\DAE MASTER\_archivo_tmp` (10 GB), 80
  versiones superadas en `05 EXPORTS` (9,1 GB) y `05 EXPORTS\_master` (4,2 GB). Con costo:
  `E:\DAE MASTER\respaldo de d` (27,9 GB; sus 1.326 archivos están en D: con el mismo tamaño) y las
  entregas vigentes de `05 EXPORTS` (42 GB; están en Drive).

## Una fuente puede llegar solo en audio (JR, inicio de la U4, 19 nov 2026)

El enlace que pasó Sebastián era «Justica restuaraativa-  Unidad 4 inicio.m4a»: AAC estéreo, 9:04, sin
pista de video. Es el audio suelto que Zoom deja junto al .mp4. **Antes de preparar una fuente se mira el
`mimeType` en Drive.** Sebastián decidió esperar el .mp4. La transcripción ya está
(`D:\DAE\_tmp\jr_p\jru4i\prep\turnos.txt`: Víctor presenta de 0:11 a 1:52, Jhonatan de 1:53 a 5:07,
Martín de 5:11 a 7:15 y cierra Víctor de 7:19 a 8:54) y el audio quedó en `UNIDAD 4\INICIO\01 VIDEO`.
En la carpeta VIDEOS del curso hay además dos grabaciones sin producir, que él todavía no pidió: el cierre
de la U2 (`1xFAc3bR31B6qONEN_aRL_TCvkAA7MpFX`) y el cierre de la U3 (`1gC1QllKcxwjnSVrsBI0sjmFu0HhTA4X0`).

## Una palabra que Scribe no resuelve: primero más contexto, después más lento (JR, cierre de la U4, 19 nov 2026)

Scribe oyó «Excelente insertación», que no es una palabra. Seis pasadas sobre recortes de 4 a 8 s (normal y al
75 %) repitieron «insertación», «insertaciones» o «investigaciones». La que acertó fue **el recorte largo, de diez
segundos, con la frase anterior y la siguiente**, a velocidad normal: «Gracias profesores… Excelente disertación, es
un análisis muy interesante». Un recorte corto le quita al modelo el contexto que necesita; frenarlo no se lo
devuelve. `stt_tramo.py <video> <desde> <hasta>` con al menos una frase entera a cada lado, y recién después las
velocidades. Lo que se decide así se anota en el README de subtítulos como decisión, no como certeza.

## Hacer sitio en E: moviendo a D: (19 nov 2026)

Con D: liberado, lo que no usa el pool y estorba en E: se mueve entero con
`robocopy <origen> <destino> /E /MOVE /R:1 /W:1 /NFL /NDL /NP /LOG:<log>` en segundo plano (20 GB en 9 min) y se
deja un `LEER` donde estaba. `E:\DAE MASTER\_archivo_tmp` está ahora en `D:\DAE\_movido_de_E\_archivo_tmp`.
`profe_cadena` pide 1 GB libre en E: para 11 minutos de video; una pieza deja en E: unos 0,9 GB (fuente,
compuesto, cartones y entrega).

## Cambiar el fondo virtual de un profe por el de la Fiscalía (Ley 1826, 19 nov 2026)

Sebastián pidió los diez videos de profe de la Ley 1826 (inicio y cierre del curso y de las cuatro unidades) con el
fondo virtual de biblioteca cambiado por el de la Fiscalía, y eligió el encuadre **«B: 10 % más chico»**. Todo está
en `cursos/ley_1826/profe/` (base, diez planes, `lote/` y su README).

- **`herramientas/video/recorta_cuadro.py`**: Robust Video Matting sobre el cuadro entero de la fuente (no un
  cuadrado), escalado 0,9 y apoyado abajo sobre `FONDO 4 V2.png`. Con escala 0,9 el borde izquierdo de la fuente
  queda en x=386 y el de arriba en y=108, **dentro** del cuadro.
- **Lo que se vio tarde: el borde recto.** Una mano que entra por la izquierda o la cabeza que se sale por arriba
  quedaban cortadas por una línea recta en medio del fondo (116 cuadros en nueve gestos en el inicio del curso, 48
  en el inicio de la U1). Se notó **después** de entregar la U1 INICIO: la revisión miraba el mate por saltos, no
  sus bordes. Arreglo: `--pluma-x 96 --pluma-y 48` (rampa smoothstep del alfa en los bordes del rectángulo que caen
  dentro del cuadro) y `lote/emplumar.py <clave>…` para los recortes ya hechos sin volver a correr el modelo. La U1
  INICIO salió de nuevo como -v2 (la v1, a la papelera). **Antes de entregar un recorte, mirar cuántos cuadros
  tocan los bordes del rectángulo que quedan dentro del cuadro** (`D:\DAE\_tmp\lp_p\rev_borde.py` y
  `rev_borde_arriba.py`).
- **`SUAVE = n` en un plan** (`ic_pieza.tramos_vf`): en un corte entre dos tramos con la misma ventana, el último
  cuadro del tramo anterior se funde en n cuadros sobre el siguiente; no cambia la cantidad de cuadros ni el audio.
  Lo llevan `plan_lpu2i` y `plan_lpu3c` (cortes de arranques en falso con el profe quieto).
- **El lote de recortes y la cadena no se conocen.** `lote_cadena.py` no espera a que exista el `_recortado.mp4`:
  un plan que entra en `cola.txt` antes de que termine su recorte falla. El que pone en la cola
  (`D:\DAE\_tmp\lp_p\orquesta_c.py`) espera la línea `RECORTE <clave> OK` de `recorta_lote.log`.
- **Ritmo con todo a la vez:** dos recortes (≈3 cuadros/s cada uno, 2,7–3,4), un compuesto y un emplumado se
  pelean la CPU; el compuesto del inicio del curso (6,9 min) tardó 30 min en vez de 9. La placa no pasa del 40 %.
  Para decir la hora de entrega, contar los cuadros que faltan recortar a 6 cuadros/s entre los dos.
- **C: y el archivo de paginación**, otra vez (ver «C: se llena por el archivo de paginación»): con dos recortes,
  Resolve y Chrome abierto C: llegó a 0,27 GB libres. Se movió a `D:\DAE\_movido_de_C\` (robocopy /MOVE, sin
  borrar nada) `C:\DAE_masters_archivo` (11 grabaciones originales, 3,7 GB; deja `LEER.txt`) y los temporales
  `%TEMP%\dae_recorte` y `dae_rindiendo`; los 11 `LEER - la fuente esta en C.txt` de E: dicen la ruta nueva
  (`D:\DAE\_movido_de_C\leer_actualizados.log`). La cadena va de a una (`lote_cadena.py 1`).

## Una regla de subtítulos con comillas va con « » (JR, cierre de la U3, 19 nov 2026)

`srt_de_stt` aplica primero las reglas de `_todos`, y en los cursos que las tienen una de ellas ya cambió las comillas
rectas de Scribe por « ». Una regla del video escrita sobre el texto crudo («decía: "Si tenemos…»)
no encuentra nada y no avisa. Se escribe con « », y después de regenerar se busca en el `.rev.txt` que cada regla
haya entrado. Otra cosa del mismo día: el arranque fallido que un profe pide cortar a mitad de una videollamada
(«voy a repetir ahí porque de pronto no queda bien el corte») se corta de silencio a silencio, eligiendo el par de
cuadros con menos diferencia de imagen, y con `SUAVE = 3` el salto de dos personas que se acomodan en la silla
se ve como una disolvencia corta. La medida de la fuente de un cierre de JR quedó en un solo guion:
`D:\DAE\_tmp\jr_p\prep2_cierre.py <clave> <carpeta> <archivo>` (brillo, bordes, mosaicos, turnos, pausas y empalmes).

## Una grabación de la que salen todas las piezas de un curso (Desaparición forzada, 19 nov 2026)

Llegó una sola grabación de 1 h 58 min en la que el profe lee, uno tras otro, los guiones de todos los videos del
curso y dice en voz alta dónde termina cada uno («Finaliza ese video y comienza el video de retroalimentación…»).
Salieron 17 piezas (`cursos/desaparicion_forzada/profe/`). Lo que sirvió:

- **El reparto sale del documento del curso, no de la grabación.** Se listan los videos que pide la ficha («Video de
  presentación», «de retroalimentación de evaluaciones», «de cierre» por unidad, más inicio y cierre del curso) y se
  busca cada uno en la transcripción entera. Si el profe grabó más guiones que casillas (tres retroalimentaciones por
  unidad contra un video), van juntos en la casilla que les corresponde, y se dice.
- **Las frases para marcar los videos se cortan en la palabra**, no en el párrafo: Scribe las pega a la última frase
  del guion («…Muchos éxitos y adelante. Finaliza ese video y comienza…») sin pausa larga entre medio. Cada pieza se
  define por su primera y su última palabra, buscadas en la lista de palabras, y los bordes van a la mitad del silencio
  (hasta 0,45 s antes y 0,7 s después).
- **Una toma repetida se elige leyendo las dos**: la primera del cierre de la U1 decía «artículo 166» (es el 165) y él
  mismo pidió repetir.
- **Los tiempos de Scribe pueden venir corridos 0,1–0,2 s.** En un corte sin silencio largo (una palabra en falso) el
  borde se busca en el RMS de 10 ms alrededor del tiempo de Scribe, y se elige el cuadro que cae adentro del silencio
  (los cortes se redondean al cuadro de 30).
- **`CUADRO_0`**: `ic_pieza` abría la fuente desde el principio en cada pieza y la decodificaba dos veces (medida de
  loudnorm y compuesto); la pieza del final tardaba 15 minutos solo en llegar a su tramo. Con `CUADRO_0` en el plan la
  fuente se abre con `-ss` en la mitad del cuadro anterior: el primer cuadro que sale es exactamente ese, y el audio se
  corta medio cuadro corrido. Verificado al cuadro (PSNR máximo en el cuadro esperado) y al milisegundo (correlación
  del audio: 0,00 ms).
- **`ic_pieza` no crea las carpetas de la pieza.** Sin `01 VIDEO`, ffmpeg falla al escribir el compuesto con el código
  4294967294 (−2, ENOENT), y falla *después* de la medida de loudnorm: diecisiete fallos en 15 minutos antes de verlo.
  El lote de un curso nuevo crea el árbol antes de lanzar nada.
- **Una fuente dentro de un lienzo blanco** (mismo editor que Justicia restaurativa): la imagen iba de x 16 a 1903 y de
  y 9 a 1070. La ventana toma solo la imagen (1888×1062 desde (16, 9)), que es 16:9, y se lleva el marco y la raya.
- **El nombre del profe se pregunta en cuanto se ve que no lo dice**, con los compuestos ya corriendo: el rótulo se
  rinde justo antes de armar la línea, así que la respuesta no demora nada.
- **Entregar y verificar de a una, mientras el lote sigue.** Cada entrega que aparece en `_MA subidas` se copia en una
  carpeta de verificación de Drive (`copy_file`, con la clave como nombre); un bucle en la máquina
  (`D:\DAE\_tmp\df_p\verif_loop.py`) espera a que Drive para escritorio la baje y la compara con la de `05 EXPORTS`; con
  el «OK» el video pasa a su carpeta (`update_file` con `parentId`) y la copia va a la papelera. Otro bucle
  (`stt_loop.py`) transcribe cada final apenas sale, así los subtítulos van detrás de cada video y no al final.
- **Las reglas de subtítulos de cada video se escriben contra el texto ya pasado por `_todos`**: después de la regla del
  curso, «mecanismo de búsqueda urgente» ya es «Mecanismo de Búsqueda Urgente», y una regla con «urgente valola--» no
  agarra nada sin avisar. Después de correr, buscar en el `.rev.txt` que cada arreglo esté (y que no quede «…»).
- **Una palabra que Scribe oye al revés se lee por el sentido y por lo que dura**, y se dice que es una lectura: «teoría del
  caso vulnerable» (1,1 s) es «invulnerable», como el profe dice en la retroalimentación de la misma unidad.
- El AAC de Resolve volvió a salir roto en una pieza larga (cierre del curso, 15 min: pico +28,8 dB); `entrega_gpu.py` lo
  detectó y la volvió a rendir con PCM + AAC de ffmpeg sin intervención.

## Grabaciones de Teams a 25 cuadros (Audiencias preliminares, 20 nov 2026)

Ocho grabaciones de Teams (introducción y recapitulación de cada unidad), 1280×720 a 25 fps, un solo profe que lee
rápido. Salieron en una noche (`cursos/audiencias_preliminares/profe/`). Lo que sirvió:

- **El rótulo de Teams con el nombre se deja fuera de la ventana**, no se tapa: está abajo a la izquierda (x 0–180,
  y 684–717); la ventana de 1200×675 desde (40, 0) es 16:9, se escala ×1,6 y lo deja afuera. Pero se lee: de ahí sale el
  nombre del rótulo (con la ficha), y se dice de dónde salió.
- **25 fps → la línea va a 23,976**: `FPS_FUENTE = 25` (los tramos se cuentan a 25) y `FPS_COMPUESTO = '24000/1001'`
  (el compuesto ya sale al ritmo de la línea; si no, Resolve lo estira o lo recorta).
- **Las grabaciones empiezan con silencio digital** y algunas terminan justo en la última palabra: el tramo final es la
  duración exacta del archivo, nunca `None` (`profe_cadena` usa `T1 - T0`).
- **La ficha puede estar copiada de otro curso.** Aquí repetía el nombre de la unidad 3 en la 4, decía «cinco unidades»
  (son cuatro) y hablaba de trata en la certificación. El cartón toma el nombre de la lista de contenidos del curso, y
  se avisa.
- **Un número que el profe dice mal** («artículo ciento cincuenta constitucional», tres veces, por el 250 que él mismo
  nombra en otras unidades) se confirma por lo que dura la palabra, el video queda como está y el subtítulo lleva el
  número correcto. Se dice en el informe.
- **Un profe que lee rápido** deja muchos subtítulos sobre 20 caracteres por segundo (hasta ~27): se acepta; partirlos
  más los deja de menos de un segundo.
- **El STT del final no es el de la fuente**: el mismo número sale distinto («dos cuarenta y dos B», «21 26», «dos 94»).
  Las reglas de números van genéricas en `_todos`/`_despues`, y al cambiarlas se regeneran los `.srt` ya subidos para
  confirmar que no cambiaron (mismo hash).

## Subtítulos de un avatar: los guiones no están en el documento (Trata, 20 nov 2026)

- Los once videos de profe de Trata (ocho del avatar, tres de una presentadora) se subtitularon en una tanda: Scribe
  sobre las once entregas tardó dos minutos. El cotejo palabra a palabra contra los documentos del curso coincidió en
  menos del 30 %: **los guiones del avatar se escribieron aparte**. El documento sirve para los nombres (personas,
  casos) y la forma de las normas, no para corregir frases.
- **Un pasaje dudoso se vuelve a transcribir suelto**, normal y al 75 % (`D:\DAE\_tmp\tr_s\clips.json`): donde la
  transcripción entera oyó «a quienes investigaban», el tramo corto dio «a quien es investigado». Si las tres versiones
  coinciden, va como se dice.
- **La transcripción de la entrega encuentra defectos de la fuente**: dos grabaciones de la presentadora terminan a
  mitad de frase. Se avisa a Sebastián y se anota en el inventario; el subtítulo termina en «…».

## Grabaciones con varias tomas: se compone con la toma buena y se cortan las charlas con el técnico (Derecho de petición, 20 nov 2026)

Siete grabaciones de videollamada de un solo profe (`cursos/derecho_peticion/profe/`): entre toma y toma le habla al
técnico («Suspendamos ahí, por favor, Camilo»), vuelve a empezar la frase y sigue. Salieron seis piezas.

- **La transcripción entera, en párrafos con la pausa al final de cada uno** (`leer.py`: corta en pausas de más de
  0,8 s y en cambio de hablante). Las tomas fallidas se ven solas: una frase que se traba, la orden al técnico y la
  misma frase otra vez. Se completa con una búsqueda de 5-gramas repetidos a menos de 90 s y de las palabras
  «perdón», «paremos», «suspendamos», «listo», el nombre del técnico y los cortes con «--».
- **Cuando hay dos archivos de la misma pieza** («TOMA 1» y «TOMA 2»), se leen los dos antes de mezclar: acá la toma 2
  traía el guion entero en tres tramos y la toma 1 era un primer intento; la pieza sale solo de la 2. Mezclar tomas
  de dos archivos cambia el encuadre (la cámara se había desconectado entre una y otra).
- **Bordes con RMS de 10 ms** (`D:\DAE\_tmp\dp_p\rms_bordes.py`, un JSON con borde y ventana entre palabras): Scribe
  mete a veces una «palabra» «.» suelta con tiempo propio que corre el borde calculado; y dos grabaciones traían ruido
  o una respiración antes de la primera palabra (hasta −21 dB): el borde se lleva a donde baja de −45 dB.
- **Seis cuadros de mezcla** (`SUAVE = 6`) entre tomas: con el profe en otra postura se lee como una disolvencia corta
  (tira de 24 cuadros con `profe_sim.py plan c1@t`).
- **Los tropiezos sueltos de una palabra sin disculpa quedan en el video** y salen del subtítulo.
- **El rótulo va abajo a la derecha** cuando las manos del profe entran en la esquina izquierda (hoja de 48 cuadros de
  todas las fuentes con las dos cajas dibujadas antes de elegir); `PROFE = (nombre, cargo, {'x': 1330})`.
- **Una carpeta de entrega que no existe se crea** con `create_file` y `application/vnd.google-apps.folder` dentro de la
  carpeta del curso (VIDEOS PROFE), y se dice.
- **Los `.srt` se suben por referencia desde el directorio de trabajo** (`/home/claude/...`): con una ruta en
  `/mnt/user-data/outputs/` (con o sin espacios) `create_file` responde «Nothing was uploaded».
- **`verificar_drive.py` con un mapa de piezas que todavía no están en disco se cae** en el primer `getsize`: para
  una tanda que va saliendo, el bucle `verif_loop.py` (espera la entrega local y la copia de Drive de cada una).
- **Un subtítulo que contradice al documento**: «el cumplimiento injustificado» (cuatro pasadas iguales) va como
  «incumplimiento», que es lo que dice el documento de la unidad; lo que no se puede confirmar se deja como se oye y se
  avisa (README de subtítulos del curso).
- **El rótulo va al empezar en todos los videos de un curso.** En el inicio del curso lo había puesto cuando el profe
  dice su nombre (1:31) y Sebastián no lo vio; salió una v2. Y `timeline.SetName` devuelve False (y no renombra) si el
  nombre lleva «:» o «,»: antes de lanzar `entrega_gpu` para una v2, leer de vuelta que la línea vieja cambió de
  nombre, porque si no la cadena encuentra la línea vieja y la rinde como v2 (pasó; se paró a tiempo).

## Una tanda de avatares que tiene que salir rápido (Trata, unidades 4 y 5, 21 nov 2026)

Seis videos (cuatro del avatar, que se recortan; dos de la presentadora, que no) con el lote de `cursos/prioridad-03/profe/lote/`.
Lo que decidió el tiempo:

- **El recorte es el cuello de botella y comparte procesador.** Dos a la vez van a 4,9 cuadros/s cada uno con la máquina libre;
  con `prep_tr2.py` midiendo cuadro a cuadro y dos compuestos andando bajaron a 1,7–2,9. Para un avatar o una fuente ya
  conocida no hace falta la medida cuadro a cuadro: basta la transcripción (`D:\DAE\_tmp\tr_p\stt_rapido.py`, solo Scribe),
  y el `prep` se para.
- **Lo que no se recorta va primero a la cola** (`cola.txt` a mano): los dos cierres estuvieron entregados y verificados
  mientras el primer par de avatares todavía se recortaba. Los planes de los avatares se pueden escribir con los tiempos
  provisionales y corregir antes de que termine su recorte (la cadena importa el plan cuando arranca).
- **La transcripción del video final puede perder una palabra** que la de la grabación sí tiene («Hagan una comprobación»):
  conviene cotejar los dos textos antes de dar el `.srt` por leído.
- **Un nombre largo en el rótulo va en dos renglones, y el rótulo sube** (cierres de Trata en v2, 21 nov 2026): con la
  presentadora centrada, «Mariana Lisbeth Rodríguez Muñoz» en un renglón le tocaba el pelo; en dos renglones el bloque bajaba
  hasta y=1090 (`ic_pieza … cartones` imprime «fondo»: tiene que quedar bajo 1080). `{'top': 820}` en el tercer elemento del
  rótulo lo deja en 1051. Se mira con `profe_sim.py` (necesita el `_lt01.mov` ya rendido).

## Un logo que el profe le puso a su video se tapa con su propio fondo (Delitos informáticos, 22 nov 2026)

El profe de Delitos informáticos entregó sus videos ya editados, con una placa «DAE | FISCALÍA» arriba a la derecha
junto con sus rótulos de sección. Sebastián: el logo no va; sus rótulos y láminas sí. `cursos/delitos_informaticos/profe/limpia_logo_di.py`:

- **Detrás de la placa está el fondo virtual de la videollamada, que es una foto quieta**: no se difumina; se pone
  encima el mismo fondo, sacado de la grabación (mediana de los cuadros del profe), con 8 px de borde suave, solo en los cuadros con la placa (más 4 a cada lado, que entra y
  sale con fundido) y solo sobre el profe (las láminas no se tocan). En YUV 4:2:0 por tubos, sin pasar por RGB; x264
  CRF 14, audio copiado.
- **La placa no está siempre en el mismo sitio** (x 998–1226 en unos rótulos, x 1016–1270 en otros, y de 17 a 88). La
  primera pasada usaba el rectángulo medido en un solo rótulo y dejaba el borde de la placa en los otros. Se vio en la
  tira de comprobación —un recorte de 640×200 de la esquina, **original arriba y limpio abajo**, en cada tramo con
  placa, al entrar, a la mitad y al salir— antes de rendir nada. Medir la placa en TODOS sus tramos antes de fijar el
  rectángulo.
- **El cartón propio del profe** (fondo azul noche, silencio digital) se quita con el borde del tramo: entra en el corte
  de escena o medio segundo antes de la primera palabra, lo que venga después.
- **La franja de Teams con el nombre del participante** (abajo a la izquierda, y 704–720) queda fuera de la ventana.

## Scribe puede estirar la última palabra sobre el outro (subtítulos de Medio ambiente, 22 nov 2026)

En la U3 L5 de Medio ambiente, Scribe le dio a «gracias.» un final 16 s más tarde (416,1 → 432,1 s), por encima del
outro, y `srt_de_stt.py` (que a una palabra de más de 3 s le pone el arranque en fin − 1) sacó el último subtítulo en
7:11, sobre la música. Se corrige el fin de esa palabra en el JSON antes de generar. Revisar siempre el tiempo del
último subtítulo contra donde empieza el outro.

- **La segunda escucha confirma lo que se dice, no lo que debería decirse.** En el cierre del curso de Bienes, las dos
  escuchas (normal y al 75 %) oyen «inmueble adquirido ilícitamente» donde el contexto pide «lícitamente»: el `.srt`
  deja lo que dice y queda anotado en el inventario para que lo decida Sebastián.
- **Un nombre de curso dicho a medias se corrige al nombre del curso** («delitos con el medio ambiente» → «contra»),
  como los títulos de unidad: es un nombre propio, no una cita.

## Sacar una frase de un video ya entregado sin rearmar la línea (Medio ambiente, 23 nov 2026)

«La profe debe presentarse una única vez»: se quitó su presentación de cinco introducciones de unidad ya entregadas.
No hizo falta tocar las líneas: se rinde cada línea tal cual a un máster de paso (H.264 NVIDIA 80000, PCM) y el corte
se hace sobre el máster con ffmpeg (`cursos/medio-ambiente/sin_presentacion/ma_corta.py`):

- se quitan cuadros enteros de la línea y el audio en las mismas muestras (1 cuadro = 2002 a 48 kHz), con bordes en
  silencio o en el valle antes de la palabra (RMS de 10 ms) y fundidos de 12 ms;
- después del corte, un plano cerrado (recorte de la salida, ×1,15, con el panel DAE/Fiscalía entero) hasta el
  primer cartón: ahí no hay gráficos y el salto no se ve;
- el `.srt` sale del ya revisado (`srt_sin_pres.py`): se quitan los subtítulos del corte, se corren los de después y
  se reescribe el que cruza. No hace falta otra transcripción.

Si un gráfico cruza el corte (el lower third del cierre del curso), eso no sirve: se rehace por la cadena del plan
(`CORTE` + `TRAMOS` + `a_salida`), y `ic_pieza.cartones` le da al ítem la duración que le queda en la salida.

## Antes de subir una versión corregida, compararla con la anterior cuadro a cuadro (caso 3 de Bienes, 23 nov 2026)

Para quitar «Tarea del foro» de un cartón del caso 3 de Bienes se duplicó la línea de octubre, se cambió ese cartón y
se rindió. La entrega pasó todo el chequeo (cuadros = línea, audio, sonoridad) y se subió. Después, la PSNR por cuadro
contra la entrega anterior mostró tres tramos distintos: el cartón (esperado) y el intro y el outro (3,7 dB). El clip
del intro había perdido su medio en el pool del caso y Resolve lo rendía como «Media Offline», en rojo y mudo. La
entrega mala se mandó a la papelera antes de pasar el enlace; se volvieron a poner el intro y el outro desde
` 00 COMUNES/INTRO` y se rindió otra vez.

- Una corrección sobre una línea vieja se compara con la entrega anterior **antes de subirla**: PSNR por cuadro a
  480×270 (`psnr=stats_file=`), y los tramos bajo 35 dB tienen que ser solo los que se cambiaron.
- `mp4_entrega.master` ahora se niega a rendir si un ítem con nombre de archivo no tiene medio en el pool o su ruta no
  existe («MEDIOS OFFLINE en la línea»).
- Un cartón rehecho se rinde primero con el texto viejo y se compara con el archivo viejo (`framemd5`): si sale
  idéntico, el código no cambió y el nuevo se verá igual que sus vecinos (`c5u3_foro_v2.py`).

El mismo día se hizo igual con los casos 1 y 2 de Bienes y con Los Chapulines (SRPA U5C1): `cartones/foros_v2.py`,
`montaje/foros_v2_lineas.py` y `montaje/foros_v2_cadena.py`. Las tres líneas también tenían el intro y el outro sin
medio. La comparación con la entrega anterior se hace también con el **audio** (nueva menos vieja, por segundo):

- Una diferencia no siempre es un error nuestro. La entrega vieja del C5U2 tenía dos microcortes de audio que la
  línea no tiene; la nueva sale bien.
- **La línea puede tener cambios que nunca se entregaron.** En U5C1 la entrega de revisión (13 oct, 19:54) es
  anterior a dos ajustes de la línea (planos de la avenida retocados en V4 y el cartón «Yos» más tarde) y al `.drt`
  de `10 TIMELINE SEBASTIAN` (20:22). Antes de rendir una corrección, se mira la fecha de la entrega contra la de
  los medios y del `.drt`, y si la línea cambió, se dice en la entrega.
- El limitador de `mp4_entrega` (pico del máster sobre −1 dBTP) deja el audio 48 muestras (1 ms) corrido respecto
  del máster: inaudible, pero la diferencia contra la entrega vieja ya no da cero.


## Revisión de los Genially (flujo «revisión», 24 nov 2026)

Cuando Sebastián dice «revisión» no es video: es contrastar DI, mapa de virtualización y Genially por diapositiva, y
devolver al virtualizador comentarios cortos (tono colombiano, informal, sin pinta de IA) con una miniatura SVG por
celda, en una **copia** del mapa con la hoja de la unidad duplicada. El diseño visual de los Genially está aprobado:
se propone distribución y recurso, nunca estilo. Para bloques de texto pesado vale proponer un botón a PDF
descargable. Todo el método, los recursos de Genially y las trampas del Excel están en `herramientas/revision/README.md`.
Tres reglas que pidió él: **una frase por celda**, en letra grande (20); **solo cambios en el Genially**: nunca «en
el mapa corregir…», el mapa se nombra solo para decir qué recurso pide; y **las palabras de Genially**: «animación»,
no «máquina de escribir».

## La voz de un profe se mide y se ecualiza a su medida (Delitos informáticos, 24 nov 2026)

Sebastián: «me recomendaron que mejorara los niveles y ecualización de estos videos». Las diez grabaciones del 24 nov
(otro coautor; nombre sin confirmar) llegaron a −38/−42 LUFS, con el ruido a 20 dB de la voz y el espectro cargado entre 125 y 630 Hz (+5 a +9 dB) y
apagado arriba de 2,5 kHz (−5 a −16), medido contra la voz media de referencia (LTASS de Byrne, 1994). La cadena fija
de los profes (`srpa_audio.CADENA`: +3 dB en 3 kHz, −2 en 250 Hz) dejaba el desvío en ~7 dB.

`herramientas/audio/voz_analisis.py` mide cada grabación (piso, voz, LTAS por tercios de octava solo en ventanas con
voz) y arma su cadena: paso alto 90 Hz, ganancia previa a −20 LUFS, `firequalizer` con el 70 % de la diferencia
(suavizada, topes −8/+7 dB), `afftdn` nr 6, expansor, compresor de picos, de-esser y limitador. El plan la lleva en
`AUDIO_CADENA` e `ic_pieza.base_audio` la pone **antes del dual-mono** (se midió en mono: la ganancia previa y los
umbrales cuentan con eso) y antes del loudnorm de siempre. Desvío: de 8–9 dB a 3–3,6; piso en las pausas, 2 a 9 dB
más abajo.

- **La reducción de ruido va después de la curva y suave.** `afftdn` nr 12 antes del ecualizador se comía los
  agudos, que en estas grabaciones están a solo 8–10 dB del ruido, y el desvío quedaba igual que sin ecualizar.
  `anlmdn` hizo lo mismo.
- **Se escucha antes de aplicar.** Va un A/B de 20 s (original nivelado / cadena) en mp3 y el espectro en png.

## Un rótulo con nombre sin confirmar no sale, y el nombre tampoco va en el archivo (Delitos informáticos, 24 nov 2026)

Sebastián dio un nombre para el rótulo y después: «por ahora no le pongamos rótulo al profesor porque no está
confirmado». Salió una versión nueva de las diez sin rótulo (`ROTULO_CONFIRMADO = False` en la base: `rotulo()` no
devuelve nada) y con «24NOV» en el nombre del archivo y de la carpeta de Drive en vez del apellido. Sacar el rótulo no
cambia el largo ni el sonido: el `.srt` es el mismo, con el nombre nuevo.

## Un titubeo pegado a la palabra: el borde del corte sale de la energía, no del STT

En el cierre de la U1, «pasamos a-- de comprender»: el STT de la fuente daba «pasamos» hasta 152,74 y el corte se
puso en 152,60, en un bache de −47 dB que parecía el hueco entre palabras. Era el medio de «pasamos»: la entrega decía
«pasa de comprender». Lo cazó Scribe sobre la entrega al hacer los subtítulos. Con dos sílabas pegadas, la energía en
ventanas de 5 ms y una escucha del compuesto (`stt_tramo.py` sobre el tramo del corte) antes de rendir. Y se leen las
transcripciones de las entregas buscando titubeos que el STT de la fuente juntó en una palabra («Buda-de Budapest»).

