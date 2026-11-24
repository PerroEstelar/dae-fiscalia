# Un HTML autocontenido por lección (24 nov 2026)

Pedido de Sebastián: «un html por cada lección que sea completamente compatible y funcional con Genially para poderlo
subir a través de la plataforma de la Fiscalía». Eligió la lección autocontenida (todo adentro, sin depender de
Genially ni de GitHub) sobre un HTML que solo inserta el Genially.

```
python3 armar.py ta|dp [1.1 …]      ->  out/<curso>/TA_U1_L1.html …
python3 revisar_todo.py out/dp/*.html   recorre cada página con la flecha: errores de JS, iframes vacíos, imágenes rotas
python3 probar2.py <html> <pág. con descarga> <pág. con caso>   índice, instrucciones, descarga y audio del caso
```

## Cómo está hecho

- **El marco** sale del buffer del Genially nativo (`genially/lUL.json`): texto, SVG, imagen, grupo y contenido
  enriquecido, cada uno en su sitio sobre un lienzo de 1200 × 675 que se escala a la ventana. Las interactividades
  son las mismas (siguiente, anterior, ir a la diapositiva). Teclado: flechas, Inicio, Fin; `#p5` abre la página 5.
  - Genially dibuja el texto desde `Content` (ProseMirror), no desde `TextMessage`: el rótulo «Curso» traía
    «Soy un subtítulo…» en `TextMessage`.
  - Los SVG se recolorean por clase (`.color1`, `.color2`…) con `Colors`. El botón de Genially (dos medias lunas
    y el centro) necesita su CSS y `overflow` oculto: el rectángulo del centro es más ancho que su viewBox.
  - `Classes` (`text-align-center`) cuenta: el «Ver lección» va centrado.
- **Cada escena** es un iframe `srcdoc` con la página del motor en línea (CSS, fuentes, objetos.js y app.js
  parcheado). La escena va en `window.__Q` («?escena=N»), que el parche lee en lugar de `location.search`.
- **Los archivos** (ilustraciones, PDF, PNG, audios, videos, subtítulos, pósteres) van en base64 y se vuelven Blob
  URL cuando se piden: `app.js` pide cada ruta por `__R()`, que sube por los marcos hasta `window.__ovaR` del lector.
  La ventana del caso con audio va por `srcdoc` (`__F` / `__ovaDoc`): un documento Blob abierto desde `file://`
  tiene otro origen y no alcanza al lector.
- **Las plantillas** (motor, fin, instrucciones, caso) van en base64: un `</script>` o un `<!--` dentro de un
  `<script type="text/plain">` corta el bloque o lo deja abierto.
- El lector publica `window.ovaLeccion` (`pantallaCompleta`, `enPantallaCompleta`, `ventana`, `cerrarVentana`): el
  contrato que `app.js` e `instrucciones.html` ya traían para el SCORM dibujado desde Genially.
- Logos, portada, bombillo y las fuentes Montserrat Bold/ExtraBold se bajaron del CDN de Genially en la máquina de
  Sebastián (`D:\DAE\_tmp\sr\genially_assets`); las fuentes van recortadas a woff2.

## Pesos

- DP: 5,8 a 11,4 MB por lección (unos 5,5 MB son el motor y las páginas en línea).
- TA: 4,5 a 66 MB. Los videos van a 540p con H.264 CRF 30 (`D:\DAE\_tmp\sr\html_videos`), un 32 % menos que los
  del sitio; la 1.1 lleva cuatro videos.
- Probado en Chromium por `file://` y dentro de un iframe de otra página (como un recurso del aula).
