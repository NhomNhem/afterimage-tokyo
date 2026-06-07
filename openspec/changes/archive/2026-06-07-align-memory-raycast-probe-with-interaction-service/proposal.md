## Why

S3/S4 evidence repeatedly classifies `MemoryRaycastProProbe` as a debug mismatch: gameplay interaction succeeds through `MemoryInteractionService`, while the probe can log `hitName=None` and confuse smoke evidence. This is a good gameplay/debug slice because it improves player-facing QA readability without moving memory truth out of the service.

## What Changes

- Align `MemoryRaycastProProbe` debug output with the same eligible-fragment context used by `MemoryInteractionService`, or formally mark the probe as non-truth debug evidence if direct alignment is not viable.
- Preserve `MemoryInteractionService` as the interaction orchestration and eligibility authority.
- Preserve `MemoryState` as reveal/collect truth.
- Keep the probe presentation/debug-only; it must not decide interaction validity or execute Interact.
- Add focused tests/evidence comparing probe debug classification against service eligibility.
- Preserve existing prompt, accepted Interact, reveal feedback, runtime memory log, and duplicate/spam behavior.

## Capabilities

### New Capabilities

- `memory-raycast-probe-alignment`: Debug probe alignment for memory interaction evidence, keeping `MemoryInteractionService` as gameplay truth.

### Modified Capabilities

- None. Existing memory interaction, prompt, reveal feedback, runtime log, and memory truth behavior remain unchanged.

## Impact

- Affected code:
  - `MemoryRaycastProProbe`
  - focused memory/debug tests or source guardrails
  - possible evidence/story docs for S4-7
- Affected systems:
  - M1 memory interaction debug evidence
  - PlayMode smoke observability
- Ownership boundary:
  - `MemoryInteractionService` owns eligible interaction orchestration.
  - `MemoryState` owns reveal/collect truth.
  - `MemoryRaycastProProbe` remains debug-only and never owns gameplay truth.
- M0/M1 loop impact:
  - Behavior-preserving. The `Interact -> MemoryInteractionService -> MemoryState -> prompt/reveal/log` path must remain unchanged.

## Non-goals

- No MemoryInteractionService behavior change unless explicitly required and covered by a separate approved spec.
- No MemoryState acceptance/rejection or duplicate policy change.
- No input architecture refactor.
- No prompt, reveal feedback, runtime memory log, CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, camera, R3, or MessagePipe refactor.
- No broad scene discovery, Service Locator, `Resources.Load`, or direct `UnityEngine.Debug.*`.
- No full interaction system rewrite.
