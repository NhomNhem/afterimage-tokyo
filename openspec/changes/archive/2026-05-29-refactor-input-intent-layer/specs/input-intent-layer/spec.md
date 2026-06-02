## ADDED Requirements

### Requirement: Input Layer SHALL be split into Unity Adapter and Gameplay Intent publication
The system MUST separate Unity InputAction callback binding/state capture from gameplay-facing intent snapshot/event publication. The Unity Adapter layer SHALL own callback binding only, and the Gameplay Intent layer SHALL own raw intent publication only.

#### Scenario: Unity callback ownership is isolated
- **WHEN** input actions are wired for gameplay
- **THEN** Unity InputAction callback binding and raw device state capture are handled by the Unity Adapter layer only
- **AND** the adapter does not perform gameplay validity or outcome decisions

#### Scenario: Gameplay intent publication is isolated
- **WHEN** gameplay systems consume input
- **THEN** they consume raw intent snapshots/events from the Gameplay Intent layer
- **AND** the Gameplay Intent layer does not own combat, locomotion, target, or memory truth

### Requirement: Input behavior SHALL remain equivalent for current M0 and S3-2 actions
The refactor MUST preserve behavior for Move, LightAttack, HeavyAttack (if present), Dodge, Parry, Counter, LockOn, and Interact under current M0 and S3-2 playable flows.

#### Scenario: Core action routing parity is preserved
- **WHEN** the supported actions are triggered through the Unity New Input System
- **THEN** routed intents exposed to gameplay are behavior-equivalent to pre-refactor behavior
- **AND** no new gameplay outcomes are introduced by the input refactor itself

#### Scenario: Interact remains compatible with Memory Fragment flow
- **WHEN** Interact is triggered while in memory fragment interaction conditions
- **THEN** MemoryInteractionService continues to orchestrate interaction handling
- **AND** MemoryState continues to own reveal/collect acceptance and truth

### Requirement: Input Layer SHALL remain raw-intent-only
The Input Layer MUST publish only raw intent and MUST NOT own gameplay truth or resolve gameplay validity.

#### Scenario: Combat truth remains outside Input
- **WHEN** attack/defensive intents are published
- **THEN** CombatCore remains the owner of combat validity and result transitions
- **AND** Input does not decide success/failure outcomes

#### Scenario: Movement and target truth remain outside Input
- **WHEN** Move and LockOn-related intents are published
- **THEN** PlayerLocomotion remains owner of movement truth
- **AND** TargetContext remains owner of lock-on truth

### Requirement: Debug evidence SHALL remain available after refactor
The refactor MUST preserve LastInput or equivalent debug/evidence visibility so smoke and regression checks remain operable.

#### Scenario: LastInput evidence continuity
- **WHEN** supported gameplay actions are triggered
- **THEN** debug/evidence output continues to expose latest routed input intent label or equivalent
- **AND** the output remains usable for manual smoke and regression classification

### Requirement: Verification evidence SHALL include focused routing checks and smoke classification
The change MUST provide focused routing verification and manual smoke evidence with explicit PASS/PARTIAL/FAIL classification.

#### Scenario: Focused routing evidence exists
- **WHEN** implementation is verified
- **THEN** focused checks or tests exist for key action routing and edge transitions
- **AND** evidence covers Interact compatibility with the active S3-2 flow

#### Scenario: Manual smoke checklist and classification exists
- **WHEN** manual smoke is executed
- **THEN** results include Move, LightAttack, Dodge, Parry, Counter (if available), LockOn acquire/release, and Interact
- **AND** console/log classification and PASS/PARTIAL/FAIL summary are recorded
