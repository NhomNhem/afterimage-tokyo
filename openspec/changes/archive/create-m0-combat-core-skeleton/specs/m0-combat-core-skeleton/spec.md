## ADDED Requirements

### Requirement: Combat Core SHALL own combat validation and result truth

The system MUST treat Combat Core as the authoritative owner of combat action validity, combat state truth, and combat result truth for M0. Input Mapping, Player Locomotion, Enemy Intent & Telegraph, Health/Damage/Hit Reaction, Lock-On & Combat Camera, Memory State, Animator, and Debug Overlay MUST NOT own or override combat validation or result truth.

#### Scenario: Combat truth stays in Combat Core
- **WHEN** a combat action is requested during the M0 duel
- **THEN** the resulting authoritative combat state and action result MUST be owned by Combat Core

#### Scenario: Other systems remain non-authoritative
- **WHEN** Input, Locomotion, Enemy, Camera, Animator, or Debug observe combat state
- **THEN** those systems MUST treat combat truth as read-only authority

### Requirement: Combat Core SHALL define a pure C# combat state model

The system MUST define a pure C# state model with all M0 combat states: Neutral, AttackStartup, AttackActive, AttackRecovery, DodgeStartup, DodgeActive, DodgeRecovery, ParryStartup, ParryActive, ParryRecovery, CounterWindow, CounterActive, HitReact, RevealBeat, Disabled.

#### Scenario: State model is inspectable
- **WHEN** combat transitions occur
- **THEN** the current combat state MUST be inspectable through a read-only snapshot

#### Scenario: State model is not owned by Animator
- **WHEN** the Animator plays combat visuals
- **THEN** the Animator MUST NOT own the authoritative combat state

### Requirement: Combat Core SHALL accept and validate combat action requests

The system MUST represent typed combat action requests (LightAttack, HeavyAttack, Dodge, Parry, Counter) and return accepted, rejected, or ignored results.

#### Scenario: Valid request is accepted
- **WHEN** a LightAttack request arrives while Combat Core is in Neutral
- **THEN** the request MUST be accepted and Combat Core transitions to AttackStartup

#### Scenario: Invalid request is rejected
- **WHEN** a Dodge request arrives while Combat Core is in AttackStartup (not DodgeStartup-eligible)
- **THEN** the request MUST be rejected with a readable reason

### Requirement: Combat Core SHALL emit action lock/recovery context

The system MUST emit ActionLockContext and RecoveryContext when entering committed action states or recovery states. Player Locomotion owns movement-side expression of those locks and recovery states.

#### Scenario: Lock context emitted on attack commit
- **WHEN** Combat Core transitions to AttackStartup
- **THEN** it MUST emit an ActionLockContext indicating that movement is locked or restricted

#### Scenario: Recovery context emitted after action
- **WHEN** Combat Core transitions to AttackRecovery
- **THEN** it MUST emit a RecoveryContext indicating that recovery is active

### Requirement: CounterWindow SHALL be represented as a placeholder state

The system MUST represent CounterWindow as an inspectable state with open/closed, source tag, elapsed time, and remaining duration fields. Full CounterWindow validation rules are deferred.

#### Scenario: CounterWindow opens after placeholder parry success
- **WHEN** a parry transition triggers CounterWindow in the skeleton placeholder
- **THEN** CounterWindowState MUST indicate open with the source tag and remaining duration

#### Scenario: CounterWindow closes after duration or on exit
- **WHEN** CounterWindow duration expires or the state exits
- **THEN** CounterWindowState MUST indicate closed

### Requirement: RevealRequestContext SHALL be represented as a placeholder

The system MUST emit RevealRequestContext when Combat Core transitions from CounterActive to RevealBeat. Memory State owns reveal request acceptance/rejection.

#### Scenario: Reveal request emitted after counter path
- **WHEN** Combat Core transitions CounterActive → RevealBeat
- **THEN** it MUST emit a RevealRequestContext with the combat result source

#### Scenario: Reveal request does not imply acceptance
- **WHEN** RevealRequestContext is emitted
- **THEN** Memory STILL owns acceptance or rejection of the reveal request

### Requirement: Combat Core SHALL expose a read-only combat snapshot

The system MUST expose a read-only M0CombatSnapshot containing current combat state, last action result, last resolution result, CounterWindow state, and active lock/recovery context. Debug Overlay and downstream observers MUST NOT be able to mutate Combat Core state through this snapshot.

#### Scenario: Snapshot reflects current combat truth
- **WHEN** combat state or last result changes
- **THEN** the latest snapshot MUST reflect the current combat truth

#### Scenario: Snapshot cannot be mutated by consumers
- **WHEN** a consumer reads M0CombatSnapshot
- **THEN** the consumer MUST NOT be able to mutate the authoritative combat state through that snapshot

### Requirement: Adjacent systems SHALL observe but not own combat truth

The system MUST allow Player Locomotion, Enemy Intent & Telegraph, Health/Damage/Hit Reaction, Memory State, Lock-On & Combat Camera, and Debug Overlay to observe combat state while keeping their roles non-authoritative for combat validation.

#### Scenario: Locomotion can read combat truth
- **WHEN** Player Locomotion needs action lock/recovery context
- **THEN** it MUST be able to read combat snapshot and action lock/recovery context without owning combat validation

#### Scenario: Memory State can read combat truth
- **WHEN** Memory State needs reveal request context
- **THEN** it MUST be able to read RevealRequestContext without Combat Core owning reveal acceptance

#### Scenario: Debug Overlay can read combat truth
- **WHEN** Debug Overlay needs to display combat state
- **THEN** it MUST be able to read M0CombatSnapshot without mutating combat state
