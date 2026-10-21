$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    New-Item -ItemType Directory -Force build, ../exports | Out-Null
    1..3 | ForEach-Object {
        & lualatex '-interaction=nonstopmode' '-halt-on-error' '-no-shell-escape' '-output-directory=build' main.tex
        if ($LASTEXITCODE -ne 0) { throw 'Compilation LuaLaTeX échouée : consulter build/main.log.' }
    }
    $layoutIssues = Select-String -LiteralPath build/main.log -Pattern 'Overfull|Missing character'
    if ($layoutIssues) { throw 'Débordement ou caractère manquant : aucun PDF exporté.' }
    Copy-Item build/main.pdf ../exports/calcul-differentiel-premier-ordre.pdf -Force
} finally { Pop-Location }
