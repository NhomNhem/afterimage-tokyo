## ADDED Requirements

### Requirement: Accepted memory reveal appends one runtime log entry
The system SHALL append exactly one visible runtime memory log entry after a Memory Fragment reveal/collect outcome is accepted by the MemoryState-backed interaction path.

#### Scenario: Accepted reveal appends log entry
- **WHEN** a Memory Fragment interaction is accepted through the S3-2 route
- **THEN** one runtime memory log entry is visible for that accepted fragment outcome

#### Scenario: Accepted reveal entry follows memory truth
- **WHEN** the runtime memory log appends an entry
- **THEN** the entry is driven by an accepted interaction/reveal context or read-only memory response snapshot downstream of MemoryState acceptance

### Requirement: Non-accepted interactions do not append runtime log entries
The system SHALL NOT append runtime memory log entries for unavailable, rejected, duplicate, ignored, or cooldown-gated interactions.

#### Scenario: No eligible fragment appends no entry
- **WHEN** Interact is pressed without an eligible Memory Fragment
- **THEN** the runtime memory log does not append an entry

#### Scenario: Rejected reveal appends no entry
- **WHEN** MemoryState rejects a reveal or collect request
- **THEN** the runtime memory log does not append an entry

#### Scenario: Duplicate interaction appends no duplicate entry
- **WHEN** a duplicate Memory Fragment interaction is rejected or ignored by the S3-2 path after an accepted entry already exists
- **THEN** the runtime memory log does not append another entry for the same accepted fragment outcome

### Requirement: Runtime log remains presentation-only
The runtime memory log system MUST remain downstream UI/presentation or read-model state and MUST NOT decide interaction validity, reveal acceptance, duplicate handling truth, MemoryState truth, combat outcome, or input execution.

#### Scenario: Runtime log observes read-only context
- **WHEN** runtime log state evaluates whether to append an entry
- **THEN** it observes an approved read-only accepted interaction/reveal context or memory response snapshot

#### Scenario: Runtime log does not mutate gameplay truth
- **WHEN** runtime log state appends, displays, updates, clears, or suppresses an entry
- **THEN** it does not call MemoryState mutation APIs, MemoryInteractionService command paths, input callbacks, fragment mutation paths, CombatCore result APIs, or TargetContext mutation APIs

### Requirement: Runtime log suppresses duplicates as display state only
The runtime memory log system SHALL suppress duplicate visible entries for the same accepted fragment outcome without changing gameplay duplicate handling.

#### Scenario: Repeated accepted context is observed
- **WHEN** the same accepted fragment outcome is observed more than once by the runtime log
- **THEN** only one visible runtime memory log entry exists for that outcome

#### Scenario: Presentation deduplication does not affect MemoryState
- **WHEN** the runtime log suppresses a duplicate visible entry
- **THEN** MemoryState reveal/collect truth and MemoryInteractionService duplicate handling remain unchanged

### Requirement: Runtime log entry content remains placeholder-scoped
The runtime memory log entry SHALL use minimal placeholder content and SHALL NOT introduce journal, inventory, quest, lore, save/profile, progression, dialogue, narrative branching, clue tracking, contradiction tracking, district reinterpretation, or truth restoration behavior.

#### Scenario: Minimal placeholder entry is displayed
- **WHEN** a runtime memory log entry is rendered
- **THEN** it shows only a concise fragment label or fallback identifier plus a short revealed/collected state

#### Scenario: Missing display data uses fallback
- **WHEN** an accepted fragment outcome has missing display data
- **THEN** the runtime memory log uses a placeholder-safe fallback label and does not crash

### Requirement: Existing M1 prompt and reveal feedback behavior is preserved
The runtime memory log system MUST preserve S3-2 Memory Fragment interaction behavior, S3-3 prompt behavior, and S3-4 reveal feedback behavior.

#### Scenario: Existing interaction route is preserved
- **WHEN** the player presses Interact on an eligible Memory Fragment
- **THEN** the route remains input intent to MemoryInteractionService to MemoryState before any runtime log entry appears

#### Scenario: Prompt and reveal feedback remain unchanged
- **WHEN** the runtime memory log placeholder is added
- **THEN** interaction prompt visibility and accepted reveal feedback playback remain consistent with S3-3 and S3-4 evidence

### Requirement: Runtime memory log evidence is captured
S4-2 verification MUST record evidence for accepted log append, duplicate suppression, ownership boundary preservation, manual PlayMode visibility, console classification, and dirty asset classification.

#### Scenario: Evidence capture
- **WHEN** S4-2 verification is recorded
- **THEN** evidence includes PASS/PARTIAL/FAIL classification for runtime log behavior, scope boundaries, console output, and asset edit classification

#### Scenario: Focused automated tests are recorded
- **WHEN** S4-2 automated verification is recorded
- **THEN** focused EditMode tests cover accepted append, non-accepted non-append, duplicate suppression, fallback display data, and ownership guardrails
