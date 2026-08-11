# Arcane Engineer Rebuild Package

Files: - `Arcane-Engineer-Rebuild-Backup-2026-08-11.md` --- master
state/rules/workflow snapshot. - `NEW-CHAT-BOOTSTRAP.md` --- use to
initialize a fresh chat. - `SCHEDULED-TASK.md` --- exact schedule and
task prompt.

Recommended recovery: 1. Upload the master backup and bootstrap file to
a new chat. 2. Provide/verify the current Guild repository. 3. Let
repository canonical state override stale backup values. 4. Use
`SCHEDULED-TASK.md` to recreate the weekday automation. 5. Continue the
normal quest/review/SYSTEM EVENT/PR workflow.

Consider storing these files in a versioned backup/docs folder in the
Guild repository.
