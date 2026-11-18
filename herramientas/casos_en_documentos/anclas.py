# Saca de los guiones el principio y el final del texto de cada pieza (para buscarlo en los documentos).
import importlib,sys,json,re
sys.path.insert(0,'/home/claude/repo/herramientas/voz/textos')
def limpia(t):
    t=re.sub(r'<break[^>]*/>','',t); return re.sub(r'\s+',' ',t).strip()
def textos_de(v):
    # lista de bloques (id, voz, texto, ...) | str | lista de ('p', texto)
    if isinstance(v,str): return [limpia(v)]
    out=[]
    for b in v:
        if isinstance(b,str): out.append(limpia(b))
        elif isinstance(b,(tuple,list)):
            ss=[x for x in b if isinstance(x,str)]
            if len(b)>=3 and isinstance(b[2],str): out.append(limpia(b[2]))
            elif len(ss)>=2: out.append(limpia(ss[-1]))
    return [x for x in out if x]
A={}
def mete(pref,d):
    for k,v in d.items():
        ts=textos_de(v)
        if ts: A['%s_%s'%(pref,k)]={'ini':ts[0][:400],'fin':ts[-1][-400:],'n':len(ts),'palabras':sum(len(t.split()) for t in ts)}
for mod,pref,attrs in [('guion_lp','LP',['TEXTOS','BLOQUES']),('guion_ed','ED',['BLOQUES']),('guion_dh','DH',['BLOQUES']),('guion_ei','EI',['TEXTOS','BLOQUES']),('guion_gj','GJ',['BLOQUES']),('guion_jr','JR',['BLOQUES']),('guion_da','DA',['BLOQUES']),('guion_df','DF',['CAPITULOS']),('guion_sit','SIT',['TEXTOS','BLOQUES']),('guion_sr','SR',['BLOQUES'])]:
    m=importlib.import_module(mod)
    for a in attrs: mete(pref,getattr(m,a))
for mod,k in [('guion_p3c1','P3_C1'),('guion_p3c2','P3_C2'),('guion_p3c4','P3_C4'),('guion_p3c5','P3_C5'),('guion_c5u3','C5_U3'),('guion_c5u4','C5_U4')]:
    m=importlib.import_module(mod); ts=textos_de(m.BLOQUES)
    A[k]={'ini':ts[0][:400],'fin':ts[-1][-400:],'n':len(ts),'palabras':sum(len(t.split()) for t in ts)}
json.dump(A,open('/home/claude/casos/anclas.json','w'),ensure_ascii=False,indent=1)
print(len(A))
for k,v in A.items(): print(k,v['n'],v['palabras'],'|',v['ini'][:70],'…',v['fin'][-50:])
