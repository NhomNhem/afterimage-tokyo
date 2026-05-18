# Spec: Combat State Snapshot

## Overview

Capability for Combat Core to expose read-only combat state and result snapshot for debug and presentation systems without allowing mutation.

## ADDED Requirements

### Requirement: Combat Core exposes read-only combat state snapshot
The Combat Core SHALL expose a read-only CombatResultSnapshot containing current combat state, attack type, result, and reasons for debug and presentation systems.

#### Scenario: Snapshot contains current combat state
- **GIVEN** CombatCore is in any combat state
- **WHEN** snapshot is requested
- **THEN** the snapshot includes the current combat state (e.g., Neutral, AttackStartup, AttackActive, AttackRecovery)
- **AND** the snapshot is read-only (init-only properties)

#### Scenario: Snapshot contains attack type
- **GIVEN** CombatCore has processed an attack request
- **WHEN** snapshot is requested
- **THEN** the snapshot includes the attack type (light vs heavy)
- **AND** the snapshot is read-only

#### Scenario: Snapshot contains result
- **GIVEN** CombatCore has resolved an attack
- **WHEN** snapshot is requested
- **THEN** the snapshot includes the result (hit, whiff, rejected)
- **AND** the snapshot is read-only

#### Scenario: Snapshot contains reasons
- **GIVEN** CombatCore has resolved an attack or rejected a request
- **WHEN** snapshot is requested
- **THEN** the snapshot includes a reason string explaining the outcome
- **AND** the snapshot is read-only

### Requirement: Combat Core snapshot is read-only and cannot mutate combat truth
The Combat Core snapshot SHALL have init-only properties (no setters) and cannot be used to mutate combat truth by downstream systems.

#### Scenario: Snapshot cannot mutate combat state
- **GIVEN** a debug or presentation system receives a CombatResultSnapshot
- **WHEN** the system attempts to modify snapshot properties
- **THEN** the modification fails or is ignored
- **AND** Combat Core truth remains unchanged

#### Scenario: Snapshot exposes data only
- **GIVEN** a debug or presentation system reads CombatResultSnapshot
- **WHEN** the system displays combat state
- **THEN** the display reflects Combat Core truth
- **AND** the system does not own combat truth (ADR-0003 compliance)

## REMOVED Requirements

None. This is a new capability introducing combat state snapshot.
