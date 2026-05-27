## Context

M0 currently demonstrates Dodge as an input + combat-state timeline (`DodgeStartup -> DodgeActive -> DodgeRecovery`) but not as a reliable world-space movement expression. Evidence triage showed this is not a LockOn regression; it is a missing integration between Combat Core dodge states and Locomotion movement truth. Architecture ownership already defines Player Locomotion as movement truth owner and Combat Core as action validity/timing owner.

## Goals / Non-Goals

**Goals:**
- Add a deterministic locomotion dodge displacement path triggered by accepted Dodge flow.
- Keep ownership boundaries explicit:
  - Combat Core decides dodge validity and timing state.
  - Player Locomotion owns displacement execution.
  - Tick/bootstrap layer bridges state-to-movement intent.
- Make behavior testable and evidence-friendly via before/after movement proof.

**Non-Goals:**
- No changes to Dodge acceptance criteria in Combat Core.
- No Parry/Counter, LockOn, Memory, or camera behavior expansion.
- No animation-authoritative movement.
- No broad locomotion refactor beyond required dodge pathway.

## Decisions

1. **Introduce explicit dodge displacement request in locomotion boundary**
   - Rationale: Movement truth remains in locomotion; avoids camera/UI/presentation leakage.
   - Alternative rejected: apply displacement directly in tick handler by transform mutation (would bypass locomotion truth).

2. **Bridge using combat snapshot/state transition, not raw input press**
   - Rationale: Guarantees displacement only when Dodge is accepted and in valid timeline.
   - Alternative rejected: trigger displacement from input event alone (can desync on rejection).

3. **Use dedicated dodge tuning profile in locomotion settings**
   - Rationale: `MoveSpeed` alone is insufficient for dodge readability and temporal shaping.
   - Alternative rejected: overload normal movement speed multipliers during dodge.

4. **Retain debug/evidence hooks under existing logging rules**
   - Rationale: verification depends on concrete displacement proof; logging remains wrapper-based and define-gated where noisy.

## Risks / Trade-offs

- **[Risk] Double-application of displacement during repeated snapshots**
  → Mitigation: edge-trigger on state transition or one-shot latch per dodge cycle.

- **[Risk] Direction ambiguity (input, facing, camera basis) causes inconsistent feel**
  → Mitigation: define single direction policy for M0 and document it in specs/tests.

- **[Risk] Regression to existing movement/recovery restrictions**
  → Mitigation: add focused smoke scenarios for dodge during neutral vs recovery and verify rejection/acceptance behavior remains correct.

- **[Risk] Over-noisy logs in PlayMode**
  → Mitigation: keep transition-level logging only; gate verbose diagnostics with project defines.

## Migration Plan

1. Add spec-driven requirements for dodge displacement behavior and evidence.
2. Implement locomotion API/settings additions and bridge logic in M0 tick path.
3. Run focused EditMode/PlayMode verification for:
   - Dodge accepted displacement visible.
   - No displacement on rejected dodge.
   - No regressions to lock-on and defensive flow.
4. Update evidence artifacts with transform before/after and state/log proof.

Rollback strategy:
- Revert change set for locomotion displacement bridge/profile and return to prior state-only dodge behavior if integration causes instability.

## Open Questions

- Direction source for M0 dodge displacement priority:
  1) move input vector, 2) current facing, or 3) camera-relative fallback?
- Should displacement shaping be constant-speed or eased over dodge active window for first implementation?
- Minimum acceptable displacement magnitude for “readable dodge” in current arena scale.
