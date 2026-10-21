#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p build ../exports
for pass in 1 2 3; do
  lualatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=build main.tex
done
if grep -Eq 'Overfull|Missing character' build/main.log; then
  echo 'Débordement ou caractère manquant : aucun PDF exporté.' >&2
  exit 1
fi
cp build/main.pdf ../exports/optimisation-dans-rn.pdf
