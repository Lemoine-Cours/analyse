# Analyse différentielle et convexité

**50 slides principales et 4 compléments séparés** ; couverture et clôture : **56 pages**. Notations du support, vecteurs colonnes et charte IMT Atlantique. Théorèmes avec hypothèses, résultats admis sans preuves ; aucun corrigé de TD projeté.

- [PDF](exports/analyse-differentielle-convexite.pdf)
- [Sources Beamer autonomes](exports/analyse-differentielle-convexite-sources.zip)
- [Source principale](beamer/main.tex), [contenu](beamer/body.tex)
- [Plan](cadrage/plan-detaille.md), [storyboard](cadrage/storyboard.json), [notations](cadrage/notations.json), [périmètre du TD](cadrage/perimetre-td.json)
- [Contrôle final](verification/controle-final.json), [science](verification/scientifique.json), [visuel](verification/visuel.json)

Segments et contrôle des variations → régularité C1 → différentielle seconde et Hessienne → Taylor → convexité, stricte convexité et forte convexité. Les exemples relient les notions sans résoudre les 12 exercices de base. Compléments séparés : limites du TAF vectoriel, différentiabilité sans C1, chaîne au second ordre et Jensen.

La différentielle seconde est bilinéaire ; la Hessienne la représente pour une fonction réelle. Composition avec `\circ`, vecteurs et coordonnées en colonnes, paramètre de forte convexité `mu>0` uniforme. Distinguer les conditions suffisantes et nécessaires, les vérifications en un point et sur tout un domaine, la norme opérateur et sa majoration par coefficients.

Compiler avec `./beamer/build.ps1` ou `bash beamer/build.sh` après initialisation du sous-module. LuaLaTeX, Montserrat et STIX Two Math nécessaires. Trois passages ; tout débordement ou caractère manquant bloque l’export. Le ZIP contient le thème et se compile sans sous-module. Figures TikZ éditables.

Contrôles : `python verification/verifier_calculs.py` et `python verification/verifier_structure.py`. 28 contrôles exacts ; 56 pages rendues et inspectées. Le paquet autonome est compilé séparément et son rendu comparé pixel par pixel. Relecture primaire, sans revue indépendante. Durée et niveau précis non fournis.

Les deux PDF originaux sont conservés avec empreintes SHA-256 ; les originaux du Drive restent inchangés. Les extraits théoriques du profil de génération excluent les sections d’exercices intégrés et leurs corrigés.
