# Revisión de los Genially de la Fiscalía

Cuando Sebastián dice **«revisión»** es este flujo: contrastar el diseño instruccional (DI), el mapa de
virtualización y el Genially tal como está, diapositiva por diapositiva, con criterio pedagógico y de usuario final,
y devolverle al virtualizador comentarios cortos con una miniatura de cómo quedaría mejor. Piloto: Derecho de
petición, U1 L1.1 (24 nov 2026).

## Insumos

- `E:\DAE MASTER\<curso>\Revision\`: el DI (pdf), el mapa (pdf; en Derecho de petición es el mismo DI, md5
  idéntico) y el Excel de enlaces (hoja «Lecciones»: enlace de vista, de editor, aula, Revisado/Observaciones).
- El mapa editable está en Drive como `.xlsx` de un tercero, **solo lectura**. Se trabaja sobre una copia. Nunca se
  escribe el correo del dueño en ninguna parte.

## Cómo están armados los Genially

- Marco de Genially: cabecera con logos DAE y Fiscalía, chip «Lección N», flechas, menú; barra de título; pie con
  Curso y Unidad. Adentro, un iframe de 1113×448 con una escena HTML (GitHub Pages de estebanioi,
  `…/unidad-0N/leccion-0N/index.html?escena=N`).
- La escena sale de un JSON (`<script id="contenido">`): `scenes` con `layout` (`lamina`, `esquema`, `rejilla`,
  `compara`, `compacta`, `giro`), ventanas, acordeón, malla. Gamificación: puntos, nivel, exploración, «Clic para
  texto fijo» (el texto entra con máquina de escribir).
- **El diseño visual está aprobado** (paleta marino #002F46, teal #396B83, óxido #A75260, coral #EE616B, crema
  #F8F5C6, niebla #E5F1F1, hielo #F2F8F8; fuentes; logos). Se propone distribución y recurso, no estilo.

## Cómo se navega

- El Genially, en el navegador integrado a 1280×720, con la flecha siguiente.
- Las ventanas se prueban abriendo la escena suelta a 1113×448: dentro del iframe escalado los clics fallan.
- El JSON del Genially (`view.genially.com/api/view/<id>`) y el de la escena se bajan por el equipo, porque el proxy
  de la nube da 403 con genially.com y github.io. `resumen_genially.py` lo resume por diapositiva.

## Qué se mira en cada diapositiva

1. Fiel al DI: texto completo y títulos iguales.
2. Fiel al mapa: el recurso que pidió.
3. Jerarquía: ideas paralelas, secuencia o plazos que se pierden en un párrafo.
4. Legibilidad: si cabe sin scroll, el tamaño de letra, y si algo tapa el texto.
5. Errores visuales y fallas de navegación.
6. Incongruencias del propio DI: se avisan, no se corrigen («preguntarle al autor»).

## Recursos

- Genially nativo: ventana emergente, etiqueta (tooltip), ir a página, enlace (sirve para abrir o descargar un PDF)
  y botones. No trae pestañas: se simulan con botones.
- En las escenas HTML, los layouts que ya usa el motor.
- **Botón a PDF descargable** (pedido de Sebastián, 24 nov) para bloques de texto pesado que no dan para volverse
  interactivos sin forzarlos, y para guías de actividad (preguntas de reflexión con espacio para responder).

## Regla de texto (24 nov 2026)

Sebastián vio el piloto y pidió **una sola frase por celda** que resuma propuesta y errores; las miniaturas se
quedan. Donde no hay nada que cambiar: «Bien así.» Lo que se repite en todo el curso no se repite en cada celda:
va en la hoja «Generales - revisión», una frase por asunto.

## Cómo se hizo el curso completo (Derecho de petición, 16 lecciones)

1. `analisis/crawl_escenas.py` (en el equipo): lee los JSON de Genially, baja todas las escenas HTML con su css, js,
   fuentes e ilustraciones (`unidad-0N/comun/ilustraciones-tutela/`) y deja un zip.
2. En la nube, servidor local sobre ese espejo y `analisis/render_escenas.py`: cada escena visible a 1113×448 con
   texto fijo, captura, palabras, ítems y si pide scroll → `escenas.json`. `hoja_leccion.py` arma la hoja de
   contacto de cada lección para mirarla de una.
3. `analisis/cobertura_di.py` + `huecos_por_seccion.py`: frases del DI (cortado antes de «Recursos académicos»)
   que no aparecen en las escenas, agrupadas por sección. Así salieron las secciones que faltan y los textos de
   una versión anterior del DI. `ver.py` muestra DI y escena lado a lado.
4. Comentarios y miniaturas en `dp/revision_dp.json` (las miniaturas por plantilla: `plantillas.py`), y
   `mapa_revision.py` arma el Excel con las cuatro hojas de revisión y la de generales.

Los scripts de `analisis/` tienen rutas de la sesión (`/tmp/claude-0/rev/…`); se ajustan para el próximo curso.

## Salida

La salida es una copia del mapa con la hoja de la unidad duplicada, «Unidad N - revisión», con pestaña coral.

- **La grilla queda igual.** La fila 1 lleva los títulos de lección y la columna A el número de diapositiva.
- **Las celdas de contenido se vacían.** En su lugar va el comentario, con la miniatura en la misma celda: el texto
  arriba y la miniatura pegada al fondo.
- **Debajo de la grilla van dos filas más:** Generales y Convenciones.
- **Las etiquetas son:**
  - BIEN
  - CAMBIAR / AJUSTE
  - OJO / ERROR
  - IDEA / OPCIÓN
  - MAPA, que corrige el propio mapa.
- **El tono:** frases cortas, español claro con un toque colombiano, informal. Nada de emojis ni guiones largos;
  no tiene que parecer hecho por IA.
- **Las miniaturas:**
  - son SVG de 400×170 con la paleta del curso y la etiqueta PROPUESTA;
  - se rinden a PNG ×2 para incrustarlas;
  - se guardan junto al xlsx en `Revision\miniaturas U<n> L<n.n>\`.

```
python3 dp_u1l1/miniaturas.py svg/
python3 render_svg.py svg/ png/ 2
python3 mapa_revision.py mapa.xlsx dp_u1l1/comentarios.json png/ salida.xlsx
```

## Detalles que costaron

- **El texto enriquecido no conservaba su formato.** Este openpyxl guarda todo el texto como `inlineStr`, y
  LibreOffice ignora la negrita y el color en ese formato. `mapa_revision.py` pasa todo a `sharedStrings`, que leen
  bien Excel, Sheets y LibreOffice.
- **El alto de fila no se puede medir.** Se usa una estimación conservadora (56 caracteres por línea, Arial 9). La
  miniatura va anclada al fondo de la celda, así que si sobra alto queda aire y el texto no se tapa.
- **La verificación es visual.** Se convierte la copia a PDF con LibreOffice, con las demás hojas ocultas, y se mira
  página por página.

## Hecho

- **Derecho de petición, v3 (24 nov 2026):** letra de 9,5 a 11 («está muy chiquita»), nota gris en las celdas sin
  diapositiva en el mapa («No hay diapositiva para esta fila en el mapa»; no es que falten por virtualizar) y una
  segunda pasada pedagógica a U3–U4, que tenían muchos «Bien así» por fidelidad. Drive:
  [VIRTUALIZACIÓN DERECHO DE PETICIÓN - revisión v3.xlsx](https://drive.google.com/file/d/1NULmzPHXqlpONU9jf8oTZnsazoC4POBa/view);
  la v2 quedó en `_anteriores`.
- **Derecho de petición, curso completo (v2, 24 nov 2026):** 16 lecciones, una frase por celda, 55 miniaturas
  nuevas + las 12 del piloto, hoja de generales. Drive:
  [VIRTUALIZACIÓN DERECHO DE PETICIÓN - revisión v2.xlsx](https://drive.google.com/file/d/1Mmrp7AEnJ4kqazIQpNPGW1674degAJmu/view);
  local en `Revision\` con `miniaturas v2\`. El piloto quedó en `_anteriores` (Drive y disco).
- **Derecho de petición, U1 L1.1 (piloto, 24 nov 2026, superado por la v2):**
  - 11 diapositivas, más los generales;
  - Drive: «Revisión Genially · Derecho de petición» →
    [VIRTUALIZACIÓN DERECHO DE PETICIÓN - revisión U1 L1.1.xlsx](https://drive.google.com/file/d/1FxhTO7MIQkl_-cRKab4fmaYelv4Zdq3z/view);
  - copia local en `E:\DAE MASTER\CURSO DERECHOS DE PETICION\Revision\`.
