FROM mcr.microsoft.com/powershell:7.4-ubuntu-22.04

WORKDIR /validation

COPY scripts/Test-Json.ps1 ./scripts/Test-Json.ps1
COPY events ./events

ENTRYPOINT ["pwsh", "./scripts/Test-Json.ps1"]