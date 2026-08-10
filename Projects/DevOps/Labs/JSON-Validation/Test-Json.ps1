param(
    [Parameter(Mandatory)]
    [string]$Path
)

Write-Host "`nTesting: $Path" -ForegroundColor Cyan

try {
    $content = Get-Content $Path -Raw
    $null = $content | ConvertFrom-Json -ErrorAction Stop

    Write-Host "VALID JSON" -ForegroundColor Green
}
catch {
    Write-Host "INVALID JSON" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
}