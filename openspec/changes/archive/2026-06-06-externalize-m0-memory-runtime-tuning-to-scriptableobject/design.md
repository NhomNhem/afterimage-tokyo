## Context

`GameplayLifetimeScope` has already been reduced by moving scene component registration and post-build wiring into `M0SceneCompositionRegistrar`. It still manually constructs memory runtime services with hardcoded values:

- `M0MemoryState("M0RevealCandidate")`
- `M0MemoryVFXResponse(0.25f, 0f, "standard")`

Those values are authored tuning/configuration, not gameplay truth. Keeping them inline makes the composition root harder to scan and prevents designers from safely tuning memory reveal defaults through an asset.

This change is intentionally narrower than a memory architecture rewrite. It only externalizes composition-time memory runtime tuning while preserving all M0/S4 behavior.

## Goals / Non-Goals

**Goals:**

- Introduce a small ScriptableObject config for M0 memory runtime tuning.
- Move hardcoded memory candidate id, reveal feedback duration, cooldown duration, and intensity label out of `GameplayLifetimeScope`.
- Keep behavior-preserving defaults equivalent to current runtime values.
- Keep `GameplayLifetimeScope` responsible for validating the assigned config and registering the runtime services.
- Preserve MemoryState, MemoryInteractionService, Memory VFX response, runtime log, prompt, and duplicate interaction behavior.
- Add tests/evidence proving the config is explicit and does not introduce broad lookup, direct Unity debug logging, or presentation gameplay authority.

**Non-Goals:**

- No rewrite of `M0MemoryState`, `MemoryInteractionService`, `M0MemoryVFXResponse`, runtime memory log, prompt, or reveal feedback behavior.
- No changes to reveal acceptance/rejection, duplicate handling, cooldown policy, or interaction eligibility.
- No scene/prefab redesign beyond assigning the new config asset if needed.
- No CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, input routing, R3, or MessagePipe refactor.
- No broad NhemDI migration or removal of the remaining documented manual factory registrations.

## Decisions

### Decision: Add `M0MemoryRuntimeTuningConfig` as a Bootstrap/Memory authored ScriptableObject

The config should be an authored asset with the current runtime defaults:

- default reveal candidate id: `M0RevealCandidate`
- reveal feedback duration seconds: `0.25`
- reveal feedback cooldown seconds: `0`
- reveal feedback intensity label: `standard`

Rationale: these values are composition-time defaults and are already authored-style tuning. A ScriptableObject matches the existing combat and locomotion tuning direction and keeps values visible in the `GameplayLifetimeScope` inspector.

Alternative considered: keep constants in `GameplayLifetimeScope`. Rejected because it keeps the scope noisier and hides memory tuning from the inspector.

### Decision: Keep runtime service construction in `GameplayLifetimeScope`

`GameplayLifetimeScope` should keep creating `M0MemoryState` and `M0MemoryVFXResponse` from the config during composition.

Rationale: this preserves current lifetime ownership and avoids pretending that a ScriptableObject is runtime truth. The SO is data; the runtime services still own state and behavior.

Alternative considered: make the ScriptableObject create services directly. Rejected because it would mix authored data with factory/composition behavior and make testing/ownership fuzzier.

### Decision: Validate config assignment explicitly

If the memory runtime tuning config is missing, composition should fail clearly with a setup error, consistent with combat/locomotion config validation.

Rationale: a missing required runtime config should not silently create fallback behavior or perform resource lookup.

Alternative considered: auto-load a default asset via `Resources.Load`. Rejected because it violates project composition guardrails.

### Decision: Preserve scene composition registrar boundaries

`M0SceneCompositionRegistrar` should remain focused on explicit scene components and post-build wiring. Memory tuning config belongs in the root scope alongside other authored runtime config fields.

Rationale: the registrar handles scene references; the memory config is authored data used for service construction.

## Risks / Trade-offs

- [Risk] Missing config assignment can block PlayMode startup.
  - Mitigation: create a default asset and source/scene composition tests proving it is assigned.

- [Risk] Tuning defaults accidentally drift from current behavior.
  - Mitigation: test default values and rerun memory/runtime-log regression tests.

- [Risk] ScriptableObject is mistaken for runtime truth.
  - Mitigation: spec and tests must assert config contains static tuning only and runtime collected/revealed truth remains in `MemoryState`.

- [Risk] Inspector becomes busy again.
  - Mitigation: place the config in the existing `Configs` or `Memory System` group and keep registrar scene references separate.

## Migration Plan

1. Add `M0MemoryRuntimeTuningConfig`.
2. Create a default asset with current hardcoded values.
3. Add a serialized config reference to `GameplayLifetimeScope`.
4. Replace inline memory service constructor values with config-derived settings.
5. Update scene/source composition tests and focused memory regression tests.
6. Record evidence and archive only after compile, tests, console classification, and manual/PlayMode smoke pass.

Rollback is straightforward: restore the inline constructor values and remove the serialized config reference before archive/commit.

## Open Questions

- Should the config asset live under `Assets/_Project/Content/Data/Memory/` to match combat/locomotion data layout? Recommended: yes.
- Should future memory prompt/log tuning join this same config? Recommended: not in this slice; add only when a concrete duplicated tuning need appears.
