# Spec: Combat Manual DI

## Overview

Capability for manual VContainer registration of Combat Core and related combat services in the GameplayLifetimeScope composition root.

## ADDED Requirements

### Requirement: Combat Core is registered with manual VContainer registration
The Combat Core SHALL be registered in the GameplayLifetimeScope using manual builder.Register calls, not automatic scanning or code generation.

#### Scenario: Manual registration of Combat Core
- **GIVEN** GameplayLifetimeScope is the manual composition root
- **WHEN** Combat Core is registered
- **THEN** the registration uses builder.Register<M0CombatCore>(Lifetime.Scoped)
- **AND** no automatic scanning or VContainer.SourceGenerator is used

#### Scenario: Combat Core resolves from GameplayScope
- **GIVEN** Combat Core is registered in GameplayLifetimeScope
- **WHEN** a dependent service requests IM0CombatCore
- **THEN** the dependency resolves to the manually registered instance
- **AND** the instance is scoped to the GameplayScope

### Requirement: Combat intent contracts are registered manually
The Combat Core intent contracts (LightAttackIntent, HeavyAttackIntent, CombatResultSnapshot) SHALL be registered in M0Contracts.cs as contracts-only (no behavior logic).

#### Scenario: Contracts-only in M0Contracts
- **GIVEN** M0Contracts.cs is the shared contract hub
- **WHEN** combat intent contracts are added
- **THEN** the contracts contain only data structures (no behavior logic)
- **AND** the contracts comply with ADR-0005

#### Scenario: Combat intent contracts resolve from GameplayScope
- **GIVEN** combat intent contracts are registered
- **WHEN** Combat Core or Input Mapping requests the contracts
- **THEN** the contracts resolve from the GameplayScope
- **AND** no ProjectRoot registrations exist for combat contracts

### Requirement: No automatic scanning or generated DI for combat services
The Combat Core and related combat services SHALL NOT use automatic assembly scanning, VContainer.SourceGenerator, or code-generated DI registration.

#### Scenario: No automatic scanning
- **GIVEN** Combat Core and related services exist
- **WHEN** DI resolution is performed
- **THEN** the resolution uses only manual builder.Register calls
- **AND** no automatic assembly scanning occurs

#### Scenario: No VContainer.SourceGenerator
- **GIVEN** Combat Core and related services exist
- **WHEN** DI registration is performed
- **THEN** no VContainer.SourceGenerator attributes or generated registration code is used
- **AND** registration is explicitly manual per ADR-0004

## REMOVED Requirements

None. This is a new capability introducing manual DI registration for combat services.
