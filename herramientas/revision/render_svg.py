"""Rinde cada .svg de una carpeta a .png con Chromium (Playwright), lienzo 400x170.

    python3 render_svg.py <carpeta_svg> <carpeta_png> <escala>   (2 para incrustar en el Excel)
"""
import sys, glob, os
from playwright.sync_api import sync_playwright
src, dst, escala = sys.argv[1], sys.argv[2], float(sys.argv[3])
os.makedirs(dst, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 400, 'height': 170}, device_scale_factor=escala)
    for f in sorted(glob.glob(src + '/*.svg')):
        pg.set_content('<html><body style="margin:0">' + open(f, encoding='utf-8').read() + '</body></html>')
        pg.wait_for_timeout(150)
        pg.screenshot(path=os.path.join(dst, os.path.basename(f)[:-4] + '.png'), clip={'x':0,'y':0,'width':400,'height':170}, omit_background=False)
    b.close()
