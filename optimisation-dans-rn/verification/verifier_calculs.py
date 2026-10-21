from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
C=Path(__file__).resolve().parents[1];checks=[]
def check(n,x):
 assert x,n
 checks.append(n)
def clean(a):return {k:Q(v) for k,v in a.items() if v}
def plus(a,b):
 d=a.copy()
 for k,v in b.items():d[k]=d.get(k,0)+v
 return clean(d)
def times(a,b):
 d={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():d[i+k,j+l]=d.get((i+k,j+l),0)+v*w
 return clean(d)
def scale(a,k):return clean({i:v*k for i,v in a.items()})
def deriv(a,j):
 d={}
 for e,v in a.items():
  if e[j]:
   f=list(e);f[j]-=1;d[tuple(f)]=v*e[j]
 return clean(d)
def val(a,x,y):return sum(v*x**i*y**j for (i,j),v in a.items())

def grad(f,a,b):return [val(deriv(f,i),a,b) for i in range(2)]
def hess(f,a,b):return [[val(deriv(deriv(f,j),i),a,b) for j in range(2)]for i in range(2)]
def mm(A,B):return [[sum(Q(u)*Q(v) for u,v in zip(row,col))for col in zip(*B)]for row in A]
x={(1,0):Q(1)};y={(0,1):Q(1)}
f1={(1,0):Q(2),(0,1):Q(1)};f2={(1,0):Q(1),(0,1):Q(1),(0,2):Q(1)}
J=[grad(f1,0,0),grad(f2,0,0)];inverse=[[1,-1],[-1,2]]
check('Jacobienne de l’exemple d’inversion par dérivation',J==[[2,1],[1,1]])
check('Inverse exacte des deux côtés',mm(J,inverse)==mm(inverse,J)==[[1,0],[0,1]])
ellipse={(2,0):Q(1),(0,2):Q(2),(0,0):Q(-6)}
check('Point de l’ellipse et régularité',val(ellipse,2,1)==0 and grad(ellipse,2,1)==[4,4])
check('Dérivée implicite exacte',-grad(ellipse,2,1)[0]/grad(ellipse,2,1)[1]==-1)
check('Tangente de l’ellipse',4*1+4*(-1)==0)
bowl={(2,0):Q(1),(1,0):Q(2),(0,2):Q(3),(0,1):Q(-12),(0,0):Q(13)}
check('Bol : gradient au minimiseur',grad(bowl,-1,2)==[0,0])
check('Bol : Hessienne et valeur minimale',hess(bowl,-1,2)==[[2,0],[0,6]] and val(bowl,-1,2)==0)
x1=plus(x,{(0,0):1});y2=plus(y,{(0,0):-2})
check('Bol : identité globale en sommes de carrés',plus(times(x1,x1),scale(times(y2,y2),3))==bowl)
saddle={(2,0):Q(1),(0,2):Q(-2)}
check('Selle : gradient et Hessienne',grad(saddle,0,0)==[0,0] and hess(saddle,0,0)==[[2,0],[0,-4]])
check('Selle : signes opposés sur axes',val(saddle,Q(1,10),0)>0 and val(saddle,0,Q(1,10))<0)
for sign in (1,-1):
 quartic={(4,0):Q(sign),(0,4):Q(sign)}
 check('Quartique de signe '+str(sign)+' : second ordre nul',grad(quartic,0,0)==[0,0] and hess(quartic,0,0)==[[0,0],[0,0]])
quartic={(4,0):Q(1),(0,4):Q(-1)}
check('Quartique selle : second ordre nul et signes',hess(quartic,0,0)==[[0,0],[0,0]] and val(quartic,1,0)>0 and val(quartic,0,1)<0)
obj={(2,0):Q(1),(0,2):Q(1)};constraint={(1,0):Q(1),(0,1):Q(1),(0,0):Q(-2)}
check('Égalité : admissibilité',val(constraint,1,1)==0)
check('Lagrange : signe moins et lambda=2',[u-2*v for u,v in zip(grad(obj,1,1),grad(constraint,1,1))]==[0,0])
# Sur y=2-x, l’écart à la valeur minimale est 2(x-1)^2.
substituted={(2,0):Q(2),(1,0):Q(-4),(0,0):Q(2)}
check('Égalité : écart global exact',scale(times(plus(x,{(0,0):-1}),plus(x,{(0,0):-1})),2)==substituted)
for point,lam in [((1,0),Q(1,2)),((-1,0),Q(-1,2))]:
 xx,yy=point
 check('Cercle : candidat '+str(point),xx*xx+yy*yy==1 and [1-2*lam*xx,-2*lam*yy]==[0,0])
active={(2,0):Q(1),(1,0):Q(-4),(0,0):Q(4),(0,2):Q(1)}
check('Inégalité active : gradient',grad(active,0,0)==[-4,0])
check('Inégalité active : stationnarité et signe',[grad(active,0,0)[0]+4,grad(active,0,0)[1]]==[0,0] and 4>=0)
check('Inégalité active : écart x²-4x+y²',plus(active,{(0,0):-4})=={(2,0):1,(1,0):-4,(0,2):1})
inactive={(2,0):Q(1),(1,0):Q(2),(0,0):Q(1),(0,2):Q(1)}
check('Inégalité inactive : admissibilité stricte et gradient',-1-1<0 and grad(inactive,-1,0)==[0,0])
check('Contrainte active avec mu=0',grad(obj,0,0)==[0,0])
# Bloc quadratique : Q=2I, A=(1 1), b=2, c=0, x=(1;1), lambda=2.
block=[[2,0,-1],[0,2,-1],[1,1,0]]
check('Signe du bloc quadratique et solution',mm(block,[[1],[1],[2]])==[[0],[0],[2]])
for r in json.loads((C/'references/manifest.json').read_text(encoding='utf-8')):
 check('Intégrité '+r['file'],hashlib.sha256((C/'references'/r['file']).read_bytes()).hexdigest()==r['sha256'])
(C/'verification/calculs.json').write_text(json.dumps({'status':'passed','count':len(checks),'method':'Fractions exactes, dérivations de polynômes, produits matriciels et identités en sommes de carrés.','checks':checks,'limit':'Exemples recalculés ; les théorèmes sont relus avec leurs hypothèses, sans preuve formelle.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(checks),'contrôles exacts réussis.')
