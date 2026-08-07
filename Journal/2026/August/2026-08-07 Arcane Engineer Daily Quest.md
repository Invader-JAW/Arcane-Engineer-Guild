# ⚔ Friday Boss Battle

**Quest ID:** `2026-08-07-main-engine-self-test`

**Type:** Boss Battle (Portfolio)

**Estimated Time:** Extended (60–120 min)

**Reward:** 250 XP

### Objective

Validate that the Arcane Engineer Engine can recover from real-world failures.

Complete the following:

- Create three intentionally invalid SYSTEM EVENT files:
    - malformed JSON
    - missing required field
    - duplicate `event_id`
- Verify the importer rejects each one without clearing `Event-Drop.json`.
- Process one valid SYSTEM EVENT afterward to confirm the normal pipeline still succeeds.
- Document the results in a new testing document (for example, `Docs/Event-System-Test-Report.md`).

### Evidence

- Test report committed to the repository.
- Console output or screenshots showing both failed validation and successful processing.
- Git commit.

I rejected the the Quest, I'm not ready. **Quest ID:** `2026-08-07-main-engine-self-test`

---

# 📖 Lore Quest

**Quest ID:** `2026-08-07-lore-event-sourcing`

**Estimated Time:** Standard (20–30 min)

**Reward:** 35 XP

### Objective

Read about:

- Event Sourcing
- CQRS (high-level overview)
- Immutable event logs

Relate each concept to one feature already present in the Arcane Engineer Guild.

### Evidence

A short Markdown note summarizing:

- three ideas learned
- one improvement idea for a future v3 backlog

---

# 🧠 Intellect Trial

**Quest ID:** `2026-08-07-intellect-schema-review`

**Estimated Time:** Micro (10–15 min)

**Reward:** 20 XP

### Objective

Review the current SYSTEM EVENT schema.

Identify:

- one field that could become optional,
- one field that should remain mandatory,
- one field that could be added in a future schema version.

### Evidence

A Markdown note with your reasoning.

---

# 🗣️ Charisma Challenge

**Quest ID:** `2026-08-07-charisma-project-summary`

**Estimated Time:** Micro (10–15 min)

**Reward:** 20 XP

### Objective

Write a concise explanation (about 200 words) of the Arcane Engineer Guild that could be shared with another engineer.

Cover:

- the problem it solves,
- how the event system works,
- why it is valuable as a portfolio project.

### Evidence

The finished write-up.

---

# 🎨 Creativity Quest

**Quest ID:** `2026-08-07-creativity-guild-dashboard`

**Estimated Time:** Standard (30–60 min)

**Reward:** 50 XP

### Objective

Create a polished visual mock-up of the **Guild Hall** dashboard for Obsidian.

Include:

- Status Screen
- Character summary
- Quest Board
- Inventory shortcut
- Achievements
- Current campaign
- Primary paths
- Recent loot

This should become the visual target for future renderer improvements.

### Evidence

One of:

- an Obsidian page,
- a Figma mock-up,
- a diagram,
- or a high-quality Markdown layout committed to the repository.

---

## 🎯 Total Possible Rewards

|Quest|XP|
|---|---|
|Friday Boss Battle|250|
|Lore Quest|35|
|Intellect Trial|20|
|Charisma Challenge|20|
|Creativity Quest|50|
|**Total**|**375 XP**|

---

## Quest Completion Reminder

When you complete one or more quests:

1. Submit your evidence for review.
2. The Guild Master will evaluate the work.
3. You'll receive:
    - an immersive **SYSTEM completion screen**,
    - exactly one **SYSTEM EVENT JSON** matching the approved rewards.
4. Paste the JSON into `System/Event-Drop.json`.
5. Run:
    
    ```
    .\Scripts\Import-SystemEvent.ps1
    .\Scripts\Sync-Guild.ps1 -Commit -Push
    ```
    
6. Your character sheet, achievements, inventory, and Guild Hall will automatically regenerate from the updated save state.