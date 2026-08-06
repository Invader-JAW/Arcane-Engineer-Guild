param([string]$RepoPath=".",[switch]$Commit,[switch]$Push)
$ErrorActionPreference="Stop"
$RepoPath=(Resolve-Path $RepoPath).Path
Push-Location $RepoPath
try {
    python ".\Scripts\apply_events.py" --repo "."
    git status --short
    if ($Commit -or $Push) {
        git add Data Character Journal System
        git diff --cached --quiet
        if ($LASTEXITCODE -ne 0) { git commit -m "system: apply quest completion events" }
    }
    if ($Push) { git push origin main }
} finally { Pop-Location }
