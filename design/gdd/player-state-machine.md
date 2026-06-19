# Player State Machine

> **Status**: In Design
> **Author**: Codex
> **Last Updated**: 2026-06-16
> **Implements Pillar**: Combat As Interpretation, Debuggable Design

## 1. Overview

`PlayerStateMachine` is a pure C# aggregate observer that unifies `CombatCoreState` (15 states from `M0CombatCore`) and `LocomotionState` (10 states per locomotion GDD) into a single authoritative `PlayerStateSnapshot`. It does not own gameplay truth — it observes, aggregates, and publishes. The resolved `PlayerState` follows a strict priority hierarchy (`Disabled > HitReaction > RevealBeat > CounterActive > Attack > Parry > Dodge > TargetFocusMove > Moving > Idle`) so that presentation, debug, and animation layers can read one unambiguous player state without duplicating priority logic. The state machine publishes changes via R3 `Observable<PlayerStateSnapshot>` and feeds `IPlayerAnimationService` for Animancer-driven animation. It also exposes aggregated `ActionLockContext` and `RecoveryContext` so downstream systems never need to poll two separate sources.

## 2. Player Fantasy

The player should never feel or see a disjoint between their combat state and their movement state. When the player dodges, they feel one unified action — not a combat state machine ticking separately from a locomotion displacement bridge. When they attack, movement locks and combat commitment feel like a single system responding to their input. The `PlayerStateMachine` exists to erase this seam from the player's experience. For the developer, it exists to make state inspection, debug overlay, and animation routing trivial: one snapshot, one observable, one priority rule that explains every transition.

## 3. Detailed Rules

### 3.1 Composite Observation Model

`PlayerStateMachine` subscribes to:

- `M0CombatCore.SnapshotChanged` event (type `Action<M0CombatSnapshot>`)
- `IM0PlayerLocomotion.SnapshotChanged` event (type `Action<LocomotionStateSnapshot>`)

On each event, the machine:

1. Stores the latest snapshot from each source
2. Re-resolves a single `PlayerState` via priority rules
3. Aggregates `ActionLockContext` (active if either combat or locomotion reports a lock)
4. Aggregates `RecoveryContext` (active if either combat or locomotion reports recovery, preferring combat for source label)
5. Builds a new `PlayerStateSnapshot`
6. Publishes via `_stateSubject.OnNext(snapshot)` (R3 `Subject<PlayerStateSnapshot>`)
7. Calls `_animationService.PlayTransition(snapshot)` if the resolved `PlayerState` changed

### 3.2 PlayerState Enum

```csharp
public enum PlayerState {
    Idle = 0,            // LocomotionIdle, CombatNeutral, no action
    Moving = 1,          // LocomotionMove, no combat override
    TargetFocusMove = 2, // TargetFocusMove active, no combat override
    Dodge = 3,           // Any dodge sub-state (startup/active/recovery)
    Parry = 4,           // Any parry sub-state (startup/active/recovery)
    Attack = 5,          // Any attack sub-state or CounterWindow
    CounterActive = 6,   // CounterActive specifically
    RevealBeat = 7,      // RevealBeat
    HitReaction = 8,     // HitReact
    Disabled = 9         // Disabled
}
```

### 3.3 Priority Resolution

The machine resolves `PlayerState` by checking CombatCoreState first, then LocomotionState, using this priority (highest first):

| Priority | PlayerState | Trigger Condition |
|----------|-------------|-------------------|
| 9 (highest) | Disabled | CombatCoreState == Disabled |
| 8 | HitReaction | CombatCoreState == HitReact |
| 7 | RevealBeat | CombatCoreState == RevealBeat |
| 6 | CounterActive | CombatCoreState == CounterActive |
| 5 | Attack | CombatCoreState is AttackStartup, AttackActive, AttackRecovery, or CounterWindow |
| 4 | Parry | CombatCoreState is ParryStartup, ParryActive, ParryRecovery |
| 3 | Dodge | CombatCoreState is DodgeStartup, DodgeActive, DodgeRecovery |
| 2 | TargetFocusMove | LocomotionState == TargetFocusMove and no combat override above |
| 1 | Moving | LocomotionState == Moving and no combat override above |
| 0 (lowest) | Idle | LocomotionState == Idle (or no stronger state) |

If no match is found, the machine defaults to `PlayerState.Idle`.

### 3.4 PlayerStateSnapshot

```csharp
public readonly struct PlayerStateSnapshot {
    public PlayerState ResolvedState { get; }
    public CombatCoreState CombatState { get; }
    public LocomotionState LocomotionState { get; }
    public ActionLockContext ActionLock { get; }
    public RecoveryContext Recovery { get; }
    public bool HasTargetFocus { get; }
    public string StateDetail { get; }
}
```

Aggregation rules for `ActionLockContext`:
- `LockActive` = combat `ActionLockContext.IsLocked` OR locomotion `MovementRestrictionContext` prevents translation
- `LockSource` = combat lock source if combat is locking, else locomotion restriction source
- `RequestingState` = combat state if combat is locking, else `CombatCoreState.Neutral`

Aggregation rules for `RecoveryContext`:
- `RecoveryActive` = combat `RecoveryContext.IsRecovering` OR locomotion `RecoveryContext.IsRecovering`
- If both are recovering, combat recovery wins for `Source` and `Detail`
- `RemainingSeconds` = max of both remaining times

### 3.5 R3 Observable Shape

```csharp
public sealed class PlayerStateMachine : IDisposable {
    private readonly Subject<PlayerStateSnapshot> _stateSubject = new();

    // Public observable for debug overlay, UI, camera, VFX
    public Observable<PlayerStateSnapshot> StateChanges => _stateSubject;

    // Latest snapshot for synchronous reads (no allocation)
    public PlayerStateSnapshot CurrentSnapshot { get; private set; }
}
```

Observable contract:
- Fires on every resolved state change (not every tick)
- Does NOT fire if only sub-state changes within the same resolved `PlayerState` (e.g., AttackStartup to AttackActive)
- Debug overlay can subscribe to `StateChanges` for live updates
- Camera/VFX systems can filter by `ResolvedState` to trigger feedback

### 3.6 Animation Integration

`PlayerStateMachine` consumes `IPlayerAnimationService`:

```csharp
private void PlayAnimationForState(PlayerStateSnapshot snapshot) {
    switch (snapshot.ResolvedState) {
        case PlayerState.Idle:
        case PlayerState.Moving:
        case PlayerState.TargetFocusMove:
            _animationService.PlayLocomotion(snapshot.LocomotionState, snapshot);
            break;
        case PlayerState.Dodge:
            _animationService.PlayDodge(new DodgeAnimationRequest(snapshot.CombatState, snapshot.StateDetail));
            break;
        case PlayerState.Parry:
            _animationService.PlayParry(new ParryAnimationRequest(snapshot.CombatState, snapshot.StateDetail));
            break;
        case PlayerState.Attack:
            _animationService.PlayAttack(new AttackAnimationRequest(
                ResolveAttackType(snapshot), snapshot.CombatState, snapshot.StateDetail));
            break;
        case PlayerState.CounterActive:
            _animationService.PlayCounter(new AttackAnimationRequest(
                CombatActionType.Counter, snapshot.CombatState, snapshot.StateDetail));
            break;
        case PlayerState.RevealBeat:
            _animationService.PlayCounter(new AttackAnimationRequest(
                CombatActionType.Counter, snapshot.CombatState, "RevealBeat"));
            break;
        case PlayerState.HitReaction:
            _animationService.PlayAttack(new AttackAnimationRequest(
                CombatActionType.LightAttack, snapshot.CombatState, "HitReaction"));
            break;
        case PlayerState.Disabled:
            _animationService.PlayNeutral();
            break;
    }
}
```

This replaces the current dual-observer pattern in `M0AnimationPresentationAdapter` (which manually skips locomotion during combat states via a priority check at line 73-75). With `PlayerStateMachine`, the animation adapter subscribes to one observable and trusts the resolved priority.

The existing `IPlayerAnimationService` interface will need a new method:

```csharp
void PlayLocomotion(LocomotionState state, PlayerStateSnapshot fullSnapshot);
```

To pass the full snapshot for richer animation decisions (e.g., blend between idle and move based on target focus context).

### 3.7 Replacing M0DodgeDisplacementBridge

Currently, `M0DodgeDisplacementBridge` (in `Bootstrap/M0DodgeDisplacementBridge.cs`) manually watches combat state transitions to trigger locomotion dodge displacement. `PlayerStateMachine` absorbs this by observing the unified `PlayerState.Dodge` transition and calling `IM0PlayerLocomotion.TryBeginDodgeDisplacement()` directly.

```csharp
private void OnResolvedStateChanged(PlayerState previous, PlayerState current, PlayerStateSnapshot snapshot) {
    if (current == PlayerState.Dodge && previous != PlayerState.Dodge) {
        _locomotion.TryBeginDodgeDisplacement();
    }
}
```

This eliminates the bridge entirely. The `PlayerStateMachine` owns the coordination that was previously split across `M0DodgeDisplacementBridge` and `M0GameplayTickHandler.OnCombatSnapshotChanged`.

### 3.8 Debug Visibility

```csharp
public PlayerStateDebugSnapshot CreateDebugSnapshot() {
    var details = new string[] {
        "ResolvedState: " + CurrentSnapshot.ResolvedState,
        "CombatState: " + CurrentSnapshot.CombatState,
        "LocomotionState: " + CurrentSnapshot.LocomotionState,
        "ActionLocked: " + CurrentSnapshot.ActionLock.IsLocked + " | " + CurrentSnapshot.ActionLock.Source,
        "Recovering: " + CurrentSnapshot.Recovery.IsRecovering + " | " + CurrentSnapshot.Recovery.Detail,
        "HasTargetFocus: " + CurrentSnapshot.HasTargetFocus,
        "Detail: " + CurrentSnapshot.StateDetail
    };
    return new PlayerStateDebugSnapshot("M0 PlayerState", Array.AsReadOnly(details));
}
```

### 3.9 Threading / Lifecycle

- `PlayerStateMachine` is a pure C# service registered in VContainer at gameplay scene scope
- `IDisposable.Dispose()` unsubscribes from both source events and disposes the R3 subject
- The machine does not hold a reference to `MonoBehaviour` or `GameObject`
- It must be constructed after both `M0CombatCore` and `M0PlayerLocomotion` are fully initialized

### 3.10 VContainer Registration

```csharp
// In M0SceneCompositionRegistrar or gameplay-scoped LifetimeScope
builder.Register<PlayerStateMachine>(Lifetime.Singleton)
    .WithParameter<M0CombatCore>()
    .WithParameter<IM0PlayerLocomotion>()
    .WithParameter<IPlayerAnimationService>();
```

## 4. Formulas

### 4.1 Priority Resolution

```
ResolvedPlayerState = max(CombatPriority(c), LocomotionPriority(l))

CombatPriority(CombatCoreState):
  Disabled       -> 9
  HitReact       -> 8
  RevealBeat     -> 7
  CounterActive  -> 6
  AttackStartup  -> 5
  AttackActive   -> 5
  AttackRecovery -> 5
  CounterWindow  -> 5
  ParryStartup   -> 4
  ParryActive    -> 4
  ParryRecovery  -> 4
  DodgeStartup   -> 3
  DodgeActive    -> 3
  DodgeRecovery  -> 3
  Neutral        -> 0

LocomotionPriority(LocomotionState):
  Disabled       -> 9
  HitReaction    -> 8
  Recovery       -> 0   (combat overrides)
  CombatActionLocked -> 0 (combat overrides)
  CounterMovement-> 0   (combat overrides)
  Dodge          -> 0   (combat overrides via CombatCore)
  ParryHold      -> 0   (combat overrides via CombatCore)
  TargetFocusMove -> 2
  Moving         -> 1
  Idle           -> 0
```

### 4.2 Aggregation Formulas

```
ActionLockActive = CombatIsLocked OR LocomotionCannotTranslate
RecoveryActive   = CombatIsRecovering OR LocomotionIsRecovering
RecoverySource   = CombatRecoverySource if CombatIsRecovering else LocomotionRecoverySource
RecoveryRemaining = max(CombatRecoveryRemaining, LocomotionRecoveryRemaining)
```

## 5. Edge Cases

### 5.1 Rapid State Switching

If combat and locomotion fire snapshot changes in the same frame (possible given they are separate event dispatches), `PlayerStateMachine` resolves the state independently for each event. The observable fires twice but with the same `ResolvedState`. The animation service only receives a call if `ResolvedState` actually changes. Consumers should use `DistinctUntilChanged` on the observable if they only want unique transitions.

### 5.2 Simultaneous Combat / Locomotion Transition

Scenario: combat enters `DodgeActive` and locomotion enters `Moving` simultaneously. Priority resolution correctly yields `PlayerState.Dodge` (priority 3 > 1). No ambiguity.

### 5.3 Missing Combat or Locomotion Service

If `M0CombatCore` or `IM0PlayerLocomotion` is null at construction time, `PlayerStateMachine` logs a warning via `NhemLogger` and operates in a degraded mode:
- Missing combat: ResolvedState is derived from locomotion only. Defaults to Idle.
- Missing locomotion: ResolvedState is derived from combat only. Defaults to Idle.
- Both missing: ResolvedState is always `Disabled`, snapshot has defaulted aggregates.

### 5.4 CounterWindow While Moving

`CounterWindow` maps to `PlayerState.Attack` (priority 5). This means the player can be moving while a counter window is open, and `PlayerStateMachine` correctly resolves to `Attack`. The animation layer sees `Attack` and plays the appropriate counter-animation blend. The locomotion layer still updates position independently; `PlayerStateMachine` does NOT freeze movement.

### 5.5 Disabled State During Encounter Reset

When `Encounter Framework` resets, both `M0CombatCore` and `M0PlayerLocomotion` reset to their neutral states. `PlayerStateMachine` receives two sequential snapshot changes. The first may briefly show `Disabled` if one system resets before the other. This transient state is correct behavior — it lasts one frame. Consumers should tolerate brief transitional snapshots or use a debounce if needed.

### 5.6 Animation vs Gameplay Mismatch

If `PlayerStateMachine` resolves to `Attack` but the animation system is still blending from a previous dodge, that is a presentation timing issue, not a state machine issue. The `PlayerStateSnapshot` remains the authoritative gameplay truth. Animancer's crossfade duration handles visual blending.

### 5.7 New Locomotion States Not Yet in Code

The current `M0PlayerLocomotion` implementation uses 5 `LocomotionState` values (Uninitialized, Idle, Moving, Restricted, Recovering). The locomotion GDD specifies 10 states. Until the locomotion implementation expands to match the GDD, `PlayerStateMachine` should map the existing 5:
- Uninitialized -> Idle
- Restricted -> check `RecoveryContext.IsRecovering` -> Recovery, else check `CombatCoreState` (parry, dodge, attack)
- Recovering -> Idle (combat `RecoveryContext` overrides via priority)

The `PlayerStateMachine` GDD priority table assumes the full 10-state locomotion model. Implementation should gracefully handle the simplified current codeset until the locomotion enum is expanded.

## 6. Dependencies

### Consumed By PlayerStateMachine

| System | Interface | What It Provides |
|--------|-----------|------------------|
| M0CombatCore | `SnapshotChanged` event | `M0CombatSnapshot` with CombatCoreState, ActionLock, Recovery, CounterWindow |
| M0PlayerLocomotion | `SnapshotChanged` event | `LocomotionStateSnapshot` with LocomotionState, MovementRestriction, Recovery |
| IPlayerAnimationService | Method injection | Animation playback for each resolved PlayerState |
| M0TargetContext | (observed indirectly) | Target focus state (fed into snapshot externally or observed via SnapshotChanged) |

### Depend On PlayerStateMachine

| System | What It Replaces / Simplifies |
|--------|-------------------------------|
| M0AnimationPresentationAdapter | Eliminates dual-observer pattern. Subscribes to one observable. |
| M0GameplayTickHandler | Removes direct dodge bridge management. Removes combat->locomotion coordination. |
| M0DodgeDisplacementBridge | Entirely eliminated. |
| Debug Overlay | Subscribes to StateChanges instead of polling two separate snapshots. |
| Lock-On & Combat Camera | Subscribes to StateChanges for camera framing triggers. |
| Memory VFX Response | Subscribes to StateChanges for RevealBeat state. |
| UI / HUD | Subscribes to StateChanges for player state display. |

### Registration Order

1. M0CombatCore registered (gameplay scope)
2. M0PlayerLocomotion registered (gameplay scope)
3. IPlayerAnimationService / AnimancerPlayerAnimationDriver registered (presentation scope)
4. PlayerStateMachine registered (gameplay scope, depends on 1, 2, 3)

## 7. Tuning Knobs

| Knob | Type | Default | Purpose |
|------|------|---------|---------|
| Priority Table | hardcoded in code | As specified in section 3.3 | Order of state resolution. Only change if new states added or priority rebalance needed. |
| Animation Fade Duration | configurable via Animancer transitions | per-transition in M0PlayerAnimationSet | Crossfade duration when transitioning between resolved states. |
| Dodge Displacement Trigger | hardcoded | DodgeStartup -> DodgeActive transition | Which combat sub-state transition triggers displacement. Tune if displacement alignment shifts. |
| Snapshot Publish Strategy | Immediate vs Debounced | Immediate | If rapid flickering is observed, add a short debounce window (e.g., 1 frame) before publishing. |

## 8. Acceptance Criteria

### AC-1: Priority Resolution

Given a combat snapshot with `CombatCoreState.HitReact` and a locomotion snapshot with `LocomotionState.Moving`, When the machine resolves, Then `ResolvedState` is `HitReaction`.

Given a combat snapshot with `CombatCoreState.Neutral` and a locomotion snapshot with `LocomotionState.TargetFocusMove`, When the machine resolves, Then `ResolvedState` is `TargetFocusMove`.

Given a combat snapshot with `CombatCoreState.Neutral` and a locomotion snapshot with `LocomotionState.Idle`, When the machine resolves, Then `ResolvedState` is `Idle`.

### AC-2: R3 Observable Fires

When either source snapshot changes and the resolved `PlayerState` changes, Then `StateChanges` emits a new `PlayerStateSnapshot`.

When the resolved `PlayerState` does NOT change (e.g., AttackStartup -> AttackActive), Then `StateChanges` does NOT emit.

### AC-3: Aggregation

When combat reports `ActionLockContext.IsLocked = true`, Then `PlayerStateSnapshot.ActionLock.IsLocked` is true regardless of locomotion state.

When locomotion reports `RecoveryContext.IsRecovering = true` and combat reports `RecoveryContext.IsRecovering = false`, Then `PlayerStateSnapshot.Recovery.IsRecovering` is true and `Recovery.Source` is `PlayerLocomotion`.

When both report recovery, Then `Recovery.Source` is `CombatCore`.

### AC-4: Animation Integration

When `PlayerState` changes from `Idle` to `Dodge`, Then `IPlayerAnimationService.PlayDodge` is called with the correct request.

When `PlayerState` changes from `Attack` to `Idle`, Then `IPlayerAnimationService.PlayLocomotion` is called.

When `PlayerState` changes from `Idle` to `Moving`, Then `IPlayerAnimationService.PlayLocomotion` is called with `LocomotionState.Moving`.

### AC-5: Replacement of M0DodgeDisplacementBridge

When `PlayerState` transitions from any non-Dodge state to `PlayerState.Dodge`, Then `IM0PlayerLocomotion.TryBeginDodgeDisplacement()` is called exactly once.

When `PlayerState` transitions from `Dodge` to another state, `TryBeginDodgeDisplacement` is NOT called.

### AC-6: Degraded Behavior

When `M0CombatCore` is null at construction, Then the machine resolves based on locomotion state only, and logs a warning via NhemLogger.

When both sources are null, Then `CurrentSnapshot.ResolvedState` is `Disabled`.

### AC-7: Debug Snapshot

`CreateDebugSnapshot()` returns a `PlayerStateDebugSnapshot` containing the resolved state, both source states, action lock state, recovery state, target focus flag, and a human-readable detail string.

### AC-8: Lifecycle

When `Dispose()` is called, Then the machine unsubscribes from both `SnapshotChanged` events and disposes the R3 `Subject`.

No memory leaks from event subscriptions after disposal.

### AC-9: No Gameplay Truth Ownership

`PlayerStateMachine` never mutates `M0CombatCore` or `M0PlayerLocomotion` state. It is strictly read-only. Verified by: all public methods return snapshots or observables; no `SetState` or `Transition` methods exist.

### AC-10: Eliminated Manual Coordination

After `PlayerStateMachine` is introduced, `M0DodgeDisplacementBridge` is removed from the codebase. `M0AnimationPresentationAdapter.ObserveCombatSnapshot` and `M0AnimationPresentationAdapter.ObserveLocomotionSnapshot` are replaced by a single method subscribing to `PlayerStateMachine.StateChanges`.
