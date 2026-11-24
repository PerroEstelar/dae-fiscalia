import sys, glob
from PIL import Image, ImageDraw
def hoja(patron, sal, cols=3, w=560):
    fs = sorted(glob.glob(patron))
    ims = [Image.open(f).convert('RGB') for f in fs]
    h = int(w * ims[0].height / ims[0].width)
    rows = (len(ims) + cols - 1) // cols
    H = Image.new('RGB', (cols * (w + 8), rows * (h + 26)), 'white')
    d = ImageDraw.Draw(H)
    for i, (f, im) in enumerate(zip(fs, ims)):
        x, y = (i % cols) * (w + 8), (i // cols) * (h + 26)
        H.paste(im.resize((w, h)), (x, y + 22))
        d.text((x + 4, y + 4), f.split('/')[-1], fill='black')
    H.save(sal)
if __name__ == '__main__':
    hoja(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 3)
