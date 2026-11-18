# Bienes en el proceso penal — subtítulos (18 nov 2026)

Prioridad 3 de la lista de Esteban: los ocho videos de unidad (inicio y cierre de U1 a U4), sobre las entregas
provisionales del 17 nov. Método y criterio: `herramientas/subtitulos/README.md`.

| video | subtítulos | dura | id del `.srt` en Drive |
|---|---|---|---|
| `bienes - U1 - INICIO-v1` | 113 | 7:17 | `1JkEDbMT22xGlxL2NpTp6PDL_9yXpVbC7` |
| `bienes - U1 - CIERRE-v1` | 424 | 26:43 | `1ZGNR8EHCr1asklWKAeTgaxxujpue-qp0` |
| `bienes - U2 - INICIO-v1` | 122 | 7:48 | `1lOqf19tJVpVaYTkZ0_aG05zbNJdj-FtO` |
| `bienes - U2 - CIERRE-v1` | 363 | 23:10 | `18TWdlQwPd0wg98hltcaOZqNa6dLCU4cy` |
| `bienes - U3 - INICIO-v1` | 91 | 5:59 | `1SSTgV-Fqly0oW4ap5Cam1IgjADpGH1PQ` |
| `bienes - U3 - CIERRE-v1` | 314 | 20:14 | `1PvTo01zUid-dSbsVym9x_K1tV5-hidxy` |
| `bienes - U4 - INICIO-v1` | 90 | 5:39 | `1YBvkMzyKsrP8IB1i6WMdjthgNccNh_uE` |
| `bienes - U4 - CIERRE-v1` | 338 | 23:50 | `16a9GnLqoIJ-KC-QFWjre-uz2iUbfhQm7` |
| `bienes - U2 - INICIO-v2` | 119 | 7:40 | `19ixdbSZKRGJUiON34WMbouKiIUISA6x9` |

**Cuatro `.srt` se subieron de nuevo el 18 nov por la tarde** (U1 INICIO, U1 CIERRE, U2 CIERRE y U4 CIERRE; los ids de la tabla son
los nuevos y los anteriores están en la papelera): «La respuesta es no.» quedaba pegado a la oración siguiente porque
`srt_de_stt.py` tomaba «no.» por abreviatura de «número». El texto no cambió, solo dónde corta el subtítulo.

Carpetas de Drive: VIDEOS de Bienes (`12Wwl_Vq9CCJVTPN7Y7g7JH0j3b9cDiAT`) › Unidad 1 a 4. Cada `.srt` está también junto a
su video en disco. El profe (Sergio Andrés López Zamora) lee: casi no hay tropiezos y Scribe falló poco («scientifican»
por «se identifican», «comienzo» por «comiso», «FEAP» por «FEAB», «Ley diecisiete cero ocho»).

## Repeticiones que quedaron en cuatro videos entregados el 17 nov

Cuando se equivoca, el profe dice «repito» y vuelve a leer la frase. Son nueve, y el compuesto debió cortarlas:

| video | dónde (tiempo del video) | qué pasa |
|---|---|---|
| U1 – CIERRE | 13:30 a 13:38 | «…vinculados con sus finales. Repito. Este régimen contiene…» |
| U1 – CIERRE | 16:59 a 17:07 | «antecedentes comen-- repito. El examen de registros…» |
| U1 – CIERRE | 22:04 a 22:07 | «Será indispensable dife-- repito.» |
| U2 – INICIO | 6:38 a 6:46 | «relacionando-- repito. Los invito a desarrollar…» (cortada en la `-v2`) |
| U2 – CIERRE | 14:24 a 14:35 | «relacionadas con des-- perdón, repito. En este ámbito…» |
| U2 – CIERRE | 19:24 a 19:27 | «hemos llegado a la-- repito.» |
| U2 – CIERRE | 19:48 a 19:54 | «exige una metodología-- repito.» |
| U2 – CIERRE | 21:01 a 21:29 | lee dos veces el párrafo «Este aprendizaje constituye la base…», sin decir «repito» |
| U4 – CIERRE | 8:58 a 9:03 | «El primer momento corresponde a la… Repito.» |

Los `.srt` de las `-v1` siguen al video tal como está.

- **U2 – INICIO: cortada el 18 nov** con `recortar_entrega.py plan_biu2i 1 2 9553 9741` (188 cuadros, 7,8 s; de 11.227 a
  11.039; 10.987 copiados sin tocar). `bienes - U2 - INICIO-v2.mp4`, `1JS2tznMGDExoQ6BhE0caP0D1f1scTdKq`, comparada byte
  a byte con una copia de servidor; −16,0 LUFS, −3,0 dBTP. Corte directo en 6:38 (el profe cambia de postura).
- **Los tres cierres no se cortan: Sebastián, 18 nov, 12:22: «ese repito no importa».** Se quedan en `-v1`, con los
  «repito» dentro, y sus `.srt` siguen al video. Lo que sigue queda como referencia por si cambia de idea. Salieron de Resolve por la placa NVIDIA (perfil Main,
  un cuadro clave cada 24), y `recortar_entrega.py` codifica los bordes con x264: el SPS no sería el mismo y no se
  pueden pegar. Solo en dos de las ocho repeticiones los dos silencios caen sobre un cuadro clave (se podrían quitar
  copiando, sin codificar nada). Lo limpio es sacar las `-v2` de los másters de 32 Mb/s
  (`D:\DAE\_masters_archivo\CURSO 5 - Bienes en el proceso penal\UNIDAD n\CIERRE`) con la receta (x264 CRF 18) y los
  cortes hechos al codificar, sin tocar Resolve: unos 25 a 40 min de máquina cada uno, y no entran en D: (1,6 GB libres).
