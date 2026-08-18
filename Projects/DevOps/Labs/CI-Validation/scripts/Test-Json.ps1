param(
    [Parameter(Mandatory)]
    [string]$Path
)

function Write-StructuredLog {
    param(
        [string]$Level,
        [string]$Message,
        [string]$Path
    )

    $logEntry = [ordered]@{
        timestamp = (Get-Date).ToUniversalTime().ToString("o")
        level     = $Level
        message   = $Message
        path      = $Path
    }

    $logEntry | ConvertTo-Json -Compress
}

try {
    Get-Content $Path -Raw |
        ConvertFrom-Json -ErrorAction Stop |
        Out-Null

    Write-Host "PASS: $Path contains valid JSON."
    Write-StructuredLog -Level "INFO" -Message "JSON validation succeeded" -Path $Path
    exit 0
}
catch {
    Write-Host "FAIL: $Path contains invalid JSON."
    Write-Host $_.Exception.Message
    Write-StructuredLog -Level "ERROR" -Message "JSON validation failed" -Path $Path
    exit 1
}