## Context

`GameplayLifetimeScope` currently constructs `M0PlayerLocomotion` with inline `M0LocomotionSettings` literals. Those values are authored movement and dodge tuning data, but they live inside the composition root. This keeps the scope longer and mixes DI wiring with moment-to-moment movement feel iteration.

The useful runtime boundary already exists: `M0PlayerLocomotion` receives an immutable `M0LocomotionSettings` value object and owns movement truth. This change keeps that runtime shape and moves only authored values into a Unity ScriptableObject.

## Goals / Non-Goals

**Goals:**

- Move M0 locomotion tuning values out of `GameplayLifetimeScope`.
- Provide a Unity-authored ScriptableObject asset for move speed, input deadzone, facing lerp speed, dodge distance, dodge speed, and dodge duration.
- Convert authored values into `M0LocomotionSettings` before constructing `M0PlayerLocomotion`.
- Preserve current locomotion values and M0 movement behavior.
- Keep `M0PlayerLocomotion` pure from Unity asset dependencies.
- Add tests/guardrails proving parity and preventing locomotion tuning literals from returning to `GameplayLifetimeScope`.

**Non-Goals:**

- No `M0PlayerLocomotion` movement algorithm rewrite.
- No locomotion tuning value changes.
- No combat, enemy intent, memory, input, target, UI, VFX, Animancer, R3, or MessagePipe changes.
- No runtime mutable tuning during a duel.
- No broad asset lookup via `Resources.Load`, Service Locator, or scene discovery fallback.

## Decisions

### Decision: Use ScriptableObject only as authored config

Create a locomotion-owned ScriptableObject that stores serialized locomotion tuning values and exposes a conversion method to `M0LocomotionSettings`.

Rationale:

- Designers can inspect and adjust locomotion tuning in Unity.
- Runtime code continues to receive the existing immutable settings value object.
- Movement truth remains in `M0PlayerLocomotion`; the asset does not apply movement, decide restrictions, or express dodge movement.

Alternative considered: inject the ScriptableObject directly into `M0PlayerLocomotion`.

- Rejected because it would leak Unity infrastructure into pure locomotion runtime logic.

### Decision: Keep `GameplayLifetimeScope` as the composition bridge

`GameplayLifetimeScope` should serialize a required config reference and pass `locomotionSettingsConfig.ToSettings()` into the existing `M0PlayerLocomotion` factory.

Rationale:

- This is the smallest behavior-preserving change.
- It avoids a broad DI or NhemDI migration in the same slice.
- It keeps scene/prefab asset selection explicit.

Alternative considered: auto-register the config through NhemDI.

- Deferred because ScriptableObject asset registration still requires explicit Unity asset instance selection. NhemDI remains preferred for pure/runtime services, while authored Unity assets stay explicit composition inputs.

### Decision: Preserve exact current gameplay values

The default config asset must match the current inline M0 locomotion values:

- move speed: `5.0`
- input deadzone: `0.1`
- facing lerp speed: `8.0`
- dodge distance: `1.5`
- dodge speed: `10.0`
- dodge duration seconds: `0.2`

Rationale:

- This is a maintainability refactor only.
- Any movement feel changes require separate design approval and evidence.

### Decision: Missing config is a setup issue

The implementation should make a missing config visible through existing validation/test evidence and project logging where appropriate. It must not silently create a hidden fallback that changes runtime tuning.

Rationale:

- Silent fallback would hide scene/config drift.
- Existing M0 evidence depends on known movement and dodge values.

## Risks / Trade-offs

- [Risk] Config asset is not assigned in the gameplay scene -> Mitigation: required serialized field, scene composition test, and console classification.
- [Risk] Default asset values drift from current inline values -> Mitigation: EditMode parity test against expected values.
- [Risk] `M0PlayerLocomotion` starts depending on Unity assets -> Mitigation: keep the conversion boundary in Bootstrap/config and keep the runtime constructor pure.
- [Risk] This does not reduce all `GameplayLifetimeScope` length -> Mitigation: this is one thin slice; scene component registration extraction remains a later change.

## Migration Plan

1. Add the M0 locomotion tuning ScriptableObject type.
2. Create a default M0 locomotion tuning asset with current inline values.
3. Assign the asset to `GameplayLifetimeScope` in `Gameplay_CombatPrototype`.
4. Replace inline `M0LocomotionSettings` construction in `GameplayLifetimeScope` with config conversion.
5. Add focused tests for config parity and composition guardrails.
6. Run compile, focused EditMode tests, locomotion regression, PlayMode smoke, OpenSpec validation, and console classification.

Rollback strategy:

- Restore the previous inline `M0LocomotionSettings` factory and remove the scene asset assignment if the config boundary causes setup issues.

## Open Questions

- None for this slice.
