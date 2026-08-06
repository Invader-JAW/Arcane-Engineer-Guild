# SYSTEM EVENT Drop-File Workflow

Use `System/Event-Drop.json` as the permanent local paste target. It is ignored by Git.

1. Paste the Guild Master's SYSTEM EVENT JSON into `System/Event-Drop.json`.
2. Save the file.
3. Run:

```powershell
.\Scripts\Import-SystemEvent.ps1
```

4. The importer validates the event and writes an immutable copy to `System/Inbox/`.
5. Only after a successful write, the drop file is reset to `{}`.
6. Apply the event with:

```powershell
.\Scripts\Sync-Guild.ps1 -Commit -Push
```

If validation fails, the drop file is left untouched so the event can be corrected.

A tracked template remains at `System/Event-Drop.example.json`.
