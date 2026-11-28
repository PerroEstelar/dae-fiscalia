import subprocess, glob, os, json, sys
from PIL import Image
FB=glob.glob(os.path.expanduser('~')+'/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
T='D:/DAE/_tmp/gj_p/'
MAN={m['clave']:m for m in json.load(open('D:/DAE/_repo/cursos/gerencia_judicial/subtitulos/manifiesto.json',encoding='utf-8'))}
F=24000/1001
for c in sys.argv[1:]:
    v=MAN[c]['video']; e=json.load(open(T+c+'/linea_estructura.json',encoding='utf-8'))
    tot=e['total']; lts=[x for x in e['items'] if x['tipo']=='video' and x['pista']>=3]
    comp=[x for x in e['items'] if x['tipo']=='video' and x['pista']==1 and 'compuesto' in x['archivo']][0]
    ts=[12.0]+[(x['ini']+70)/F for x in lts][:2]+[(comp['ini']+comp['fin'])/2/F, (comp['fin']-30)/F, (tot-200)/F]
    ts=ts[:6]
    g=Image.new('RGB',(1440,405*((len(ts)+1)//2)))
    for i,t in enumerate(ts):
        o=T+c+'/qa_%d.png'%i
        subprocess.run([FB+'/ffmpeg.exe','-y','-v','error','-ss','%.2f'%t,'-i',v,'-frames:v','1','-vf','scale=720:405',o])
        g.paste(Image.open(o),((i%2)*720,(i//2)*405))
    g.save(T+c+'/qa_grid.jpg',quality=86)
    print(c, 'tiempos', ['%.1f'%t for t in ts], 'lt', len(lts))
