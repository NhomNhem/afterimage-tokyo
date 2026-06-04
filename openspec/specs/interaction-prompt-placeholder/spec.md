# interaction-prompt-placeholder Specification

## Purpose
TBD - created by archiving change add-m1-interaction-prompt-placeholder. Update Purpose after archive.
## Requirements
### Requirement: Prompt appears for eligible Memory Fragment
The system SHALL display a minimal interaction prompt when the player has an eligible Memory Fragment interaction context.

#### Scenario: Eligible fragment prompt appears
- **WHEN** the player is within the approved eligible interaction context for a Memory Fragment
- **THEN** the prompt is visible with concise placeholder text

### Requirement: Prompt hides when interaction is unavailable
The system SHALL hide the interaction prompt when no eligible Memory Fragment interaction context is available.

#### Scenario: No eligible fragment prompt hidden
- **WHEN** the player is outside Memory Fragment eligibility or no eligible fragment exists
- **THEN** the prompt is not visible

#### Scenario: Eligibility lost prompt hidden
- **WHEN** the prompt is visible and the player leaves the eligible interaction context
- **THEN** the prompt is hidden

### Requirement: Prompt remains presentation-only
The prompt system MUST remain a UI/presentation consumer and MUST NOT decide interaction validity, reveal/collect acceptance, duplicate handling, or MemoryState truth.

#### Scenario: Prompt observes read-only context
- **WHEN** prompt visibility is updated
- **THEN** the prompt reads an approved read-only interaction context or UI-facing read model

#### Scenario: Prompt does not mutate gameplay truth
- **WHEN** prompt visibility changes
- **THEN** no MemoryState, MemoryInteractionService command, input callback, or fragment mutation path is invoked by the prompt

### Requirement: Interact route remains owned by existing input and interaction systems
The prompt system MUST NOT own Interact input callbacks or interaction execution.

#### Scenario: Prompt visible and Interact pressed
- **WHEN** the prompt is visible and the player presses Interact
- **THEN** the existing raw input route and S3-2 interaction orchestration handle the interaction

### Requirement: Prompt scope remains placeholder-only
The prompt system MUST NOT introduce runtime memory log, reveal VFX/audio, inventory, quest, dialogue, save/profile, progression, or full HUD behavior.

#### Scenario: Placeholder prompt only
- **WHEN** the prompt is implemented
- **THEN** it only communicates interaction availability and does not add broader UI/gameplay systems

### Requirement: Prompt evidence is captured
Prompt verification MUST record evidence for visible state, hidden state, ownership boundary preservation, console classification, and dirty asset classification.

#### Scenario: Evidence capture
- **WHEN** S3-3 verification is recorded
- **THEN** evidence includes PASS/PARTIAL/FAIL classification for prompt visibility behavior and scope boundaries
