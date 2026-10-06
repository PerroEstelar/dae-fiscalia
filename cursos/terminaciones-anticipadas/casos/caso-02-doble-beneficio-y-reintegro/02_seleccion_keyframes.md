# Caso 02 · Selección de keyframes y b-roll

Generados en Magnific con **Seedream 5 Pro**, 2560 × 1440, dos variantes por plano
(`_vA` / `_vB`), mismo bloque de estilo y mismo negativo base que están en
`01_guion_y_prompts.md`. Las dos variantes quedan en disco; abajo está la elegida y
el motivo. El KF 06 no se generó: es placa limpia de After Effects.

**Dónde viven los archivos** (no entran al repo: son PNG de ~8 MB cada uno)

```
E:\DAE MASTER\CURSO 4 - Curso Terminaciones Anticipadas\
  CASO 02 - doble beneficio y reintegro\
    01 PLANOS\   KF01..KF11  _vA.png / _vB.png  +  <plano>_hold.mp4
    04 B-ROLL\   BR01..BR04  _vA.png / _vB.png  +  <plano>_hold.mp4
```

Los `_hold.mp4` son sostenidos de **16 s a 23,976 fps**: un PNG suelto entra a Resolve
con 24 frames y no hay forma de estirarlo por script, así que el plano entra siempre
como clip de video.

---

## Los elegidos

| Plano | Variante | Por qué |
|---|---|---|
| **KF 01** · La oficina de contratación | **vB** | Carlos claramente girado hacia la ventana y la mano apoyada plana sobre la carpeta abierta; las dos carpetas cerradas leen mejor en el primer término. |
| **KF 02** · La entrega | **vA** | El hallazgo del plano: una mano se retira en alto, la otra todavía viene en bajo. La vB es simétrica y las dos manos llegan igual — se pierde el medio segundo. |
| **KF 03** · La bodega | **vA** | La caja es alta y gris, con la proporción de «instrumento de pie»; en la vB es un cartón cuadrado y café, que mete un acento cálido que no queremos. |
| **KF 04** · El abogado propone | **vA** | El hombro de la fiscal recortado contra el borde derecho y desenfocado, que es la geometría pedida. La palma abierta sobre la mesa está limpia. |
| **KF 05** · Andrés escucha | **vB** | En la vA mira a cámara. En la vB mira la mesa, que es el punto entero del plano: el que acepta responsabilidad no es el que habla. |
| **KF 07** · El código abierto | **vA** | El índice presiona la página y la otra mano descansa plana sobre el expediente cerrado. En la vB el dedo queda levantado y señala. |
| **KF 08** · Antes de sentarse | **vA** | De pie detrás de su propia silla, sin haberla corrido; el abanico de documentos patrimoniales lee bien y el reloj está sin numerales. |
| **KF 09** · La carpeta cerrada | **vA** | La mano cubre la carpeta sin tomarla, y la hoja del centro con dos manos cerca y ninguna encima queda clara. El azul de Andrés entra recortado. |
| **KF 10** · El facilitador | **vB** | La vA trae un halo blanco de recorte alrededor de la figura. La vB está limpia y la mirada a cámara es igual de directa. |
| **KF 11** · El acta sin firmar | **vB** | La silla del frente corrida y girada, que es lo que dice que alguien se fue sin firmar. Los dos esferos quedan paralelos y sin destapar. |
| **BR 01** · Las hojas del expediente | **vA** | La hoja a media vuelta, arqueada, sin texto legible. |
| **BR 02** · El corredor | **vA** | Tres figuras a distancias distintas, ninguna hacia cámara, foco en el vacío del medio. |
| **BR 03** · Las cajas | **vA** | Una sola estiba alta y limpia, cartones sin marca, el operario lejos y de espaldas. |
| **BR 04** · La mesa vacía | **vA** | Sillas simples y grises, coherentes con el cuarto de KF 08 y KF 11; la vB trae sillas de oficina con rodachines que no pertenecen a ese cuarto. |

---

## Lo que quedó pendiente de revisar en pantalla grande

- **KF 07 y KF 08**: la fiscal queda con la mirada un poco más hacia cámara de lo
  pedido. No molesta en movimiento, pero si en la timeline se siente, se regenera
  reforzando «she is looking down, never toward the camera».
- **BR 04**: ninguna de las dos variantes dejó una silla corrida y girada. Si el
  cierre la necesita, se pide de nuevo ese detalle solo.
- **KF 06** sigue pendiente: es gráfico de After Effects, no de Magnific.

## Lo que sigue

1. Revisar los sostenidos en la timeline y confirmar el reparto de frames de la rejilla.
2. Escribir los **prompts de movimiento** contra la imagen real — no contra la
   imaginada — ahora que los planos existen.
3. Montar el gráfico del KF 06 en After Effects.
