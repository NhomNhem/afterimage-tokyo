# m0-scene-composition-registrar Specification

## Purpose
TBD - created by archiving change extract-m0-scene-composition-registrar. Update Purpose after archive.
## Requirements
### Requirement: Scene composition registrar SHALL own scene component wiring only

The M0 scene composition registrar SHALL register explicit Unity scene component instances and perform build-time scene wiring for the gameplay scope. It MUST NOT own gameplay truth or gameplay decisions.

#### Scenario: Registrar wires scene components without owning gameplay
- **WHEN** the gameplay lifetime scope configures the M0 scene
- **THEN** scene component registration and post-build scene wiring are delegated to the registrar
- **AND** CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, MemoryState, MemoryInteractionService, Presentation, and DebugOverlay ownership remain unchanged
- **AND** the registrar does not validate combat actions, decide movement state, decide memory eligibility, accept reveals, update prompt truth, or append runtime memory log entries

### Requirement: GameplayLifetimeScope SHALL remain the gameplay composition root

`GameplayLifetimeScope` SHALL remain the VContainer gameplay composition root and SHALL keep high-level composition order visible.

#### Scenario: Gameplay root delegates scene wiring
- **WHEN** `GameplayLifetimeScope.Configure` executes
- **THEN** it performs gameplay-scope generated registration
- **AND** it composes authored combat and locomotion tuning configs into runtime settings
- **AND** it delegates scene component registration and post-build scene wiring to the registrar
- **AND** it does not become a second gameplay truth owner

### Requirement: Scene references SHALL remain explicit and assignable

Scene-provided components needed for M0 gameplay composition SHALL remain explicit serialized references on a Unity-owned composition object. They MUST remain visible and assignable in the Unity Inspector.

#### Scenario: Inspector exposes required scene references
- **WHEN** the `GameplayLifetimeScope` object is selected in the Unity Inspector
- **THEN** required scene references for core adapters, animation drivers, configs, and memory participants are visible
- **AND** the custom inspector binds the serialized fields correctly
- **AND** the user can assign missing references without disabling the custom inspector

### Requirement: Registrar SHALL avoid broad scene discovery and resource fallback

The registrar and gameplay composition code MUST NOT use broad Unity scene discovery, resource lookup, or Service Locator patterns to find scene components during normal composition.

#### Scenario: Composition uses explicit references only
- **WHEN** the registrar registers or wires scene participants
- **THEN** it uses explicit serialized references passed to it by the composition root or scene-reference container
- **AND** it does not call `FindObjectOfType`, `FindFirstObjectByType`, `FindAnyObjectByType`, broad `FindObjectsByType`, `Resources.Load`, or Service Locator lookup

### Requirement: Existing M0/S4 runtime behavior SHALL be preserved

Extracting scene composition into a registrar SHALL preserve existing M0 runtime behavior and the S4 memory loop behavior.

#### Scenario: M0 and memory loop parity is preserved
- **WHEN** the extracted registrar is used in PlayMode
- **THEN** input routing, combat transitions, locomotion, enemy intent loop, target registration, animation presentation, memory prompt, accepted Interact path, reveal feedback, and runtime memory log behavior remain equivalent to baseline
- **AND** duplicate or spam Interact behavior remains equivalent

### Requirement: Missing scene composition SHALL be diagnosable without direct Unity debug logging

Missing or invalid scene references SHALL be diagnosable through project logging, validation, focused tests, or manual checklist evidence. Owned runtime/editor code MUST NOT add direct Unity debug logging to report these issues.

#### Scenario: Missing reference is surfaced safely
- **WHEN** a required scene component reference is missing
- **THEN** the issue is visible through project logger output, validation/test evidence, or Inspector assignment state
- **AND** owned code does not call direct `UnityEngine.Debug.Log`, `Debug.LogWarning`, or `Debug.LogError`

### Requirement: Verification evidence SHALL cover composition guardrails

The change SHALL include evidence proving the registrar extraction is behavior-preserving and architecture-compliant.

#### Scenario: Evidence package is complete
- **WHEN** the change is ready for closure
- **THEN** compile evidence is recorded
- **AND** focused scene composition tests are recorded
- **AND** source guardrails for no broad discovery and no direct Unity debug logging are recorded
- **AND** inspector binding or manual assignment evidence is recorded
- **AND** M0/S4 smoke evidence is recorded
- **AND** console classification and PASS/PARTIAL/FAIL summary are recorded
