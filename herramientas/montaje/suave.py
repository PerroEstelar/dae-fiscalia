#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quita de la placa lo que el grade no debe amplificar, antes de amplificarlo.

EL PROBLEMA, DESPUES DE ROMPER EL SET TRES VECES
    Las placas del Caso 4 salieron del modelo mucho mas claras y planas que
    las del Caso 3, asi que el grade de la serie tiene que estirarlas casi el
    doble. Al estirar, lo que se ve no es el dibujo: es el grano y el
    escalonado de 8 bits, convertidos en moteado con manchas de color.

    Lo intente tres veces mal antes de dar con esto, y las tres veces la
    medida me dijo que estaba bien:

    1. Anular el tope de dureza. Lo "verifique" sobre el 60 % mas plano del
       cuadro, que en una placa con papel claro ES EL PAPEL. La mesa oscura
       -la que se rompe- nunca entro en la cuenta.
    2. Tramar al cuantizar. Arregla el redondeo final; aqui el dano es la
       AMPLIFICACION, que ocurre antes.
    3. Alisar lo medido como plano y oscuro. Dejo el papel roto por arriba
       -el grano de r08 subio a 12,51 contra 2,25 de la peor aprobada- y al
       quitarle la restriccion de oscuro se comio el texto de r16.

LO QUE SI FUNCIONA: SEPARAR POR AMPLITUD, NO POR SITIO
    El grano y el escalonado son de AMPLITUD PEQUENA -uno a tres niveles- y
    el dibujo de esta serie es de amplitud grande: un canto de mesa, un
    renglon impreso, el borde de una mano son veinte o cuarenta niveles. Asi
    que no hace falta saber DONDE mirar, que es justo lo que llevaba tres
    intentos fallando: basta con quitar el residuo cuya amplitud esta por
    debajo del umbral y dejar intacto todo lo que lo pasa.

    El umbral se mide en cada placa -la mediana del propio residuo por K- asi
    que una placa limpia casi no se toca (r01, T=0,47) y una con grano se
    limpia a fondo (r08, T=6,61).

    Medido sobre las mismas placas con que fallaron los tres intentos, contra
    las aprobadas del Caso 3 (zona clara: medio 1,02 · peor 2,25):

        r08  crudo 3,24   alisando por sitio 12,51   por amplitud 2,06
        r37  crudo 1,25   alisando por sitio  3,66   por amplitud 0,35
        r16  texto intacto, que era lo que el alisado por sitio se comia

Y LA MANCHA DE COLOR VA APARTE
    El moteado que quedaba en r25 y r22 era CROMATICO y una medida de gris no
    lo ve. `alisar_croma` lo quita sin tocar la luma: en este sistema el
    entorno va enteramente en grises, asi que el color de la mesa no es
    dibujo, es error del modelo. El dibujo vive en la luma y la luma no se
    toca. Fuera quedan el acento -croma alto- y la piel -calida-, que son las
    dos unicas cosas que aqui tienen color a proposito.
"""
import numpy as np
from scipy.ndimage import gaussian_filter

SIGMA = 2.0        # escala por debajo de la cual algo es grano y no dibujo
K = 2.5            # cuantas medianas de residuo caben dentro del grano

# EL UMBRAL TIENE QUE SABER CUANTO SE VA A AMPLIFICAR, 21 OCT 2026
#     Con K fijo quedaba grano visible a 1:1 en el papel de r08 -el crudo mas
#     granulado del set- y en ningun otro. No es que K este mal: es que a r08
#     la curva le abre la zona clara x3,8 y a las demas x1,5. El grano que
#     sobrevive al umbral sale multiplicado por eso.
#
#     Lo que hay que acotar es el ruido de SALIDA, no el de entrada, asi que
#     el umbral se escala con la pendiente que le va a caer encima. Una placa
#     que apenas se estira se limpia poco; una que se estira mucho se limpia
#     en proporcion. Es el mismo error de siempre -medir en la poblacion
#     equivocada- visto por tercera vez: antes era el sitio, ahora la escala.
PENDIENTE_NEUTRA = 2.0     # hasta aqui no hace falta limpiar de mas


def quitar_grano(a, sigma=SIGMA, k=K, pendiente=1.0):
    """a: float32 HxWx3 en 0..255. Devuelve (copia limpia, umbral usado)."""
    L = a.mean(axis=2)
    k = k * max(1.0, pendiente / PENDIENTE_NEUTRA)
    T = k * float(np.median(np.abs(L - gaussian_filter(L, sigma))))
    out = np.empty_like(a)
    for c in range(3):
        res = a[..., c] - gaussian_filter(a[..., c], sigma)
        out[..., c] = a[..., c] - np.clip(res, -T, T)
    return out, T


def alisar(a, pendiente=1.0):
    """Nombre de siempre, para no romper a quien ya la llama."""
    return quitar_grano(a, pendiente=pendiente)


# ------------------------------------------------------------------ croma
# EL TERCER PASO, 21 OCT 2026
#     `alisar` solo entra donde la region YA es plana (desviacion local bajo
#     PLANO). En r25 y r22 la mesa oscura trae textura propia, asi que la
#     mascara entro en el 6 % y el 14 % del cuadro y la mancha de color
#     sobrevivio: croma 10,99 y 3,94 contra 4,84 de la peor del Caso 3.
#
#     Pero el sistema de la casa dice que el entorno va ENTERAMENTE EN GRISES.
#     Eso significa que en la mesa oscura la informacion de color no es
#     dibujo: es error del modelo. Se puede alisar sin tope y no se pierde
#     nada, porque el dibujo vive en la LUMA y la luma no se toca.
#
#     Se alisan las dos diferencias de color y se reconstruye el pixel con la
#     luma exacta de antes: R-G y B-G quedan suaves, (R+G+B)/3 queda intacta.
#     Fuera de la mascara quedan el acento -croma alto- y la piel -calida-,
#     que son las dos unicas cosas que en esta serie tienen color a proposito.
UMBRAL_CROMA = 100.0   # igual que arriba: el entorno es gris en todo el rango
CROMA_ACENTO = 25      # por encima de esto es acento, no se toca
CALIDO = 12            # R - B por encima de esto es piel, no se toca
SIGMA_CROMA = 8.0


def alisar_croma(a):
    """Quita la mancha de color de la mitad oscura sin tocar la luma."""
    L = a.mean(axis=2)
    d1 = a[..., 0] - a[..., 1]
    d2 = a[..., 2] - a[..., 1]
    croma = a.max(axis=2) - a.min(axis=2)

    w = ((L <= np.percentile(L, UMBRAL_CROMA))
         & (croma <= CROMA_ACENTO)
         & ((a[..., 0] - a[..., 2]) <= CALIDO)).astype(np.float32)
    w = np.clip(gaussian_filter(w, SIGMA_CROMA * 0.5) * 1.2 - 0.1, 0.0, 1.0)

    s1 = gaussian_filter(d1, SIGMA_CROMA)
    s2 = gaussian_filter(d2, SIGMA_CROMA)
    n1 = d1 * (1 - w) + s1 * w
    n2 = d2 * (1 - w) + s2 * w

    g = L - (n1 + n2) / 3.0
    out = np.stack([g + n1, g, g + n2], axis=2)
    return out, float(w.mean() * 100.0)


# ----------------------------------------------------------- neutralizar
# EL TINTE QUE METE EL PROPIO GRADE, 21 OCT 2026
#     La curva se aplica POR CANAL -tres curvas, una por canal- porque asi
#     mata un dominante alineando los tres en vez de desaturar. El efecto
#     secundario es que si los percentiles de los tres canales no coinciden
#     en el crudo, alinearlos CORRE el entorno hacia un color.
#
#     Medido sobre el set ya graduado con la banda de aceptacion: r28 salio
#     con el fondo verde-azulado en el 40 % del cuadro. El crudo era gris.
#
#     Esto no lo ve `alisar_croma`, que lo unico que hace es quitarle el
#     MOTEADO al color: un tinte uniforme sigue siendo uniforme despues de
#     alisarlo. Hay que restarlo.
#
#     Se resta el tinte del ENTORNO -croma bajo, no calido- y se deja la luma
#     intacta. El acento y la piel quedan fuera por la misma mascara de
#     siempre.
#
#     Y se resta LOCALMENTE, no por media global. La primera version restaba
#     una sola media y bajaba r28 de 39,8 % a 26,2 %: el papel blanco, que es
#     medio cuadro y no tiene tinte, entraba en la media y la diluia. El
#     tinte no esta repartido por igual, asi que lo que se resta es el propio
#     tinte pasado por un filtro muy ancho -la parte que varia despacio- y no
#     un numero. Lo que varia deprisa es dibujo y se queda.
SIGMA_TINTE = 60.0         # ancho del filtro: por debajo de esto ya es dibujo

# LA PIEL NO SE DEJA FUERA CON UN NUMERO FIJO, 21 OCT 2026
#     CALIDO = 12 bastaba para el moteado, y se comio la mano de r37: en esa
#     placa la mano vive entre 4 y 12 de R-B -es una mano en penumbra sobre
#     papel claro- asi que entro en la poblacion del entorno y salio gris. La
#     poblacion calida de la placa paso del 6,09 % al 0,08 % y `piel.medir`
#     dejo de encontrarla.
#
#     El umbral no puede ser fijo por la misma razon de siempre: no describe
#     a la piel, describe a la piel de algunas placas. Asi que la piel se
#     deja fuera MIDIENDOLA, con el mismo localizador que ya usa piel.py, y
#     el numero fijo queda solo como red de seguridad.
CALIDO_SUAVE = 3           # red: por encima de esto ya es sospechoso de piel


def _mascara_piel(a):
    """Los pixeles que `piel.py` llamaria piel en esta placa, o ninguno."""
    import piel
    from PIL import Image
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    m = piel.medir(im)
    if m is None:
        return np.zeros(a.shape[:2], dtype=bool)
    mx, mn = a.max(axis=2), a.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1.0), 0.0)
    import colorsys
    # tono en grados, vectorizado a mano para no pagar colorsys por pixel
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    d = np.maximum(mx - mn, 1e-6)
    h = np.where(mx == r, ((g - b) / d) % 6,
        np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60.0
    dist = np.abs(((h - m["tono"] + 180) % 360) - 180)
    return (dist <= piel.VENTANA) & (sat >= piel.SAT_MIN) & (sat <= piel.SAT_MAX)


def neutralizar_entorno(a):
    """Lleva el entorno a gris de verdad sin tocar acento, piel ni luma."""
    L = a.mean(axis=2)
    d1 = a[..., 0] - a[..., 1]
    d2 = a[..., 2] - a[..., 1]
    croma = a.max(axis=2) - a.min(axis=2)

    w = ((croma <= CROMA_ACENTO)
         & ((a[..., 0] - a[..., 2]) <= CALIDO_SUAVE)
         & ~_mascara_piel(a)).astype(np.float32)
    if w.mean() < 0.10:
        return a, (0.0, 0.0)
    wb = gaussian_filter(w, SIGMA_TINTE) + 1e-6
    t1 = gaussian_filter(d1 * w, SIGMA_TINTE) / wb
    t2 = gaussian_filter(d2 * w, SIGMA_TINTE) / wb
    m1, m2 = float((d1 * w).sum() / w.sum()), float((d2 * w).sum() / w.sum())
    w = np.clip(gaussian_filter(w, 4.0) * 1.2 - 0.1, 0.0, 1.0)

    n1 = d1 - t1 * w
    n2 = d2 - t2 * w
    g = L - (n1 + n2) / 3.0
    return np.stack([g + n1, g, g + n2], axis=2), (m1, m2)
