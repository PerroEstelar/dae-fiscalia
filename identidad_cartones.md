# Identidad en los cartones

## Nada en mayúsculas sostenidas

No se usan versalitas ni mayúsculas sostenidas en ningún cartón de la serie. La
única excepción es la marca de agua **APRENDE CON LA DAE**, y no es una
excepción de verdad: ahí las mayúsculas son parte del logotipo, no una decisión
tipográfica del cartón.

Esto aplica a antetítulos, títulos, cuerpos, cifras, pies de gráfico y al nombre
del caso. Si una palabra necesita peso, se le da con la fuente —Bold, SemiBold—
no con mayúsculas.

En `herramientas/cartones/cartones_ta.py` esto se sostiene no llamando `.upper()`
en ninguna parte del generador. El comentario que hay sobre el antetítulo está
puesto para que no vuelva a aparecer.

## El cartón de entrada

Dos líneas, en la misma retícula de siempre:

```
Caso:                        ← antetítulo, SemiBold 30
“El doble beneficio y el reintegro”   ← título, Bold 54, entre comillas angulares
```

Las comillas son “ ” (U+201C / U+201D), no `"`.

En código:

```python
C.render_carton({"ante": "Caso:", "titulo": "“El hurto de madrugada”"},
                119, C.BLANCO_FONDO, False, salida, con_marca=True)
```

Ya está aplicado en el Caso 02 y en el Caso 06. Para los seis casos que faltan
nace así desde el principio.
