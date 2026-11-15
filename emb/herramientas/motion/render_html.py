"""render_html.py — rinde una escena HTML cuadro a cuadro con Chrome headless.
Uso: python3 render_html.py escena.html salida.mp4 [--params JSON] [--sub 2] [--alfa]
La escena expone window.ESCENA = {cuadros, render(f)} (f puede ser fraccionario: sub-cuadros
para desenfoque de movimiento real, que se promedian aquí)."""
import argparse, io, json, subprocess, sys, time
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright
ap=argparse.ArgumentParser(); ap.add_argument('html'); ap.add_argument('salida')
ap.add_argument('--params',default='{}'); ap.add_argument('--sub',type=int,default=1)
ap.add_argument('--alfa',action='store_true'); ap.add_argument('--desde',type=int,default=0); ap.add_argument('--hasta',type=int,default=None)
a=ap.parse_args()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist','--allow-file-access-from-files','--force-color-profile=srgb'])
    pg=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
    pg.goto('file://'+a.html); pg.wait_for_function('window.ESCENA && window.__listo')
    pg.evaluate(f'window.ESCENA.init && window.ESCENA.init({a.params})')
    pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
    n=pg.evaluate('window.ESCENA.cuadros'); hasta=a.hasta or n
    if a.alfa:
        enc=['-c:v','qtrle','-pix_fmt','argb']; fmt='rgba'
    else:
        enc=['-c:v','libx264','-preset','medium','-crf','14','-pix_fmt','yuv420p','-vf','scale=out_color_matrix=bt709:out_range=tv',
             '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709']; fmt='rgb24'
    ff=subprocess.Popen(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt',fmt,'-s','1920x1080','-r','24000/1001','-i','-']+enc+[a.salida],stdin=subprocess.PIPE)
    t=time.time()
    for f in range(a.desde,hasta):
        acc=None
        for k in range(a.sub):
            fr=f+(k/a.sub-0.5*(a.sub-1)/a.sub) if a.sub>1 else f
            pg.evaluate(f'window.ESCENA.render({fr})')
            png=pg.screenshot(omit_background=a.alfa)
            im=np.asarray(Image.open(io.BytesIO(png)).convert('RGBA' if a.alfa else 'RGB'),dtype=np.float32)
            acc=im if acc is None else acc+im
        ff.stdin.write((acc/a.sub+0.5).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait(); b.close()
    print(a.salida,hasta-a.desde,'cuadros',round((hasta-a.desde)/(time.time()-t),1),'cps')
