// pieza.js — fábricas de secciones para los videos del EMB (corte sin voz).
// Cada video define sus textos de locución y una lista de secciones; los tiempos salen de la
// proporción de caracteres (1,6 cuadros por carácter) hasta que llegue la voz medida.
// Requiere core.js. Las escenas usan los activos en /home/claude/emb/m1v1_assets.
const A='file:///home/claude/emb/m1v1_assets/';
const P=n=>A+'placas/'+n+'.jpg';
const C=(n,i)=>A+'clips/'+n+'/'+String(Math.max(0,Math.min(120,Math.floor(i)))).padStart(3,'0')+'.jpg';
const NS='http://www.w3.org/2000/svg';
let pend=[];
function src(im,u){if(im.__u!==u){im.__u=u;im.src=u;pend.push(im.decode().catch(()=>{}));}}
function el(tag,cls,par,html){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;par.appendChild(e);return e;}
function sv(tag,par,at){const e=document.createElementNS(NS,tag);for(const k in at)e.setAttribute(k,at[k]);par.appendChild(e);return e;}
function capa(par){const box=el('div','lay',par);const im=el('img','',box);const im2=el('img','',box);im2.style.opacity=0;return {box,im,im2};}
// cuadro fraccionario de un clip: se funden el cuadro i y el i+1 → cámara lenta sin saltos
function clipF(c,n,f){f=Math.max(0,Math.min(120,f));const i=Math.floor(f),fr=f-i;src(c.im,C(n,i));if(fr>0.02&&i<120){src(c.im2,C(n,i+1));c.im2.style.opacity=fr;}else c.im2.style.opacity=0;}
function kb2(c,s,x=0,y=0){kb(c.im,s,x,y);kb(c.im2,s,x,y);}
function placa(c,n){src(c.im,P(n));c.im2.style.opacity=0;}
// velocidad para que la ventana del clip llene la ranura sin congelarse (nunca más lento que 0,55)
function velAuto(v,D){return Math.max(0.55,Math.min(1,(v[1]-v[0])/Math.max(1,D)));}
function kb(im,s,x=0,y=0){im.style.transform=`translate(${x}px,${y}px) scale(${s})`;}
function vis(e,on){e.style.display=on?'':'none';}
function sube(e,t,t0,t1=1e9,dy=46,dur=16){const a=E.outCubic(R(t,t0,t0+dur)),b=E.inOutCubic(R(t,t1,t1+12));
  e.style.opacity=a*(1-b);e.style.transform=`translate(0,${dy*(1-a)-dy*0.5*b}px)`;}
function letras(arr,t,t0,paso=1.1,dur=14){arr.forEach((u,i)=>{const k=E.outCubic(R(t,t0+i*paso,t0+i*paso+dur));u.style.transform=`translate(0,${105*(1-k)}%)`;});}
const FPC=1.6;
function blk(txt,cola=36){const V=window.VOZ&&window.VOZ[txt.slice(0,40)];
 if(V){const m=V.mapa,ip=c=>{if(c<=m[0][0])return m[0][1];for(let i=1;i<m.length;i++)if(c<=m[i][0]){const a=m[i-1],b=m[i];return a[1]+(b[1]-a[1])*(b[0]>a[0]?(c-a[0])/(b[0]-a[0]):0);}return m[m.length-1][1];};
  return {txt,voz:V,d:V.d,k:p=>{if(typeof p==='number')return p;if(p==='fin')return 1e9;const i=txt.indexOf(p);if(i<0)throw new Error('frase no encontrada: '+p);return Math.round(ip(i))+2;}};}
 return {txt,d:Math.round(txt.length*FPC)+cola,k:p=>{if(typeof p==='number')return p;if(p==='fin')return 1e9;const i=txt.indexOf(p);if(i<0)throw new Error('frase no encontrada: '+p);return Math.round(i*FPC)+6;}};}
function etiqueta(root){return el('div','etq',root,'Situación hipotética con fines pedagógicos');}
function etqDraw(e,t,d){e.style.opacity=E.outCubic(R(t,18,34))*(1-R(t,d-6,d));}
const ICO={
 rayo:'M30 18 L66 18 L48 52 L76 52 L38 106 L50 64 L26 64 Z',
 reja:'M14 14h26v26h-26zM48 14h26v26h-26zM82 14h26v26h-26zM14 48h26v26h-26zM82 48h26v26h-26zM14 82h26v26h-26zM48 82h26v26h-26zM82 82h26v26h-26z',
 globo:'M16 20 h90 a10 10 0 0 1 10 10 v44 a10 10 0 0 1 -10 10 h-50 l-22 20 v-20 h-18 a10 10 0 0 1 -10 -10 v-44 a10 10 0 0 1 10 -10 Z M34 42 h56 M34 60 h38',
 check:'M18 62 L48 92 L104 30',
 cruz:'M28 28 L94 94 M94 28 L28 94',
 flecha:'M14 61 H100 M70 31 L104 61 L70 91',
 libro:'M61 26 C 46 16, 26 16, 12 22 V 100 C 26 94, 46 94, 61 104 C 76 94, 96 94, 110 100 V 22 C 96 16, 76 16, 61 26 Z M61 26 V 104',
 doc:'M30 10 h44 l22 22 v80 h-66 Z M74 10 v22 h22 M44 56 h36 M44 72 h36 M44 88 h24',
 sobre:'M12 30 h98 v62 h-98 Z M12 30 L61 70 L110 30',
 balanza:'M61 14 V 104 M36 104 H86 M20 34 H102 M20 34 L8 70 H32 Z M102 34 L90 70 H114 Z',
 manos:'M20 70 C 20 40, 44 34, 61 52 C 78 34, 102 40, 102 70 C 102 90, 80 104, 61 108 C 42 104, 20 90, 20 70 Z',
 escudo:'M61 12 L102 26 V 58 C 102 84, 84 100, 61 110 C 38 100, 20 84, 20 58 V 26 Z',
 megafono:'M18 48 h22 l50 -26 v78 l-50 -26 h-22 Z M40 74 l8 30 h14 l-8 -30',
 eslabon:'M20 61 a 22 22 0 0 1 22 -22 h 18 a 22 22 0 0 1 0 44 h -18 M102 61 a 22 22 0 0 1 -22 22 h -18 a 22 22 0 0 1 0 -44 h 18',
 ojo:'M10 61 C 34 24, 88 24, 112 61 C 88 98, 34 98, 10 61 Z M61 45 a16 16 0 1 0 0.1 0',
 reloj:'M61 14 a47 47 0 1 0 0.1 0 M61 34 V 61 L 80 74',
 pregunta:'M40 42 C 40 20, 84 20, 84 42 C 84 60, 61 60, 61 78 M61 98 v2',
 persona:'M61 18 a18 18 0 1 0 0.1 0 M26 106 C 26 70, 96 70, 96 106',
 casco:'M18 80 H104 M26 80 C 26 44, 96 44, 96 80 M54 46 V 30 H68 V 46',
 tienda:'M14 46 H108 L98 18 H24 Z M22 46 V 104 H100 V 46 M48 104 V 72 H74 V 104',
 casa:'M14 60 L61 20 L108 60 M26 52 V 104 H96 V 52',
 registro:'M28 12 h66 v98 h-66 Z M42 36 h38 M42 56 h38 M42 76 h24',
};

// ── entradas: cómo se monta una sección sobre la anterior ──
function entradaBuild(r,cont,tipo,o={}){
 const s=sv('svg',r,{class:'ov',width:1920,height:1080});
 const E_={tipo,dur:{iris:28,tren:24,amarillo:18,puertas:24,fundido:16,corte:0}[tipo]||0};
 if(tipo==='iris'){E_.cx=o.x||1240;E_.cy=o.y||560;E_.aro=sv('circle',s,{cx:E_.cx,cy:E_.cy,r:0,fill:'none',stroke:'#DF1F15','stroke-width':14});E_.est=sv('circle',s,{cx:E_.cx,cy:E_.cy,r:0,fill:'#fff',stroke:'#DF1F15','stroke-width':8});}
 if(tipo==='tren'){E_.g=sv('g',s,{});sv('rect',E_.g,{x:-2400,y:-60,width:2400,height:1200,fill:'#DF1F15'});
  sv('path',E_.g,{d:'M 0 -60 L 140 -60 Q 330 -60 330 300 L 330 780 Q 330 1140 140 1140 L 0 1140 Z',fill:'#DF1F15'});
  for(let i=0;i<5;i++)sv('rect',E_.g,{x:-2300+i*440,y:300,width:330,height:300,rx:40,fill:'#fff',opacity:.92});
  sv('rect',E_.g,{x:-2400,y:740,width:2560,height:26,fill:'#FFC400'});sv('rect',E_.g,{x:60,y:300,width:190,height:300,rx:60,fill:'#fff',opacity:.92});}
 if(tipo==='amarillo'){E_.bar=el('div','abs',r);Object.assign(E_.bar.style,{left:0,top:0,width:'2400px',height:'1080px',background:'#FFC400'});}
 if(tipo==='puertas'){E_.pu=[0,1].map(i=>{const d=el('div','abs',r);Object.assign(d.style,{top:0,width:'960px',height:'1080px',background:'#E9ECEF',left:(i*960)+'px'});
   d.innerHTML=`<div style="position:absolute;${i?'left':'right'}:0;top:0;width:18px;height:100%;background:#FFC400"></div><div style="position:absolute;${i?'left':'right'}:140px;top:210px;width:300px;height:420px;border-radius:40px;background:#CED4DA"></div><div style="position:absolute;left:0;right:0;top:820px;height:30px;background:#DF1F15"></div>`;return d;});}
 E_.draw=(t)=>{
  if(tipo==='iris'){const io=E.inOutExpo(R(t,4,28)),rad=io*1300;cont.style.clipPath=t<28?`circle(${Math.max(.1,rad)}px at ${E_.cx}px ${E_.cy}px)`:'none';
   E_.est.setAttribute('r',22*E.outBack(R(t,0,8),3)*(1-R(t,6,12)));E_.aro.setAttribute('r',rad);E_.aro.style.opacity=1-R(t,18,28);}
  if(tipo==='tren'){const x=lerp(-400,1920+2500,E.inOutCubic(R(t,0,24)));E_.g.setAttribute('transform',`translate(${x} 0)`);cont.style.clipPath=t<24?`inset(0 ${Math.max(0,1920-(x-2400))}px 0 0)`:'none';s.style.display=t<26?'':'none';}
  if(tipo==='amarillo'){const w=E.inOutExpo(R(t,0,18));const X=lerp(1920,-2500,w);E_.bar.style.transform=`translate(${X}px,0) skewX(-12deg)`;cont.style.clipPath=t<18?`inset(0 0 0 ${Math.max(0,X+240)}px)`:'none';vis(E_.bar,t<20);}
  if(tipo==='puertas'){const cl=E.inOutCubic(R(t,0,10))*(1-E.inOutCubic(R(t,10,24)));E_.pu[0].style.transform=`translate(${-960*(1-cl)}px,0)`;E_.pu[1].style.transform=`translate(${960*(1-cl)}px,0)`;E_.pu.forEach(p=>vis(p,cl>0.001));cont.style.opacity=t<10?0:1;}
  if(tipo==='fundido'){const a=E.inOutCubic(R(t,0,16));cont.style.opacity=a;cont.style.transform=`scale(${1.04-0.04*a})`;}
 };
 return E_;
}

// ── secciones ──
// título: ventana redondeada que sube desde la línea roja, con un clip o placa adentro
function S_titulo(o){return {id:'T',d:o.d||104,ov:0,
 build(r){r.style.background='#fff';this.win=el('div','',r);Object.assign(this.win.style,{position:'absolute',overflow:'hidden'});
  this.v=el('img','',this.win);Object.assign(this.v.style,{position:'absolute',width:'1920px',height:'1080px',objectFit:'cover'});this.v2=el('img','',this.win);Object.assign(this.v2.style,{position:'absolute',width:'1920px',height:'1080px',objectFit:'cover',opacity:0});
  const s=sv('svg',r,{class:'ov',width:1920,height:1080});this.lin=sv('path',s,{d:'M 120 880 L 1800 880',stroke:'#DF1F15','stroke-width':10,'stroke-linecap':'round',fill:'none'});
  this.ante=el('div','ante abs',r,o.ante);Object.assign(this.ante.style,{left:'120px',top:(o.lineas.length>1?402:470)+'px'});
  this.tit=el('div','k1 abs',r);Object.assign(this.tit.style,{left:'114px',top:(o.lineas.length>1?452:520)+'px'});
  this.L=[];o.lineas.forEach(x=>{const l=el('span','lin',this.tit,x);this.L.push(...partir(l));});},
 draw(t){trazo(this.lin,E.outExpo(R(t,0,22))*(1-E.inOutCubic(R(t,70,90))));
  if(!this.wx){const rr=this.tit.getBoundingClientRect();this.wx=Math.max(760,Math.min(980,rr.right+60));}
  const op=E.outExpo(R(t,10,40)),ex=E.inOutCubic(R(t,70,98));
  const x=lerp(this.wx,0,ex),w=lerp(1800-this.wx,1920,ex),b=lerp(870,1080,ex),h=lerp(700*op,1080,ex),rad=lerp(30,0,ex);
  Object.assign(this.win.style,{left:x+'px',top:(b-h)+'px',width:w+'px',height:h+'px',borderRadius:rad+'px'});
  const s=lerp(1.14,1.0,E.inOutCubic(R(t,0,this.d)));for(const v of [this.v,this.v2]){v.style.left=(-x)+'px';v.style.top=(-(b-h))+'px';v.style.transform=`scale(${s})`;}
  if(o.clip){const f=Math.min(120,(o.desde||0)+t*(o.vel||(120-(o.desde||0))/(this.d+28))),i=Math.floor(f);src(this.v,C(o.clip,i));if(f-i>0.02&&i<120){src(this.v2,C(o.clip,i+1));this.v2.style.opacity=f-i;}else this.v2.style.opacity=0;}else src(this.v,P(o.placa));
  this.ante.style.opacity=E.outCubic(R(t,14,30))*(1-E.inOutCubic(R(t,68,84)));this.ante.style.transform=`translate(${-60*E.inOutCubic(R(t,68,86))}px,0)`;
  letras(this.L,t,18,1.0,16);this.tit.style.opacity=1-E.inOutCubic(R(t,70,86));this.tit.style.transform=`translate(${-90*E.inOutCubic(R(t,70,90))}px,0)`;
 },subs:[[70,98]]};}

// planos: secuencia de tomas (clip o placa) con cámara horneada y textos cinéticos
// o={id, txt, entrada, entradaOpt, planos:[{en, clip|placa, ventana:[a,b], vel, s:[s0,s1], x:[..], y:[..], filtro}], textos:[{html, en, hasta, left, top, dy}], sombra:true, etiqueta:true}
function S_planos(o){const T=blk(o.txt,o.cola);return {voz:T.voz,id:o.id,d:T.d+(o.extra||0),ov:o.ov!=null?o.ov:({iris:28,tren:24,amarillo:18,puertas:12,fundido:16,corte:0}[o.entrada]||0),
 build(r){this.cont=el('div','sec',r);
  this.pl=o.planos.map(p=>({p,c:capa(this.cont),en:T.k(p.en||0)}));
  this.pl.forEach((x,i)=>{x.fin=i<this.pl.length-1?T.k(this.pl[i+1].p.en):1e9;});
  this.som=el('div','lay',this.cont);this.som.style.background='linear-gradient(0deg,rgba(15,18,22,.78) 0%,rgba(15,18,22,0) 52%)';
  this.som2=el('div','lay',this.cont);this.som2.style.background='linear-gradient(180deg,rgba(15,18,22,.55) 0%,rgba(15,18,22,0) 34%)';
  this.tx=(o.textos||[]).map(x=>{let bar=null;if(x.banda){bar=el('div','abs',this.cont);Object.assign(bar.style,{left:'-120px',top:((x.top||790)-34)+'px',width:(x.ancho||1560)+'px',height:(x.alto||200)+'px',background:x.banda===true?'#FFC400':x.banda,transform:'skewX(-16deg)',transformOrigin:'0 100%',boxShadow:'0 24px 60px rgba(0,0,0,.25)'});}
   const e=el('div','abs',this.cont,x.html);Object.assign(e.style,{left:(x.left||120)+'px',top:(x.top||790)+'px'});return {x,e,bar,a:T.k(x.en),b:x.hasta?T.k(x.hasta)-10:1e9};});
  if(o.cierre==='puertas'){this.blanco=el('div','lay',r);this.blanco.style.background='#fff';this.pc=[0,1].map(i=>{const d=el('div','abs',r);Object.assign(d.style,{top:0,width:'960px',height:'1080px',background:'#E9ECEF',left:(i*960)+'px'});
   d.innerHTML=`<div style="position:absolute;${i?'left':'right'}:0;top:0;width:18px;height:100%;background:#FFC400"></div><div style="position:absolute;${i?'left':'right'}:140px;top:210px;width:300px;height:420px;border-radius:40px;background:#CED4DA"></div><div style="position:absolute;left:0;right:0;top:820px;height:30px;background:#DF1F15"></div>`;return d;});}
  this.anyTop=(o.textos||[]).some(x=>(x.top||790)<400);
  if(o.etiqueta!==false)this.e=etiqueta(this.cont);
  this.ent=entradaBuild(r,this.cont,o.entrada,o.entradaOpt);},
 draw(t){const d=this.d;this.ent.draw(t);
  let cur=this.pl[0];for(const x of this.pl)if(t>=x.en)cur=x;
  this.pl.forEach(x=>vis(x.c.box,x===cur));
  const p=cur.p,u=t-cur.en,D=Math.min(cur.fin,d)-cur.en,k=E.inOutCubic(R(u,0,D));
  if(p.clip){const v=p.ventana||[0,120];clipF(cur.c,p.clip,Math.min(v[1],v[0]+u*(p.vel||velAuto(v,D))));}else placa(cur.c,p.placa);
  const S=p.s||[1.04,1.12],X=p.x||[0,0],Y=p.y||[0,0];kb2(cur.c,lerp(S[0],S[1],k),lerp(X[0],X[1],k),lerp(Y[0],Y[1],k));
  cur.c.im.style.filter=cur.c.im2.style.filter=p.filtro||'none';
  const hay=this.tx.some(x=>t>=x.a-8&&t<x.b+12);
  this.som.style.opacity=lerp(+this.som.style.opacity||0,hay?1:0.0,0)+0;this.som.style.opacity=hay?E.outCubic(R(t,Math.min(...this.tx.map(x=>x.a))-14,Math.min(...this.tx.map(x=>x.a))))*1:0.25;
  this.som2.style.opacity=this.anyTop?1:0;
  this.tx.forEach(x=>{sube(x.e,t,x.a+(x.bar?8:0),Math.min(x.b,d-14),x.x.dy||46,x.x.dur||16);
   if(x.bar){const a=E.outExpo(R(t,x.a-4,x.a+16)),b=E.inOutCubic(R(t,Math.min(x.b,d-14),Math.min(x.b,d-14)+14));x.bar.style.transform=`skewX(-16deg) scaleX(${a*(1-b)})`;x.bar.style.opacity=a>0?1:0;}});
  if(this.pc){const cl=E.inOutCubic(R(t,d-50,d-30))*(1-E.inOutCubic(R(t,d-24,d-2)));this.pc[0].style.transform=`translate(${-960*(1-cl)}px,0)`;this.pc[1].style.transform=`translate(${960*(1-cl)}px,0)`;this.pc.forEach(q=>vis(q,cl>0.001));vis(this.blanco,t>=d-30);}
  if(this.e)etqDraw(this.e,t,d);
 },subs:[[0,({iris:28,tren:24,amarillo:18,puertas:24,fundido:16}[o.entrada]||0)]].concat(o.cierre?[[T.d+(o.extra||0)-50,T.d+(o.extra||0)]]:[])};}

// tarjetas: fondo en duotono amarillo (Sebastián: el rojo intenso pesa demasiado), cabecera y n tarjetas en perspectiva que se activan con la voz
// o={id, txt, fondo, cab:{tit,sub}, items:[{tit, def, ej, ico, en, rojo}], banda:{html,en}, alto}
// tarjetas: fondo en duotono amarillo, gris o blanco (Sebastián: el rojo intenso pesa demasiado),
// entran empujando la toma anterior; la activación se funde, no salta
// o={id, txt, fondo:'<placa>_duoY'|'<placa>_duoG'|'blanco', cab:{tit,sub}, items:[{tit, def, ej, ico, en}], banda:{html,en}, alto, top}
function S_tarjetas(o){const T=blk(o.txt,o.cola);const n=o.items.length;return {voz:T.voz,id:o.id,d:T.d,ov:20,
 build(r){this.bg=capa(r);
  if(o.fondo==='blanco'){r.style.background='#F4F5F7';vis(this.bg.box,false);
   const g=sv('svg',r,{class:'ov',width:1920,height:1080});for(let i=0;i<16;i++)sv('line',g,{x1:-200+i*160,y1:0,x2:-200+i*160+560,y2:1080,stroke:'#E6E8EC','stroke-width':2});
   sv('circle',g,{cx:1700,cy:180,r:260,fill:'none',stroke:'#FFC400','stroke-width':3,opacity:.5});}
  else src(this.bg.im,P(o.fondo));
  this.cab=el('div','abs',r,`<div style="font:800 60px Montserrat;color:#212529">${o.cab.tit}</div>`+(o.cab.sub?`<div style="font:500 28px 'Work Sans';color:rgba(33,37,41,.82);margin-top:8px;max-width:1500px">${o.cab.sub}</div>`:''));
  if(/_duoG$/.test(o.fondo||''))this.cab.querySelectorAll('div').forEach((q,i)=>q.style.color=i?'rgba(255,255,255,.85)':'#fff');
  Object.assign(this.cab.style,{left:'120px',top:'92px'});
  this.esc=el('div','abs',r);Object.assign(this.esc.style,{left:0,top:0,width:'1920px',height:'1080px',perspective:'1900px',perspectiveOrigin:'960px 560px'});
  const gap=40,w=Math.min(520,(1680-(n-1)*gap)/n),x0=(1920-(n*w+(n-1)*gap))/2,top=o.top||(o.cab.sub?350:320),h=o.alto||560;
  const fs=n>=4?44:54,fd=n>=4?29:33;
  this.cs=o.items.map((x,i)=>{const c=el('div','tarj',this.esc);Object.assign(c.style,{left:(x0+i*(w+gap))+'px',top:top+'px',width:w+'px',height:h+'px',padding:'40px 38px',transformOrigin:'50% 60%',overflow:'hidden'});
   c.innerHTML=`<div class="barra" style="position:absolute;left:0;top:0;height:12px;width:100%;background:${x.rojo===false?'#FFC400':'#DF1F15'};transform-origin:0 0"></div>`+
   (x.ico?`<svg width="112" height="112" viewBox="0 0 122 122"><path class="ico" d="${ICO[x.ico]||x.ico}" fill="none" stroke="#DF1F15" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/></svg>`:'')+
   (x.pre?`<div style="font:600 26px 'Work Sans';color:#6C757D;margin-top:10px">${x.pre}</div>`:'')+
   `<div style="font:800 ${fs}px/1.08 Montserrat;margin-top:12px">${x.tit}</div>`+
   (x.def?`<div style="font:500 ${fd}px/1.25 'Work Sans';margin-top:14px">${x.def}</div>`:'')+
   (x.ej?`<div class="ej" style="font:italic 400 ${n>=4?24:27}px/1.3 'Work Sans';color:#495057;margin-top:24px;padding-top:20px;border-top:2px solid #E9ECEF">${x.ej}</div>`:'');
   return {c,barra:c.querySelector('.barra'),ico:c.querySelector('.ico'),ej:c.querySelector('.ej'),en:T.k(x.en)};});
  this.k0=T.k(o.en0||0);
  if(o.banda){this.banda=el('div','abs',r,`<div style="background:#fff;border-radius:22px;padding:22px 34px;font:700 34px/1.25 Montserrat;color:#212529;box-shadow:0 20px 50px rgba(0,0,0,.22);max-width:1500px">${o.banda.html}</div>`);
   Object.assign(this.banda.style,{left:'120px',top:(top+h+36)+'px'});this.kb=T.k(o.banda.en);}},
 draw(t,r){const d=this.d;
  // entra empujando: el panel nuevo cruza desde la derecha sobre la toma anterior
  const pe=E.inOutExpo(R(t,0,22));r.style.transform=`translateX(${(1-pe)*1920}px)`;r.style.boxShadow=pe<1?'-40px 0 80px rgba(0,0,0,.35)':'none';
  kb(this.bg.im,lerp(1.2,1.1,E.outCubic(R(t,0,50)))+0.04*R(t,50,d),lerp(0,-40,R(t,0,d)),0);
  sube(this.cab,t,14,d-16,40,18);
  const cam=Math.sin(t/80)*2;
  const w=this.cs.map((o2,i)=>{const on=E.inOutCubic(R(t,o2.en,o2.en+22));const sig=this.cs[i+1];return on*(sig?1-E.inOutCubic(R(t,sig.en,sig.en+22)):1);});
  const A=Math.max(0,...w);
  this.cs.forEach((o2,i)=>{const e=E.outCubic(R(t,this.k0+10+i*7,this.k0+10+i*7+30));const wi=w[i],otro=(1-wi)*A;
   const ry=lerp(-40,0,e)+(i-(n-1)/2)*-6+cam;const z=lerp(-400,0,e)+wi*60-otro*40;
   o2.c.style.transform=`translate3d(0,${(1-e)*90}px,${z}px) rotateY(${ry}deg) scale(${1-otro*0.03})`;
   o2.c.style.opacity=e*(1-otro*0.35)*(1-R(t,d-14,d));o2.barra.style.transform=`scaleX(${wi})`;
   if(o2.ico){if(t<o2.en-2){trazo(o2.ico,0);}else trazo(o2.ico,E.inOutCubic(R(t,o2.en-2,o2.en+28)));}
   if(o2.ej)o2.ej.style.opacity=E.outCubic(R(t,o2.en+18,o2.en+34));
   o2.c.style.boxShadow=`0 ${24+20*wi}px ${60+30*wi}px rgba(0,0,0,${0.2+0.14*wi})`;});
  if(this.banda)sube(this.banda,t,this.kb,d-14,40,16);
 },subs:[[0,22]]};}

// escalera: la toma retrocede en 2.5D hasta quedar como tarjeta a la derecha y crece la escalera
function S_escalera(o){const T=blk(o.txt,o.cola);return {voz:T.voz,id:o.id,d:T.d,ov:o.ov!=null?o.ov:0,
 build(r){r.style.background='#F7F7F8';
  this.esc=el('div','abs',r);Object.assign(this.esc.style,{left:0,top:0,width:'1920px',height:'1080px',perspective:'1800px',perspectiveOrigin:'1500px 540px'});
  this.card=el('div','abs',this.esc);Object.assign(this.card.style,{left:0,top:0,width:'1920px',height:'1080px',overflow:'hidden',transformOrigin:'50% 50%'});
  this.im=el('img','',this.card);Object.assign(this.im.style,{width:'1920px',height:'1080px',objectFit:'cover'});
  if(o.rotulo){this.rot=el('div','abs',r,`<div style="font:600 26px 'Work Sans';color:#6C757D">${o.rotulo}</div>`);Object.assign(this.rot.style,{left:'130px',top:'110px'});}
  const s=sv('svg',r,{class:'ov',width:1920,height:1080});
  let fd='';const NI=o.items.length;for(let i=0;i<NI;i++){const x=76+i*40,y0=770-i*160+136,y1=770-i*160+20;fd+=(i?` L ${x} ${y0}`:`M ${x} ${y0+40}`)+` L ${x} ${y1}`+(i<NI-1?` L ${x+40} ${y1}`:'');}
  this.flecha=sv('path',s,{d:fd,fill:'none',stroke:'#DF1F15','stroke-width':6,'stroke-linecap':'round'});
  this.st=o.items.map((x,i)=>{const c=el('div','tarj',r);Object.assign(c.style,{left:(100+i*40)+'px',top:(770-i*160)+'px',width:'860px',height:'136px',padding:'20px 34px 0 46px',transformOrigin:'0 50%',boxShadow:'0 14px 34px rgba(0,0,0,.12)'});
   const ult=i===o.items.length-1&&o.ultimoRojo!==false;
   c.innerHTML=`<div class="b" style="position:absolute;left:0;top:0;bottom:0;width:12px;background:#CED4DA;border-radius:26px 0 0 26px"></div>
   <div style="display:flex;align-items:baseline;gap:20px;white-space:nowrap"><span style="font:800 42px Montserrat;color:${ult?'#DF1F15':'#212529'}">${x.tit}</span><span style="font:500 24px 'Work Sans';color:#495057">${x.def}</span></div>
   <div class="r" style="font:600 28px 'Work Sans';color:#212529;margin-top:10px">${x.resp}</div>`;
   return {c,b:c.querySelector('.b'),r:c.querySelector('.r'),en:T.k(x.en),re:T.k(x.re||x.en)+20,ult};});},
 draw(t,r){const d=this.d;src(this.im,o.clip?C(o.clip,Math.min(120,(o.desde||120))):P(o.placa));
  const p=E.inOutExpo(R(t,0,26));const tx=lerp(0,620,p),s=lerp(1,0.44,p),ry=lerp(0,-16,p);
  this.card.style.transform=`translate3d(${tx}px,${-20*p}px,0) rotateY(${ry+Math.sin(t/60)*1.2}deg) scale(${s})`;
  this.card.style.borderRadius=lerp(0,80,p)+'px';this.card.style.boxShadow=`0 40px 90px rgba(0,0,0,${0.25*p})`;
  this.im.style.transform=`scale(${1+0.06*R(t,0,d)})`;
  if(this.rot)sube(this.rot,t,20,d-14,30);
  this.st.forEach((o2,i)=>{const a=E.outExpo(R(t,o2.en-6,o2.en+16));o2.c.style.opacity=R(t,o2.en-6,o2.en)*(1-R(t,d-10,d));
   o2.c.style.transform=`translate(${-40*(1-a)}px,${30*(1-a)}px) scaleX(${0.6+0.4*a})`;
   o2.r.style.opacity=E.outCubic(R(t,o2.re,o2.re+12));const sig=this.st[i+1];
   o2.b.style.background=(t>=o2.en&&(!sig||t<sig.en))||o2.ult&&t>=o2.en?'#DF1F15':'#CED4DA';});
  trazo(this.flecha,this.st.reduce((acc,o2)=>acc+E.inOutCubic(R(t,o2.en-4,o2.en+18)),0)/this.st.length);this.flecha.style.opacity=1-R(t,d-10,d);
 },subs:[[0,26]]};}

// pantalla partida: base a cuadro completo, paneles que suben cuando la voz los nombra
// o={id,txt,entrada, base:{clip|placa, ventana}, panes:[{clip|placa, x,y,s, tit, sub, en}], cierre:[{html,en,top}]}
function S_partida(o){const T=blk(o.txt,o.cola);const n=o.panes.length,W=1920/n;return {voz:T.voz,id:o.id,d:T.d,ov:{tren:24,amarillo:18,iris:28,puertas:12,fundido:16}[o.entrada]||0,
 build(r){this.cont=el('div','sec',r);this.base=capa(this.cont);
  this.panes=o.panes.map((p,i)=>{const b=el('div','lay',this.cont);Object.assign(b.style,{left:(i*W)+'px',width:W+'px'});const im=el('img','',b);const im2=el('img','',b);im2.style.opacity=0;
   const g=el('div','lay',b);g.style.background='linear-gradient(0deg,rgba(15,18,22,.85) 0%,rgba(15,18,22,0) 45%)';
   const tx=el('div','abs',b,`<div style="font:800 40px Montserrat">${p.tit}</div><div style="font:500 28px/1.25 'Work Sans';opacity:.92;margin-top:6px">${p.sub}</div>`);Object.assign(tx.style,{left:'44px',bottom:'60px',right:'40px',color:'#fff'});
   if(i<n-1){const sep=el('div','abs',b);Object.assign(sep.style,{right:0,top:0,width:'6px',height:'1080px',background:'#fff'});}
   return {b,im,im2,tx,p,en:T.k(p.en)};});
  this.salen=T.k(o.salen||'fin');
  this.som=el('div','lay',this.cont);this.som.style.background='linear-gradient(0deg,rgba(15,18,22,.8) 0%,rgba(15,18,22,0) 50%)';
  this.ci=(o.cierre||[]).map(x=>{const e=el('div','abs',this.cont,x.html);Object.assign(e.style,{left:'120px',top:(x.top||800)+'px'});return {e,a:T.k(x.en),b:x.hasta?T.k(x.hasta)-10:1e9};});
  if(o.etiqueta!==false)this.e=etiqueta(this.cont);
  this.ent=entradaBuild(r,this.cont,o.entrada,o.entradaOpt);},
 draw(t){const d=this.d;this.ent.draw(t);const b=o.base;
  if(b.clip){const v=b.ventana||[0,120];clipF(this.base,b.clip,v[0]+t*velAuto(v,d));}else placa(this.base,b.placa);
  kb2(this.base,lerp(1.12,1.0,E.outCubic(R(t,0,this.panes[0].en)))+0.06*E.inOutCubic(R(t,this.salen,d)));
  this.base.im.style.filter=this.base.im2.style.filter=`brightness(${1-0.35*R(t,this.panes[0].en,this.panes[0].en+12)*(1-R(t,this.salen,this.salen+14))})`;
  this.panes.forEach((q,i)=>{const a=E.outExpo(R(t,q.en,q.en+20)),bb=E.inOutExpo(R(t,this.salen+i*4,this.salen+i*4+18));
   vis(q.b,a>0&&bb<1);q.b.style.clipPath=`inset(${(1-a)*100}% 0 ${bb*100}% 0)`;const u=t-q.en,p=q.p;
   if(p.clip){const v=p.ventana||[0,120];clipF({im:q.im,im2:q.im2},p.clip,v[0]+Math.max(0,u)*velAuto(v,this.salen-q.en+20));}else{src(q.im,P(p.placa));q.im2.style.opacity=0;}
   q.im2.style.transformOrigin=q.im.style.transformOrigin='0 0';q.im2.style.transform=q.im.style.transform=`translate(${(p.x||0)-12*u/100}px,${(p.y||0)+(1-a)*80}px) scale(${(p.s||1)*(1+0.04*u/200)})`;
   sube(q.tx,t,q.en+12,1e9,30,14);});
  this.som.style.opacity=Math.max(1-R(t,this.panes[0].en-8,this.panes[0].en),this.ci.length?R(t,this.salen-6,this.salen+6):0);
  this.ci.forEach(x=>sube(x.e,t,x.a,Math.min(x.b,d-14),50,16));
  if(this.e)etqDraw(this.e,t,d);
 },subs:[[0,24]]};}

// cita: tarjeta blanca grande con la cita y valores que aparecen como fichas
function S_cita(o){const T=blk(o.txt,o.cola);return {voz:T.voz,id:o.id,d:T.d,ov:16,
 build(r){this.bg=capa(r);src(this.bg.im,P(o.fondo));
  this.card=el('div','tarj',r,`<div style="font:600 28px 'Work Sans';color:#DF1F15">${o.fuente}</div><div style="font:800 54px/1.12 Montserrat;margin-top:16px">${o.tit}</div>`);
  Object.assign(this.card.style,{left:'120px',top:'150px',width:'1100px',padding:'48px 56px'});
  this.fichas=el('div','abs',r);Object.assign(this.fichas.style,{left:'120px',top:'560px',width:'1300px',display:'flex',flexWrap:'wrap',gap:'22px 22px'});
  this.ch=o.chips.map((x,i)=>{const c=el('div','pill',this.fichas,x.t);Object.assign(c.style,{position:'relative',background:'#fff',color:'#212529',boxShadow:'0 14px 34px rgba(0,0,0,.25)'});return {c,a:T.k(x.en)};});},
 draw(t,r){const d=this.d;r.style.opacity=E.inOutCubic(R(t,0,16));kb(this.bg.im,lerp(1.2,1.08,E.outCubic(R(t,0,60)))+0.04*R(t,60,d),lerp(-20,30,R(t,0,d)),0);
  sube(this.card,t,6,d-14,50,18);this.ch.forEach(x=>{const k=E.outBack(R(t,x.a,x.a+14),2);x.c.style.opacity=R(t,x.a,x.a+6)*(1-R(t,d-12,d));x.c.style.transform=`scale(${0.6+0.4*k})`;});
 },subs:[[0,16]]};}

// actividad: vagón amarillo con preguntas u opciones
function S_actividad(o){const T=blk(o.txt,o.cola);return {voz:T.voz,id:o.id||'ACT',d:T.d+(o.extra||80),ov:20,
 build(r){this.pan=el('div','abs',r);Object.assign(this.pan.style,{left:0,top:0,width:'2300px',height:'1080px',background:'#FFC400',borderRadius:'120px 0 0 120px'});
  el('div','abs',this.pan).style.cssText='left:0;right:0;top:960px;height:22px;background:#DF1F15';
  this.tit=el('div','abs',r,`<div style="font:800 72px Montserrat;color:#212529">${o.titulo}</div>`+(o.sub?`<div style="font:500 34px/1.3 'Work Sans';color:#212529;margin-top:10px;max-width:1500px">${o.sub}</div>`:''));Object.assign(this.tit.style,{left:'160px',top:'140px'});
  const y0=o.sub?(o.lineas.length>4?385:o.lineas.length>3?400:430):380,dy=o.lineas.length>4?104:o.lineas.length>3?120:140;
  this.q=o.lineas.map((x,i)=>{const c=el('div','abs',r);Object.assign(c.style,{left:'160px',top:(y0+i*dy)+'px',display:'flex',alignItems:'center',gap:'34px'});
   const n=el('div','',c,x.n||String(i+1));Object.assign(n.style,{width:'80px',height:'80px',borderRadius:'50%',background:'#DF1F15',color:'#fff',font:'800 42px Montserrat',display:'flex',alignItems:'center',justifyContent:'center',flex:'none'});
   const tt=el('div','',c,x.t);Object.assign(tt.style,{font:`700 ${o.lineas.length>3?48:54}px Montserrat`,color:'#212529',maxWidth:'1500px'});return {c,n,L:partir(tt,true),a:T.k(x.en)};});
  if(o.pie){this.pie=el('div','abs',r,`<div style="font:600 34px 'Work Sans';color:#212529">${o.pie.t}</div>`);Object.assign(this.pie.style,{left:'160px',top:'880px'});this.kp=T.k(o.pie.en);}},
 draw(t,r){const d=this.d;const e=E.inOutExpo(R(t,0,20));this.pan.style.transform=`translate(${lerp(1920,0,e)}px,0)`;
  sube(this.tit,t,14,1e9,40,18);
  this.q.forEach(o2=>{const k=E.outBack(R(t,o2.a,o2.a+12),2.2);o2.n.style.transform=`scale(${k})`;o2.c.style.opacity=t>=o2.a?1:0;letras(o2.L,t,o2.a+4,0.6,12);});
  if(this.pie)sube(this.pie,t,this.kp,1e9,30,14);r.style.opacity=1-R(t,d-8,d);
 },subs:[[0,20]]};}

// ruta: infografía de línea de metro vista desde arriba, como el intro. Las paradas son los temas
// del video; el tren va de una a otra y cada etiqueta entra cuando llega. modo 'agenda' (al
// comienzo) termina acercándose a la primera parada; 'repaso' (al final) recorre todas encendidas.
// o={id, titulo, paradas:[...], modo, entrada}
function S_ruta(o){const N=o.paradas.length,paso=o.paso||34,d=o.d||(46+N*paso+(o.modo==='agenda'?40:30));return {id:o.id||'RUTA',d,ov:{tren:24,puertas:20,fundido:16}[o.entrada||'tren'],
 build(r){this.cam=el('div','abs',r);Object.assign(this.cam.style,{left:0,top:0,width:'1920px',height:'1080px',transformOrigin:'960px 540px'});
  const s=sv('svg',this.cam,{class:'ov',width:1920,height:1080});sv('rect',s,{x:-3000,y:-3000,width:8000,height:8000,fill:'#F7F7F8'});
  // trama de calles, como el mapa del intro
  for(let i=0;i<22;i++){const x=-300+i*110+rnd(i)*40;sv('line',s,{x1:x,y1:-20,x2:x+260,y2:1100,stroke:'#E3E6EA','stroke-width':i%4?2:5});}
  for(let i=0;i<12;i++){const y=-40+i*100+rnd(i+9)*30;sv('line',s,{x1:-20,y1:y,x2:1940,y2:y-180,stroke:'#E3E6EA','stroke-width':i%3?2:5});}
  sv('path',s,{d:'M -40 1000 C 300 960, 520 1040, 820 990 S 1500 900, 1980 960 L 1980 1100 L -40 1100 Z',fill:'#E9F0E4',opacity:.8});
  // la línea y sus paradas
  const xs=Array.from({length:N},(_,i)=>N===1?960:360+i*(1200/(N-1)));const ys=xs.map((_,i)=>i%2?660:470);
  let dd=`M ${xs[0]-260} ${ys[0]+90} C ${xs[0]-140} ${ys[0]+40}, ${xs[0]-80} ${ys[0]}, ${xs[0]} ${ys[0]}`;
  for(let i=1;i<N;i++){const mx=(xs[i-1]+xs[i])/2;dd+=` C ${mx} ${ys[i-1]}, ${mx} ${ys[i]}, ${xs[i]} ${ys[i]}`;}
  dd+=` C ${xs[N-1]+80} ${ys[N-1]}, ${xs[N-1]+140} ${ys[N-1]-40}, ${xs[N-1]+260} ${ys[N-1]-90}`;
  this.via0=sv('path',s,{d:dd,fill:'none',stroke:'#CED4DA','stroke-width':22,'stroke-linecap':'round'});
  this.via=sv('path',s,{d:dd,fill:'none',stroke:'#DF1F15','stroke-width':12,'stroke-linecap':'round'});
  this.L=this.via.getTotalLength();
  // posición de cada parada sobre la vía
  this.sl=xs.map((x,i)=>{let best=0,bd=1e9;for(let l=0;l<=this.L;l+=4){const q=this.via.getPointAtLength(l);const dd2=(q.x-x)**2+(q.y-ys[i])**2;if(dd2<bd){bd=dd2;best=l;}}return best;});
  this.st=xs.map((x,i)=>{const g=sv('g',s,{transform:`translate(${x} ${ys[i]})`});const c=sv('circle',g,{r:0,fill:'#fff',stroke:'#DF1F15','stroke-width':9});const c2=sv('circle',g,{r:0,fill:'#DF1F15'});
   const lab=el('div','abs',this.cam,`<div style="display:flex;align-items:center;gap:16px;background:#fff;border-radius:40px;padding:14px 28px 14px 16px;box-shadow:0 16px 40px rgba(0,0,0,.14);white-space:nowrap"><span style="width:46px;height:46px;border-radius:50%;background:#FFC400;color:#212529;font:800 24px Montserrat;display:flex;align-items:center;justify-content:center">${i+1}</span><span style="font:700 32px Montserrat;color:#212529">${o.paradas[i]}</span></div>`);
   Object.assign(lab.style,{left:x+'px',top:(i%2?ys[i]+52:ys[i]-118)+'px',transform:'translateX(-50%)'});return {g,c,c2,lab,x,y:ys[i]};});
  // el tren: cápsula roja con ventanas, gira con la vía
  this.tren=sv('g',s,{});sv('rect',this.tren,{x:-74,y:-26,width:148,height:52,rx:26,fill:'#DF1F15',stroke:'#fff','stroke-width':5});
  for(let i=0;i<3;i++)sv('rect',this.tren,{x:-50+i*36,y:-12,width:24,height:24,rx:6,fill:'#fff'});
  this.cab=el('div','abs',r,`<div style="font:600 28px 'Work Sans';color:#DF1F15">${o.ante||''}</div><div style="font:800 58px Montserrat;color:#212529;margin-top:6px">${o.titulo}</div>`);Object.assign(this.cab.style,{left:'120px',top:'96px'});
  this.ent=entradaBuild(r,this.cam,o.entrada||'tren');},
 draw(t,r){const d=this.d;this.ent.draw(t);
  sube(this.cab,t,10,d-16,30,16);
  const tv=E.inOutCubic(R(t,6,40));trazo(this.via0,tv);trazo(this.via,tv*(o.modo==='repaso'?1:0)+(o.modo==='repaso'?0:0));
  // el tren avanza de parada en parada, frenando en cada una
  const t0=34;let pos=-1;
  for(let i=0;i<N;i++){const a=t0+i*paso;const k=E.inOutCubic(R(t,a,a+paso-8));const from=i===0?this.sl[0]-220:this.sl[i-1];if(t>=a)pos=from+(this.sl[i]-from)*k;}
  if(pos<0)pos=this.sl[0]-220;
  if(o.modo==='agenda')trazo(this.via,Math.max(0,pos)/this.L);else trazo(this.via,Math.max(0,pos)/this.L);
  const q=this.via.getPointAtLength(Math.max(0,pos)),q2=this.via.getPointAtLength(Math.min(this.L,Math.max(0,pos)+6));
  const ang=Math.atan2(q2.y-q.y,q2.x-q.x)*180/Math.PI;this.tren.setAttribute('transform',`translate(${q.x} ${q.y}) rotate(${ang})`);this.tren.style.opacity=R(t,30,36);
  this.st.forEach((p2,i)=>{const lleg=t0+i*paso+paso-8;const k=E.outBack(R(t,lleg-6,lleg+8),2.4);p2.c.setAttribute('r',4+18*E.outCubic(R(t,12+i*3,28+i*3)));p2.c2.setAttribute('r',10*k);
   const kl=E.outCubic(R(t,lleg,lleg+14));p2.lab.style.opacity=kl;p2.lab.style.transform=`translateX(-50%) translateY(${(i%2?-1:1)*-24*(1-kl)}px)`;});
  // cámara: acompaña al tren; en la agenda termina entrando a la primera parada
  const fx=lerp(0,(960-q.x)*0.06,R(t,30,60));let sc=lerp(1.08,1.0,E.outCubic(R(t,0,60)));let tx=fx,ty=0;
  if(o.modo==='agenda'){const z=E.inOutExpo(R(t,d-30,d));const p0=this.st[0];sc=sc*(1-z)+9*z;tx=lerp(fx,(960-p0.x)*9,z);ty=lerp(0,(540-p0.y)*9,z);}
  this.cam.style.transform=`translate(${tx}px,${ty}px) scale(${sc})`;
 },subs:[[0,24]].concat(o.modo==='agenda'?[[d-30,d]]:[])};}

// matriz: las tablas del documento como motion. Cabecera de columnas, filas que entran con la voz;
// la primera celda es la ficha de la fila, un trazo la une con las demás, que se revelan en `re`.
// o={id,txt,fondo:'blanco'|'<placa>_duoG'|'<placa>_duoY',cab:{tit,sub},cols:[..],anchos:[..],filas:[{c:[..],en,re,ico}],banda:{html,en},entrada}
function S_matriz(o){const T=blk(o.txt,o.cola);const n=o.filas.length,nc=o.cols.length;return {voz:T.voz,id:o.id,d:T.d,ov:{tren:24,amarillo:18,fundido:16,puertas:12}[o.entrada||'tren']||0,
 build(r){this.cont=el('div','sec',r);const osc=/_duoG$/.test(o.fondo||'');
  if(!o.fondo||o.fondo==='blanco'){this.cont.style.background='#F4F5F7';const g=sv('svg',this.cont,{class:'ov',width:1920,height:1080});
   for(let i=0;i<16;i++)sv('line',g,{x1:-200+i*160,y1:0,x2:-200+i*160+560,y2:1080,stroke:'#E6E8EC','stroke-width':2});
   sv('circle',g,{cx:1720,cy:150,r:240,fill:'none',stroke:'#FFC400','stroke-width':3,opacity:.5});}
  else{this.bg=capa(this.cont);src(this.bg.im,P(o.fondo));}
  this.cab=el('div','abs',this.cont,`<div style="font:800 58px Montserrat;color:${osc?'#fff':'#212529'}">${o.cab.tit}</div>`+(o.cab.sub?`<div style="font:500 28px 'Work Sans';color:${osc?'rgba(255,255,255,.85)':'#495057'};margin-top:8px;max-width:1500px">${o.cab.sub}</div>`:''));
  Object.assign(this.cab.style,{left:'120px',top:'84px'});
  const X0=120,W=1680,top=o.top||(o.cab.sub?268:236),hc=56,gap=16,alto=(o.banda?700:800)-top+ (o.cab.sub?0:0),h=Math.min(o.altoFila||150,Math.floor((1010-(o.banda?110:0)-top-hc-gap*(n))/n));
  const an=o.anchos||o.cols.map(()=>1),sa=an.reduce((a,b)=>a+b,0);const cw=an.map(a=>(W-(nc-1)*gap)*a/sa);const cx=cw.map((_,i)=>X0+cw.slice(0,i).reduce((a,b)=>a+b+gap,0));
  this.hd=o.cols.map((c,i)=>{const e=el('div','abs',this.cont,`<div style="font:700 24px 'Work Sans';letter-spacing:.02em;color:${osc?'#FFC400':'#DF1F15'}">${c}</div>`);Object.assign(e.style,{left:(cx[i]+(i?26:30))+'px',top:top+'px'});return e;});
  const s=sv('svg',this.cont,{class:'ov',width:1920,height:1080});
  this.fs=o.filas.map((f,j)=>{const y=top+hc+j*(h+gap);
   const cel=f.c.map((t,i)=>{const e=el('div','abs',this.cont);Object.assign(e.style,{left:cx[i]+'px',top:y+'px',width:cw[i]+'px',height:h+'px',borderRadius:'22px',background:i===0?'#fff':'rgba(255,255,255,.94)',boxShadow:'0 14px 34px rgba(0,0,0,.12)',display:'flex',alignItems:'center',overflow:'hidden',transformOrigin:'0 50%'});
    e.innerHTML=(i===0?`<div class="b" style="position:absolute;left:0;top:0;bottom:0;width:12px;background:#CED4DA"></div>`+(f.ico?`<svg width="64" height="64" viewBox="0 0 122 122" style="flex:none;margin-left:34px"><path class="ico" d="${ICO[f.ico]||f.ico}" fill="none" stroke="#DF1F15" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/></svg>`:''):'')+
     `<div style="padding:0 26px 0 ${i===0?(f.ico?22:36):28}px;font:${i===0?'800':'500'} ${i===0?(o.fs0||38):(o.fs||33)}px/1.2 ${i===0?'Montserrat':"'Work Sans'"};color:#212529">${t}</div>`;return e;});
   const li=cel.slice(1).map((_,i)=>sv('path',s,{d:`M ${cx[i]+cw[i]-4} ${y+h/2} L ${cx[i+1]+4} ${y+h/2}`,stroke:'#DF1F15','stroke-width':5,'stroke-linecap':'round',fill:'none'}));
   const en=T.k(f.en),re=f.re!=null?[].concat(f.re).map(x=>T.k(x)):[en+18];
   return {cel,li,en,re,b:cel[0].querySelector('.b'),ico:cel[0].querySelector('.ico')};});
  if(o.banda){this.banda=el('div','abs',this.cont,`<div style="background:#FFC400;border-radius:22px;padding:20px 34px;font:700 34px/1.25 Montserrat;color:#212529;box-shadow:0 20px 50px rgba(0,0,0,.2);max-width:1600px">${o.banda.html}</div>`);
   Object.assign(this.banda.style,{left:'120px',top:(top+hc+n*(h+gap)+10)+'px'});this.kb=T.k(o.banda.en);}
  this.ent=entradaBuild(r,this.cont,o.entrada||'tren');},
 draw(t,r){const d=this.d;this.ent.draw(t);
  if(this.bg)kb(this.bg.im,lerp(1.16,1.08,E.outCubic(R(t,0,60)))+0.04*R(t,60,d),lerp(0,-30,R(t,0,d)),0);
  sube(this.cab,t,10,d-16,40,18);
  this.hd.forEach((e,i)=>sube(e,t,this.fs[0].en-10+i*4,d-14,20,14));
  let act=-1;this.fs.forEach((f,j)=>{if(t>=f.en)act=j;});
  this.fs.forEach((f,j)=>{const on=j===act,sal=1-R(t,d-12,d);
   f.cel.forEach((e,i)=>{const a=i===0?f.en:(f.re[Math.min(i-1,f.re.length-1)]);const k=E.outExpo(R(t,a-4,a+18));
    e.style.opacity=R(t,a-4,a+2)*(on||t<f.en?1:0.62)*sal;e.style.transform=`translate(${-50*(1-k)}px,0) scaleX(${0.7+0.3*k})`;
    if(i>0)trazo(f.li[i-1],E.inOutCubic(R(t,a-12,a+2)));});
   f.li.forEach(l=>l.style.opacity=(on?1:0.35)*sal);
   f.b.style.background=on?'#DF1F15':'#CED4DA';if(f.ico)trazo(f.ico,E.inOutCubic(R(t,f.en,f.en+26)));});
  if(this.banda)sube(this.banda,t,this.kb,d-14,40,16);
 },subs:[[0,24]]};}

// red: mapa de actores. Nodos que aparecen con la voz y enlaces que se dibujan; por los enlaces con
// `flujo` circulan fichas (lo que va de un actor a otro). o={id,txt,cab,nodos:[{id,x,y,tit,sub,ico,en,alerta}],
// enlaces:[{a,b,en,color,rot,flujo,curva,punteado,hasta}],notas:[{html,en,x,y}],entrada}
function S_red(o){const T=blk(o.txt,o.cola);return {voz:T.voz,id:o.id,d:T.d,ov:{tren:24,amarillo:18,fundido:16,puertas:12}[o.entrada||'tren']||0,
 build(r){this.cont=el('div','sec',r);this.cont.style.background='#F7F7F8';this.cam=el('div','abs',this.cont);Object.assign(this.cam.style,{left:0,top:0,width:'1920px',height:'1080px',transformOrigin:'960px 560px'});
  const s=sv('svg',this.cam,{class:'ov',width:1920,height:1080});
  for(let i=0;i<22;i++){const x=-300+i*110+rnd(i)*40;sv('line',s,{x1:x,y1:-20,x2:x+260,y2:1100,stroke:'#E9EBEF','stroke-width':i%4?2:4});}
  for(let i=0;i<12;i++){const y=-40+i*100+rnd(i+9)*30;sv('line',s,{x1:-20,y1:y,x2:1940,y2:y-180,stroke:'#E9EBEF','stroke-width':i%3?2:4});}
  const N={};o.nodos.forEach(n=>N[n.id]=n);
  this.en=o.enlaces.map(e=>{const a=N[e.a],b=N[e.b],mx=(a.x+b.x)/2,my=(a.y+b.y)/2,dx=b.x-a.x,dy=b.y-a.y,L=Math.hypot(dx,dy),c=e.curva||0,qx=mx-dy/L*c,qy=my+dx/L*c;
   const dd=`M ${a.x} ${a.y} Q ${qx} ${qy} ${b.x} ${b.y}`;const base=sv('path',s,{d:dd,fill:'none',stroke:'#D5D9DF','stroke-width':16,'stroke-linecap':'round'});
   const p=sv('path',s,{d:dd,fill:'none',stroke:e.color||'#DF1F15','stroke-width':8,'stroke-linecap':'round'});
   const dots=e.flujo?[0,1,2].map(()=>sv('rect',s,{x:-15,y:-11,width:30,height:22,rx:5,fill:'#fff',stroke:e.color||'#DF1F15','stroke-width':5})):[];
   let lab=null;if(e.rot){lab=el('div','abs',this.cam,`<div style="background:#fff;border:3px solid ${e.color||'#DF1F15'};border-radius:30px;padding:10px 22px;font:700 26px Montserrat;color:#212529;white-space:nowrap;box-shadow:0 12px 30px rgba(0,0,0,.12)">${e.rot}</div>`);
    const q=p.getPointAtLength(p.getTotalLength()*(e.rotEn||0.5));Object.assign(lab.style,{left:q.x+'px',top:q.y+'px'});}
   return {e,base,p,dots,lab,a:T.k(e.en),h:e.hasta?T.k(e.hasta):1e9,L:p.getTotalLength()};});
  this.nd=o.nodos.map(n=>{const g=el('div','abs',this.cam);Object.assign(g.style,{left:n.x+'px',top:n.y+'px'});
   g.innerHTML=`<div class="aro" style="position:absolute;left:0;top:0;width:${n.r*2||190}px;height:${n.r*2||190}px;margin:-${n.r||95}px 0 0 -${n.r||95}px;border-radius:50%;border:6px solid #DF1F15;opacity:0"></div>
   <div class="c" style="position:relative;transform:translate(-50%,-50%);background:#fff;border-radius:34px;padding:22px 34px 22px 26px;display:flex;align-items:center;gap:20px;box-shadow:0 22px 54px rgba(0,0,0,.16);border-top:10px solid ${n.color||'#DF1F15'};white-space:nowrap">
   ${n.ico?`<svg width="76" height="76" viewBox="0 0 122 122"><path class="ico" d="${ICO[n.ico]||n.ico}" fill="none" stroke="${n.color==='#FFC400'?'#212529':'#DF1F15'}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/></svg>`:''}
   <div><div style="font:800 40px Montserrat;color:#212529">${n.tit}</div>${n.sub?`<div style="font:500 26px 'Work Sans';color:#495057;margin-top:4px">${n.sub}</div>`:''}</div></div>`;
   return {n,g,c:g.querySelector('.c'),aro:g.querySelector('.aro'),ico:g.querySelector('.ico'),a:T.k(n.en),al:n.alerta?T.k(n.alerta):1e9};});
  this.nt=(o.notas||[]).map(x=>{const e=el('div','abs',this.cam,x.html);Object.assign(e.style,{left:x.x+'px',top:x.y+'px'});return {e,a:T.k(x.en),b:x.hasta?T.k(x.hasta)-8:1e9};});
  this.cab=el('div','abs',this.cont,`<div style="font:600 28px 'Work Sans';color:#DF1F15">${o.cab.ante||''}</div><div style="font:800 58px Montserrat;color:#212529;margin-top:6px">${o.cab.tit}</div>`);Object.assign(this.cab.style,{left:'120px',top:'84px'});
  this.ent=entradaBuild(r,this.cont,o.entrada||'tren');},
 draw(t,r){const d=this.d;this.ent.draw(t);sube(this.cab,t,10,d-16,30,16);
  this.cam.style.transform=`scale(${lerp(1.07,1.0,E.outCubic(R(t,0,d)))}) translate(${Math.sin(t/90)*6}px,0)`;
  this.en.forEach((x,j)=>{const k=E.inOutCubic(R(t,x.a,x.a+22)),f=1-R(t,x.h,x.h+14);trazo(x.base,k);trazo(x.p,k);x.base.style.opacity=k>0?f:0;x.p.style.opacity=k>0?f:0;
   if(x.e.punteado){x.p.style.strokeDasharray='';x.p.setAttribute('stroke-dasharray','2 22');x.p.style.opacity=R(t,x.a,x.a+10)*f;x.base.style.opacity=0;}
   x.dots.forEach((q,i)=>{const u=((t-x.a-22)/52+i/3)%1,vis2=t>x.a+22?1:0;const pt=x.p.getPointAtLength(x.L*Math.max(0,u));q.setAttribute('transform',`translate(${pt.x} ${pt.y})`);q.style.opacity=vis2*f*Math.min(1,u*8,(1-u)*8);});
   if(x.lab){const kl=E.outBack(R(t,x.a+12,x.a+26),1.8);x.lab.style.opacity=R(t,x.a+12,x.a+18)*f;x.lab.style.transform=`translate(-50%,-50%) scale(${0.6+0.4*kl})`;}});
  this.nd.forEach(x=>{const k=E.outBack(R(t,x.a,x.a+16),1.6);x.g.style.opacity=R(t,x.a,x.a+6)*(1-R(t,d-10,d));x.c.style.transform=`translate(-50%,-50%) scale(${0.5+0.5*k})`;
   if(x.ico)trazo(x.ico,E.inOutCubic(R(t,x.a+4,x.a+30)));
   const u=t>=x.al?((t-x.al)%40)/40:0;x.aro.style.opacity=t>=x.al?(1-u)*0.8:0;x.aro.style.transform=`scale(${1+u*0.9})`;});
  this.nt.forEach(x=>sube(x.e,t,x.a,Math.min(x.b,d-14),30,14));
 },subs:[[0,24]]};}

// mapa del módulo, general: un centro, acciones arriba y ramas abajo. o={txt,titulo,centro,arriba:[[texto,clave]],abajo:[[tit,sub,clave]],X}
function S_mapaMod(o){const T=blk(o.txt,o.cola);return {voz:T.voz,id:o.id||'MAPA',d:T.d,ov:16,
 build(r){r.style.background='#F7F7F8';this.cam=el('div','abs',r);Object.assign(this.cam.style,{left:0,top:0,width:'1920px',height:'1080px',transformOrigin:'960px 520px'});
  this.cab=el('div','abs',this.cam,`<div style="font:600 28px 'Work Sans';color:#6C757D">${o.titulo}</div>`);Object.assign(this.cab.style,{left:'120px',top:'70px'});
  const s=sv('svg',this.cam,{class:'ov',width:1920,height:1080});const C0={x:960,y:520};
  this.cen=el('div','abs',this.cam,`<div style="background:#DF1F15;color:#fff;border-radius:34px;padding:30px 46px;font:800 46px/1.1 Montserrat;text-align:center;box-shadow:0 24px 60px rgba(223,31,21,.35);white-space:nowrap">${o.centro}</div>`);
  Object.assign(this.cen.style,{left:C0.x+'px',top:C0.y+'px'});const X=o.X||[380,960,1540];this.n=[];
  (o.arriba||[]).forEach((a,i)=>{const p={x:X[i],y:230};const l=sv('path',s,{d:`M ${C0.x} ${C0.y-70} C ${C0.x} ${C0.y-170}, ${p.x} ${p.y+150}, ${p.x} ${p.y+50}`,fill:'none',stroke:'#CED4DA','stroke-width':5,'stroke-linecap':'round'});
   const e=el('div','abs',this.cam,`<div style="background:#fff;border:3px solid #DF1F15;border-radius:28px;padding:18px 30px;font:700 32px/1.15 Montserrat;color:#212529;text-align:center;box-shadow:0 14px 34px rgba(0,0,0,.1)">${a[0]}</div>`);
   Object.assign(e.style,{left:p.x+'px',top:p.y+'px'});this.n.push({e,l,a:T.k(a[1])});});
  (o.abajo||[]).forEach((a,i)=>{const p={x:X[i],y:840};const l=sv('path',s,{d:`M ${C0.x} ${C0.y+70} C ${C0.x} ${C0.y+170}, ${p.x} ${p.y-170}, ${p.x} ${p.y-70}`,fill:'none',stroke:'#CED4DA','stroke-width':5,'stroke-linecap':'round'});
   const e=el('div','abs',this.cam,`<div style="background:#fff;border-radius:28px;padding:24px 34px;text-align:center;box-shadow:0 18px 40px rgba(0,0,0,.12);border-top:12px solid #FFC400"><div style="font:800 38px Montserrat;color:#212529;white-space:nowrap">${a[0]}</div><div style="font:500 26px/1.2 'Work Sans';color:#495057;margin-top:6px">${a[1]}</div></div>`);
   Object.assign(e.style,{left:p.x+'px',top:p.y+'px'});this.n.push({e,l,a:T.k(a[2])});});},
 draw(t,r){const d=this.d;r.style.opacity=E.inOutCubic(R(t,0,16));this.cam.style.transform=`scale(${lerp(1.06,1.0,E.outCubic(R(t,0,d)))})`;
  sube(this.cab,t,6,1e9,20,14);const k=E.outBack(R(t,6,24),1.6);this.cen.style.transform=`translate(-50%,-50%) scale(${0.5+0.5*k})`;this.cen.style.opacity=R(t,6,12);
  let act=-1;this.n.forEach((n,i)=>{if(t>=n.a)act=i;});
  this.n.forEach((n,i)=>{trazo(n.l,E.inOutCubic(R(t,n.a-8,n.a+12)));const kk=E.outCubic(R(t,n.a,n.a+16));const on=i===act;
   n.l.setAttribute('stroke',t>=n.a?(on?'#DF1F15':'#ADB5BD'):'#CED4DA');n.e.style.opacity=R(t,n.a,n.a+6);n.e.style.transform=`translate(-50%,-50%) scale(${(0.6+0.4*kk)*(on?1.06:1)})`;});
  r.style.filter=`opacity(${1-R(t,d-10,d)})`;},subs:[[0,16]]};}

// ── línea de tiempo ──
function montar(S){
 let ini=0;S.forEach((s,i)=>{s.ini=i===0?0:ini;ini=s.ini+s.d;});
 S.forEach((s,i)=>{s.desde=s.ini-(s.ov||0);s.hasta=s.ini+s.d+(S[i+1]?(S[i+1].ov||0):0);});
 const N=ini,subs=new Array(N).fill(1);
 S.forEach(s=>(s.subs||[]).forEach(([a,b])=>{for(let f=s.ini+a-(s.ov||0);f<s.ini+b&&f<N;f++)if(f>=0)subs[f]=2;}));
 const raiz=document.getElementById('raiz'),grano=[];
 window.ESCENA={cuadros:N,subs,
  async init(){S.forEach(s=>{s.r=el('div','sec',raiz);s.build(s.r);s.r.style.display='none';});
   for(let i=0;i<6;i++){const c=document.createElement('canvas');c.width=960;c.height=540;const g=c.getContext('2d'),im=g.createImageData(960,540);
    for(let j=0;j<im.data.length;j+=4){const v=rnd(j*0.37+i*13.1)*255;im.data[j]=im.data[j+1]=im.data[j+2]=v;im.data[j+3]=255;}g.putImageData(im,0,0);grano.push(c);}
   await document.fonts.ready;return true;},
  async render(f){pend=[];for(const s of S){const on=f>=s.desde&&f<s.hasta;s.r.style.display=on?'':'none';if(on)s.draw(f-s.ini,s.r);}
   document.getElementById('grano').getContext('2d').drawImage(grano[Math.floor(f)%6],0,0);await Promise.all(pend);return true;},
  tabla(){return S.map(s=>[s.id,s.ini,s.d]);},
  voz(){return S.filter(s=>s.voz).map(s=>[s.voz.i,s.ini+s.voz.off]);}};
 window.__listo=true;
}
