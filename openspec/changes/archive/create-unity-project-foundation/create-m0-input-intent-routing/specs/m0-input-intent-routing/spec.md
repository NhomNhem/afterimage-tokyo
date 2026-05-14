## ADDED Requirements

### Requirement: Unity New Input System SHALL be the only input path
The project MUST route M0 input through Unity New Input System actions only and MUST NOT introduce a legacy Unity Input Manager path.

#### Scenario: New input path is represented
- **WHEN** the input foundation is defined for M0
- **THEN** the project MUST expose gameplay action mapping through Unity New Input System actions

#### Scenario: Legacy input path is excluded
- **WHEN** input routing artifacts are created or updated
- **THEN** the project MUST NOT add a Unity Input Manager-based path for M0

### Requirement: Raw M0 input intent SHALL be represented as read-only snapshot data
The project MUST represent raw player input as a read-only input intent snapshot that captures the current M0 action values and input enable state without performing gameplay validation.

#### Scenario: Snapshot reflects current raw intent
- **WHEN** the player provides movement or action input
- **THEN** the latest input snapshot MUST capture the raw intent values for the configured M0 actions

#### Scenario: Snapshot tracks enable state
- **WHEN** input is enabled or disabled at the input-contract level
- **THEN** the snapshot MUST represent that enabled/disabled state

### Requirement: Input routing outcomes SHALL distinguish disabled, ignored, routed, and rejected states
The project MUST record input routing outcomes in a way that distinguishes input disabled, input ignored, input routed downstream, and input rejected downstream, with an optional reason when a downstream system provides one.

#### Scenario: Disabled input is distinguishable
- **WHEN** input is disabled before a raw action is routed
- **THEN** the routing outcome MUST indicate that input was disabled rather than gameplay-rejected

#### Scenario: Ignored and rejected outcomes remain distinct
- **WHEN** a raw intent is not consumed or is rejected by a downstream system
- **THEN** the outcome MUST distinguish ignored from routed or rejected states

#### Scenario: Downstream reasons can be preserved
- **WHEN** a downstream system provides a rejection reason
- **THEN** the input routing outcome MUST be able to carry that reason without owning the validation rule itself

### Requirement: Input Mapping SHALL emit intent only and SHALL NOT own gameplay validation
The project MUST keep Input Mapping limited to sampling and routing raw input intent and MUST NOT make validity decisions for combat, movement, target, counter-window, or reveal truth.

#### Scenario: Combat validity is not decided in input
- **WHEN** a player presses attack, dodge, parry, or counter
- **THEN** Input Mapping MUST emit the intent without deciding whether the action is valid

#### Scenario: Movement truth is not decided in input
- **WHEN** a player provides move intent
- **THEN** Input Mapping MUST NOT decide final movement truth or camera-relative movement resolution

#### Scenario: Target and reveal truth are not decided in input
- **WHEN** lock-on or debug-related input is sampled
- **THEN** Input Mapping MUST NOT decide target validity, CounterWindow truth, or reveal validity

### Requirement: Input snapshot and routing data SHALL be debug-consumable and read-only
The project MUST expose the latest input snapshot and routing history in a read-only form suitable for future Debug Overlay consumption.

#### Scenario: Debug can read snapshot state
- **WHEN** debug presentation consumes input state later
- **THEN** it MUST be able to read the latest input snapshot without mutating gameplay truth

#### Scenario: Read-only data remains immutable by consumers
- **WHEN** a consumer reads the input snapshot or routing outcome
- **THEN** the consumer MUST NOT be able to change the authoritative input state through that read path

### Requirement: Input routing SHALL remain decoupled from concrete combat and locomotion implementations
The project MUST keep Input Mapping free of direct coupling to concrete Combat, Locomotion, Targeting, or Camera implementation classes, and MUST NOT use a service locator to reach them.

#### Scenario: Routing uses contracts, not concrete gameplay classes
- **WHEN** input routing is defined
- **THEN** it MUST depend on shared contracts or abstractions rather than concrete gameplay implementations

#### Scenario: No service locator is introduced
- **WHEN** the input router is connected to the rest of M0
- **THEN** it MUST NOT rely on a service locator to find downstream consumers
