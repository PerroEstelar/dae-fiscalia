# Justicia restaurativa en la práctica del fiscal · videos de profe

## Cierre del curso (18 nov 2026) — entrega provisional

Pedido de Sebastián (18 nov, 08:55): «por favor continúa con justicia restaurativa [carpeta VIDEOS del curso]; creo que
por ahora el único es el cierre del curso». En la carpeta (`1s-ZDIhTCPriybRjIIzSYx1GIqkcmgZvy`) había un solo archivo:
«Justica restuaraativa-  Cierre curso.mp4» (`1dGNePRbK98Td0Q45F07m7tKQzZkp1IRv`, 567 MB).

| | |
|---|---|
| entrega | `justiciarestaurativa - CURSO - CIERRE-v1.mp4` · `1yldH5QJQxz7UTnLpyoZBuN8MyjzIy9Pl` |
| carpeta de Drive | VIDEOS › VIDEOS FINALIZADOS (`11XMZRms3FGeaPvLepeYoM9z0qZO0uB5o`) |
| subtítulos | `justiciarestaurativa - CURSO - CIERRE-v1.srt` · `1xuKv_o5UkvBMXuwx_PspTtD8NtTSbvi2` (ver `../subtitulos/`) |
| largo | 44:49,6 · 64.487 cuadros (= línea) · 1.800.362.042 bytes |
| video | H.264 Main L4.0, 1920×1080, 23,976, Rec.709, 5,16 Mb/s (placa NVIDIA, directo de Resolve) |
| audio | AAC 48 kHz estéreo · −16,0 LUFS · pico −2,6 dBTP |
| línea de Resolve | `JR - CURSO - CIERRE` (bin PRIORIDAD 1 › CURSO - JUSTICIA RESTAURATIVA) |
| disco | `E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\CIERRE DEL CURSO\` |

Verificada en Drive byte a byte (copia de servidor a `_MA subidas` y comparación por bloques de 1 MiB, `verificar_drive.py`).

**Qué es «provisional»** (lo mismo que las clases de SRPA y las unidades de Bienes): intro, cartón de título, rótulos de
nombre, cartón de cierre y outro; el cuerpo va sin cartones ni gráficos. Y sale directo de Resolve por la placa NVIDIA,
sin máster de 32 Mb/s (pesaría ~10 GB y E: tenía 5). Si Sebastián quiere gráficos, sale una `-v2` sobre el mismo
compuesto.

### La fuente

- 1920×1080, 30 fps, 80.225 cuadros (44:34), BT.601, pico −1,3 dBFS. El mismo editor que las de Bienes: **trae pegados
  una intro (cuadros 0–277) y un outro (desde el 79949; el 79947 y el 79948 son blancos)**. Entra del 280 al 79947.
- **Dos coautores en videollamada**, cada uno en un mosaico de 936×528 sobre un lienzo blanco (izquierda x 7–942,
  derecha x 982–1916, los dos en y 290–817). Va el cuadro entero, sin ventana.
- Habla Víctor de 0:09,6 a 5:35; Martín de 5:37,7 a 23:09; cierra Víctor de 23:11 a 44:24.
- **Sin reinicios** (se leyó la transcripción buscando «repito», «perdón», «volver a empezar», frases repetidas y
  pausas). Hablan sin leer y hay tropiezos; no se cortó nada.

### Nombres y rótulos: de la ficha, no inferidos

Ficha «Prioridad 1 - Presentacion Vaciado_ Justicia Restaurativa en la Práctica del Fiscal.docx»
(`1bQcllAcXC6Ka9i76T3Ep4ZLYv1o1YY2y`): nombre del curso «Justicia restaurativa en la práctica del fiscal»; «Víctor Hugo
Ospina Vargas, profesor de pregrado y posgrado de la Universidad Nacional, y Martín Posada Martínez, investigador
académico». En el video se presentan ellos mismos (Scribe oye «Espina»).

- Izquierda: «Víctor Hugo Ospina Vargas · Coautor del curso. Profesor de pregrado y posgrado de la Universidad Nacional
  de Colombia». Derecha: «Martín Posada Martínez · Coautor del curso. Investigador académico».
- **Van debajo de cada mosaico, sobre el blanco, en tinta azul (22, 58, 79) y sin sombra.** El rótulo blanco con sombra
  de la serie no se lee sobre el lienzo, y dentro del mosaico taparía a la persona. `cartones_srpa.lower_third` acepta
  un tercer elemento con opciones: `x`, `top`, `ancho`, `tinta` (con `tinta` no dibuja sombra).
- Tres rótulos: Víctor 11,0–18,5 s de la fuente, Martín 19,2–26,7 y Martín otra vez 338,6–346,6, cuando toma la palabra.
- Se revisaron compuestos sobre un cuadro de la fuente antes de armar la línea: caja de (40, 851) a (829, 994) y de
  (1015, 852) a (1656, 962); no tocan los mosaicos (terminan en y 817) ni salen del cuadro.

### Cómo se hizo

```
profe_cadena.py plan_jrcc componer titulo cartones      # 09:14 a 09:35 (el compuesto, 19 min)
lote/entrega_gpu.py                                     # 12:14 a 12:20: línea, calibración, render (271 s), copia a G:
```

- `base_jr_profe.py`: raíz, bin, nombre del curso en dos renglones, 30 fps de fuente, `AUDIO_META I=-16:TP=-3:LRA=7`,
  los dos rótulos y `armar(...)`. `plan_jrcc.py`: el tramo y los tres rótulos.
- `lote/entrega_gpu.py` es el de Trata con dos cambios: **rinde en `%TEMP%\dae_rindiendo` (C:) y mueve la entrega a
  `05 EXPORTS` al final**, porque E: no tenía sitio para el render y el compuesto a la vez; y acepta el caudal ya
  calibrado como argumento. Pidió 5000 kb/s y salió a 5355.
- `profe_cadena.py` se negaba a empezar («SIN ESPACIO EN E:»): calculaba 0,35 GB por minuto, pensando en una pieza con
  gráficos y máster. Si todos los ítems del plan son rótulos, calcula 0,06 GB por minuto (mínimo 1 GB).
- Entre las 09:35 y las 12:13 no pasó nada: la sesión se cortó con el compuesto ya hecho. No se perdió trabajo.
