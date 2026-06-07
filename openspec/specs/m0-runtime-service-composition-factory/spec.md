# m0-runtime-service-composition-factory Specification

## Purpose
TBD - created by archiving change extract-m0-runtime-service-composition-factory. Update Purpose after archive.
## Requirements
### Requirement: Runtime Service Composition Collaborator
The system SHALL provide a Bootstrap-owned collaborator for manually constructed M0 runtime service registrations that are backed by authored configs or factory-time dependencies.

#### Scenario: Collaborator registers config-backed runtime services
- **WHEN** gameplay scope composition runs
- **THEN** `M0CombatCore`, `M0PlayerLocomotion`, `M0MemoryState`, and `M0MemoryVFXResponse` manual factory registrations are owned by the runtime service composition collaborator rather than inline `GameplayLifetimeScope` code

#### Scenario: GameplayLifetimeScope remains high-level composition root
- **WHEN** `GameplayLifetimeScope.Configure` is inspected
- **THEN** it shows high-level composition order and delegates runtime service registration detail to the collaborator

### Requirement: Registration Parity Is Preserved
The runtime service composition collaborator SHALL preserve existing service lifetimes, exposed service types, and construction inputs.

#### Scenario: CombatCore registration parity
- **WHEN** `M0CombatCore` is registered
- **THEN** it remains a singleton registered as `IM0CombatCore` and self, using combat timing settings and `INhemLogger`

#### Scenario: PlayerLocomotion registration parity
- **WHEN** `M0PlayerLocomotion` is registered
- **THEN** it remains a singleton registered as `IM0PlayerLocomotion` and self, using locomotion settings

#### Scenario: MemoryState registration parity
- **WHEN** `M0MemoryState` is registered
- **THEN** it remains a singleton registered as `IM0MemoryState` and self, using the configured default reveal candidate id

#### Scenario: MemoryVFXResponse registration parity
- **WHEN** `M0MemoryVFXResponse` is registered
- **THEN** it remains a singleton registered as self, using configured reveal feedback duration, cooldown, and intensity label

### Requirement: Config Validation Remains Explicit
The runtime service composition collaborator SHALL fail clearly when required authored configs are missing and SHALL NOT silently fall back to broad lookup or default resource loading.

#### Scenario: Missing combat config fails clearly
- **WHEN** combat timing config is missing during composition
- **THEN** setup fails with a clear composition error

#### Scenario: Missing locomotion config fails clearly
- **WHEN** locomotion config is missing during composition
- **THEN** setup fails with a clear composition error

#### Scenario: Missing memory runtime tuning config fails clearly
- **WHEN** memory runtime tuning config is missing during composition
- **THEN** setup fails with a clear composition error

### Requirement: Runtime Service Composition Does Not Own Gameplay Truth
The runtime service composition collaborator SHALL only construct and register services. It MUST NOT decide or mutate gameplay outcomes.

#### Scenario: Combat truth remains in CombatCore
- **WHEN** combat actions are requested or resolved
- **THEN** combat validity, timing, result, and counter/reveal request context remain owned by CombatCore

#### Scenario: Movement truth remains in PlayerLocomotion
- **WHEN** movement input or recovery movement is evaluated
- **THEN** movement truth remains owned by PlayerLocomotion

#### Scenario: Memory truth remains in MemoryState
- **WHEN** memory reveal or collect is accepted, rejected, or duplicated
- **THEN** memory truth remains owned by MemoryState and MemoryInteractionService remains the orchestration owner

### Requirement: Runtime Service Composition Avoids Forbidden Runtime Composition APIs
Owned runtime service composition code SHALL avoid broad Unity discovery, resource fallback, service locator lookup, and direct Unity debug logging.

#### Scenario: No broad lookup introduced
- **WHEN** source guardrails scan the runtime service composition collaborator and `GameplayLifetimeScope`
- **THEN** no `FindObject*`, broad `FindObjectsByType`, `Resources.Load`, or Service Locator lookup is introduced

#### Scenario: No direct Unity debug logging introduced
- **WHEN** source guardrails scan the runtime service composition collaborator and `GameplayLifetimeScope`
- **THEN** no direct `UnityEngine.Debug.Log`, `Debug.LogWarning`, `Debug.LogError`, `Debug.Log`, `Debug.LogWarning`, or `Debug.LogError` call is introduced

### Requirement: M0/S4 Behavior Is Preserved
Extracting runtime service composition SHALL preserve verified M0/S4 behavior.

#### Scenario: M0 combat and locomotion regressions remain green
- **WHEN** focused EditMode tests for combat, locomotion, input routing, and enemy intent run
- **THEN** they pass with behavior equivalent to baseline

#### Scenario: Memory path regressions remain green
- **WHEN** focused EditMode tests for memory interaction, reveal feedback state, and runtime memory log run
- **THEN** they pass with behavior equivalent to baseline

#### Scenario: PlayMode or manual memory smoke remains equivalent
- **WHEN** the player runs the memory interaction smoke path
- **THEN** eligible prompt, accepted Interact, reveal feedback once, runtime log append once, and duplicate/spam safety remain equivalent to baseline

### Requirement: Verification Evidence Covers Composition Extraction
Closure evidence SHALL prove the runtime service composition extraction is behavior-preserving and architecture-compliant.

#### Scenario: Evidence package is complete
- **WHEN** the change is ready for closure
- **THEN** evidence records compile validation, source composition tests, focused regression tests, console classification, OpenSpec strict validation, and PASS/PARTIAL/FAIL summary
