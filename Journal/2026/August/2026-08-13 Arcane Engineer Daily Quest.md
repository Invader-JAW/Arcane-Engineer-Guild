---
date: 2026-08-13
level: "6"
xp_before: 1065
xp_after:
status: active
tags:
  - daily-quest
---

# Daily Quest Log — 2026-08-13

## Character Status

**Level:**  6
**XP Before:**  1065
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
6

XP
1065 / 1350

███████████████░░░░░ 79%

285 XP UNTIL LEVEL 7

Active Titles
🏰 Guild Founder
⚙ Arcane Systems Architect

Primary Paths
⚙ Senior DevOps / Site Reliability Engineer
🧶 The Wizard Who Crochets

Current Chapter
Chapter I — Foundations of the Guild Engine

Recent Meaningful Progress
✓ Safe PowerShell validation practices established
✓ GitHub main branch protected through PR workflow
✓ Local JSON validator converted into CI automation
✓ GitHub Actions quality gate successfully executed
✓ Controlled CI failure propagated exit code 1 correctly
✓ CI/CD, GitHub Actions, and Testing skills advanced
✓ Level 6 achieved

══════════════════════════════════════════════════════
              THURSDAY QUEST BOARD
                   2026-08-13

             THE QUALITY GATE
     From CI Check → Enforced Merge Protection
══════════════════════════════════════════════════════
```

Today's progression builds directly on the Pipeline Sentinel. You have proven that CI can detect a bad change. The next practical Senior DevOps/SRE skill is learning how teams turn a CI check into an **enforced repository control**.

The engineering concept is simple:

```
Developer opens PR
        ↓
Automated CI executes
        ↓
Required check passes?
     ↙        ↘
   NO          YES
    ↓            ↓
Merge blocked   Review/merge allowed
```

This is a common production workflow and gives you a useful interview story: you didn't merely create CI—you integrated automated validation with repository governance.

## ⚙ Main Quest — Enforce the Quality Gate

**quest_id:** `2026-08-13-main-required-ci-check`  
**Path:** Senior DevOps/SRE  
**Type:** Guided Infrastructure Quest  
**Estimated time:** Standard — 30–45 minutes  
**Expected XP:** **100 XP**

**Workplace scenario:** A team has automated tests, but developers can still merge a PR when those tests fail. Your task is to make successful validation a requirement for changes entering the protected branch.

### Prerequisites

You already have the important pieces:

```
Protected main branch
        +
Pull-request workflow
        +
GitHub Actions validation job
```

Today's work should reuse those rather than create another validator.

### Safety boundary

Work only with the existing repository ruleset and the disposable `CI-Validation` lab.

Do **not** modify production credentials, secrets, deployments, cloud infrastructure, `System/Event-Drop.json`, processed events, or canonical character state as part of this experiment.

Do not push experimental changes directly to `main`.

### Step 1 — Inspect the existing protection

In [GitHub](https://github.com/Invader-JAW/Arcane-Engineer-Guild?utm_source=chatgpt.com), open:

```
Arcane-Engineer-Guild
→ Settings
→ Rules
→ Rulesets
```

Open the ruleset protecting the default branch.

Before changing anything, record in your Adventurer Journal which protections are currently enabled.

### Step 2 — Find required status checks

Inside the ruleset, look for the protection normally called:

```
Require status checks to pass
```

Enable it if it is not already enabled.

GitHub's documentation describes required status checks as a way to require checks to pass before collaborators can merge into a protected branch.

### Step 3 — Select your CI check

Configure the rule to require the validation check created yesterday.

Look for the check associated with:

```
validate-json
```

Do not guess a different check name if GitHub presents something slightly different. Use the check actually produced by yesterday's successful workflow.

Save the ruleset.

### Step 4 — Verify the successful path

Use your current feature branch/PR workflow.

Confirm that a PR with the validator succeeding shows the required check as passing.

Record:

```
Required Check:
Result:
Merge State:
```

### Step 5 — Controlled failure test

Only if you are comfortable repeating yesterday's safe experiment, temporarily point the training workflow at:

```
invalid-event.json
```

Push the feature-branch change.

Expected result:

```
PowerShell validator
        ↓
exit 1
        ↓
GitHub Actions failure
        ↓
Required check fails
        ↓
Merge should be blocked
```

Capture evidence.

Then **restore the workflow to `valid-event.json`**, push again, and verify that CI becomes green.

Do not leave the intentionally failing configuration in the final PR.

### Verification

Your evidence should demonstrate both:

```
Bad validation
→ CI failure
→ merge protection

Good validation
→ CI success
→ quality gate satisfied
```

### Evidence required

Record in today's Adventurer Journal:

- screenshot or description of the ruleset setting;
- required check name;
- successful check result;
- controlled failed result if attempted;
- whether GitHub prevented merging;
- final confirmation that the workflow was restored to the passing configuration.

### Optional stretch goal

Write one sentence explaining why **branch protection without automated tests** and **automated tests without branch protection** each leave a different gap.

---

## 📖 Lore Quest — Required Checks vs CI

**quest_id:** `2026-08-13-lore-required-checks`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated time:** 10–15 minutes  
**Expected XP:** **25 XP**

Read the relevant section of GitHub's official documentation on protected branches and required status checks:

[About protected branches — GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com)

Then explain the distinction in your own words:

```
CI answers:
_____________________________

A required status check answers:
_____________________________

Together they provide:
_____________________________
```

The key lesson is that **running validation** and **enforcing its result** are separate responsibilities.

**Evidence required:** Your three answers.

---

## 🧠 Intellect Trial — Find the Missing Control

**quest_id:** `2026-08-13-intellect-defense-in-depth`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated time:** 5–10 minutes  
**Expected XP:** **20 XP**

Consider these three repositories:

```
Repository A
Pull requests required
CI not configured

Repository B
CI configured
CI is not required for merging

Repository C
Pull requests required
CI configured
CI must pass before merge
```

Rank them from **weakest → strongest protection**.

For each repository, identify one realistic way a bad change could reach `main`.

For Repository C, explain what risk still remains even with these controls.

There is no perfect repository protection—the Senior-level skill is understanding what each layer does and does not protect against.

**Evidence required:** Ranking plus your reasoning.

---

## 🗣 Charisma Challenge — Senior DevOps Interview Story

**quest_id:** `2026-08-13-charisma-quality-gate-story`  
**Path:** Senior DevOps/SRE  
**Type:** Micro Quest  
**Estimated time:** 10–15 minutes  
**Expected XP:** **25 XP**

Prepare a short interview response to:

> “Tell me about a time you improved the safety of a software delivery workflow.”

Use this structure:

```
Situation
What problem existed?

Task
What needed to become safer?

Action
What did you implement?

Result
What failure can the system now catch or prevent?
```

Base the answer on the actual progression you built:

```
PowerShell validation
→ process exit codes
→ GitHub Actions
→ controlled CI failure
→ required merge quality gate
```

Aim for roughly **60–90 seconds spoken**.

Do not describe the Arcane Engineer game system to the interviewer. Present this as the technical lab/project it actually is.

**Evidence required:** Your completed interview answer.

---

## 🎨 Creativity Quest — CI Quality Gate Portfolio README

**quest_id:** `2026-08-13-creativity-ci-portfolio-readme`  
**Path:** Senior DevOps/SRE  
**Type:** Portfolio Artifact  
**Estimated time:** Standard — 20–30 minutes  
**Expected XP:** **50 XP**

Create or expand:

```
Projects/DevOps/Labs/CI-Validation/README.md
```

Make this understandable to someone reviewing your GitHub portfolio.

Include:

```
# CI Validation Quality Gate

## Problem

## Solution

## Architecture

## Local Validation

## CI Validation

## Failure Behavior

## Branch Protection

## Verification

## Skills Demonstrated

## Production Improvements
```

Under **Architecture**, you can use:

Under **Production Improvements**, identify at least three ways you would mature this beyond the training lab.

Examples include:

```
JSON Schema validation
unit tests
multiple configuration files
dependency pinning
security scanning
CODEOWNERS
environment approvals
least-privilege workflow permissions
artifact/log retention
```

You don't need to implement those today.

**Evidence required:** Completed portfolio README committed with the lab.

```
══════════════════════════════════════════════════════
                    QUEST REWARDS
══════════════════════════════════════════════════════

⚙ Enforce the Quality Gate                   100 XP
📖 Required Checks vs CI                      25 XP
🧠 Defense in Depth                           20 XP
🗣 Senior DevOps Interview Story              25 XP
🎨 CI Quality Gate Portfolio README           50 XP
──────────────────────────────────────────────────────
Maximum Available                            220 XP

Canonical Starting XP
1065 / 1350

XP Needed for Level 7
285

Maximum Possible XP Today
1285 / 1350

Level 7 Possible Today
NO

This is intentional.

Today's progression deepens an existing
production-relevant skill instead of rushing
toward another level.

Complete              ✓ Valid
Partial               ✓ Valid
Deferred              ✓ Valid
Not Attempted         ✓ Valid
Rest & Recovery       ✓ Valid

No unfinished work removes XP.
══════════════════════════════════════════════════════
```

### Quest Completion Template Reminder

Save today's Quest Assignment separately from `Journal/2026/August/2026-08-13.md`. The assignment records what the System asked; the Adventurer Journal records what you actually did, including quest statuses, ruleset observations, CI results, screenshots, interview response, portfolio artifact, blockers, lessons learned, and evidence paths.

After review, the Guild Master will award only completed and verified work. You will receive one visible **SYSTEM completion screen** and exactly one matching machine-readable **SYSTEM EVENT JSON** block for processing through `System/Event-Drop.json`. No unfinished quest creates XP loss or quest debt.