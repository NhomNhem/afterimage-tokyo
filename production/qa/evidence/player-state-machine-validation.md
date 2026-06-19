# PlayerStateMachine — QA Validation Report

**Date**: 2026-06-16
**Tester**: OpenCode (gameplay-programmer / QA)
**Scope**: Validation of PlayerStateMachine implementation against GDD §8 Acceptance Criteria (AC-1 through AC-10)

---

## Remaining References Check: M0DodgeDisplacementBridge

| Result | Location | Details |
|--------|----------|---------|
| ✅ Deleted | `Assets/_Project/Code/Bootstrap/M0DodgeDisplacementBridge.cs` | File confirmed removed (glob returns no results) |
| ❌ Stale refs (5) | `Assets/_Project/Tests/PlayMode/M0DodgeDisplacementIntegrationTests.cs` | Lines 12, 34, 51, 71, 85 still `new M0DodgeDisplacementBridge()` |

---

## Per-AC Results

### AC-1: Priority Resolution — **PASS**

- `ResolvePlayerState()` uses `CombatPriorityTable` / `LocomotionPriorityTable` arrays
- `HitReact` → `PlayerState.HitReaction` (p8): confirmed — line 207: `case CombatCoreState.HitReact: return PlayerState.HitReaction;`
- `Neutral` + `Moving` → `PlayerState.Moving` (p1): confirmed — `combatPriority=0 < locomotionPriority=1`, falls to `LocomotionPriorityToPlayerState(Moving)` → `PlayerState.Moving`
- `Neutral` + `Idle` → `PlayerState.Idle` (p0): confirmed — falls through default to Idle
- Combat states (Disabled, HitReaction, RevealBeat, CounterActive, Attack, Parry, Dodge) all override locomotion correctly via priority comparison `combatPriority >= locomotionPriority && _combatCore != null`
- `TargetFocusMove` is **unreachable** — `LocomotionPriorityTable` only has 5 entries matching the current 5-value `LocomotionState` enum; `TargetFocusMove` (value 2 in `PlayerState`) is never resolved. This is a **known gap** per GDD §5.7 and arch §11.2 — locomotion enum expansion is deferred.

### AC-2: R3 Observable Fires — **PASS**

- `Subject<PlayerStateSnapshot> _stateSubject` is created at line 20, exposed as `Observable<PlayerStateSnapshot> StateChanges` at line 52
- `OnNext()` is gated by `resolvedSnapshot.ResolvedState != previousResolvedState` in both `OnCombatSnapshotChanged` and `OnLocomotionSnapshotChanged`
- Sub-state changes within same `PlayerState` (e.g., `AttackStartup` → `AttackActive` → `AttackRecovery` all map to `PlayerState.Attack`) do **not** fire, because `ResolvePlayerState()` returns the same `PlayerState`
- Initial fire: `TryPublishInitialSnapshot()` fires after both sources deliver their first snapshot

### AC-3: Aggregation — **PASS**

- `AggregateActionLock()` at line 231: combat lock (`_latestCombatSnapshot.ActionLock.IsLocked`) OR locomotion cannot translate (`!_latestLocomotionSnapshot.MovementRestriction.CanTranslate`); combat source wins if both locked
- `AggregateRecovery()` at line 247: combat recovery wins (`combatRecovering` checked first), else locomotion recovery; `RemainingSeconds` inherits from the winning source directly (not `max()` as specified in formula §4.2, but in practice both are from the same `RecoveryContext` struct)
- `HasTargetFocus` is **hardcoded to `false`** at line 161 — target context is not yet integrated. This is a **known gap** per GDD §6 ("M0TargetContext observed indirectly")

### AC-4: Animation Integration — **PASS**

- `M0AnimationPresentationAdapter.OnPlayerStateChanged()` (line 32) has a `switch` covering all 10 `PlayerState` values:
  - `Idle` / `Moving` / `TargetFocusMove` → calls `PlayLocomotion(LocomotionState, PlayerStateSnapshot)`
  - `Dodge` → calls `PlayDodge(new DodgeAnimationRequest(...))`
  - `Parry` → calls `PlayParry(new ParryAnimationRequest(...))`
  - `Attack` → calls `PlayAttack(new AttackAnimationRequest(...))` via `ResolveAttackType(snapshot)`
  - `CounterActive` / `RevealBeat` → calls `PlayCounter`
  - `HitReaction` → calls `PlayAttack`
  - `Disabled` → calls `PlayNeutral()`
- `IPlayerAnimationService.PlayLocomotion(LocomotionState, PlayerStateSnapshot)` overload exists at line 7 of `IPlayerAnimationService.cs`
- `AnimancerPlayerAnimationDriver` implements the new overload (line 48), delegates to same animation logic

### AC-5: Replacement of M0DodgeDisplacementBridge — **WARNING**

Core behavior is correct:
- `OnResolvedStateChanged()` at line 262: `current == PlayerState.Dodge && previous != PlayerState.Dodge` → calls `_locomotion?.TryBeginDodgeDisplacement()`
- Only called when **entering** Dodge (not leaving, not for other states)
- `M0DodgeDisplacementBridge.cs` file is deleted

**WARNING**: `Assets/_Project/Tests/PlayMode/M0DodgeDisplacementIntegrationTests.cs` still directly instantiates `M0DodgeDisplacementBridge` in 5 tests. These tests will fail to compile. They need to be either:
- Rewritten to use `PlayerStateMachine` and verify `TryBeginDodgeDisplacement()` is called on Dodge transition
- Or deleted if the bridge-specific testing is no longer relevant

### AC-6: Degraded Behavior — **WARNING**

Core degraded behavior is implemented:
- Constructor takes nullable `M0CombatCore?` and `IM0PlayerLocomotion?`
- `PlayerStateMachineFactory.Create()` logs appropriate warnings via NhemLogger
- `ResolvePlayerState()` handles null `_combatCore` by deriving from locomotion only (or vice versa)

**WARNING — Both-null initialization mismatch**:
- Architecture §9.3 specifies both null → `PlayerState.Disabled`
- Factory warning message says "always Disabled"
- But constructor initializes `_currentSnapshot` to `PlayerState.Idle` (line 65), and `Resolve()` when both null returns `PlayerState.Idle` (because `combatPriority=0 >= locomotionPriority=0` but `_combatCore != null` is false, falls to `LocomotionPriorityToPlayerState(Uninitialized)` → Idle)

Not a crash bug (the machine continues in a safe degraded state), but the behavior does not match the spec. Either update the architecture/factory message to match the Idle behavior or add explicit both-null → Disabled logic.

### AC-7: Debug Snapshot — **PASS**

- `CreateDebugSnapshot()` at line 268 returns `PlayerStateDebugSnapshot`
- Contains: `ResolvedState`, `CombatState`, `LocomotionState`, `ActionLocked/Source`, `Recovering/Detail`, `HasTargetFocus`, `Detail`
- `DebugOverlayChannelId.PlayerState = 9` is present in `M0Contracts.cs` (line 1535)
- `PlayerStateDebugSnapshot` readonly struct follows existing debug snapshot patterns (`Summary` + `IReadOnlyList<string> Details`)

### AC-8: Lifecycle — **PASS**

- `Dispose()` (line 281) unsubscribes from both `SnapshotChanged` events (combat at line 286, locomotion at line 289)
- `_stateSubject.Dispose()` called at line 293
- `_disposed` guard flag prevents double-disposal
- `M0AnimationPresentationAdapter` properly disposes its R3 subscription in `OnDestroy()` (line 102)
- `PlayerStateMachine` is registered `Lifetime.Singleton` in gameplay scope — VContainer handles disposal when scope ends

### AC-9: No Gameplay Truth Ownership — **PASS**

- No methods that mutate combat or locomotion state
- Only reads snapshots (via `_latestCombatSnapshot` / `_latestLocomotionSnapshot`)
- Publishes aggregated read-only snapshots via observable
- Only "action" call is `_locomotion?.TryBeginDodgeDisplacement()` which is a **request**, not a state mutation — locomotion decides whether to accept
- All public API surface is read-only: `StateChanges` (observable), `CurrentSnapshot` (property), `CreateDebugSnapshot()` (method)

### AC-10: Eliminated Manual Coordination — **FAIL**

- ✅ `M0DodgeDisplacementBridge.cs` is deleted
- ✅ `M0AnimationPresentationAdapter` no longer has `ObserveCombatSnapshot` / `ObserveLocomotionSnapshot` — replaced by `ObservePlayerState(IPlayerStateMachine)`
- ✅ `M0GameplayTickHandler` no longer manages dodge bridge or forwards combat/locomotion snapshots to animation adapter
- ❌ `M0DodgeDisplacementIntegrationTests.cs` (PlayMode) still references `M0DodgeDisplacementBridge` in 5 tests — will not compile
- ❌ `AnimatorPresentationOnly_test.cs` (EditMode, line 149-150) still asserts `ObserveCombatSnapshot` and `ObserveLocomotionSnapshot` exist — these methods were removed, tests will fail

---

## Additional Code Review Findings

### 1. Design Deviation: PlayerStateMachine does not consume IPlayerAnimationService

| Aspect | GDD/Arch Spec | Actual Implementation |
|--------|--------------|----------------------|
| Constructor | `PlayerStateMachine(..., IPlayerAnimationService, ...)` | `PlayerStateMachine(..., INhemLogger?)` |
| Animation routing | In `PlayerStateMachine.PlayAnimationForState()` | In `M0AnimationPresentationAdapter.OnPlayerStateChanged()` |
| Factory | Passes `IPlayerAnimationService` | No animation service needed |

The animation routing was delegated to the presentation adapter instead of living in `PlayerStateMachine`. This is **architecturally cleaner** (separation of concerns) and functionally equivalent (the adapter subscribes to `StateChanges` and routes correctly). However, it deviates from the GDD §3.6 and architecture §3.1 (step 7) which describe animation as a responsibility of `PlayerStateMachine`. Consider updating the GDD and architecture to reflect this design choice.

### 2. Stale Tests

Two test files will fail to compile:
- `Assets/_Project/Tests/PlayMode/M0DodgeDisplacementIntegrationTests.cs` — 5 tests reference deleted `M0DodgeDisplacementBridge`
- `Assets/_Project/Tests/EditMode/AnimatorPresentationOnly_test.cs` — lines 149-150 test for removed methods `ObserveCombatSnapshot` and `ObserveLocomotionSnapshot`

### 3. HasTargetFocus Hardcoded to False

`PlayerStateSnapshot.HasTargetFocus` is set to `false` at `PlayerStateMachine.cs:161`. The PlayerStateMachine doesn't observe target context. The GDD §6 lists `M0TargetContext` as a dependency ("observed indirectly"). This is a **known gap** for M0 — the locomotion enum also lacks `TargetFocusMove`. Neither gap blocks M0 combat feel.

### 4. Recovery RemainingSeconds

`AggregateRecovery()` returns `_latestCombatSnapshot.Recovery` or `_latestLocomotionSnapshot.Recovery` directly. The GDD formula §4.2 specifies `RemainingSeconds = max(CombatRecoveryRemaining, LocomotionRecoveryRemaining)`. Since in practice only one source is recovering at a time (combat recovery preempts locomotion), the current behavior is correct for all expected scenarios. The `max()` formula is only relevant if both are simultaneously recovering, which doesn't occur in M0 combat.

### 5. No Explicit Dispose of PlayerStateMachine in M0GameplayTickHandler

`M0GameplayTickHandler.OnDestroy()` does not call `_playerStateMachine.Dispose()`. This is **acceptable** because `PlayerStateMachine` is registered as `Lifetime.Singleton` in the gameplay-scoped VContainer LifetimeScope, and VContainer disposes all `IDisposable` singleton instances when the scope is destroyed. Adding explicit disposal would be defensive but is not required for correctness.

### 6. Naming Compliance

- `_camelCase` for private fields: ✅ (e.g., `_locomotion`, `_combatCore`, `_stateSubject`)
- PascalCase for properties/methods: ✅
- `PlayerState` enum values match GDD: ✅
- No underscore for serialized fields: ✅ (no serialized fields in pure C# classes)
- Namespace follows layer (`GlassRefrain.Application`): ✅
- File-per-type rule: ✅ (each type in its own file)

### 7. Convention Compliance

- `M0Contracts.cs` has `DebugOverlayChannelId.PlayerState = 9`: ✅
- `IM0PlayerLocomotion.TryBeginDodgeDisplacement()` is used: ✅
- `INhemLogger` is used for warnings (no `Debug.Log`): ✅
- No forbidden patterns (NavMesh, Animator, Resources.Load, etc.): ✅

---

## Overall Verdict: **NEEDS WORK**

| Component | Status |
|-----------|--------|
| Core PlayerStateMachine logic | ✅ COMPLETE |
| Priority resolution | ✅ PASS |
| R3 Observable | ✅ PASS |
| Aggregation | ✅ PASS |
| Animation routing | ✅ PASS (delegated to adapter) |
| Dodge displacement bridge replacement | ❌ Stale test references |
| Debug snapshot | ✅ PASS |
| Lifecycle | ✅ PASS |
| No gameplay truth ownership | ✅ PASS |
| Manual coordination elimination | ❌ Stale tests must be repaired |
| DebugOverlayChannelId | ✅ PASS |
| Naming/style conventions | ✅ PASS |

### Required Fixes (blocking completion)

1. **Fix `M0DodgeDisplacementIntegrationTests.cs`** — Update or remove the 5 tests that directly instantiate `M0DodgeDisplacementBridge`. Replace with tests that verify `PlayerStateMachine` calls `TryBeginDodgeDisplacement()` on Dodge entry.

2. **Fix `AnimatorPresentationOnly_test.cs`** — Lines 149-150 assert `ObserveCombatSnapshot` and `ObserveLocomotionSnapshot` exist. Replace with test for `ObservePlayerState(IPlayerStateMachine)` method.

### Recommended Fixes (non-blocking)

3. **Both-null → Disabled mismatch** — Either add explicit both-null check in `ResolvePlayerState()` returning `PlayerState.Disabled`, or update architecture §9.3 and factory warning to reflect actual behavior (Idle).

4. **Update GDD §3.6 and architecture** — Document that animation routing lives in `M0AnimationPresentationAdapter` (not `PlayerStateMachine`), reflecting the cleaner separation of concerns.
