from pathlib import Path
import re,json
C=Path(__file__).resolve().parents[1];source=C/'beamer/body.tex'
if not source.exists():source=C/'body.tex'
s=source.read_text(encoding='utf-8');story=json.loads((C/'cadrage/storyboard.json').read_text(encoding='utf-8'));seen={'prérequis du cours'}
for slide in story:
 assert set(slide['prerequisites'])<=seen,slide['id'];seen.add(slide['id'])
assert len(story)==52 and re.findall(r'%% (CD\d+)\n',s)==[x['id'] for x in story]
assert s.count(r'\begin{frame}')==52
# Restrict to projected content; oral notes may document excluded source machinery.
visible=re.sub(r'\\note\{.*?\}\s*\\end\{frame\}',r'\\end{frame}',s,flags=re.S)
for term in ['hessienne','inversion locale','base duale','riesz','démonstration','preuve :']:
 assert term not in visible.lower(),term
assert r'\circ\df f{\vec a}' in s
# Detect explicit vector assignments to row tuples; function arguments and product-space pairs are distinct.
assert not re.search(r'\\vec\s*[a-z](?:_\w+)?\s*=\s*\([^()]*[,;][^()]*\)',visible)
cols=re.findall(r'\\vcol\{([^{}]*)\}',s);assert cols and all(r'\\' in c for c in cols)
(C/'verification/notations-dependances.json').write_text(json.dumps({'status':'passed','slides':52,'core_slides':48,'complement_slides':4,'vectors':'Colonnes vcol ; pas d’affectation de vecteur à un tuple en ligne. Les matrices jacobiennes scalaires ont une ligne, conformément au cours.','composition':'circ entre différentielles ; produit de jacobiennes distinct.','prerequisites':'Graphe ordonné ; définitions avant emploi. La slide 29 annonce explicitement les règles détaillées dans la dernière partie.','limit':'Contrôles lexicaux et graphe déclaré, complétés par relecture primaire ; pas de vérification formelle.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('52 slides : notations et dépendances vérifiées.')
