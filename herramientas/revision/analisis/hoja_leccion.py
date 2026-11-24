import json, sys, glob
from PIL import Image, ImageDraw, ImageFont
ll = sys.argv[1]
fs = sorted(glob.glob('/tmp/claude-0/rev/escenas/%s_E*.png' % ll))
W, H = 556, 224
cols = 2
filas = (len(fs) + cols - 1) // cols
img = Image.new('RGB', (cols * (W + 8) + 8, filas * (H + 26) + 8), 'white')
d = ImageDraw.Draw(img)
try: fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
except Exception: fnt = None
for i, f in enumerate(fs):
    x, y = 8 + (i % cols) * (W + 8), 8 + (i // cols) * (H + 26)
    im = Image.open(f).convert('RGB').resize((W, H))
    img.paste(im, (x, y + 20))
    d.text((x, y), f.split('_')[-1][:-4], fill=(200, 40, 60), font=fnt)
img.save('/tmp/claude-0/rev/hoja_%s.png' % ll)
print(img.size)
