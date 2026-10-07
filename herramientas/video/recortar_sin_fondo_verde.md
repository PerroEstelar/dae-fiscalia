# Recortar una persona sin fondo verde, sin castigar la GPU

Probado el 7 de octubre de 2026 contra un clip de WhatsApp de 832×464, 41 s,
con un señor de pelo gris largo sobre un edificio de ladrillo. El pelo es
justo donde la Magic Mask se rompe.

## Por qué no Magic Mask

No es que recorte mal: es que **la recalcula cada vez que tocas el clip**, y
la V2 de Resolve 20 pide más VRAM de la que tiene una GTX 970 de 4 GB. El día
de la prueba el log repetía `cuMemAlloc failed 801` cientos de veces, con
870 MB libres de VRAM y Chrome, Spotify, WhatsApp, Telegram y nueve servicios
de ReasonLabs abiertos.

## Robust Video Matting

Modelo de 15 MB, hecho específicamente para recortar personas en video sin
croma. Lo que lo distingue de los recortadores por imagen (U²-Net, rembg) es
que **lleva estado recurrente entre cuadros**: el borde no parpadea, que es
exactamente el defecto que arruina el pelo.

- Pesos ONNX: `rvm_mobilenetv3_fp32.onnx`, de las releases de
  `PeterL1n/RobustVideoMatting`.
- Corre con `onnxruntime` en CPU. No necesita torch ni GPU.
- **Medido: 5,3 cuadros/s en el contenedor, 1 240 cuadros en 236 s.**

`herramientas/video/mattear.py` toma el video y escribe un ProRes 4444 con
alfa recto. El `fgr` que devuelve el modelo ya trae descontado el derrame de
color del fondo viejo, así que no hay que despillar aparte.

```
python3 mattear.py <entrada> <salida.mov> <ancho> <alto> <cuadros> <fps> [ratio]
```

El `ratio` es cuánto se reduce la imagen para el paso neuronal. RVM pide que
el lado largo del reducido quede cerca de 512: para 832 de ancho, 0.6.

## El ProRes 4444 no cabe por el puente

41 s a 832×464 dieron **862 MB**, y `device_commit_files` admite 30 MB por
archivo. La vuelta que funciona:

1. En el contenedor, partir el ProRes en dos H.264 `yuv444p` (sin submuestreo
   de croma, que es lo que destroza los bordes):
   - color: `-crf 13` → 14 MB
   - alfa: `-vf alphaextract,format=gray -crf 10` → 1,2 MB
2. Mandar esas dos piezas.
3. Re-armar allá con un solo ffmpeg:

```
ffmpeg -i _fgr.mp4 -i _alpha.mp4 \
  -filter_complex "[0:v]format=rgba[c];[1:v]format=gray[a];[c][a]alphamerge[v]" \
  -map "[v]" -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le \
  -alpha_bits 16 -vendor apl0 -r 30 salida.mov
```

De 862 MB a 15 MB de transferencia, sin pérdida visible.

## Dos tropiezos de la prueba

- **Un encode que se pasa del límite de tiempo deja el .mp4 sin `moov atom`**
  y el archivo no abre. El síntoma es `moov atom not found`. Siempre verificar
  con `-count_frames` antes de usarlo, no por tamaño.
- **Comparar bytes para validar una transferencia no sirve**: los archivos
  llegaron con 5 875 bytes de más y estaban perfectos. Lo que vale es contar
  cuadros decodificando.

## Lo que aplica a cualquier recorte en Resolve

Hornea la máscara una sola vez. Magic Mask en la página **Color** (no en
Fusion, que carga el análisis entero en VRAM), exportar a ProRes 4444 con
alfa, reimportar, y editar con ese archivo. A partir de ahí la GPU no vuelve
a calcular nada.

Y matear a resolución de fuente, no de línea: un clip de 832×464 en una línea
de 1080 se analiza a 1920×1080, cinco veces más píxeles para nada.
