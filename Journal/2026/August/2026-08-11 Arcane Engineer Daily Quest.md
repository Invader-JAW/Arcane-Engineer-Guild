---
date:
level:
xp_before:
xp_after:
status: active
tags:
  - daily-quest
---

# Daily Quest Log — YYYY-MM-DD

## Character Status

**Level:**  
**XP Before:**  
**XP After:**  

## Main Quest
## ⚙ Main Quest — Guard the Second Gate

**quest_id:** `2026-08-11-main-json-semantic-validator`  
**Path:** Senior DevOps/SRE  
**Type:** Guided Infrastructure Quest  
**Estimated Time:** Standard — 30–45 min  
**Expected XP:** **100 XP**
### Objective
**Objective:** Extend yesterday's disposable JSON lab so it distinguishes three states: malformed JSON, valid JSON with required data, and valid JSON missing required data.

Continue working only inside:

```
Projects/DevOps/Labs/JSON-Validation/
```

Do **not** modify the real Guild importer for this quest.

First, in VS Code create:

```
missing-fields-event.json
```

with:

```
{
  "event_id": "training-event-003"
}
```

This file is perfectly valid JSON—but it doesn't contain everything our imaginary training event requires.

Now create a **new** PowerShell script rather than overwriting yesterday's artifact:

```
Test-TrainingEvent.ps1
```

Use:

```
param(
    [Parameter(Mandatory)]
    [string]$Path
)

Write-Host "`nTesting event: $Path" -ForegroundColor Cyan

try {
    $content = Get-Content $Path -Raw
    $eventData = $content | ConvertFrom-Json -ErrorAction Stop
}
catch {
    Write-Host "FAIL: Malformed JSON" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
    exit 1
}

$requiredFields = @(
    "event_id",
    "quest_name",
    "xp"
)

$missingFields = @()

foreach ($field in $requiredFields) {
    if ($null -eq $eventData.$field) {
        $missingFields += $field
    }
}

if ($missingFields.Count -gt 0) {
    Write-Host "FAIL: JSON syntax is valid, but required data is missing." `
        -ForegroundColor Red

    Write-Host "Missing fields:" -ForegroundColor Yellow

    foreach ($field in $missingFields) {
        Write-Host " - $field"
    }

    exit 2
}

Write-Host "PASS: JSON syntax and required fields are valid." `
    -ForegroundColor Green

exit 0
```

Run the validator against yesterday's valid training event:

```
.\Projects\DevOps\Labs\JSON-Validation\Test-TrainingEvent.ps1 `
    -Path .\Projects\DevOps\Labs\JSON-Validation\valid-event.json
```

Expected:

```
PASS: JSON syntax and required fields are valid.
```

Now run it against yesterday's malformed event:

```
.\Projects\DevOps\Labs\JSON-Validation\Test-TrainingEvent.ps1 `
    -Path .\Projects\DevOps\Labs\JSON-Validation\malformed-event.json
```

Expected:

```
FAIL: Malformed JSON
```

Finally:

```
.\Projects\DevOps\Labs\JSON-Validation\Test-TrainingEvent.ps1 `
    -Path .\Projects\DevOps\Labs\JSON-Validation\missing-fields-event.json
```

Expected:

```
FAIL: JSON syntax is valid, but required data is missing.

Missing fields:
 - quest_name
 - xp
```

**Verification:** After each command, PowerShell exposes the program's exit code through:

```
$LASTEXITCODE
```

You should observe:

```
Valid event          → 0
Malformed JSON       → 1
Missing fields       → 2
```

This is particularly useful in CI/CD: automation doesn't have to interpret colored console text. It can make decisions from the process exit code.

**Safety Boundary:** This validator only reads training files. It does not call `Import-SystemEvent.ps1`, write to `System/Event-Drop.json`, or modify `Data/character-state.json`.

**Evidence required:** `Test-TrainingEvent.ps1`, `missing-fields-event.json`, console results from all three cases, their `$LASTEXITCODE` values, and one journal sentence explaining the difference between **syntax validation** and **data validation**.

**Optional Stretch Goal:** Add another training event where `"xp"` exists but contains `"ten"` instead of a number. Do not solve the problem yet. Record whether today's validator accepts it and why. That observation can become the next validation lesson.
### Evidence

### What I Did

### What I Learned

### What Was Difficult

### Guild Master Feedback

### Reward

- XP:
- Stats:
- Skills:
- Loot:

## Lore Quest
## 📖 Lore Quest — Exit Codes: How Scripts Speak to Automation

**quest_id:** `2026-08-11-lore-process-exit-codes`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated Time:** 10–15 min  
**Expected XP:** **25 XP**

**Objective:** Understand why yesterday's script printing `VALID JSON` was useful to a human, while today's explicit exit codes are more useful to another program.

Study the basic idea of process exit codes and PowerShell's `$LASTEXITCODE`.

Then answer in your journal:

```
1. What does exit code 0 conventionally mean?

2. Why can a CI/CD pipeline use an exit code more reliably
   than reading Write-Host text?

3. In today's validator, what do exit codes 1 and 2 represent?

4. Give one example of what a pipeline could do after receiving
   a non-zero exit code.
```

**Evidence required:** Your four answers.
### Reading or Resource

### Chapter or Section

### Lesson Learned

### Real-World Connection

### Guild Master Feedback

### Reward

## Intellect Trial
## 🧠 Intellect Trial — Valid Does Not Mean Acceptable

**quest_id:** `2026-08-11-intellect-valid-vs-acceptable`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated Time:** 5–10 min  
**Expected XP:** **20 XP**

Before executing `missing-fields-event.json`, predict:

```
Will ConvertFrom-Json succeed?

Will catch execute?

Will the required-field check execute?

Which fields will be reported missing?

What exit code will PowerShell receive?
```

Then run the experiment.

Record:

```
### My Prediction

### What Actually Happened

### What I Learned
```

**Evidence required:** Your prediction and comparison with the observed result.
### Challenge

### My Reasoning

### My Answer

### Guild Master Feedback

### Reward

## Charisma Challenge
## 🗣 Charisma Challenge — Explain the Two Gates

**quest_id:** `2026-08-11-charisma-explain-two-gates`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated Time:** 5–10 min  
**Expected XP:** **20 XP**

A teammate says:

> "If `ConvertFrom-Json` succeeds, why do we need more validation?"

Write a **3–5 sentence response** explaining the difference between:

```
Gate 1
Can the computer parse this JSON?

             ↓

Gate 2
Does this JSON contain the data our system requires?
```

Use your own words rather than copying the explanation from today's assignment.

**Evidence required:** Your completed explanation in the Adventurer Journal.
### Topic

### Audience

### My Explanation

### Guild Master Feedback

### Reward

## Creativity Quest
## 🎨 Creativity Quest — Finish the JSON Validation Portfolio Artifact

**quest_id:** `2026-08-11-creativity-json-validation-readme`  
**Path:** Senior DevOps/SRE  
**Type:** Portfolio Artifact  
**Estimated Time:** Standard — 20–30 min  
**Expected XP:** **50 XP**

Yesterday's README quest was **Not Attempted**, so there is no penalty and no debt attached to it. Today's Creativity Quest makes the README relevant to the larger lab you've now built.

Create:

```
Projects/DevOps/Labs/JSON-Validation/README.md
```

Document both stages of your experiment:

```
# PowerShell JSON Validation Lab

## Purpose

## Validation Model

### Gate 1 — JSON Syntax

### Gate 2 — Required Data

## Files

## Test Case 1 — Valid Event

Expected:
Actual:
Exit Code:

## Test Case 2 — Malformed JSON

Expected:
Actual:
Exit Code:

## Test Case 3 — Missing Required Fields

Expected:
Actual:
Exit Code:

## What I Learned

## Why Exit Codes Matter

## Safety Boundary

## DevOps / SRE Relevance

## Next Improvement
```

For **Next Improvement**, describe one thing the validator still cannot detect. You do not have to implement that improvement today.

This creates a tangible portfolio artifact demonstrating **PowerShell, JSON parsing, defensive validation, testing methodology, failure classification, exit codes, documentation, and safe experimentation**.

**Evidence required:** Completed `README.md` committed with the lab.
**Path:**

- [ ] The Wizard Who Crochets
- [ ] Senior DevOps/SRE

### Objective

### Deliverable

### Evidence

### How This Advances My Goal

### Guild Master Feedback

### Reward

## Daily Reflection

### Best Accomplishment

### Biggest Lesson

### Main Blocker

### Next Action

## Daily Rewards

**Total XP Earned:**  

**Stats Increased:**  

**Skills Improved:**  

**Achievements Unlocked:**  

**Loot Acquired:**  