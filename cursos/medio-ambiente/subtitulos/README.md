# Delitos contra el medio ambiente — subtítulos (22 nov 2026)

Los doce videos de profe del curso, sobre las entregas que están en Drive. Método y criterio:
`herramientas/subtitulos/README.md`. Correcciones: `correcciones.json` (las de `_todos` valen para los doce).

| video | subtítulos | dura | id del `.srt` en Drive |
|---|---|---|---|
| `delitosambientales - CURSO - INTRODUCCION-v1` | 50 | 4:22 | `1gYOHvw0YNJZR9gObMBYZp078Q1R2xZ8w` |
| `delitosambientales - U1 - INTRODUCCION-v4` | 80 | 6:31 | `1sr12c26t41yW3xnOC9Dc3umh7SPwF8aB` |
| `delitosambientales - U1 - CONVERSATORIO DEMA y DECOC-v1` | 305 | 19:54 | `1mUzkU1DC-nvrIytxmZE9WbnPQQ9e9O8Y` |
| `delitosambientales - U2 - INTRODUCCION-v3` | 78 | 5:42 | `10wl8hup3Ykd1H_Qkc2R8J-RWf559oZJe` |
| `delitosambientales - U3 - INTRODUCCION-v3` | 69 | 5:32 | `1UvnZSyqj6fTQ4-5DqeVPAQQ4GPL_5YBc` |
| `delitosambientales - U3 - ENTREVISTA TECNICAS ESPECIALES-v1` | 208 | 15:33 | `1SHx0JTmJF0pFcCeOGoxvTjZHhqR-7ROj` |
| `delitosambientales - U3 - LECCION 4-v1` | 77 | 5:38 | `1GAGuRNCPFMB0aa1rqupdzuNwKTQemKkJ` |
| `delitosambientales - U3 - LECCION 5-v1` | 106 | 7:13 | `1hhh2xs2lGA0VGrsuz9wPszI0DWXxG7Wd` |
| `delitosambientales - U4 - INTRODUCCION-v3` | 86 | 6:16 | `1jaqigbkKQ1xza0zeWrc5KgprzqYG_vXd` |
| `delitosambientales - U4 - LECCION 1-v1` | 448 | 28:11 | `1mflIc1prJR1EYS3O0z3zu-WVltEWCSSw` |
| `delitosambientales - U5 - INTRODUCCION-v3` | 79 | 5:47 | `16u1c_JBmlAMeIGahfMBu8ejRiMy4og0r` |
| `delitosambientales - CURSO - CIERRE-v2` | 40 | 3:24 | `1A8KaogDt_3TGvAq9u08sEzX82W6IzMKz` |

**23 nov 2026: sin la presentación de la docente.** Las cinco introducciones de unidad y el cierre del curso se volvieron
a entregar sin el tramo en que ella dice su nombre y sus credenciales (`../sin_presentacion/README.md`). Sus `.srt`
salen de los de la tabla anterior con `srt_sin_pres.py`: se quitan los subtítulos del corte, se corren los de después y
el que cruza el corte queda con lo que se oye («Y en esta oportunidad…», «Y quiero felicitarlos»). Las versiones
anteriores y sus `.srt` están en Drive en `VIDEOS › _anteriores` (U1 v3: `1luNM-RF1FY0tBGPobXoSZppzFnTbgzVL`, U2 v2:
`1SSuyirDoXnhX55RBDWB7eMMsISdElHW-`, U3 v2: `14xtPYQjJQdwIX1cGMcfhOciBFRyqMAdW`, U4 v2: `16h4pMCfyzCxaa3cZRmAhRrhRHeyN11kJ`,
U5 v2: `1FgFgES1O1rT6UuElQHCt6tOzVWm_fbPa`, cierre v1: `1PJbAzQzUmtKKpCQFyPYFmwYkBYTCjACj`).

Cada `.srt` va en la carpeta de Drive de su video (la carpeta VIDEOS del curso, `1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_`, o la
de su lección) y junto al video en su `05 EXPORTS`.

- **Rótulo y nombres.** La profe dice «Diana Carolina Flórez Bayona»; el `.srt` lleva el nombre del rótulo, «Diana
  Carolina Florez Vallona» (confirmado por Sebastián). «DEMMA» → DEMA. En el conversatorio: DAIACO, UIAF, DIAN, ANLA.
- **Segunda escucha** (normal y al 75 %) de los tramos dudosos. Se confirmó lo que se dice y se dejó: «concertarse»
  (U3 L4, 3:13), «al unirla a ese día» (conversatorio, 13:08). Se corrigió: «una célula teoría del caso» → «una teoría
  del caso» (conversatorio, 17:01; dice «una ce-- la teoría»), «una atención de derechos» → «una tensión de derechos»
  (U4 L1, 25:10), «delitos con el medio ambiente» → «contra el medio ambiente» (introducción al curso, 0:45, nombre del
  curso), «unos situaciones» → «unas situaciones» (entrevista, 0:49).
- **Scribe estiró la última palabra de la U3 L5** («gracias.», 416,1 → 432,1 s) por encima del outro y el último
  subtítulo caía en 7:11. Se corrigió el fin de esa palabra en el JSON antes de generar: si el último subtítulo
  termina sobre el outro, mirar la última palabra.
- **U4 L1:** Resolución 0211 de 2025, artículo 521, Acerías Paz del Río (Scribe: «Hacaría Espadas del Río»).
