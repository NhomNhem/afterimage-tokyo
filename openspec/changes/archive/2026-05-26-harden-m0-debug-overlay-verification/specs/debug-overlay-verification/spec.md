## ADDED Requirements

### Requirement: Debug Overlay SHALL remain read-only
The system SHALL ensure Debug Overlay only displays snapshot/read-model values and MUST NOT mutate gameplay truth owned by CombatCore, EnemyIntent, TargetContext, InputRouter, or Locomotion systems.

#### Scenario: Overlay update receives snapshot values
- **WHEN** GameplayTickHandler forwards snapshot updates to Debug Overlay adapter
- **THEN** Debug Overlay updates display fields without calling gameplay mutation APIs

### Requirement: Debug Overlay SHALL prove key duel-loop fields in PlayMode
The system SHALL expose the following fields in PlayMode Debug Overlay using existing snapshot values:
- CombatState from CombatCore snapshot
- EnemyIntent from EnemyIntent snapshot
- LastInput from input snapshot/router
- CounterWindow from CombatCore snapshot (if present)
- LockOnTarget from TargetContext snapshot

#### Scenario: Combat and enemy state are visible
- **WHEN** player performs an action sequence that advances combat and enemy states
- **THEN** CombatState and EnemyIntent fields show current snapshot-backed values

#### Scenario: Input and lock-on state are visible
- **WHEN** player performs LockOn and combat inputs
- **THEN** LastInput and LockOnTarget fields show current snapshot-backed values

#### Scenario: Counter window state is visible
- **WHEN** combat enters/exits counter-eligible windows
- **THEN** CounterWindow field reflects current CombatCore snapshot value

### Requirement: Verification evidence SHALL include concrete overlay proof
The system SHALL provide a focused evidence artifact for Story 1-9 closure with concrete proof of overlay visibility and required field transitions.

#### Scenario: Evidence artifact contains required proof
- **WHEN** verification is executed for this change
- **THEN** evidence includes screenshot/log/manual table proving required fields and their observed transitions
