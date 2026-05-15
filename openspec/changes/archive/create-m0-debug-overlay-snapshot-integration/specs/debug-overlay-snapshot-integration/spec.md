## ADDED Requirements

### Requirement: Read-Only Aggregate Debug Snapshot
The system SHALL expose a read-only aggregate debug snapshot for M0. The snapshot SHALL combine read-only state from the required debug channels without mutating or reinterpreting gameplay truth.

#### Scenario: Aggregate snapshot is readable
- **WHEN** the aggregate snapshot is requested
- **THEN** it contains read-only data from the source systems

#### Scenario: Aggregate snapshot does not own gameplay truth
- **WHEN** the aggregate snapshot is built
- **THEN** it does not change the underlying source systems

### Requirement: Per-Channel Debug Groups
The system SHALL expose separate debug groups for Input, Locomotion, Target Context, Combat Core, Enemy Intent / Telegraph, Health / Damage / Hit Reaction, Memory State, Memory VFX Response, and Encounter Framework.

#### Scenario: All required channels are present
- **WHEN** the aggregate snapshot is built
- **THEN** each required debug channel is represented

#### Scenario: Channel groups remain independently readable
- **WHEN** a consumer reads one channel group
- **THEN** the other source systems remain unaffected

### Requirement: Simple Channel Visibility State
The system SHALL support simple read-only visibility/toggle state for each debug channel. Visibility SHALL be controlled by the debug overlay layer only and SHALL NOT affect gameplay state.

#### Scenario: Channel visibility can be toggled
- **WHEN** a channel visibility flag is changed
- **THEN** the aggregate snapshot reflects the new visibility state

#### Scenario: Visibility does not mutate gameplay
- **WHEN** a channel is hidden or shown
- **THEN** source gameplay systems remain unchanged

### Requirement: Last Accepted or Rejected Reason Pass-Through
The system SHALL surface last accepted or rejected reason data only from source snapshots, source results, or explicit upstream context. The overlay SHALL NOT infer missing reasons.

#### Scenario: Source reason is passed through
- **WHEN** a source system provides a last reason value
- **THEN** the aggregate snapshot can expose that value read-only

#### Scenario: Missing reason is not invented
- **WHEN** a source system does not provide a reason
- **THEN** the overlay does not fabricate one

### Requirement: No Gameplay Authority
The debug overlay aggregation model SHALL remain read-only and SHALL NOT own or change combat, locomotion, target, enemy, health, memory, memory VFX, or encounter truth.

#### Scenario: Overlay cannot mutate source systems
- **WHEN** the aggregate snapshot is assembled
- **THEN** no source system state is changed

#### Scenario: Overlay does not infer hidden truth
- **WHEN** source data is incomplete
- **THEN** the overlay reports only what is explicitly available
