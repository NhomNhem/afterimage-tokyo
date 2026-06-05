## ADDED Requirements

### Requirement: Accepted memory reveal plays placeholder feedback
The system SHALL play restrained placeholder VFX and/or audio feedback after a Memory Fragment reveal/collect outcome is accepted by the MemoryState-backed path.

#### Scenario: Accepted reveal feedback plays
- **WHEN** a Memory Fragment interaction is accepted through the S3-2 route
- **THEN** the placeholder reveal feedback is played

#### Scenario: Feedback follows accepted response context
- **WHEN** accepted reveal feedback is triggered
- **THEN** it is driven by an accepted reveal/result context or memory VFX response state that is downstream of MemoryState acceptance

### Requirement: Non-accepted interactions do not play accepted reveal feedback
The system SHALL NOT play accepted reveal placeholder feedback for unavailable, rejected, duplicate, ignored, or cooldown-gated interactions.

#### Scenario: No eligible fragment does not play feedback
- **WHEN** Interact is pressed without an eligible Memory Fragment
- **THEN** accepted reveal feedback is not played

#### Scenario: Duplicate interaction does not replay accepted feedback
- **WHEN** a duplicate Memory Fragment interaction is rejected or ignored by the S3-2 path
- **THEN** accepted reveal feedback is not replayed

#### Scenario: Rejected reveal does not play feedback
- **WHEN** MemoryState rejects a reveal or collect request
- **THEN** accepted reveal feedback is not played

### Requirement: Reveal feedback remains presentation-only
The reveal feedback system MUST remain downstream presentation and MUST NOT decide interaction validity, reveal acceptance, duplicate handling, MemoryState truth, combat outcome, or input execution.

#### Scenario: Feedback observes read-only response state
- **WHEN** reveal feedback evaluates whether to play
- **THEN** it observes an approved read-only accepted reveal/result context or memory VFX response snapshot

#### Scenario: Feedback does not mutate gameplay truth
- **WHEN** reveal feedback starts, updates, completes, or resets
- **THEN** it does not call MemoryState mutation APIs, MemoryInteractionService command paths, input callbacks, fragment mutation paths, CombatCore result APIs, or TargetContext mutation APIs

### Requirement: Placeholder scope remains minimal
The reveal feedback system SHALL use minimal placeholder presentation sufficient for Sprint 3 readability and SHALL NOT introduce full cinematic, memory log UI, inventory, quest, dialogue, save/profile, progression, or final authored VFX/audio production scope.

#### Scenario: Placeholder feedback only
- **WHEN** S3-4 is implemented
- **THEN** the added behavior is limited to a small visual and/or audio acknowledgement of an accepted memory reveal

### Requirement: Reveal feedback preserves S3-2 and S3-3 behavior
The reveal feedback system MUST preserve the existing Memory Fragment interaction route and interaction prompt behavior.

#### Scenario: S3-2 route preserved
- **WHEN** the player presses Interact on an eligible Memory Fragment
- **THEN** the route remains input intent to MemoryInteractionService to MemoryState before any accepted feedback plays

#### Scenario: S3-3 prompt preserved
- **WHEN** reveal feedback is added
- **THEN** interaction prompt visibility and ownership behavior remain unchanged

### Requirement: Reveal feedback evidence is captured
S3-4 verification MUST record evidence for accepted feedback playback, non-playback on rejected or duplicate paths, ownership boundary preservation, console classification, and dirty asset classification.

#### Scenario: Evidence capture
- **WHEN** S3-4 verification is recorded
- **THEN** evidence includes PASS/PARTIAL/FAIL classification for accepted feedback, non-accepted feedback suppression, scope boundaries, console output, and asset edit classification
