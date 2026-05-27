# target-context-validation Specification

## Purpose
TBD - created by archiving change wire-m0-lockon-target-context. Update Purpose after archive.
## Requirements
### Requirement: Target Context invalidates on enemy state change
The Target Context system SHALL invalidate and clear the active target when the enemy becomes unregistered, disabled, defeated, or no longer targetable for the current duel.

#### Scenario: Invalidation on unregistered
- **GIVEN** the M0 enemy is the active target
- **WHEN** the enemy is unregistered from the encounter
- **THEN** `M0TargetContext` invalidates the target
- **AND** `Active` becomes `false`
- **AND** the invalidation reason "Unregistered" is recorded

#### Scenario: Invalidation on disabled
- **GIVEN** the M0 enemy is the active target
- **WHEN** the enemy is disabled (e.g., paused, hidden)
- **THEN** `M0TargetContext` invalidates the target
- **AND** the invalidation reason "Disabled" is recorded

#### Scenario: Invalidation on defeated
- **GIVEN** the M0 enemy is the active target
- **WHEN** the enemy is defeated
- **THEN** `M0TargetContext` invalidates the target
- **AND** the invalidation reason "Defeated" is recorded

#### Scenario: Validity rules exclude scoring
- **GIVEN** target validation is checked
- **THEN** the system SHALL NOT apply range scoring, visibility scoring, or target priority scoring
- **AND** validity is determined solely by existence, registration, and targetable state
