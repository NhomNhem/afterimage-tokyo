## ADDED Requirements

### Requirement: Authored Unity project structure SHALL exist under Assets/_Project
The project SHALL place all authored M0 game code, content, data, and tests under `Assets/_Project` and SHALL keep third-party packages and imported assets outside that authored root.

#### Scenario: Authored roots are created
- **WHEN** the Unity project foundation change is applied
- **THEN** the project SHALL contain authored folder roots under `Assets/_Project` for code, content, data, and tests

#### Scenario: Third-party boundary is preserved
- **WHEN** foundation scaffolding is added
- **THEN** authored Glass Refrain work SHALL NOT be placed under `Assets/ThirdParty`

### Requirement: Minimal M0 assembly boundaries SHALL be created
The project SHALL create the minimal M0 assembly-definition structure described by the architecture and SHALL enforce dependency direction that keeps gameplay truth out of presentation and bootstrap assemblies.

#### Scenario: Minimal asmdefs exist
- **WHEN** the foundation change is applied
- **THEN** the minimal M0 asmdef set SHALL exist for core, infrastructure, bootstrap, gameplay-domain, presentation, and test boundaries

#### Scenario: Forbidden dependencies are not introduced
- **WHEN** runtime assemblies are configured
- **THEN** `Combat`, `Locomotion`, `Targeting`, `Memory`, and other gameplay-domain assemblies SHALL NOT directly depend on `UI`, `VFX`, or `Camera` implementation assemblies for gameplay truth

### Requirement: M0 additive scene architecture SHALL be represented
The project SHALL represent the approved M0 additive scene architecture through named scene roles for bootstrap, systems, gameplay, camera, UI debug, and level blockout.

#### Scenario: Required scene roles are present
- **WHEN** the M0 scene foundation is scaffolded
- **THEN** the project SHALL contain scene entries or scene assets representing:
  - `Bootstrap`
  - `Systems`
  - `Gameplay_CombatPrototype`
  - `Camera_CombatPrototype`
  - `UI_DebugOverlay`
  - `Level_TokyoStreet_Blockout`

#### Scenario: Scene ownership boundaries are preserved
- **WHEN** additive scene composition is represented
- **THEN** level scenes SHALL NOT own gameplay rules, camera scenes SHALL NOT own target or movement truth, and UI scenes SHALL NOT own gameplay state

### Requirement: VContainer scope structure SHALL separate app lifetime from duel truth
The project SHALL represent a `ProjectRootLifetimeScope` for app-level services and SHALL keep duel-state truth in scene-scoped gameplay composition rather than root scope.

#### Scenario: Root scope stays thin
- **WHEN** root composition is scaffolded
- **THEN** `ProjectRootLifetimeScope` SHALL contain only app-level bootstrap, configuration, loading, and safe shared services

#### Scenario: Duel truth is not global
- **WHEN** gameplay composition is scaffolded
- **THEN** current combat state, locomotion state, target truth, encounter truth, and memory truth SHALL NOT be registered as project-root singletons

### Requirement: Unity New Input System SHALL be the only input foundation
The project SHALL use Unity New Input System for raw input intent and SHALL NOT introduce a legacy Unity Input Manager path.

#### Scenario: Input foundation is represented
- **WHEN** the input foundation is scaffolded
- **THEN** the project SHALL contain Unity New Input System action-map structure for M0 gameplay inputs

#### Scenario: Legacy input path is excluded
- **WHEN** input setup is configured
- **THEN** the project SHALL NOT add a legacy Unity Input Manager architecture path for M0 gameplay

### Requirement: Core cross-system contracts SHALL be defined at the architecture layer
The project SHALL define shared contract/DTO shapes for M0 cross-system communication before gameplay behavior implementation begins.

#### Scenario: Core contract layer exists
- **WHEN** the foundation change is applied
- **THEN** the project SHALL represent architecture-level contracts for:
  - input intent
  - combat action request/result
  - action lock/recovery context
  - locomotion state snapshot
  - target context snapshot
  - enemy intent snapshot
  - health/damage/hit reaction context
  - memory reveal request/result
  - encounter state snapshot

#### Scenario: Camera-relative movement basis is explicit
- **WHEN** locomotion and camera contracts are represented
- **THEN** camera-relative movement SHALL be exposed as a read-only basis contract and SHALL NOT let camera directly decide locomotion truth

### Requirement: Debug Overlay SHALL consume read-only snapshots only
The project SHALL represent the M0 debug system as a read-only overlay built from per-system debug snapshots and optional transition/rejection events.

#### Scenario: Snapshot ownership remains with authoritative systems
- **WHEN** debug snapshot contracts are defined
- **THEN** each authoritative gameplay system SHALL own its own debug truth for its domain

#### Scenario: Debug overlay remains read-only
- **WHEN** debug presentation is scaffolded
- **THEN** `Debug Overlay` SHALL group and display snapshots without mutating gameplay state

### Requirement: Presentation systems SHALL NOT own gameplay truth
The project foundation SHALL preserve architecture guardrails that keep gameplay truth out of `Animator`, camera presentation, VFX, audio, and UI systems.

#### Scenario: Animator does not own gameplay state
- **WHEN** animation integration is later attached to the foundation
- **THEN** gameplay truth SHALL remain in Pure C# state models and SHALL NOT live in Animator state transitions or clip timing

#### Scenario: Camera, VFX, and UI do not become authorities
- **WHEN** presentation adapters are scaffolded
- **THEN** camera, VFX, and UI layers SHALL remain downstream observers of confirmed gameplay context only

### Requirement: Foundation test scaffolding SHALL exist for architecture verification
The project SHALL include initial EditMode and PlayMode test structure that can verify assembly boundaries, scene composition, DI scope boundaries, and first M0 smoke readiness.

#### Scenario: EditMode and PlayMode test roots exist
- **WHEN** the foundation change is applied
- **THEN** the project SHALL contain test roots for EditMode and PlayMode architecture verification

#### Scenario: First architecture smoke path is represented
- **WHEN** test scaffolding is created
- **THEN** the project SHALL have a path to verify loading the minimal M0 additive scene set and composing root, gameplay, camera, and debug scopes without gameplay implementation completeness
