# Subtítulos (.srt) de las entregas

Pedido de Esteban (18 nov 2026): un archivo de subtítulos por video, `.srt` o `.vtt`, en español, **con los tiempos
del video final (intro incluida)**, con el mismo nombre del video y en la misma carpeta de Drive. Sebastián: «tomar
estas transcripciones de los videos que nosotros ya procesamos; con eso mantienen la línea de tiempo tal cual la
tenemos».

Por eso no se reusa la transcripción de la fuente que se hizo al montar: se transcribe **el archivo entregado**.

## Los pasos

1. **Manifiesto** del curso (`cursos/<curso>/subtitulos/manifiesto.json`): por video, `clave`, `video` (ruta local del
   archivo entregado), `nombre` (el del video en Drive, sin extensión), `carpeta` (id de la carpeta de Drive),
   `video_id` y `bytes`. Antes de transcribir se comprueba que el archivo local pesa lo mismo que el de Drive: los
   exports a mano tienen a veces otro nombre en disco.
2. **`stt_final.py <manifiesto> <salida>`** (en la máquina): Scribe por palabra sobre el audio del video final. El
   audio va a WAV mono de 16 kHz en memoria. Anota palabras, primera y última, ritmo (unas 2,3 palabras por segundo)
   y el consumo de la cuenta. Va a unas 30 veces el tiempo real.
3. **`srt_de_stt.py <manifiesto> <json de Scribe> <salida> [correcciones.json]`** (en cualquier lado): parte en
   subtítulos y escribe `<nombre>.srt` (UTF-8 sin BOM, CRLF), `<nombre>.vtt` y `<clave>.rev.txt` para revisar.
4. **Revisión**: se lee la transcripción entera de cada video. Los casos se cotejan con el texto del profesor
   (`fuentes/`). Lo dudoso se escucha otra vez con `stt_tramo.py <video> <desde> <hasta>` (el recorte, a velocidad
   normal y al 75 %). Las correcciones van a `correcciones.json` y se regenera.
5. **Entrega**: el `.srt` junto al video en disco y en la carpeta de Drive del video, con `create_file`
   (`contentMimeType: application/x-subrip`, `disableConversionToGoogleType: true`).

## Criterio de los subtítulos

- Dos renglones de hasta 42 caracteres; de 1,2 a 7 s; corte en el final de la oración o en una pausa; un renglón no
  termina en artículo, preposición o conjunción si se puede evitar; un número no se separa de su sustantivo ni de «%».
- **Transcripción limpia, no literal del tropiezo**: se quitan los arranques en falso cortos («deben repe--
  respetarse» → «deben respetarse») y los «eh». No se corrige la gramática ni lo que el profe dijo mal.
  `srt_de_stt.tropiezos` lo hace solo en los casos seguros: la palabra cortada que se retoma, la que repite las
  palabras de antes («de las af-- de las personas»), el artículo o la preposición sueltos cuando la oración sigue
  («También la-- el artículo» → «También el artículo»; «de la-- del principio» → «del principio»), el tartamudeo
  dentro de una palabra («compe-complejidad» → «complejidad»; los compuestos como «infancia-adolescencia» quedan) y la
  palabra función repetida («a, a la comunidad»). Lo demás queda con puntos suspensivos («es un pro… puede ser») y
  se resuelve a mano en `correcciones.json`, mirando el texto crudo (`.rev.txt` lista lo que queda con «…»).
- **Una toma repetida entera no se esconde**: si el video trae «voy a volver a empezar» y repite, el subtítulo lo
  sigue tal como suena, y se le avisa a Sebastián, porque el defecto es del video.
- Cifras en números cuando son de 11 para arriba, artículos de ley y porcentajes («artículo 348», «80 millones»,
  «50 %»): así están en los cartones. Scribe las da en letras, a veces. `srt_de_stt.numeros` las pasa solo
  («artículo ciento ochenta y siete» → «artículo 187», «Ley mil noventa y ocho de dos mil seis» → «Ley 1098 de
  2006», «ochenta por ciento» → «80 %»); un «cien» o un «mil» suelto se deja. Lo que el profe dice por partes
  («decreto veintisiete treinta y siete», «el tres veintiséis») va en `correcciones.json`.
- «la Fiscalía», con mayúscula. Una pregunta que sigue a dos puntos empieza con mayúscula.
- Las comillas del texto del profesor se respetan (“X”, “se robó su dinero”).

## Lo que se midió (Terminaciones anticipadas, 19 videos, 102 min)

- Scribe sobre el video final: sin una sola palabra jurídica mal oída en los casos (voz sintética) y una en los diez
  videos de profe («la tipicidad» por «la atipicidad»; en la segunda escucha del recorte salió bien).
- Tres dudas de sentido se escucharon otra vez y Scribe repitió lo mismo: se dejaron como las dijo el profe.
- **Consumo:** el contador de la cuenta de ElevenLabs (plan Creator, 243.910 por mes) pasó de 37.898 a 39.802 con
  los 102 min y las segundas escuchas: unos 19 créditos por minuto de audio. El contador se actualiza con retraso.
- `create_file` acepta una referencia `sha256:<hash>:<ruta>` en `base64Content` y sube el archivo sin pasar su
  contenido por la conversación, **pero solo desde el directorio de trabajo** (`/home/claude/...`); desde
  `/mnt/user-data/outputs/` responde que no puede. Y la ruta va sin espacios, por las dudas.

## Lo que se agregó con SRPA (15 videos, 3 h 43 min, profes que hablan sin leer)

- Con profes que improvisan hay cientos de tropiezos: las reglas de arriba salieron de ahí. Se probó que no cambian
  ni una letra de los 19 `.srt` ya entregados de Terminaciones anticipadas.
- **Dónde mirar cuando no se puede leer todo con el mismo cuidado:** las palabras con `logprob` bajo de Scribe (menos
  de −0,42: 157 en 29.000), las mayúsculas en medio de oración y las cifras (nombres, leyes, radicados), lo que
  queda con «…», y un corrector ortográfico (`pyspellchecker`) sobre el texto: así salieron «derecho blandoso, law»
  (soft law), «ultrabajarla» (ultrajarla), «vérase», «Paul Krimmel» (Polcrymed) y «tres de ponderación» (test).
- **Los nombres propios se cotejan contra lo que ya está escrito en pantalla** (los cartones del plan del video) y
  contra los documentos del curso en Drive, no contra el oído.
- Una segunda escucha (`stt_tramo.py`) no siempre resuelve: si tres pasadas dan tres cosas distintas, no se inventa.


## Lo que se agregó con Enfoque diferencial y Justicia restaurativa (18 videos, 3 h 20 min)

- **«no.» ya no es siempre una abreviatura.** `fin_oracion` la tomaba por «número» y no cortaba la oración: «La
  respuesta es no. En / este sistema procesal,» o un subtítulo que empezaba con «no.» de la oración anterior. Ahora
  `fin_oracion(t, sig)` recibe la palabra que sigue: «no.» es abreviatura solo si sigue una cifra. Probado contra todo
  lo entregado: cambian seis `.srt` (uno de Terminaciones anticipadas, cuatro de Bienes y uno de Derechos humanos), que
  se subieron de nuevo, y los otros 56 salen idénticos byte a byte.
- **Una regla de `correcciones.json` reparte el tiempo de todo el tramo que toca por cantidad de letras**, y le da a
  todo el tramo el hablante de la primera palabra. Por eso:
  - una regla que quita un tropiezo toca solo el tropiezo, no la oración («ley cinco ochenta y uno» → «Ley 581», no
    desde «la» hasta «de 2000»);
  - las comillas se ponen con reglas de una sola palabra, con miradas hacia atrás y adelante:
    `(?<=preguntó: )¿Pero` → `«¿Pero`, `amante\?(?= Dando)` → `amante?»,`. Una regla que cruzaba del narrador al
    personaje dejaba ««¿Pero» en el subtítulo del narrador;
  - las comillas rectas de Scribe pasan a «» con dos reglas generales de un solo carácter, no con `"([^"]+)"`.
- **Los casos animados se cotejan con el documento con un script**, no a ojo: se alinean las palabras del `.srt` y las
  del texto verbatim (`difflib` sobre las palabras sin tildes ni signos) y se listan las que difieren en la escritura.
  Así salieron los nombres mal oídos, las mayúsculas y todas las comillas del profesor.
- **Después de escribir las reglas se comprueba que cada una encontró su texto** (una regla que no coincide no avisa).
- **Un «perdón» o «discúlpenme» en medio de una palabra retomada se va con el tropiezo**; un «Perdón.» suelto, dicho
  entre dos oraciones, queda.
- **La segunda escucha vale más con el recorte corto** (5 a 10 s) y sirve para tres cosas distintas: confirmar lo que
  parece un error de Scribe y no lo es («menor e indígena», «en cuestión cuestiones»), recuperar una palabra que la
  primera pasada se comió («a la *aplicación* de la justicia restaurativa») y decidir entre dos lecturas. Cuando dos
  palabras suenan igual («la tensión» / «la atención») decide el sentido, y se anota.
- La hoja de revisión (`.rev.txt`) puede mostrar «0:60.0» por redondeo; el `.srt` y el `.vtt` no (se validan: segundos
  y minutos menores que 60, tiempos crecientes, de uno a dos renglones, 42 caracteres, CRLF, sin BOM).
