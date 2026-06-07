## Why

After extracting scene composition and memory runtime tuning, `GameplayLifetimeScope` still contains the inline factories and VContainer registrations for M0 runtime services. This keeps the root scope harder to scan and mixes high-level composition order with service-construction details.

This change continues the same behavior-preserving refactor direction: keep `GameplayLifetimeScope` as the root, but move runtime service factory/registration detail into a small Bootstrap-owned collaborator.

## What Changes

- Add a Bootstrap-owned runtime service composition factory/registrar for the remaining manually constructed M0 services.
- Move manual registration details for `M0CombatCore`, `M0PlayerLocomotion`, `M0MemoryState`, and `M0MemoryVFXResponse` out of `GameplayLifetimeScope`.
- Keep `GameplayLifetimeScope` responsible for high-level composition order, generated NhemDI registration, explicit config references, and scene registrar invocation.
- Preserve existing service lifetimes, interfaces, settings conversion, logger dependency, and behavior.
- Keep authored ScriptableObject configs as static tuning sources only.
- Add/update source composition tests and focused regressions proving no gameplay truth moved into Bootstrap.

## Capabilities

### New Capabilities

- `m0-runtime-service-composition-factory`: Bootstrap-owned factory/registrar that composes manually constructed M0 runtime services from explicit authored configs while preserving gameplay ownership boundaries.

### Modified Capabilities

- None. Existing runtime composition, combat, locomotion, memory interaction, memory VFX, and runtime log behavior remain unchanged.

## Impact

- Affected code:
  - `GameplayLifetimeScope`
  - new Bootstrap runtime service composition collaborator
  - source/scene composition tests
- Affected systems:
  - Bootstrap/DI composition
  - CombatCore registration
  - PlayerLocomotion registration
  - MemoryState registration
  - MemoryVFXResponse registration
- Ownership boundary:
  - Bootstrap owns construction and registration only.
  - CombatCore remains combat truth.
  - PlayerLocomotion remains movement truth.
  - MemoryState remains memory truth.
  - Presentation/VFX/log remain downstream.
- M0 loop impact:
  - Behavior-preserving only. The `read -> evade/parry -> counter -> reveal` loop must remain unchanged.

## Non-goals

- No CombatCore state machine refactor.
- No PlayerLocomotion movement behavior change.
- No MemoryState, MemoryInteractionService, Memory VFX response, prompt, or runtime log behavior change.
- No lifetime changes unless tests prove exact parity.
- No R3/MessagePipe migration.
- No broad NhemDI migration of manual factory special cases.
- No scene/prefab redesign.
- No direct `UnityEngine.Debug.*`, Service Locator, `FindObject*`, broad `FindObjectsByType`, or `Resources.Load`.
