# Dónde está cada caso en el documento de su curso (18 nov 2026)

Sebastián: «haz un excel nuevo con todos los casos que hayamos hecho donde diga de qué curso, prioridad, de qué unidad es;
si tienes acceso a los documentos de los cursos como tal, en qué página exacta está y en qué párrafo; también puedes incluir
cómo es el ejercicio práctico o didáctico de tal lección, o como lo estén llamando en esos documentos. Necesitamos poder
ubicar fácilmente con relación a los documentos los casos y dónde van». Después: «incluye un enlace al documento en cada caso».

## Lo entregado

- Hoja de Google «Casos_ubicación en documentos_18 NOV»:
  https://docs.google.com/spreadsheets/d/1_Xkp7w3beVXhViua8Ok0Vu3ID0qKU38BfKDzUUqufqM/edit
- El mismo libro en Excel: https://drive.google.com/file/d/1m9YER4yQbBRMmpmah-5t09x9Q_xfaQKA/view
- Aquí, `casos_ubicacion.csv`: las mismas 94 filas, para leerlas sin abrir Drive.

94 piezas (75 videos y 19 láminas) de doce cursos. Cada fila: prioridad, curso, unidad, caso, pieza, lección o sección,
título o rótulo con que aparece, actividad como la llama el documento, momento o tipo de estrategia, recurso que pide el
documento, enlace al documento, página de inicio, párrafo en esa página, página final, primeras y últimas palabras, cómo
se midió la página, documento de trabajo de la agencia, archivo entregado y notas.

## Qué es «el documento del curso»

La ficha de cada unidad que la agencia tiene en Drive (Word: «Unidad n - Vaciado…» o «Unidad n - Curso…») o el PDF fechado
del curso cuando existe (Justicia restaurativa 10 nov, SRPA 11 nov, Bienes 12 nov, Delitos ambientales 6 nov). Se
encontraron con una sola búsqueda: `(title contains 'Curso' or title contains 'Ficha' or title contains 'Vaciado')` con tipo
Word, Google Docs o PDF y `owner != 'me'`. Los ids están en `docs_curso.json` y en `arma.py`.

## Cómo se hizo

1. **Bajar los documentos.** `mcp__Google_Drive__download_file_content` no devuelve el archivo en la conversación: lo
   guarda en `tool-results/` de la sesión y contesta con la ruta. `recoge.py` lee el transcript y arma el índice
   id → archivo. Tope de 10 MB por archivo; para uno mayor (la unidad 1 de Terminaciones anticipadas, 14 MB): `copy_file`
   a una carpeta propia de Drive, esperar a que aparezca en `G:\My Drive`, copiarlo a `D:\DAE\_tmp` y `device_stage_files`.
   Un Google Doc se baja como PDF con `exportMimeType: application/pdf` (el del curso de Terminaciones anticipadas es
   demasiado grande para exportar).
2. **Páginas.** Los PDF traen la página exacta. Los Word no guardan páginas (vienen de Google Docs: ni un
   `w:lastRenderedPageBreak`) y usan Ancizar Sans, que casi nadie tiene instalada; se convierten con
   `soffice --headless --convert-to pdf` y la página queda **aproximada**. El Word de la unidad 1 de Terminaciones
   anticipadas no cargaba en LibreOffice por `word/footnotes.xml`: se rehicieron sus 4 notas como texto simple.
3. **Párrafos.** `docx_parr.py` saca los párrafos reales del Word (cuerpo y celdas) y `ubica.carga_docx` le pone a cada
   uno su página buscando su comienzo en el texto del PDF convertido, en orden. `ubica.carga_pdf` arma los párrafos de un
   PDF con las líneas de `pdftotext -bbox-layout` (salto por interlineado o por renglón corto), sin el encabezado y el pie
   repetidos, sin números de página y sin los comentarios del margen. El trozo de un párrafo que viene de la página
   anterior cuenta como el primero de la página.
4. **Buscar cada caso.** `anclas.py` saca de los guiones (`herramientas/voz/textos/guion_*.py`) las primeras y las últimas
   palabras del texto narrado; `arma.py` las busca en el documento (o busca el rótulo con una expresión regular cuando el
   guion no es literal) y guarda título, página, párrafo, lección, sección, actividad, estrategia y fase más cercanas.
   `build.py` une eso con los datos de cada pieza y `hoja.py` escribe el libro (ajustes de redacción por caso en `OV`).
5. **Comprobación.** Para las 94 filas se releyó la página anotada con `pdftotext -f P -l P` y se comprobó que el título,
   las primeras palabras y las últimas están ahí: 0 diferencias.

Los guiones corren en el contenedor de la sesión con las rutas `/home/claude/casos/…`; para repetirlo hay que volver a
bajar los documentos (paso 1).

## Lo que apareció al ubicarlos

- Cuatro casos de SRPA no están en el PDF del curso del 11 de noviembre: Lenin, Operativo Las Lagañas, El accidente de
  los Miradores de La Calera y los hechos de Santiago y Valeria (solo se lo nombra en los talleres de la unidad 3).
- Disney abre la unidad 5 en ese PDF; el inventario del 17 de noviembre lo tenía en la unidad 4.
- El capítulo 1 del caso integrador de Desaparición forzada no está en el vaciado de la unidad 1; los capítulos 2 a 5 sí,
  al comienzo de cada unidad. No se encontró en Drive el video del capítulo 5.
- Los documentos de unidad de Derechos humanos no traen el guion de los videos: solo presentan la escena en «3.2
  Introducción a la unidad».
- El documento de Ley 1826 pide «video animado» para los cinco casos de la unidad 1; se entregaron láminas.
- Estándares interamericanos: entregas y carpeta dicen «Prioridad 3»; el vaciado de presentación, «Prioridad 1».
- Siguen con nombre de trabajo en Drive: `DA_V02_v1` a `DA_V06_v1`, `P3C3_RUTA_DEL_GOLFO_v1`,
  `P3C4_PUERTO_DE_SALIDA_v4_revisado`, `P3C5_CASO 05-REGISTROS_Y_CUENTAS_`, `U5C1_LOS_CHAPULINES_revision`.
