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