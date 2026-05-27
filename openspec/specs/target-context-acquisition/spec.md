# target-context-acquisition Specification

## Purpose
TBD - created by archiving change wire-m0-lockon-target-context. Update Purpose after archive.
## Requirements
### Requirement: Target Context acquires single M0 enemy on toggle
The Target Context system SHALL acquire the single registered M0 enemy as the active target when a `LockOn` intent is received while no target is currently active.

#### Scenario: Acquire when no active target
- **GIVEN** one player and one registered targetable M0 enemy exist
- **AND** no target is currently active (`Active == false`)
- **WHEN** `M0TargetContext` receives a `LockOn` intent
- **THEN** `TargetContext.Active` becomes `true`
- **AND** `CurrentTarget` references the registered M0 enemy

#### Scenario: Acquire only single target
- **GIVEN** multiple entities exist in the scene
- **AND** only one is registered as the targetable M0 enemy
- **WHEN** acquire is triggered
- **THEN** only the registered M0 enemy becomes the current target
- **AND** no multi-target selection or cycling occurs

#### Scenario: Acquire exposes reason
- **WHEN** target acquisition succeeds
- **THEN** the acquire reason is recorded (e.g., "PlayerRequest", "EncounterSeed")
- **AND** the reason is available in the read-only snapshot for debug visibility
