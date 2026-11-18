# Arma el Excel de casos a partir de casos.json
import json,re,sys
sys.path.insert(0,'/home/claude/casos')
import casa
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.utils import get_column_letter
F=json.load(open('casos.json'))
def limpia_est(t):
    t=re.sub(r'^Tipo de estrategia:?\s*','',t,flags=re.I).strip()
    if len(t)>170:
        k=t.find('. ',40); t=t[:k+1] if 0<k<220 else t[:170]+'…'
    return t
OV={}
for k in ['LP_U1C1','LP_U1C2','LP_U1C3','LP_U1C4','LP_U1C5']: OV[k]={'recurso':'Video animado planteando los cinco casos derivados con su solución.','nota+':'El documento del curso pide video animado; la pieza entregada es una lámina, como la marcó la agencia en su documento de casos.'}
for k in ['LP_U2C1','LP_U2C2']: OV[k]={'actividad':'Actividad 1: Estudio reverso de caso','recurso':'Video animado del caso planteando los dos casos derivados con su solución.'}
for k in ['LP_U3C1','LP_U3C2','LP_U3C3','LP_U4C1','LP_U4C2','LP_U4C3']: OV[k]={'recurso':'','actividad':'Cuestionario de la unidad (los casos son sus enunciados)'}
OV['JR_C1']={'actividad':'Evaluación de la unidad segunda','recurso':''}
OV['JR_C2']={'actividad':'Evaluación sumativa de la unidad tercera › Análisis de casos › «Tercero a quinto»','recurso':''}
OV['JR_U1']={'recurso':'Antes del relato: «Observe este video» (una escena de la película Relatos salvajes) y «Ahora se examinará el hecho paso a paso».','actividad':'Situación inicial de la lección («Comencemos analizando una situación, específicamente un conflicto»)'}
for k in ['JR_U2','JR_U3','JR_U4']: OV[k]={'recurso':'','actividad':'Situación reflexiva que abre la unidad (conversación con Juana)'}
for k in ['SR_IPANEMA','SR_NICO','SR_CH02','SR_CH03','SR_CH04','SR_CHAP']: OV[k]={'recurso':'','actividad':''}
OV['SR_IPANEMA']['actividad']='Estudio de caso para la unidad'
OV['SR_NICO']['actividad']='Caso que ilustra el principio de culpabilidad'
OV['SR_CH01']={'actividad':'Talleres de casos','fase':'','recurso':''}
OV['SR_CH05']={'actividad':'','recurso':'','seccion':'Lección 3. Remisión de casos o medidas extrajudiciales.'}
TA1L={'TA_06':'Lección 1.1. Fundamentos jurídicos, causales y procedencia del archivo de la indagación.','TA_07':'Lección 1.1. Fundamentos jurídicos, causales y procedencia del archivo de la indagación.','TA_09':'Lección 1.2. Diferencias entre archivo, inadmisión de denuncia y preclusión.','TA_08':'Lección 1.3. Control del desarchivo de las diligencias, reactivación de la investigación y derechos de las víctimas.'}
for n in range(1,10):
    k='TA_%02d'%n; OV[k]={'actividad':'Ejemplo dentro de la lección (bloque «Veamos un ejemplo…»)','recurso':''}
    if k in TA1L: OV[k]['seccion']=TA1L[k]
for k in ['C5_U1','C5_U2','C5_U3','C5_U4']: OV[k]={'fase':'Fase I. Experiencia Concreta','actividad':'Caso práctico de la unidad; lo sigue el «Cuestionario de Análisis Estratégico y Reflexión para el Fiscal»','recurso':''}
for n in range(1,6): OV['ED_C%d'%n]={'recurso':'','actividad':'Caso que abre la unidad'}
OV['DH_U1']={'fase':'','recurso':'Video animado interactivo H5P con pausa y reflexión. Duración entre 4 a 6 minutos.','actividad':'Video de apertura: «Llega la noticia»','seccion':'3.2 Introducción a la unidad No. 1'}
OV['DH_U2']={'fase':'','recurso':'','actividad':'El documento la llama «simulación ramificada» de la unidad','seccion':'3.2 Introducción a la unidad No. 2'}
OV['DH_U3']={'fase':'','recurso':'','actividad':'«Una entrevista a Carmen Elisa en dos versiones»; más adelante la llama «audiodrama»','seccion':'3.2 Introducción a la unidad No. 3'}
OV['DH_U4']={'fase':'','recurso':'','actividad':'El documento la llama «simulación de audiencia»','seccion':'3.2 Introducción a la unidad No. 4'}
OV['DH_U5']={'fase':'Experiencia concreta','recurso':'','actividad':'«Cierre del expediente: decisión integral (acusar, proteger y solicitar medidas) con un giro final que obliga a reponderar» (3.9, p. 9)','seccion':'3.2 Introducción a la unidad No. 5'}
for k in ['GJ_T1','GJ_T3','GJ_T4']: OV[k]={'actividad':'Caso introductorio del tema','recurso':''}
for k in ['DF_2','DF_3','DF_4','DF_5']: OV[k]={'actividad':'Capítulo del caso integrador','recurso':'Después del texto del capítulo viene el «Guion técnico para la animación».'}
for k in 'ABCDE': OV['SIT_'+k]={'actividad':'Actividad 1. ¿Qué tenemos aquí?','estrategia':'Ejercicio de análisis casuístico con retroalimentación automática interactiva por opción.','recurso':''}
for k in 'FGHIJK': OV['SIT_'+k]={'recurso':''}
for n in range(1,6): OV['P3_C%d'%n]={'seccion':'3.9 Actividades y productos de aprendizaje No. %d'%n,'estrategia':'','recurso':'','actividad':'Caso de la unidad; lo sigue la «Observación reflexiva»'}
OV['P3_C2']['fase']='Experiencia concreta'
OV['DA_V04']={'actividad':'Ficha de virtualización','recurso':''}
OV['DA_V05']={'actividad':'Caso práctico de la lección','recurso':''}
for k in ['DA_V01','DA_V02','DA_V03','DA_V06']: OV[k]={'recurso':'*sig','actividad':''}
ORD=['LP','JR','SR','TA','C5','ED','DH','GJ','EI','DA','DF','P3']
rows=[]
docs={}
for f in F:
    c=f.get('c'); w=f.get('w'); ov=OV.get(f['clave'],{})
    base=c or w
    d=dict(seccion=base.get('seccion',''),actividad=base.get('actividad',''),estrategia=limpia_est(base.get('estrategia','')),fase=base.get('fase',''),recurso=base.get('recurso',''))
    if not c: d=dict(seccion='',actividad='',estrategia='',fase='',recurso='')
    for k,v in ov.items():
        if k in d: d[k]=v
    if d['recurso']=='*sig':
        pars=casa.carga(c['fid'])
        import ubica
        R=json.load(open('ubic.json'))[f['ubi']]
        t=pars[R['it']+1]['t']; d['recurso']=(t[:260]+'…') if len(t)>260 else t
    d['recurso']=re.sub(r'^(Recurso|Herramienta):\s*','',d['recurso'])
    mom=' · '.join(x for x in [re.sub(r'^(Propósito pedagógico|Momento pedagógico|Tipo de actividad):\s*','',d['fase']).rstrip('.'),d['estrategia']] if x)
    nota=f['nota']
    if ov.get('nota+'): nota=(nota+' ' if nota else '')+ov['nota+']
    medida='Exacta (PDF)' if base['exacta'] else 'Aproximada (Word convertido a PDF)'
    if f['clave']=='TA_06' or f['clave'] in ('TA_07','TA_08','TA_09'): medida='Aproximada (Word convertido a PDF; notas al pie rehechas)'
    if c and base['fin_aprox']: nota=(nota+' ' if nota else '')+'El final del caso se tomó donde empieza el siguiente rótulo del documento.'
    if not c:
        sec='No figura en el documento del curso'
        docn='%s (documento de trabajo: el caso no está en el documento del curso)'%w['doc']
    else:
        sec=d['seccion']; docn=c['doc']
    uni=f['uni']; uni=('Unidad '+uni[1:]) if re.fullmatch(r'U\d',uni) else uni
    rows.append(dict(ord=(f['prioridad'],ORD.index(f['cur'])),prioridad=f['prioridad'],curso=f['curso'],unidad=uni,caso=f['nombre'],pieza=f['pieza'],seccion=sec,titulo=base['titulo'],actividad=d['actividad'],momento=mom,recurso=d['recurso'],doc=docn,doc_url=base['url'],pag=base['pag_ini'],parr=base['n_ini'],pagf=base['pag_fin'],empieza='«%s…»'%base['empieza'],termina='«…%s»'%base['termina'],medida=medida,trab=f['trab'][0],trab_url=('https://docs.google.com/document/d/%s/edit'%f['trab'][1]) if f['trab'][2] else ('https://drive.google.com/file/d/%s/view'%f['trab'][1]),ent=f['ent_nombre'] or 'Sin entrega en Drive',ent_url=('https://drive.google.com/file/d/%s/view'%f['ent']) if f['ent'] else '',clave=f['clave'],nota=nota))
    if c: docs.setdefault(c['fid'],dict(curso=f['curso'],prioridad=f['prioridad'],ordk=(f['prioridad'],ORD.index(f['cur'])),doc=c['doc'],url=c['url'],npags=c['npags'],medida='Exacta (PDF)' if c['exacta'] else 'Aproximada (Word convertido a PDF)',n=0))
    if c: docs[c['fid']]['n']+=1
rows.sort(key=lambda r:r['ord'])   # estable: conserva el orden dentro del curso
json.dump(rows,open('filas.json','w'),ensure_ascii=False,indent=1)
AR='Arial'
wb=Workbook(); ws=wb.active; ws.title='Casos'
COLS=[('Prioridad','prioridad',9),('Curso','curso',30),('Unidad','unidad',10),('Caso','caso',34),('Pieza','pieza',11),('Lección o sección del documento','seccion',40),('Cómo aparece en el documento (título o rótulo)','titulo',36),('Actividad o ejercicio, como lo llama el documento','actividad',40),('Momento o tipo de estrategia','momento',34),('Recurso que pide el documento','recurso',38),('Documento (enlace)','doc',44),('Página de inicio','pag',9),('Párrafo n.º en esa página','parr',10),('Página final','pagf',9),('Empieza con','empieza',40),('Termina con','termina',36),('Cómo se midió la página','medida',22),('Documento de trabajo de donde se tomó el texto (enlace)','trab',34),('Archivo entregado (enlace)','ent',44),('Clave interna','clave',11),('Notas','nota',50)]
hf=Font(name=AR,bold=True,color='FFFFFF',size=10); hfill=PatternFill('solid',fgColor='1F3864')
thin=Side(style='thin',color='BFBFBF'); bd=Border(left=thin,right=thin,top=thin,bottom=thin)
for j,(h,_,wd) in enumerate(COLS,1):
    c=ws.cell(row=1,column=j,value=h); c.font=hf; c.fill=hfill; c.alignment=Alignment(wrap_text=True,vertical='center',horizontal='center'); c.border=bd
    ws.column_dimensions[get_column_letter(j)].width=wd
ws.row_dimensions[1].height=44
link=Font(name=AR,size=10,color='0563C1',underline='single'); nf=Font(name=AR,size=10)
fills={1:'FFFFFF',2:'F2F7FB',3:'FFFFFF'}
prev=None; banda=False
for i,r in enumerate(rows,2):
    if r['curso']!=prev: banda=not banda; prev=r['curso']
    fill=PatternFill('solid',fgColor='EEF3F9' if banda else 'FFFFFF')
    maxl=1
    for j,(h,k,wd) in enumerate(COLS,1):
        v=r[k]; c=ws.cell(row=i,column=j,value=v); c.font=nf; c.border=bd; c.fill=fill
        c.alignment=Alignment(wrap_text=True,vertical='top',horizontal='center' if k in('prioridad','pag','parr','pagf','unidad','pieza','clave') else 'left')
        url={'doc':r['doc_url'],'trab':r['trab_url'],'ent':r['ent_url']}.get(k)
        if url: c.hyperlink=url; c.font=link
        if isinstance(v,str) and v: maxl=max(maxl,-(-len(v)//max(8,int(wd*1.05))))
    ws.row_dimensions[i].height=min(260,max(30,13.5*maxl+4))
ws.freeze_panes='E2'; ws.auto_filter.ref='A1:%s%d'%(get_column_letter(len(COLS)),len(rows)+1)
# Documentos
wd=wb.create_sheet('Documentos')
H=[('Prioridad',9),('Curso',46),('Documento del curso (enlace)',70),('Páginas',9),('Cómo se midió la página',34),('Casos ubicados en él',12)]
for j,(h,w_) in enumerate(H,1):
    c=wd.cell(row=1,column=j,value=h); c.font=hf; c.fill=hfill; c.alignment=Alignment(wrap_text=True,vertical='center',horizontal='center'); c.border=bd; wd.column_dimensions[get_column_letter(j)].width=w_
dl=sorted(docs.values(),key=lambda d:(d['ordk'],d['doc']))
for i,d in enumerate(dl,2):
    for j,v in enumerate([d['prioridad'],d['curso'],d['doc'],d['npags'],d['medida'],None],1):
        c=wd.cell(row=i,column=j,value=v); c.font=nf; c.border=bd; c.alignment=Alignment(wrap_text=True,vertical='top',horizontal='left' if j in (2,3,5) else 'center')
    wd.cell(row=i,column=3).hyperlink=d['url']; wd.cell(row=i,column=3).font=link
    c=wd.cell(row=i,column=6,value='=COUNTIF(Casos!$K$2:$K$%d,C%d)'%(len(rows)+1,i)); c.font=nf; c.border=bd; c.alignment=Alignment(horizontal='center',vertical='top')
wd.freeze_panes='A2'
# Resumen
wr=wb.create_sheet('Resumen')
for j,(h,w_) in enumerate([('Prioridad',10),('Curso',70),('Casos',9),('Videos',9),('Láminas',9)],1):
    c=wr.cell(row=1,column=j,value=h); c.font=hf; c.fill=hfill; c.alignment=Alignment(horizontal='center',vertical='center'); c.border=bd; wr.column_dimensions[get_column_letter(j)].width=w_
cursos=[]
for r in rows:
    if (r['prioridad'],r['curso']) not in cursos: cursos.append((r['prioridad'],r['curso']))
n=len(rows)+1
for i,(p,cu) in enumerate(cursos,2):
    vals=[p,cu,'=COUNTIF(Casos!$B$2:$B$%d,B%d)'%(n,i),'=COUNTIFS(Casos!$B$2:$B$%d,B%d,Casos!$E$2:$E$%d,"Video animado")'%(n,i,n),'=COUNTIFS(Casos!$B$2:$B$%d,B%d,Casos!$E$2:$E$%d,"Lámina")'%(n,i,n)]
    for j,v in enumerate(vals,1):
        c=wr.cell(row=i,column=j,value=v); c.font=nf; c.border=bd; c.alignment=Alignment(horizontal='left' if j==2 else 'center',vertical='top',wrap_text=True)
t=len(cursos)+2
for j,v in enumerate(['','Total','=SUM(C2:C%d)'%(t-1),'=SUM(D2:D%d)'%(t-1),'=SUM(E2:E%d)'%(t-1)],1):
    c=wr.cell(row=t,column=j,value=v); c.font=Font(name=AR,size=10,bold=True); c.border=bd; c.alignment=Alignment(horizontal='left' if j==2 else 'center')
# Notas
wn=wb.create_sheet('Notas'); wn.column_dimensions['A'].width=150
NOT=json.load(open('notas.json'))
for i,(t,b) in enumerate(NOT,1):
    c=wn.cell(row=i,column=1,value=t); c.font=Font(name=AR,size=11 if b else 10,bold=bool(b)); c.alignment=Alignment(wrap_text=True,vertical='top')
    wn.row_dimensions[i].height=max(16,14*(-(-len(t)//150))+4)
wb.move_sheet('Resumen',offset=-1)   # Casos, Resumen, Documentos, Notas
wb.active=0
out=sys.argv[1] if len(sys.argv)>1 else '/home/claude/casos/Casos_ubicacion_en_documentos_18 NOV.xlsx'
wb.save(out); print('filas',len(rows),'docs',len(dl),out)
