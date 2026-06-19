# S8-8 Evidence — Decompose PlayerStateMachine

**Status**: PASS
**Date**: 2026-06-17
**Implementer**: unity-specialist

## Implementation Summary

### Files Created
- `Assets/_Project/Code/Application/CombatStateMachine.cs`
- `Assets/_Project/Code/Application/LocomotionStateMachine.cs`
- `Assets/_Project/Code/Application/PlayerStateResolver.cs`

### Files Deleted
- `Assets/_Project/Code/Application/PlayerStateMachine.cs`
- `Assets/_Project/Code/Application/PlayerStateMachineFactory.cs`

### Files Modified
- `Assets/_Project/Code/Bootstrap/M0SceneCompositionRegistrar.cs`
- `Assets/_Project/Tests/PlayMode/M0PlayerStateMachineDodgeTests.cs`
- `Assets/_Project/Tests/EditMode/GlassRefrain.Tests.EditMode.asmdef`

### Test File
- `Assets/_Project/Tests/EditMode/M0StateMachineDecompositionTests.cs` — 8 tests

## Target Architecture

```
M0CombatCore ──→ CombatStateMachine ──┐
                                      ├── PlayerStateResolver ──→ IPlayerStateMachine
IM0PlayerLocomotion ──→ LocomotionStateMachine ─┘
                            ↑
                        GroundState (Idle/Moving/Restricted/Recovering)
```

## Test Results

| Suite | Tests | Result |
|-------|-------|--------|
| M0StateMachineDecompositionTests (EditMode) | 8/8 | PASS |
| M0PlayerStateMachineDodgeTests (PlayMode) | 3/3 | PASS (updated constructor) |

## Acceptance Criteria

| AC | Status | Notes |
|----|--------|-------|
| CombatStateMachine compiles, observes CombatCore | ✅ | Maps CombatCoreState → PlayerState |
| LocomotionStateMachine with GroundState | ✅ | GroundState: Idle/Moving/Restricted/Recovering |
| PlayerStateResolver priority merge | ✅ | Same logic as old ResolvePlayerState |
| IPlayerStateMachine unchanged | ✅ | No upstream consumer changes |
| M0SceneCompositionRegistrar updated | ✅ | Resolver via new 3-class chain |
| Action lock + recovery preserved | ✅ | Same aggregation in resolver |
| CreateDebugSnapshot format preserved | ✅ | Verified by test |
| All EditMode tests pass | ✅ | Full suite PASS |
| M0PlayerStateMachineDodgeTests pass | ✅ | Updated for new constructor |
| No new compile warnings | ✅ | Clean build |

## Deviations from Scope
- `PlayerStateResolver` does not dispose child machines in `Dispose()` — DI container handles lifetime
- Exposes `HasCore` / `HasLocomotion` properties for clean degraded-mode detection
