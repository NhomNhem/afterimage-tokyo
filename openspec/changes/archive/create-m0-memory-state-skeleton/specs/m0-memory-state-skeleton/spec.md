## ADDED Requirements

### Requirement: Memory State SHALL own reveal acceptance and rejection
The system MUST treat Memory State as the authoritative owner of reveal acceptance/rejection decisions for M0. Combat Core and Health systems MUST NOT accept reveal directly.

#### Scenario: Reveal ownership is enforced
- **WHEN** reveal request context is produced by combat or consequence systems
- **THEN** only Memory State MUST decide accepted or rejected reveal outcome

#### Scenario: Adjacent systems remain non-authoritative
- **WHEN** Combat Core or Health emits context that could contribute to reveal flow
- **THEN** those systems MUST remain context providers only and MUST NOT finalize reveal acceptance

### Requirement: Memory skeleton SHALL define pure C# reveal phase model
The system MUST provide a pure C# memory state model supporting dormant, requested, accepted, rejected, responding, and cooldown phases.

#### Scenario: Phase progression is inspectable
- **WHEN** reveal requests are processed
- **THEN** memory phase transitions MUST be observable through read-only snapshot data

#### Scenario: No scene runtime dependency
- **WHEN** memory phase transitions execute
- **THEN** they MUST NOT require scene/prefab wiring, animation controllers, or cutscene runtime dependencies

### Requirement: Reveal request/result shape SHALL be represented
The system MUST represent reveal request processing as explicit request/result contracts including acceptance/rejection and readable reason/context placeholders.

#### Scenario: Accepted reveal returns explicit result
- **WHEN** a valid reveal request is processed in an acceptable state
- **THEN** Memory State MUST return an accepted reveal result shape

#### Scenario: Rejected reveal returns explicit reason
- **WHEN** a reveal request is invalid or disallowed for current phase/context
- **THEN** Memory State MUST return a rejected reveal result shape with readable reason/context

### Requirement: Reveal response and cooldown state SHALL be represented
The system MUST represent responding and cooldown as explicit state shapes under Memory State ownership.

#### Scenario: Responding phase follows acceptance
- **WHEN** reveal request is accepted
- **THEN** Memory State MUST expose responding phase before transitioning to cooldown

#### Scenario: Cooldown phase is explicit
- **WHEN** responding phase completes
- **THEN** Memory State MUST expose cooldown phase state in snapshot data

### Requirement: Memory snapshot SHALL be read-only
The system MUST expose a read-only memory snapshot for Debug Overlay and downstream observers.

#### Scenario: Snapshot reflects current memory truth
- **WHEN** memory phase or last reveal result changes
- **THEN** snapshot MUST reflect latest memory state and reveal result context

#### Scenario: Debug remains observer-only
- **WHEN** Debug Overlay consumes memory snapshot data
- **THEN** it MUST remain read-only and MUST NOT mutate Memory State authority

### Requirement: Invalid/presentation-only trigger categories SHALL NOT be accepted
Generic hits, failed dodge, failed parry, invalid counter, and presentation-only events MUST NOT produce accepted reveal outcomes.

#### Scenario: Generic hit does not accept reveal
- **WHEN** reveal request context indicates generic hit
- **THEN** Memory State MUST reject the request

#### Scenario: Failed defense/counter categories do not accept reveal
- **WHEN** reveal request context indicates failed dodge, failed parry, or invalid counter
- **THEN** Memory State MUST reject the request

#### Scenario: Presentation-only events do not accept reveal
- **WHEN** reveal request context is presentation-only
- **THEN** Memory State MUST reject the request

### Requirement: Skeleton SHALL exclude deferred subsystems
The system MUST remain a skeleton-only memory state change and exclude non-goal subsystem implementation.

#### Scenario: Non-goal systems are not implemented
- **WHEN** this change is implemented
- **THEN** there MUST be no Memory VFX playback, narrative graph, clue database, branching progression, district reinterpretation, save/persistence, cutscene system, combat validation, damage application, or scene/prefab wiring logic

#### Scenario: Framework constraints remain enforced
- **WHEN** files are added or modified for this capability
- **THEN** there MUST be no legacy Input Manager references, no Nhem generated DI usage, and VContainer scopes MUST remain manual

#### Scenario: Contracts remain contracts-only
- **WHEN** `M0Contracts.cs` is updated for memory request/result/snapshot types
- **THEN** it MUST remain data contracts only and MUST NOT contain behavior logic
