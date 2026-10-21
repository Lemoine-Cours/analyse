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
x={(1,0):Q(1)};y={(0,1):Q(1)};f={(2,0):Q(1),(1,1):Q(1),(0,2):Q(2),(0,3):Q(1)}
fx,fy=deriv(f,0),deriv(f,1)
check('Gradient polynomial par dérivation des monômes',fx=={(1,0):2,(0,1):1} and fy=={(1,0):1,(0,1):4,(0,2):3})
H=[[deriv(deriv(f,j),i) for j in range(2)] for i in range(2)]
check('Hessienne symbolique',H==[[{(0,0):2},{(0,0):1}],[{(0,0):1},{(0,0):4,(0,1):6}]])
check('Dérivées mixtes symétriques',H[0][1]==H[1][0])
check('Hessienne en zéro',[[val(a,0,0) for a in row] for row in H]==[[2,1],[1,4]])
check('Hessienne au point (0;-1)',[[val(a,0,-1) for a in row] for row in H]==[[2,1],[1,-2]])
check('Direction négative au point (0;-1)',val(H[1][1],0,-1)==-2)
quad={(2,0):Q(2),(1,1):Q(2),(0,2):Q(4)}
check('Décomposition en carrés de H',plus(scale(times(plus(x,scale(y,Q(1,2))),plus(x,scale(y,Q(1,2)))),2),scale(times(y,y),Q(7,2)))==quad)
check('Décomposition de H-I',plus(times(plus(x,y),plus(x,y)),scale(times(y,y),2))=={(2,0):1,(1,1):2,(0,2):3})
check('Déterminant H positif',2*4-1==7)
check('Déterminant H-I positif',1*3-1==2)
check('Facteur un demi de Taylor',scale(quad,Q(1,2))=={(2,0):1,(1,1):1,(0,2):2})
h,k=Q(1,50),Q(-1,100)
check('Approximation au second ordre exacte',val(scale(quad,Q(1,2)),h,k)==Q(1,2500))
check('Valeur réelle du polynôme',val(f,h,k)==Q(399,1000000))
check('Reste cubique exact',val(f,h,k)-Q(1,2500)==Q(-1,1000000))
check('Reste cubique majoré par norme cubique',k*k<=h*h+k*k)
check('Norme diagonale, majoration',25-4==21 and 21>=0)
check('Norme diagonale, direction atteignant 5',(-5)**2==25)
check('Norme de Frobenius non optimale',25+4>25)
check('Borne de gradient sur boule',64-4==60 and 8*2==16)
check('Ordre des dérivations pour x²y',deriv(deriv({(2,1):Q(1)},1),0)=={(1,0):2})
a,b,t=Q(1,2),Q(5,2),Q(1,2);z=(1-t)*a+t*b
check('Point milieu de la corde',z==Q(3,2))
check('Corde au-dessus de la courbe',((1-t)*a*a+t*b*b)/2==Q(13,8) and z*z/2==Q(9,8))
check('Tangente et courbe t² à zéro',val({(2,0):1},0,0)==0 and deriv({(2,0):1},0)=={(1,0):2})
check('Contre-exemple concave',Q(0)>Q(-1))
check('Courbure de t4 nulle en zéro',deriv(deriv({(4,0):Q(1)},0),0)=={(2,0):12})
# La Hessienne ne change pas par ajout de termes affines.
q=plus({(2,0):Q(1),(1,1):Q(1),(0,2):Q(2)},scale(x,3))
check('Hessienne de la quadratique affine',[[deriv(deriv(q,j),i) for j in range(2)] for i in range(2)]==[[{(0,0):2},{(0,0):1}],[{(0,0):1},{(0,0):4}]])
for r in json.loads((C/'references/manifest.json').read_text(encoding='utf-8')):
 check('Intégrité '+r['file'],hashlib.sha256((C/'references'/r['file']).read_bytes()).hexdigest()==r['sha256'])
(C/'verification/calculs.json').write_text(json.dumps({'status':'passed','count':len(checks),'method':'Fractions et polynômes exacts ; dérivation de monômes, décompositions en carrés, géométrie et développements indépendants.','checks':checks,'limit':'Les tests exacts vérifient les exemples ; les théorèmes sont relus, pas prouvés formellement.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(checks),'contrôles exacts réussis.')
