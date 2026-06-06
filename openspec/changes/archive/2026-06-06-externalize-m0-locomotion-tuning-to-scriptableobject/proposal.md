# externalize-m0-locomotion-tuning-to-scriptableobject

## Why

`GameplayLifetimeScope` still composes `M0PlayerLocomotion` with inline `M0LocomotionSettings` values. This keeps authored movement and dodge tuning hidden inside bootstrap code, increases composition noise, and makes iteration harder as M0 tuning grows.

After externalizing M0 combat timing to a ScriptableObject, locomotion tuning is the next small behavior-preserving composition cleanup. The runtime movement truth should stay in `M0PlayerLocomotion`; the asset should only own authored tuning data.

## What Changes

- Add a locomotion-owned ScriptableObject config for M0 locomotion tuning.
- Preserve the current values exactly:
  - move speed: `5.0`
  - input deadzone: `0.1`
  - facing lerp speed: `8.0`
  - dodge distance: `1.5`
  - dodge speed: `10.0`
  - dodge duration seconds: `0.2`
- Convert the authored config into the existing immutable `M0LocomotionSettings` runtime value.
- Update `GameplayLifetimeScope` to use the authored config instead of inline numeric tuning.
- Keep `M0PlayerLocomotion` pure and independent from Unity asset types.
- Add focused parity/composition checks so the change is evidence-backed.

## Capabilities

### New: `m0-locomotion-tuning-scriptableobject`

M0 locomotion movement and dodge tuning can be authored in a Unity ScriptableObject and converted into runtime locomotion settings during gameplay composition.

### Modified

None.

## Impact

- Unity submodule code:
  - `Assets/_Project/Code/Locomotion/M0LocomotionSettings.cs`
  - `Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
  - new locomotion tuning config type under `Assets/_Project/Code/Locomotion/`
- Unity authored data:
  - new default config asset under `Assets/_Project/Content/Data/Locomotion/`
  - gameplay scene reference assignment to the config asset
- Tests/evidence:
  - config-to-runtime parity check
  - gameplay composition check
  - existing locomotion regression coverage
  - compile/source-guardrail evidence

Ownership boundary:

- `PlayerLocomotion` remains the owner of movement truth.
- The ScriptableObject owns authored tuning data only.
- `GameplayLifetimeScope` remains the composition boundary.
- Presentation, camera, VFX, UI, and debug systems must not gain movement authority.

M0 loop impact:

- Behavior-preserving.
- No movement value changes.
- No dodge timing/distance changes.
- No changes to `read -> evade/parry -> counter -> reveal` ownership.

## Non-goals

- No `M0PlayerLocomotion` algorithm rewrite.
- No combat timing/result changes.
- No input architecture refactor.
- No enemy intent, target context, memory, camera, UI, VFX, or Animancer authority changes.
- No runtime mutable tuning during a duel.
- No R3 or MessagePipe migration in this slice.
- No Service Locator, `FindObjectOfType`, `Resources.Load`, or hidden fallback discovery.
- No broad NhemDI migration.
- No direct Unity debug logging.
