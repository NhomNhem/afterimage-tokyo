# target-manual-di Specification

## Purpose
TBD - created by archiving change wire-m0-lockon-target-context. Update Purpose after archive.
## Requirements
### Requirement: Manual VContainer registration for Target Context
The Target Context system SHALL be registered in `GameplayScope` through manual VContainer composition, without using generated DI or automatic scanning.

#### Scenario: ITargetContext registered
- **WHEN** `GameplayScope` composition root configures DI
- **THEN** `ITargetContext` is registered with `M0TargetContext` implementation
- **AND** lifetime is Scoped (per gameplay session)
- **AND** registration is explicit in code

#### Scenario: No automatic scanning
- **GIVEN** VContainer configuration exists
- **THEN** the system SHALL NOT use automatic type scanning
- **AND** the system SHALL NOT use `VContainer.SourceGenerator` for targeting services
- **AND** all registrations are hand-written in composition roots

#### Scenario: GameplayScope only
- **WHEN** Target Context services are registered
- **THEN** they are registered in `GameplayScope` (not ProjectRoot)
- **AND** services are disposed when Gameplay scene unloads

#### Scenario: M0InputRouter receives ITargetContext
- **GIVEN** `M0InputRouter` is registered
- **WHEN** it is resolved
- **THEN** it receives injected `ITargetContext` dependency
- **AND** it routes `LockOnIntent` to the context
