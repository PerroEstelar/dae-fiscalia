# Delitos informáticos · videos de profe (22 nov 2026)

Curso «Delitos informáticos» (Prioridad 3). Profe: **Yefrin Garavito Navarro** (formato del curso, «1.5 Autor»; su
rótulo dice «Ing. Yefrin Garavito Navarro»). **Entrega provisional**: intro, cartón de título, cartón de cierre y outro;
el cuerpo es la edición del profe.

## El pedido

Sebastián (22 nov): «tenemos que procesar videos para el curso delitos informáticos, creo que solo están las unidades 3
y 4; este profe metió su propia gracia: lo que debemos quitarle es inicio y cierre, donde intentó hacer un cartón del
caso inicial que no puede ir, reemplazarlos por el nuestro; sus lower thirds y gracia dentro del video pueden ir; lo
que no puede ir es ese logo que él le puso en la esquina superior derecha, creo que está hacia el comienzo y final del
video, pero podemos dejar su graficación interna (…) intro, cartón de entrada, cartón de salida y outro».

## Lo que llegó

`E:\DAE MASTER\CURSO DELITOS INFORMATICOS\`: cinco videos ya editados por el profe en DaVinci (1280×720 a 25, BT.709,
AAC estéreo). Cada uno empieza con un cartón suyo sobre fondo azul noche (2 a 5 s, en silencio digital); el inicio y el
cierre de la U4 terminan con otro. Adentro: el profe sobre el fondo virtual del campus, sus rótulos («Docente · Ing.
Yefrin Garavito Navarro», los de sección), sus láminas a cuadro completo (con la marca DAE | FISCALÍA abajo a la
derecha, que es parte de su lámina y queda) y, junto con los rótulos de sección, una placa «DAE | FISCALÍA» arriba a la
derecha, que es la que sale.

| plan | pieza | fuente | entrega | entra (s) | su placa (s) |
|---|---|---|---|---|---|
| `plan_diu3i` | U3 inicio | `1. bienvenida unidad 3.mov` (5:57,6) | 6:27 | 2,16–355,46 | 2,16–10,36 · 12,48–17,80 · 352,20–357,56 |
| `plan_diu3m` | U3 intermedio | `2. Intermedia unidad 3.mov` (5:24,1) | 5:52 | 6,46–324,00 | 18,64–23,96 |
| `plan_diu4i` | U4 inicio | `4. Bienvenida Unidad 4.mov` (5:55,7) | 6:19 | 5,36–350,32 | 22,28–30,04 · 345,44–350,60 |
| `plan_diu4m` | U4 intermedio | `5. intermedio unidad 4.mov` (6:40,3) | 7:10 | 4,28–399,74 | 10,48–15,68 |
| `plan_diu4c` | U4 cierre | `6. cierre unidad 4.mov` (5:51,5) | 6:16 | 5,00–346,40 | 5,00–12,20 · 328,40–333,72 |

`4. Bienvenida Unidad 4 (1).mov` es el mismo archivo (md5 igual). **Falta el «3.»**, que por la numeración sería el
cierre de la U3; tampoco hay nada de las U1 y U2 ni la presentación del curso.

## Cómo se arma

- **La placa de arriba a la derecha** (`limpia_logo_di.py`): detrás está el fondo virtual de la videollamada, que es
  una foto quieta, así que se tapa con ese mismo fondo sacado de la grabación (la mediana de los cuadros del profe), con
  8 px de borde suave, solo en los cuadros en que está la placa (más 4 cuadros a cada lado: entra y sale con fundido) y
  solo sobre el profe (en las láminas no se toca nada). Se trabaja en YUV 4:2:0, sin pasar por RGB; x264 CRF 14 y el
  audio copiado: `01 VIDEO/<PREFIJO>_fuente_limpia.mp4` es la `ORIGINAL` del plan.
  - La placa no siempre está en el mismo sitio (x 998–1226, y 40–88 en unos rótulos; x 1016–1270, y 17–83 en otros).
    La primera pasada usaba el rectángulo del primero y dejaba un borde de la placa en los otros: se vio en la tira de
    comprobación (original y limpio lado a lado) y esos compuestos fueron a `_descartes` antes de rendir nada. El
    rectángulo es ahora x 984–1278, y 8–100.
- **Ventana** 1248×702 desde (16, 0), subida a 1080 (×1,54): deja fuera la franja con el nombre del participante de la
  videollamada que hay abajo a la izquierda («Yefrin Alexis Garavito Navarro», y 704–720) y pierde 16 px a cada lado,
  que las láminas del profe tienen de margen.
- **Bordes**: entra en el corte de su cartón o medio segundo antes de la primera palabra, lo que venga después; sale
  0,7 s después de la última palabra, o en su cartón final, o con el archivo. Adentro no se corta nada.
- **Sin rótulo nuestro**: los suyos ya dicen quién es.
- Cartón de título: «Delitos informáticos» y «Unidad 3. Investigación y judicialización» / «Unidad 4. Evidencia
  digital».
- `lote/cadena_di.py` (por pieza, `lote/pieza_di.py`: fuente limpia, compuesto, cartón de título) y `lote/entrega_gpu.py`
  (línea de Resolve y entrega por la placa NVIDIA, ~5 Mb/s, fuera de receta, como en Derecho de petición), con
  `D:\DAE\_tmp\di_p\` como carpeta de trabajo.
- Árbol: `E:\DAE MASTER\PRIORIDAD 03\CURSO DELITOS INFORMATICOS - VIDEOS PROFE\UNIDAD n\<INICIO|INTERMEDIO|CIERRE>`.

## Entregas (22 nov 2026)

Las cinco entre las 10:36 y las 10:47 (hora de Colombia), en Drive: carpeta del curso «Delitos Informáticos»
(`1eqVUqpAHTHxAsLADFj8ryvbHe0_kSwX1`) › **VIDEOS PROFE** (`1LHDRmw_ud3RZmGwXIyiX8P6VWTqNp6Fw`), cada una con su `.srt` al
lado (y en `05 EXPORTS` junto al video). Render por la placa NVIDIA desde Resolve, ~5,3 Mb/s, a 23,976 cuadros/s (fuera de
receta, como en Derecho de petición). Sonido: −16,1 LUFS, pico −2,9 a −3,0.

| video | dura | MB | id en Drive | `.srt` |
|---|---|---|---|---|
| `delitosinformaticos - U3 - INICIO-v1.mp4` | 6:27 | 244 | `1ctxUrBbWt8TgLliUeBzZkBbzzaJ7Je4B` | `1yHUNFnK4n6EsHT_uJ1rRWWx6twJQHtls` |
| `delitosinformaticos - U3 - INTERMEDIO-v1.mp4` | 5:52 | 225 | `1A4lMSIShQ4EJvdz096RwaKHyocBj7g6q` | `1dxCD6bKCHI81mM6_JBvtrhmiZh2TNMrR` |
| `delitosinformaticos - U4 - INICIO-v1.mp4` | 6:19 | 242 | `125Svs4XlCZ8vXZM31iEIMNpnBpgAIaBd` | `1-gvmS7i2rbB3oMDjDFZ7vfRPuwqQrOmT` |
| `delitosinformaticos - U4 - INTERMEDIO-v1.mp4` | 7:10 | 274 | `1A79XCs5zI0GmgYqhTqMOycJijlLIN6y6` | `1isGYURX02FJ5aIwlcvygwlP-hwKyBacU` |
| `delitosinformaticos - U4 - CIERRE-v1.mp4` | 6:16 | 240 | `1MdqiBaNoYDOmBUJNCw9S2Gq0s1kdv_4R` | `1orfjIK1VEHWX_M4KNE7Y-y9KjO062gD3` |

- **La placa, comprobada tres veces**: en la fuente limpia (recorte de la esquina, original arriba y limpio abajo, al
  entrar, a la mitad y al salir de cada tramo: `D:\DAE\_tmp\di\verif2_<u>.png|jpg`), en el compuesto y en la entrega
  (`verif_ent_u4m.jpg`). No queda borde.
- **Cuadros contra la línea**: los cinco salieron con los cuadros exactos de su línea (9289, 8430, 9088, 10300, 9003).
- **Verificadas byte a byte** contra `05 EXPORTS` (copia de servidor `verif_<clave>.mp4` en `_MA subidas`,
  `D:\DAE\_tmp\di_p\verif_<clave>.log`); después el video pasó a VIDEOS PROFE y la copia, a la papelera.
- Subtítulos: `../subtitulos/README.md`.

### Lo que hay que avisar

- **U3 inicio, 5:39**: él dice «Segundo, avance en el caso sin registrar ante su decisión»; su lámina dice «Registre su
  decisión antes de avanzar». Queda como se oye.
- **U4 intermedio, 4:54**: él dice «encenderlo describe en el disco, altera las máscaras de tiempo»; el subtítulo dice
  «escribe… las marcas de tiempo» (como lo dice él en el cierre). El video queda como está.
- **U4 intermedio, 5:41**: «Es una condición necesaria y suficiente, pero no nos demuestra autenticidad» (por lo que
  sigue, sería «necesaria pero no suficiente»). Queda como se oye.
- **Falta el «3.»** (cierre de la U3, por la numeración de los archivos) y no llegó nada de las U1 y U2 ni la
  presentación del curso.
