---
date: 2026-08-12
level: "5"
xp_before: 920
xp_after:
status: active
tags:
  - daily-quest
---

# Daily Quest Log — 2026-08-12

## Character Status

**Level:**  5
**XP Before:**  920
**XP After:**  


```
══════════════════════════════════════════════════════
                 ARCANE ENGINEER
                  STATUS SCREEN
══════════════════════════════════════════════════════

Campaign
The Journey to Level 100

Class
Arcane Engineer — Automation Wizard

Level
5

XP
920 / 1000

██████████████████░░ 92%

80 XP UNTIL LEVEL 6

Active Titles
Guild Founder
Arcane Systems Architect

Primary Paths
⚙ Senior DevOps / Site Reliability Engineer
🧶 The Wizard Who Crochets

Current Chapter
Chapter I — Foundations of the Guild Engine

Recent Progress
✓ Safe Proving Grounds completed
✓ PowerShell validation/error handling practiced
✓ Controlled testing workflow demonstrated
✓ main branch protected through PR workflow
✓ PR #3 merged into canonical history
✓ Aug. 11 recognized as Rest & Recovery

══════════════════════════════════════════════════════
             WEDNESDAY QUEST BOARD
                  2026-08-12

             THE PIPELINE SENTINEL
     Turn a Local Check into a CI Quality Gate
══════════════════════════════════════════════════════
```

Today moves away from adding more Arcane-engine mechanics and toward a **real Senior DevOps/SRE workflow**: taking a validator that works locally and making CI run it automatically.

The professional skill being practiced is **shift-left validation**: catching a bad change automatically before it reaches `main`.

### ⚙ Main Quest — Build the Pipeline Sentinel

**quest_id:** `2026-08-12-main-github-actions-validation`  
**Path:** Senior DevOps/SRE  
**Type:** Guided Infrastructure Quest  
**Estimated time:** Standard, 45–60 min  
**Expected XP:** **100 XP**

**Workplace scenario:** Your team accepts JSON configuration through pull requests. Engineers currently remember to run validation manually. Someone eventually forgets. Your job is to make the repository perform the check automatically.

**Objective:** Create your first small CI quality gate using GitHub Actions.

**Prerequisites:** Use a feature branch rather than `main`. Work only with disposable training JSON. Do not connect this workflow to the Guild's real `System/Event-Drop.json`, importer, character state, secrets, production resources, or deployment infrastructure.

Create this lab structure in VS Code:

```
Projects/DevOps/Labs/CI-Validation/
├── events/
│   ├── valid-event.json
│   └── invalid-event.json
├── scripts/
│   └── Test-Json.ps1
└── README.md
```

Create `events/valid-event.json`:

```
{
  "event_id": "ci-training-001",
  "service": "training-api",
  "environment": "development"
}
```

Create `events/invalid-event.json` intentionally malformed:

```
{
  "event_id": "ci-training-002",
  "service": "training-api",
}
```

Create `scripts/Test-Json.ps1`:

```
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
```

Before touching CI, verify the tool locally:

```
.\Projects\DevOps\Labs\CI-Validation\scripts\Test-Json.ps1 `
  -Path .\Projects\DevOps\Labs\CI-Validation\events\valid-event.json

$LASTEXITCODE
```

Expected exit code:

```
0
```

Then test the malformed file:

```
.\Projects\DevOps\Labs\CI-Validation\scripts\Test-Json.ps1 `
  -Path .\Projects\DevOps\Labs\CI-Validation\events\invalid-event.json

$LASTEXITCODE
```

Expected exit code:

```
1
```

Only after those local tests work, create:

```
.github/workflows/json-validation.yml
```

Use this deliberately small workflow:

```
name: JSON Validation Lab

on:
  pull_request:
    paths:
      - "Projects/DevOps/Labs/CI-Validation/**"
      - ".github/workflows/json-validation.yml"

jobs:
  validate-json:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Validate training JSON
        shell: pwsh
        run: |
          ./Projects/DevOps/Labs/CI-Validation/scripts/Test-Json.ps1 `
            -Path ./Projects/DevOps/Labs/CI-Validation/events/valid-event.json
```

Commit and push the work through your normal VS Code Source Control workflow, then open/update the PR.

**Expected result:** GitHub Actions starts a `validate-json` job, checks out the repository, launches PowerShell on a Linux runner, executes the same validation script you tested locally, receives exit code `0`, and marks the job successful.

**Verification evidence:** Capture the Actions/PR check showing `validate-json` passing. Also preserve your successful local test and `$LASTEXITCODE`.

**Safety boundary:** Today's goal is **CI validation**, not deployment. Do not add credentials, Azure access, secrets, production environments, package publishing, automatic merging, or modifications to Guild canonical state.

**Optional stretch goal:** After obtaining a successful CI run, temporarily change the workflow's `-Path` to `invalid-event.json` on the feature branch and observe the CI job fail. Restore the workflow to the valid file afterward. This provides direct evidence that the quality gate actually blocks bad input rather than merely displaying a green check.

**Evidence required:** workflow YAML, PowerShell validator, training JSON, successful local output, `$LASTEXITCODE`, successful CI check, and—if attempted—the controlled failed CI check.

---

### 📖 Lore Quest — Understand the CI Execution Chain

**quest_id:** `2026-08-12-lore-ci-execution-chain`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated time:** 10–15 min  
**Expected XP:** **25 XP**

Read the relevant introductory sections of the official [GitHub Actions documentation](https://docs.github.com/en/actions/get-started/understand-github-actions?utm_source=chatgpt.com) covering workflows, events, jobs, runners, steps, and actions.

Then map today's implementation:

```
Pull Request
     ↓
Workflow
     ↓
Job
     ↓
Runner
     ↓
Steps
     ↓
PowerShell validator
     ↓
Exit code
     ↓
Pass / Fail
```

In your Adventurer Journal, explain what each layer contributes in **one sentence each**.

**Evidence required:** Your execution-chain explanation.

---

### 🧠 Intellect Trial — Predict the Failure Propagation

**quest_id:** `2026-08-12-intellect-ci-failure-propagation`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated time:** 5–10 min  
**Expected XP:** **20 XP**

Before attempting the optional failure test, predict what happens when:

```
ConvertFrom-Json
      ↓
throws an error
      ↓
catch
      ↓
exit 1
      ↓
GitHub Actions
      ↓
?
```

Record answers to three questions:

1. Does the PowerShell step pass or fail?
2. Does the `validate-json` job pass or fail?
3. What should appear on the PR?

Then compare your prediction with the actual result if you perform the stretch test.

**Evidence required:** Prediction plus observed result, or prediction alone if the stretch test is not attempted.

---

### 🗣 Charisma Challenge — Explain the Business Value

**quest_id:** `2026-08-12-charisma-ci-quality-gate`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated time:** 5–10 min  
**Expected XP:** **20 XP**

Imagine an interviewer asks:

> “Why would you put validation in CI instead of relying on developers to run a script locally?”

Give a **30–60 second interview-style answer**.

A strong explanation should touch on consistency, automation, early failure detection, protecting shared branches, and reducing dependence on human memory.

Do not merely explain what YAML does. Explain **why the engineering practice matters**.

**Evidence required:** Your answer in your Adventurer Journal.

---

### 🎨 Creativity Quest — Create a Portfolio Architecture Diagram

**quest_id:** `2026-08-12-creativity-ci-architecture`  
**Path:** Senior DevOps/SRE  
**Type:** Portfolio Artifact  
**Estimated time:** Standard, 20–30 min  
**Expected XP:** **50 XP**

Create:

```
Projects/DevOps/Labs/CI-Validation/docs/ci-validation-flow.md
```

Build a Mermaid diagram showing:

```
Developer
   ↓
Feature Branch
   ↓
Pull Request
   ↓
GitHub Actions
   ↓
PowerShell Validator
   ↓
Valid? ── Yes → CI Pass
   │
   No
   ↓
CI Failure
   ↓
Fix Before Merge
```

Below the diagram, add short sections titled:

```
## Problem

## Solution

## Failure Behavior

## Why This Matters in Production

## Skills Demonstrated
```

The finished artifact should be understandable by a hiring manager or engineer who encounters the repository without knowing anything about the Arcane Engineer system.

**Evidence required:** Completed Markdown architecture artifact committed with the lab.

```
══════════════════════════════════════════════════════
                    QUEST REWARDS
══════════════════════════════════════════════════════

⚙ Pipeline Sentinel                         100 XP
📖 CI Execution Chain                        25 XP
🧠 Failure Propagation                       20 XP
🗣 CI Quality-Gate Explanation               20 XP
🎨 CI Architecture Artifact                  50 XP
──────────────────────────────────────────────────────
Maximum Available                           215 XP

Canonical Starting XP                       920 / 1000
XP Needed for Level 6                        80

Potential Level-Up                           YES

Rewards are awarded only after evidence review.
Crossing 1000 XP does not require completing
the entire board.

Rest & Recovery            ✓ Valid
Partial                    ✓ Valid
Deferred                   ✓ Valid
Not Attempted              ✓ Valid

No unfinished work removes XP.
══════════════════════════════════════════════════════
```

### Quest Completion Template Reminder

Keep today's **Quest Assignment immutable** after saving it. Record actual work separately in `Journal/2026/August/2026-08-12.md`, including quest status, commands/results, CI evidence, screenshots, observations, blockers, reflections, and artifact paths.

After Guild Master review, the approved work will receive one visible **SYSTEM completion screen** and exactly **one machine-readable SYSTEM EVENT JSON block** whose rewards match that screen. That event can then move through the established `System/Event-Drop.json` workflow.