# PlayerStateMachine Architecture

> **Status**: Draft
> **Author**: OpenCode (gameplay-programmer)
> **Date**: 2026-06-16
> **GDD**: `design/gdd/player-state-machine.md`
> **Implements**: M0 Combat Feel — unified player state aggregation

---

## 1. File Inventory

### 1.1 New Files

| File | Namespace | Purpose |
|------|-----------|---------|
| `Assets/_Project/Code/Core/PlayerState.cs` | `GlassRefrain.Core` | `PlayerState` enum (Idle, Moving, TargetFocusMove, Dodge, Parry, Attack, CounterActive, RevealBeat, HitReaction, Disabled) |
| `Assets/_Project/Code/Core/PlayerStateSnapshot.cs` | `GlassRefrain.Core` | `PlayerStateSnapshot` readonly struct — unified snapshot with ResolvedState, CombatState, LocomotionState, ActionLock, Recovery, HasTargetFocus, StateDetail |
| `Assets/_Project/Code/Core/PlayerStateDebugSnapshot.cs` | `GlassRefrain.Core` | `PlayerStateDebugSnapshot` readonly struct — follows `{X}DebugSnapshot` pattern (Summary + IReadOnlyList<string> Details) |
| `Assets/_Project/Code/Application/IPlayerStateMachine.cs` | `GlassRefrain.Application` | Interface: `StateChanges` observable, `CurrentSnapshot`, `CreateDebugSnapshot()`, `IDisposable` |
| `Assets/_Project/Code/Application/PlayerStateMachine.cs` | `GlassRefrain.Application` | Sealed class — aggregate observer, priority resolver, animation router, dodge bridge replacement |
| `Assets/_Project/Code/Application/PlayerStateMachineFactory.cs` | `GlassRefrain.Application` | Factory for safe construction with degraded-mode handling |

### 1.2 Modified Files

| File | Change |
|------|--------|
| `Assets/_Project/Code/Core/M0Contracts.cs` | Add `DebugOverlayChannelId.PlayerState` enum entry |
| `Assets/_Project/Code/Presentation/IPlayerAnimationService.cs` | Add `PlayLocomotion(LocomotionState, PlayerStateSnapshot)` overload |
| `Assets/_Project/Code/Presentation/M0AnimationPresentationAdapter.cs` | Replace dual-observer pattern with single `ObservePlayerState(PlayerStateSnapshot)` |
| `Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs` | Remove `_dodgeDisplacementBridge`, remove per-snapshot forwarding to animation adapter; keep combat/locomotion snapshot event subscriptions for visual feedback only |
| `Assets/_Project/Code/Bootstrap/M0RuntimeServiceCompositionRegistrar.cs` | Register `PlayerStateMachine` with combat, locomotion, and animation service |
| `Assets/_Project/Code/Bootstrap/M0SceneCompositionRegistrar.cs` | Wire `PlayerStateMachine` to `M0AnimationPresentationAdapter` if needed |

### 1.3 Deleted Files

| File | Reason |
|------|--------|
| `Assets/_Project/Code/Bootstrap/M0DodgeDisplacementBridge.cs` | Absorbed into `PlayerStateMachine.OnResolvedStateChanged` |

---

## 2. Interface Definitions

### 2.1 `IPlayerStateMachine` (new)

```csharp
namespace GlassRefrain.Application;

public interface IPlayerStateMachine : IDisposable {
    // R3 observable — fires when resolved PlayerState changes (not sub-state)
    Observable<PlayerStateSnapshot> StateChanges { get; }

    // Latest snapshot for synchronous reads (no allocation)
    PlayerStateSnapshot CurrentSnapshot { get; }

    // Debug overlay snapshot
    PlayerStateDebugSnapshot CreateDebugSnapshot();
}
```

### 2.2 `IPlayerAnimationService` (modified)

```csharp
namespace GlassRefrain.Presentation;

public interface IPlayerAnimationService {
    void PlayNeutral();
    void PlayLocomotion(LocomotionStateSnapshot snapshot);
    void PlayLocomotion(LocomotionState state, PlayerStateSnapshot fullSnapshot); // NEW
    void PlayAttack(AttackAnimationRequest request);
    void PlayDodge(DodgeAnimationRequest request);
    void PlayParry(ParryAnimationRequest request);
    void PlayCounter(AttackAnimationRequest request);
}
```

The new overload allows the animation layer to make richer blend decisions (e.g., blend idle→move based on target focus context from the full snapshot).

---

## 3. Class Structures

### 3.1 `PlayerStateMachine` (sealed class)

```csharp
namespace GlassRefrain.Application;

public sealed class PlayerStateMachine : IPlayerStateMachine {
    // Dependencies (injected via constructor)
    private readonly IPlayerAnimationService _animationService;
    private readonly IM0PlayerLocomotion? _locomotion;       // nullable for degraded mode
    private readonly M0CombatCore? _combatCore;              // nullable for degraded mode
    private readonly INhemLogger? _logger;

    // Internal state
    private M0CombatSnapshot _latestCombatSnapshot;
    private LocomotionStateSnapshot _latestLocomotionSnapshot;
    private PlayerState _lastResolvedState;
    private PlayerStateSnapshot _currentSnapshot;

    // R3 subject
    private readonly Subject<PlayerStateSnapshot> _stateSubject = new();

    // Events that must fire on first subscription
    private bool _hasReceivedCombatSnapshot;
    private bool _hasReceivedLocomotionSnapshot;

    // Public properties
    public Observable<PlayerStateSnapshot> StateChanges => _stateSubject;
    public PlayerStateSnapshot CurrentSnapshot => _currentSnapshot;

    // Constructor — subscription happens here
    public PlayerStateMachine(
        M0CombatCore? combatCore,
        IM0PlayerLocomotion? locomotion,
        IPlayerAnimationService animationService,
        INhemLogger? logger) { ... }

    // Event handlers
    private void OnCombatSnapshotChanged(M0CombatSnapshot snapshot) { ... }
    private void OnLocomotionSnapshotChanged(LocomotionStateSnapshot snapshot) { ... }

    // Core resolution
    private PlayerStateSnapshot Resolve() { ... }
    private PlayerState ResolvePlayerState() { ... }
    private ActionLockContext AggregateActionLock() { ... }
    private RecoveryContext AggregateRecovery() { ... }

    // Dodge displacement bridge replacement
    private void OnResolvedStateChanged(PlayerState previous, PlayerState current) { ... }

    // Animation routing
    private void PlayAnimationForState(PlayerStateSnapshot snapshot) { ... }

    // Debug
    public PlayerStateDebugSnapshot CreateDebugSnapshot() { ... }

    // Cleanup
    public void Dispose() { ... }

    // Priority table — hardcoded
    private static int CombatPriority(CombatCoreState state) { ... }
    private static int LocomotionPriority(LocomotionState state) { ... }
}
```

### 3.2 `PlayerStateSnapshot` (readonly struct)

```csharp
namespace GlassRefrain.Core;

public readonly struct PlayerStateSnapshot {
    public PlayerState ResolvedState { get; }
    public CombatCoreState CombatState { get; }
    public LocomotionState LocomotionState { get; }
    public ActionLockContext ActionLock { get; }
    public RecoveryContext Recovery { get; }
    public bool HasTargetFocus { get; }
    public string StateDetail { get; }

    public PlayerStateSnapshot(
        PlayerState resolvedState,
        CombatCoreState combatState,
        LocomotionState locomotionState,
        ActionLockContext actionLock,
        RecoveryContext recovery,
        bool hasTargetFocus,
        string stateDetail) { ... }
}
```

### 3.3 `PlayerStateDebugSnapshot` (readonly struct)

```csharp
namespace GlassRefrain.Core;

public readonly struct PlayerStateDebugSnapshot {
    public string Summary { get; }
    public IReadOnlyList<string> Details { get; }

    public PlayerStateDebugSnapshot(string summary, IReadOnlyList<string> details) { ... }
}
```

### 3.4 `PlayerStateMachineFactory`

```csharp
namespace GlassRefrain.Application;

public static class PlayerStateMachineFactory {
    public static IPlayerStateMachine Create(
        M0CombatCore? combatCore,
        IM0PlayerLocomotion? locomotion,
        IPlayerAnimationService animationService,
        INhemLogger? logger) {

        if (combatCore == null)
            logger?.LogWarning("[M0PlayerStateMachine] CombatCore is null — degraded mode (locomotion only)");
        if (locomotion == null)
            logger?.LogWarning("[M0PlayerStateMachine] Locomotion is null — degraded mode (combat only)");
        if (combatCore == null && locomotion == null)
            logger?.LogWarning("[M0PlayerStateMachine] Both sources null — always Disabled");

        return new PlayerStateMachine(combatCore, locomotion, animationService, logger);
    }
}
```

---

## 4. Data Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                        M0GameplayTickHandler                         │
│                                                                      │
│  Tick() → _combatCore.Tick() → SnapshotChanged fires                 │
│  Tick() → _locomotion.Tick() → SnapshotChanged fires                 │
└──────┬──────────────────────────────────────┬───────────────────────┘
       │ M0CombatSnapshot                     │ LocomotionStateSnapshot
       ▼                                      ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        PlayerStateMachine                             │
│                                                                       │
│  OnCombatSnapshotChanged(snapshot) → _latestCombatSnapshot = snapshot │
│  OnLocomotionSnapshotChanged(snapshot) → _latestLocomotionSnap = snap│
│                                                                       │
│  Resolve():                                                            │
│    state = max(CombatPriority(c), LocomotionPriority(l))             │
│    lock  = combat.LockActive OR locomotion.CanTranslate == false     │
│    recovery = combat.IsRecovering OR locomotion.IsRecovering          │
│    build PlayerStateSnapshot                                           │
│                                                                       │
│  if ResolvedState changed:                                            │
│    → _stateSubject.OnNext(snapshot)     ──────→ R3 subscribers        │
│    → PlayAnimationForState(snapshot)    ──────→ IPlayerAnimationSvc   │
│    → TryBeginDodgeDisplacement() if     ──────→ IM0PlayerLocomotion   │
│      previous != Dodge && current == Dodge                            │
└──────────────────────────────────────────────────────────────────────┘
       │
       │ PlayerStateSnapshot (via R3)
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        R3 Subscribers                                 │
│                                                                       │
│  M0AnimationPresentationAdapter.ObservePlayerState(snapshot)          │
│    → single source of truth for animation routing                     │
│                                                                       │
│  Debug Overlay → CreateDebugSnapshot() or StateChanges                │
│                                                                       │
│  Camera/VFX systems can subscribe and filter by ResolvedState         │
└──────────────────────────────────────────────────────────────────────┘
```

### Priority Resolution Flowchart

```
PlayerStateMachine.ResolvePlayerState()
│
├── CombatCoreState == Disabled        → PlayerState.Disabled (p9)
├── CombatCoreState == HitReact         → PlayerState.HitReaction (p8)
├── CombatCoreState == RevealBeat       → PlayerState.RevealBeat (p7)
├── CombatCoreState == CounterActive    → PlayerState.CounterActive (p6)
├── CombatCoreState in (AttackStartup, AttackActive, AttackRecovery, CounterWindow)
│                                       → PlayerState.Attack (p5)
├── CombatCoreState in (ParryStartup, ParryActive, ParryRecovery)
│                                       → PlayerState.Parry (p4)
├── CombatCoreState in (DodgeStartup, DodgeActive, DodgeRecovery)
│                                       → PlayerState.Dodge (p3)
├── LocomotionState == TargetFocusMove  → PlayerState.TargetFocusMove (p2)
├── LocomotionState == Moving           → PlayerState.Moving (p1)
└── (else)                              → PlayerState.Idle (p0)
```

---

## 5. R3 Observable Contract

```csharp
// Subject construction (internal)
private readonly Subject<PlayerStateSnapshot> _stateSubject = new();

// Public exposure
public Observable<PlayerStateSnapshot> StateChanges => _stateSubject;

// Fire rule:
//   Only fires when ResolvedState changes (e.g., Idle → Dodge).
//   Does NOT fire when sub-state changes within same PlayerState
//   (e.g., AttackStartup → AttackActive → AttackRecovery all map to PlayerState.Attack).
//
// Initial fire:
//   Fires once when both combat and locomotion have delivered their first snapshot.
//   This ensures subscribers always have a valid initial state.

// Consumer usage pattern:
//   stateMachine.StateChanges
//       .DistinctUntilChanged()
//       .Subscribe(snapshot => { ... });
```

### Subject Lifetime

| Phase | State | Behavior |
|-------|-------|----------|
| Construction | Not yet resolved | No fire |
| First combat snapshot received | Partial resolution | Cache, wait for locomotion (or vice versa) |
| Both sources received | Full resolution | Fire initial snapshot |
| Subsequent changes | Re-resolve | Fire only if ResolvedState changed |
| Dispose | Disposed | `_stateSubject.Dispose()` + event unsubscription |

---

## 6. Integration Points — Detailed Changes

### 6.1 `M0CombatCore` (`Combat/M0CombatCore.cs`)

**No changes required.** `M0CombatCore` already exposes:
- `SnapshotChanged` event (`Action<M0CombatSnapshot>`)
- `Snapshot` property

`PlayerStateMachine` subscribes directly to these. No interface modifications needed.

### 6.2 `M0PlayerLocomotion` (`Locomotion/M0PlayerLocomotion.cs`)

**No changes required.** `IM0PlayerLocomotion` already exposes:
- `SnapshotChanged` event (`Action<LocomotionStateSnapshot>`)
- `Snapshot` property
- `TryBeginDodgeDisplacement()` method

The only change needed is adding `TargetFocusMove` to the `LocomotionState` resolution in `ResolveState()` — currently `LocomotionState` has 5 values (no TargetFocusMove). This is a future/enum-expansion concern, not a blocker for `PlayerStateMachine`. Until then, `TargetFocusMove` is never emitted, which is safe.

### 6.3 `M0AnimationPresentationAdapter` (`Presentation/M0AnimationPresentationAdapter.cs`)

**Replace dual-observer with single observer:**

```csharp
// REMOVED:
// public void ObserveCombatSnapshot(M0CombatSnapshot snapshot) { ... }
// public void ObserveLocomotionSnapshot(LocomotionStateSnapshot snapshot) { ... }

// ADDED:
private IDisposable _playerStateSubscription; // for cleanup

public void ObservePlayerState(IPlayerStateMachine stateMachine) {
    _playerStateSubscription?.Dispose();
    _playerStateSubscription = stateMachine.StateChanges
        .Subscribe(OnPlayerStateChanged);
}

private void OnPlayerStateChanged(PlayerStateSnapshot snapshot) {
    // Single switch on ResolvedState — no priority logic needed
    // See GDD section 3.6 for the full switch body
    switch (snapshot.ResolvedState) {
        case PlayerState.Idle:
        case PlayerState.Moving:
        case PlayerState.TargetFocusMove:
            _playerAnimationService.PlayLocomotion(snapshot.LocomotionState, snapshot);
            break;
        case PlayerState.Dodge:
            _playerAnimationService.PlayDodge(new DodgeAnimationRequest(
                snapshot.CombatState, snapshot.StateDetail));
            break;
        // ... other states
    }
}

// Add cleanup in OnDestroy:
private void OnDestroy() {
    _playerStateSubscription?.Dispose();
    _playerStateSubscription = null;
}
```

**Removed fields:** `_lastCombatState`, `_lastAttackType`, `_lastLocomotionState`, `_lastEnemyIntentState` (if only used by the old observers — `_lastEnemyIntentState` is still used by `ObserveEnemyIntentSnapshot`, which remains).

### 6.4 `M0GameplayTickHandler` (`Bootstrap/M0GameplayTickHandler.cs`)

**Changes:**

1. **Remove** `_dodgeDisplacementBridge` field and `M0DodgeDisplacementBridge` import
2. **Remove** `OnCombatSnapshotChanged` lines that call `_dodgeDisplacementBridge.HandleCombatTransition()`
3. **Remove** `OnLocomotionSnapshotChanged` — the animation adapter no longer receives locomotion snapshots directly
4. **Remove** `_dodgeDisplacementBridge.Reset()` from `ResetEncounterLifecycle()`
5. **Add** `IPlayerStateMachine` dependency to `Construct()` (inject via VContainer)
6. **Add** wiring in `Construct()` to connect `_playerStateMachine` to the animation adapter

```csharp
// In Construct() — after existing subscriptions:
_playerStateMachine = playerStateMachine;
animationPresentationAdapter?.ObservePlayerState(_playerStateMachine);
```

7. **Add** `_playerStateMachine` field
8. **Add** cleanup in `OnDestroy()` — dispose `_playerStateMachine`

**Simplified `OnCombatSnapshotChanged`:** Remove the dodge displacement block. Keep visual feedback, debug overlay, and `animationPresentationAdapter?.ObserveCombatSnapshot(snapshot)` — this last line should be replaced or removed since animation now comes from `PlayerStateMachine`. However, visual feedback still needs raw combat snapshots. The visual feedback switch and debug overlay updates remain.

```csharp
// Simplified OnCombatSnapshotChanged:
private void OnCombatSnapshotChanged(M0CombatSnapshot snapshot) {
    var previousState = lastCombatSnapshot.State;
    var currentState = snapshot.State;

    // REMOVED: _dodgeDisplacementBridge block
    // REMOVED: animationPresentationAdapter?.ObserveCombatSnapshot(snapshot)

    // KEPT: visual feedback
    if (visualFeedbackAdapter != null && previousState != currentState) {
        switch (currentState) {
            case CombatCoreState.AttackStartup:
            case CombatCoreState.AttackActive:
                visualFeedbackAdapter.TriggerLightAttackFeedback();
                break;
            case CombatCoreState.ParryStartup:
            case CombatCoreState.ParryActive:
                visualFeedbackAdapter.TriggerParryFeedback();
                break;
            case CombatCoreState.DodgeStartup:
            case CombatCoreState.DodgeActive:
                visualFeedbackAdapter.TriggerDodgeFeedback();
                break;
            case CombatCoreState.CounterActive:
                visualFeedbackAdapter.TriggerCounterFeedback();
                break;
        }
    }

    // KEPT: counter window visual feedback
    bool counterWindowOpened = !lastCombatSnapshot.CounterWindow.IsOpen && snapshot.CounterWindow.IsOpen;
    if (visualFeedbackAdapter != null && counterWindowOpened) {
        visualFeedbackAdapter.TriggerCounterAvailableFeedback();
    }

    // KEPT: debug overlay
    if (debugOverlayAdapter != null) {
        debugOverlayAdapter.UpdateCombatState(currentState.ToString());
        debugOverlayAdapter.UpdateCounterWindowState(
            snapshot.CounterWindow.IsOpen,
            snapshot.CounterWindow.ElapsedSeconds,
            snapshot.CounterWindow.DurationSeconds);
    }

    lastCombatSnapshot = snapshot;
}

// Simplified OnLocomotionSnapshotChanged:
private void OnLocomotionSnapshotChanged(LocomotionStateSnapshot snapshot) {
    // REMOVED: animationPresentationAdapter?.ObserveLocomotionSnapshot(snapshot)
    // Animation now comes from PlayerStateMachine only.
    // Keep if locomotion snapshots are needed for other purposes (debug, etc.)
}
```

### 6.5 `M0DodgeDisplacementBridge` (`Bootstrap/M0DodgeDisplacementBridge.cs`)

**Deleted entirely.** Logic absorbed into `PlayerStateMachine.OnResolvedStateChanged()`:

```csharp
private void OnResolvedStateChanged(PlayerState previous, PlayerState current) {
    if (current == PlayerState.Dodge && previous != PlayerState.Dodge) {
        _locomotion?.TryBeginDodgeDisplacement();
    }
}
```

### 6.6 `M0SceneCompositionRegistrar` (`Bootstrap/M0SceneCompositionRegistrar.cs`)

**Minor addition:** Wire `PlayerStateMachine` to animation adapter in `WirePresentationAdapters()`:

```csharp
private void WirePresentationAdapters() {
    if (_tickHandler != null) {
        _tickHandler.SetVisualFeedbackAdapter(_visualFeedbackAdapter);
        _tickHandler.SetDebugOverlayAdapter(_debugOverlayAdapter);
        _tickHandler.SetAnimationPresentationAdapter(_animationPresentationAdapter);
    }

    // NEW: wire PlayerStateMachine to animation adapter
    var container = /* from RegisterBuildCallback */;
    var playerStateMachine = container.Resolve<IPlayerStateMachine>();
    _animationPresentationAdapter?.ObservePlayerState(playerStateMachine);

    // ... existing warning logic
}
```

Note: The container reference must be captured from `RegisterBuildCallback` — same pattern as the existing `_logger` resolve.

### 6.7 `M0RuntimeServiceCompositionRegistrar` (`Bootstrap/M0RuntimeServiceCompositionRegistrar.cs`)

**Add PlayerStateMachine registration:**

```csharp
public void Register(IContainerBuilder builder) {
    // ... existing M0CombatCore, M0PlayerLocomotion, M0MemoryState, M0MemoryVFXResponse registrations

    // NEW: PlayerStateMachine
    builder.Register<IPlayerStateMachine>(resolver => {
        var combatCore = resolver.Resolve<M0CombatCore>();
        var locomotion = resolver.Resolve<IM0PlayerLocomotion>();
        var animationService = resolver.Resolve<IPlayerAnimationService>();
        var logger = resolver.Resolve<INhemLogger>();
        return PlayerStateMachineFactory.Create(combatCore, locomotion, animationService, logger);
    }, Lifetime.Singleton).As<IPlayerStateMachine>().AsSelf();
}
```

Registration order matters — M0CombatCore and M0PlayerLocomotion must be registered before PlayerStateMachine (they are, in the existing code above).

### 6.8 `IPlayerAnimationService` (`Presentation/IPlayerAnimationService.cs`)

**Add one new method:**

```csharp
void PlayLocomotion(LocomotionState state, PlayerStateSnapshot fullSnapshot);
```

The `AnimancerPlayerAnimationDriver` (implementation) must add this method. For M0, it can delegate to the existing `PlayLocomotion(LocomotionStateSnapshot snapshot)` internally if no richer blending is needed yet.

---

## 7. VContainer Registration

### 7.1 Registration in `M0RuntimeServiceCompositionRegistrar.Register()`

```csharp
builder.Register<IPlayerStateMachine>(resolver => {
    var combatCore = resolver.Resolve<M0CombatCore>();
    var locomotion = resolver.Resolve<IM0PlayerLocomotion>();
    var animationService = resolver.Resolve<IPlayerAnimationService>();
    var logger = resolver.Resolve<INhemLogger>();
    return PlayerStateMachineFactory.Create(combatCore, locomotion, animationService, logger);
}, Lifetime.Singleton).As<IPlayerStateMachine>().AsSelf();
```

### 7.2 Registration Order

```txt
1. M0CombatCore.As<IM0CombatCore>().AsSelf()          ← M0RuntimeServiceCompositionRegistrar
2. M0PlayerLocomotion.As<IM0PlayerLocomotion>().AsSelf()  ← M0RuntimeServiceCompositionRegistrar
3. AnimancerPlayerAnimationDriver.As<IPlayerAnimationService>()  ← M0SceneCompositionRegistrar
4. PlayerStateMachine.As<IPlayerStateMachine>().AsSelf()  ← M0RuntimeServiceCompositionRegistrar (NEW)
```

Steps 1-3 already exist. Step 4 is added after step 3.

### 7.3 Lifetime Decision

`Lifetime.Singleton` at gameplay scope (same scope as `M0CombatCore` and `M0PlayerLocomotion`). This is correct because:
- Gameplay scope is scoped to the encounter/demo scene level (VContainer LifetimeScope)
- The machine holds event subscriptions to gameplay-scoped services
- When the scope is disposed, the machine is disposed along with its dependencies

---

## 8. Debug Overlay Integration

### 8.1 New Channel ID

Add to `DebugOverlayChannelId` enum in `M0Contracts.cs`:

```csharp
PlayerState = 9,  // NEW — inserted after EncounterFramework = 8
```

Consider updating `DebugOverlayAggregateSnapshot` to include the new channel, or expose `PlayerStateDebugSnapshot` through the existing `CreateDebugSnapshot()` method pattern that the debug overlay already knows how to consume.

### 8.2 Debug Snapshot Shape

`PlayerStateDebugSnapshot` follows the established pattern:

```csharp
public readonly struct PlayerStateDebugSnapshot {
    public string Summary { get; }           // "M0 PlayerState"
    public IReadOnlyList<string> Details { get; }  // One string per field
}
```

Details content:

```
ResolvedState: Dodge
CombatState: DodgeActive
LocomotionState: Restricted
ActionLocked: True | DodgeActive
Recovering: False |
HasTargetFocus: True
Detail: Dodge accepted
```

---

## 9. Degraded Mode Handling

### 9.1 Null Combat Core

```csharp
// _combatCore is null
private PlayerState ResolvePlayerState() {
    if (_combatCore == null) {
        // Derive from locomotion only
        return locomotionState switch {
            LocomotionState.Uninitialized => PlayerState.Idle,
            LocomotionState.Idle => PlayerState.Idle,
            LocomotionState.Moving => PlayerState.Moving,
            LocomotionState.Restricted => PlayerState.Idle,
            LocomotionState.Recovering => PlayerState.Idle,
            _ => PlayerState.Idle
        };
    }
    // ... normal priority resolution
}
```

### 9.2 Null Locomotion

```csharp
// _locomotion == null
private PlayerState ResolvePlayerState() {
    if (_locomotion == null) {
        // Derive from combat only
        return CombatToPlayerState(_combatCore.Snapshot.State);
    }
    // ... normal priority resolution
}
```

### 9.3 Both Null

```csharp
// Both null → always Disabled
public PlayerStateSnapshot CurrentSnapshot { get; private set; }
    = new PlayerStateSnapshot(
        PlayerState.Disabled, CombatCoreState.Disabled,
        LocomotionState.Uninitialized,
        new ActionLockContext(true, "NoServices", CombatCoreState.Disabled),
        new RecoveryContext(RecoverySource.Unknown, false, 0f, "No services available"),
        false, "PlayerStateMachine: all sources null");
```

### 9.4 Animation Service Null

If `IPlayerAnimationService` is null, the machine logs a warning and skips `PlayAnimationForState` calls. The observable still fires and the snapshot is still available for debug / other consumers.

---

## 10. Priority Resolution — Implementation

### 10.1 Priority Values

```csharp
private static readonly (CombatCoreState State, int Priority)[] CombatPriorityTable = {
    (CombatCoreState.Disabled,       9),
    (CombatCoreState.HitReact,       8),
    (CombatCoreState.RevealBeat,     7),
    (CombatCoreState.CounterActive,  6),
    (CombatCoreState.AttackStartup,  5),
    (CombatCoreState.AttackActive,   5),
    (CombatCoreState.AttackRecovery, 5),
    (CombatCoreState.CounterWindow,  5),
    (CombatCoreState.ParryStartup,   4),
    (CombatCoreState.ParryActive,    4),
    (CombatCoreState.ParryRecovery,  4),
    (CombatCoreState.DodgeStartup,   3),
    (CombatCoreState.DodgeActive,    3),
    (CombatCoreState.DodgeRecovery,  3),
    (CombatCoreState.Neutral,        0),
};

private static readonly (LocomotionState State, int Priority)[] LocomotionPriorityTable = {
    (LocomotionState.Uninitialized, 0),
    (LocomotionState.Idle,          0),
    (LocomotionState.Moving,        1),
    (LocomotionState.Restricted,    0),  // combat overrides
    (LocomotionState.Recovering,    0),  // combat overrides
};
```

### 10.2 Resolution Logic

```csharp
private PlayerState ResolvePlayerState() {
    int combatPriority = 0;
    int locomotionPriority = 0;

    if (_combatCore != null) {
        var combatState = _latestCombatSnapshot.State;
        combatPriority = CombatPriorityTable.First(t => t.State == combatState).Priority;
    }

    if (_locomotion != null) {
        var locomotionState = _latestLocomotionSnapshot.State;
        locomotionPriority = LocomotionPriorityTable.First(t => t.State == locomotionState).Priority;
    }

    if (combatPriority >= locomotionPriority) {
        return CombatPriorityToPlayerState(_latestCombatSnapshot.State);
    }

    return LocomotionPriorityToPlayerState(_latestLocomotionSnapshot.State);
}
```

---

## 11. Edge Cases — Implementation Notes

### 11.1 First Frame Race Condition

Both combat and locomotion may fire their initial `SnapshotChanged` in the same frame. `PlayerStateMachine` handles this by:

```csharp
private bool _hasReceivedCombatSnapshot;
private bool _hasReceivedLocomotionSnapshot;

private void TryPublishInitialSnapshot() {
    if (!_hasReceivedCombatSnapshot || !_hasReceivedLocomotionSnapshot) return;

    // Both sources received for the first time — publish initial snapshot
    var snapshot = Resolve();
    _currentSnapshot = snapshot;
    _lastResolvedState = snapshot.ResolvedState;
    _stateSubject.OnNext(snapshot);
}
```

### 11.2 Degraded Initialization Order

If `Construct()` is called before either service is fully initialized, the machine waits until the first snapshot change from each source. Until then, `CurrentSnapshot` defaults to `PlayerState.Idle` with `StateDetail: "Awaiting initial snapshots"`.

### 11.3 CounterWindow While Moving

Per GDD §5.4: `CounterWindow` maps to `PlayerState.Attack` (priority 5). If the player is moving (priority 1), the machine correctly resolves to `Attack`. The animation layer sees `Attack` and plays the counter blend. Locomotion still updates independently.

---

## 12. Animation Routing — Complete Switch

```csharp
private void PlayAnimationForState(PlayerStateSnapshot snapshot) {
    if (_animationService == null) return;

    switch (snapshot.ResolvedState) {
        case PlayerState.Idle:
        case PlayerState.Moving:
        case PlayerState.TargetFocusMove:
            _animationService.PlayLocomotion(snapshot.LocomotionState, snapshot);
            break;
        case PlayerState.Dodge:
            _animationService.PlayDodge(new DodgeAnimationRequest(
                snapshot.CombatState, snapshot.StateDetail));
            break;
        case PlayerState.Parry:
            _animationService.PlayParry(new ParryAnimationRequest(
                snapshot.CombatState, snapshot.StateDetail));
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

private static CombatActionType ResolveAttackType(PlayerStateSnapshot snapshot) {
    var actionType = snapshot.LastResolutionResult?.ActionType
                     ?? CombatActionType.LightAttack;
    if (actionType == CombatActionType.LightAttack || actionType == CombatActionType.HeavyAttack)
        return actionType;
    return CombatActionType.LightAttack;
}
```

Note: `LastResolutionResult` is currently on `M0CombatSnapshot`, not on `PlayerStateSnapshot`. The GDD's `PlayerStateSnapshot` does not include `LastResolutionResult`. To resolve attack type here without that field, we can:
1. Add `CombatActionRequestResult LastActionResult` and/or `CombatResolutionResult LastResolutionResult` to `PlayerStateSnapshot`
2. Or pass it through `StateDetail`

**Recommendation:** Add `LastResolutionResult` to `PlayerStateSnapshot` for animation routing fidelity.

---

## 13. Implementation Order

The recommended order minimizes breakage and allows incremental testing:

```txt
Phase 1: Contracts (no behavior change)
─────────────────────────────────────────
Step 1:  Add PlayerState enum to M0Contracts.cs (or new file)
Step 2:  Add PlayerStateSnapshot readonly struct (new file)
Step 3:  Add PlayerStateDebugSnapshot (new file)
Step 4:  Add DebugOverlayChannelId.PlayerState to M0Contracts.cs
Step 5:  Add IPlayerStateMachine interface (new file)

Phase 2: PlayerStateMachine implementation (self-contained)
────────────────────────────────────────────────────────────
Step 6:  Implement PlayerStateMachineFactory (new file)
Step 7:  Implement PlayerStateMachine class (new file)
         - Constructor with null-safe subscriptions
         - Event handlers
         - Priority resolution
         - Aggregation logic
         - Dodge displacement bridge absorption
         - Animation routing
         - Debug snapshot
         - Dispose

Phase 3: Integration (one file at a time)
─────────────────────────────────────────
Step 8:  Add PlayLocomotion(state, fullSnapshot) to IPlayerAnimationService
Step 9:  Update AnimancerPlayerAnimationDriver to implement new overload
Step 10: Refactor M0AnimationPresentationAdapter
         - Add ObservePlayerState(IPlayerStateMachine)
         - Remove ObserveCombatSnapshot / ObserveLocomotionSnapshot
         - Add IDisposable subscription cleanup
Step 11: Refactor M0GameplayTickHandler
         - Inject IPlayerStateMachine
         - Remove _dodgeDisplacementBridge
         - Remove dodge bridge handling in OnCombatSnapshotChanged
         - Wire PlayerStateMachine to animation adapter in Construct()
         - Remove animation forwarding from OnLocomotionSnapshotChanged
Step 12: Register PlayerStateMachine in M0RuntimeServiceCompositionRegistrar
Step 13: Wire animation adapter in M0SceneCompositionRegistrar
Step 14: Delete M0DodgeDisplacementBridge.cs

Phase 4: Verification
─────────────────────
Step 15: Verify compilation — no dead code references
Step 16: Run existing combat + locomotion tests
Step 17: Run smoke test — dodge should still trigger displacement
Step 18: Verify debug overlay shows PlayerState channel
```

---

## 14. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Event subscription order: PlayerStateMachine misses first snapshot from one source | Medium | Medium | Use `_hasReceivedCombatSnapshot`/`_hasReceivedLocomotionSnapshot` flags; publish only after both received |
| `PlayerState` flickers during encounter reset (transient Disabled) | Medium | Low | Per GDD §5.5: correct behavior, one frame transient. Consumers use `DistinctUntilChanged()` if needed |
| `LocomotionState` enum lacks `TargetFocusMove` | High | Low | Until TargetFocusMove is added, it maps to Idle — no incorrect behavior, just neutral state |
| Animation timing regression: old system forwarded every combat state; new system only fires on ResolvedState change | Medium | High | Verify: AttackStartup→AttackActive normally keeps same PlayerState (Attack), so no fire. But the old adapter tracked `_lastCombatState` and fired on every sub-state change. **This is the single biggest behavioral change.** Animation crossfades should still work because PlayerStateMachine fires on entry to Attack (AttackStartup), and Animancer handles sub-state blending internally. |
| `LastResolutionResult` not in `PlayerStateSnapshot` | Low | Medium | Add it to the struct if attack type resolution is needed for animation calls |
| Circular dependency: PlayerStateMachine depends on animation service, animation adapter depends on PlayerStateMachine | Low | Low | PlayerStateMachine depends on interface (IPlayerAnimationService), not the adapter. Adapter depends on interface (IPlayerStateMachine). Both are registered independently. No cycle. |
| R3 Subject memory leak if Dispose not called | Low | High | `IDisposable` pattern + VContainer cleanup ensures disposal when gameplay scope is released |
| `IPlayerAnimationService.PlayLocomotion(LocomotionState, PlayerStateSnapshot)` — existing implementation gets a new method it doesn't implement | Low | High | Must be implemented in `AnimancerPlayerAnimationDriver`. For M0, can call existing `PlayLocomotion(LocomotionStateSnapshot snapshot)` internally, ignoring the new `fullSnapshot` parameter |

---

## 15. Verification Checklist

- [ ] `PlayerStateMachine.Dispose()` unsubscribes from both source events
- [ ] `PlayerStateMachine.Dispose()` disposes R3 `Subject`
- [ ] `StateChanges` observable fires only when `ResolvedState` changes
- [ ] `TryBeginDodgeDisplacement()` called exactly once per Dodge entry
- [ ] `IPlayerAnimationService` receives correct animation requests per `ResolvedState`
- [ ] Degraded mode: null combat core → locomotion-only resolution
- [ ] Degraded mode: null locomotion → combat-only resolution
- [ ] Degraded mode: both null → always `Disabled`
- [ ] `M0DodgeDisplacementBridge.cs` removed with no remaining references
- [ ] `DebugOverlayChannelId.PlayerState` added
- [ ] `PlayerStateDebugSnapshot` available via `CreateDebugSnapshot()`
- [ ] `M0AnimationPresentationAdapter` no longer subscribes to combat/locomotion snapshots directly
- [ ] All existing combat state transitions still trigger visual feedback via `M0GameplayTickHandler`
