# Cours d’analyse

Dépôt de David Lemoine pour les supports universitaires d’analyse en **Beamer et PDF**, avec la charte **IMT Atlantique** partagée avec le [cours d’algèbre](https://github.com/Lemoine-Cours/algebre).

Les chapitres sont construits à partir du cours, des TD et des supports existants fournis par l’enseignant.

## Organisation

Un dossier par chapitre, nommé selon son contenu. Le [modèle de chapitre](_modele-chapitre/README.md) contient :

- `references/` : copies des supports d’origine et leurs empreintes ; originaux préservés.
- `brief/` : périmètre, niveau, durée, exclusions et attentes.
- `cadrage/` : plan, enchaînement des notions, notations et storyboard.
- `beamer/` : sources LaTeX et scripts de compilation.
- `exports/` : PDF du cours et archive autonome de ses sources.
- `verification/` : contrôles scientifiques, calculs et relecture visuelle.

Le [thème commun](https://github.com/Lemoine-Cours/theme-imt-atlantique) est épinglé au même commit que dans le dépôt algèbre. Le [système de production](https://github.com/Lemoine-Cours/atelier-slides) reste commun aux matières.

## Ligne pédagogique

Définitions → théorèmes et hypothèses → compréhension par exemples et figures → méthodes en étapes courtes. Pas de preuves dans les slides. Le TD délimite les notions utiles en arrière-plan, sans fournir le plan du cours ni des corrigés projetés. Compléments séparés du socle.

Respect strict des notations du support ; composition avec `\circ` ; vecteurs et coordonnées en colonnes. Lecture verticale, espaces bien répartis, une propriété par ligne et colonnes seulement si nécessaires. Définitions cyan, théorèmes bleu marine, conclusions vertes ; figures vectorielles pédagogiques.

## Préparer un chapitre

Fournir le support de cours, le TD sans correction et les slides existants s’ils sont disponibles. Préciser le chapitre de départ et le périmètre du TD. Un plan détaillé est proposé avant la génération des slides.

Copier `_modele-chapitre/` vers le dossier du chapitre, puis adapter le brief et les métadonnées. Ne pas publier le modèle comme un cours terminé.

## Compiler

```powershell
git clone --recurse-submodules https://github.com/Lemoine-Cours/analyse.git
cd analyse
./_modele-chapitre/beamer/build.ps1
```

Ou `bash _modele-chapitre/beamer/build.sh`. LuaLaTeX, Montserrat, STIX Two Math et les dépendances du thème sont nécessaires. Après un clonage simple : `git submodule update --init --recursive`. Les scripts effectuent trois passages et bloquent l’export en cas de débordement ou de caractère manquant.

La compilation seule ne valide pas la mise en page. Inspecter les pages rendues, vérifier les résultats et leurs hypothèses, puis compiler le paquet autonome avant de publier un chapitre.

## Calcul différentiel du premier ordre

[Chapitre](calcul-differentiel-premier-ordre/README.md) · [PDF](calcul-differentiel-premier-ordre/exports/calcul-differentiel-premier-ordre.pdf) · [Beamer autonome](calcul-differentiel-premier-ordre/exports/calcul-differentiel-premier-ordre-sources.zip). 48 slides de socle, 4 compléments ; définitions, théorèmes admis, exemples, figures et contrôles.

## Analyse différentielle et convexité

[Chapitre](analyse-differentielle-convexite/README.md) · [PDF](analyse-differentielle-convexite/exports/analyse-differentielle-convexite.pdf) · [Sources autonomes](analyse-differentielle-convexite/exports/analyse-differentielle-convexite-sources.zip). 50 slides principales et 4 compléments : accroissements finis, régularité, Taylor et convexité.
