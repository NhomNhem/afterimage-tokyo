## ADDED Requirements

### Requirement: Player Locomotion SHALL own movement truth
The system MUST treat Player Locomotion as the authoritative owner of movement state for M0. Input, Combat Core, Camera, Target Context, and Animator MUST NOT own or override movement truth.

#### Scenario: Movement truth stays in locomotion
- **WHEN** movement state changes during the M0 duel
- **THEN** the resulting authoritative movement state MUST be owned by Player Locomotion

#### Scenario: Other systems remain non-authoritative
- **WHEN** Input, Combat Core, Camera, Target Context, or Animator observe movement
- **THEN** those systems MUST treat locomotion state as read-only authority

### Requirement: Raw movement intent SHALL be consumed as data only
The system MUST consume raw movement intent from the input routing layer as data only and MUST NOT require Input Mapping to validate movement truth.

#### Scenario: Raw move intent is accepted as input data
- **WHEN** input routing provides a movement intent snapshot
- **THEN** Player Locomotion MUST be able to read that intent without asking Input to decide validity

#### Scenario: Input does not own movement validation
- **WHEN** movement is restricted or recovered later
- **THEN** the restriction MUST be represented outside Input Mapping

### Requirement: Player Locomotion SHALL expose a read-only snapshot
The system MUST expose locomotion state through a read-only snapshot suitable for debug consumption and downstream observation.

#### Scenario: Snapshot reflects current locomotion state
- **WHEN** locomotion changes state between idle, moving, restricted, or recovering
- **THEN** the latest snapshot MUST reflect that current state

#### Scenario: Snapshot cannot be mutated by consumers
- **WHEN** a consumer reads the locomotion snapshot
- **THEN** the consumer MUST NOT be able to mutate the authoritative locomotion state through that snapshot

### Requirement: Player Locomotion SHALL represent movement restriction and recovery contexts
The system MUST represent movement restriction and recovery/action-lock seams as explicit context data that Combat Core or adjacent gameplay systems can influence without taking over movement truth.

#### Scenario: Restriction context is visible
- **WHEN** movement is restricted by a combat or gameplay condition
- **THEN** locomotion MUST expose a restriction context that explains the restriction source or reason

#### Scenario: Recovery context is visible
- **WHEN** locomotion is recovering from a committed action
- **THEN** locomotion MUST expose a recovery context that explains the recovery source or reason

### Requirement: Camera-relative movement basis SHALL remain read-only and deferred
The system MUST treat camera-relative movement basis as read-only context if represented and MUST NOT let Camera own movement truth.

#### Scenario: Basis can be observed without owning movement
- **WHEN** locomotion receives a camera-relative basis placeholder
- **THEN** the basis MUST be read-only context and not the source of movement authority

#### Scenario: Camera remains non-authoritative
- **WHEN** camera state changes
- **THEN** locomotion truth MUST remain owned by Player Locomotion

### Requirement: Animator SHALL not own locomotion truth
The system MUST keep Animator and root motion non-authoritative for locomotion truth in M0.

#### Scenario: Animation remains presentation-only
- **WHEN** animation state changes
- **THEN** locomotion truth MUST remain unchanged unless Player Locomotion changes it

#### Scenario: Root motion is deferred
- **WHEN** root motion is present later
- **THEN** it MUST not become the source of locomotion authority in this skeleton

### Requirement: Locomotion debug data SHALL be read-only
The system MUST expose locomotion debug data in read-only form for future Debug Overlay consumption.

#### Scenario: Debug can inspect locomotion
- **WHEN** debug overlay reads locomotion state
- **THEN** it MUST be able to read the latest snapshot without mutating gameplay truth

#### Scenario: Debug data remains immutable
- **WHEN** a consumer receives locomotion debug data
- **THEN** the consumer MUST NOT be able to change authoritative locomotion state through that data
