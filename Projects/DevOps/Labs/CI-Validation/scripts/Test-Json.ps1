param(
    [Parameter(Mandatory)]
    [string]$Path
)

try {
    Get-Content $Path -Raw |
        ConvertFrom-Json -ErrorAction Stop |
        Out-Null

    Write-Host "PASS: $Path contains valid JSON."
    exit 0
}
catch {
    Write-Host "FAIL: $Path contains invalid JSON."
    Write-Host $_.Exception.Message
    exit 1
}