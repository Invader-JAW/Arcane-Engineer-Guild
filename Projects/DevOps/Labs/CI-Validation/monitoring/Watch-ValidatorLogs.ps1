param(
    [Parameter(Mandatory)]
    [string]$Path
)

$healthyCount = 0
$alertCount = 0
$invalidCount = 0

if (-not (Test-Path -Path $Path)) {
    Write-Error "Log file not found: $Path"
    exit 1
}

$logLines = Get-Content -Path $Path

foreach ($line in $logLines) {
    try {
        $log = $line | ConvertFrom-Json -ErrorAction Stop
    }
    catch {
        Write-Warning "Unable to parse structured log record."
        $invalidCount++
        continue
    }

    if ($log.level -eq "INFO") {
        Write-Host "[HEALTHY] $($log.message)"
        $healthyCount++

    }elseif ($log.level -eq "ERROR") {
        Write-Host "[ALERT] $($log.message)"
        Write-Host "Path: $($log.path)"
        $alertCount++

    }else {
        Write-Warning "Unknown log level: $($log.level)"
    }
}

Write-Host ""
Write-Host "Monitoring Summary"
Write-Host "Healthy Events: $healthyCount"
Write-Host "Alert Events:   $alertCount"
Write-Host "Invalid Events: $invalidCount"