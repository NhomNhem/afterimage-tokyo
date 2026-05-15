## ADDED Requirements

### Requirement: Encounter Lifecycle State Machine
The system SHALL maintain an explicit encounter lifecycle state machine for M0. The lifecycle SHALL include: Uninitialized, Preparing, Ready, Starting, Active, Completing, Completed, Failed, Aborted, and Resetting. The encounter SHALL transition only through explicit lifecycle requests and observed end conditions.

#### Scenario: Encounter begins uninitialized
- **WHEN** the encounter is constructed
- **THEN** the current state is Uninitialized

#### Scenario: Encounter can prepare and become ready
- **WHEN** preparation succeeds and readiness blockers are cleared
- **THEN** the state transitions to Ready

#### Scenario: Encounter can become active
- **WHEN** a start request is accepted while Ready
- **THEN** the state transitions to Starting and then Active

#### Scenario: Encounter can complete, fail, abort, and reset
- **WHEN** a valid completion, fail, abort, or reset request is observed
- **THEN** the state transitions through the corresponding lifecycle state and returns to a reusable idle-ready path

### Requirement: One Player and One Enemy Registration
The system SHALL support registration of exactly one player participant and one enemy participant for M0. Registration SHALL be explicit and SHALL surface invalid, missing, or duplicate participant conditions as readiness blockers.

#### Scenario: Player and enemy registration makes the encounter eligible for readiness
- **WHEN** one valid player and one valid enemy are registered
- **THEN** the encounter can move toward Ready if no other blockers exist

#### Scenario: Missing participant blocks readiness
- **WHEN** either the player or enemy participant is missing
- **THEN** readiness is blocked and the blocker is exposed

#### Scenario: Duplicate participant registration is surfaced
- **WHEN** a duplicate registration is attempted
- **THEN** the encounter records a debug-visible blocker or error state

### Requirement: Readiness Blocker Reporting
The system SHALL expose readiness blockers in read-only form. Blockers SHALL explain why the encounter is not yet ready to start, including missing participant references and invalid minimal configuration.

#### Scenario: Readiness blockers are visible before start
- **WHEN** the encounter is not ready
- **THEN** the snapshot exposes the blocker list or blocker reason

#### Scenario: Blockers clear when conditions become valid
- **WHEN** the missing requirement is satisfied
- **THEN** the blocker is removed and the encounter may become Ready

### Requirement: Start, End, Fail, Abort, and Reset Request/Result Shape
The system SHALL provide explicit request and result shapes for start, end, fail, abort, and reset actions. These shapes SHALL carry state, reason, and debug-readable outcome data.

#### Scenario: Start request reports why start succeeded or failed
- **WHEN** a start request is issued
- **THEN** the result indicates whether the encounter started and why

#### Scenario: End, fail, abort, and reset are explainable
- **WHEN** the encounter ends for completion, failure, abort, or reset
- **THEN** the result includes a debug-readable reason

### Requirement: Observe-Only Completion, Fail, and Reveal Context
The encounter framework SHALL observe completion, failure, reveal acceptance, and manual reset or abort signals only. It SHALL NOT validate combat results, reveal validity, or target truth. It MAY expose these observed conditions in read-only snapshot form.

#### Scenario: Encounter can observe enemy defeat
- **WHEN** the enemy is observed defeated by an owning system
- **THEN** the encounter may transition toward completion without owning the defeat logic

#### Scenario: Encounter can observe player defeat
- **WHEN** the player is observed defeated by Health
- **THEN** the encounter may transition toward failure without mutating health state

#### Scenario: Encounter can observe reveal acceptance
- **WHEN** Memory State reports accepted reveal context
- **THEN** the encounter may expose that observation in debug data without deciding reveal validity

### Requirement: Read-Only Encounter Snapshot
The system SHALL expose a read-only encounter snapshot. The snapshot SHALL include lifecycle state, registered participants, readiness blockers, observed end reasons, and key encounter observations such as reveal acceptance or defeat signals when available. The snapshot SHALL be immutable from the perspective of consumers.

#### Scenario: Snapshot reflects lifecycle state
- **WHEN** the snapshot is read
- **THEN** it reports the current encounter lifecycle state

#### Scenario: Snapshot exposes participants and blockers
- **WHEN** the snapshot is read while preparing or blocked
- **THEN** it includes registered participant references and blocker information

#### Scenario: Snapshot is read-only
- **WHEN** a consumer receives the snapshot
- **THEN** the consumer cannot mutate encounter ownership or lifecycle truth through it

### Requirement: Debug Visibility and Ownership Boundaries
The system SHALL surface debug-visible reasons for prepare, ready, start, complete, fail, abort, and reset decisions. It SHALL NOT own combat validation, enemy intent, health mutation, target switching, memory acceptance, or camera behavior.

#### Scenario: Debug can explain why encounter is not ready
- **WHEN** readiness fails
- **THEN** the reason is available to Debug Overlay

#### Scenario: Encounter does not own combat validation
- **WHEN** the encounter is active
- **THEN** combat result validation remains owned by Combat Core

#### Scenario: Encounter does not own target truth
- **WHEN** the encounter is active
- **THEN** runtime target truth remains owned by Lock-On / Target Context

