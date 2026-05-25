## ADDED Requirements

### Requirement: Dodge displacement executes only for accepted dodge flow
The system SHALL apply player world-space dodge displacement only when Combat Core has accepted Dodge and entered its dodge state timeline.

#### Scenario: Accepted dodge applies displacement
- **WHEN** player triggers Dodge from Neutral and Combat Core transitions into `DodgeStartup` then `DodgeActive`
- **THEN** Player Locomotion applies measurable world-space displacement during the dodge cycle
- **AND** debug/evidence can show position before and after displacement

#### Scenario: Rejected dodge does not apply displacement
- **WHEN** player triggers Dodge while Combat Core is not in a state that accepts new dodge requests
- **THEN** no dodge displacement is applied by Player Locomotion
- **AND** locomotion position remains unchanged except normal movement already in progress

### Requirement: Player Locomotion remains movement truth owner for dodge
The system SHALL keep dodge displacement authority in Player Locomotion and SHALL NOT move gameplay truth into TickHandler, camera, UI, or presentation adapters.

#### Scenario: Tick layer only bridges intent/state
- **WHEN** dodge displacement is triggered during gameplay tick
- **THEN** TickHandler only forwards state/request into locomotion
- **AND** transform movement remains derived from locomotion snapshot/output

### Requirement: Dodge displacement uses explicit tuning profile
The system SHALL define dodge displacement tuning independently from normal move speed and SHALL expose profile fields needed for M0 readability tuning.

#### Scenario: Tuning profile controls dodge expression
- **WHEN** dodge profile values are adjusted within valid bounds
- **THEN** displacement magnitude/timing changes according to profile
- **AND** normal locomotion move speed behavior remains unaffected outside dodge

#### Scenario: Invalid tuning values are rejected
- **WHEN** dodge profile contains invalid values (for example non-positive duration or negative distance)
- **THEN** setup validation fails with clear diagnostics
- **AND** runtime does not silently execute undefined displacement behavior

### Requirement: Evidence must prove visible dodge movement
The system SHALL provide evidence outputs that prove dodge state progression and actual displacement.

#### Scenario: Evidence captures displacement with state chain
- **WHEN** a verification run is executed
- **THEN** evidence includes combat dodge state chain (`Neutral -> DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral`)
- **AND** evidence includes displacement proof (before/after transform or equivalent movement log)
- **AND** evidence indicates whether any gameplay console errors occurred
