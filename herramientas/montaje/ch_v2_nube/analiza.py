import json, re, numpy as np, librosa, warnings
warnings.filterwarnings('ignore')
S='/mnt/user-data/uploads/DAE/_tmp/ch/stt/caso%02d.json'
T='/mnt/user-data/uploads/DAE/_tmp/ch/tts/CH_U1_C%02d_%s_%s.mp3'
def words(n):
    j=json.load(open(S%n)); return [w for w in j['words'] if w.get('type')=='word']
def norm(s): return re.sub(r'[^a-záéíóúñü0-9 ]','',s.lower())
SPANS={(1,'r1'):('El equipo','hacia él.'),(2,'r1'):('El informe','el entorno.'),(2,'r2'):('Ambos se','oferta educativa.'),
(3,'r1'):('La mujer','dieciséis años.'),(3,'r2'):('Se capturan','dieciséis años.'),(3,'r3'):('El equipo','habitacionales adecuadas.'),
(3,'r4'):('Estaba matriculada','para adolescentes.'),(4,'r1'):('Entre mediados','de Arley.'),(4,'r2'):('Arley vivía','ningún tipo.'),
(5,'r1'):('La investigación','de salud.'),(5,'r2'):('Y estableció','manera irregular.'),(6,'r1'):('En un','de once.'),(6,'r2'):('El grupo','y autodeterminación.')}
def find(ws, a, b, after=0):
    a=norm(a).split(); b=norm(b).split()
    for i in range(len(ws)):
        if ws[i]['start']<after: continue
        if [norm(ws[i+k]['text']) for k in range(len(a))]==a:
            for j in range(i,len(ws)-len(b)+1):
                if [norm(ws[j+k]['text']) for k in range(len(b))]==b:
                    return i, j+len(b)-1
    return None
def speech(path):
    y,sr=librosa.load(path,sr=16000)
    it=librosa.effects.split(y,top_db=35)
    return it[0][0]/sr, it[-1][1]/sr, len(y)/sr
res={}
for (n,i),(a,b) in SPANS.items():
    ws=words(n)
    after=60 if (n,i)==(3,'r3') else 0
    r=find(ws,a,b,after)
    if not r: print('NO',n,i); continue
    s,e=ws[r[0]]['start'],ws[r[1]]['end']
    nxt=ws[r[1]+1]['start'] if r[1]+1<len(ws) else None
    prv=ws[r[0]-1]['end'] if r[0]>0 else None
    out=[]
    for t in 'ab':
        s0,e0,L=speech(T%(n,i,t)); out.append((t,round(e0-s0,2),round(s0,2),round(L-e0,2)))
    res['%d_%s'%(n,i)]={'orig':[round(s,2),round(e,2)],'dur':round(e-s,2),'prev_end':prv,'next':nxt,'tts':out}
    print(n,i,'orig %.2f-%.2f dur %.2f  hueco antes %.2f despues %s'%(s,e,e-s,(s-prv) if prv else -1,'%.2f'%(nxt-e) if nxt else '-'),' tts',out)
json.dump(res,open('spans.json','w'),indent=1)
