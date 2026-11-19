# Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado · videos de profe

## Inicio y cierre del curso y de las unidades 1 a 4 (19 nov 2026) — entrega provisional

Pedido de Sebastián (19 nov): editar repeticiones, errores, cortes, silencios, entradas y salidas, **cambiar el fondo
virtual por el de la Fiscalía** y hacer todo el procedimiento habitual con gráfica provisional. Fuente: carpeta
«VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), diez grabaciones del 18 nov y una repetida. Eligió el
encuadre «B: 10 % más chico» y la carpeta del curso como destino.

| pieza | entrega · id | `.srt` | largo | edición |
|---|---|---|---|---|
| Inicio del curso | `ley1826 - CURSO - INICIO-v1.mp4` · `1OIC6NYJDGGNGp4y4_tO8KX-lXOYIvn84` | `1Lv-0gbmOtLGsmkAQDQlC29EKNyfGwBKt` | 7:28,4 · 10.752 cuadros | sin cortes |
| Inicio de la U1 | `ley1826 - U1 - INICIO-v2.mp4` · `1W3q85n6z__m7K--xAXbBRdw9SZjZo5E6` | `1KLWisdca8KajBtiF0r39TZmcIY3vLhFo` | 5:40,8 · 8.170 cuadros | sin cortes · **v2** |
| Cierre de la U1 | `ley1826 - U1 - CIERRE-v1.mp4` · `1Wv-L6CDja0L5ycAUnj-HWBH1rnPiqY-1` | `1hAOVwTa_Cdz7ggPjCCY9o0o5w_6zOiFb` | 5:19,6 · 7.662 cuadros | sin cortes |
| Inicio de la U2 | `ley1826 - U2 - INICIO-v1.mp4` · `1MuoycyGq3wi9vFzi3fzC22GMztBrUdOa` | `1jPMrp5cYoXgZTz06dwwTFLc_pDrL_2dp` | 5:44,0 · 8.248 cuadros | dos cortes (`SUAVE = 3`) |
| Cierre de la U2 | `ley1826 - U2 - CIERRE-v1.mp4` · `1zkUqqqiKYMwhf5n6V17uHINHIWu__UBc` | `14SBo36jXykJlS9q-AE2HTmK0acHTbXbf` | 5:38,7 · 8.121 cuadros | sin cortes |
| Inicio de la U3 | `ley1826 - U3 - INICIO-v1.mp4` · `1kNeg95ypwz7EVuRURvw6GYjfVhmkO3ch` | `1jHRvUVbN5jO7Tihg11Y_hVu90PQmiaBH` | 6:36,0 · 9.494 cuadros | sin cortes |
| Cierre de la U3 | `ley1826 - U3 - CIERRE-v1.mp4` · `1WTuLfpY5MOre1YLsjpAOqX8s0kRfna9D` | `1stk4JSR5KKgT69TvWo81ERBP8ox2BqRD` | 5:28,1 · 7.866 cuadros | un corte (`SUAVE = 3`) |
| Inicio de la U4 | `ley1826 - U4 - INICIO-v1.mp4` · `1XPoihKdmmB6M8iRfbqM0c-LRLHzBPDWo` | `1F1OxjS-wg9VUdUv1nlourCyBBLCXpAjY` | 5:21,0 · 7.696 cuadros | un corte seco + 4 s de `CERRADO` |
| Cierre de la U4 | `ley1826 - U4 - CIERRE-v1.mp4` · `1Bjr-x-VJloOkDiIfwOrinaY5p4wWhV6D` | `1ZmXLiFPDzoqfQqnXrbdiLTYEuqWPAicK` | 6:36,9 · 9.516 cuadros | sin cortes |
| Cierre del curso | `ley1826 - CURSO - CIERRE-v1.mp4` · `19A-bDSHdykBQ9WGtG5yLPAE718idGJKo` | `1aL5yGGRr09ISmctz1pf2fclhKTFYdnF1` | 8:30,3 · 12.235 cuadros | sin cortes |

Total: 62 minutos. Carpeta: VIDEOS › VIDEOS FINALIZADOS (`1mIFyAi87UosQ8Rue7j9g6aL4db9bRG2d`); cada `.srt` al lado de
su video (ver `../subtitulos/`). Todas verificadas en Drive byte a byte (`verificar_drive.py`).

- **Video:** H.264, 1920×1080, 23,976, Rec.709, ≈5,35 Mb/s, directo de Resolve por la placa NVIDIA
  (`lote/entrega_gpu.py`), sin máster de 32 Mb/s. **Audio:** AAC 48 kHz estéreo (la fuente es mono), −16,0/−16,1 LUFS,
  pico −2,6 a −3,0 dBTP. Líneas de Resolve `LEY1826 - CURSO|Un - INICIO|CIERRE`.
- **Provisional:** intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos.
- **El inicio de la U1 está en v2.** La v1 (`1lkHo9dOmF-ojNGAXyBEZE2o7BUsd6GFm`) salió antes de la pluma de los
  bordes: una mano y la cabeza quedaban cortadas en línea recta en el borde del recorte. Sigue en la carpeta;
  Sebastián decide si se borra.
- Base, criterios de edición, recorte y lower third: `base_lp_profe.py`. Cada plan cuenta sus cortes con tiempos.

## Cómo se hizo (el lote)

`lote/recorta_lote.py` recorta dos a la vez por la placa (≈3,4 c/s cada uno con la CPU compartida; 52 min el más largo
de los primeros, el inicio del curso). `D:\DAE\_tmp\lp_p\orquesta_c.py` pone cada plan en `cola.txt` **recién cuando su
recorte terminó** (y empluma los que salieron sin pluma); `lote/lote_cadena.py 1` corre componer + título + cartones de
a uno (con dos recortes y Resolve abiertos, más de uno a la vez hace crecer el archivo de paginación en C:);
`lote/entrega_gpu.py 5000` arma la línea, rinde, mide y copia a `_MA subidas`; `D:\DAE\_tmp\lp_p\subs\subs_lote.py`
transcribe cada entrega apenas aparece. `lote/estado.py` resume todo. La revisión de cada entrega: hoja de cuadros
(`hoja_rev_*.jpg`), los cortes cuadro a cuadro y los picos del mate que marca `rev_recortes.log` (todos manos que entran
por el borde, ya difuminadas).

Tiempos reales: el recorte de los diez, de 10:30 a ≈14:50; las cadenas, 8 a 10 min cada una (30 min la primera, con
cuatro procesos peleando la CPU); la entrega, 1 a 2 min.
