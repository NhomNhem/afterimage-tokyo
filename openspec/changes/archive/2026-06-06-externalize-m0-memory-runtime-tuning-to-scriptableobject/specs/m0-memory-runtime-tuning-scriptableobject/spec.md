## ADDED Requirements

### Requirement: Authored Memory Runtime Tuning Config
The system SHALL provide an authored ScriptableObject config for M0 memory runtime tuning values used by gameplay scope memory service composition.

#### Scenario: Config contains current memory runtime defaults
- **WHEN** the default M0 memory runtime tuning config asset is inspected
- **THEN** it exposes the current default reveal candidate id, reveal feedback duration seconds, reveal feedback cooldown seconds, and reveal feedback intensity label

#### Scenario: Config stores static tuning only
- **WHEN** runtime memory interaction occurs
- **THEN** collected, revealed, accepted, rejected, duplicate, or playback runtime state is not stored in the ScriptableObject config

### Requirement: GameplayLifetimeScope Uses Explicit Memory Runtime Config
`GameplayLifetimeScope` SHALL use an explicitly assigned memory runtime tuning config when composing `M0MemoryState` and `M0MemoryVFXResponse`.

#### Scenario: MemoryState composition uses config value
- **WHEN** gameplay scope composition creates `M0MemoryState`
- **THEN** the default reveal candidate id comes from the assigned memory runtime tuning config

#### Scenario: MemoryVFXResponse composition uses config values
- **WHEN** gameplay scope composition creates `M0MemoryVFXResponse`
- **THEN** reveal feedback duration, cooldown duration, and intensity label come from the assigned memory runtime tuning config

#### Scenario: Missing config fails clearly
- **WHEN** gameplay scope composition runs without an assigned memory runtime tuning config
- **THEN** setup fails with a clear composition error rather than silently using fallback lookup

### Requirement: Memory Runtime Tuning Preserves Gameplay Truth Ownership
Externalizing memory runtime tuning SHALL NOT move gameplay truth into the ScriptableObject config, Bootstrap, UI, VFX, audio, or runtime log systems.

#### Scenario: MemoryState remains truth owner
- **WHEN** a memory reveal or collect request is accepted or rejected
- **THEN** `MemoryState` remains the authority for reveal/collect truth

#### Scenario: MemoryInteractionService remains orchestration owner
- **WHEN** the player presses Interact on an eligible memory fragment
- **THEN** the route remains Interact to `MemoryInteractionService` to `MemoryState` before downstream presentation/log response

#### Scenario: Presentation remains downstream
- **WHEN** reveal feedback, audio placeholder, prompt, or runtime memory log reacts to an accepted memory outcome
- **THEN** those systems remain downstream presentation/read-model consumers and do not decide reveal acceptance or duplicate behavior

### Requirement: Memory Runtime Tuning Avoids Broad Lookup And Direct Debug Logging
The implementation SHALL avoid broad Unity lookup, resource fallback, service locator lookup, and direct Unity debug logging in owned runtime composition code.

#### Scenario: No broad lookup introduced
- **WHEN** source guardrails scan owned memory runtime tuning composition code
- **THEN** no `FindObject*`, broad `FindObjectsByType`, `Resources.Load`, or Service Locator pattern is introduced

#### Scenario: No direct Unity debug logging introduced
- **WHEN** source guardrails scan owned memory runtime tuning composition code
- **THEN** no direct `UnityEngine.Debug.Log`, `Debug.LogWarning`, `Debug.LogError`, `Debug.Log`, `Debug.LogWarning`, or `Debug.LogError` call is introduced

### Requirement: Memory Runtime Tuning Preserves M0/S4 Behavior
Externalizing memory runtime tuning SHALL preserve verified M0/S4 memory behavior.

#### Scenario: Accepted interaction path remains equivalent
- **WHEN** the player interacts with an eligible memory fragment
- **THEN** the accepted path remains equivalent to the baseline MemoryInteractionService to MemoryState route

#### Scenario: Reveal feedback remains one-shot
- **WHEN** an accepted memory reveal occurs
- **THEN** reveal feedback appears once and spam Interact does not replay feedback incorrectly

#### Scenario: Runtime memory log remains single-entry
- **WHEN** an accepted memory reveal appends a runtime memory log entry
- **THEN** exactly one entry is appended for the accepted fragment outcome and duplicate/spam Interact does not append a duplicate

### Requirement: Verification Evidence Covers Config And Regression
Closure evidence SHALL prove the memory runtime tuning refactor is behavior-preserving and architecture-compliant.

#### Scenario: Evidence records automated checks
- **WHEN** the change is ready for closure
- **THEN** evidence records compile validation, focused source/scene composition tests, memory interaction tests, runtime memory log tests, and OpenSpec strict validation

#### Scenario: Evidence records smoke classification
- **WHEN** the change is ready for closure
- **THEN** evidence records PlayMode or manual smoke classification for eligible prompt, accepted Interact, reveal feedback once, runtime log append once, duplicate/spam safety, and console output
