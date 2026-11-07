# -*- coding: utf-8 -*-
# 7 nov (DA V02 r05, Sebastian: «el mapa de Colombia no esta accurate»):
# Seedream dibuja una Colombia inventada. La placa se pide con la pizarra en
# blanco (la r05 como referencia, «solo cambia: la pizarra esta vacia») y el
# mapa se dibuja encima con los departamentos de Natural Earth, multiplicado
# sobre la luz de la placa para que conserve la franja de sol.
#   python mapa_pizarra_da.py pizarra_blanca.png colombia_dptos.geojson salida.png
import json, math, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BASE, GEO, SAL = sys.argv[1], sys.argv[2], sys.argv[3]
base = Image.open(BASE).convert('RGB')
W, H = base.size
SS = 2                                     # supersampling
g = json.load(open(GEO, encoding='utf-8'))

def polis(f):
    gm = f['geometry']
    ps = gm['coordinates'] if gm['type'] == 'MultiPolygon' else [gm['coordinates']]
    for p in ps:
        ring = p[0]
        lon = sum(x for x, _ in ring) / len(ring); lat = sum(y for _, y in ring) / len(ring)
        if (lon < -78.5 and lat > 11) or lon < -80:   # San Andres, Providencia y Malpelo: fuera
            continue
        yield ring

anillos = [[r for r in polis(f)] for f in g['features']]
todos = [pt for a in anillos for r in a for pt in r]
lon0, lon1 = min(p[0] for p in todos), max(p[0] for p in todos)
lat0, lat1 = min(p[1] for p in todos), max(p[1] for p in todos)
k = math.cos(math.radians((lat0 + lat1) / 2))
ancho_geo, alto_geo = (lon1 - lon0) * k, (lat1 - lat0)
ALTO = 920
esc = ALTO / alto_geo
CX, TOP = 1600, 150
x0 = CX - ancho_geo * esc / 2

def xy(lon, lat):
    return ((x0 + (lon - lon0) * k * esc) * SS, (TOP + (lat1 - lat) * esc) * SS)

# capas en escala de grises: 255 = no oscurece
relleno = Image.new('L', (W * SS, H * SS), 255)
lineas = Image.new('L', (W * SS, H * SS), 255)
borde = Image.new('L', (W * SS, H * SS), 255)
sombra = Image.new('L', (W * SS, H * SS), 0)
dr, dl, db, ds = (ImageDraw.Draw(i) for i in (relleno, lineas, borde, sombra))
for a in anillos:
    for r in a:
        pts = [xy(*p) for p in r]
        dr.polygon(pts, fill=int(255 * 0.93))
        ds.polygon([(x + 10 * SS, y + 12 * SS) for x, y in pts], fill=255)
        dl.line(pts + [pts[0]], fill=int(255 * 0.70), width=3 * SS, joint='curve')
# el contorno del pais: la union de los relleno, dibujado como borde grueso
mask = Image.new('L', (W * SS, H * SS), 0)
dm = ImageDraw.Draw(mask)
for a in anillos:
    for r in a:
        dm.polygon([xy(*p) for p in r], fill=255)
dil = mask.filter(ImageFilter.MaxFilter(2 * 3 * SS + 1))
ero = mask.filter(ImageFilter.MinFilter(2 * 2 * SS + 1))
contorno = np.asarray(dil, np.float32) - np.asarray(ero, np.float32)
borde = Image.fromarray((255 - contorno * (1 - 0.46)).clip(0, 255).astype(np.uint8))

def baja(im):
    return np.asarray(im.resize((W, H), Image.LANCZOS), np.float32) / 255.0

m = baja(relleno) * baja(lineas) * baja(borde)
sh = baja(sombra.filter(ImageFilter.GaussianBlur(14 * SS)))
m = m * (1 - 0.10 * sh * (baja(mask) < 0.5))
out = np.asarray(base, np.float32) * m[..., None]
img = Image.fromarray(out.clip(0, 255).astype(np.uint8))

# alfileres: sur y costa pacifica (como pedia el plano)
PINES = [(-76.6, 0.7), (-74.6, 1.4), (-78.6, 1.7), (-77.2, 5.4), (-72.6, 2.4)]
capa = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0))
dc = ImageDraw.Draw(capa)
sc = Image.new('L', (W * SS, H * SS), 0)
dsc = ImageDraw.Draw(sc)
for lon, lat in PINES:
    px, py = xy(lon, lat)
    R = 19 * SS
    hx, hy = px, py - 46 * SS                     # la cabeza, arriba de la punta
    dsc.ellipse([px + 4 * SS, py - 4 * SS, px + 30 * SS, py + 6 * SS], fill=150)
    dsc.ellipse([hx + 12 * SS - R, hy + 22 * SS - R, hx + 12 * SS + R, hy + 22 * SS + R], fill=90)
    dc.line([(px, py), (hx, hy)], fill=(110, 110, 112, 255), width=4 * SS)
    dc.ellipse([hx - R, hy - R, hx + R, hy + R], fill=(78, 78, 80, 255))
    dc.ellipse([hx - R * 0.55, hy - R * 0.6, hx - R * 0.05, hy - R * 0.1], fill=(150, 150, 152, 255))
sc = np.asarray(sc.filter(ImageFilter.GaussianBlur(6 * SS)).resize((W, H), Image.LANCZOS), np.float32) / 255
arr = np.asarray(img, np.float32) * (1 - 0.35 * sc[..., None])
img = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
capa = capa.resize((W, H), Image.LANCZOS)
img.paste(capa, (0, 0), capa)
img.save(SAL)
print('ok', SAL, 'mapa x %.0f-%.0f' % (x0, x0 + ancho_geo * esc), 'y %d-%d' % (TOP, TOP + ALTO))
