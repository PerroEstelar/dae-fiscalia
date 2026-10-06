#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones azules para MA - U1 - INTRODUCCION.

Misma retícula medida de la serie JEP:
  barra  #FEB900, 14 px, borde izquierdo x=175
  texto  Montserrat, borde izquierdo x=243
  centro óptico y=590 · MAXW 1330 · sangría 62 · BAR_PAD 64
  título Bold 58 · cuerpo Medium 48 · frase suelta Bold 64
  tinte  #03398B al 46 % (alfa 117/255)
  fundidos 12 f de entrada, 10 f de salida

Las posiciones son frames del CLIP de la unidad (no de la línea de tiempo).
En la timeline hay que sumarles 194: el clip arranca ahí.
"""
from PIL import Image, ImageDraw, ImageFont
import subprocess, os, json

FPS = 24000 / 1001
FT = "/usr/share/fonts/truetype/montserrat/Montserrat-%s.ttf"
BOLD, MED = FT % "Bold", FT % "Medium"

W, H = 1920, 1080
BAR_X, BAR_W, BAR_C = 175, 14, (254, 185, 0, 255)
TEXT_X, CENTER_Y = 243, 590
BAR_PAD, MAXW, SANGRIA = 64, 1330, 62
WHITE = (255, 255, 255, 255)
AZUL, ALFA_AZUL = (3, 57, 139), 117
ENTRA, SALE = 12, 10

OUT = "/home/claude/ma/out"
os.makedirs(OUT, exist_ok=True)


def wrap(d, text, font, maxw):
    out, line = [], ""
    for w in text.split():
        probe = (line + " " + w).strip()
        if d.textlength(probe, font=font) <= maxw or not line:
            line = probe
        else:
            out.append(line); line = w
    if line:
        out.append(line)
    return out


def build(lines):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    laid, y = [], 0
    for text, weight, px, gap in lines:
        ft = ImageFont.truetype(BOLD if weight == "bold" else MED, px)
        y += gap
        sangra = text[:1] in "123456789" and text[1:2] == "."
        for i, ln in enumerate(wrap(d, text, ft, MAXW - (SANGRIA if sangra else 0))):
            laid.append((ln, ft, y, SANGRIA if (sangra and i) else 0))
            y += int(px * 1.32)
    total = y - int(lines[-1][2] * 0.32)
    off = CENTER_Y - total // 2
    for ln, ft, yy, dx in laid:
        d.text((TEXT_X + dx, off + yy), ln, font=ft, fill=WHITE)
    d.rectangle([BAR_X, off - BAR_PAD, BAR_X + BAR_W, off + total + BAR_PAD], fill=BAR_C)
    return img, total


def con_azul(txt):
    base = Image.new("RGBA", (W, H), AZUL + (ALFA_AZUL,))
    base.alpha_composite(txt)
    return base


def render(img, frames, out):
    tmp = "/tmp/claude-0/ma"
    os.makedirs(tmp, exist_ok=True)
    src = f"{tmp}/_f.png"
    img.save(src)
    vf = (f"fade=t=in:st=0:d={ENTRA/FPS:.4f}:alpha=1,"
          f"fade=t=out:st={(frames-SALE)/FPS:.4f}:d={SALE/FPS:.4f}:alpha=1")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1",
                    "-framerate", "24000/1001", "-i", src,
                    "-frames:v", str(frames), "-vf", vf,
                    "-c:v", "qtrle", "-pix_fmt", "argb", "-r", "24000/1001",
                    out], check=True)


# ---------------------------------------------------------------------------
# (nombre, frame del clip donde entra, duración en frames, líneas)
CARTONES = [
 ("c01_unidad", 975, 265, [
    ("Unidad 1", "bold", 58, 0),
    ("Desafíos del Derecho Penal Ambiental y la Constitución Ecológica", "med", 48, 38)]),

 ("c02_al_finalizar", 1470, 300, [
    ("Al finalizar esta unidad", "bold", 58, 0),
    ("Aplicar el marco normativo, institucional y dogmático de protección de "
     "los recursos naturales.", "med", 48, 38)]),

 ("c03_sina", 1860, 290, [
    ("Evaluar la intervención", "bold", 58, 0),
    ("Del derecho penal y del Sistema Nacional Ambiental — SINA — frente a los "
     "daños ecológicos y la explotación ilícita.", "med", 48, 38)]),

 ("c04_cinco_lecciones", 2330, 195, [
    ("Cinco lecciones", "bold", 64, 0)]),

 ("c05_leccion1", 2650, 310, [
    ("Lección 1 · Problemáticas del daño al medio ambiente", "bold", 58, 0),
    ("Deforestación · Explotación ilícita · Vinculación de grupos armados",
     "med", 48, 38)]),

 ("c06_leccion2", 3320, 300, [
    ("Lección 2 · La Constitución Ecológica", "bold", 58, 0),
    ("Base fundamental del derecho penal ambiental y referente de la actuación "
     "del Estado.", "med", 48, 38)]),

 ("c07_leccion3", 3880, 290, [
    ("Lección 3 · El Sistema Nacional Ambiental", "bold", 58, 0),
    ("Entidades, institutos, órganos y competencias.", "med", 48, 38)]),

 ("c08_leccion4", 4660, 265, [
    ("Lección 4 · Los ecosistemas", "bold", 58, 0),
    ("Sujetos de protección especial.", "med", 48, 38)]),

 ("c09_leccion5", 5100, 300, [
    ("Lección 5 · Daño ambiental y daño ecológico", "bold", 58, 0),
    ("La distinción que permite comprender las formas de afectación y sus "
     "efectos.", "med", 48, 38)]),

 ("c10_actividades", 5950, 340, [
    ("Las actividades", "bold", 58, 0),
    ("1. Video introductorio sobre problemáticas ambientales y criminalidad",
     "med", 48, 38),
    ("2. Análisis de casos: economías ilícitas y minería ilegal", "med", 48, 14)]),

 ("c11_material_dema", 6870, 330, [
    ("También encontrarán", "bold", 58, 0),
    ("3. Material virtual de fundamentación conceptual y jurídica", "med", 48, 38),
    ("4. Conversatorio institucional con la DEMA", "med", 48, 14)]),

 ("c12_cierre", 7790, 330, [
    ("Al cerrar la unidad", "bold", 58, 0),
    ("5. Video integrador de repaso", "med", 48, 38),
    ("6. Actividad evaluativa de consolidación de conceptos", "med", 48, 14)]),
]


if __name__ == "__main__":
    plan, prev = [], 0
    print(f"{'cartón':22} {'clip':>6} {'tl':>6} {'dura':>5} {'seg':>6} {'hueco':>6} {'alto':>5}")
    for nom, a, n, lineas in CARTONES:
        txt, alto = build(lineas)
        render(con_azul(txt), n, f"{OUT}/MA_U1_{nom}_AZUL.mov")
        render(txt, n, f"{OUT}/MA_U1_{nom}_ALFA.mov")
        hueco = a - prev
        print(f"{nom:22} {a:6d} {a+194:6d} {n:5d} {n/FPS:6.1f} {hueco/FPS:6.1f}"
              f" {alto:5d}" + ("   <-- SE SALE" if alto > 760 else ""))
        prev = a + n
        plan.append([nom, a, n])
    cubierto = sum(n for _, _, n in plan)
    print(f"\n{len(plan)} cartones · {cubierto} f en pantalla de 9220 "
          f"({100*cubierto/9220:.0f} % del clip)")
    json.dump(plan, open('/home/claude/ma/plan_u1.json', 'w'), ensure_ascii=False)
