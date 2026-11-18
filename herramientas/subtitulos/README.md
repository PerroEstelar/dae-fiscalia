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
- **Una toma repetida entera no se esconde**: si el video trae «voy a volver a empezar» y repite, el subtítulo lo
  sigue tal como suena, y se le avisa a Sebastián, porque el defecto es del video.
- Cifras en números cuando son de 11 para arriba, artículos de ley y porcentajes («artículo 348», «80 millones»,
  «50 %»): así están en los cartones. Scribe las da en letras.
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
