# Optimisation dans les espaces réels de dimension finie

[PDF](exports/optimisation-dans-rn.pdf) · [Beamer autonome](exports/optimisation-dans-rn-sources.zip) · [Plan détaillé](cadrage/plan-detaille.md) · [Contrôles](verification/controle-final.md).

50 diapositives principales et 4 compléments, plus couverture et clôture. Définitions, théorèmes avec hypothèses, exemples de compréhension et figures TikZ éditables, sans preuves ni corrigés du TD. Charte IMT Atlantique et vecteurs colonnes.

Progression : inversion locale → fonctions implicites → optimisation sans contrainte → égalités et Lagrange → inégalités et KKT. Nécessité et suffisance sont séparées. Les signes du Lagrangien suivent le cours original.

## Compilation

Dans le dépôt cloné avec ses sous-modules, exécuter `./beamer/build.ps1` ou `bash beamer/build.sh`. Le PDF est exporté après trois passages LuaLaTeX sans débordement ni caractère manquant. Le ZIP inclut le thème et les fonds : l’extraire puis exécuter son script pour produire `cours.pdf`.

Les références originales sont conservées avec leurs empreintes dans `references/`. La relecture est effectuée par le même assistant, avec contrôles exacts des exemples et inspection visuelle, sans certification formelle ni revue indépendante.
