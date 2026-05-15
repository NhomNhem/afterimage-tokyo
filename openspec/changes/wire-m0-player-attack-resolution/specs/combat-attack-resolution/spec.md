# Spec: Combat Attack Resolution

## Overview

Capability for Combat Core to resolve placeholder hit/whiff results using read-only Target Context spacing/timing truth without damage/health mutation.

## ADDED Requirements

### Requirement: Combat Core resolves placeholder hit result when valid target exists
The Combat Core SHALL resolve a placeholder hit result when a valid active target exists and is in range, without applying damage or health mutation.

#### Scenario: Hit resolution with valid target
- **GIVEN** CombatCore state is AttackActive and a valid active target exists in Target Context
- **WHEN** hit resolution is evaluated
- **THEN** CombatCore resolves a hit result
- **AND** the result indicates successful hit
- **AND** no damage or health mutation occurs

#### Scenario: Hit resolution uses read-only Target Context data
- **GIVEN** CombatCore is resolving a hit
- **WHEN** spacing/timing truth is needed
- **THEN** CombatCore reads from Target Context snapshot (read-only)
- **AND** CombatCore does not mutate Target Context truth

### Requirement: Combat Core resolves whiff result when no valid target exists
The Combat Core SHALL resolve a whiff/no-target result when no valid active target exists or target is out of range.

#### Scenario: Whiff resolution with no target
- **GIVEN** CombatCore state is AttackActive and no valid active target exists
- **WHEN** hit resolution is evaluated
- **THEN** CombatCore resolves a whiff result
- **AND** the result indicates no target hit

#### Scenario: Whiff resolution with out-of-range target
- **GIVEN** CombatCore state is AttackActive and target exists but is out of range
- **WHEN** hit resolution is evaluated
- **THEN** CombatCore resolves a whiff result
- **AND** the result indicates target missed due to spacing

### Requirement: Combat Core does not mutate damage or health in this story
The Combat Core SHALL NOT apply damage, health mutation, or hit reaction effects during attack resolution in this story.

#### Scenario: No damage mutation on hit
- **GIVEN** CombatCore resolves a hit result
- **WHEN** the result is generated
- **THEN** no damage is applied to any entity
- **AND** no health mutation occurs

#### Scenario: No hit reaction mutation
- **GIVEN** CombatCore resolves a hit or whiff result
- **WHEN** the result is generated
- **THEN** no hit reaction state is mutated
- **AND** no animation or VFX is triggered from Combat Core

### Requirement: Combat Core emits movement restriction/recovery context on successful attack
The Combat Core SHALL emit MovementRestrictionContext and RecoveryContext shapes on successful attack requests if supported by skeleton.

#### Scenario: Emit movement restriction on attack
- **GIVEN** CombatCore accepts an attack request
- **WHEN** the attack transitions to AttackStartup or AttackActive
- **THEN** CombatCore emits MovementRestrictionContext if supported
- **AND** Locomotion receives the restriction request

#### Scenario: Emit recovery context after attack
- **GIVEN** CombatCore completes an attack
- **WHEN** the attack transitions to AttackRecovery
- **THEN** CombatCore emits RecoveryContext if supported
- **AND** Locomotion receives the recovery request

## REMOVED Requirements

None. This is a new capability introducing attack resolution.
