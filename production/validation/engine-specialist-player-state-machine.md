# Engine Specialist Validation — PlayerStateMachine Architecture

> **Validator**: OpenCode (unity-specialist)
> **Date**: 2026-06-16
> **Document**: `production/architecture/player-state-machine-arch.md`
> **GDD**: `design/gdd/player-state-machine.md`
> **Engine**: Unity 6000.3.x, URP, Animancer, R3, VContainer

---

## 1. Architecture Idiom

### Q: Is the pure C# service + interface + VContainer factory pattern idiomatic for Unity 6 / this project?

**YES.** The existing codebase follows this pattern exactly. `M0CombatCore` (pure C# sealed class + `IM0CombatCore` interface + factory lambda registration in `M0RuntimeServiceCompositionRegistrar`) and `M0PlayerLocomotion` (`IM0PlayerLocomotion` interface + factory lambda) are the canonical examples. `PlayerStateMachine` mirrors this structure.

The factory decomposition (`PlayerStateMachineFactory.Create()`) matches the existing pattern where constructors are called explicitly in registration lambdas (see `M0RuntimeServiceCompositionRegistrar.cs:31-40`). The nullable-parameter degraded-mode approach is a slight divergence — no existing service uses it — but is justified by the architecture's stated M0 prototyping context.

### Q: Are there engine-native systems (Animancer, Unity Animator, ECS) that should replace any proposed custom code?

**NO.** The architecture does not propose any custom code that replaces an engine-native system. Animancer is already used via `AnimancerPlayerAnimationDriver` and the proposed `IPlayerAnimationService` routing delegates to it. ECS is not used anywhere in the project — introducing it for this would be over-engineering. The architecture's single-observable approach replaces the existing dual `Action<T>` observer pattern, which is a pure C# improvement, not an engine-native concern.

### Q: Are any proposed APIs deprecated or changed in Unity 6000.3.x?

**YES — minor concern.** The architecture proposes `new Subject<PlayerStateSnapshot>()` from R3. This is correct usage. However, note that in Unity 6000, `System.IObservable<T>` can be used with `UniTask`'s `await foreach` pattern for async streams. The architecture doesn't consider this alternative, but that's acceptable — R3 `Observable<T>` is the project's declared reactive layer and `Subject<T>` → `Observable<T>` is the standard pattern.

No deprecated Unity APIs are used. Animancer's `animancer.Play(clip, fadeDuration)` usage in the existing driver matches the architecture's assumptions.

---

## 2. Event / Reactive Pattern

### Q: Is subscribing to `Action<T>` SnapshotChanged events from pure C# services the right approach, or should R3 `Observable` be used from the source?

**YES — subscribing to the existing `Action<T>` events is correct.**

Both `M0CombatCore` and `M0PlayerLocomotion` expose `Action<T>` events (`SnapshotChanged`). The architecture correctly consumes these as-is. Refactoring the source services to emit R3 `Observable<T>` would be a larger, unnecessary change for M0. The architecture's layering (keep source events, convert to R3 at the aggregate boundary) follows the Strangler Fig pattern and is pragmatic.

**CONCERNS — one edge case:** The existing `Action<T>` event pattern in `M0CombatCore` and `M0PlayerLocomotion` uses a null-check handler invocation pattern (`var handler = SnapshotChanged; if (handler != null) handler(...)`). This means:
- If `PlayerStateMachine` subscribes after the first snapshot is emitted, it misses the initial value.
- The architecture handles this with `_hasReceivedCombatSnapshot`/`_hasReceivedLocomotionSnapshot` flags, which is correct. But these flags depend on both services having emitted at least one snapshot. If the machine is constructed before Tick() runs for the first time, it correctly waits.
- **However**, the architecture's constructor subscribes directly to the source events, which is fine because `M0CombatCore` and `M0PlayerLocomotion` both emit their initial snapshot in their constructors via `RefreshSnapshot()`. So if `PlayerStateMachine` is constructed after both services (which VContainer's registration order guarantees), it will receive the initial snapshots. The `_hasReceived` flags are still needed for the race-condition case where both fire in the same frame.

### Q: The architecture uses `Subject<PlayerStateSnapshot>` in the PlayerStateMachine — is this appropriate for the R3 pattern in Unity 6?

**YES.** `Subject<T>` is the standard R3 class for manually-pushed observable sequences. The pattern:
```csharp
private readonly Subject<PlayerStateSnapshot> _stateSubject = new();
public Observable<PlayerStateSnapshot> StateChanges => _stateSubject;
```
...is the idiomatic R3 approach for converting imperative events (the `Action<T>` callbacks) into an observable stream. The `Dispose()` call on the subject matches R3's `IDisposable` pattern.

**One detail:** The architecture's `Dispose()` should call `_stateSubject.Dispose()`. After disposal, `OnNext()` on a disposed Subject throws. Since `Dispose()` also unsubscribes from the source events, this shouldn't happen — but adding a guard or using `try/finally` in the event handlers is a safety consideration.

### Q: Is `DistinctUntilChanged` the right operator for subscriber filtering?

**YES.** The architecture's contract says `StateChanges` only fires when the resolved `PlayerState` changes. `DistinctUntilChanged` is a defensive measure for consumers that don't want consecutive duplicates. Since the machine already deduplicates at the source, this is redundant for well-behaved consumers but harmless. It's also the standard R3 extension for this use case.

**One important thing:** The architecture should clarify whether `DistinctUntilChanged` compares by value equality (struct) or reference. `PlayerStateSnapshot` is a readonly struct, so R3's default equality comparer (`EqualityComparer<T>.Default`) will use structural equality. If any field other than `ResolvedState` changes while `ResolvedState` stays the same, the snapshot will compare as not-equal and fire. **This means `DistinctUntilChanged` on `PlayerStateSnapshot` does NOT equal filtering to ResolvedState changes only.** Consumers that filter by ResolvedState alone should use `.DistinctUntilChanged(s => s.ResolvedState)` instead. The architecture's `StateChanges` should document this clearly, or the machine should use a custom distinct comparer that only checks `ResolvedState`.

---

## 3. Animancer Integration

### Q: The architecture routes animation through `IPlayerAnimationService.PlayLocomotion(LocomotionState, PlayerStateSnapshot)` — is this consistent with Animancer's API (`AnimancerComponent.Play()`)?

**YES — with a caveat.** The existing `AnimancerPlayerAnimationDriver.Play()` at line 86 calls `animancer.Play(clip, transition.FadeDuration).Time = 0f`. The architecture routes through the same `IPlayerAnimationService` methods. The new `PlayLocomotion(LocomotionState, PlayerStateSnapshot)` overload delegates to the same underlying `Play()` method. No Animancer API conflict.

**CONCERNS:** The new overload receives `LocomotionState` (an enum value) instead of `LocomotionStateSnapshot` (a struct). The current `PlayLocomotion(LocomotionStateSnapshot)` uses `snapshot.State` and `snapshot.CameraMovementBasis` etc. The new overload strips away `CameraMovementBasis`, `MoveIntent`, and other context that the animation driver might want for blend decisions. The architecture mentions "the full snapshot" enables richer blend decisions — but the method signature takes `LocomotionState state` (enum only), not `LocomotionStateSnapshot`. If the driver needs the full locomotion context, this signature is insufficient. **Recommendation:** either pass `LocomotionStateSnapshot` instead of `LocomotionState`, or confirm the M0 scope doesn't need it.

### Q: Is there a risk that routing ALL animation through a single switch in PlayerStateMachine misses sub-state nuance that the current per-sub-state adapter provided?

**CONCERNS — Low risk, but documented.**

**Current behavior:** `M0AnimationPresentationAdapter.ObserveCombatSnapshot` fires on every `CombatCoreState` change:
- AttackStartup → `PlayAttack`
- AttackActive → `PlayAttack` (same clip, no-op'd by `_currentClipName` guard at line 81)
- AttackRecovery → `PlayAttack` (same, no-op'd)
- DodgeStartup/DodgeActive/DodgeRecovery → each calls `PlayDodge` (same clip, no-op'd)

**New behavior:** `PlayAnimationForState` fires once on entry to `PlayerState.Dodge`, `PlayerState.Attack`, etc.

**Impact:** The `AnimancerPlayerAnimationDriver.Play()` at line 81 already short-circuits repeated clip plays (`if (_currentClipName == clip.name) return;`). So the current system already produces only one effective `Play()` call per clip sequence. The architecture simply eliminates redundant calls that were already no-ops. **No behavioral regression for Animancer.**

**However**, if future sub-states need different animations (e.g., `AttackStartup` plays a wind-up, `AttackActive` plays a strike), the current architecture would need modification because `PlayerStateMachine` doesn't expose sub-state changes. The architecture correctly identifies this and defers it — for M0, all sub-states within a `PlayerState` use the same clip. This should be explicitly documented as a limitation for future work.

---

## 4. VContainer Registration

### Q: Is resolving `IPlayerAnimationService` in a factory lambda the right approach, or should it be injected differently?

**YES — factory lambda is correct.** The architecture's registration:
```csharp
builder.Register<IPlayerStateMachine>(resolver => {
    var combatCore = resolver.Resolve<M0CombatCore>();
    var locomotion = resolver.Resolve<IM0PlayerLocomotion>();
    var animationService = resolver.Resolve<IPlayerAnimationService>();
    var logger = resolver.Resolve<INhemLogger>();
    return PlayerStateMachineFactory.Create(combatCore, locomotion, animationService, logger);
}, Lifetime.Singleton).As<IPlayerStateMachine>().AsSelf();
```
This matches the existing patterns in `M0RuntimeServiceCompositionRegistrar.cs:31-40`. The `PlayerStateMachineFactory.Create()` wrapper adds degraded-mode logging, which is a reasonable factory concern.

### Q: The architecture uses `builder.Register<IPlayerStateMachine>(resolver => { ... })` — is this idiomatic VContainer usage?

**YES.** This is exactly how VContainer factory registrations work. The `resolver` parameter is an `IObjectResolver` that allows resolving other dependencies. The existing `M0CombatCore` registration uses the same pattern: `builder.Register(resolver => new M0CombatCore(combatTimingSettings, resolver.Resolve<INhemLogger>()), Lifetime.Singleton)`.

**One difference:** The architecture registers `.As<IPlayerStateMachine>().AsSelf()`. The existing pattern uses `.As<IM0CombatCore>().AsSelf()`. This is correct — it allows resolving by both interface and concrete type. However, no consumer currently resolves `PlayerStateMachine` by concrete type, so `.AsSelf()` may be unnecessary. Not a problem, just dead weight.

### Q: Registration order — steps 1-3 exist, step 4 is new. Any concerns?

**NO — order is correct.** The existing registration order in `GameplayLifetimeScope.Configure()`:
1. `M0RuntimeServiceCompositionRegistrar.Register()` — registers `M0CombatCore` and `M0PlayerLocomotion`
2. `M0SceneCompositionRegistrar.Register()` — registers scene components including `IPlayerAnimationService`
3. (after both) — PlayerStateMachine needs all three services registered

The architecture places PlayerStateMachine registration in `M0RuntimeServiceCompositionRegistrar`, which runs first. But the architecture's section 7.2 notes steps 1-3 must precede step 4. Since step 2 (`M0SceneCompositionRegistrar`) runs after step 1, and `IPlayerAnimationService` is registered in step 2, **PlayerStateMachine must be registered after step 2**, not in step 1.

**RECOMMENDATION:** Move PlayerStateMachine registration to `M0SceneCompositionRegistrar.Register()` or create a separate registration step after both registrars run. The current architecture doc (section 6.7, 7.1) puts it in `M0RuntimeServiceCompositionRegistrar`, which resolves before `M0SceneCompositionRegistrar` registers `IPlayerAnimationService`. This is a **registration order bug** that must be fixed.

---

## 5. Risk Assessment

### Q: Biggest risk flagged: old adapter fired on every combat sub-state change; new machine only fires on resolved PlayerState change. How much of a concern for Animancer?

**LOW CONCERN.** My analysis of the existing `AnimancerPlayerAnimationDriver` code at line 81 confirms:
```csharp
if (_currentClipName == clip.name) { return; }
```
Repeated `Play()` calls with the same clip are already no-ops. The old adapter's per-sub-state firing pattern was producing redundant calls that were silently ignored. The new architecture simply eliminates this redundancy. Animancer's crossfade system works on entries to new states, not on repeated calls to the same state.

**Edge case:** If the `M0PlayerAnimationSet` assigns different clips for `AttackStartup`, `AttackActive`, and `AttackRecovery` in the future, the current architecture would need modification. Document this as a future limitation.

### Q: Any other risks not already flagged?

**CONCERN — Dodge displacement timing change (MEDIUM).**

The current `M0DodgeDisplacementBridge`:
1. Arms on `DodgeStartup` entry (line 18)
2. Fires `TryBeginDodgeDisplacement()` on `DodgeActive` entry (line 23)

The proposed `OnResolvedStateChanged`:
1. Fires on first entry to `PlayerState.Dodge` (line 461-463)

Since `PlayerState.Dodge` maps to `CombatCoreState.DodgeStartup` in the priority table, **displacement will start one sub-state earlier** (during DodgeStartup instead of DodgeActive). This changes the feel of the dodge. The dodge displacement in `M0PlayerLocomotion` sets a distance and duration — starting it earlier means the displacement will partially overlap with the startup animation.

**Options:**
A. Keep the architecture as-is and retune dodge feel (simplest).
B. Add a one-frame delay to `OnResolvedStateChanged` for dodge displacement (adds complexity).
C. Keep `M0DodgeDisplacementBridge` but have it observe `PlayerStateMachine.StateChanges` instead of raw combat snapshots (cleaner bridge).

The architecture doc should flag this behavioral change explicitly. Recommend **Option C** as a middle ground, or note that the team should verify displacement timing feels correct.

**CONCERN — `M0SceneCompositionRegistrar.WirePresentationAdapters()` needs a container reference.**

The architecture's section 6.6 shows:
```csharp
var container = /* from RegisterBuildCallback */;
var playerStateMachine = container.Resolve<IPlayerStateMachine>();
_animationPresentationAdapter?.ObservePlayerState(playerStateMachine);
```

The current `WirePresentationAdapters()` at `M0SceneCompositionRegistrar.cs:87` has no container reference. The `RegisterBuildCallback` at line 77 does have `container`. The wiring should happen inside `RegisterBuildCallback` after the existing `WirePresentationAdapters()` call, or `WirePresentationAdapters()` should receive the container as a parameter. The architecture's code sketch is correct in intent but needs adaptation.

**CONCERN — `DebugOverlayAggregateSnapshot` is a closed struct with 9 fixed fields.**

Adding `PlayerState` as channel ID 9 requires either:
1. Adding a new field `PlayerState` to `DebugOverlayAggregateSnapshot` (breaking change — all construction sites must be updated)
2. Or routing `PlayerStateDebugSnapshot` through the existing channel list without adding a struct field

The architecture's section 8.1 vaguely says "Consider updating `DebugOverlayAggregateSnapshot` to include the new channel, or expose `PlayerStateDebugSnapshot` through the existing `CreateDebugSnapshot()` method." This needs a concrete decision. For M0 scope, exposing the snapshot through the debug overlay's `CreateDebugSnapshot()` polling pattern (like `LocomotionDebugSnapshot` and `CombatDebugSnapshot` already do) is simpler than modifying the closed struct.

**CONCERN — `LastResolutionResult` not on `PlayerStateSnapshot`.**

The architecture's section 12 identifies this. `ResolveAttackType()` in `PlayAnimationForState` needs `snapshot.LastResolutionResult.ActionType` to distinguish light/heavy attack. The GDD's `PlayerStateSnapshot` doesn't include this field. The architecture recommends adding it (line 793). **This must be done before Phase 4 verification** or the attack animation routing will always default to `LightAttack`.

---

## 6. Additional Edge Cases

1. **First R3 usage in the codebase.** No existing code uses R3. The team should verify the R3 package is installed and configure the Unity script compilation for it. The architecture assumes R3 import paths without specifying them.

2. **`OnResolvedStateChanged` is called inside `Resolve()`.** The architecture shows `OnResolvedStateChanged` called only when the resolved state changes. This is done inside `OnCombatSnapshotChanged` and `OnLocomotionSnapshotChanged`. But `TryPublishInitialSnapshot()` also calls `_stateSubject.OnNext()` and should also trigger `PlayAnimationForState`. The architecture must ensure the initial snapshot triggers animation routing, not just the observable.

3. **`M0AnimationPresentationAdapter` cleanup of old fields.** The architecture correctly removes `_lastCombatState`, `_lastAttackType`, `_lastLocomotionState` from the adapter. But `_lastEnemyIntentState` remains for enemy animation. This is fine and correctly documented.

4. **`_lastEnemyIntentState` usage in new adapter.** The architecture says `_lastEnemyIntentState` is still used by `ObserveEnemyIntentSnapshot` (which remains). The adapter's `ObserveEnemyIntentSnapshot` method is separate from the PlayerStateMachine flow, so no conflict.

---

## 7. Overall Verdict

**APPROVED WITH NOTES**

The architecture is well-structured, follows existing project patterns, and correctly addresses the core problem of unified player state aggregation. No fundamental design flaws were found.

### Required Before Implementation

| # | Item | Source |
|---|------|--------|
| 1 | **Fix registration order:** Move PlayerStateMachine registration after `IPlayerAnimationService` is registered (currently placed in `M0RuntimeServiceCompositionRegistrar` which runs before `M0SceneCompositionRegistrar` registers the animation service). | §7.2 |
| 2 | **Add `LastResolutionResult` to `PlayerStateSnapshot`** or the attack animation routing will always default to `LightAttack`. | §12 |
| 3 | **Document the `DistinctUntilChanged` behavior:** Struct-value equality on `PlayerStateSnapshot` will fire on any field change, not just `ResolvedState`. Use `.DistinctUntilChanged(s => s.ResolvedState)` for ResolvedState-only filtering. | §5 |

### Recommended Before Implementation

| # | Item | Source |
|---|------|--------|
| 4 | **Flag dodge displacement timing change** to the team. Displacement will start one sub-state earlier (DodgeStartup vs DodgeActive). Verify feel in playtest. | §6.5, §14 |
| 5 | **Decide `DebugOverlayAggregateSnapshot` approach** — modify the struct (breaking) or use polling pattern (non-breaking). Current architecture is vague. | §8.1 |
| 6 | **Consider using `LocomotionStateSnapshot` instead of `LocomotionState`** in the new `PlayLocomotion(LocomotionState, PlayerStateSnapshot)` overload, or confirm the simpler signature is sufficient for M0. | §6.8 |
| 7 | **Add disposal guard in `OnCombatSnapshotChanged`/`OnLocomotionSnapshotChanged`** if the subject might be accessed after disposal. | §3.1, §15 |
| 8 | **Ensure `TryPublishInitialSnapshot` triggers `PlayAnimationForState`**, not just the R3 subject. | §11.1 |

### How Implementation Plan Should Change

| Phase | Step | Change |
|-------|------|--------|
| 3 | Step 12 | Move PlayerStateMachine registration from `M0RuntimeServiceCompositionRegistrar` to `M0SceneCompositionRegistrar` (or a later registration step). |
| 1 | Step 2 | Add `LastResolutionResult` (or `CombatResolutionResult` equivalent) to `PlayerStateSnapshot` struct. |
| 3 | Step 9 | Use `LocomotionStateSnapshot` (not `LocomotionState`) in the new overload, or confirm scope. |
| 3 | Step 13 | Wire `IPlayerStateMachine` from `RegisterBuildCallback` container, not from `WirePresentationAdapters()` directly. |
