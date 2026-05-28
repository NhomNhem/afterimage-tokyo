# m0-runtime-foundation Specification

## Purpose
TBD - created by archiving change wire-m0-foundation-and-vcontainer. Update Purpose after archive.
## Requirements
### Requirement: Additive Scene Composition Sequence
The system SHALL load the M0 prototype scenes in a specific, additive sequence to ensure correct dependency resolution and scene responsibility boundaries.

#### Scenario: Successful scene load sequence
- **WHEN** the Bootstrap scene completes its initial configuration
- **THEN** it SHALL load the following scenes additively and in order: `Systems`, `Level_TokyoStreet_Blockout`, `Gameplay_CombatPrototype`, `Camera_CombatPrototype`, and `UI_DebugOverlay`.

### Requirement: ProjectRoot Lifetime Scope Resolution
The system SHALL maintain a `ProjectRootLifetimeScope` that resolves application-level services which must persist across gameplay sessions.

#### Scenario: Resolve global services
- **WHEN** the application is initialized in the `Bootstrap` scene
- **THEN** the `ProjectRootLifetimeScope` SHALL resolve application-level infrastructure services if present.

### Requirement: Gameplay Lifetime Scope Resolution
The system SHALL maintain a `GameplayScope` that resolves M0 core gameplay skeleton services, isolated from application-level services.

#### Scenario: Resolve M0 core skeletons
- **WHEN** the `Gameplay_CombatPrototype` scene is loaded
- **THEN** the `GameplayScope` SHALL resolve the existing M0 technical skeleton services (Combat, Locomotion, Targeting, Health, Enemy, and Memory).

### Requirement: Manual VContainer Registration
The system SHALL use manual registration for all VContainer scopes in M0 to maintain strict traceability and avoid automatic scanning.

#### Scenario: Verify manual registration
- **WHEN** inspecting the `ProjectRootLifetimeScope` or `GameplayScope` code
- **THEN** all service-to-implementation mappings SHALL be explicitly defined in the `Configure` method without using reflection-based discovery or source generators.

### Requirement: Bootstrap Single Entry Point
The system SHALL ensure that the `Bootstrap` scene is the valid entry point for the M0 prototype to guarantee correct scope initialization.

#### Scenario: Verify bootstrap initialization
- **WHEN** entering Play Mode
- **THEN** the system SHALL verify that the Bootstrap scene is loaded first to ensure all required scopes are initialized correctly.
