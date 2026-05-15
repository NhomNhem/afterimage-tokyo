## ADDED Requirements

### Requirement: Lock-On / Target Context SHALL own target truth
The system MUST treat Lock-On / Target Context as the authoritative owner of target focus state and target validity for M0. Input, Camera, Player Locomotion, Combat Core, and Animator MUST NOT own or override target truth.

#### Scenario: Target truth stays in target context
- **WHEN** target focus changes during the M0 duel
- **THEN** the resulting authoritative target state MUST be owned by Lock-On / Target Context

#### Scenario: Other systems remain non-authoritative
- **WHEN** Input, Camera, Player Locomotion, Combat Core, or Animator observe target state
- **THEN** those systems MUST treat target truth as read-only authority

### Requirement: Raw LockOn intent SHALL be consumed as a request source only
The system MUST consume raw `LockOn` intent from the input routing layer as request data only and MUST NOT require Input Mapping to validate target truth.

#### Scenario: LockOn intent is represented as a request
- **WHEN** input routing provides raw `LockOn` intent
- **THEN** Lock-On / Target Context MUST be able to interpret it as an acquire or release request source

#### Scenario: Input does not own target validation
- **WHEN** a target is accepted, rejected, or becomes invalid later
- **THEN** the reason and validity MUST be represented outside Input Mapping

### Requirement: Target context SHALL expose a read-only snapshot
The system MUST expose target focus state, target validity, and target direction/context through a read-only snapshot suitable for debug and downstream observation.

#### Scenario: Snapshot reflects current target state
- **WHEN** target focus or target validity changes
- **THEN** the latest snapshot MUST reflect the current target state

#### Scenario: Snapshot cannot be mutated by consumers
- **WHEN** a consumer reads target snapshot data
- **THEN** the consumer MUST NOT be able to mutate the authoritative target state through that snapshot

### Requirement: Target focus state SHALL be represented
The system MUST represent whether target focus is active or inactive and MUST distinguish acquire, focused, release, and invalid states if needed by the skeleton.

#### Scenario: Focus state is visible
- **WHEN** target focus is active or inactive
- **THEN** the target context MUST expose that state explicitly

#### Scenario: Focus transitions are distinguishable
- **WHEN** the player requests focus, releases focus, or the target becomes invalid
- **THEN** the target context MUST distinguish those states in its model

### Requirement: Target validity SHALL be represented
The system MUST represent whether the current target is valid and MUST expose a reason when the target becomes invalid or unavailable.

#### Scenario: Valid target is observable
- **WHEN** a current duel enemy remains targetable
- **THEN** the target context MUST expose the target as valid

#### Scenario: Invalid target is observable
- **WHEN** the target is defeated, removed, or otherwise unavailable
- **THEN** the target context MUST expose an invalid target state with a readable reason

### Requirement: Target direction/context SHALL be read-only and debug-consumable
The system MUST expose target direction/context data in read-only form for locomotion, camera, combat, and debug use.

#### Scenario: Direction/context can be observed
- **WHEN** locomotion or camera reads target direction/context
- **THEN** it MUST receive read-only data only

#### Scenario: Debug data remains immutable
- **WHEN** debug overlay reads target snapshot data
- **THEN** the consumer MUST NOT be able to change authoritative target truth through that data

### Requirement: Adjacent systems SHALL observe but not own target truth
The system MUST allow locomotion, camera, and combat to observe target context while keeping their roles non-authoritative for target truth.

#### Scenario: Locomotion can read target truth
- **WHEN** Player Locomotion needs orientation support
- **THEN** it MUST be able to read target context without owning target validity

#### Scenario: Camera can read target truth
- **WHEN** Lock-On & Combat Camera needs framing support
- **THEN** it MUST be able to read target context without owning target validity

#### Scenario: Combat can observe target truth
- **WHEN** Combat Core needs contextual observation
- **THEN** it MUST be able to read target context without deciding hit, dodge, parry, or counter validity
