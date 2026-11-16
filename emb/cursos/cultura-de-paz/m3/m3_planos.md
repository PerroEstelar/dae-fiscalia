# M3 · planos, clips y registro de Magnific (16 nov 2026)

Mismo método que M1 y M2: ancla `rgedn6jxtc`, hojas de personaje y la placa madre como referencias `image`;
Seedream 5.5 a 2k, una variante por plano; Kling 2.5 720p 5 s. Todas las placas y los clips se revisaron en hoja de contactos.

Hojas nuevas: **coordinador** `Xm4tXwRBfo` (el cordón sale rojo en la hoja: en las placas se pide gris) · **integrante del equipo** `fHGFfA6CDY`.

| plano | qué es | placa | Kling | ventana útil |
|---|---|---|---|---|
| M1 | punto de atención: la residente llega al mostrador («nos hicieron perder la mañana») | `fHGFfTzCDY` | `UPhPlQowny` | 0–50 (después se van del mostrador) |
| M2 | sobre el hombro de la servidora: la residente habla | `1leljuer4r` | `79a9SLdJAL` | 0–120 |
| M3 | la servidora escucha, el bolígrafo quieto | `LwowgrnswO` | `rgdgK5Xxtc` | 0–120 |
| M4 | detalle: las dos manos sobre el mostrador | `jUBUggpLD0` | `s787xsIl8e` | 0–120 |
| M5 | la residente señala el aviso en blanco; la servidora mira | `LwowSPGswO` | `fHGHvFECDY` | 0–120 |
| M6 | el paso restringido: la comunidad ante las barreras | `UPhyU1mwny` | `0eSeW8oTfW` | 0–80 (después caminan) |
| M7 | la servidora explica el límite; la comerciante, brazos cruzados | `huZuCjLvqL` | `KLDLbJ8kqp` | 0–70 (después ella camina) |
| M8 | oficina: la servidora redacta, cuatro pilas separadas | `xSXgxkmjfW` | `6AqA9DeiJO` | 0–40 (humo en los cerros) |
| M9 | salón: el vecino crítico con el dedo en alto; ella, la palma abierta | `Bh9h8mXoQR` | `gOtOsG5SXO` | 0–120 |
| N1 | la reunión: el coordinador ridiculiza la pregunta | `jUBUgnfLD0` | `ksps5Yt16B` | 0–50 (los colegas aplauden) |
| N2 | primer plano de la integrante, los ojos en el cuaderno | `79a99BsJAL` | `dtPtpwWXSL` | 0–120 |
| N3 | pasillo: «hablar para olvidar el asunto» | `P3u33ES42C` | `s787joQl8e` | 0–120 |
| N4 | cenital: el mismo mensaje en cuatro escritorios | `nVLV0KxYQD` | `LwowxIkswO` | 0–120 |
| N5 | la servidora escucha a la integrante, a solas | `s787U8al8e` | `ksps5hS16B` | 0–120 |
| N6 | la servidora con el coordinador, a solas | `DoJoX62pcl` | `lJIJLHEgv9` | 0–120 |
| N7 | sillas en círculo, vacías | `1lelLfVr4r` | `yiEiJsuPW9` | 0–120 |
| N8 | detalle: la mano registra en la carpeta | `Bh9htpYoQR` | `ksps5F416B` | 0–120 |
| N9 | el coordinador rectifica ante el equipo | `s7877a9l8e` | `p8O8Mp4ehw` | 0–90 (aplausos al final) |
| P1 | salón: mesa de diálogo con los actores; la servidora en el tablero | `N2H2iV26D9` | `1lelkLfr4r` | 0–120 |
| P2 | la usuaria de silla busca el ingreso; aviso escondido | `fHGHESrCDY` | `rgdg1UWxtc` | 0–55 (la silla sale de cuadro) |
| P3 | la presentación técnica que se come el tiempo | `EbnbqQduuO` | `WDlDYoVcXe` | 0–75 (rayas en la pantalla) |
| P4 | la comerciante atiende y no puede mirar la reunión virtual | `8a6atgeIrU` | `tC3CIwKmZJ` | 0–120 |
| P5 | recorrido conjunto junto al cerramiento | `xSXSgJ6jfW` | `tC3CIOrmZJ` | 0–120 |
| P6 | posiciones: mover el aviso o conservarlo | `Xm4mtHxBfo` | `Xm4md7ABfo` | 0–45 (el ingeniero saluda) |
| P7 | el consenso: la comerciante calla con los brazos cruzados | `DoJovFEpcl` | `3z5zitnREY` | 0–120 |
| P8 | detalle: cinco tarjetas en el tablero | `rgdglYIxtc` | `iGbG6kM3uK` | 0–120 |
| P9 | semanas después: la usuaria encuentra el ingreso | `JNfN9mgOq4` | `3z5zijvREY` | 0–120 |

P7 se pidió dos veces: la primera (`TdUdeFwVNR`) traía a la usuaria de silla duplicada sentada en la mesa.

Créditos: hojas 100 · placas ≈ 2.000 · Kling 27 × 140 = 3.780 · **total ≈ 5.880**.

## Motion nuevo (pieza.js)

- `S_mensaje`: el mensaje modelo se escribe frase a frase al ritmo de la voz en una tarjeta 2.5D; cada frase recibe su etiqueta de función por un hilo. La toma sigue detrás y se desenfoca cuando entra el panel (`intro.hasta`).
- `S_espectro`: formas de responder a lo mismo; las que no sirven se tachan y se apagan, la que sirve se subraya y avanza.
- `S_reescribe`: formulación imprecisa → formulación para validar, con tachado y flecha.
- `fondoVivo`/`fondoDraw`: fondo de cine para los paneles (la toma corre desenfocada detrás, con oscuridad ajustable).

## Dos cosas medidas

- Magnific acepta **unas cuatro llamadas de Kling en paralelo**; en una tanda de 27 solo entró la primera. Se mandan de a cuatro.
- La descarga en bloque desde el navegador integrado puede quedar como archivo oculto `.XXXX.com.anthropic.claudefordesktop.*` en Descargas, con el tamaño completo; se puede pasar a la nube tal cual.
