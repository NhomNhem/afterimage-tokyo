# lockon-input-routing Specification

## Purpose
TBD - created by archiving change wire-m0-lockon-target-context. Update Purpose after archive.
## Requirements
### Requirement: Input Mapping emits raw LockOn intent only
The Input Mapping system SHALL emit a raw `LockOn` intent when the New Input System `LockOn` action is triggered, without deciding target acquire/release or storing target truth.

#### Scenario: Raw intent emission
- **WHEN** the New Input System `LockOn` action is triggered by the player
- **THEN** `M0InputRouter` emits a `LockOnIntent` containing only the raw request state
- **AND** the intent does not contain target selection, validation results, or target state

#### Scenario: No target selection in Input
- **GIVEN** the player triggers the `LockOn` action
- **WHEN** `M0InputRouter` processes the input
- **THEN** the emitted intent does not reference any specific target or enemy
- **AND** target selection remains the responsibility of Target Context

#### Scenario: No hardcoded device polling
- **WHEN** input is processed
- **THEN** the system SHALL NOT use `Keyboard.current`, `Mouse.current`, `Gamepad.current`, or direct device polling
- **AND** all gameplay input SHALL be read through `InputActionAsset` / `M0InputActions` action maps only
