## ADDED Requirements

### Requirement: Attack Dodge Parry Readability Definition
The system SHALL define readability tuning for Attack, Dodge, and Parry as improved phase clarity and outcome clarity in the existing M0 duel loop, without adding new combat mechanics.

#### Scenario: Readability axes are explicit before tuning
- **WHEN** S2-2 planning artifacts are reviewed
- **THEN** the change SHALL explicitly define readable phase expectations for Attack, Dodge, and Parry using the existing phase model (windup/active/recovery and success/failure feedback)

### Requirement: Safe Tuning Surface and Ownership Boundaries
The system SHALL constrain S2-2 tuning to ownership-safe surfaces and SHALL preserve gameplay authority boundaries.

#### Scenario: CombatCore authority is preserved
- **WHEN** S2-2 implementation is proposed or reviewed
- **THEN** CombatCore SHALL remain authority for combat timing, action validity, results, CounterWindow, and reveal request emission

#### Scenario: PlayerLocomotion authority is preserved
- **WHEN** dodge readability adjustments are proposed
- **THEN** PlayerLocomotion SHALL remain authority for dodge movement, facing support, recovery movement, and movement restrictions

#### Scenario: Presentation stays downstream-only
- **WHEN** animation, VFX, or camera adjustments are included
- **THEN** Animator/VFX/Camera SHALL remain presentation-only and SHALL NOT mutate gameplay truth or action validity

#### Scenario: Forbidden gameplay-authority shortcuts are blocked
- **WHEN** tuning introduces root motion authority, animation event-driven gameplay resolution, or input bypass paths
- **THEN** the change SHALL be classified as out of scope and rejected for S2-2

### Requirement: Evidence-First Verification Contract
The system SHALL require evidence artifacts that prove readability outcomes with explicit classification.

#### Scenario: Required evidence table exists
- **WHEN** S2-2 verification is submitted
- **THEN** the evidence SHALL include a PASS/PARTIAL/FAIL table for Attack readability, Dodge readability, Parry readability, and overall duel readability

#### Scenario: Before/after proof exists
- **WHEN** readability tuning is claimed complete
- **THEN** evidence SHALL include before/after captures or logs that show phase readability impact without ownership boundary violations

#### Scenario: Console classification is recorded
- **WHEN** verification is documented
- **THEN** the evidence SHALL classify warnings/errors into blocking vs non-blocking and SHALL identify any external/unrelated issues

### Requirement: Manual PlayMode Readability Checklist
The system SHALL define a repeatable manual checklist for Attack, Dodge, and Parry readability review in PlayMode.

#### Scenario: Checklist covers Attack readability
- **WHEN** manual PlayMode review is run
- **THEN** the checklist SHALL verify readable Attack windup, active, and recovery beats and clear hit/whiff feedback

#### Scenario: Checklist covers Dodge readability
- **WHEN** manual PlayMode review is run
- **THEN** the checklist SHALL verify Dodge start/commit/recovery readability and clear success/failure interpretation by tester

#### Scenario: Checklist covers Parry readability
- **WHEN** manual PlayMode review is run
- **THEN** the checklist SHALL verify Parry timing readability, success/failure distinction, and CounterWindow readability

### Requirement: Test Requirements for Timing or Logic Contract Changes
The system SHALL require focused automated tests when tuning includes timing/logic contract changes in gameplay-authoritative systems.

#### Scenario: No new timing logic change
- **WHEN** tuning is presentation-only or config-only with no logic contract change
- **THEN** existing focused tests MAY be rerun without requiring new test creation

#### Scenario: Timing or logic contract changes
- **WHEN** tuning modifies combat timing transitions, validation rules, or state contract behavior
- **THEN** focused EditMode tests SHALL be added or updated for the changed contract and included in verification evidence

### Requirement: S2-2 Acceptance Criteria Classification
The system SHALL use clear PASS/PARTIAL/FAIL criteria to determine closure of S2-2.

#### Scenario: PASS closure
- **WHEN** Attack, Dodge, and Parry readability each pass manual checklist and no blocking regressions are found
- **THEN** S2-2 SHALL be classified PASS

#### Scenario: PARTIAL closure
- **WHEN** at least one readability axis remains unclear but core loop remains stable and safe
- **THEN** S2-2 SHALL be classified PARTIAL with explicit follow-up actions

#### Scenario: FAIL closure
- **WHEN** tuning introduces ownership boundary violations, gameplay regressions, or unreadable core beats
- **THEN** S2-2 SHALL be classified FAIL and SHALL NOT be closed
