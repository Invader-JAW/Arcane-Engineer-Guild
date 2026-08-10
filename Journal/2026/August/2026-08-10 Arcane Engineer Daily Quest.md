## ⚙ Main Quest — Build the Safe Proving Grounds

**quest_id:** `2026-08-10-main-safe-json-lab`  
**Path:** Senior DevOps/SRE  
**Type:** Guided Lab / Infrastructure Quest  
**Estimated Time:** Standard — 30–45 min  
**Expected XP:** **100 XP**

**Objective:** Learn how to deliberately test valid and malformed JSON in a disposable environment without touching the real Arcane Engineer event pipeline.

**Prerequisites:** VS Code for creating/managing the lab files, and PowerShell for executing the test script. You do **not** need to understand the Guild's complete event engine yet.

**Safety Boundary:** Do not modify `System/Event-Drop.json`, do not place these training events in `System/Inbox`, and do not run `Import-SystemEvent.ps1`. Nothing in this lab should modify `Data/character-state.json`.

In VS Code, create:

```
Labs/
└── JSON-Validation/
    ├── valid-event.json
    ├── malformed-event.json
    └── Test-Json.ps1
```

Put this into `valid-event.json`:

```
{
  "event_id": "training-event-001",
  "quest_name": "Training Event",
  "xp": 10
}
```

Put this deliberately broken JSON into `malformed-event.json`:

```
{
  "event_id": "training-event-002",
  "quest_name": "Broken Training Event",
  "xp": 10,
}
```

Create `Test-Json.ps1`:

```
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
```

From the repository root, test the valid file:

```
.\Labs\JSON-Validation\Test-Json.ps1 `
    -Path .\Labs\JSON-Validation\valid-event.json
```

**Expected result:**

```
VALID JSON
```

Before running the malformed test, stop here and complete today's Intellect Trial.

Then execute:

```
.\Labs\JSON-Validation\Test-Json.ps1 `
    -Path .\Labs\JSON-Validation\malformed-event.json
```

**Expected result:**

```
INVALID JSON
```

The exact error text may vary. That is okay. What matters is that the script enters `catch` instead of treating the input as valid.

**Verification:** In VS Code Source Control, inspect the changed files. The lab files should be new, but your real character/event files should not have changed merely because you executed these tests.

In particular, you should see no test-caused modification to:

```
System/Event-Drop.json
Data/character-state.json
Character/Character-Sheet.md
Guild-Hall.md
```

**Evidence required:** `Test-Json.ps1`, both JSON files, the VALID and INVALID results in your journal or screenshots, and 2–3 sentences explaining why this lab cannot alter your canonical character state.

**Optional Stretch Goal — 0 required XP:** Add a third `empty-event.json` containing `{}` and predict whether the current script considers it valid. This begins demonstrating the difference between **valid JSON syntax** and **valid SYSTEM EVENT data**.

---

## 📖 Lore Quest — Understanding PowerShell Error Handling

**quest_id:** `2026-08-10-lore-powershell-errors`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated Time:** Micro — 10–15 min  
**Expected XP:** **25 XP**

**Objective:** Learn what the Main Quest's `try`, `catch`, and `-ErrorAction Stop` are doing rather than simply copying the script.

Study the PowerShell concepts of `try {}`, `catch {}`, terminating errors, and `-ErrorAction Stop`.

Then answer in today's Adventurer Journal:

```
1. What code belongs inside try?

2. Under what condition does catch execute?

3. Why does this script use -ErrorAction Stop?

4. Give one example of where this kind of error handling
   could protect a DevOps automation pipeline.
```

**Evidence required:** Your four answers in the journal. They can be short; demonstrating understanding matters more than length.

---

## 🧠 Intellect Trial — Predict Before Executing

**quest_id:** `2026-08-10-intellect-json-prediction`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated Time:** Micro — 5–10 min  
**Expected XP:** **20 XP**

**Objective:** Practice the engineering cycle:

**Hypothesis → Controlled Experiment → Observation → Conclusion**

Before running `malformed-event.json`, create this section in today's journal:

```
### My Prediction

Will PowerShell stop completely?

Will catch execute?

Will malformed-event.json change?

Will anything be deleted?

Will Data/character-state.json change?
```

Write your predictions without looking up the answers.

Then execute the malformed test.

Add:

```
### What Actually Happened

...

### Difference Between My Prediction and Reality

...
```

Being wrong does **not** reduce the reward. A useful experiment that disproves your hypothesis is successful engineering.

**Evidence required:** Prediction, actual result, and at least one comparison between the two.

---

## 🗣 Charisma Challenge — Explain the Safety Boundary

**quest_id:** `2026-08-10-charisma-explain-safe-lab`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated Time:** Micro — 5–10 min  
**Expected XP:** **20 XP**

**Objective:** Imagine another engineer asks:

> Why didn't you just put malformed JSON into the real Arcane Engineer importer and see what happened?

Write a **3–5 sentence technical explanation**.

Try to communicate this progression:

```
Unknown behavior
      ↓
Controlled environment
      ↓
Experiment
      ↓
Understanding
      ↓
Confidence
      ↓
Production-like testing
```

Avoid simply saying, "because it might break."

Explain what isolation gives the engineer.

**Evidence required:** Your finished explanation in today's Adventurer Journal.

---

## 🎨 Creativity Quest — Build the Portfolio Lab README

**quest_id:** `2026-08-10-creativity-json-lab-readme`  
**Path:** Senior DevOps/SRE  
**Type:** Portfolio Artifact  
**Estimated Time:** Standard — 20–30 min  
**Expected XP:** **50 XP**

**Objective:** Turn today's learning exercise into something another engineer could understand from your repository.

Create:

```
Labs/
└── JSON-Validation/
    └── README.md
```

Use this structure:

```
# PowerShell JSON Validation Lab

## Purpose

Explain what problem this experiment investigates.

## What I Built

Explain the small PowerShell validator.

## Lab Files

Explain:
- valid-event.json
- malformed-event.json
- Test-Json.ps1

## Valid JSON Test

Command used:

Result:

What the result means:

## Invalid JSON Test

Command used:

Result:

What the result means:

## What I Learned

Explain try/catch, ConvertFrom-Json, and
-ErrorAction Stop in your own words.

## Safety

Explain why this experiment cannot alter the
Arcane Engineer Guild character state.

## Why This Matters in DevOps

Explain why validating data before allowing it
into later automation stages is useful.
```

If you capture screenshots, you may store them with the project and embed them in the README or your Adventurer Journal.

**Evidence required:** `Labs/JSON-Validation/README.md` containing your actual test results and explanation.

This is a tangible **Senior DevOps/SRE portfolio artifact**, not merely quest paperwork.

```
══════════════════════════════════════════════════════
                   REWARD TABLE
══════════════════════════════════════════════════════

⚙ Safe JSON Lab                         100 XP
📖 PowerShell Error Handling             25 XP
🧠 JSON Prediction Trial                 20 XP
🗣 Explain the Safety Boundary           20 XP
🎨 JSON Validation Lab README            50 XP
──────────────────────────────────────────────
Maximum Available                       215 XP

Current XP                              750
Potential XP                            965 / 1000

Level 6 is NOT required today.

Partial completion is valid progress.

Also recognized:
🌎 Worldbuilding Quests
🏗 Infrastructure Quests
⚡ Micro Quests
☠ Boss Battles
🌿 Rest & Recovery Quests

Protected weekends create no missed quests.
Missed or deferred weekday quests never remove XP.
══════════════════════════════════════════════════════
```

### Quest Completion Template Reminder

Keep the immutable quest assignment separate from `Journal/2026/August/2026-08-10.md`. Use the Adventurer Journal for what you actually did: notes, PowerShell output, predictions, difficulties, screenshots, evidence paths, lessons learned, partial work, and questions.

You do **not** need to complete all five quests before submitting work. Mark each quest **Complete**, **Partial**, **Deferred**, **Not Attempted**, or **Rest & Recovery** as appropriate.

After quest review, the Guild Master will issue one visible **SYSTEM completion screen** containing the approved rewards and **one machine-readable SYSTEM EVENT JSON block matching exactly those awarded rewards** for processing through `System/Event-Drop.json`.