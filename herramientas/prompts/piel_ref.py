# -*- coding: utf-8 -*-
r"""La piel de las REFERENCIAS (Derechos humanos, 31 oct).

Sebastian vio en vivo que la piel de las candidatas se iba saturando. Medido:
siete de las nueve hojas de personaje de Seedream salieron con la piel
durazno-rosada (saturacion mediana 0,22-0,30, tono 15 grados, hasta 11 % de
pixeles rosados; la regla es gris calido, tono ~25, s <= 0,20), y en DH las
placas aprobadas entraban como referencia CRUDAS, no graduadas como en
Justicia restaurativa. Cada placa copiaba la piel de la anterior y la subia
un poco: U2, U4 y U5 llegaron a mediana 0,25 y 3-8 % de rosado.

Toda imagen que se sube a Magnific como referencia (hoja o placa) pasa por
aqui ANTES de subir, sin tocar el archivo de la pieza:
  - banda de piel = tono PIL 0-18 (0-25 grados) con rampa de 3, mas el lado
    magenta del rojo (>= 245). La mostaza vive en 29-33 graduada y en 22-24
    cruda: la rampa termina en 21 y no la toca;
  - saturacion a tope 0,15 dentro de la banda (la regla es 0,20: la
    referencia queda por debajo para que la generacion no la pase);
  - el tono de la banda se acerca a medias a 17 (25 grados): sale gris
    calido, no rojo.
"""
import numpy as np

TOPE = 0.15
TONO = 17.0


def piel_ref(rgb):
    """rgb: PIL.Image RGB -> PIL.Image RGB con la piel de referencia."""
    from PIL import Image
    hsv = np.asarray(rgb.convert('HSV')).astype(np.float32)
    h, s = hsv[..., 0], hsv[..., 1]
    hh = np.where(h >= 245, h - 256.0, h)
    w = np.clip((21.0 - hh) / 3.0, 0, 1) * (hh >= -11)
    s = s - w * np.clip(s - TOPE * 255, 0, None)
    hh = hh + w * 0.5 * (TONO - hh)
    hsv[..., 0] = np.mod(hh, 256.0)
    hsv[..., 1] = s
    return Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV').convert('RGB')


def medir(rgb):
    """p50/p90 de saturacion y % rosado en la banda de piel (para el log)."""
    im = rgb.resize((960, int(rgb.height * 960 / rgb.width)))
    a = np.asarray(im.convert('HSV')).reshape(-1, 3).astype(np.float32)
    h, s, v = a[:, 0], a[:, 1] / 255.0, a[:, 2]
    piel = (h <= 20) & (s > 0.08) & (s < 0.85) & (v > 90) & (v < 245)
    ros = float(((v > 40) & (s > 0.20) & (h <= 12)).mean()) * 100
    if piel.sum() < 300:
        return {'p50': 0, 'p90': 0, 'rosado': round(ros, 2)}
    return {'p50': round(float(np.percentile(s[piel], 50)), 3),
            'p90': round(float(np.percentile(s[piel], 90)), 3),
            'rosado': round(ros, 2)}
