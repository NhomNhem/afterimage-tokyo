## ADDED Requirements

### Requirement: Animator Observer Adapters Are Presentation-Only

The M0 animation observer adapter stack shall observe CombatCore, Locomotion, and EnemyIntent snapshots and route them to animation drivers without owning, modifying, or deciding any gameplay truth.

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
- **THEN** the animation driver logs a warning via `INhemLogger`
- **AND** gameplay continues without interruption (no NullReferenceException, no state corruption)
- **AND** the combat loop (read → evade/parry → counter → reveal) remains functional

#### Scenario: Root motion does not control movement
- **WHEN** an animation clip with root motion data is played
- **THEN** `Animator.applyRootMotion` is set to `false` before playback
- **AND** character position is determined solely by `M0PlayerLocomotion` position truth
- **AND** disabling the Animator component does not prevent character movement

#### Scenario: Duplicate state observations are skipped
- **WHEN** `M0AnimationPresentationAdapter` receives a snapshot with the same state as the previous observation
- **THEN** no animation service method is called
- **AND** the animation clip is not restarted

#### Scenario: DI composition succeeds with animation components wired
- **WHEN** `GameplayLifetimeScope` builds the VContainer scope with `M0AnimationPresentationAdapter`, `AnimancerPlayerAnimationDriver`, and `AnimancerEnemyAnimationDriver` registered
- **THEN** no `VContainerException` is thrown
- **AND** `M0GameplayTickHandler` receives non-null animation adapter reference
- **AND** runtime starts without DI errors
