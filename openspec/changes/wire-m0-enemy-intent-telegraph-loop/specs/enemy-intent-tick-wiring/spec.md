## ADDED Requirements

### Requirement: M0GameplayTickHandler Ticks M0EnemyIntentModel Each Frame

`M0GameplayTickHandler` SHALL inject `M0EnemyIntentModel` via VContainer and call `model.Tick(Time.deltaTime)` in its `Update()` method each frame, alongside the existing locomotion tick. The injection SHALL be manual (VContainer `[Inject]` attribute on `Construct()`). Enemy intent timing counters (telegraph remaining, punish window remaining) SHALL advance in real time.

#### Scenario: Enemy intent tick advances telegraph remaining seconds

- **WHEN** `M0EnemyIntentModel` is in Telegraph state with `RemainingSeconds = 1.0f`
- **AND** `M0GameplayTickHandler.Update()` runs with `Time.deltaTime = 0.1f`
- **THEN** `model.Snapshot.RemainingSeconds` decreases by approximately 0.1f per frame

#### Scenario: Enemy intent tick advances punish window remaining seconds

- **WHEN** `M0EnemyIntentModel` is in Recovery state with `PunishWindow.IsOpen = true` and `RemainingSeconds = 0.3f`
- **AND** `M0GameplayTickHandler.Update()` runs for multiple frames
- **THEN** `model.Snapshot.PunishWindow.RemainingSeconds` decreases toward 0 and eventually `IsOpen` becomes false

#### Scenario: Null model guard does not throw

- **WHEN** `M0EnemyIntentModel` is null (not injected)
- **THEN** `M0GameplayTickHandler.Update()` continues without exception

---

### Requirement: M0EnemyIntentLoopDriver Drives Scripted Duel Sequence

`M0EnemyIntentLoopDriver` SHALL be a MonoBehaviour that holds authored timing constants as `[SerializeField]` fields and drives `M0EnemyIntentModel` through the scripted duel sequence: `Idle → Telegraph → Commit → Active → Recovery → Idle (repeat)`. The loop driver SHALL receive `M0EnemyIntentModel` via VContainer `[Inject]`. The loop SHALL run as a coroutine or timer-based update. The loop SHALL be deterministic — no random timing, no decision logic, no branching based on player state.

#### Scenario: Loop driver runs full cycle Idle → Telegraph → Commit → Active → Recovery → Idle

- **GIVEN** `idleDuration`, `telegraphDuration`, `commitDuration`, `activeDuration`, `recoveryDuration` are all configured with positive values
- **WHEN** `M0EnemyIntentLoopDriver` starts
- **THEN** enemy intent state advances in order: `Idle → Telegraph → Commit → Active → Recovery → Idle`
- **AND** the cycle repeats from `Idle` after the recovery duration elapses

#### Scenario: Telegraph phase duration is respected before Commit

- **GIVEN** `telegraphDuration = 1.0f`
- **WHEN** the loop enters Telegraph
- **THEN** state remains `Telegraph` until approximately 1.0 seconds of real time have elapsed
- **AND** state transitions to `Commit` only after the configured duration

#### Scenario: Loop driver does not advance state faster than configured timing

- **GIVEN** all durations are set to 0.5f
- **WHEN** 0.3f has elapsed since entering Telegraph
- **THEN** state is still `Telegraph`, not `Commit`

#### Scenario: Punish window is opened during Recovery

- **WHEN** the loop transitions into Recovery
- **THEN** `M0EnemyIntentModel.Snapshot.PunishWindow.IsOpen` is true
- **AND** `Snapshot.PunishWindow.RemainingSeconds` is positive

#### Scenario: Loop driver contains no AI decision logic

- **WHEN** `Assets/_Project/Code/Enemy/M0EnemyIntentLoopDriver.cs` is inspected
- **THEN** the file contains no reference to `NavMesh`, `NavMeshAgent`, scoring, utility functions, behavior trees, or conditional player-state checks

#### Scenario: Loop driver contains no forbidden APIs

- **WHEN** `Assets/_Project/Code/Enemy/M0EnemyIntentLoopDriver.cs` is inspected
- **THEN** the file contains no reference to `FindObjectOfType`, `FindFirstObjectByType`, `GameObject.Find`, `Resources.Load`, `RegisterGeneratedFor<`, `UnityEngine.Input;`, `InputManager`, or `NhemDangFugBixs.Attributes`

---

### Requirement: Manual VContainer DI Wiring for Loop Driver

`M0EnemyIntentLoopDriver` SHALL be registered in `GameplayLifetimeScope` using `RegisterComponent` (manual scene component registration per ADR-0004). `M0EnemyIntentModel` SHALL be injected into the loop driver via `[Inject]`. No automatic scanning, no generated DI.

#### Scenario: Loop driver receives M0EnemyIntentModel via injection

- **WHEN** `GameplayLifetimeScope` builds the container
- **THEN** `M0EnemyIntentLoopDriver.Construct(M0EnemyIntentModel)` is called with the singleton instance

#### Scenario: Loop driver serialized field is assigned in scene

- **WHEN** the scene is loaded
- **THEN** `GameplayLifetimeScope.loopDriver` serialized field is not null
- **AND** `RegisterComponent(loopDriver)` is called in `Configure()`

#### Scenario: No generated DI patterns used

- **WHEN** `GameplayLifetimeScope.cs` and `M0EnemyIntentLoopDriver.cs` are inspected
- **THEN** neither file contains `RegisterGeneratedFor<`, `[NhemDangFugBixs.Attributes...]`, or any automatic scanning pattern

---

### Requirement: Debug Overlay Receives Live EnemyIntent Snapshot

The `M0DebugOverlaySnapshotAggregator.Capture()` call in the gameplay tick path SHALL receive the current `M0EnemyIntentModel.Snapshot` so the `EnemyIntent` channel displays live state, `IntentLabel`, `IsTelegraphing`, `RemainingSeconds`, and `PunishWindow` data. The Debug Overlay remains read-only.

#### Scenario: Debug Overlay EnemyIntent channel shows active state

- **WHEN** PlayMode is running and the loop driver is active
- **AND** the Debug Overlay is toggled on
- **THEN** the EnemyIntent channel shows the current `EnemyIntentState` enum label
- **AND** the channel shows the current `IntentLabel` reason string
- **AND** when in Telegraph state, the channel shows a positive `RemainingSeconds` value that decreases over time

#### Scenario: Debug Overlay does not mutate enemy intent state

- **WHEN** `M0DebugOverlaySnapshotAggregator.Capture(enemyIntentSnapshot: model.Snapshot, ...)` is called
- **THEN** the aggregator reads the snapshot as a value copy; the model's internal state is unchanged
