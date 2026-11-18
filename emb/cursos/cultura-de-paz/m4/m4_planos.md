# M4 · planos y clips

Placas Seedream 5.5 (2k, 16:9) con el ancla de estilo `rgedn6jxtc` y las hojas de personaje; clips Kling 2.5 (720p, 5 s) desde la placa como cuadro inicial.
Proyecto de Magnific: «EMB · Cultura de Paz». Costo aproximado: placas ~2.400 cr + clips 31 × 140 = 4.340 cr.

| plano | qué es | placa | clip | ventana |
|---|---|---|---|---|
| Q1 | Salón comunal, servidora saluda (madre del salón) | `VXwW6GYMMU` | `YMszk2vWeC` | completo |
| Q2 | Veedor pregunta con la hoja | `dtPM06VXSL` | `lJILdwAgv9` | completo |
| Q3 | Vocero fuerte; manos que esperan turno | `dtPM0cmXSL` | `1leKTg4r4r` | completo |
| Q4 | Comerciante explica el territorio | `YMsARYnWeC` | `UPhgo2Wwny` | completo |
| Q5 | Mesa de recepción presencial en la calle | `1lebHUfr4r` | `huZtNjYvqL` | completo |
| Q6 | Tablero de tres columnas | `Lwo1KRvswO` | `SymlBYaUb8` | [0, 60] |
| Q7 | Devolución de hojas en el círculo | `5jMFuZDKxe` | `N2H4Cvk6D9` | completo |
| R1 | Dos servidores con indicaciones contradictorias | `mERocoRhJQ` | `dtPpwwaXSL` | completo |
| R2 | Teléfono contra aviso físico | `s78rkeIl8e` | `1leKTMIr4r` | completo |
| R3 | Servidora compara y corrige | `Xm4DVWdBfo` | `ovNXORS829` | completo |
| R4 | Trato digno a cuidadora y adulto mayor | `fHGmIIMCDY` | `bxVHYBL5Y2` | completo |
| R5 | Pila de solicitudes repetidas | `yiEwU9bPW9` | `dtPpwAxXSL` | completo |
| R6 | Oficina: coordinación con ingeniero | `aFAtoibfSh` | `yiEJhl7PW9` | completo |
| R7 | Tablero de seguimiento | `IfiXdFgtvE` | `aFAhiIIfSh` | completo |
| R8 | Actualización honesta a la comerciante | `dtPMVqSXSL` | `p8OMSMTehw` | completo |
| S1 | Calle con recorrido provisional (madre) | `s78rEHUl8e` | `O6C7hiCynm` | [55, 120] |
| S3 | Rampa empinada | `aFAtIJvfSh` | `79aUtiwJAL` | [0, 40] |
| S4 | Comerciante y acceso cerrado | `TdUYnlZVNR` | `MB7TghnDCm` | completo |
| S5 | Cuidadora con adulto mayor en el recorrido | `Xm4DM42Bfo` | `huZt6LYvqL` | completo |
| S6 | Vecinos leen el aviso | `kspqHHj16B` | `s78jdGHl8e` | completo |
| S7 | Servidor gris descalifica en el salón | `Bh9pptMoQR` | `WDlnxQjcXe` | completo |
| S8 | Veedor entrega solicitud en la caseta | `3z599VwREY` | `N2H4EvK6D9` | completo |
| S9 | Ingeniero en el acceso cerrado | `4RQJJpJ9Aa` | `p8OMUUlehw` | completo |
| T1 | Verificación en terreno con cinta | `mERooOIhJQ` | `vQ2miYAa47` | completo |
| T2 | Aviso nuevo colocado | `mERooRuhJQ` | `ksp5TCW16B` | completo |
| T3 | Apertura asertiva en el salón | `YMsAAOUWeC` | `w4vSIjv7EI` | completo |
| T4 | Servidor gris reconoce | `huZ88XdvqL` | `yiEJvUOPW9` | completo |
| T5 | Cenital de alternativas | `TdUYWh1VNR` | `Cqza2FQEEy` | [0, 60] |
| T6 | Rampa nueva | `s78rxcKl8e` | `tC38NEbmZJ` | [0, 45] |
| T7 | Acceso peatonal nuevo | `w4vlgdq7EI` | `VXw0gIkMMU` | completo |
| T8 | Cierre con tren rojo en el viaducto | `8a6dX6tIrU` | `5jMq0UtKxe` | completo |

Descartada: `R6_dos_cascos` (`u5YadFjQLD`), el ingeniero llevaba dos cascos.

## Ventanas, y por qué

- **Q6**: desde ~60 la cámara se mueve y reencuadra el tablero.
- **S1**: una mujer entra en primer plano desde abajo al segundo 1; se entra en 55.
- **S3**: Kling la sube a la rampa, y el caso dice que no puede completar el recorrido. Se corta en 40.
- **T5**: la regla se duplica desde ~70.
- **T6**: la servidora cruza al otro lado de la silla.

## Notas de esta tanda

- Kling aceptó a veces una sola llamada en paralelo y otras tres; se mandó de a tres sin perder ninguna.
- Las escenas se generan con `m4/escenas_m4.py`: el texto de voz entra desde `bloques.py` como objeto `T`, así que escena y locución no se pueden desincronizar.
- Verificación antes de la voz: cargar cada escena en Playwright, `ESCENA.init()` y `render` de todos los cuadros. `init` lanza «frase no encontrada» si un `en` no existe en el texto del bloque. Cargar la página sola no lo detecta.
- `S_reescribe` acepta `lit:false` en una fila: el «antes» va en cursiva gris y sin comillas, para un campo que no es una cita («Sin precisar»).
- `S_ruta` dibuja cuatro paradas; con cinco la quinta no aparece.

## Pautas de Kling

- **Q1**: The servant in the red jacket at the back takes two steps forward and raises one open hand to greet the room; the seated neighbours turn their heads toward her, the woman in the yellow apron settles in her chair, the man in front writes a line in his notebook.
- **Q2**: The older man with glasses lifts the sheet, taps a line on it with his finger and speaks a short question; the servant in the red jacket listens, nods once and writes it down in her notebook; behind them the neighbours turn to look.
- **Q3**: The broad-shouldered man in the dark suit speaks loudly with both arms open to the room; the servant in the red jacket turns her head toward the quiet neighbours on the left, who lift their hands a little, waiting their turn.
- **Q4**: The shopkeeper in the yellow apron points along the fence toward the far end of the street and explains, moving her hand along the route; the servant in the red jacket follows the gesture with her eyes and nods, writing on her clipboard.
- **Q5**: The elderly man hands a folded sheet across the table; the servant in the red jacket takes it with both hands, reads it, nods and places it in the box beside her; the woman beside him keeps her hand on his arm.
- **Q6**: The servant in the red jacket presses one more paper note onto the board, smooths it flat and steps back half a pace to look at the three columns; the two young people in the foreground lean forward slightly to read.
- **Q7**: The servant in the red jacket walks along the circle handing a sheet to the woman in the wheelchair, then turns to the next person; the neighbours look down and read their sheets, one man turns a page.
- **R1**: The two servants inside the booth point in opposite directions at the same time and both speak; the young woman with the phone looks from one hand to the other, confused, and lowers her phone.
- **R2**: The young woman scrolls on her phone, looks up at the paper notice on the fence, then back down at the phone, comparing the two; her thumb keeps scrolling.
- **R3**: The servant in the red jacket looks from the phone on the desk to the paper beside it, picks up her pen, crosses out one line and writes a correction next to it, then puts the pen down.
- **R4**: The servant in the red jacket leans slightly toward the window and speaks calmly; the carer outside nods and the elderly man with the cane lifts his head to listen, then nods slowly.
- **R5**: The servant in the red jacket picks up one envelope from the tall stack, opens it, reads it, and lays it on top of a second identical sheet already on the desk; she sighs and places her hand flat on both.
- **R6**: The engineer in the hi-vis vest traces a line on the plan with his finger and explains; the servant in the red jacket writes in her notebook; the woman with the laptop types and looks up at them.
- **R7**: The servant in the red jacket moves a paper note from one column of the board to the next and presses it flat; the engineer with the clipboard checks something off and nods.
- **R8**: The servant in the red jacket holds up the sheet and explains with an open hand; the shopkeeper in the yellow apron listens with both hands on the counter, then nods once, serious.
- **S1**: Pedestrians walk slowly along the narrow route between the construction fence and the barriers, one woman carries a bag toward the camera; a few people walk in the far distance; the cables sway very lightly.
- **S3**: The woman in the wheelchair rolls forward to the bottom edge of the steep wooden ramp, stops, looks up the slope, and pulls her hands back from the wheels.
- **S4**: The shopkeeper in the yellow apron rests one hand on the half-raised metal shutter and looks out at the grey fence blocking her doorway, then lets her other hand fall to her side.
- **S5**: The carer and the elderly man with the cane walk slowly along the narrow route toward the camera, one careful step at a time, her hand under his elbow; a figure walks in the distance.
- **S6**: The neighbours gather in front of the paper notice on the fence; one woman reads it close up, a man takes a photo with his phone, another points at a line and turns to the others.
- **S7**: The man in the grey suit makes a short dismissive wave of his hand toward the seated neighbours; the servant in the red jacket turns her head toward him; the woman in the yellow apron in front crosses her arms.
- **S8**: The older man with glasses pushes the folded request across the counter; the servant in the red jacket takes it in both hands, lays it on the pile and nods to him.
- **S9**: The engineer in the hard hat stands by the closed access and looks along the street, then turns and gestures toward the fence; a pedestrian with a bag walks along the route toward the camera.
- **T1**: The engineer in the hi-vis vest kneels and pulls the measuring tape along the wooden ramp; the woman in the wheelchair points at the top edge; the servant in the red jacket writes on her notepad.
- **T2**: The worker presses the new paper notice flat on the fence with both hands; the servant in the red jacket checks it against her phone and nods; a passer-by stops behind them to read.
- **T3**: The servant in the red jacket at the front speaks with both palms open; the seated neighbours listen, the woman in the wheelchair nods, the man in the plaid shirt uncrosses his arms.
- **T4**: The man in the grey suit lowers his head slightly, places a hand on his chest and speaks to the room; the servant in the red jacket beside him nods; the neighbours look up at him.
- **T5**: Seen from above, the engineer draws a line along the ruler on the plan, the servant in the red jacket writes in her notebook, the woman at the top turns a page; their hands move and stop.
- **T6**: The woman in the wheelchair rolls up the new gentle ramp holding the handrail, reaches the top and stops; the servant in the red jacket beside her lowers her clipboard and nods.
- **T7**: Two people walk through the new open pedestrian access toward the camera carrying bags; a cyclist passes on the road; the shopkeeper in the yellow apron stands in her open doorway.
- **T8**: The red metro train glides across the viaduct from left to right; below, people walk along the open street and the woman in the wheelchair rolls along the pavement.
