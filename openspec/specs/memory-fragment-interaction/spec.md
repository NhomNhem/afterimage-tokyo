# memory-fragment-interaction Specification

## Purpose
TBD - created by archiving change implement-m1-memory-fragment-interaction. Update Purpose after archive.
## Requirements
### Requirement: Eligible Memory Fragment Interaction
The system MUST allow the player to trigger Interact only when a Memory Fragment is eligible by proximity/interaction rules.

#### Scenario: Interact when eligible
- **WHEN** the player is within eligible interaction range of a fragment and presses Interact
- **THEN** the interaction request is emitted for orchestration

#### Scenario: Interact when not eligible
- **WHEN** the player presses Interact without an eligible fragment
- **THEN** no reveal/collect request is accepted and the system remains stable

### Requirement: Interaction Orchestration Ownership
The interaction flow MUST route through `MemoryInteractionService` or an equivalent clearly owned use-case service.

#### Scenario: Service-owned flow
- **WHEN** an eligible Interact request is triggered
- **THEN** `MemoryInteractionService` orchestrates the request to MemoryState rather than UI/VFX/Animancer components

### Requirement: MemoryState Truth Ownership
MemoryState MUST be the source of truth for accepted/rejected reveal/collect outcomes.

#### Scenario: Accepted outcome
- **WHEN** MemoryState accepts a reveal/collect request
- **THEN** the accepted state transition is recorded as authoritative truth

#### Scenario: Rejected outcome
- **WHEN** MemoryState rejects a reveal/collect request
- **THEN** rejection is recorded and no truth ownership moves to presentation layers

### Requirement: Duplicate Interaction Safety
Duplicate interaction with the same fragment MUST be rejected, ignored safely, or reported as already collected.

#### Scenario: Duplicate handled safely
- **WHEN** the player re-triggers interaction on an already processed fragment
- **THEN** the system returns a safe duplicate result without crash, corruption, or duplicate truth mutation

### Requirement: Presentation-Only Response
UI/VFX/Audio/Animancer MUST NOT determine whether a fragment was collected.

#### Scenario: Accepted presentation response
- **WHEN** MemoryState emits accepted result
- **THEN** presentation layers may play accepted placeholder response only as downstream effect

#### Scenario: Rejected presentation response
- **WHEN** MemoryState emits rejected result
- **THEN** presentation layers may show rejected placeholder response only as downstream effect

### Requirement: ScriptableObject Static Data Boundary
`MemoryFragmentDefinition` ScriptableObject MUST contain static fragment definition/config data and MUST NOT store runtime collected/revealed state.

#### Scenario: Static data authored
- **WHEN** a fragment definition asset is authored
- **THEN** only static metadata/config fields are present (id/title/text/icon/presentation refs)

#### Scenario: Runtime state excluded
- **WHEN** runtime interaction occurs
- **THEN** collected/revealed runtime truth is stored outside ScriptableObject

### Requirement: Debug/Evidence Observability
Debug/evidence output MUST expose enough state to verify nearby fragment, interact pressed, accepted/rejected result, and duplicate handling behavior.

#### Scenario: Evidence capture
- **WHEN** smoke/test evidence is recorded
- **THEN** logs/snapshots can demonstrate interaction eligibility, request route, acceptance/rejection, and duplicate safety

### Requirement: Scene/Prefab Change Disclosure
Any scene or prefab changes introduced for this capability MUST be explicitly listed and justified in evidence.

#### Scenario: Scene change introduced
- **WHEN** scene/prefab edits are required for minimal fragment placement
- **THEN** evidence includes explicit change list and scope justification
