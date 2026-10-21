from pathlib import Path
import json,re
C=Path(__file__).resolve().parents[1];p=C/'beamer/body.tex'
if not p.exists():p=C/'body.tex'
s=p.read_text(encoding='utf-8');story=json.loads((C/'cadrage/storyboard.json').read_text(encoding='utf-8'));seen={'prérequis Analyse I et algèbre'}
for slide in story:
 assert set(slide['prerequisites'])<=seen,slide['id'];seen.add(slide['id'])
assert len(story)==54 and re.findall(r'%% (AC\d+)\n',s)==[x['id'] for x in story]
assert s.count(r'\begin{frame}')==54
visible=re.sub(r'\\note\{.*?\}\s*\\end\{frame\}',r'\\end{frame}',s,flags=re.S)
assert not re.search(r'\\vec\s*[a-z](?:_\w+)?\s*=\s*\([^()]*[,;][^()]*\)',visible)
assert all(r'\\' in c for c in re.findall(r'\\vcol\{([^{}]*)\}',s))
assert r'\circ' in s and 'preuve :' not in visible.lower() and 'démonstration' not in visible.lower()
(C/'verification/notations-dependances.json').write_text(json.dumps({'status':'passed','slides':54,'core_slides':50,'complement_slides':4,'coordinates':'Vecteurs colonnes ; couples de directions dans espaces produits autorisés.','composition':'circ explicite','prerequisites':'Graphe ordonné ; convexité des ensembles avant les conclusions globales.','limit':'Contrôle lexical et graphe déclaré complétés par relecture primaire, sans certification formelle.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('54 slides : notations et dépendances vérifiées.')
