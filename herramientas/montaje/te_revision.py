import glob, json, os, re, subprocess, sys
sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente\entrevista_tecnicas')
import plan_te as P
from PIL import Image, ImageDraw, ImageFont
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
f = '%s/05 EXPORTS/%s.mov' % (P.R, P.EXPORT % int(sys.argv[1]))
j = json.loads(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-count_packets', '-show_streams', '-of', 'json', f], capture_output=True, text=True).stdout)
v = [s for s in j['streams'] if s['codec_type'] == 'video'][0]
a = [s for s in j['streams'] if s['codec_type'] == 'audio']
r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', f, '-vn', '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
s = r[r.rfind('Summary'):]
print(v['codec_name'], v.get('profile'), v['width'], v['height'], v['nb_read_packets'], 'audio', bool(a), re.findall(r'(I|Peak):\s+(-?[\d.]+)', s), os.path.getsize(f) // 1000000, 'MB')
clip = float(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', P.COMPUESTO], capture_output=True, text=True).stdout)
fin = P.CLIP0 + int(round(clip * P.FPS))
marcas = [('intro', 100), ('titulo', 300)] + [(c, (P.cuadro(a) + P.cuadro(b)) // 2) for c, t, a, b, _ in P.ITEMS]
marcas += [('cierre', fin + 30), ('cierre', fin + 120), ('cierre', fin + 200), ('outro', fin + 275), ('outro', fin + 365)]
os.makedirs('D:/DAE/_tmp/ma/te/rev', exist_ok=True)
col = 6; out = Image.new('RGB', (480 * col, 300 * ((len(marcas) + col - 1) // col)), 'black'); d = ImageDraw.Draw(out)
for i, (nm, fr) in enumerate(marcas):
    p = 'D:/DAE/_tmp/ma/te/rev/%03d.png' % i
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', '%.3f' % (fr / P.FPS), '-i', f, '-frames:v', '1', '-vf', 'scale=480:270', p])
    x, y = (i % col) * 480, (i // col) * 300
    out.paste(Image.open(p), (x, y)); d.text((x + 6, y + 276), '%s %d' % (nm, fr), fill='white')
out.save('D:/DAE/_tmp/ma/te/hoja_rev.jpg', quality=82)
print('hoja lista')
