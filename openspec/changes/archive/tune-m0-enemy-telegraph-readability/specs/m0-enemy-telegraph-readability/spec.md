# Spec: M0 Enemy Telegraph Readability

## Intent

Improve readability of EnemyIntent `Telegraph -> Commit -> Active -> Recovery` in M0 duel playtests while preserving gameplay ownership boundaries.

## Requirements

### Requirement: EnemyIntent remains authority

EnemyIntent MUST remain the sole authority for telegraph lifecycle truth (phase state, timing windows, punish context).

#### Scenario: Readability tuning preserves EnemyIntent ownership

- **GIVEN** S2-3 readability tuning is applied
- **WHEN** enemy telegraph cues are observed and validated
- **THEN** phase truth still originates from EnemyIntent snapshot/model
- **AND** no presentation layer mutates enemy lifecycle truth

### Requirement: CombatCore authority remains unchanged

CombatCore MUST remain authority for combat timing/results and MUST NOT be replaced by presentation-driven timing.

#### Scenario: Telegraph readability does not alter combat ownership

- **GIVEN** telegraph readability pass is active
- **WHEN** combat resolution events occur
- **THEN** CombatCore still decides combat outcomes
- **AND** telegraph cues are advisory/readability signals only

### Requirement: Readability criteria for phase distinction

Telegraph, Commit, Active, and Recovery cues MUST be distinguishable enough for repeatable manual verification.

#### Scenario: Manual phase distinction

- **GIVEN** a tester observes at least 3 enemy intent loops in PlayMode
- **WHEN** cues are reviewed
- **THEN** tester can consistently identify phase order and transitions
- **AND** can explain defensive timing opportunity from cues

### Requirement: Presentation remains non-authoritative

Animator/Animancer, VFX, Camera, UI, and Debug Overlay MUST remain presentation/read-only systems.

#### Scenario: No gameplay truth migration

- **GIVEN** readability enhancements are in place
- **WHEN** inspecting system boundaries
- **THEN** no gameplay truth is owned by Animator/VFX/Camera/UI/Debug Overlay
- **AND** Debug Overlay remains read-only

### Requirement: Evidence-first closure

S2-3 closure MUST include focused verification evidence with PASS/PARTIAL/FAIL classification.

#### Scenario: Evidence package completeness

- **GIVEN** S2-3 verification is performed
- **WHEN** reviewing evidence artifact
- **THEN** it includes:
  - phase readability table (Telegraph/Commit/Active/Recovery)
  - console classification
  - scope creep classification
  - boundary confirmation
- **AND** final verdict is PASS, PARTIAL, or FAIL with rationale
