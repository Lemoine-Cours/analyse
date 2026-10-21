# Calcul différentiel du premier ordre

**48 slides de socle et 4 compléments séparés** ; couverture et clôture : **54 pages**. Cours construit à partir des deux PDF de l’enseignant, avec ses notations et la charte IMT Atlantique. Résultats admis, sans preuves ni corrigés projetés.

- [PDF](exports/calcul-differentiel-premier-ordre.pdf)
- [Sources Beamer autonomes](exports/calcul-differentiel-premier-ordre-sources.zip)
- [Source principale](beamer/main.tex) et [contenu](beamer/body.tex)
- [Plan](cadrage/plan-detaille.md), [storyboard](cadrage/storyboard.json), [notations](cadrage/notations.json), [périmètre du TD](cadrage/perimetre-td.json)
- [Contrôle final](verification/controle-final.json), [science](verification/scientifique.json), [inspection visuelle](verification/visuel.json)

Voisinages et limites → approximation linéaire → différentielle → partielles et jacobienne → gradient → calcul et composition. Les exemples conceptuels et les figures éditables relient les notions. Le TD de base sert de périmètre ; ses 12 exercices ne sont pas résolus dans les slides. Les compléments portent sur la compacité, les autres bases et les applications bilinéaires.

La différentielle fléchée est une application linéaire ; la jacobienne sa matrice dans les bases canoniques ; le gradient est un vecteur colonne. La jacobienne d’une fonction scalaire est une matrice ligne. La composition se note `\circ`. La dérivée suivant un vecteur conserve son échelle : aucune normalisation implicite.

Compiler avec `./beamer/build.ps1` ou `bash beamer/build.sh` après initialisation du sous-module. LuaLaTeX, Montserrat, STIX Two Math et dépendances du thème nécessaires. Le ZIP contient le thème et se compile sans sous-module. Trois passages et contrôle des débordements avant export. Figures TikZ modifiables.

Contrôles : `python verification/verifier_calculs.py` et `python verification/verifier_structure.py`. Les développements polynomiaux et calculs rationnels sont exacts ; les théorèmes et hypothèses sont relus séparément. Les 54 pages sont rendues et inspectées ; le paquet autonome est compilé et comparé pixel par pixel. Relecture primaire du même assistant, sans revue indépendante. Durée et niveau précis non renseignés.

Les deux PDF d’origine sont préservés avec empreintes SHA-256. Les extraits théoriques du profil de génération excluent les sections d’exercices intégrés et leurs corrections. Les originaux du Drive restent inchangés.
