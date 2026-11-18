# Ubica cada caso en el documento del curso y deja ubic.json
import sys,json,re
sys.path.insert(0,'/home/claude/casos')
import casa,ubica
LP=['10f0bH2lIOML3-jvsgC44CdtnpxAbyGPn','12bsV6wouZdEehJRAVFkvOZAJjC0PjIBE','1ovkVhalzhZ6UUtyxhv-EwQVZyqtDfOA8','1kYOU38XZUHtQX5kVzyYwfJuTlbfpEpzQ']
D=json.load(open('docs_curso.json'))
ED,DH,GJ,EI,DF=D['ED'],D['DH'],D['GJ'],D['EI'],D['DF']
P3=[D['P3'][0],'10bN8nvtQIelWG0lX2g_ElaQjQBCCC5np']+D['P3'][1:]
TA1,TA4='1ux9nZMZVuFDbi5WQMQg50bPRPQTklCoo','1927lJFG0yhR1PHCwxxz24HdcWCUWM3nM'
JR,SR,BI,DA='1WjbL40IW0mgYWmEGia8TMAwaj2082s56','17gd_nUnJ2WcWvz6K_yBhOKV30Q8r-OIy','1ipQSFy_Pa-nHAA6N7iY2hl6_Hg4AFJd8','1HOT5p71fNf2kfg93Q-NnQZMMdYRHv0Xa'
S=[]  # (clave, fid, ('a',ancla)|('r',regex), fin opcional ('r',regex del parrafo siguiente al final) )
for k,f in [('LP_U1C1',LP[0]),('LP_U1C2',LP[0]),('LP_U1C3',LP[0]),('LP_U1C4',LP[0]),('LP_U1C5',LP[0]),('LP_U2C1',LP[1]),('LP_U2C2',LP[1]),('LP_U3C1',LP[2]),('LP_U3C2',LP[2]),('LP_U3C3',LP[2]),('LP_U4C1',LP[3]),('LP_U4C2',LP[3]),('LP_U4C3',LP[3])]: S.append((k,f,('a',k),None))
for n in range(5): S.append(('ED_C%d'%(n+1),ED[n],('a','ED_C%d'%(n+1)),None))
S+=[('GJ_T1',GJ[0],('a','GJ_T1'),None),('GJ_T3',GJ[0],('a','GJ_T3'),None),('GJ_T4',GJ[1],('a','GJ_T4'),None)]
for k in ['S01','S02','S03','S04','S05','S09','S10','S11']: S.append(('EI_'+k,EI[0],('a','EI_'+k),None))
for k in ['S06','S07','S08']: S.append(('EI_'+k,EI[3],('a','EI_'+k),None))
S+=[('DF_2',DF[1],('r',r'^Ante la indolencia policial'),('r',r'^Guion t[eé]cnico')),('DF_3',DF[2],('a','DF_3'),('r',r'^Guion t[eé]cnico')),('DF_4',DF[3],('r',r'^La Sra\. Rosa Elena Morales vive un viacrucis'),('r',r'^Guion t[eé]cnico')),('DF_5',DF[4],('a','DF_5'),('r',r'^Guion t[eé]cnico'))]
for k,u in [('A',0),('B',0),('C',0),('D',0),('E',0),('F',1),('G',1),('H',3),('I',3),('J',4),('K',4)]: S.append(('SIT_'+k,DF[u],('a','SIT_'+k),None))
S+=[('DH_U1',DH[0],('r',r'^Video de apertura'),('r',r'^3\.3 Competencias')),('DH_U2',DH[1],('r',r'^El expediente del curso da su primer giro'),('r',r'^3\.3 Competencias')),('DH_U3',DH[2],('r',r'^Bienvenida y bienvenido a la Unidad 3'),('r',r'^3\.3 Competencias')),('DH_U4',DH[3],('r',r'^Bienvenida, Bienvenido'),('r',r'^3\.3 Competencias')),('DH_U5',DH[4],('r',r'^Bienvenido\. El caso de Carmen Elisa'),('r',r'^3\.3 Competencias'))]
S+=[('P3_C1',P3[0],('r',r'^Caso: «El hospedaje El Mirador»'),('r',r'Observaci[oó]n reflexiva')),('P3_C2',P3[1],('r',r'^Caso: «El taller del segundo piso»'),('r',r'Observaci[oó]n reflexiva')),('P3_C3',P3[2],('r',r'^Caso: «Ruta del Golfo»'),('r',r'Observaci[oó]n reflexiva')),('P3_C4',P3[3],('r',r'^Caso: «Puerto de salida»'),('r',r'Observaci[oó]n reflexiva')),('P3_C5',P3[4],('r',r'^Caso: «Voces, registros y cuentas»'),('r',r'Observaci[oó]n reflexiva'))]
for k in ['01','02','03','04','05']: S.append(('TA_'+k,TA4,('a','TA_'+k),None))
for k in ['06','07','08']: S.append(('TA_'+k,TA1,('a','TA_'+k),None))
S.append(('TA_09',TA1,('r',r'^Un conductor causa lesiones a una mujer'),('r',r'.')))
S+=[('JR_C1',JR,('a','JR_C1'),None),('JR_C2',JR,('a','JR_C2'),None),('JR_U1',JR,('a','JR_U1'),None),('JR_U2',JR,('a','JR_U2'),None),('JR_U3',JR,('r',r'^Prosigue la situaci[oó]n reflexiva'),('rl',r'se queda pensativa')),('JR_U4',JR,('a','JR_U4'),None)]
S+=[('SR_IPANEMA',SR,('r',r'^Estudio de caso para la Unidad\. Caso Ipanema'),None),('SR_NICO',SR,('a','SR_NICO'),None),('SR_CH02',SR,('r',r'^Caso: Rodman'),None),('SR_CH03',SR,('r',r'^Caso: Disney'),None),('SR_CH04',SR,('r',r'^Caso Arley y Susana'),None),('SR_CH05',SR,('r',r'^Caso Juan'),('r',r'^Pregunta orientadora')),('SR_CHAP',SR,('r',r'^Caso: Los Chapulines'),None),('SR_CH01',SR,('r',r'^Talleres de casos: Caso 1 Santiago'),None)]
S+=[('C5_U1',BI,('r',r'^Caso Pr[aá]ctico – Unidad Primera'),('r',r'^Cuestionario de An[aá]lisis')),('C5_U2',BI,('r',r'^Caso Pr[aá]ctico – Unidad Segunda'),('r',r'^Cuestionario de An[aá]lisis')),('C5_U3',BI,('r',r'^Caso Pr[aá]ctico – Unidad Tercera'),('r',r'^Cuestionario de An[aá]lisis')),('C5_U4',BI,('r',r'^Caso Pr[aá]ctico – Unidad Cuarta'),('r',r'^Cuestionario de An[aá]lisis'))]
S+=[('DA_V01',DA,('r',r'^Video introductorio: problem[aá]tica ambiental'),None),('DA_V02',DA,('r',r'^Video explicativo: Plan de priorizaci'),None),('DA_V03',DA,('r',r'^Producci[oó]n de video interactivo'),('rl',r'^Video del Dr\. Porras')),('DA_V04',DA,('r',r'T[ií]tulo del Caso: El R[ií]o y la F[aá]brica'),None),('DA_V05',DA,('r',r'^Caso Pr[aá]ctico: Operaci[oó]n'),None),('DA_V06',DA,('r',r'^Video Narrativo del caso Francisco'),None)]
CT,ED_,DF1='13Yjz-pOJaAW0-Dly7xcTcc2ty89pE8xO','1CrcaP2Im1jcDhpXBKgCmMYYEtZUAbgXW','1ixWWF0NNTmUp_vYIphBuLEGzehV6hZdpXt7ba1iPwbA'
S+=[('W_CH01',CT,('r',r'^CASO 1: Santiago y Valeria'),('r',r'^CASO 2')),('W_CH06',CT,('r',r'^Caso 6: Lenin'),('r',r'^ZZZ')),('W_EDA',ED_,('r',r'^Caso hipot[eé]tico No\.1'),('r',r'^Caso No\. 2')),('W_EDB',ED_,('r',r'^Caso No\. 2'),('r',r'^Caso 3')),('W_DF1',DF1,('r',r'^CAP[IÍ]TULO 1 DEL CASO INTEGRADOR'),('r',r'^Guion t[eé]cnico'))]
FINRX=re.compile(r'^(Fase|Cap[ií]tulo|Lecci[oó]n|Pregunta|Preguntas|Actividad|Evaluaci[oó]n|Ejercicio|Consigna|Video|Caso|Situaci[oó]n|Guion t[eé]cnico|Resoluci[oó]n|Problema jur[ií]dico|\d+\.\d|_{5,}|Instrucci|Opci[oó]n|Retroalimentaci|A partir|Con base|Recurso|Para el an[aá]lisis|An[aá]lisis|Comentado|Objetivo|Estudio|Material|Cuestionario|Momento|Tipo de|Nota)',re.I)
UNI=re.compile(r'Nombre de la unidad\s*(No\.?|N[°º])?\s*(\d+)|^Unidad\s+(\d+)\b|unidad No\.?\s*(\d+)',re.I)
def palabras(t,n,fin=False):
    w=t.split(); return ' '.join(w[-n:] if fin else w[:n])
R={}
for clave,fid,ini,fin in S:
    pars=casa.carga(fid); i=j=None; L=0
    if ini[0]=='a':
        hi,L=casa.halla_txt(fid,casa.A[ini[1]]['ini'])
        if hi and L>=24:
            i=hi[0]
            hf,Lf=casa.halla_txt(fid,casa.A[ini[1]]['fin'],True)
            cand=[x for x in hf if x>=i and x-i<120]
            if cand and Lf>=24: j=cand[0]
    else:
        rx=re.compile(ini[1],re.I)
        for k,p in enumerate(pars):
            if rx.search(p['t']): i=k; break
    if i is None: R[clave]={'fid':fid,'hallado':False}; continue
    aprox=False
    if fin is not None or j is None:
        rx=re.compile(fin[1],re.I) if fin else FINRX
        jj=None
        incl=1 if (fin and fin[0]=='rl') else 0
        for k in range(i+1,min(len(pars),i+160)):
            if rx.search(pars[k]['t']) and (fin is not None or len(pars[k]['t'])<400): jj=k-1+incl; break
        if fin is not None and jj is not None: aprox_fin=False
        if j is None: j=jj if jj is not None else i; aprox=(fin is None)
        elif fin is not None and jj is not None: j=max(j,jj) if jj-i<160 else j
    f=casa.ficha(pars,i)
    TIT=re.compile(r'^(Caso de (estudio|an[aá]lisis)|Estudio reverso de caso|CASO II?\b|Situaci[oó]n( inicial| de aprendizaje| investigativa)?\s*:?$|Fase de experiencia concreta|Tercero a quinto|Situaci[oó]n\s*[A-K]?\s*:|CAP[IÍ]TULO \d|Estudio de caso|Importancia del principio|Inicio: el encuentro|Veamos un ejemplo|\d\. Caso introductorio|Comencemos la unidad|Culminamos la situaci|Video de apertura)',re.I)
    it=i
    for k in range(i-1,max(-1,i-9),-1):
        if TIT.search(pars[k]['t']) and len(pars[k]['t'])<160: it=k; break
    uni=None
    for k in range(i,-1,-1):
        m=UNI.search(pars[k]['t'])
        if m and len(pars[k]['t'])<160: uni=(k,pars[k]['t'][:120]); break
    des=act=None
    for k in range(i,-1,-1):
        t=pars[k]['t']
        if des is None and re.search(r'Desarrollo del contenido tem[aá]tico',t) and len(t)<120: des=k
        if act is None and re.search(r'Actividades y productos de aprendizaje',t) and len(t)<120: act=k
        if des is not None and act is not None: break
    R[clave]={'fid':fid,'hallado':True,'modo':ini[0],'i':i,'j':j,'L':L,'fin_aprox':aprox,'pag_ini':pars[i]['pag'],'n_ini':pars[i]['n'],'pag_fin':pars[j]['pag'],'n_fin':pars[j]['n'],
        'it':it,'titulo':pars[it]['t'][:200],'pag_tit':pars[it]['pag'],'n_tit':pars[it]['n'],'empieza':palabras(pars[i]['t'],12),'termina':palabras(pars[j]['t'],9,True),'t_ini':pars[i]['t'][:300],
        'rot':[t for _,t in f['rot']][-3:],'num':f['num'],'leccion':f['leccion'],'tema':f.get('tema'),'actividad':f['actividad'],'estrategia':f.get('estrategia'),'fase':f['fase'],'recurso':f['recurso'],'unidad':uni,'des':des,'act':act,'npars':j-i+1}
json.dump(R,open('ubic.json','w'),ensure_ascii=False,indent=1)
if __name__=='__main__':
    c=lambda v,n=58: (v[1][:n] if v else '-')
    for k,r in R.items():
        if not r['hallado']: print('%-10s NO HALLADO'%k); continue
        print('%-10s p%d n%d → p%d n%d (%d párr%s) | U:%s | L:%s[%s] | num:%s | act:%s | est:%s | fase:%s | rec:%s | rot:%s'%(k,r['pag_ini'],r['n_ini'],r['pag_fin'],r['n_fin'],r['npars'],'~' if r['fin_aprox'] else '',c(r['unidad'],34),c(r['leccion'],40),('ok' if (r['leccion'] and r['des'] is not None and r['leccion'][0]>r['des'] and not (r['act'] is not None and r['act']>r['leccion'][0])) else 'x'),c(r['num'],44),c(r['actividad'],50),c(r['estrategia'],60),c(r['fase'],40),c(r['recurso'],50),' ¦ '.join(x[:38] for x in r['rot'])))
