---
date: 2026-08-17
level: "6"
xp_before: 1285
xp_after: 1385
status: Complete
tags:
  - daily-quest
---

# Daily Quest Log — 2026-08-17

## Character Status

**Level:**  6
**XP Before:**  1285
**XP After:**   1385
**Status:** Complete 
```
══════════════════════════════════════════════════════
                 ARCANE ENGINEER
                  STATUS SCREEN
══════════════════════════════════════════════════════

Campaign       The Journey to Level 100
Class          Arcane Engineer — Automation Wizard

Level          6
XP             1285 / 1350
Progress       ███████████████████░ 95%
Next Level     65 XP

Active Titles
🏰 Guild Founder
⚙ Arcane Systems Architect

Primary Paths
⚙ Senior DevOps / Site Reliability Engineer
🧶 The Wizard Who Crochets

Streak
No weekend obligation applied.
Saturday and Sunday were protected Rest & Recovery.

Current Chapter
Chapter I — Foundations of the Guild Engine

Recent Meaningful Progress
✓ PowerShell JSON validation
✓ GitHub Actions CI validation
✓ Controlled failure testing
✓ Required status-check merge protection
✓ Dockerized validator
✓ Container success path verified: exit 0
✓ Container failure path verified: exit 1

Engineering 17 · Automation 16 · Intellect 15
CI/CD Lv. 4 · GitHub Actions Lv. 2
Docker Lv. 1 · Testing Lv. 3
DevOps Guild Reputation 19

══════════════════════════════════════════════════════
                 MONDAY QUEST BOARD
                   August 17, 2026

              THE OBSERVABILITY LENS
       Turn Raw Execution into Useful Signals
══════════════════════════════════════════════════════
```

The weekend created **no missed quests, deferred work, XP loss, or streak penalty**. Today's progression resumes from Friday's completed Container Forge at **Level 6 · 1285 / 1350 XP**.

You've demonstrated that a service/tool can return a reliable success or failure signal. The next Senior DevOps/SRE progression is learning that an exit code tells you **that something failed**, while observability helps an engineer understand **what happened and where to investigate**.

## ⚙ Main Quest — Add Structured Logging to the Validator

**quest_id:** `2026-08-17-main-structured-logging`  
**Type:** Guided Infrastructure Quest  
**Path:** Senior DevOps/SRE  
**Estimated time:** Standard — 40–60 min  
**Expected XP:** **100 XP**

**Workplace scenario:** Your validator now runs locally, in CI, and inside Docker. Imagine that dozens of validation jobs execute every day. `PASS` and `FAIL` are useful, but operations teams need output that can eventually be searched, filtered, shipped to monitoring systems, and correlated with failures.

Your objective is to make the validator emit **structured JSON log records** while preserving its existing exit-code behavior.

### Prerequisites

Use the existing disposable lab:

```
Projects/DevOps/Labs/CI-Validation/
```

Before modifying anything, verify the existing container still behaves correctly:

```
docker run --rm arcane-json-validator:lab `
  -Path ./events/valid-event.json

$LASTEXITCODE
```

Expected:

```
PASS...
0
```

If the existing lab no longer passes, record the blocker instead of stacking new changes onto a broken baseline.

### Safe lab setup

Create a feature branch through your normal VS Code Source Control workflow.

Only modify the CI-Validation lab.

Do **not** connect this exercise to Azure, production monitoring, external logging services, credentials, secrets, cloud resources, or Guild canonical state.

### Step 1 — Add a logging function

Open:

```
Projects/DevOps/Labs/CI-Validation/scripts/Test-Json.ps1
```

Add a small reusable function:

```
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
```

The important engineering idea is the shape of the record:

```
timestamp
level
message
path
```

instead of an unstructured sentence whose fields would need to be extracted later.

### Step 2 — Log successful validation

In the success path, emit something equivalent to:

```
Write-StructuredLog `
    -Level "INFO" `
    -Message "JSON validation succeeded" `
    -Path $Path
```

Preserve:

```
exit 0
```

### Step 3 — Log failed validation

In the failure path, emit:

```
Write-StructuredLog `
    -Level "ERROR" `
    -Message "JSON validation failed" `
    -Path $Path
```

Preserve:

```
exit 1
```

Do not remove reliable process exit behavior merely because logging was added.

### Step 4 — Rebuild the image

```
docker build `
  -t arcane-json-validator:observability `
  .\Projects\DevOps\Labs\CI-Validation
```

Expected result: successful image build.

### Step 5 — Test the success signal

```
docker run --rm `
  arcane-json-validator:observability `
  -Path ./events/valid-event.json

$LASTEXITCODE
```

Expected output should resemble:

```
{"timestamp":"2026-08-17T...Z","level":"INFO","message":"JSON validation succeeded","path":"./events/valid-event.json"}
```

and:

```
0
```

### Step 6 — Test the failure signal

Run the malformed fixture.

Expected structured output should contain:

```
{
  "level": "ERROR",
  "message": "JSON validation failed"
}
```

The exact timestamp will differ.

Then verify:

```
$LASTEXITCODE
1
```

### Step 7 — Prove the output is machine-readable

Capture the successful output:

```
$log = docker run --rm `
  arcane-json-validator:observability `
  -Path ./events/valid-event.json

$parsed = $log | ConvertFrom-Json

$parsed.level
$parsed.message
$parsed.path
```

Expected:

```
INFO
JSON validation succeeded
./events/valid-event.json
```

That final test matters. You're proving another program can consume the output—not merely that it looks like JSON to a human.

### Verification

Your final evidence should demonstrate:

```
VALID JSON
    ↓
Structured INFO log
    ↓
exit 0

INVALID JSON
    ↓
Structured ERROR log
    ↓
exit 1

JSON log
    ↓
ConvertFrom-Json
    ↓
Individual fields accessible
```

**Evidence required:** updated `Test-Json.ps1`, successful Docker build, INFO log + exit 0, ERROR log + exit 1, successful parsing of the log record, and journal observations.

**Safety boundary:** Do not send logs anywhere externally. Do not include credentials, tokens, environment secrets, personal data, or full production payloads in log messages.

**Optional stretch:** Add a `correlation_id` generated once per validator execution and explain how such an identifier could help correlate messages belonging to the same CI run.

---

## 📖 Lore Quest — Logs, Metrics, and Traces

**quest_id:** `2026-08-17-lore-observability-signals`  
**Type:** Micro Quest  
**Path:** Senior DevOps/SRE  
**Estimated time:** 10–15 min  
**Expected XP:** **25 XP**

Learn the conceptual distinction between the three common observability signals:

```
LOGS
What happened?

METRICS
How much / how often?

TRACES
Where did the request travel?
```

Then write one example of each for a hypothetical validation service.

For example, don't simply define a metric—identify something measurable such as validation duration or failed validations.

**Objective:** Be able to explain why monitoring and observability are related but not identical.

**Evidence required:** one practical log, metric, and trace example plus a 2–3 sentence explanation of the distinction.

---

## 🧠 Intellect Trial — Diagnose the Invisible Failure

**quest_id:** `2026-08-17-intellect-observability-diagnosis`  
**Type:** Micro Quest  
**Path:** Senior DevOps/SRE  
**Estimated time:** 10–15 min  
**Expected XP:** **20 XP**

Consider this production incident:

```
CI failure rate increased from
2% → 35%

The application still reports:

exit 1
```

You can add only **three pieces of diagnostic information**.

Choose three from—or invent better alternatives to:

```
timestamp
file/path
validation error
duration
runner hostname
commit SHA
correlation ID
PowerShell version
container image version
```

For each one, explain:

```
Signal:
Why I chose it:
Question it helps answer:
```

There isn't one required combination. The trial is about prioritizing useful signals under constraints.

**Evidence required:** three choices with reasoning.

---

## 🗣 Charisma Challenge — Incident Update

**quest_id:** `2026-08-17-charisma-incident-update`  
**Type:** Micro Quest  
**Path:** Senior DevOps/SRE  
**Estimated time:** 10–15 min  
**Expected XP:** **25 XP**

Imagine you're the engineer investigating:

```
CI validation failures:
Normal: 2%
Current: 35%
```

Write a concise update you could give your engineering team.

Include:

```
Impact
What you know
What you don't know yet
What you're investigating
Next update/action
```

Avoid claiming a root cause you haven't proven.

**Objective:** Practice communicating uncertainty clearly during an incident—an important SRE and senior-engineering skill.

**Evidence required:** approximately 4–7 sentences suitable for a Slack/Teams incident channel.

---

## 🎨 Creativity Quest — Build an Observability Runbook

**quest_id:** `2026-08-17-creativity-validator-runbook`  
**Type:** Portfolio Artifact  
**Path:** Senior DevOps/SRE  
**Estimated time:** Standard — 20–30 min  
**Expected XP:** **50 XP**

Create:

```
Projects/DevOps/Labs/CI-Validation/RUNBOOK.md
```

This is not another README. Treat it as an operational document an engineer would open **after the validator starts failing**.

Include:

```
# JSON Validator Incident Runbook

## Purpose

## Symptoms

## First Checks

## Inspect Structured Logs

## Reproduce Locally

## Reproduce with Docker

## Common Failure Scenarios

## Recovery

## Verification After Recovery

## Escalation Information
```

Under **Common Failure Scenarios**, document at least:

```
Malformed JSON
Container/image problem
Unexpected validator/script failure
```

Under **Verification After Recovery**, explicitly require both:

```
valid fixture → exit 0
invalid fixture → exit 1
```

**Objective:** Produce a portfolio artifact demonstrating that you think beyond deployment and consider how software will actually be supported.

**Evidence required:** completed `RUNBOOK.md` committed with the CI-Validation lab.

```
══════════════════════════════════════════════════════
                 AVAILABLE REWARDS
══════════════════════════════════════════════════════

⚙ Structured Logging                     100 XP
📖 Observability Signals                   25 XP
🧠 Diagnostic Prioritization               20 XP
🗣 Incident Communication                  25 XP
🎨 Validator Incident Runbook              50 XP
──────────────────────────────────────────────────────
Maximum                                   220 XP

Starting XP                        1285 / 1350
XP Required for Level 7                     65

Level 7 is possible today,
but only completed and reviewed work earns XP.

No XP is awarded for the weekend.
No XP was lost during the weekend.
No quest debt was created.

Complete             ✓
Partial              ✓
Deferred             ✓
Not Attempted        ✓
Rest & Recovery      ✓
══════════════════════════════════════════════════════
```

### Quest Completion Template Reminder

Keep today's Quest Assignment separate from `Journal/2026/August/2026-08-17.md`. The assignment records what the System asked you to do; the Adventurer Journal records what actually happened—including completion status, commands, output, screenshots, evidence, observations, mistakes, corrections, blockers, and reflections.

After evidence review, the Guild Master will issue one visible **SYSTEM completion screen** showing the approved rewards and exactly one machine-readable **SYSTEM EVENT JSON** block whose rewards match that screen. The event can then be processed through `System/Event-Drop.json`.

Anything unfinished receives an appropriate **Partial, Deferred, Not Attempted, or Rest & Recovery** status with no XP loss.