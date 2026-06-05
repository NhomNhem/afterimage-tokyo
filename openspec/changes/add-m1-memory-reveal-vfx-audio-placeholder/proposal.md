## Why

Sprint 3 needs the Memory Fragment loop to communicate that an accepted interaction changed memory state. S3-2 proves the interaction truth path and S3-3 proves the interaction prompt, but the reveal/collect response still needs a restrained placeholder VFX/audio acknowledgement before Sprint 3 smoke.

## What Changes

- Add a minimal memory reveal VFX/audio placeholder that plays only after an accepted MemoryState-backed reveal/collect outcome.
- Keep reveal feedback strictly presentation-only:
  - no reveal/collect truth ownership,
  - no interaction validity decisions,
  - no duplicate handling decisions,
  - no input callback ownership.
- Use an approved read-only accepted reveal/interaction result context from the S3-2 path.
- Preserve existing S3-2 interaction behavior and S3-3 prompt behavior.
- Add evidence expectations for accepted reveal feedback, rejection/duplicate non-playback behavior, ownership boundaries, console classification, and dirty asset classification.

## Non-goals

- No MemoryState behavior changes.
- No MemoryInteractionService command-path changes.
- No CombatCore timing/result changes.
- No input architecture refactor.
- No runtime memory log UI; that remains S3-5.
- No full cinematic, dialogue, quest, inventory, save/profile, progression, or final narrative memory system.
- No polished final VFX/audio asset pass, mixing pass, localization, accessibility pass, or broad presentation architecture refactor.
- No scene/prefab changes unless required for minimal placeholder wiring and explicitly classified in evidence.

## Capabilities

### New Capabilities
- `memory-reveal-feedback-placeholder`: Player receives restrained placeholder VFX/audio feedback after an accepted Memory Fragment reveal/collect outcome, while presentation remains downstream of memory truth.

### Modified Capabilities
- None.

## Impact

- Affected systems:
  - Presentation / VFX / Audio placeholder response
  - Read-only accepted memory reveal/result consumption
  - Debug/evidence capture for reveal feedback readability
- Dependencies:
  - S3-2 Memory Fragment interaction path and evidence
  - S3-3 interaction prompt placeholder remains unchanged
  - Existing `MemoryState`, `MemoryInteractionService`, and memory VFX presentation conventions
- M0/M1 loop impact:
  - Improves readability for `approach -> interact -> reveal feedback`.
  - Does not change M0 combat loop behavior or S3-2 interaction truth.
- Ownership boundary affected:
  - Presentation/VFX/Audio observes accepted memory reveal/result context but must not own or mutate `MemoryState`, `MemoryInteractionService`, input callbacks, or fragment runtime truth.
