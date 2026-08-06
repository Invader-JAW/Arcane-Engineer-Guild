# Automated SYSTEM EVENT Protocol

`Data/character-state.json` is the canonical save state.

After a quest is completed:

1. Submit the Quest Completion Template to the Guild Master.
2. The Guild Master reviews the evidence.
3. The Guild Master returns a visible SYSTEM reward screen plus a machine-readable `SYSTEM EVENT` JSON block.
4. Copy the JSON block.
5. From the repository root run:

```powershell
.\Scripts\Import-SystemEvent.ps1
.\Scripts\Sync-Guild.ps1 -Commit -Push
```

The event is applied exactly once because every event has a unique `event_id`.

## Inbox Lifecycle

```text
System/
├── Inbox/
├── Processed/
└── Rejected/
```

## Generated Files

These are generated from `Data/character-state.json`:

- `Character/Character-Sheet.md`
- `Character/Achievements.md`
- `Character/Inventory.md`
- `Character/Skill-Trees.md`

Do not manually change tracked values in those files. Apply a SYSTEM EVENT instead.

## Example SYSTEM EVENT

See `System/Inbox/EXAMPLE-DO-NOT-PROCESS.json`.

## Nightly Sync

The GitHub Action runs at 11:37 PM in `America/Los_Angeles`, on manual dispatch, and whenever Inbox/data/script changes are pushed.

Push-triggered processing is the preferred immediate workflow; the nightly run is the safety net.
