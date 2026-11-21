# Une la ubicacion (ubic.json) con los datos de cada caso y deja casos.json (filas del Excel)
import sys,json,re
sys.path.insert(0,'/home/claude/casos')
import casa,ubica
R=json.load(open('ubic.json'))
IDX=ubica.IDX
PRIO={x['id']:x['title'] for x in json.load(open('src/busq_prio.json'))}
def enlace(fid,gdoc=False): return ('https://docs.google.com/document/d/%s/edit'%fid) if gdoc else ('https://drive.google.com/file/d/%s/view'%fid)
CURSO={'LP':(1,'Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado'),'JR':(1,'Justicia restaurativa en la práctica del fiscal'),'SR':(1,'Sistema de responsabilidad penal para adolescentes y justicia restaurativa'),'TA':(1,'Terminaciones anticipadas del proceso penal'),'C5':(1,'Bienes en el proceso penal'),'ED':(2,'Enfoques diferenciales'),'DH':(2,'Derechos humanos aplicados a la función judicial'),'GJ':(2,'Gerencia judicial'),'EI':(3,'Estándares interamericanos de investigación de graves violaciones a los derechos humanos'),'DA':(3,'Investigación y judicialización de delitos contra el medio ambiente y los recursos naturales'),'DF':(3,'Investigación judicial y forense de la desaparición forzada'),'P3':(3,'Investigación y judicialización de los delitos de tráfico de migrantes y trata de personas')}
V,L='Video animado','Lámina'
# clave: (curso, unidad, nombre, pieza, id entrega, nombre entrega (None = el de Drive), doc de trabajo (titulo,id,gdoc) , clave en ubic del doc del curso, clave en ubic del doc de trabajo)
LPD={1:('Unidad 1','19sUHVAjN274yGppu5FfycjWOD3aNIJlZn6roKfB8g3I'),2:('Unidad 2','1vcQ0m43uwjbM8z91CjxIRs8iz0SF5G8LB7wL3h0PbCQ'),3:('Unidad 3','1KW16n185CvAqImjWceADFgSdXQSR1LyN1p-ttAYJ3Go'),4:('Unidad 4','1hcAKvKVVySOw3YK65tzZIx_mDn7xc9ICgf0YnbzOjmM')}
C=[]
def add(clave,cur,uni,nombre,pieza,ent,ent_nombre,trab,ubi=None,ubiw=None,nota=''):
    C.append(dict(clave=clave,cur=cur,uni=uni,nombre=nombre,pieza=pieza,ent=ent,ent_nombre=ent_nombre,trab=trab,ubi=ubi if ubi is not None else clave,ubiw=ubiw,nota=nota))
for k,u,n,p,e in [('LP_U1C1',1,'Traslado del escrito y congruencia',L,'1Azw5jVCZNQ2hSNqqJheWEcpNjzGFP5W6'),('LP_U1C2',1,'Técnica de redacción de los HJR',L,'1E1BxutRCbw5PqhCLgQuCYngR8GfGkL5h'),('LP_U1C3',1,'Concursos, subsidiariedad y vía procedimental',L,'1lzRZGTGe6QOVRLHePeS_LjeYvP2S2Q5B'),('LP_U1C4',1,'Maltrato psicológico y libertad probatoria',L,'1PFYbkn4W52Pcioj-aBVQfyBQiQH8tbmF'),('LP_U1C5',1,'Núcleo familiar y duración de la convivencia',L,'1hPAWlBml1Ygn7TPh_V8l6c6OeuPbYcxc'),('LP_U2C1',2,'Estudio reverso 1: escrito de acusación, flagrancia y nulidad',V,'1ZK86YTtEh9fPS5zYIk8K6dFfn7d0VgBG'),('LP_U2C2',2,'Estudio reverso 2: audiencia de prueba anticipada',V,'1-OAnn0_zO0f7K6ujq35Iv4ID5vRXdvqn'),('LP_U3C1',3,'Viabilidad en delitos contra el patrimonio económico',L,'176G0zwKjnqzzS6JRggLNdCm0fhUBlf5A'),('LP_U3C2',3,'Improcedencia por concurso o inimputabilidad',L,'1-CvmzSryuzvM_R36Ou3Chz9EWV3WeI8W'),('LP_U3C3',3,'Reversión por desviación de poder',L,'13EHY5bfvje1crltJ2qgTeZRQUgMmCRTZ'),('LP_U4C1',4,'Conciliación en inasistencia alimentaria',V,'1wQuMlgjGJiXFClq2cSXgGDb0DtjAtDq3'),('LP_U4C2',4,'Mediación en accidente de tránsito',V,'1pYNBcyXD_l6Bn7vVEiGTo8_XmK0ChOGT'),('LP_U4C3',4,'Desistimiento en violencia intrafamiliar',V,'1RstfERMeZENQA-gWr02i-wkx9r3msTtJ')]:
    add(k,'LP','U%d'%u,n,p,e,None,('Documento «%s» (casos, de la agencia)'%LPD[u][0],LPD[u][1],True),nota=('El nombre es una referencia que puso Claude: el documento solo dice «Caso de análisis %s».'%k[-1]) if u==4 else '')
JRD={'C1':('Casos 1 y 2','1Yvl7ORJWYWkP6eiIdQHXcYn3TzTZQ1z8LaEkmiI1SZQ'),'C2':('Casos 1 y 2','1Yvl7ORJWYWkP6eiIdQHXcYn3TzTZQ1z8LaEkmiI1SZQ'),'U1':('Unidad 1','1qfMktq16FumRacfW-wv0IeasBxOsIXt4ivdZy6TGawI'),'U2':('Unidad 2','1Edh0CoxVfEFErGt1XrNw5z205q6UgduoEObS5QLiNfU'),'U3':('Unidad 3','1hkKAjI_eN1-kLi7IqRnDTKwiZKwehfzD272sal6_kBg'),'U4':('Unidad 4','15AC_eHPdbjnKD1wNFgYzCMAB4_TLiLpSzKQ4jz72Qz0')}
for k,u,n,e,nota in [('C1','U2','Caso 1: una discusión en un sitio público','1x5YtIuh6_ENh49eL03JW7FxjjFeDlqko','El texto del caso en el documento de trabajo es un enlace a la presentación «Preguntas sobre Mediación. Curso JR».'),('C2','U3','Caso 2 (de lesividad alta) · Fase 1: la historia','1UvzArxMOhsLSdJOPZdjb-W00GHR3EtZ5','El título «CASO II (de lesividad alta)» aparece antes, en la evaluación de la unidad 2 (p. 78, con el marco normativo y las preguntas 4 y 5); los hechos que narra el video están en la evaluación de la unidad 3.'),('U1','U1','El encuentro en la carretera','1U4fxc4OVQkgU8kejkA-C5_s2eSnkOIzy',''),('U2','U2','La situación reflexiva: Juana pregunta por la justicia restaurativa','1_BMjlR5DUFNJ1Y4Qm-orP15iorf4KBT-',''),('U3','U3','Prosigue la situación reflexiva: ¿justicia restaurativa significa perdonar?','1_5nKCluhHy3FWtCJJcXEs_ziJxa3NbFU',''),('U4','U4','Culminamos la situación','1R9U_Cxq-IpV80Hc87dWFIg38luz1Q1xT','')]:
    add('JR_'+k,'JR',u,n,V,e,None,('Documento «%s» (de la agencia)'%JRD[k][0],JRD[k][1],True),nota=nota)
add('SR_IPANEMA','SR','U1','Caso Ipanema',V,'19RMIMz94vzubFDWettiOgud713sIqhBG','CASO IPANEMA V7.mov',('CAsoIpanema.pdf','1Dg3OQwdvPRmuJJxF_foL8ciePkPyfUMe',False),nota='El caso vuelve a citarse en la lección 4 («Estudio de caso. Caso Ipanema», p. 96).')
add('SR_NICO','SR','U1','Caso Nico: principio de culpabilidad',V,'1d_VRGsS3M5PQY2kCO-6IhPXMMsyxK3U4',None,('Caso Nico','1TWtuxipDr0u5irRp8Dz_FfOaAV6tTkj_08bR1p-4bFg',True))
add('SR_EDA','SR','No figura','Caso A: Operativo Las Lagañas',V,'1I5jYAGmimUgjEu7_PtDhGLmpSqTB4z-J','U1 caso A - las laganas.mov',('Casos hipoteticos_Edwin.docx','1CrcaP2Im1jcDhpXBKgCmMYYEtZUAbgXW',False),ubi='',ubiw='W_EDA',nota='No aparece en el PDF del curso del 11 de noviembre. El archivo entregado dice «U1».')
add('SR_EDB','SR','No figura','Caso B: El accidente de los Miradores de La Calera',V,'1cFyYCKSM7n1HmQNOKlnn7UVEds2b2TX_','U1 caso B - miradores de la calera.mov',('Casos hipoteticos_Edwin.docx','1CrcaP2Im1jcDhpXBKgCmMYYEtZUAbgXW',False),ubi='',ubiw='W_EDB',nota='No aparece en el PDF del curso del 11 de noviembre. El archivo entregado dice «U1».')
CT=('casos para talleres.docx','13Yjz-pOJaAW0-Dly7xcTcc2ty89pE8xO',False)
add('SR_CH01','SR','U3','Santiago y Valeria',V,'1pBDLMcyu__q88PCxKGPILr1G1Vmx4Qcw','CH U1 CASO 01 - Santiago y Valeria V2.mp4',CT,ubiw='W_CH01',nota='El PDF del curso solo lo nombra («Talleres de casos: Caso 1 Santiago y Valeria, Caso 2 Rodman, Caso 4 Arley»); los hechos están en el documento de trabajo.')
add('SR_CH02','SR','U4','Rodman',V,'1Sjj5IRxsRbswch9GxdStZYVPBzn0jHOg','CH U1 CASO 02 - Rodman V2.mp4',CT,nota='También se nombra en los talleres de la unidad 3 (p. 190).')
add('SR_CH03','SR','U5','Disney',V,'1XVFNsGR6rzz9F0PNx5x3BeGPyjMNM3pZ','CH U1 CASO 03 - Disney V2.mp4',CT,nota='El inventario del 17 de noviembre lo tenía en U4 «según la ficha»; en el PDF del 11 de noviembre abre la unidad 5 y se retoma en la p. 257.')
add('SR_CH04','SR','U3','Arley y Susana',V,'1oruxRqzliUTmGqfz-DgfYPQ9u_m2s6Ak','CH U1 CASO 04 - Arley y Susana V2.mp4',CT)
add('SR_CH05','SR','U3','Juan',V,'1DwIF5it-T8kFcnt-oLqd-MXT83ZQiNgW','CH U1 CASO 05 - Juan V2.mp4',CT)
add('SR_CH06','SR','No figura','Lenin',V,'1_oABIZC4_GTtUNlxi2TCK2blBRpB1m8L','CH U1 CASO 06 - Lenin V2.mp4',CT,ubi='',ubiw='W_CH06',nota='No aparece en el PDF del curso del 11 de noviembre. El archivo entregado dice «U1».')
add('SR_CHAP','SR','U5','Los Chapulines',V,'1m2qqNRiPTxRRFtbtsref2A5e3qsvQe13','U5C1_LOS_CHAPULINES_revision.mov',('CASO unidad 5 leccion2.docx','1bdDfoQMMv4EzKufLOwknAjYnOp1U_l6G',False),nota='Entregado como versión de revisión.')
VE=('Veamos un ejemplo: Curso Terminaciones Anticipadas FGN-UNAL','117ilx24cSD3UIrD1GSQPi-ICmBZunddO5RsD4XdRZFQ',True)
for k,u,n,e,en in [('01','U4','Los tres escenarios probatorios','15p-SnJ4jhxDU3mShxN2OwLSOg2Bmxp_X','TA - U4 - CASO TRES ESCENARIOS PROBATORIOS - V1'),('02','U4','El doble beneficio y el reintegro','1SuHqre4Dnba6D6QGgslnXvBXSpK7TgvK','TA - U4 - CASO EL DOBLE BENEFICIO Y EL REINTEGRO - V1'),('03','U4','Coautoría, complicidad y subrogados','1wuLxmKyAIXGkfsPOSmsuVbuTGhdqydjn','TA - U4 - CASO COAUTORÍA, COMPLICIDAD Y SUBROGADOS - V1'),('04','U4','La marginalidad alegada sin sustento','1N08Qi9yeGONJXkZFbvJEuJlShzJ9ID9W','TA - U4 - CASO MARGINALIDAD SIN SUSTENTO - V1'),('05','U4','La negociación paso a paso','175mQAe_Rc1dZEofeJ6iis1MbmrdOAER3','TA - U4 - CASO LA NEGOCIACIÓN PASO A PASO - V1'),('06','U1','El hurto de madrugada y la indagación que no se hizo','1DL7PG0FWoy_wX_KHzKisfKslewRldJZc','Hurto de madrugada TA - U1 - CASO 06 - V1'),('07','U1','¿Incumplimiento contractual o delito?','1AIEdZEaOzHoLGhE1Uk32sZFoeuVav8wN','TA - U1 - CASO INCUMPLIMIENTO O DELITO - V1'),('08','U1','El video que aparece seis meses después','1PqodrE--lZKGSsIzWfwUu2x0tOzq9XQj','TA - U1 - CASO EL VIDEO SEIS MESES DESPUÉS - V1'),('09','U1','El conductor y la maniobra','119zH7Vgo2oqu80aGMdUBJVNR_ZCmSQge','TA - U1 - CASO EL CONDUCTOR Y LA MANIOBRA - V1')]:
    add('TA_'+k,'TA',u,n,V,e,en,VE)
BD=('4 CASOS COMPLETOS','1enu-Fh1FKte8MKg6yQX9xQ-kZrx4STV_LlMEB79MTDY',True)
for k,n,e,en in [('U1','Logística C.M.R. del Norte','1DJxGFuvFqKTzXK2gIbgIiAOyMna6P5jT','CURSO BPP U1 CASO LOGÍSTICA C.M.R. DEL NORTE.mov'),('U2','El siniestro vial','1VBxrWcbI6oEgXHbJYXHK9OAdKDd4N29E','CURSO BPP U2 CASO EL SINIESTRO VIAL.mov'),('U3','Eslabón Financiero','1KGBkZ8FxwaSWhbhZB_e21nuV51SSLrfl','CURSO BPP U3 CASO ESLABÓN FINANCIERO.mov'),('U4','Los Ilustres','108gCmDrWVrjIUVdpYVJ0DptzgY7OL9c9','CURSO BPP U4 CASO LOS ILUSTRES - v2 sin preguntas.mov')]:
    add('C5_'+k,'C5',k,n,V,e,en,BD)
EDD=[('Caso: Édgar Molano','1n2um_ejZs1sDQLp-Il1G3nsiHVYigqJHnCFYNg19Mu0'),('Caso: Jairo Montero Salas','18Dh4Ez_pKGdfhMPjpoTZUjzbRFWDl1814WWlyqcCUIs'),('Caso: el patrullero Wilmer','1PDSbCfkrhv0y4PSVUcmEX5eEJrIOHeiYVSkM612ylRw'),('Caso: la niña del resguardo de Putumayo','157Z6fbWlkv0BaY1ArQs-nz7xREii0XOpulEToytgOQU'),('Caso: la denuncia de Valentina','1EQLkbB2Qh83Cf8drTzhu-hFBT6Xze3sFI7hngeohDV0')]
for n,(nom,e) in enumerate([('Édgar Molano','1y73bAumsCauu1EpopufJZHYtp0wBoCPa'),('Jairo Montero Salas','1BZUppd4nYSmb_06Ps86qqYYFDxJXD1-h'),('El patrullero Wilmer','13nUHnPO0K35pLLYFIoGPl59IUxAdVcBo'),('La niña del resguardo de Putumayo','14W63d4YqaqSkyk-Fva7H0Hcz2Np6gKNn'),('La denuncia de Valentina','1fP0XJPaVtIvyk0mnHuL2C7aZyGsArCOP')]):
    add('ED_C%d'%(n+1),'ED','U%d'%(n+1),nom,V,e,None,(EDD[n][0],EDD[n][1],True))
DHD=['1Xh-74ikYMaSmH_MS3aJWSfye_QtVCTWNtdrvT-ym_wI','1qY_LuQ-TacvdjtR02eScCc6aFkyRQx7E3pQeZ2Q_4Bs','1GvGp-8rzhQnvgY8xn21WucXNXKww_Zfzv7HdaXmYLec','1jsfGwEkwR2Rsvnqj8N_btg5P1I9xezVZVkIT8sCfdI0','143EoBika5MUsoJLpV7ZsG2J6ot6r5u4xTEB7WqOZu8I']
for n,(nom,e) in enumerate([('Llega la noticia','1l8wOrTutaeOcaE__Rz1hvr6EZ8FwYtOp'),('La defensa invoca un tratado','1VgEijZn-ADzMw0-epZwhOY1gVRGgC3OJ'),('Dos versiones de la misma entrevista','1TPTzhZjC2RZ2yzvAsYCMB_70tm9iJwyT'),('La medida de aseguramiento','14k_ryU-mtLcMxL4m7DxLtah5W74_x23-'),('La decisión integral y el giro','1t-mlOu56P7z2rpCC44mKbn-avABOxhGI')]):
    add('DH_U%d'%(n+1),'DH','U%d'%(n+1),'Expediente Carmen Elisa Rojas · '+nom,V,e,None,('Guión animado %d (Unidad %d)'%(n+1,n+1),DHD[n],True),nota='El guion del video no está transcrito en el documento de la unidad: allí solo se presenta la escena; el texto completo está en el «Guión animado».')
GD=('Gerencia judicial - Casos varios','1kZrQeecvuwx4Jj9h_7PDxAZFMtCGakATgyvjp_W-7QE',True)
for k,u,n,e in [('T1','U1','El despacho de los 2000 casos','1C87HmDfSeiTQGjLza6mgpmsm0vXKy2eO'),('T3','U1','Aceptar o negociar','1eSqAQg5fMnb3GyPmaeQc4I3SxFhk-mlM'),('T4','U2','Dos situaciones al comenzar la semana','11QkDBZkdm0KKKfEmobQpCoftqlDROOcT')]:
    add('GJ_'+k,'GJ',u,n,V,e,None,GD)
EID=('Estándares Interamericanos - Actividades de aprendizaje','1er8p3nu7Ut2d97i0XsJV92v8mR516YiHlVV9o5yJOnE',True)
for k,u,n,p,e in [('S01','U1','¿Quién responde por una violación de derechos humanos?',V,'1y_PWCYJf6hOIqIjUciJBYZXfO7vbTq-S'),('S02','U1','¿Cómo se organiza la protección internacional de los derechos humanos?',L,'1PZ9fHEXNxDPBY3Czafzsf7uQDPvni1Wv'),('S03','U1','¿Qué fuente internacional necesito consultar?',L,'1-ztqAdFBKJWNpOgFzgruSfKDn-EvodmN'),('S04','U1','¿Cómo utilizaría una fuente internacional en una investigación penal?',V,'1DN51MFrMicSmIJ268Ja1GahCnHHt25WK'),('S05','U1','¿Cómo utilizaría la jurisprudencia interamericana en una investigación?',L,'15et_4JW7t9Me7ufRowZB4uQa43HPaVOI'),('S06','U4','La muerte de dos jóvenes',V,'1nBvkdockMaDJ3vuukZTowobYsEtF-xUP'),('S07','U4','La fosa clandestina',V,'1G10VID5HC4ft1t8pJEUHXG5mo_AxbQF7'),('S08','U4','Bajo custodia policial',V,'17S0IWslRxLEWdGqjoq3P7LJgIOgnkacU'),('S09','U1','¿Es suficiente abrir una investigación penal?',L,'1rW9ZCYG0LYcw5BE5kK40svTTwY1zO0Ca'),('S10','U1','¿Qué examina la Corte Interamericana de una investigación penal?',L,'1llu2OjLW25etfyrHdpKHJFn1NBJnwdgJ'),('S11','U1','¿Qué decide y qué ordena la Corte Interamericana?',L,'1TzJYu7cv3hDtlt3NUP3NTUiMOjptJKWl')]:
    add('EI_'+k,'EI',u,n,p,e,None,EID)
DAD=('6_11_2026_CURSO_DELITOS AMBIENTALES_DEFINITIVO.pdf','1HOT5p71fNf2kfg93Q-NnQZMMdYRHv0Xa',False)
for k,u,n,e,en,nota in [('V01','U1','Problemática ambiental y criminalidad','1njdmwH4XbTmEs_dL2xlIXwBNlRbe8Wmi',None,'Video explicativo, no es un caso: el documento pide el recurso y el guion es nuestro.'),('V02','U3','Plan de priorización de la Fiscalía General de la Nación','1KMl1--ublZVzV6sIiCvWjAOhcpmjaKFc','DA_V02_v1.mp4','Video explicativo, no es un caso: el documento pide el recurso y el guion es nuestro.'),('V03','U3','Técnicas especiales de investigación','1AxpjnIeS4jWqoNXbbgJiBLp1_wm5ZyVo','DA_V03_v1.mp4','Video explicativo, no es un caso: el documento pide el recurso y el guion es nuestro.'),('V04','U4','El río y la fábrica: midiendo el daño para reparar','1o9W4qQmyTx9nSo9vuARYo3Qg-hJCTWVH','DA_V04_v1.mp4',''),('V05','U4','Operación «Raíces Profundas»','1uAEvnUkD2xnqZse-DifMQUslPOpECKNc','DA_V05_v1.mp4',''),('V06','U4','El caso Francisco','1BK8lxgBAQvLwoL0OzUvqk_0tcOoqTHVK','DA_V06_v1.mp4','El libreto está en el insumo «DOCUMENTO 1 - CASO FRANCISCO», no en el PDF.')]:
    add('DA_'+k,'DA',u,n,V,e,en,DAD,nota=nota)
DFD=['1ixWWF0NNTmUp_vYIphBuLEGzehV6hZdpXt7ba1iPwbA','','','','']
import glob
for f in sorted(glob.glob('/home/claude/repo/cursos/desaparicion_forzada/CASO MIRIAM Y MARIANA/CAP*_fuente.md')):
    n=int(re.search(r'CAP(\d)',f).group(1)); m=re.search(r'origen: https://docs.google.com/document/d/([\w-]+)',open(f,encoding='utf-8').read()); DFD[n-1]=m.group(1)
for n,(nom,e) in enumerate([('El eco en la plaza y la respuesta de papel','1vqoOQYc-XWMCC5TXbCBoy3-xpBBF90Tv'),('Relojes en pausa y el clamor en las redes','1-FxKqndSOW8R4uVvVa2Lgs5w5Jl-HtZm'),('El engranaje roto y el mapa de competencias','1KroP4wBWgKOxh9XElvUWW8iRwYsxdl_v'),('Las voces que no se apagan y el dolor en la ventanilla','1V_8O-F6i1XQq-HO3MQPgeUvR42i31XQ2'),('La tierra habla y la matriz del silencio','1EjKILyuHiynlGtG23d62kWm8nQmYIlbJ')]):
    add('DF_%d'%(n+1),'DF','U%d'%(n+1),'Caso integrador Miriam y Mariana · capítulo %d: %s'%(n+1,nom),V,e,None,('Capítulo %d del caso integrador'%(n+1),DFD[n],True),ubi=('' if n==0 else None),ubiw=('W_DF1' if n==0 else None),nota=('El capítulo 1 no está en el vaciado de la unidad 1 (los capítulos 2 a 5 sí abren el desarrollo temático de sus unidades); por analogía va al comienzo de «3.1.4. Desarrollo del contenido temático», antes de la lección 1.' if n==0 else ''))
SD=('16 situaciones','13Q4a3gys0g72GVogX78s13zod5uUyFxM0VZDsxQnFh4',True)
for k,u,n,p,e in [('A','U1','La última llamada',V,'1NOrLYqM3SISqj5oC174GuyWdyrFPU6zk'),('B','U1','La nota sobre la cama',V,'1n2jhqJmT-oGddqxE2O64dbihiM8u4dxs'),('C','U1','El plazo de 24 horas',V,'18SPJm9joACmbK98hgsBLNUgklQqDXEBV'),('D','U1','La creciente de La Miel',V,'18lXpmZi55AymJXk28wDVwGKbTG0bQWmB'),('E','U1','El camión hacia El Vergel',V,'153DPIoePz6aweRTvmOLkNrY05XpNUFz2'),('F','U2','El primer contacto',L,'1aEQFk8FsyUvpLv4_bG45X5OkArst4hCQ'),('G','U2','La vocera',V,'1T-tKzFObY_IezsUEBQ7nsg7Kk8P2UVyV'),('H','U4','Dos mujeres, dos impactos',L,'1M1EMHp_Ma8pwtARk-FI7rtYvgk2PzDNg'),('I','U4','La minuta',L,'1_WoLwU97KPKYVlvb-PhMELgr5E0R1rEw'),('J','U5','Las piezas del expediente',L,'11Nl5UIU-dRidBn2lRWHvRX3g9Z8Xbi4v'),('K','U5','El informe integral',L,'1VBu1-GfK8oYmIrQH2Q9WFgvJZwALRBww')]:
    add('SIT_'+k,'DF',u,'Situación %s: %s'%(k,n),p,e,None,SD,nota=('Además del video hay una lámina con el mismo nombre.' if k=='G' else ''))
P3D=[('Caso: «El hospedaje El Mirador»','1gy9Bm3EVFIMqiZC8OLsJ5g17duU8SbZWx-PWkFfYP5M'),('Caso: «El taller del segundo piso»','1le_Tbs0hAhTccLUO--X6FiLzG6ldZD4nD5eSO2nv6zA'),('Caso: «Ruta del Golfo»','1_d_xFKKmLzGD6tp0OOt4bU3bdA6kVXyFg-UAWfeN0_Y'),('Caso: «Puerto de salida»','1MH0Vn81VTmm28DnYX2hi5QRy0Zws5BRP0VFqMJCAY8Y'),('Caso: «Voces, registros y cuentas»','1PnIMOzGKwlFMuHfwUjcbxvqkSS-xmMYDQWjP0STWhVw')]
for n,(nom,e,en) in enumerate([('El hospedaje El Mirador','1W75e4q2pomjGOrzZsEndTjttKfVRaO4W','CURSO TRATA CASO 1 - EL HOSPEDAJE EL MIRADOR v2.mov'),('El taller del segundo piso','1NaTTNiOjsEZXBNABNCE8la9D90yvJtSN','CURSO TRATA CASO 2 - EL TALLER DEL SEGUNDO PISO v2.mov'),('Ruta del Golfo','15-chSs7wA5Q9O56C2wABOg7IBXuyrJuv','P3C3_RUTA_DEL_GOLFO_v1.mov'),('Puerto de salida','1KBA02RL32zmFTXY9JGr2sDc_XfbqZhj6','P3C4_PUERTO_DE_SALIDA_v4_revisado.mp4'),('Voces, registros y cuentas','1IrPdImuzkDqQc-ErgX1MYGque9HbIFWh','P3C5_CASO 05-REGISTROS_Y_CUENTAS_.mp4')]):
    add('P3_C%d'%(n+1),'P3','U%d'%(n+1),nom,V,e,en,(P3D[n][0],P3D[n][1],True))
import subprocess
_pt={}
def pagtxt(pdf,p):
    if (pdf,p) not in _pt: _pt[(pdf,p)]=ubica.norm(subprocess.run(['pdftotext','-f',str(p),'-l',str(p),pdf,'-'],capture_output=True,text=True).stdout)
    return _pt[(pdf,p)]
def T(fid,k): return casa.carga(fid)[k]['t']
def campos(r):
    fid=r['fid']; i=r['i']; d={}
    lok=bool(r['leccion'] and r['des'] is not None and r['leccion'][0]>r['des'])
    en_act=r['act'] is not None and (r['des'] is None or r['act']>r['des']) and not (lok and r['leccion'][0]>r['act'])
    sec=[]
    if en_act: sec.append(T(fid,r['act']))
    elif lok: sec.append(r['leccion'][1])
    elif r['des'] is not None: sec.append(T(fid,r['des'])+' (al comienzo, antes de la primera lección)')
    base=max([x for x in (r['des'],r['act'],r['leccion'][0] if lok else None) if x is not None] or [0])
    if r.get('tema') and r['tema'][0]>(r['des'] or 0): sec.append(r['tema'][1])
    if r['num'] and r['num'][0]>base and not re.search(r'Desarrollo del contenido|Actividades y productos',r['num'][1]): sec.append('apartado «%s»'%r['num'][1])
    d['seccion']=' › '.join(sec)
    a=r['actividad']; d['actividad']=a[1] if a and i-a[0]<70 and a[0]>=(r['des'] or 0) else ''
    e=r.get('estrategia'); d['estrategia']=e[1] if e and i-e[0]<70 else ''
    f=r['fase']; d['fase']=f[1] if f and i-f[0]<45 else ''
    c=r['recurso']; d['recurso']=c[1] if c and i-c[0]<25 else ''
    return d
filas=[]
for c in C:
    pr,curso=CURSO[c['cur']]
    row=dict(c); row['prioridad']=pr; row['curso']=curso
    row['ent_nombre']=c['ent_nombre'] or PRIO.get(c['ent'],'')
    for pref,key in (('c',c['ubi']),('w',c['ubiw'])):
        if not key: continue
        r=R[key]; fid=r['fid']; pars=casa.carga(fid)
        j=r['j']
        if key=='W_CH06': j=len(pars)-1
        it=r['it']; i=r['i']
        ie=i+1 if (r['modo']=='r' and it==i and j>i and len(pars[i]['t'])<140) else i
        w=lambda t,n,fin=False: ' '.join(t.split()[-n:] if fin else t.split()[:n])
        es_pdf='.docx' not in IDX[fid]['files']
        pdf=IDX[fid]['files']['.pdf'] if es_pdf else '/home/claude/casos/lo/%s.pdf'%fid
        pf=pars[j]['pag']; cola=ubica.norm(w(pars[j]['t'],9,True))[-22:]
        for q in (pf,pf+1,pf+2):
            if cola in pagtxt(pdf,q): pf=q; break
        row[pref]=dict(fid=fid,doc=IDX[fid]['title'],url=enlace(fid, gdoc=(fid in ('1ixWWF0NNTmUp_vYIphBuLEGzehV6hZdpXt7ba1iPwbA',))),pag_ini=pars[it]['pag'],n_ini=pars[it]['n'],pag_fin=pf,titulo=pars[it]['t'][:160],empieza=w(pars[ie]['t'],12),termina=w(pars[j]['t'],9,True),exacta=es_pdf,fin_aprox=r['fin_aprox'],pag_txt=pars[ie]['pag'],n_txt=pars[ie]['n'],npags=pars[-1]['pag'],**campos(r))
    filas.append(row)
json.dump(filas,open('casos.json','w'),ensure_ascii=False,indent=1)
if __name__=='__main__':
    print(len(filas))
    for f in filas:
        c=f.get('c')
        if not c: print('%-10s (sin doc curso) w:%s'%(f['clave'],bool(f.get('w')))); continue
        print('%-10s sec:%s | act:%s | est:%s | fase:%s | rec:%s'%(f['clave'],c['seccion'][:70],c['actividad'][:48],c['estrategia'][:50],c['fase'][:36],c['recurso'][:44]))
