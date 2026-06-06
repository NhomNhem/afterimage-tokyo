# externalize-m0-combat-tuning-to-scriptableobject Verification — 2026-06-06

## Verdict

PASS — M0 combat timing was externalized to a ScriptableObject config while preserving compile, focused EditMode, M0 defensive regression, and PlayMode smoke behavior.

## Scope

OpenSpec change: `externalize-m0-combat-tuning-to-scriptableobject`

Implementation moves the M0 combat timing values previously hard-coded in `GameplayLifetimeScope` into an authored Unity ScriptableObject asset:

- `Assets/_Project/Code/Combat/M0CombatTimingConfig.cs`
- `Assets/_Project/Content/Data/Combat/M0CombatTimingConfig.asset`

`M0CombatCore` still receives immutable `M0CombatTimingSettings` and remains independent from Unity asset types.

## Changed Runtime Surface

- `afterimage-tokyo/Assets/_Project/Code/Combat/M0CombatTimingConfig.cs`
  - New ScriptableObject authored config for attack, dodge, parry, counter-window, and recovery timings.
  - Converts to `M0CombatTimingSettings`.
- `afterimage-tokyo/Assets/_Project/Content/Data/Combat/M0CombatTimingConfig.asset`
  - Default M0 values match the previously verified inline values.
- `afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
  - Adds explicit required `M0CombatTimingConfig` reference.
  - Replaces inline `M0CombatTimingSettings` literals with `combatTimingConfig.ToSettings()`.
  - Fails fast if config is missing instead of silently using a hidden fallback.
- `afterimage-tokyo/Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`
  - Assigns the default combat timing config asset.
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/SceneComposition_test.cs`
  - Adds config parity and composition guardrail tests.

## Ownership Classification

| Area | Result | Notes |
|---|---:|---|
| CombatCore | PASS | Continues to own combat validity, timing progression, counter windows, hit resolution, and reveal request context. |
| ScriptableObject config | PASS | Owns authored tuning values only. |
| Bootstrap/DI | PASS | Composes explicit config into runtime settings; no combat truth added. |
| Scene composition | PASS | Config asset is assigned explicitly in `Gameplay_CombatPrototype`. |
| Input/Locomotion/EnemyIntent/Target/Memory/UI/VFX/Animancer | PASS | No authority or behavior changes in this slice. |

## Automated Evidence

| Check | Result | Evidence |
|---|---:|---|
| Baseline M0 defensive regression | PASS | Unity MCP EditMode `M0DefensiveResolutionTests`: 23/23 passed before implementation. |
| Compile smoke | PASS | `dotnet build afterimage-tokyo/afterimage-tokyo.sln --no-restore -v:quiet` exited 0. Existing vendor/package warnings only. |
| Focused config/composition tests | PASS | Unity MCP EditMode `SceneComposition_test`: 7/7 passed. |
| M0 defensive regression after refactor | PASS | Unity MCP EditMode `M0DefensiveResolutionTests`: 23/23 passed. |
| PlayMode smoke | PASS | Unity MCP PlayMode suite: 2/2 passed. |
| OpenSpec strict validation | PASS | `openspec validate externalize-m0-combat-tuning-to-scriptableobject --strict` passed. |
| Diff whitespace check | PASS | `git diff --check` passed for parent repo and Unity submodule. |

## Guardrail Evidence

| Guardrail | Result | Notes |
|---|---:|---|
| No owned runtime scene/resource fallback | PASS | `rg "FindObject|FindFirstObject|FindAnyObject|FindObjectsByType|Resources\\.Load|ServiceLocator" Assets/_Project/Code -g "*.cs"` returned no matches. |
| No new direct Unity Debug logging | PASS WITH NOTES | Direct Debug scan only matched generated `M0InputActions.cs` comments/assert. No new owned runtime direct `Debug.Log*` calls were added. |
| CombatCore remains Unity asset independent | PASS | `M0CombatCore.cs` does not reference `M0CombatTimingConfig`, `ScriptableObject`, or `UnityEngine`; Unity asset dependency is isolated to `M0CombatTimingConfig`. |
| GameplayLifetimeScope no longer inlines M0 timing values | PASS | `SceneComposition_test.GameplayLifetimeScope_UsesExplicitCombatTimingConfigComposition` passed. |

## Console Classification

| Console Class | Result | Notes |
|---|---:|---|
| Project compile/runtime errors | PASS | No project compile/runtime blocker was reported by focused checks. |
| Unity Test Runner artifacts | PASS WITH NOTES | Console contained Unity Test Runner result-save output and `Unity.PerformanceTesting.Editor.TestRunBuilder` cleanup warning; classified as test framework noise, not project runtime failure. |

## PASS / PARTIAL / FAIL Summary

| Category | Result |
|---|---:|
| Compile | PASS |
| Config parity | PASS |
| Composition guardrails | PASS |
| M0 regression | PASS |
| PlayMode smoke | PASS |
| Source guardrails | PASS |
| Console classification | PASS WITH NOTES |
| OpenSpec | PASS |

## Working Tree Note

The Unity submodule also shows unrelated staged/dirty Enemy/Health interface extraction files that are outside this OpenSpec slice. They were not modified for this change and should be reviewed/staged separately from the combat tuning ScriptableObject slice.

## Follow-Up

Ready for review and archive after scoped staging/commit. Deferred follow-up slices remain:

- externalize M0 locomotion tuning to ScriptableObject
- extract M0 scene component registration out of `GameplayLifetimeScope`
- introduce R3 read-only debug/tuning observation only where needed
- introduce MessagePipe events only for confirmed cross-system domain events
