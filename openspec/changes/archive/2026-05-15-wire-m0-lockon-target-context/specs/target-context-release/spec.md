# Spec: Target Context Release

## Overview

Capability for Target Context to release the active target when `LockOn` intent is received while a target is active, or when explicitly invalidated.

## ADDED Requirements

### Requirement: Target Context releases active target on toggle
The Target Context system SHALL release (clear) the active target when a `LockOn` intent is received while a target is currently active.

#### Scenario: Release when active target exists
- **GIVEN** `M0TargetContext` has an active target (`Active == true`)
- **WHEN** a `LockOn` intent is received
- **THEN** `CurrentTarget` is cleared
- **AND** `Active` becomes `false`
- **AND** a release reason is recorded

#### Scenario: Release exposes reason
- **WHEN** target release occurs
- **THEN** the release reason is recorded (e.g., "PlayerRequest", "Invalidation")
- **AND** the reason is available in the read-only snapshot for debug visibility

#### Scenario: Toggle behavior cycles through states
- **GIVEN** no active target
- **WHEN** first `LockOn` intent
- **THEN** target is acquired (Active = true)
- **WHEN** second `LockOn` intent
- **THEN** target is released (Active = false)
- **AND** the cycle can repeat

## REMOVED Requirements

None. This is a new capability introducing target release behavior.
