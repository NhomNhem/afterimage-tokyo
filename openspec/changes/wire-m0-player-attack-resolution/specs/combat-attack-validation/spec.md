# Spec: Combat Attack Validation

## Overview

Capability for Combat Core to validate attack requests against current combat state, rejecting attacks that cannot start (e.g., during recovery).

## ADDED Requirements

### Requirement: Combat Core validates attack requests against current state
The Combat Core SHALL validate whether an attack request can start based on the current combat state (e.g., Neutral, AttackRecovery, HitReact).

#### Scenario: Reject attack during recovery
- **GIVEN** CombatCore state is AttackRecovery
- **WHEN** LightAttack or HeavyAttack intent is received
- **THEN** CombatCore rejects the attack request
- **AND** state remains AttackRecovery
- **AND** a rejection reason is exposed for debug

#### Scenario: Accept attack from Neutral state
- **GIVEN** CombatCore state is Neutral
- **WHEN** LightAttack or HeavyAttack intent is received
- **THEN** CombatCore accepts the attack request
- **AND** state transitions to AttackStartup

#### Scenario: Reject attack during HitReact
- **GIVEN** CombatCore state is HitReact
- **WHEN** LightAttack or HeavyAttack intent is received
- **THEN** CombatCore rejects the attack request
- **AND** state remains HitReact

#### Scenario: Reject attack during other committed states
- **GIVEN** CombatCore state is AttackStartup, AttackActive, DodgeStartup, DodgeActive, ParryStartup, or ParryActive
- **WHEN** LightAttack or HeavyAttack intent is received
- **THEN** CombatCore rejects the attack request
- **AND** state remains unchanged

### Requirement: Combat Core distinguishes light attack vs heavy attack requests
The Combat Core SHALL distinguish between LightAttackIntent and HeavyAttackIntent and apply appropriate validation rules.

#### Scenario: Light attack validation
- **GIVEN** CombatCore state is Neutral
- **WHEN** LightAttackIntent is received
- **THEN** CombatCore validates as light attack request
- **AND** transitions to AttackStartup with light attack timing parameters

#### Scenario: Heavy attack validation
- **GIVEN** CombatCore state is Neutral
- **WHEN** HeavyAttackIntent is received
- **THEN** CombatCore validates as heavy attack request
- **AND** transitions to AttackStartup with heavy attack timing parameters

#### Scenario: Distinguish attack type in result
- **GIVEN** CombatCore accepts an attack request
- **WHEN** the attack result is generated
- **THEN** the result includes the attack type (light vs heavy)
- **AND** timing windows reflect the attack type

## REMOVED Requirements

None. This is a new capability introducing attack validation.
