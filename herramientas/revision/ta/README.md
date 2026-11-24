# Propuesta de diapositivas · Terminaciones anticipadas (24 nov 2026)

Para este curso no había un Genially que revisar: el pedido fue **diseñar cada diapositiva**
con la dirección creativa que ya está en marcha (la de Derecho de petición) y entregarla en el
Excel de revisión de siempre. Hojas «Unidad N - revisión», fila 1 = lecciones, columna A = número
de diapositiva, y una celda por diapositiva. La celda lleva el letrero **«Propuesta:» fuera de la
miniatura**, el título y un comentario corto solo si hace falta. Además va la hoja «Generales - revisión».

Sebastián pidió actuar «como un maestro pedagogo UI-UX senior», con la legibilidad y la navegación
del usuario final como criterio.

## Cómo se arma

1. **Texto del DI, no inventado.** `extrae.py` saca del PDF solo el cuerpo a 12 pt. Así quedan fuera
   las notas al pie (10 pt), los encabezados y los pies de página. El resultado es `cuerpo.txt`.
   - `parrafos.py` arma los párrafos.
   - En las lecciones, `T(renglón, n, desde)` toma el párrafo que empieza en ese renglón, o
     n de sus oraciones.
   - `B(a, b)` toma las viñetas entre dos renglones.
   - Las infografías del DI (preclusión; inadmisión, archivo o preclusión) se leyeron de la imagen
     y se pasaron tal cual.
2. **El motor de las mediaciones** (el `app.js` de Derecho de petición) arma las escenas:
   - `maqueta.py` publica cada lección en el espejo local:
     `…/terminaciones-anticipadas/unidad-0U/leccion-0L/index.html`, con `comun` copiado.
   - Se usan los recursos que el motor ya trae para Terminaciones: video en la escena,
     actividad V/F y de selección múltiple, listas de chequeo, mapas conceptuales con descarga,
     rutas, rejillas, comparadores y tarjetas que giran.
   - El tema del curso suma una regla: pantallas de lectura sin la columna de íconos decorativos.
3. **El marco Genially** se rehace en HTML (`render.py`, `MARCO`), medido sobre la captura
   real de Derecho de petición:
   - cabecera `#002F46` con los logos recortados de la captura (`logos.png`);
   - chip coral «Lección N», flechas y menú;
   - barra blanca con el bombillo y el título;
   - escena a 1029×414;
   - pie «Curso» y «Unidad N».

   Se rinde con Playwright a 1112×625 ×2.
4. **Casos y videos de profe con su cuadro real.** Se sacó un cuadro de cada video ya producido:
   - los nueve casos animados (cuadro 700);
   - el inicio y el cierre del curso y de cada unidad.

   Los cuadros están en `D:\DAE\_tmp\rev_ta\frames` y van como póster del video de la escena.
5. `excel_ta.py` arma el Excel. Usa miniaturas de 560×315 y Arial 20 en las celdas.

```
python3 render.py 1.1            # publica y rinde la lección (servidor del espejo en :8765)
python3 hoja.py L1.1 /tmp/hoja   # hojas de contacto para revisar
python3 excel_ta.py salida.xlsx
```

## Decisiones de diseño (las de «Generales»)

- **Una idea por pantalla.** El texto completo va en ventanas (tarjetas, recuadros, pasos), no
  en muros con scroll. Cuando algo no cupo, se partió en dos pantallas: el cuadro de las figuras
  de la causal primera, las metodologías y los criterios.
- **Índice por temas.** Cada lección tiene su pregunta orientadora y su «Ruta de la lección».
- **Citas de las cortes en cursiva**, separadas del texto del autor. Las reglas, alertas y
  elementos clave llevan sello.
- **Casos:**
  - Los casos animados van una vez, con las preguntas del DI al lado. Si no caben, va un máximo
    de cuatro o cinco y sin el párrafo de entrada.
  - El análisis va en la pantalla siguiente, con los tres momentos al mismo nivel.
  - Los ejemplos sin video llevan la situación en ventana y los tres momentos en la misma pantalla.
- **Actividades autocalificables**, con la explicación del DI y sin «objetivo de la actividad».
- **Evaluaciones de unidad** como cuestionarios del aula, no dentro del Genially.
- **Niveles del juego:** Observador, Investigador, Fiscal en formación y Referente en
  terminaciones. No se usa «Analista».

## Lo que el DI no trae y se señaló

- **Unidad 3:** el DI del 10 nov solo tiene la estructura de las lecciones, la guía A–F y la
  evaluación. Las pantallas quedan armadas con «Texto pendiente».
- **1.1:**
  - el análisis del ejemplo de la servidora pública repite el del ejemplo de Pedro;
  - el párrafo de la motivación está dos veces.
- **1.2:** la infografía dice «reviste las medidas de aseguramiento».
- **4.3:** la lista de errores frecuentes salta del 7 al 9.
- **Erratas de extracción** («proposiión», «argumenta ndo»…): se corrigen en `limpia()`.
