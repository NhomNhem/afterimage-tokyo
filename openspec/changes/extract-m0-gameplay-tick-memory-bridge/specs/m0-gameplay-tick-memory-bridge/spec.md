## ADDED Requirements

### Requirement: Gameplay Tick Handler SHALL remain orchestration owner
`M0GameplayTickHandler` MUST remain the owner of top-level update orchestration order after memory bridge extraction. The extracted memory bridge MUST be invoked by the tick handler and MUST NOT become an autonomous owner of runtime loop flow.

#### Scenario: Tick orchestration ownership preserved
- **WHEN** the memory bridge is introduced for Slice 1 extraction
- **THEN** `M0GameplayTickHandler` continues to own and execute the explicit orchestration order
- **AND** no memory bridge component independently drives update order outside tick-handler orchestration

### Requirement: Extracted bridge SHALL handle memory orchestration only
The extracted bridge MUST be limited to memory interaction/reveal orchestration routing concerns. It MUST NOT absorb non-memory routing concerns from combat, locomotion, target context, camera, or general input architecture.

#### Scenario: Scope boundary enforced
- **WHEN** memory-related logic is moved from `M0GameplayTickHandler`
- **THEN** only memory interaction/reveal orchestration logic is moved
- **AND** non-memory orchestration responsibilities remain outside this bridge

### Requirement: Memory truth ownership SHALL remain unchanged
`MemoryState` MUST remain reveal/collect truth authority and `MemoryInteractionService` MUST remain S3-2 interaction orchestration authority. The bridge MUST NOT make reveal acceptance/rejection decisions.

#### Scenario: Reveal acceptance ownership preserved
- **WHEN** an interact/reveal path executes through the extracted bridge
- **THEN** acceptance/rejection decisions are still made by `MemoryState`
- **AND** interaction orchestration remains in `MemoryInteractionService`
- **AND** the bridge performs routing/orchestration support only

### Requirement: S3-2 interaction behavior SHALL be preserved
Extraction MUST preserve S3-2 interact accepted path behavior and current duplicate interaction behavior exactly unless a separate approved change modifies that behavior.

#### Scenario: Interact accepted path parity
- **WHEN** the player executes Interact under accepted fragment conditions
- **THEN** the path `Interact -> MemoryInteractionService -> MemoryState` remains behavior-equivalent to baseline
- **AND** outcome acceptance remains unchanged

#### Scenario: Duplicate interaction parity
- **WHEN** duplicate interaction behavior occurs in baseline flow
- **THEN** extraction preserves the same observed duplicate behavior
- **AND** no deduplication policy change is introduced in this slice

### Requirement: Debug and evidence output SHALL remain equivalent or better
Extraction MUST keep memory-path debug/evidence outputs equivalent or better for triage and verification.

#### Scenario: Evidence quality maintained
- **WHEN** Slice 1 extraction is verified
- **THEN** debug/evidence outputs for memory interaction/reveal path remain available
- **AND** output quality is equivalent to or better than baseline for troubleshooting

### Requirement: Verification evidence SHALL include focused and regression checks
The change MUST include focused memory interaction checks, M0 regression checks, manual PlayMode checks for Interact path, console classification, and PASS/PARTIAL/FAIL summary.

#### Scenario: Evidence package complete
- **WHEN** extraction implementation is validated
- **THEN** focused tests cover memory interaction path
- **AND** regression checks cover M0 loop
- **AND** manual checklist covers `Interact -> MemoryInteractionService -> MemoryState`
- **AND** console classification and PASS/PARTIAL/FAIL table are recorded
