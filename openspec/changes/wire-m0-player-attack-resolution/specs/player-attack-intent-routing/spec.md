# Spec: Player Attack Intent Routing

## Overview

Capability for Input Mapping to emit raw `LightAttack` and `HeavyAttack` intents without combat decisions, target selection, or combat truth ownership.

## ADDED Requirements

### Requirement: Input Mapping emits raw LightAttack intent only
The Input Mapping system SHALL emit a raw `LightAttackIntent` when the New Input System `LightAttack` action is triggered, without deciding attack validity, target selection, or combat state.

#### Scenario: Raw LightAttack intent emission
- **WHEN** the New Input System `LightAttack` action is triggered by the player
- **THEN** `M0InputRouter` emits a `LightAttackIntent` containing only the raw request state
- **AND** the intent does not contain combat validity results, target selection, or combat state

#### Scenario: No combat decision in Input
- **GIVEN** the player triggers the `LightAttack` action
- **WHEN** `M0InputRouter` processes the input
- **THEN** the emitted intent does not reference any combat validity or result
- **AND** combat validity remains the responsibility of Combat Core

### Requirement: Input Mapping emits raw HeavyAttack intent only
The Input Mapping system SHALL emit a raw `HeavyAttackIntent` when the New Input System `HeavyAttack` action is triggered, without deciding attack validity, target selection, or combat state.

#### Scenario: Raw HeavyAttack intent emission
- **WHEN** the New Input System `HeavyAttack` action is triggered by the player
- **THEN** `M0InputRouter` emits a `HeavyAttackIntent` containing only the raw request state
- **AND** the intent does not contain combat validity results, target selection, or combat state

#### Scenario: Distinguish light vs heavy attack in intent
- **GIVEN** the player triggers either `LightAttack` or `HeavyAttack` action
- **WHEN** `M0InputRouter` processes the input
- **THEN** the emitted intent type (LightAttackIntent vs HeavyAttackIntent) distinguishes the attack request
- **AND** Combat Core receives the correct attack type for validation

### Requirement: No hardcoded device polling for attack inputs
The Input Mapping system SHALL NOT use `Keyboard.current`, `Mouse.current`, `Gamepad.current`, or direct device polling for attack input processing.

#### Scenario: No hardcoded device polling
- **WHEN** attack input is processed
- **THEN** the system SHALL NOT use `Keyboard.current`, `Mouse.current`, `Gamepad.current`, or direct device polling
- **AND** all gameplay attack input SHALL be read through `InputActionAsset` / `M0InputActions` action maps only

## REMOVED Requirements

None. This is a new capability introducing attack intent handling.
