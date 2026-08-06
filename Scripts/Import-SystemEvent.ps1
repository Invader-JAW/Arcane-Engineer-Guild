param([string]$RepoPath=".")
$ErrorActionPreference="Stop"
$RepoPath=(Resolve-Path $RepoPath).Path
$Inbox=Join-Path $RepoPath "System\Inbox"
New-Item -ItemType Directory -Path $Inbox -Force | Out-Null

$text=Get-Clipboard -Raw
if ($text -match '(?s)```json\s*(\{.*?\})\s*```') { $text=$Matches[1] }
try { $event=$text | ConvertFrom-Json } catch { throw "Clipboard does not contain valid SYSTEM EVENT JSON." }
if (-not $event.event_id) { throw "SYSTEM EVENT is missing event_id." }

$safe=([string]$event.event_id) -replace '[^A-Za-z0-9._-]','-'
$out=Join-Path $Inbox "$safe.json"
if (Test-Path $out) { throw "Inbox event already exists: $out" }

$event | ConvertTo-Json -Depth 20 | Set-Content -Path $out -Encoding UTF8
Write-Host "Imported SYSTEM EVENT -> $out" -ForegroundColor Green
