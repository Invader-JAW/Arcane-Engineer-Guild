param(
    [string]$RepoPath = ".",
    [string]$DropFile = "System\Event-Drop.json"
)

$ErrorActionPreference = "Stop"
$RepoPath = (Resolve-Path $RepoPath).Path
$Inbox = Join-Path $RepoPath "System\Inbox"
$Processed = Join-Path $RepoPath "System\Processed"
$DropPath = Join-Path $RepoPath $DropFile

New-Item -ItemType Directory -Path $Inbox -Force | Out-Null
New-Item -ItemType Directory -Path $Processed -Force | Out-Null

if (-not (Test-Path $DropPath)) {
    "{}" | Set-Content -Path $DropPath -Encoding UTF8
    Write-Host "Created $DropPath. Paste a SYSTEM EVENT JSON object into it, save, and run again." -ForegroundColor Yellow
    exit 0
}

$text = (Get-Content -Path $DropPath -Raw -Encoding UTF8).Trim()
if ([string]::IsNullOrWhiteSpace($text) -or $text -eq "{}") {
    throw "Event-Drop.json is empty. Paste the SYSTEM EVENT JSON into it and save the file."
}

if ($text -match '(?s)```json\s*(\{.*\})\s*```') { $text = $Matches[1] }

try { $event = $text | ConvertFrom-Json }
catch { throw "Event-Drop.json is not valid JSON. The file was NOT cleared." }

$required = @("schema_version","event_id","date","quest_type","quest_name","xp")
$missing = @()
foreach ($field in $required) {
    if ($null -eq $event.$field -or [string]::IsNullOrWhiteSpace([string]$event.$field)) { $missing += $field }
}
if ($missing.Count -gt 0) { throw "Missing required field(s): $($missing -join ', '). The file was NOT cleared." }
if ([int]$event.schema_version -ne 1) { throw "Unsupported schema_version. The file was NOT cleared." }

$eventId = [string]$event.event_id
$safeName = $eventId -replace '[^A-Za-z0-9._-]','-'
$outPath = Join-Path $Inbox "$safeName.json"
$processedPath = Join-Path $Processed "$safeName.json"

if (Test-Path $outPath) { throw "Inbox event already exists for '$eventId'. The file was NOT cleared." }
if (Test-Path $processedPath) { throw "Event '$eventId' was already processed. The file was NOT cleared." }

$tempPath = "$outPath.tmp"
$event | ConvertTo-Json -Depth 30 | Set-Content -Path $tempPath -Encoding UTF8
Move-Item $tempPath $outPath -Force

"{}" | Set-Content -Path $DropPath -Encoding UTF8

Write-Host "SYSTEM EVENT imported successfully." -ForegroundColor Green
Write-Host "Inbox: $outPath"
Write-Host "Event-Drop.json has been cleared."
Write-Host "Next: .\Scripts\Sync-Guild.ps1"
