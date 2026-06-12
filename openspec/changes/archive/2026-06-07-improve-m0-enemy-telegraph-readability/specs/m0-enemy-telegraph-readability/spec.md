## ADDED Requirements

### Requirement: Enemy Telegraph Readability Snapshot

The M0 enemy intent system SHALL expose a read-only readability snapshot that describes the current enemy phase, phase progress or remaining time, committed attack tags when applicable, and punish availability.

#### Scenario: Telegraph phase is distinguishable

- **GIVEN** the simple M0 enemy enters Telegraph
- **WHEN** an observer reads the enemy readability snapshot
- **THEN** the snapshot identifies Telegraph as distinct from Commit, Active, and Recovery
- **AND** the snapshot provides enough timing/progress information for debug/evidence to explain when commitment is expected

#### Scenario: Commit and Active preserve attack tags

- **GIVEN** the simple M0 enemy commits to an attack with M0 prototype attack tags
- **WHEN** the enemy transitions from Commit into Active
- **THEN** the readability snapshot preserves the committed attack tags
- **AND** observers can explain what attack intent is active without owning combat truth

#### Scenario: Recovery exposes punish availability

- **GIVEN** the simple M0 enemy enters Recovery with a punish window
- **WHEN** an observer reads the enemy readability snapshot
- **THEN** the snapshot indicates punish availability
- **AND** the value is derived from Enemy Intent and Telegraph truth, not from Debug Overlay or presentation state

### Requirement: Presentation Observes Telegraph Truth

Presentation, camera, VFX, audio, and Debug Overlay systems SHALL consume enemy telegraph readability as observers only.

#### Scenario: Debug Overlay cannot mutate enemy intent

- **GIVEN** Debug Overlay displays the enemy phase and punish availability
- **WHEN** the overlay refreshes or formats labels
- **THEN** it does not mutate enemy intent phase, timers, attack tags, punish windows, or combat results

#### Scenario: Presentation cue does not decide combat outcome

- **GIVEN** a presentation cue is aligned with Telegraph, Commit, Active, or Recovery
- **WHEN** the player evades, parries, or counters
- **THEN** Combat Core and Enemy Intent remain the only authorities for gameplay outcome and timing truth
- **AND** presentation state cannot accept or reject the action

### Requirement: Readability Evidence

The implementation SHALL produce focused automated and manual evidence that the M0 telegraph loop is readable enough for the `read -> evade/parry -> counter -> reveal` loop.

#### Scenario: Focused tests cover readability data

- **GIVEN** the change is implemented
- **WHEN** focused EditMode tests run
- **THEN** they verify the readability snapshot shape, phase distinction, attack tag continuity, and punish availability

#### Scenario: Manual loop sampling is recorded

- **GIVEN** the M0 duel scene is available
- **WHEN** manual PlayMode evidence is captured
- **THEN** at least three complete enemy intent loops are sampled
- **AND** Telegraph, Commit/Active, Recovery, punish readability, console output, and ownership boundaries are recorded
