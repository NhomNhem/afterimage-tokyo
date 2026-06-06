## Why

`GameplayLifetimeScope` has become easier to read after tuning values moved to ScriptableObjects, but it still mixes several bootstrap concerns in one class: pure service registration, explicit scene component registration, post-build scene wiring, animation warning classification, and memory participant injection.

This change extracts scene component composition into a narrow registrar while preserving `GameplayLifetimeScope` as the composition root and preserving current M0/S4 behavior.

## What Changes

- Add a narrow M0 scene composition registrar/collaborator owned by Bootstrap.
- Move explicit scene component registration and post-build scene wiring out of `GameplayLifetimeScope`.
- Keep all Unity scene references serialized on `GameplayLifetimeScope` or an explicit scene-owned serialized container, with no broad discovery fallback.
- Keep pure/runtime services registered through NhemDI generated registration or documented manual special cases.
- Preserve ScriptableObject tuning composition for combat and locomotion.
- Preserve memory probe/fragment injection behavior and diagnostic output.
- Preserve animation driver registration and presentation adapter wiring.
- Keep behavior-preserving tests/evidence for M0 runtime composition and the M1 memory loop.

## Capabilities

### New Capabilities

- `m0-scene-composition-registrar`: Bootstrap-owned registrar for explicit scene component registration and post-build scene wiring in the M0 gameplay scope.

### Modified Capabilities

- None.

## Impact

- Affected code:
  - `afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
  - new Bootstrap registrar/collaborator type under `Assets/_Project/Code/Bootstrap/`
  - focused EditMode tests for scene composition guardrails
  - evidence file for behavior-preserving composition extraction
- Affected editor UX:
  - `GameplayLifetimeScope` inspector must continue showing all serialized references clearly.
  - UI Toolkit editor can remain, but it must bind existing serialized fields correctly.
- Ownership boundary affected:
  - Bootstrap/DI owns scene composition only.
  - CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, MemoryState, MemoryInteraction, Presentation, and DebugOverlay ownership stay unchanged.
- M0 loop impact:
  - Behavior-preserving.
  - No changes to `read -> evade/parry -> counter -> reveal` timing, validity, memory reveal, prompt, runtime log, or duplicate interaction behavior.

## Non-goals

- No CombatCore state-machine refactor.
- No PlayerLocomotion movement refactor.
- No input architecture refactor.
- No MemoryState or MemoryInteractionService behavior changes.
- No scene/prefab hierarchy redesign.
- No broad NhemDI migration beyond using the existing generated gameplay-scope registration hook.
- No R3 or MessagePipe migration in this slice.
- No Service Locator, `FindObjectOfType`, `FindFirstObjectByType`, `FindAnyObjectByType`, broad `FindObjectsByType`, or `Resources.Load`.
- No direct Unity debug logging in owned runtime/editor code.
- No gameplay tuning value changes.
