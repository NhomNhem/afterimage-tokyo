# Verification Evidence: extract-m0-runtime-service-composition-factory

Date: 2026-06-07

## Change Summary

Extracted config-backed M0 runtime service registrations from `GameplayLifetimeScope` into `M0RuntimeServiceCompositionRegistrar`.

Moved manual factory registrations:

- `M0CombatCore`
- `M0PlayerLocomotion`
- `M0MemoryState`
- `M0MemoryVFXResponse`

Preserved in `GameplayLifetimeScope`:

- generated NhemDI gameplay-scope registration
- logger registration
- explicit serialized config references
- scene component registration through `M0SceneCompositionRegistrar`

## Automated Checks

PASS - Baseline focused EditMode tests before implementation:

- `GlassRefrain.Tests.EditMode.SceneComposition_test`
- `GlassRefrain.Tests.EditMode.M0CombatCoreTests`
- `GlassRefrain.Tests.EditMode.M0DefensiveResolutionTests`
- `GlassRefrain.Tests.EditMode.M0PlayerLocomotionTests`
- `GlassRefrain.Tests.EditMode.M0InputRouterTests`
- `GlassRefrain.Tests.EditMode.M0EnemyIntentTests`
- `GlassRefrain.Tests.EditMode.MemoryInteractionServiceTests`
- `GlassRefrain.Tests.EditMode.M0MemoryStateTests`
- `GlassRefrain.Tests.EditMode.M0MemoryVFXResponseTests`
- `GlassRefrain.Tests.EditMode.M1RuntimeMemoryLogPlaceholderTests`
- `GlassRefrain.Tests.EditMode.M1MemoryRevealFeedbackBridgeTests`
- Result: 119/119 passed

PASS - Post-change focused EditMode tests:

- same focused set as baseline plus updated `VContainerRegistry_test`
- Result: 125/125 passed

PASS - Final compact composition check after pruning editor churn:

- `GlassRefrain.Tests.EditMode.SceneComposition_test`
- `GlassRefrain.Tests.EditMode.VContainerRegistry_test`
- Result: 22/22 passed

PASS - PlayMode startup smoke:

- `GlassRefrain.Tests.PlayMode.SceneFoundationTests`
- Result: 2/2 passed

PASS - Script validation:

- `Assets/_Project/Code/Bootstrap/M0RuntimeServiceCompositionRegistrar.cs`
- `Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
- `Assets/_Project/Code/Bootstrap/M0SceneCompositionRegistrar.cs`
- `Assets/_Project/Tests/EditMode/SceneComposition_test.cs`
- `Assets/_Project/Tests/EditMode/VContainerRegistry_test.cs`
- Result: 0 errors, 0 warnings from Unity MCP script validation

PASS - OpenSpec validation:

- `openspec validate extract-m0-runtime-service-composition-factory --strict`
- Result: valid

## Guardrail Checks

PASS - Source guardrail scan over `GameplayLifetimeScope` and `M0RuntimeServiceCompositionRegistrar` found no introduced:

- `FindObjectOfType`
- `FindFirstObjectByType`
- `FindAnyObjectByType`
- `FindObjectsByType`
- `Resources.Load`
- `ServiceLocator`
- direct `UnityEngine.Debug.Log`
- direct `Debug.Log`, `Debug.LogWarning`, or `Debug.LogError`

PASS - Gameplay-truth guardrail scan found no registrar calls to:

- combat request APIs
- locomotion input consumption
- memory interaction commands
- memory reveal evaluation commands
- memory VFX playback authority calls

## Console Classification

PASS - Compile smoke:

- Unity returned to idle after script refresh and domain reload.
- No compile errors were reported for changed scripts.

PARTIAL - Console after final checks:

- Unity reported existing analyzer/plugin warnings as `Exception` entries.
- Entries were outside the changed Bootstrap files, including plugin/vendor paths such as KinematicCharacterController, BroAudio samples, Sirenix Odin Validator, Dark UI, GUPS, Toon shader assets, and VFX/editor sample scripts.
- No console entries pointed at `GameplayLifetimeScope`, `M0RuntimeServiceCompositionRegistrar`, `SceneComposition_test`, or `VContainerRegistry_test`.

## M0/S4 Behavior Classification

PASS - Automated M0 behavior regressions:

- combat and defensive resolution
- locomotion
- input routing
- enemy intent
- memory interaction
- memory state
- memory VFX response
- runtime memory log
- memory reveal feedback bridge

PARTIAL - Hands-on memory interaction smoke:

- PlayMode startup was verified through existing PlayMode tests.
- A full manual controller/keyboard pass for visible eligible prompt, accepted Interact, reveal feedback once, runtime log append once, and duplicate/spam safety was not performed in this session.

## Dirty Asset Classification

Expected Unity project changes:

- `Assets/_Project/Code/Bootstrap/M0RuntimeServiceCompositionRegistrar.cs`
- `Assets/_Project/Code/Bootstrap/M0RuntimeServiceCompositionRegistrar.cs.meta`
- `Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
- `Assets/_Project/Tests/EditMode/SceneComposition_test.cs`
- `Assets/_Project/Tests/EditMode/VContainerRegistry_test.cs`

Expected OpenSpec/evidence changes:

- `openspec/changes/extract-m0-runtime-service-composition-factory/tasks.md`
- `production/qa/evidence/extract-m0-runtime-service-composition-factory-verification-2026-06-07.md`

No scene or ScriptableObject asset changes were required for this slice.

## Deferred Follow-ups

- CombatCore state-machine decomposition remains deferred.
- Generated NhemDI migration for config-backed special-case factories remains deferred.
- R3/MessagePipe composition events remain deferred.
- Further `GameplayLifetimeScope` inspector redesign remains deferred.
