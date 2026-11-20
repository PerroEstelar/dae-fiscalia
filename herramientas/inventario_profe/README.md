# Inventario de videos de profe a cámara (18 nov 2026)

Pedido de Sebastián: «¿puedes hacer un inventario de videos de profe hablando a cámara y sus enlaces? De qué prioridad,
de qué curso, de qué profe es y qué unidad, y lo que veas pertinente».

**La hoja:** «Videos de profe_inventario y enlaces_18 NOV», en la raíz de su Drive, junto a la de casos
(`13wsiWOYCbAxg4IPKHJq4r63uCkDWWaub1YKMP4h_xxM`). Tres pestañas: `Videos de profe` (una fila por pieza, con la versión
vigente y enlaces al video, al `.srt` y a la carpeta), `Resumen` (por curso, con fórmulas) y `Notas`.

Al 18 de noviembre: 90 filas, **85 videos entregados, 935 minutos, 60 con subtítulos, 34 con gráfica provisional** y 5
pendientes o en pausa.

| archivo | qué hace |
|---|---|
| `datos.py` | las filas. Salen de `cursos/<curso>/subtitulos/manifiesto.json` (nombre e id del video), de la tabla del README de subtítulos (duración e id del `.srt`), del README de Trata y de una lista a mano para Delitos ambientales y el curso de Bienes, que no tienen subtítulos |
| `duraciones.json` | duración medida con ffprobe de las entregas que están en `05 EXPORTS` (para las que no tienen subtítulos) |
| `notas.py` | el texto de la pestaña de notas |
| `hoja.py` | arma el `.xlsx` (openpyxl); se sube a Drive con `create_file` y Drive lo convierte a hoja de Google |

Para rehacerla: `python hoja.py salida.xlsx` y subirla de nuevo (queda otra hoja con otro id: la vieja va a la papelera).

**Un video nuevo se anota en `datos.py`** (si tiene subtítulos, basta con que esté en el manifiesto y en la tabla del
README de su curso, y agregar su renglón a la lista del curso).

Lo que no entra: casos animados y láminas (están en `herramientas/casos_en_documentos`), y los cinco cierres de unidad
de Delitos ambientales, que son diapositivas con voz.

Cómo se comprobó: las fórmulas del resumen se recalcularon con LibreOffice antes de subir y se leyeron de vuelta desde
la hoja de Google (85 / 935 / 60 / 34 / 5); 86 enlaces de video, sin ids repetidos. **No se abrió cada enlace**: los ids
son los que devolvió Drive al entregar cada archivo.
La fecha de los seis `.mov` de SRPA del 11 de noviembre es aproximada (sale del documento de esa tanda, no de Drive).

**20 nov 2026: Desaparición forzada.** Las 17 piezas (`datos.py`, bloque de Prioridad 3) se agregaron a la hoja en su
lugar, sin rehacerla: 17 filas nuevas en `Videos de profe` (105–121, entre Trata y Estándares, con el formato de la fila
de arriba y los enlaces como formato de celda), una fila en `Resumen` con las mismas fórmulas que las demás (rangos
hasta la 122), el total con `SUM` en lugar de números escritos, y el curso sale de «Cursos sin videos de profe».
Leído de vuelta: 116 entregados, 1171 minutos, 91 con subtítulos, 65 con gráfica provisional, 5 pendientes.

**20 nov 2026: Audiencias preliminares.** Nueve filas (`datos.py`, bloque de Prioridad 1, después de Ley 1826) en
`Videos de profe` (57–65, entre Ley 1826 y Derechos humanos): la presentación del curso como «Sin grabación» (la pide la
ficha y no está) y las ocho entregas. Una fila en `Resumen` (la 7) con las mismas fórmulas, rangos hasta la 131. Leído
de vuelta: 124 entregados, 1225 minutos, 99 con subtítulos, 73 con gráfica provisional, 6 pendientes.
