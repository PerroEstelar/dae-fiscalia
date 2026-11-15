// core.js — línea de tiempo determinista para render cuadro a cuadro (sin transiciones CSS).
const FPS = 24000/1001;
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const R=(f,a,b)=>clamp((f-a)/(b-a));                 // 0..1 entre cuadros a y b
const E={
  lin:t=>t,
  outCubic:t=>1-Math.pow(1-t,3),
  inOutCubic:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2,
  outExpo:t=>t===1?1:1-Math.pow(2,-10*t),
  inExpo:t=>t===0?0:Math.pow(2,10*t-10),
  inOutExpo:t=>t===0?0:t===1?1:t<.5?Math.pow(2,20*t-10)/2:(2-Math.pow(2,-20*t+10))/2,
  outBack:(t,s=1.7)=>1+(s+1)*Math.pow(t-1,3)+s*Math.pow(t-1,2),
  outQuint:t=>1-Math.pow(1-t,5),
};
const lerp=(a,b,t)=>a+(b-a)*t;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
// parte un texto en letras (envueltas en máscara) para tipografía cinética
function partir(el, porPalabra=false){
  const txt=el.textContent; el.textContent='';
  const unidades = porPalabra ? txt.split(/(\s+)/) : [...txt];
  return unidades.map(u=>{
    if(/^\s+$/.test(u)){el.appendChild(document.createTextNode(u));return null;}
    const m=document.createElement('span');m.className='mask';
    const s=document.createElement('span');s.className='u';s.textContent=u;
    m.appendChild(s);el.appendChild(m);return s;
  }).filter(Boolean);
}
// trazo que se dibuja (trim path)
function trazo(path,t,desde=0){
  const L=path.__L||(path.__L=path.getTotalLength());
  path.style.strokeDasharray=`${L} ${L}`;
  path.style.strokeDashoffset=L*(1-t)+L*desde;
}
// trazo visible solo entre las fracciones a y b del recorrido
function trazoRango(path,a,b){
  const L=path.__L||(path.__L=path.getTotalLength());
  path.style.strokeDasharray=`0 ${a*L} ${Math.max(0,(b-a)*L)} ${L*2}`;
  path.style.strokeDashoffset=0;
}
// ruido determinista
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
window.__listo=true;
