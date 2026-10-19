#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las dos gráficas de motion del Caso 1: la línea de tiempo y el mapa.

LA CUARTA FAMILIA
    Sebastián la pidió por su nombre en la revisión: «hay un tipo de plano
    nuevo, motion graphics de documental — si hablan de una trayectoria
    sobre el mapa de Colombia, muestre el mapa y dibuje la trayectoria».
    Estas dos ocupan la ranura entera, a cuadro completo, y no llevan
    cartón encima: la gráfica ES el cartón.

EL MAPA SALE DE LA PLACA, PERO NO ES LA PLACA
    `P3C1_br07_mapa_colombia.png` se generó como silueta y midió razón de
    dureza 3,81: el fondo es una textura moteada que no es de la casa. De
    ahí sólo se toma la SILUETA -un umbral sobre el brillo- y se vuelve a
    dibujar plana sobre azul noche. Así la gráfica queda limpia y la placa
    moteada no entra al montaje.

LA TRAYECTORIA QUE SE DIBUJA ES LA ÚNICA QUE EL CASO ENUNCIA
    Daniela viajó desde Cúcuta. Es el único desplazamiento con origen
    nombrado en el documento, y es el único que se dibuja. Las demás
    llegadas existen pero el texto no dice de dónde, y la regla de la casa
    es que el cartón no afirma lo que la fuente no enuncia. El mapa dice
    entonces lo que sí dice el guion: todo ocurrió dentro de Colombia.

LAS POSICIONES SON APROXIMADAS Y ASÍ ESTÁ DICHO
    La silueta no es una proyección: es un dibujo. Los puntos se colocan
    por latitud y longitud sobre la caja de la silueta, lo que es exacto
    para leer «noreste, cerca de la frontera» y no para medir distancias.
    Para lo que la gráfica tiene que decir, alcanza.

LOS NUMEROS VAN EN DIGITOS, NO EN LETRAS
    Peticion de Sebastian: en PANTALLA todo numero -el ano, la edad, el dia,
    las horas, la suma- va en digitos. «2025», no «dos mil veinticinco»;
    «23 anos», no «veintitres anos». Se lee de un vistazo, que es justo lo que
    un carton tiene que permitir.

    La LOCUCION no cambia: ahi el numero sigue escrito en letras, porque el
    texto de voz es lo que el sintetizador pronuncia y en digitos lo lee mal.
    Son dos escrituras del mismo dato y cada una sirve a su medio.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

W, H = 1920, 1080
FPS = "24000/1001"
OUT = "/mnt/user-data/outputs/cartones_p3c1"
PLACA_MAPA = "/mnt/user-data/uploads/DAE/_tmp/P3C1_br07_mapa_colombia.png"

FONDO = C.AZUL_NOCHE
TIERRA = (206, 209, 214)
AMARILLO = (252, 181, 0)
BLANCO = (255, 255, 255)

# extremos continentales de Colombia, para colocar los puntos sobre la caja
LON_O, LON_E = -79.0, -66.85
LAT_S, LAT_N = -4.23, 12.46
CIUDADES = {"Cúcuta": (7.89, -72.50), "Bucaramanga": (7.12, -73.12)}


def _silueta(caja):
    """Umbral sobre el brillo de la placa -> máscara de la silueta, recortada
    a su propia caja y escalada para caber en `caja` (x, y, an, al)."""
    im = Image.open(PLACA_MAPA).convert("L")
    # El umbral NO puede ser un numero fijo: la placa viene graduada y su
    # blanco real llego a 163, no a 255. Se saca del propio histograma, a
    # medio camino entre el fondo y el valor mas alto que existe.
    h = im.histogram()
    alto = max(i for i, v in enumerate(h) if v > 0)
    acum, mitad, fondo = 0, sum(h) * 0.5, 0
    for i, v in enumerate(h):
        acum += v
        if acum >= mitad:
            fondo = i
            break
    m = im.point(lambda v, u=(fondo + alto) // 2: 255 if v > u else 0).convert("L")
    bb = m.getbbox()
    m = m.crop(bb)
    bx, by, ban, bal = caja
    k = min(ban / float(m.width), bal / float(m.height))
    nm = m.resize((int(m.width * k), int(m.height * k)), Image.LANCZOS)
    off = (bx + (ban - nm.width) // 2, by + (bal - nm.height) // 2)
    return nm, off, bb, k


def _punto(lat, lon, bb, k, off):
    """lat/lon -> pixel, sobre la caja ORIGINAL de la silueta ya escalada."""
    x0, y0, x1, y1 = bb
    fx = (lon - LON_O) / (LON_E - LON_O)
    fy = (LAT_N - lat) / (LAT_N - LAT_S)
    return (off[0] + fx * (x1 - x0) * k, off[1] + fy * (y1 - y0) * k)


def _escritor(salida, n):
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    return subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", "%dx%d" % (W, H), "-r", FPS, "-i", "-", "-an", "-c:v", "libx264",
         "-preset", "slow", "-crf", "12", "-pix_fmt", "yuv420p", "-g", "600",
         "-keyint_min", "600", "-sc_threshold", "0", salida], stdin=subprocess.PIPE)


def _tramo(f, a, b):
    """0 antes de `a`, 1 después de `b`, con ease_out_cubic en medio."""
    if f <= a:
        return 0.0
    if f >= b:
        return 1.0
    return C.ease_out_cubic((f - a) / float(b - a))


def _texto(d, lineas, x, ys, f, desde, paso):
    for i, ((txt, font, sz, _, sg), y) in enumerate(zip(lineas, ys)):
        t = _tramo(f, desde + i * paso, desde + i * paso + 10)
        if t <= 0.004:
            continue
        dy = int(12 * (1 - t))
        d.text((x + sg, y + dy), txt, font=font,
               fill=BLANCO + (int(255 * t),))


def _bloque(spec, x, centro_y, maxw):
    """Arma las líneas de un spec de la casa y devuelve (líneas, ys, barra)."""
    probe = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    viejo, C.MAXW = C.MAXW, maxw
    lineas = C.armar_lineas(spec, probe)
    C.MAXW = viejo
    alturas = [int(sz * C.INTERLINEA) for (_, _, sz, _, _) in lineas]
    gaps = [g for (_, _, _, g, _) in lineas]
    top = centro_y - (sum(alturas) + sum(gaps)) // 2
    ys, y = [], top
    for h, g in zip(alturas, gaps):
        y += g
        ys.append(y)
        y += h
    return lineas, ys, (top - C.BAR_PAD, y + C.BAR_PAD - int(alturas[-1] * 0.22))


# ------------------------------------------------------------------ ae07
def linea_tiempo(n=124, salida=None):
    salida = salida or "%s/P3C1_ae07_linea_tiempo.mov" % OUT
    spec = {"ante": "Sin interrupción",
            "titulo": "Enero de 2025 · septiembre de 2026"}
    lineas, ys, (bt, bb_) = _bloque(spec, C.TEXT_X, 430, 1250)

    EJE_Y, EJE_X0, EJE_X1 = 740, C.TEXT_X, 1671
    MESES = 21                      # enero 2025 .. septiembre 2026, inclusive
    f_med = C.fuente(C.F_MED, 30)
    p = _escritor(salida, n)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)
        d = ImageDraw.Draw(im, "RGBA")

        d.rectangle([C.BAR_X, bt, C.BAR_X + C.BAR_W - 1,
                     bt + int((bb_ - bt) * _tramo(f, 0, 10))], fill=AMARILLO)
        _texto(d, lineas, C.TEXT_X, ys, f, 2, 1)

        # el riel, y encima la barra que lo recorre
        ap = _tramo(f, 14, 26)
        if ap > 0:
            d.rectangle([EJE_X0, EJE_Y - 3, EJE_X0 + int((EJE_X1 - EJE_X0) * ap),
                         EJE_Y + 3], fill=(255, 255, 255, 46))
        av = _tramo(f, 28, n - 34)
        if av > 0:
            d.rectangle([EJE_X0, EJE_Y - 3, EJE_X0 + int((EJE_X1 - EJE_X0) * av),
                         EJE_Y + 3], fill=AMARILLO)
        # una marca por mes, que aparecen a medida que la barra las alcanza
        for i in range(MESES):
            fx = i / float(MESES - 1)
            if fx > ap:
                continue
            x = EJE_X0 + fx * (EJE_X1 - EJE_X0)
            alto = 20 if i in (0, MESES - 1) else 10
            col = AMARILLO if fx <= av else (255, 255, 255, 70)
            d.rectangle([x - 1, EJE_Y - alto, x + 1, EJE_Y + alto], fill=col)
        for x, txt, anc in ((EJE_X0, "enero de 2025", "l"),
                            (EJE_X1, "septiembre de 2026", "r")):
            t = _tramo(f, 30, 44)
            if t > 0.004:
                an = d.textlength(txt, font=f_med)
                d.text((x if anc == "l" else x - an, EJE_Y + 40), txt,
                       font=f_med, fill=BLANCO + (int(220 * t),))
        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(os.path.basename(salida), n, "f", os.path.getsize(salida) // 1024, "KB")


# ------------------------------------------------------------------ ae11
def mapa(n=221, salida=None):
    salida = salida or "%s/P3C1_ae11_las_nueve.mov" % OUT
    spec = {"ante": "9 personas",
            "titulo": "Un solo hospedaje",
            "cuerpo": "Y ninguna en la misma situación"}
    lineas, ys, (bt, bb_) = _bloque(spec, C.TEXT_X, 560, 700)

    sil, off, bb, k = _silueta((1040, 120, 560, 840))
    X_ROT = 1660          # donde empiezan los rotulos, ya fuera de la tierra
    cu = _punto(*CIUDADES["Cúcuta"], bb=bb, k=k, off=off)
    bu = _punto(*CIUDADES["Bucaramanga"], bb=bb, k=k, off=off)

    tierra = Image.new("RGB", sil.size, TIERRA)
    f_med = C.fuente(C.F_MED, 28)
    f_semi = C.fuente(C.F_SEMI, 30)
    p = _escritor(salida, n)
    for f in range(n):
        im = Image.new("RGB", (W, H), FONDO)

        t = _tramo(f, 0, 22)
        if t > 0.004:
            m = sil.point(lambda v, a=t: int(v * a))
            im.paste(tierra, off, m)
        d = ImageDraw.Draw(im, "RGBA")

        # Cúcuta: el punto, la guia y el rotulo
        #
        # Los dos rotulos salen de la tierra y se leen sobre el azul. Puestos
        # encima de la silueta quedaban blancos sobre gris claro, que no se
        # lee; y la casa no usa caja detras del texto. La guia amarilla es la
        # que los amarra a su punto.
        tc = _tramo(f, 26, 40)
        if tc > 0.004:
            r = 9 * tc
            d.ellipse([cu[0] - r, cu[1] - r, cu[0] + r, cu[1] + r], fill=AMARILLO)
            y_cu = cu[1] - 90
            d.line([(cu[0] + 10, cu[1]), (X_ROT - 26, cu[1]),
                    (X_ROT - 14, y_cu), (X_ROT, y_cu)],
                   fill=AMARILLO + (int(255 * tc),), width=3)
            d.text((X_ROT + 4, y_cu - 20), "Cúcuta", font=f_semi,
                   fill=BLANCO + (int(235 * tc),))

        # la trayectoria, que se dibuja
        tv = _tramo(f, 44, 96)
        if tv > 0.004:
            d.line([cu, (cu[0] + (bu[0] - cu[0]) * tv, cu[1] + (bu[1] - cu[1]) * tv)],
                   fill=AMARILLO, width=5)

        tb = _tramo(f, 92, 108)
        if tb > 0.004:
            r = 11 * tb
            d.ellipse([bu[0] - r, bu[1] - r, bu[0] + r, bu[1] + r], fill=AMARILLO)
            # el anillo que se abre una vez y se apaga
            ta = _tramo(f, 96, 140)
            if 0 < ta < 1:
                ra = 11 + 52 * ta
                d.ellipse([bu[0] - ra, bu[1] - ra, bu[0] + ra, bu[1] + ra],
                          outline=AMARILLO + (int(210 * (1 - ta)),), width=3)
            y_bu = bu[1] + 110
            d.line([(bu[0] + 12, bu[1]), (X_ROT - 26, bu[1]),
                    (X_ROT - 14, y_bu), (X_ROT, y_bu)],
                   fill=AMARILLO + (int(255 * tb),), width=3)
            d.text((X_ROT + 4, y_bu - 22), "Bucaramanga", font=f_semi,
                   fill=BLANCO + (int(235 * tb),))
            d.text((X_ROT + 4, y_bu + 16), "el hospedaje", font=f_med,
                   fill=BLANCO + (int(165 * tb),))

        tt = _tramo(f, 118, 130)
        if tt > 0.004:
            d.rectangle([C.BAR_X, bt, C.BAR_X + C.BAR_W - 1,
                         bt + int((bb_ - bt) * tt)], fill=AMARILLO)
        _texto(d, lineas, C.TEXT_X, ys, f, 122, 3)

        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()
    print(os.path.basename(salida), n, "f", os.path.getsize(salida) // 1024, "KB")


if __name__ == "__main__":
    linea_tiempo()
    mapa()
