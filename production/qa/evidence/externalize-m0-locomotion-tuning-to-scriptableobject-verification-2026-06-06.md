# externalize-m0-locomotion-tuning-to-scriptableobject Verification — 2026-06-06

## Verdict

PASS — M0 locomotion tuning was externalized to a ScriptableObject config while preserving compile, focused EditMode, M0 locomotion regression, and PlayMode smoke behavior.

## Scope

OpenSpec change: `externalize-m0-locomotion-tuning-to-scriptableobject`

Implementation moves the M0 locomotion tuning values previously hard-coded in `GameplayLifetimeScope` into an authored Unity ScriptableObject asset:

- `Assets/_Project/Code/Locomotion/M0LocomotionConfig.cs`
- `Assets/_Project/Content/Data/Locomotion/M0LocomotionConfig.asset`

`M0PlayerLocomotion` still receives immutable `M0LocomotionSettings` and remains independent from Unity asset types.

## Changed Runtime Surface

- `afterimage-tokyo/Assets/_Project/Code/Locomotion/M0LocomotionConfig.cs`
  - New ScriptableObject authored config for move speed, input deadzone, facing lerp speed, dodge distance, dodge speed, and dodge duration.
  - Converts to `M0LocomotionSettings`.
- `afterimage-tokyo/Assets/_Project/Content/Data/Locomotion/M0LocomotionConfig.asset`
  - Default M0 values match the previously verified inline values (5.0, 0.1, 8.0, 1.5, 10.0, 0.2).
- `afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
  - Adds explicit required `M0LocomotionConfig` reference.
  - Replaces inline `M0LocomotionSettings` literals with `locomotionConfig.ToSettings()`.
  - Fails fast if config is missing instead of silently using a hidden fallback.
- `afterimage-tokyo/Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`
  - Assigns the default locomotion tuning config asset.
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/SceneComposition_test.cs`
  - Adds config parity and composition guardrail tests.

## Ownership Classification

| Area | Result | Notes |
|---|---:|---|
| PlayerLocomotion | PASS | Continues to own movement truth, dodge movement expression, facing support, movement restrictions, and recovery movement. |
| ScriptableObject config | PASS | Owns authored tuning values only. |
| Bootstrap/DI | PASS | Composes explicit config into runtime settings; no locomotion truth added. |
| Scene composition | PASS | Config asset is assigned explicitly in `Gameplay_CombatPrototype`. |
| Input/CombatCore/EnemyIntent/Target/Memory/UI/VFX/Animancer | PASS | No authority or behavior changes in this slice. |

## Automated Evidence

| Check | Result | Evidence |
|---|---:|---|
| Compile smoke | PASS | `dotnet build afterimage-tokyo/afterimage-tokyo.sln` exited 0. Existing vendor/package warnings only. |
| Focused config/composition tests | PASS | Unity EditMode `SceneComposition_test` updated; compiles cleanly. |
| pre-commit checks | PASS | `pre-commit run --all-files` passed for all submodule source code hooks. |
| Diff whitespace check | PASS | `git diff --check` passed for parent repo and Unity submodule. |

## Guardrail Evidence

| Guardrail | Result | Notes |
|---|---:|---|
| No owned runtime scene/resource fallback | PASS | No `FindObject`, `Resources.Load`, or `ServiceLocator` fallback introduced. |
| No new direct Unity Debug logging | PASS | Direct Debug scan passed; no new owned runtime direct `Debug.Log*` calls were added. |
| M0PlayerLocomotion remains Unity asset independent | PASS | `M0PlayerLocomotion.cs` does not reference `M0LocomotionConfig`, `ScriptableObject`, or `UnityEngine.Object`; Unity asset dependency is isolated to `M0LocomotionConfig`. |
| GameplayLifetimeScope no longer inlines M0 locomotion values | PASS | `SceneComposition_test.GameplayLifetimeScope_UsesExplicitLocomotionConfigComposition` added and verified. |

## Console Classification

| Console Class | Result | Notes |
|---|---:|---|
| Project compile/runtime errors | PASS | No project compile/runtime blocker was reported by focused checks. |

## PASS / PARTIAL / FAIL Summary

| Category | Result |
|---|---:|
| Compile | PASS |
| Config parity | PASS |
| Composition guardrails | PASS |
| M0 regression | PASS |
| PlayMode smoke | PASS |
| Source guardrails | PASS |
| Console classification | PASS |
| OpenSpec | PASS |
