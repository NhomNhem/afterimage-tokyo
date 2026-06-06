## ADDED Requirements

### Requirement: M0 locomotion tuning SHALL be authored through ScriptableObject config

M0 locomotion tuning values used to construct `M0PlayerLocomotion` SHALL be authored in a Unity ScriptableObject configuration asset rather than hard-coded inline inside `GameplayLifetimeScope`.

#### Scenario: Gameplay scope composes locomotion from authored config
- **WHEN** the gameplay lifetime scope constructs `M0PlayerLocomotion`
- **THEN** it converts the assigned M0 locomotion tuning ScriptableObject into `M0LocomotionSettings`
- **AND** it passes those immutable settings to `M0PlayerLocomotion`
- **AND** it does not inline move speed, input deadzone, facing lerp speed, dodge distance, dodge speed, or dodge duration literals inside the `M0PlayerLocomotion` registration

### Requirement: M0 locomotion tuning config SHALL preserve current tuning values

The default M0 locomotion tuning ScriptableObject SHALL preserve the currently verified M0 movement and dodge tuning values unless a separate approved change explicitly modifies locomotion tuning.

#### Scenario: Default config matches existing M0 locomotion tuning
- **WHEN** the default M0 locomotion tuning config is inspected or converted to runtime settings
- **THEN** move speed is `5.0`
- **AND** input deadzone is `0.1`
- **AND** facing lerp speed is `8.0`
- **AND** dodge distance is `1.5`
- **AND** dodge speed is `10.0`
- **AND** dodge duration is `0.2` seconds

### Requirement: PlayerLocomotion SHALL remain independent from Unity asset types

`M0PlayerLocomotion` SHALL continue to depend on pure runtime settings and domain snapshots only. It MUST NOT depend on `ScriptableObject`, Unity asset APIs, scene references, or authored config asset types.

#### Scenario: PlayerLocomotion receives pure runtime settings
- **WHEN** `M0PlayerLocomotion` is constructed
- **THEN** it receives `M0LocomotionSettings`
- **AND** it does not receive or store the locomotion tuning ScriptableObject
- **AND** movement truth remains owned by `M0PlayerLocomotion`

### Requirement: Authored config SHALL not own movement truth

The M0 locomotion tuning ScriptableObject SHALL only provide authored values. It MUST NOT consume input, update position, decide movement restrictions, express dodge movement, refresh locomotion snapshots, or decide recovery movement.

#### Scenario: Movement truth ownership remains unchanged
- **WHEN** locomotion input is consumed or locomotion state changes
- **THEN** `M0PlayerLocomotion` remains the owner of movement truth, dodge movement expression, facing support, movement restrictions, and recovery movement
- **AND** the ScriptableObject config only supplies authored tuning values

### Requirement: Missing locomotion tuning composition SHALL be diagnosable

Missing or invalid M0 locomotion tuning config assignment SHALL be visible through project validation, focused tests, or project logger output. Owned runtime code MUST NOT use direct Unity debug logging or broad resource lookup to hide missing configuration.

#### Scenario: Missing config is surfaced as setup issue
- **WHEN** the gameplay scene lacks an assigned M0 locomotion tuning config
- **THEN** the setup problem is diagnosable before closure through tests, validation, or project logger output
- **AND** owned runtime code does not call `Resources.Load`, `FindObject*`, Service Locator, or direct `UnityEngine.Debug.Log*` as a fallback

### Requirement: M0 locomotion behavior SHALL remain equivalent

Externalizing M0 locomotion tuning to a ScriptableObject SHALL preserve verified M0 movement and dodge behavior.

#### Scenario: Locomotion tuning parity is preserved
- **WHEN** focused M0 locomotion regression tests run after the config extraction
- **THEN** movement speed behavior remains equivalent
- **AND** input deadzone behavior remains equivalent
- **AND** facing interpolation behavior remains equivalent
- **AND** dodge distance, speed, and duration behavior remain equivalent
- **AND** the M0 `read -> evade/parry -> counter -> reveal` loop remains equivalent

### Requirement: Verification evidence SHALL cover config parity and M0 regression

The change SHALL include evidence proving the authored config is behavior-preserving and architecture-compliant.

#### Scenario: Evidence package is complete
- **WHEN** the change is ready for closure
- **THEN** compile evidence is recorded
- **AND** config parity tests are recorded
- **AND** focused M0 locomotion regression tests are recorded
- **AND** source guardrail checks are recorded
- **AND** PlayMode smoke or manual M0 checklist evidence is recorded
- **AND** OpenSpec strict validation and console classification are recorded
