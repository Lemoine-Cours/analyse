from pathlib import Path
import json,hashlib,re
from fractions import Fraction as Q
from math import comb
C=Path(__file__).resolve().parents[1];results=[]
def check(n,ok):
 assert ok,n
 results.append(n)
def add(a,b):
 d=a.copy()
 for k,v in b.items():d[k]=d.get(k,Q(0))+v
 return {k:v for k,v in d.items() if v}
def mul(a,b):
 d={}
 for i,x in a.items():
  for j,y in b.items():d[i+j]=d.get(i+j,Q(0))+x*y
 return {k:v for k,v in d.items() if v}
def scale(a,k):return {i:v*k for i,v in a.items() if v*k}
def line(a,h):return {0:Q(a),1:Q(h)}
def quad(x,y):return add(mul(x,x),scale(mul(y,y),3))
x,y=line(1,2),line(1,-3);t=quad(x,y)
check('Développement quadratique exact',t=={0:Q(4),1:Q(-14),2:Q(31)})
check('Gradient obtenu par coefficients de déplacement',quad(line(1,1),line(1,0))[1]==2 and quad(line(1,0),line(1,1))[1]==6)
h,k=Q(1,50),Q(-1,100);v=(1+h)**2+3*(1+k)**2
check('Valeur numérique exacte',v==Q(39807,10000))
check('Variation affine',2*h+6*k==Q(-1,50))
check('Erreur de linéarisation exacte',v-(4+2*h+6*k)==Q(7,10000))
check('Reste majoré par trois normes au carré',h*h+3*k*k<=3*(h*h+k*k))
# Dérivées de F par extraction du coefficient de t, indépendamment des formules partielles.
x,y=line(1,2),line(1,-3);F1=add(mul(x,x),y);F2=add(mul(x,y),scale(mul(y,y),-1))
check('Action différentielle vectorielle',F1[1]==1 and F2[1]==5)
check('Reste de F',F1[2]==4 and F2[2]==-15)
# Chaîne : développer g(f(a+t h)) avant d’extraire le coefficient.
x,y=line(1,2),line(0,3);u=add(x,scale(y,2));w=add(x,scale(y,-1));composed=add(mul(u,u),scale(w,2))
check('Composition directe',composed[0]==3 and composed[1]==14)
check('Produit jacobien',tuple(sum(a*b for a,b in zip((2,2),c)) for c in [(1,1),(2,-1)])==(4,2))
check('Dérivée suivant le vecteur donné',2*3+6*4==30)
check('Vecteur donné norme 5',3**2+4**2==25)
check('Dérivée unitaire',Q(30,5)==6)
check('Norme du gradient au carré',2**2+6**2==40)
check('Direction maximale normalisée',Q(1,10)+Q(9,10)==1)
check('Tangente de niveau perpendiculaire au gradient',2*3+6*(-1)==0)
check('Point de la figure sur niveau 4',1**2+3*1**2==4)
check('Flèche à échelle 1/5',Q(2,5)==Q(14,10)-1 and Q(6,5)==Q(22,10)-1)
# Trajectoire directe f(t,1-t).
z=quad({1:Q(1)},{0:Q(1),1:Q(-1)})
check('Trajectoire polynomiale directe',z=={0:Q(3),1:Q(-6),2:Q(4)})
check('Dérivée trajectoire',z[1]==-6 and 2*z[2]==8)
# Produit xy² développé sur une droite arbitraire.
x,y=line(2,3),line(-1,4);w=mul(x,mul(y,y))
check('Règle du produit contrôlée par développement',w[1]==(-1)**2*3+2*2*(-1)*4)
check('Contre-exemple deux chemins',Q(1*1,1+1)==Q(1,2) and Q(0,1)==0)
check('Tangente à x² en 1',1==2*1-1 and 2==2*1)
for ref in json.loads((C/'references/manifest.json').read_text(encoding='utf-8')):
 check('Intégrité '+ref['file'],hashlib.sha256((C/'references'/ref['file']).read_bytes()).hexdigest()==ref['sha256'])
(C/'verification/calculs.json').write_text(json.dumps({'status':'passed','count':len(results),'method':'Fractions exactes ; développement polynomial sur des droites, extraction du coefficient du premier ordre ; produits matriciels et géométrie exacte.','checks':results,'limit':'Les calculs exacts ne constituent pas une preuve des théorèmes généraux.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(len(results),'contrôles exacts réussis.')
