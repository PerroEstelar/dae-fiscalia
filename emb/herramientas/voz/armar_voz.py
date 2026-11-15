"""armar_voz.py escena.html voz.wav calzado.json cuerpo.mp4[,cuerpo2.mp4] salida.mp4 [musica.wav]
Intro + cuerpo + outro, con la voz montada por tramos: cada bloque en el cuadro de su sección
(lo da la escena: ESCENA.voz()). Si se pasa música, se mezcla debajo ya agachada."""
import json, subprocess, sys
from playwright.sync_api import sync_playwright
html, voz, cal, cuerpos, salida = sys.argv[1:6]; musica = sys.argv[6] if len(sys.argv) > 6 else None
FPS = 24000 / 1001; INTRO = 112; R = '/home/claude/emb/render/m1v1'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}); pg.goto('file://' + html)
    pg.wait_for_function('window.ESCENA && window.__listo'); pg.evaluate('window.ESCENA.init({})')
    pos = pg.evaluate('window.ESCENA.voz ? window.ESCENA.voz() : null'); N = pg.evaluate('window.ESCENA.cuadros'); b.close()
bloques = json.load(open(cal))['bloques']
ins = ['-i', f'{R}/v2/intro_v4.mp4'] + sum([['-i', c] for c in cuerpos.split(',')], []) + ['-i', f'{R}/outro.mp4']
nv = len(cuerpos.split(',')) + 2
fc = ''.join(f'[{i}:v]' for i in range(nv)) + f'concat=n={nv}:v=1:a=0,setsar=1[v];'
ins += ['-i', voz]; vi = nv
partes = []
for k, (i, cuadro) in enumerate(pos):
    bq = bloques[i]; a = bq['ini']; fin = bloques[i + 1]['ini'] if i + 1 < len(bloques) else None
    ms = round((INTRO + cuadro) / FPS * 1000)
    trim = f'atrim=start={max(0,a-0.05)}' + (f':end={fin-0.05}' if fin else '')
    fc += f'[{vi}:a]{trim},asetpts=PTS-STARTPTS,afade=t=in:d=0.04,adelay={ms}|{ms}[v{k}];'
    partes.append(f'[v{k}]')
fc += ''.join(partes) + f'amix=inputs={len(partes)}:normalize=0[voz];'
total = (INTRO + N + 108) / FPS
tramos = []
for i, cuadro in pos:
    bq = bloques[i]; t0 = (INTRO + cuadro) / FPS
    tramos.append((t0, t0 + (bq['fin'] - bq['ini'])))
if musica:
    import sys as _s; _s.path.insert(0, '/home/claude/dae-fiscalia/emb/herramientas/musica')
    from cama_emb import cama
    musica = cama(musica, total, tramos, salida + '.cama.wav')
    ins += ['-i', musica]
    fc += f'[{vi+1}:a]atrim=end={total}[mus];[voz][mus]amix=inputs=2:normalize=0,volume=-1.5dB,alimiter=limit=0.84:level=false[a]'
else:
    fc += '[voz]anull[a]'
cmd = ['ffmpeg', '-loglevel', 'error', '-y'] + ins + ['-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', f'{total:.3f}',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709',
       '-color_trc', 'bt709', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', salida]
subprocess.run(cmd, check=True)
json.dump({'pos': pos, 'N': N, 'total': total}, open(salida + '.voz.json', 'w'))
print('listo', salida, round(total, 2), 's', pos)
