# extract-m0-scene-composition-registrar Verification

Date: 2026-06-06
Change: `extract-m0-scene-composition-registrar`
Scope: Behavior-preserving Bootstrap extraction for explicit M0 scene component registration and post-build wiring.

## Summary

`GameplayLifetimeScope` remains the gameplay composition root and keeps high-level generated NhemDI registration plus authored SO-to-settings conversion. Explicit scene component registration and post-build scene wiring were moved into `M0SceneCompositionRegistrar`.

The UI Toolkit inspector remains bound through `rootElement.Bind(serializedObject)`, and the UXML keeps explicit binding paths for gameplay adapters, animation drivers, tuning configs, and memory scene references.

## Verification Table

| Check | Result | Evidence |
| --- | --- | --- |
| C# validate: `M0SceneCompositionRegistrar.cs` | PASS | 0 warnings, 0 errors |
| C# validate: `GameplayLifetimeScope.cs` | PASS | 0 warnings, 0 errors |
| C# validate: `GameplayLifetimeScopeEditor.cs` | PASS | 0 warnings, 0 errors |
| C# validate: `SceneComposition_test.cs` | PASS | 0 warnings, 0 errors |
| C# validate: `M0EnemyIntentTests.cs` | PASS | 0 errors; analyzer reported an existing generic `GetComponent` null-check warning |
| SceneComposition EditMode | PASS | 12/12 passed |
| Memory interaction + runtime log EditMode | PASS | 9/9 passed |
| M0 input/combat/locomotion/enemy intent EditMode | PASS | 48/48 passed |
| PlayMode smoke | PASS | 2/2 passed |
| OpenSpec strict validation | PASS | `openspec validate extract-m0-scene-composition-registrar --strict` |
| Bootstrap source guardrail scan | PASS | No `Debug.Log`, `FindObject*`, broad `FindObjectsByType`, `Resources.Load`, or `ServiceLocator` matches under Bootstrap |
| Console classification | PASS | Final console check: 0 errors, 0 warnings |

## Notes

- A transient Unity Test Runner batch retry was orphaned after domain reload before executing tests. It reported no test failures. The same coverage was rerun in smaller focused batches and passed.
- The old EnemyIntent guardrail test still treated `NhemDangFugBixs.Attributes` as forbidden. That was updated to match the current approved NhemDI attribute-registration direction while still forbidding gameplay/input/presentation dependency leaks.
- Unity changed `ProjectSettings/EditorSettings.asset` during the test session; that unrelated Enter Play Mode setting churn was reverted out of this change.

## PASS/PARTIAL/FAIL

| Area | Status |
| --- | --- |
| Registrar extraction | PASS |
| GameplayLifetimeScope readability | PASS |
| Inspector serialized binding | PASS |
| Behavior-preserving smoke | PASS |
| OpenSpec readiness for archive | PASS |
