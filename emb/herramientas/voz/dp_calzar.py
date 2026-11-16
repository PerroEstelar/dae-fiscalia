import json,re,subprocess,sys
wav,bl,out=sys.argv[1:4]
B=json.load(open(bl));L=[len(b) for b in B];N=len(B)
o=subprocess.run(['ffmpeg','-hide_banner','-i',wav,'-af','silencedetect=noise=-34dB:d=0.30','-f','null','-'],capture_output=True,text=True).stderr
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',wav],capture_output=True,text=True).stdout)
ss=[float(x) for x in re.findall(r'silence_start: ([0-9.]+)',o)];se=[float(x) for x in re.findall(r'silence_end: ([0-9.]+)',o)]
sil=list(zip(ss,se))
# habla = tramos con voz
h=[];t=0
for a,b in sil:
    h.append((t,a));t=b
h.append((t,dur));h=[x for x in h if x[1]-x[0]>0.05]
# candidatos: frontera = hueco entre h[i] y h[i+1]
G=[(h[i][1],h[i+1][0]) for i in range(len(h)-1)]
cum=[0];
for x in h: cum.append(cum[-1]+x[1]-x[0])   # habla acumulada hasta fin de tramo i
S=cum[-1];C=sum(L);k=S/C
# tiempo hablado de bloque j..: cum entre fronteras (tramo index)
M=len(h)
INF=1e18
# dp[j][i]: bloques 0..j-1 cubren tramos 0..i-1 (i = nº de tramos usados)
dp=[[INF]*(M+1) for _ in range(N+1)];pr=[[0]*(M+1) for _ in range(N+1)];dp[0][0]=0
for j in range(1,N+1):
    for i in range(j,M+1):
        for p in range(j-1,i):
            if dp[j-1][p]>=INF: continue
            sp=cum[i]-cum[p]
            if j==N and i!=M: continue
            e=(sp-L[j-1]*k)/(L[j-1]**0.5*k)
            # premio por pausa larga en la frontera p
            pausa=(h[p][0]-h[p-1][1]) if p>0 else 1
            c=dp[j-1][p]+e*e-0.8*min(pausa,1.5)
            if c<dp[j][i]:dp[j][i]=c;pr[j][i]=p
i=M;cuts=[]
for j in range(N,0,-1):
    p=pr[j][i];cuts.append((p,i));i=p
cuts.reverse()
res=[]
for j,(p,i) in enumerate(cuts):
    a,b=h[p][0],h[i-1][1];res.append((a,b))
    print(j,round(a,2),round(b,2),L[j],round((cum[i]-cum[p])/L[j]/k,2))
json.dump({'dur':dur,'bloques':[{'ini':a,'fin':b} for a,b in res]},open(out,'w'))
