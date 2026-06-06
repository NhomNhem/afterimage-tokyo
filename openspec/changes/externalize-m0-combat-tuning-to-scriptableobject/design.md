## Context

`GameplayLifetimeScope` currently constructs `M0CombatCore` with inline `M0CombatTimingSettings` literals. The values are authored tuning data, but they live in the composition root, making the scope longer and mixing DI wiring with combat feel iteration.

The existing runtime boundary is useful: `M0CombatCore` receives an immutable `M0CombatTimingSettings` value object and owns all combat timing progression and combat validity. This change keeps that runtime shape and moves only authored values into a Unity ScriptableObject.

## Goals / Non-Goals

**Goals:**

- Move M0 combat timing tuning values out of `GameplayLifetimeScope`.
- Provide a Unity-authored ScriptableObject asset for attack, dodge, parry, counter-window, and recovery timing.
- Convert authored values into `M0CombatTimingSettings` before constructing `M0CombatCore`.
- Preserve current timing values and M0 combat behavior.
- Keep `M0CombatCore` pure from Unity asset dependencies.
- Add tests/guardrails proving parity and preventing timing literals from returning to `GameplayLifetimeScope`.

**Non-Goals:**

- No CombatCore state-machine rewrite.
- No timing value changes.
- No locomotion, enemy intent, memory, input, target, UI, VFX, Animancer, R3, or MessagePipe changes.
- No runtime mutable tuning during a duel.
- No broad asset lookup via `Resources.Load`, Service Locator, or scene discovery fallback.

## Decisions

### Decision: Use ScriptableObject only as authored config

Create a `M0CombatTimingConfig : ScriptableObject` that stores serialized float values and exposes a conversion method to `M0CombatTimingSettings`.

Rationale:

- Designers can inspect and adjust timing values in Unity.
- Domain/runtime code continues to receive the existing immutable settings value object.
- Combat truth remains in `M0CombatCore`; the asset does not own timing progression or combat decisions.

Alternative considered: inject the ScriptableObject directly into `M0CombatCore`.

- Rejected because it would leak Unity infrastructure into combat runtime logic.

### Decision: Keep `GameplayLifetimeScope` as the composition bridge

`GameplayLifetimeScope` should serialize a required config reference and pass `combatTimingConfig.ToSettings()` into the existing `M0CombatCore` factory.

Rationale:

- This is the smallest behavior-preserving change.
- It avoids a broad DI or NhemDI migration in the same slice.
- It keeps scene/prefab assignment explicit and compatible with the recently archived runtime composition hardening.

Alternative considered: auto-register the config through NhemDI.

- Deferred because ScriptableObject asset registration requires explicit Unity asset instance selection. NhemDI registration remains preferred for pure/runtime services, while authored Unity assets are explicit composition inputs.

### Decision: Preserve exact current gameplay values

The default config asset must match the current `GameplayLifetimeScope` inline M0 values:

- attack startup: `0.14`
- attack active: `0.20`
- attack recovery: `0.26`
- dodge startup: `0.09`
- dodge active: `0.20`
- dodge recovery: `0.24`
- parry startup: `0.10`
- parry active: `0.18`
- parry recovery: `0.24`
- counter window duration: `3.0`
- recovery duration: `0.24`

Rationale:

- This is a maintainability refactor only.
- Any timing changes require separate design approval and evidence.

### Decision: Missing config is a setup issue

The implementation should make a missing config visible through existing validation/test evidence and project logging where appropriate. It must not silently create a hidden fallback that changes runtime tuning.

Rationale:

- Silent fallback would hide scene/config drift.
- Existing M0 evidence depends on known tuning values.

## Risks / Trade-offs

- [Risk] Config asset is not assigned in the gameplay scene -> Mitigation: required serialized field, scene composition test, and console classification.
- [Risk] Default asset values drift from current inline values -> Mitigation: EditMode parity test against expected values.
- [Risk] CombatCore starts depending on Unity assets -> Mitigation: keep the conversion boundary in Bootstrap/config and keep `M0CombatCore` constructor unchanged.
- [Risk] This does not reduce all `GameplayLifetimeScope` length -> Mitigation: this is one thin slice; scene component registration extraction remains a later change.

## Migration Plan

1. Add `M0CombatTimingConfig` ScriptableObject type.
2. Create a default M0 combat timing asset with current inline values.
3. Assign the asset to `GameplayLifetimeScope` in `Gameplay_CombatPrototype`.
4. Replace inline `M0CombatTimingSettings` construction in `GameplayLifetimeScope` with `combatTimingConfig.ToSettings()`.
5. Add focused tests for config parity and composition guardrails.
6. Run compile, focused EditMode tests, M0 defensive regression, PlayMode smoke, OpenSpec validation, and console classification.

Rollback strategy:

- Restore the previous inline `M0CombatTimingSettings` factory and remove the scene asset assignment if the config boundary causes setup issues.

## Open Questions

- None for this slice.
