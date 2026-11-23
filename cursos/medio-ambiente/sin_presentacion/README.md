# Sin la presentación de la docente (23 nov 2026)

Pedido: «la profe Diana debe presentarse una única vez, en el video de inicio». Se quitó el tramo en que dice su
nombre y sus credenciales de las cinco introducciones de unidad y del cierre del curso. La introducción al curso
queda como estaba: es la única en que se presenta.

## Qué se quitó

| video | se quitó | queda |
|---|---|---|
| U1 | «Mi nombre es Diana Carolina Florez Vallona. Soy abogada, doctora, magíster y especialista… en materia de justicia transicional y política criminal.» (28,2 s) | «…recursos naturales. En este video quiero presentarles la unidad uno…» |
| U2 | «Mi nombre es Diana Carolina Florez Vallona y estaré acompañándolos en la presentación de esta unidad.» (7,2 s) | «…recursos naturales. En esta oportunidad conoceremos la unidad dos…» |
| U3 | «Mi nombre es Diana Carolina Florez Vallona» (2,5 s) | «…recursos naturales. Y en esta oportunidad quiero presentarles la unidad tres…» |
| U4 | ídem (2,4 s) | «…recursos naturales. Y en esta oportunidad quiero presentarles la unidad cuatro…» |
| U5 | ídem (2,8 s) | «…recursos naturales. Y en esta oportunidad quiero presentarles la unidad quinta…» |
| cierre del curso | «Soy Diana Carolina Flórez Bayona» (2,3 s) | «Cordial saludo para todos ustedes. Y quiero felicitarlos…» |

El lower third con su nombre se queda en todos: es gráfica, no presentación hablada.

## Introducciones de unidad (`ma_corta.py`)

No se rearmó ninguna línea. `rinde_masters.py` rinde cada `MA - Un - INTRODUCCION` tal como está a un máster de paso
(H.264 NVIDIA a `VideoQuality` 80000, PCM de 24 bits, en `%TEMP%/dae_rindiendo/ma_sinpres`); el de la U1 contra la
entrega v3 dio 47,6 dB de PSNR. `ma_corta.py` hace el corte sobre ese máster, en cuadros de la línea:

- `CORTES = {u: (fA, fB, fC, versión)}`: se quitan los cuadros [fA, fB); de fB a fC (el cuadro en que entra el primer
  cartón de la unidad) va un plano cerrado; desde fC, el plano abierto de siempre.
- **Bordes del audio** en RMS de 10 ms: U1 y U2 en silencio; U3–U5 en el valle de energía antes de «y». Lo quitado
  es un número entero de cuadros y el audio se corta en las mismas muestras (1 cuadro = 2002 muestras a 48 kHz), con
  fundidos de 12 ms: la sincronía no se mueve.
- **Plano cerrado**: `crop=1664:936:36:30` sobre la salida, ×1,154 a 1920×1080 (lanczos, bt709). El panel
  DAE/Fiscalía entra entero y la cabeza también. Entre el corte y el primer cartón no hay gráficos: el lower third
  termina en el cuadro 569, antes de todos los cortes.
- Entrega con la receta de `ic_mp4` (x264 CRF 18 slow, tune animation, High L4.0, keyint 48, bt709) y AAC a 320 kb/s,
  por `.parcial`, y se comprueba que los cuadros sean los de la línea menos los quitados.

## Cierre del curso (`plan_cc.py`, v2)

El lower third cruzaba el corte (0,8–8,8 s de la fuente), así que se rehízo por la cadena de siempre:

- `CORTE = (104/30, 173/30)`: de la pausa después de «…todos ustedes.» al silencio antes de «y quiero felicitarlos».
- `TRAMOS` con plano cerrado `(30, 30, 1024, 576)` de 5,77 a 8,8 s (hasta el cartón «Quiero felicitarlos…»); el
  panel empieza en x≈36 de la fuente y entra entero.
- `ic_pieza.cartones` ahora da a un ítem que cruza el corte la duración que le queda en la salida (`a_salida`):
  `lt01_v2` dura 137 cuadros y termina justo donde entra el primer cartón.
- La línea v1 quedó como «MA - CURSO - CIERRE (v1, con presentacion)» y su `.drt` en
  `10 TIMELINE SEBASTIAN/_descartes`. `cadena_cc_v2.py` (en `D:/DAE/_tmp/ma/cc`) corre componer → lower third →
  apartar la v1 → línea → `ic_mp4 2` → `ic_revision 2`.

## Subtítulos (`srt_sin_pres.py`)

Se parte del `.srt` revisado de la entrega anterior: los subtítulos dentro del corte se quitan, los de después se
corren lo que dura el corte, y el que lo cruza se reescribe con lo que queda («…y en esta oportunidad» → «Y en esta
oportunidad…»). Una última palabra que el STT estiró sobre la pausa cortada (U2, 46 ms) se recorta al borde.

## Entregas (23 nov 2026)

| video | cuadros | dura | sonoridad | pico | MB | video en Drive | `.srt` en Drive |
|---|---|---|---|---|---|---|---|
| `delitosambientales - U1 - INTRODUCCION-v4.mp4` | 9.363 (10.038 − 675) | 6:31 | −19,0 LUFS | −0,8 dBTP | 216 | `19z2MzFAjA5zhSzAQk980CrQ-xies1myW` | `1sr12c26t41yW3xnOC9Dc3umh7SPwF8aB` (80) |
| `delitosambientales - U2 - INTRODUCCION-v3.mp4` | 8.198 (8.370 − 172) | 5:42 | −19,0 | −1,2 | 186 | `19OwA__9qpNllhKcsShugpXe7yz8FohIL` | `10wl8hup3Ykd1H_Qkc2R8J-RWf559oZJe` (78) |
| `delitosambientales - U3 - INTRODUCCION-v3.mp4` | 7.950 (8.010 − 60) | 5:32 | −19,5 | −1,0 | 183 | `1AskjduHzz72ekAw1DvhwGFGTSED9Gnri` | `1UvnZSyqj6fTQ4-5DqeVPAQQ4GPL_5YBc` (69) |
| `delitosambientales - U4 - INTRODUCCION-v3.mp4` | 9.015 (9.072 − 57) | 6:16 | −19,0 | −0,8 | 215 | `1mWGUrj4uGMRipr2LTUov9CPpBf6LO4VS` | `1jaqigbkKQ1xza0zeWrc5KgprzqYG_vXd` (86) |
| `delitosambientales - U5 - INTRODUCCION-v3.mp4` | 8.320 (8.386 − 66) | 5:47 | −19,1 | −1,5 | 194 | `15ZC3brxNbXay23vZupaDUxUHg0tNbUAd` | `16u1c_JBmlAMeIGahfMBu8ejRiMy4og0r` (79) |
| `delitosambientales - CURSO - CIERRE-v2.mp4` | 4.900 (4.955 − 55) | 3:24 | −16,2 | −3,0 | 148 | `1gSVHiOkeV9quWKgzMzQyXxv03JN_BIbs` | `1A8KaogDt_3TGvAq9u08sEzX82W6IzMKz` (40) |

- Carpeta de Drive: curso → `VIDEOS` (`1h3IF2Dd7gMXpHCyyUiK0wVZyi6juUYQ_`). Las versiones anteriores (U1 v3 y U2–U5
  v2 en `.mov`, cierre v1) y sus `.srt` están en `VIDEOS › _anteriores` (`12a3_9jUl6BT-kPVofbxWrUtoQe1C4QJg`).
- Subida con `subir_exclusivo` y verificación byte a byte (`verificar_drive.py`) de las seis: OK.
- **Revisión:** tira de 4 cuadros/s alrededor de cada corte (antes · plano cerrado · plano abierto con el cartón) y
  escucha del tramo unido con `stt_tramo` (normal y al 75 %): las seis frases salen limpias.
- En disco: las entregas y sus `.srt` en cada `05 EXPORTS`, junto a las anteriores, que no se tocaron.
- `verificar_drive.py` pega la clave al tercer argumento: la carpeta va **con la barra final**. Sin ella el script
  busca `…_verif sinpres 23novdacc2.mp4` y espera una hora sin escribir nada.
