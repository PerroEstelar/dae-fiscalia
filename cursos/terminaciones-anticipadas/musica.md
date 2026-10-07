# La música de la serie

## Cómo se arma

`herramientas/musica/cama_musica.py`. Recibe la pista, el largo del lecho y los
tramos donde hay voz, y entrega un MP3 320 a 48 kHz con **el ducking ya horneado**.

Se hornea, no se automatiza en Resolve, porque **la API de este build no deja
escribir niveles ni keyframes de audio**. El archivo entra a A5 con la ganancia en
cero y no hay que tocar un fader. Si hay que cambiar el balance, se vuelve a correr
el script.

Lo que hace:

1. Decodifica a 48 kHz estéreo y recorta al largo exacto del lecho. Si la pista es
   más corta, la repite con un cruce de 1,5 s.
2. Normaliza a **−26 LUFS**, que es el nivel de hueco.
3. Baja **6 dB** donde hay voz, con rampas de 1 s a cada lado.
4. Entra con un fade de 1,5 s y sale con uno de 2,5 s.
5. Techo a −1 dBTP.

## Los niveles de la serie

```
voz       −19 LUFS
música    −32 LUFS bajo la narración       (13 dB por debajo de la voz)
música    −26 LUFS en los huecos y bajo el bloque de preguntas
```

El bloque de preguntas **no se duckea**: la voz va espaciada y el silencio entre
pregunta y pregunta necesita sostén.

## Lo que quedó puesto

| Caso | Pista | De dónde salió | Lecho | Medido |
|---|---|---|---|---|
| **02** · el doble beneficio | `senormusica81-ambient-neutral-v21` | `D:\FISCALIA\UNIDAD 1\profe carlos humberto\caso 1` | 194 → 4633 · 185,1 s | −32,0 bajo voz · −26,3 en huecos |
| **06** · el hurto de madrugada | `lexin_music-science-documentary` | `D:\DAE\unidad 1\profe edwin\caso B - miradores` | 194 → 3195 · 125,2 s | −32,5 bajo narración · −24,5 bajo preguntas |

Las dos entran con el cartón de entrada y salen con el de cierre, igual que en
`TA - CASO 01 - PLANTILLA`.

**Por qué esas dos.** No las puedo oír: elegí por uso previo en la serie, por
duración y por rango dinámico medido. La de ambiente neutro tiene **LRA 3,2**, el
más plano de las cinco candidatas, que es lo que quiere una narración densa de
cifras y norma. La de documental dura **127,3 s** contra un lecho de 125,2 — entra
casi al segundo, y el tono va con una pieza de investigación.

## Dos cosas para revisar

- **El bloque de preguntas del Caso 06 midió −24,5 y no −26**, porque esa sección de
  la pista es más fuerte de suyo. Es 1,5 dB de más. Si suena alto, se vuelve a correr
  con `objetivo: -27.5`.
- **El ducking del Caso 02 está calculado contra los tramos de voz de la rejilla, no
  contra la voz que metiste vos.** Cuando estén las voces definitivas hay que volver a
  correr el script con los tramos reales, o la música va a bajar donde no hay nadie
  hablando y a subir encima de una frase.
