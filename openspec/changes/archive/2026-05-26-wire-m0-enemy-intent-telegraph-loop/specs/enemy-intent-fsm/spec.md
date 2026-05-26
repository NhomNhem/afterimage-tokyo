## ADDED Requirements

### Requirement: Enemy Intent FSM Advances Through Duel Loop States

`M0EnemyIntentModel` SHALL advance through the M0 duel intent loop states when driven by a tick caller and a loop driver. The FSM SHALL cycle deterministically: `Idle → Telegraph → Commit → Active → Recovery → Idle`. State transitions SHALL only occur through explicit method calls (`EnterIdle`, `EnterTelegraph`, `EnterCommit`, `EnterActive`, `EnterRecovery`). Tick advances timers within a state; it does not decide state transitions.

#### Scenario: Initial state is Idle

- **WHEN** `M0EnemyIntentModel` is constructed
- **THEN** `Snapshot.State` is `EnemyIntentState.Idle`
- **AND** `Snapshot.IsTelegraphing` is false
- **AND** `Snapshot.PunishWindow.IsOpen` is false

#### Scenario: Transition to Telegraph state

- **WHEN** `EnterTelegraph(telegraphId, durationSeconds, reason)` is called
- **THEN** `Snapshot.State` is `EnemyIntentState.Telegraph`
- **AND** `Snapshot.IsTelegraphing` is true
- **AND** `Snapshot.Telegraph.IsActive` is true
- **AND** `Snapshot.Telegraph.TelegraphId` equals the provided telegraphId
- **AND** `Snapshot.RemainingSeconds` equals the provided durationSeconds

#### Scenario: Telegraph duration decrements on Tick; state does not auto-advance

- **WHEN** `EnterTelegraph("TelegraphA", 1.0f, "test")` is called
- **AND** `Tick(0.4f)` is called
- **THEN** `Snapshot.State` is still `EnemyIntentState.Telegraph`
- **AND** `Snapshot.RemainingSeconds` is approximately 0.6f
- **AND** `Snapshot.Telegraph.RemainingSeconds` is approximately 0.6f

#### Scenario: Transition to Commit state clears telegraph and sets attack intent

- **WHEN** `EnterCommit(attackIntentContext, durationSeconds, reason)` is called
- **THEN** `Snapshot.State` is `EnemyIntentState.Commit`
- **AND** `Snapshot.Telegraph.IsActive` is false
- **AND** `Snapshot.AttackIntent.AttackId` equals the provided attackId
- **AND** `Snapshot.AttackIntent.AttackTags.Tags` contains the provided tag values

#### Scenario: Transition to Active state preserves attack intent from Commit

- **WHEN** `EnterActive(durationSeconds, reason)` is called after `EnterCommit`
- **THEN** `Snapshot.State` is `EnemyIntentState.Active`
- **AND** `Snapshot.AttackIntent.AttackId` is not empty (retained from Commit)

#### Scenario: Transition to Active from Idle has empty attack intent

- **WHEN** `EnterActive(durationSeconds, reason)` is called directly without a prior `EnterCommit`
- **THEN** `Snapshot.State` is `EnemyIntentState.Active`
- **AND** `Snapshot.AttackIntent.AttackId` is empty string

#### Scenario: Transition to Recovery with punish window opens punish context

- **WHEN** `EnterRecovery(durationSeconds, reason, openPunishWindow: true, punishWindowSeconds, punishSource)` is called
- **THEN** `Snapshot.State` is `EnemyIntentState.Recovery`
- **AND** `Snapshot.PunishWindow.IsOpen` is true
- **AND** `Snapshot.PunishWindow.Source` equals the provided punishSource
- **AND** `Snapshot.PunishWindow.RemainingSeconds` is greater than 0

#### Scenario: Punish window closes via Tick expiry

- **WHEN** in Recovery state with `punishWindowSeconds = 0.25f`
- **AND** `Tick(0.3f)` is called
- **THEN** `Snapshot.PunishWindow.IsOpen` is false
- **AND** `Snapshot.PunishWindow.RemainingSeconds` is 0

#### Scenario: Transition to Recovery without punish window leaves punish context closed

- **WHEN** `EnterRecovery(durationSeconds, reason, openPunishWindow: false, 0f, "")` is called
- **THEN** `Snapshot.State` is `EnemyIntentState.Recovery`
- **AND** `Snapshot.PunishWindow.IsOpen` is false

#### Scenario: Return to Idle clears all active contexts

- **WHEN** `EnterIdle(reason)` is called from any state
- **THEN** `Snapshot.State` is `EnemyIntentState.Idle`
- **AND** `Snapshot.IsTelegraphing` is false
- **AND** `Snapshot.Telegraph.IsActive` is false
- **AND** `Snapshot.PunishWindow.IsOpen` is false
- **AND** `Snapshot.AttackIntent.AttackId` is empty string

---

### Requirement: EnemyIntentSnapshot is Read-Only

`EnemyIntentSnapshot` SHALL be exposed as a read-only value type. External consumers (Debug Overlay, Combat Core) SHALL only be able to read snapshot data; they SHALL NOT be able to mutate enemy intent state through the snapshot. The snapshot SHALL be a `readonly struct` with no settable properties.

#### Scenario: Snapshot is a value type copy

- **WHEN** `model.Snapshot` is accessed multiple times
- **THEN** each access returns an independent value; modifying a local copy does not affect the model's internal state

#### Scenario: Snapshot has no mutable setters

- **WHEN** the snapshot interface is inspected
- **THEN** all properties are read-only (get-only); no property has a public or internal setter

#### Scenario: Snapshot reflects state at the time of last state entry

- **WHEN** `EnterTelegraph` is called and then `Snapshot` is accessed
- **THEN** snapshot reflects Telegraph state with correct telegraphId and duration

---

### Requirement: Enemy Intent Does Not Apply Damage or Mutate Owned Truth

`M0EnemyIntentModel` SHALL NOT apply damage, SHALL NOT mutate player health, SHALL NOT call Combat Core resolution methods, SHALL NOT modify Target Context, and SHALL NOT trigger Memory VFX. Enemy Intent owns only its own FSM state.

#### Scenario: Enemy intent source file contains no damage application

- **WHEN** `Assets/_Project/Code/Enemy/M0EnemyIntentModel.cs` is inspected
- **THEN** the file contains no reference to `ApplyDamage`, `TakeDamage`, `Health`, `OnTrigger`, `OnCollision`, `AnimationEvent`, `AudioSource`, `ParticleSystem`, or `Cinemachine`

#### Scenario: Enemy intent contains no forbidden Unity APIs

- **WHEN** `Assets/_Project/Code/Enemy/M0EnemyIntentModel.cs` is inspected
- **THEN** the file contains no reference to `NavMesh`, `NavMeshAgent`, `Animator`, `GetComponent<`, `FindObjectOfType`, `FindFirstObjectByType`, `GameObject.Find`, `Resources.Load`, `RegisterGeneratedFor<`, or legacy `UnityEngine.Input`

#### Scenario: Enemy intent assembly references only GlassRefrain.Core

- **WHEN** `Assets/_Project/Code/Enemy/GlassRefrain.Enemy.asmdef` is inspected
- **THEN** the references array contains only `GlassRefrain.Core`; no reference to Health, Combat, Memory, Locomotion, or Targeting assemblies

#### Scenario: SnapshotChanged event carries no mutable state

- **WHEN** `model.SnapshotChanged` fires after a state transition
- **THEN** the event argument is `EnemyIntentSnapshot` (readonly struct); subscribers cannot mutate internal model state through it

---

### Requirement: EnemyAttackTagSet Communicates Defensive Availability

The attack tag set attached to `EnemyAttackIntentContext` SHALL communicate which defensive options are relevant for this attack (e.g., `DodgePunishable`, `ParryEligible`, `CounterOnWhiff`). Combat Core reads this context from the snapshot to inform its defensive validation. Enemy Intent does not decide whether a defensive action succeeded.

#### Scenario: Attack tags are preserved from Commit through Active

- **WHEN** `EnterCommit` is called with an `EnemyAttackIntentContext` containing tags `["DodgePunishable", "ParryEligible"]`
- **AND** `EnterActive` is then called
- **THEN** `Snapshot.AttackIntent.AttackTags.Tags` still contains `"DodgePunishable"` and `"ParryEligible"`

#### Scenario: Attack tags are empty in Idle and Telegraph states

- **WHEN** `model` is in `Idle` state or `Telegraph` state
- **THEN** `Snapshot.AttackIntent.AttackTags.Tags` is an empty array or has length 0

#### Scenario: Tags array contains the configured M0 prototype tags

- **WHEN** the M0 prototype loop driver constructs its `EnemyAttackIntentContext`
- **THEN** the tag set includes at minimum: `"DodgePunishable"`, `"ParryEligible"`, `"CounterOnWhiff"`
