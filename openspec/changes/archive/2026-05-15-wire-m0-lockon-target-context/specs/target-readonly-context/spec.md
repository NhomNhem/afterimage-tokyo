# Spec: Target Read-Only Context

## Overview

Capability for Target Context to expose read-only target state, direction, and snapshot to Camera, Locomotion, Combat Core, and Debug Overlay.

## ADDED Requirements

### Requirement: Target Context exposes read-only snapshot
The Target Context system SHALL expose a read-only `TargetContextSnapshot` containing target state, direction, and reasons to downstream consumers.

#### Scenario: Snapshot contains target state
- **GIVEN** an active target exists
- **WHEN** a consumer requests `GetSnapshot()`
- **THEN** the snapshot contains `Active = true`, `CurrentTarget`, and `TargetDirection`

#### Scenario: Snapshot is immutable
- **GIVEN** a consumer holds a `TargetContextSnapshot`
- **WHEN** the consumer attempts to modify snapshot properties
- **THEN** the snapshot cannot be modified (compile-time or runtime prevention)
- **AND** Target Context truth remains protected

#### Scenario: Camera reads direction
- **GIVEN** Camera system needs framing direction
- **WHEN** Camera requests target context
- **THEN** Camera receives read-only `TargetDirection` for framing
- **AND** Camera does not mutate target truth

#### Scenario: Locomotion reads direction
- **GIVEN** Locomotion may use target for orientation support
- **WHEN** Locomotion requests target context
- **THEN** Locomotion receives read-only direction
- **AND** this story does not modify Locomotion behavior (future consumption only)

#### Scenario: Debug Overlay reads reasons
- **GIVEN** Debug Overlay displays targeting state
- **WHEN** Debug requests snapshot
- **THEN** snapshot includes `LastAcquireReason`, `LastReleaseReason`, `LastInvalidationReason`
- **AND** reasons are human-readable for debugging

## REMOVED Requirements

None. This is a new capability introducing read-only context exposure.
