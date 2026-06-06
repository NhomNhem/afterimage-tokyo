## ADDED Requirements

### Requirement: M0 combat timing SHALL be authored through ScriptableObject config

M0 combat timing values used to construct `M0CombatCore` SHALL be authored in a Unity ScriptableObject configuration asset rather than hard-coded inline inside `GameplayLifetimeScope`.

#### Scenario: Gameplay scope composes combat core from authored config
- **WHEN** the gameplay lifetime scope constructs `M0CombatCore`
- **THEN** it converts the assigned M0 combat timing ScriptableObject into `M0CombatTimingSettings`
- **AND** it passes those immutable settings to `M0CombatCore`
- **AND** it does not inline attack, dodge, parry, counter-window, or recovery timing literals inside the `M0CombatCore` registration

### Requirement: M0 combat timing config SHALL preserve current tuning values

The default M0 combat timing ScriptableObject SHALL preserve the currently verified M0 combat timing values unless a separate approved change explicitly modifies combat timing.

#### Scenario: Default config matches existing M0 combat timing
- **WHEN** the default M0 combat timing config is inspected or converted to runtime settings
- **THEN** attack startup is `0.14` seconds
- **AND** attack active is `0.20` seconds
- **AND** attack recovery is `0.26` seconds
- **AND** dodge startup is `0.09` seconds
- **AND** dodge active is `0.20` seconds
- **AND** dodge recovery is `0.24` seconds
- **AND** parry startup is `0.10` seconds
- **AND** parry active is `0.18` seconds
- **AND** parry recovery is `0.24` seconds
- **AND** counter-window duration is `3.0` seconds
- **AND** recovery duration is `0.24` seconds

### Requirement: CombatCore SHALL remain independent from Unity asset types

`M0CombatCore` SHALL continue to depend on pure runtime settings and project logging only. It MUST NOT depend on `ScriptableObject`, Unity asset APIs, scene references, or authored config asset types.

#### Scenario: CombatCore receives pure runtime settings
- **WHEN** `M0CombatCore` is constructed
- **THEN** it receives `M0CombatTimingSettings`
- **AND** it does not receive or store `M0CombatTimingConfig`
- **AND** combat timing progression remains owned by `M0CombatCore`

### Requirement: Authored config SHALL not own gameplay truth

The M0 combat timing ScriptableObject SHALL only provide authored values. It MUST NOT validate combat actions, advance combat state, open or close counter windows, resolve hits, emit reveal requests, or decide combat outcomes.

#### Scenario: Combat truth ownership remains unchanged
- **WHEN** combat actions are requested or combat state advances
- **THEN** `M0CombatCore` remains the owner of combat validity, timing progression, counter windows, hit resolution, and reveal request context
- **AND** the ScriptableObject config only supplies authored timing values

### Requirement: Missing combat tuning composition SHALL be diagnosable

Missing or invalid M0 combat timing config assignment SHALL be visible through project validation, focused tests, or project logger output. Owned runtime code MUST NOT use direct Unity debug logging or broad resource lookup to hide missing configuration.

#### Scenario: Missing config is surfaced as setup issue
- **WHEN** the gameplay scene lacks an assigned M0 combat timing config
- **THEN** the setup problem is diagnosable before closure through tests, validation, or project logger output
- **AND** owned runtime code does not call `Resources.Load`, `FindObject*`, Service Locator, or direct `UnityEngine.Debug.Log*` as a fallback

### Requirement: M0 combat behavior SHALL remain equivalent

Externalizing M0 combat timing to a ScriptableObject SHALL preserve verified M0 combat behavior.

#### Scenario: Combat timing parity is preserved
- **WHEN** focused M0 combat regression tests run after the config extraction
- **THEN** attack startup, active, and recovery transitions remain equivalent
- **AND** dodge and parry timing behavior remains equivalent
- **AND** counter-window behavior remains equivalent
- **AND** the M0 `read -> evade/parry -> counter -> reveal` loop remains equivalent

### Requirement: Verification evidence SHALL cover config parity and M0 regression

The change SHALL include evidence proving the authored config is behavior-preserving and architecture-compliant.

#### Scenario: Evidence package is complete
- **WHEN** the change is ready for closure
- **THEN** compile evidence is recorded
- **AND** config parity tests are recorded
- **AND** focused M0 combat regression tests are recorded
- **AND** source guardrail checks are recorded
- **AND** PlayMode smoke or manual M0 checklist evidence is recorded
- **AND** OpenSpec strict validation and console classification are recorded
