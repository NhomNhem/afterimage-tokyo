## ADDED Requirements

### Requirement: Animator Observer Adapters Are Presentation-Only

Animator observer adapters SHALL remain presentation-only observers of gameplay snapshots. They SHALL NOT store, decide, or mutate gameplay truth for CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, MemoryState, Camera, Debug Overlay, or Encounter lifecycle. Animancer/Animator playback SHALL NOT define combat timing windows, hit results, movement truth, target truth, reveal truth, or encounter lifecycle state.

#### Scenario: Animation observes gameplay snapshots without owning gameplay truth
- **WHEN** CombatCore, PlayerLocomotion, or EnemyIntent emits a gameplay snapshot
- **THEN** the animation presentation adapter SHALL route the snapshot to the appropriate animation driver
- **AND** the animation driver SHALL NOT modify gameplay state, timing windows, hit results, movement truth, target truth, memory reveal truth, camera truth, debug overlay truth, or encounter lifecycle truth

#### Scenario: Player animation driver plays on combat state change
- **WHEN** `M0CombatCore` emits a `SnapshotChanged` event with a new `CombatCoreState`
- **THEN** `M0AnimationPresentationAdapter.ObserveCombatSnapshot` routes the snapshot to `IPlayerAnimationService`
- **AND** the appropriate animation method is called (PlayAttack, PlayDodge, PlayParry, PlayCounter, or PlayNeutral)
- **AND** no combat timing, CounterWindow, or resolution data is modified by the adapter or driver

#### Scenario: Player animation driver plays on locomotion state change
- **WHEN** `M0PlayerLocomotion` emits a `SnapshotChanged` event with a new `LocomotionState`
- **THEN** `M0AnimationPresentationAdapter.ObserveLocomotionSnapshot` routes the snapshot to `IPlayerAnimationService`
- **AND** locomotion animation is skipped if combat is not Neutral or Disabled
- **AND** no locomotion position, facing, or velocity data is modified by the adapter or driver

#### Scenario: Enemy animation driver plays on intent state change
- **WHEN** `M0EnemyIntentModel` emits a `SnapshotChanged` event with a new `EnemyIntentState`
- **THEN** `M0AnimationPresentationAdapter.ObserveEnemyIntentSnapshot` routes the snapshot to `IEnemyAnimationService`
- **AND** the appropriate animation method is called (PlayIdle, PlayIntent with Telegraph/Active/Recovery)
- **AND** no enemy intent timing, telegraph data, or punish window data is modified by the adapter or driver

#### Scenario: Missing animation clips do not break gameplay
- **WHEN** `M0PlayerAnimationSet` or `M0EnemyAnimationSet` has null clip references
- **THEN** the animation driver SHALL report the missing clip as a warning-level presentation issue via `INhemLogger`
- **AND** gameplay SHALL continue without interruption (no VContainerException, no NullReferenceException, no state corruption)
- **AND** the combat loop (read → evade/parry → counter → reveal) remains functional

#### Scenario: Root motion does not control movement
- **WHEN** an animation clip with root motion data is played
- **THEN** `Animator.applyRootMotion` SHALL remain `false` before playback
- **AND** character position SHALL be determined solely by `M0PlayerLocomotion` position truth
- **AND** disabling the Animator component SHALL NOT prevent character movement

#### Scenario: Duplicate state observations are skipped
- **WHEN** `M0AnimationPresentationAdapter` receives a snapshot with the same state as the previous observation
- **THEN** no animation service method is called
- **AND** the animation clip is not restarted

#### Scenario: DI composition succeeds with animation components wired
- **WHEN** `GameplayLifetimeScope` builds the VContainer scope with `M0AnimationPresentationAdapter`, `AnimancerPlayerAnimationDriver`, and `AnimancerEnemyAnimationDriver` registered
- **THEN** no `VContainerException` is thrown
- **AND** `M0GameplayTickHandler` receives non-null animation adapter reference
- **AND** runtime starts without DI errors
