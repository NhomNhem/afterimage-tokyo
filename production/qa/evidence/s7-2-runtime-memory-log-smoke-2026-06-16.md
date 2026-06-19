# S7-2 M1 Runtime Memory Log Smoke

Captured on: 2026-06-16
Change: `player-state-machine-integration`
Sprint: `production/sprints/sprint-7.md`

## Summary

S7-2 verifies the full EditMode test suite passes after PlayerStateMachine integration, including the M1 runtime memory log path tests. The PlayerStateMachine involved refactoring `M0InputRouter`, `M0AnimationPresentationAdapter`, and `M0GameplayTickHandler` — all upstream of the memory log path.

Additionally, this evidence documents the fix for 60 pre-existing NullReferenceException failures in the EditMode test suite caused by `SnapshotChanged?.Invoke()` being invoked when no subscriber had yet been attached.

## Automated Evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Full EditMode test suite | PASS | 265/265 passed, 0 failed, 0 skipped. Duration 0.72s. Results: `Logs/TestResults-EditMode-Final.xml` |
| NhemBootstrap Tests | PASS | 13/13 passed. |
| GlassRefrain EditMode Tests | PASS | 252/252 passed. |
| AnimatorPresentationOnlyTests | PASS | 18/18 passed. |
| M0DebugOverlaySnapshotIntegration | PASS | 6/6 passed. |
| M0InputRouterTests | PASS | 5/5 passed. |
| M0MemoryStateTests | PASS | 12/12 passed. |
| M0PlayerStateMachineDodgeTests | PASS | PlayMode test (requires Scene), run separately. |
| M1MemoryRevealFeedbackBridgeTests | PASS | 6/6 passed. |
| M1RuntimeMemoryLogPlaceholderTests | PASS | 6/6 passed. |

## Fixes Applied

Three files had `SnapshotChanged` event invoked without null check in `RefreshSnapshot()` constructor path:

| File | Line | Fix |
| --- | --- | --- |
| `Assets/_Project/Code/Input/M0InputRouter.cs` | `RefreshSnapshot()` @ L181 | `SnapshotChanged?.Invoke(latestSnapshot)` |
| `Assets/_Project/Code/Health/M0HealthDamageReactionModel.cs` | `RefreshSnapshot()` @ L94 | `SnapshotChanged?.Invoke(latestSnapshot)` |
| `Assets/_Project/Code/Memory/M0MemoryState.cs` | `RefreshSnapshot()` @ L173 | `SnapshotChanged?.Invoke(latestSnapshot)` |

One test had `AmbiguousMatchException` due to `PlayLocomotion` interface overload:

| File | Line | Fix |
| --- | --- | --- |
| `Tests/EditMode/AnimatorPresentationOnly_test.cs` | L83 | `GetMethods().Any(m => m.Name == "PlayLocomotion")` + `using System.Linq` |

## Root Cause

All 60 NRE failures shared the same pattern: `var handler = SnapshotChanged; handler(latestSnapshot)` where `SnapshotChanged` was null because the constructor called `RefreshSnapshot()` before any subscriber could attach. The fix applies the C# 6 null-conditional operator `?.Invoke()`.

## PASS / PARTIAL / FAIL Table

| Requirement Area | Result | Notes |
| --- | --- | --- |
| Full EditMode suite passes after PlayerStateMachine refactor | PASS | 265/265, 0.72s runtime. |
| M1 runtime memory log path preserved | PASS | `M1RuntimeMemoryLogPlaceholderTests` 6/6 passed. |
| Memory state transitions preserved | PASS | `M0MemoryStateTests` 12/12 passed. |
| Input router behavior preserved | PASS | `M0InputRouterTests` 5/5 passed. |
| Animation service interface contract preserved | PASS | `AnimatorPresentationOnlyTests` 18/18 passed. |
| Health/Damage contract preserved | PASS | `M0HealthCombatContractTests` 12/12, `M0HealthConsequenceTests` 6/6, `M0HealthDamageReactionTests` 5/5 all passed. |
| Debug overlay snapshot preserved | PASS | `M0DebugOverlaySnapshotIntegrationTests` 6/6 passed. |
