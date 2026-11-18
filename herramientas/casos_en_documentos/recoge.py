# Lee el transcript de la sesion y arma el indice id de Drive -> archivo descargado.
import json,re,os,shutil,sys
T='/root/.claude/projects/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f.jsonl'
SRC='/home/claude/casos/src'
idx_path=SRC+'/index.json'
idx=json.load(open(idx_path)) if os.path.exists(idx_path) else {}
rx=re.compile(r'googledrive://file/([A-Za-z0-9_-]+)\] Binary content \(([^,]+), [^)]*\) saved to (/root/[^\s"\\]+)')
rt=re.compile(r'\{\\?"id\\?":\\?"([A-Za-z0-9_-]+)\\?",\\?"title\\?":\\?"(.*?)\\?",\\?"mimeType')
titles={}
pairs=[]
for line in open(T,encoding='utf-8'):
    if 'Binary content' not in line and '(file sent separately)' not in line: continue
    try: o=json.loads(line)
    except Exception: continue
    s=json.dumps(o.get('message',{}).get('content',''),ensure_ascii=False)
    for m in rx.finditer(s): pairs.append(m.groups())
    for m in rt.finditer(s): titles[m.group(1)]=m.group(2).replace('\\\\"','"')
n=0
for fid,mime,path in pairs:
    if not os.path.exists(path): continue
    ext=os.path.splitext(path)[1]
    key=fid+('_pdf' if (mime=='application/pdf' and fid in idx and idx[fid].get('ext')!='.pdf') else '')
    dst='%s/%s%s'%(SRC,fid,ext)
    if not os.path.exists(dst): shutil.copy(path,dst); n+=1
    idx.setdefault(fid,{})
    idx[fid].setdefault('files',{})[ext]=dst
    idx[fid]['title']=titles.get(fid,idx[fid].get('title',''))
json.dump(idx,open(idx_path,'w'),ensure_ascii=False,indent=1)
print('nuevos',n,'total ids',len(idx))
if len(sys.argv)>1:
    for k,v in idx.items(): print(k, list(v['files'].keys()), v['title'][:80])
