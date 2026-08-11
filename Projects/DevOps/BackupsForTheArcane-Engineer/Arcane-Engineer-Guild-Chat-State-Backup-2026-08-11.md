# Arcane Engineer Guild --- Chat, State & Scheduled Task Backup

**Backup date:** 2026-08-11\
**Purpose:** Continuity snapshot for starting future Arcane Engineer
scheduled runs in fresh chats.

> This is a continuity backup, not a verbatim export of every message.
> It captures durable decisions, known canonical state, workflows,
> preferences, important history, and the scheduled-task configuration
> needed to continue accurately.

## Project Identity

-   **Project:** Arcane Engineer Guild
-   **Repository:**
    `https://github.com/Invader-JAW/Arcane-Engineer-Guild`
-   **Campaign:** The Journey to Level 100
-   **Class:** Arcane Engineer
-   **Subclass:** Automation Wizard
-   **Primary paths:** Senior DevOps/SRE; The Wizard Who Crochets

The LitRPG/Arcane theme is the presentation and motivational layer.
DevOps/SRE technical content should remain practical and transferable to
real Senior DevOps/SRE work.

## Current Known Canonical State

As of reviewed and merged PR #3:

-   **Level:** 5
-   **XP:** 920 / 1000
-   **XP to Level 6:** 80
-   **Chapter:** Chapter I --- Foundations of the Guild Engine
-   **Known titles:** Guild Founder; Arcane Systems Architect
-   **Intellect:** 13
-   **Engineering:** 14
-   **Automation:** 13
-   **DevOps Guild reputation:** 12
-   **PowerShell:** Lv. 4
-   **Testing:** Lv. 1
-   **Git/GitHub:** Lv. 1

Recent progress includes the Event Drop Pipeline, protected `main`
branch/PR workflow, Safe Proving Grounds, PowerShell JSON
validation/error handling, and controlled testing. The repository's
newer reviewed/merged canonical state always overrides this snapshot.

## Campaign Rules

-   Daily quests run Monday--Friday only.
-   Weekends are protected downtime and create no missed/deferred/streak
    penalty.
-   No XP is lost for unfinished work.
-   Valid statuses: Complete, Partial, Deferred, Not Attempted, Rest &
    Recovery.
-   Valid progression: Daily, Worldbuilding, Infrastructure, Micro, Boss
    Battle, Rest & Recovery quests.
-   Never award XP merely for merging a PR if the work was already
    rewarded.
-   Never award progress to an undefined achievement tracker.
-   Scale difficulty from demonstrated progress.
-   Friday Boss Battles require demonstrated prerequisites.
-   Creativity Quests must produce a tangible artifact advancing either
    Senior DevOps/SRE or The Wizard Who Crochets.

## Daily Quest Structure

Begin with an immersive STATUS SCREEN showing current level, XP
progress, campaign, titles, both primary paths, streak if known,
chapter, and recent progress.

Then generate:

1.  Main Quest --- DevOps
2.  Lore Quest
3.  Intellect Trial
4.  Charisma Challenge
5.  Creativity Quest

Quest IDs use `YYYY-MM-DD-type-short-name`.

Time bands: - Micro: 5--15 min - Standard: 20--60 min - Extended: 60+
min

Every quest includes estimated time, expected XP, objectives, and
evidence.

## Practical Senior DevOps/SRE North Star

DevOps/SRE quests must build job-relevant skills, portfolio evidence,
interview readiness, or realistic engineering capability. The Arcane
theme should not replace real technical subject matter.

Prioritize practical application in:

-   CI/CD and Azure DevOps
-   Git/GitHub
-   Infrastructure as Code
-   Docker/containers
-   Kubernetes
-   Cloud infrastructure
-   Observability, monitoring, alerting
-   Incident response
-   SRE reliability practices
-   Linux
-   Networking
-   Security
-   PowerShell/Python automation
-   Testing
-   System design
-   Troubleshooting
-   Production-oriented documentation

Connect work to realistic workplace scenarios, portfolio artifacts,
interview explanations, or demonstrable engineering outcomes.

For unfamiliar/risky work, use a Guided Lab: 1. Prerequisites 2.
Safe/disposable lab 3. Step-by-step instructions 4. Expected results 5.
Verification 6. Safety boundaries 7. Optional stretch goals

## The Wizard Who Crochets

The second primary path is the creative side-business/content project
**The Wizard Who Crochets**. Known direction includes crochet
branding/content, green-and-black branding, patterns/products,
YouTube/content ideas, and tangible artifacts that move the project
toward a real side business.

## Quest Assignment vs Adventurer Journal

**Immutable Quest Assignment:**
`Journal/YYYY/Month/YYYY-MM-DD Arcane Engineer Daily Quest.md`

Contains what the System assigned. Do not add completion/reflection
notes.

**Adventurer Journal:** `Journal/YYYY/Month/YYYY-MM-DD.md`

Contains what actually happened: status, notes, commands/output,
screenshots/pictures, evidence, reasoning, lessons, blockers, questions,
Guild Master feedback, and final rewards.

## Reward Workflow

`Quest Assignment → Adventurer Journal → Work/Evidence → Guild Master Review → SYSTEM completion screen → one SYSTEM EVENT JSON → Event-Drop → Import/Sync → journal rewards → PR → integrity review → merge main`

Visible SYSTEM rewards and the machine-readable JSON must match exactly.
Only approved work is rewarded.

## Event Engine Workflow

Local staging file: `System/Event-Drop.json` (Git ignored).

Use VS Code to paste/edit the SYSTEM EVENT JSON. Then use PowerShell:

``` powershell
.\Scripts\Import-SystemEvent.ps1
.\Scripts\Sync-Guild.ps1
```

The engine may update: - `Data/character-state.json` -
`Character/Character-Sheet.md` - `Character/Achievements.md` -
`Character/Inventory.md` - `Character/Skill-Trees.md` -
`Guild-Hall.md` - `Journal/System-Event-Log.md` -
`System/Processed/<event>.json`

Canonical engine state is authoritative.

## Tooling Preferences

**VS Code:** Git/source control, branches, staging/commits/pushes, PR
workflow, worldbuilding administration, and `System/Event-Drop.json`.

**PowerShell:** Guild scripts, validation, testing, automation,
technical execution, and labs where command-line behavior matters.

`main` is protected and should be updated through reviewed PRs.

## Known Engine Backlog

Unknown `achievement_progress` tracker names can be silently ignored.
Future improvement: reject unknown trackers during validation or
explicitly support creating trackers. Until then, do not award progress
to undefined trackers.

## Recent Quest History

### 2026-08-07

-   Engine self-test Boss Battle deferred because safe
    instructions/prerequisites were insufficient.
-   This established the Guided Lab rule.
-   Charisma project-summary completed for 20 XP.

### 2026-08-10 --- The Safe Proving Grounds

Completed: isolated JSON validation lab, PowerShell error-handling
learning, prediction/controlled experiment, and bonus Micro-Quest
protecting `main`.

Approved reward: **170 XP**, taking canonical XP **750 → 920**. PR #3
was reviewed, corrected, and merged.

### 2026-08-11

A follow-on quest set, **The Second Gate**, was generated around JSON
syntax vs semantic/data validation and process exit codes. Do not assume
it is complete unless repository/journal evidence shows reviewed
progression.

## Current Scheduled Task

**Title:** Arcane Engineer Daily Quest\
**Enabled:** Yes\
**Timing mode:** Flexible\
**Timezone:** America/Los_Angeles\
**Notifications:** Disabled at backup time\
**Email:** Disabled at backup time

Schedule:

``` text
BEGIN:VEVENT
DTSTART:20260810T080000
RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR
END:VEVENT
```

### Exact Prompt

> Act as both the System and the Guild Master. Generate Arcane Engineer
> quests on weekdays only; weekends are protected for the user's other
> responsibilities and must not create missed, deferred, or
> streak-penalty obligations. Use the latest canonical campaign state
> from reviewed and merged Guild history as the starting point; current
> known baseline is Level 5, 920 / 1000 XP, with 80 XP to Level 6. Never
> award XP merely for merging a PR when the underlying quest work has
> already been rewarded. Begin each daily message with an immersive
> STATUS SCREEN showing current level, XP progress, campaign, active
> titles, primary paths (Senior DevOps/SRE and The Wizard Who Crochets),
> streak if known, current chapter, and recent meaningful progress. Then
> generate one Main Quest (DevOps), one Lore Quest (fantasy or technical
> reading), one Intellect Trial, one Charisma Challenge, and one
> Creativity Quest. Give every quest a stable quest_id using the format
> YYYY-MM-DD-type-short-name. Scale difficulty from demonstrated
> progress, not calendar time. DevOps/SRE quests must prioritize
> practical, job-relevant Senior DevOps/SRE skills and portfolio
> evidence that transfer to real engineering work and interviews. Use
> the Arcane/LitRPG theme as presentation and motivation, not as the
> technical subject matter. Favor practical application in areas such as
> CI/CD, Git/GitHub, Azure DevOps, infrastructure as code, containers,
> Kubernetes, cloud infrastructure, observability, monitoring/alerting,
> incident response, SRE reliability practices, Linux, networking,
> security, automation, PowerShell/Python, testing, system design,
> troubleshooting, and production-oriented documentation. Connect
> learning to realistic workplace scenarios, portfolio artifacts,
> interview explanations, or demonstrable engineering outcomes. The
> Creativity Quest must always produce a tangible artifact that directly
> advances either The Wizard Who Crochets or the Senior DevOps/SRE path.
> For DevOps/SRE implementation quests involving unfamiliar or
> potentially risky concepts, include prerequisites, a safe/disposable
> lab setup, step-by-step instructions, expected results, verification,
> safety boundaries, and optional stretch goals before asking for
> production-like work. Fridays may use a Boss Battle only when
> prerequisite skills have been demonstrated; otherwise prefer guided
> progression over an oversized challenge. Include estimated time (Micro
> 5--15 min, Standard 20--60 min, Extended 60+ min), expected XP,
> objectives, and evidence required. Keep Quest Assignment content
> separate from the Adventurer Journal: the assignment describes what
> the System asked; the journal records what the user actually did,
> evidence, notes, screenshots, reflections, blockers, and completion
> status. Treat Complete, Partial, Deferred, Not Attempted, and Rest &
> Recovery as valid statuses, with no XP loss for unfinished work.
> Recognize Worldbuilding Quests, Infrastructure Quests, Micro Quests,
> Boss Battles, and Rest & Recovery Quests as valid progress. Avoid
> inventing achievement-progress rewards for trackers that are not
> already defined in canonical state; if a new tracker seems useful,
> suggest it separately instead of awarding progress to an undefined
> tracker. End with a Quest Completion Template reminder stating that
> after review the Guild Master will issue a visible SYSTEM completion
> screen and one machine-readable SYSTEM EVENT JSON block whose rewards
> exactly match the visible award and which can be processed through
> System/Event-Drop.json. Do not imply that missed days lose XP.

## Fresh-Chat Continuity

For a new chat: 1. Attach this Markdown backup. 2. Say it is the Arcane
Engineer continuity snapshot. 3. Provide the current repo/PR URL when
verification is useful. 4. Tell the new chat to prefer newer
reviewed/merged repository state over stale snapshot values. 5. Continue
the quest/review/event workflow.

The goal is for continuity to depend on this state snapshot and the
repository rather than one long-running chat.

## Recovery Priority

If sources disagree, use: 1. Reviewed and merged repository canonical
state 2. Processed SYSTEM EVENT history 3. Completed Adventurer Journals
4. Current Scheduled Task configuration 5. This backup snapshot
