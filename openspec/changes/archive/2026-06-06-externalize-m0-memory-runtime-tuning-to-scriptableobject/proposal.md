## Why

`GameplayLifetimeScope` still owns hardcoded M0 memory runtime tuning values for the default reveal candidate id and memory reveal feedback response timing. Those values are composition/config data, not runtime gameplay truth, so they should move into an authored ScriptableObject to keep the composition root smaller and easier to tune.

This is a low-risk follow-up to the scene composition registrar refactor because it removes hardcoded memory tuning without changing the verified M0/S4 memory interaction path.

## What Changes

- Add an authored M0 memory runtime tuning ScriptableObject for composition-time values currently hardcoded in `GameplayLifetimeScope`.
- Use the authored config to create `M0MemoryState` and `M0MemoryVFXResponse` with behavior-preserving defaults.
- Keep `MemoryState` as reveal/collect truth and `MemoryInteractionService` as interaction orchestration truth.
- Keep `GameplayLifetimeScope` as the root composition owner, but reduce it to config validation/conversion plus registration.
- Add source/scene composition tests proving the memory tuning config is explicit, assigned, and does not introduce broad discovery or presentation authority.
- Preserve S3/S4 verified behavior: prompt, accepted Interact, reveal feedback once, runtime memory log append once, and duplicate/spam Interact behavior.

## Capabilities

### New Capabilities

- `m0-memory-runtime-tuning-scriptableobject`: Authored ScriptableObject composition for M0 memory runtime tuning values used by gameplay scope memory services.

### Modified Capabilities

- None. Existing memory interaction, VFX response, runtime log, and NhemDI composition requirements remain behaviorally unchanged.

## Impact

- Affected code:
  - `GameplayLifetimeScope`
  - new memory tuning ScriptableObject type and asset
  - scene composition tests and focused memory regression tests
- Affected systems:
  - Bootstrap/DI composition
  - MemoryState composition
  - Memory VFX response composition
  - GameplayLifetimeScope inspector authoring
- Ownership boundary:
  - Bootstrap owns composition and config validation.
  - MemoryState remains memory truth.
  - MemoryInteractionService remains interaction orchestration truth.
  - VFX/UI/log presentation remain downstream and do not decide gameplay truth.
- M0 loop impact:
  - Behavior-preserving only. The `read -> evade/parry -> counter -> reveal` loop must remain unchanged.

## Non-goals

- No MemoryState behavior rewrite.
- No MemoryInteractionService behavior change.
- No reveal acceptance, duplicate handling, cooldown, prompt, VFX playback, or runtime log behavior changes.
- No CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, input architecture, R3, or MessagePipe refactor in this slice.
- No scene/prefab redesign beyond assigning the new authored config asset if implementation requires it.
- No broad NhemDI migration or generated registration changes beyond preserving current gameplay scope registration.
- No direct `UnityEngine.Debug.*`, Service Locator, `FindObject*`, broad `FindObjectsByType`, or `Resources.Load`.
