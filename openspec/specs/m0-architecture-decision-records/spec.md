## Purpose

Define the M0 architecture decision record and technical requirement registry deliverables used for traceability, consistency checks, and gate evaluation.

## Requirements

### Requirement: M0 ADR documents SHALL be created as a lean decision record set
The system SHALL define a documentation deliverable that creates exactly five ADR files for M0 architecture traceability:
- `docs/architecture/adr/ADR-0001-m0-runtime-foundation-and-scene-composition.md`
- `docs/architecture/adr/ADR-0002-m0-gameplay-truth-ownership-boundaries.md`
- `docs/architecture/adr/ADR-0003-m0-presentation-and-debug-read-only-boundaries.md`
- `docs/architecture/adr/ADR-0004-m0-di-and-assembly-boundary-strategy.md`
- `docs/architecture/adr/ADR-0005-m0-shared-contracts-strategy.md`

Each ADR SHALL record already-made decisions only and SHALL NOT introduce new architecture or expanded M0 scope.

#### Scenario: ADR set creation is scoped correctly
- **WHEN** the change is implemented
- **THEN** exactly the five specified ADR files exist under `docs/architecture/adr/`
- **AND** each ADR records only the provided M0 decision coverage
- **AND** unresolved decisions are marked `Open`

### Requirement: ADR-0001 SHALL capture M0 runtime foundation and scene composition boundaries
ADR-0001 SHALL record the following decisions:
- Unity 6000.3.x + URP
- Additive scene composition
- Bootstrap / Systems / Gameplay / Camera / UI / Level separation
- `ProjectRootLifetimeScope` application lifetime only
- Scene scopes own gameplay lifetime

#### Scenario: ADR-0001 coverage is complete
- **WHEN** ADR-0001 is reviewed
- **THEN** all required runtime foundation decisions are present as stated

### Requirement: ADR-0002 SHALL capture gameplay truth ownership boundaries
ADR-0002 SHALL record:
- Pure C# gameplay truth
- Input emits intent only
- Locomotion owns movement truth
- Target Context owns target truth
- Combat Core owns combat validity/results
- Enemy Intent owns telegraph/commit/recovery
- Health owns damage/consequence/reaction
- Memory State owns reveal acceptance/rejection
- Encounter owns lifecycle only

#### Scenario: ADR-0002 ownership model is explicit
- **WHEN** ADR-0002 is reviewed
- **THEN** every listed gameplay domain has an explicit truth ownership boundary

### Requirement: ADR-0003 SHALL capture presentation and debug read-only boundaries
ADR-0003 SHALL record:
- Animator presentation only
- Camera owns framing/readability only
- Memory VFX Response is downstream presentation only
- Debug Overlay is read-only snapshot aggregation
- UI/UX foundation is documentation only for now

#### Scenario: ADR-0003 preserves read-only separation
- **WHEN** ADR-0003 is reviewed
- **THEN** presentation and debug concerns are documented as downstream/read-only relative to gameplay truth

### Requirement: ADR-0004 SHALL capture M0 DI and assembly boundaries
ADR-0004 SHALL record:
- Manual VContainer scopes for M0
- Generated DI deferred
- No gameplay truth registered globally by accident
- asmdef dependency direction
- No domain assembly depends on UI/VFX/Camera unless explicitly presentation-facing

#### Scenario: ADR-0004 enforces boundary constraints
- **WHEN** ADR-0004 is reviewed
- **THEN** DI strategy and assembly dependency direction constraints are explicitly documented

### Requirement: ADR-0005 SHALL capture shared contracts strategy for M0
ADR-0005 SHALL record:
- `M0Contracts.cs` allowed as temporary shared contract hub
- `M0Contracts.cs` remains contracts-only
- No behavior logic in `M0Contracts.cs`
- Split trigger after First Playable or when contracts become too broad
- Possible future change `split-m0-contracts-by-domain`

#### Scenario: ADR-0005 documents temporary contract hub guardrails
- **WHEN** ADR-0005 is reviewed
- **THEN** temporary contract hub constraints and split trigger conditions are explicit

### Requirement: M0 technical requirement registry SHALL provide stable IDs and traceability fields
The system SHALL define `docs/architecture/tr-registry.yaml` containing stable technical requirement IDs for the M0 skeleton layer. Every entry SHALL include:
- `id`
- `title`
- `status`
- `source_gdds`
- `adr_refs`
- `implementation_refs`
- `test_refs`
- `notes`

The registry SHALL include at minimum:
- `TR-M0-FOUNDATION-001`
- `TR-M0-FOUNDATION-002`
- `TR-M0-INPUT-001`
- `TR-M0-TRUTH-001`
- `TR-M0-ANIMATION-001`
- `TR-M0-COMBAT-001`
- `TR-M0-LOCOMOTION-001`
- `TR-M0-TARGET-001`
- `TR-M0-CAMERA-001`
- `TR-M0-ENEMY-001`
- `TR-M0-HEALTH-001`
- `TR-M0-MEMORY-001`
- `TR-M0-MEMORY-VFX-001`
- `TR-M0-ENCOUNTER-001`
- `TR-M0-DEBUG-001`
- `TR-M0-DI-001`
- `TR-M0-CONTRACTS-001`

#### Scenario: TR registry is complete and evaluable
- **WHEN** `tr-registry.yaml` is reviewed
- **THEN** all required minimum TR IDs are present
- **AND** each entry includes all required fields
- **AND** unresolved decisions are marked as `Open`

### Requirement: Scope guardrails SHALL prohibit architecture expansion in this change
This change SHALL remain documentation-only and SHALL NOT include runtime code changes, Unity scene changes, prefab changes, UI/VFX implementation, generated DI enablement, or new gameplay behavior.

#### Scenario: Implementation remains documentation-only
- **WHEN** the change diff is reviewed
- **THEN** modified or added files are limited to architecture documentation artifacts
- **AND** no runtime or content behavior changes are present
