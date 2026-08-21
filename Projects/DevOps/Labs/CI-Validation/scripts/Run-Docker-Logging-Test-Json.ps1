$log = docker run --rm arcane-json-validator:observability -Path ./events/valid-event.json


# Split the multiline string into an array of lines
$lines = $log -split '`r?`n' | Where-Object { $_.Trim() }

if ($lines.Count -ge 2) {
    if ($lines.Count -ge 3) {
        # Line 0 and 1 are the text prefix, Line 2 is the JSON string this is for failed run
        $statusText = $lines[0,1].TrimEnd('.')
        $parsed = $lines[2] | ConvertFrom-Json
    }else{
        # Line 0 is the text prefix, Line 1 is the JSON string
        $statusText = $lines[0].TrimEnd('.')
        $parsed = $lines[1] | ConvertFrom-Json
    }
    # Add the text prefix as a property
    $parsed | Add-Member -NotePropertyName "ValidationResult" -NotePropertyValue $statusText
    
    # Output your properties
    $parsed.ValidationResult
    $parsed.level
    $parsed.message
    $parsed.path
} else {
    Write-Error "Log output did not contain at least two lines." 
}