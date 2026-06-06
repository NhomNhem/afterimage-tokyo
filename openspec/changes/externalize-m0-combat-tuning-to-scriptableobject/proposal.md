## Why

`GameplayLifetimeScope` still hard-codes M0 combat timing values while composing `M0CombatCore`. This keeps tuning data inside the DI composition root, makes iteration harder, and adds noise to a file that should focus on runtime composition.

This change externalizes those authored combat timing values into a Unity ScriptableObject while preserving current M0 combat behavior.

## What Changes

- Add an authored `M0CombatTimingConfig` ScriptableObject that stores the current attack, dodge, parry, counter-window, and recovery timing values.
- Convert the ScriptableObject into the existing immutable `M0CombatTimingSettings` value object before constructing `M0CombatCore`.
- Update `GameplayLifetimeScope` to reference the authored config asset instead of hard-coding combat timing literals inline.
- Add tests/guardrails proving the authored default values match the current hard-coded M0 values.
- Preserve `M0CombatCore` ownership of combat validity, timing progression, counter windows, and reveal request context.
- Preserve all current timing values and M0/S4 behavior.

## Capabilities

### New Capabilities

- `m0-combat-tuning-scriptableobject`: Authored ScriptableObject configuration for M0 combat timing values, converted into immutable runtime settings at composition time.

### Modified Capabilities

- None.

## Impact

- Affected code:
  - `afterimage-tokyo/Assets/_Project/Code/Combat/M0CombatTimingSettings.cs`
  - `afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
  - new combat tuning ScriptableObject type under owned project code
  - new or updated default config asset under `Assets/_Project/Content/Data/Configs/` or a combat-owned data folder
  - focused EditMode tests for config parity and composition guardrails

- Ownership boundary affected:
  - CombatCore remains combat truth owner.
  - ScriptableObject owns authored tuning values only.
  - Bootstrap composes the config into `M0CombatCore`; it does not own combat truth.

- M0 loop impact:
  - Behavior-preserving.
  - No changes to `read -> evade/parry -> counter -> reveal` timing, state transitions, outcomes, or memory reveal behavior.

## Non-goals

- No CombatCore state-machine refactor.
- No combat timing value changes.
- No combat validity/result changes.
- No input, locomotion, enemy intent, target context, memory, UI, VFX, or Animancer authority changes.
- No locomotion tuning ScriptableObject in this slice.
- No R3 or MessagePipe migration.
- No broad NhemDI migration.
- No scene discovery fallback, `FindObject*`, `Resources.Load`, Service Locator, or direct `UnityEngine.Debug` logging.
