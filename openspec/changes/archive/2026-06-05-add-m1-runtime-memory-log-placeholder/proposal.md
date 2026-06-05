## Why

Sprint 4 carries forward the S3-5 runtime memory log placeholder so the M1 exploration-memory loop communicates that an accepted Memory Fragment interaction produced a lasting placeholder entry. S3-2 proves interaction truth, S3-3 proves prompt readability, S3-4 proves reveal feedback, and S4-1 provides fresh test baseline evidence; the next step is a minimal read-only log surface without expanding into a full journal or progression system.

## What Changes

- Add a minimal runtime memory log placeholder that appends one visible entry after an accepted MemoryState-backed Memory Fragment reveal/collect outcome.
- Keep the runtime log strictly presentation/read-model only:
  - no reveal/collect truth ownership,
  - no interaction validity decisions,
  - no duplicate handling decisions outside presentation deduplication,
  - no input callback ownership,
  - no inventory, quest, journal progression, save/profile, dialogue, lore database, or narrative branching behavior.
- Use an approved read-only accepted interaction/reveal context or memory response snapshot from the existing S3-2/S3-4 path.
- Preserve existing S3-2 interaction behavior, S3-3 prompt behavior, and S3-4 reveal feedback behavior.
- Add focused EditMode tests and manual PlayMode evidence for accepted log append, duplicate suppression, ownership boundaries, console classification, and dirty asset classification.

## Non-goals

- No MemoryState behavior changes.
- No MemoryInteractionService command-path changes.
- No input architecture refactor or Unity InputAction callback ownership changes.
- No S3-3 prompt behavior changes.
- No S3-4 reveal feedback playback behavior changes.
- No CombatCore, EnemyIntent, TargetContext, Camera, PlayerLocomotion, Health, or Encounter behavior changes.
- No full journal, inventory, quest, lore, codex, save/profile, progression UI, narrative memory graph, clue tracking, contradiction tracking, district reinterpretation, or truth restoration framework.
- No MemoryInteractionTickBridge extraction.
- No MemoryRaycastProProbe alignment.
- No R3/MessagePipe migration.
- No broad Nhem DI migration.
- No scene/prefab/content edits unless separately approved for minimal UI wiring.

## Capabilities

### New Capabilities
- `runtime-memory-log-placeholder`: Player sees a minimal read-only runtime memory log entry after an accepted Memory Fragment reveal/collect outcome, while UI remains downstream of memory truth.

### Modified Capabilities
- None.

## Impact

- Affected systems:
  - UI / Presentation placeholder surface
  - Read-only accepted memory interaction/reveal context consumption
  - Debug/evidence capture for runtime memory log readability
- Dependencies:
  - S3-2 Memory Fragment interaction path and evidence
  - S3-3 interaction prompt placeholder remains unchanged
  - S3-4 reveal feedback placeholder remains unchanged
  - S4-1 fresh Unity test baseline evidence
- M0/M1 loop impact:
  - Improves readability for `prompt -> Interact -> reveal feedback -> runtime log`.
  - Does not change M0 combat loop behavior or S3-2 interaction truth.
- Ownership boundary affected:
  - UI observes accepted memory reveal/result context but must not own or mutate `MemoryState`, `MemoryInteractionService`, input callbacks, fragment runtime truth, or progression state.
