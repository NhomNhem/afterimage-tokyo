# Story S6-3: Parry/Counter Feedback Smoke Evidence

> **Sprint**: Sprint 6
> **Status**: Ready
> **Layer**: QA
> **Type**: Visual/Feel
> **Estimate**: 0.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

**Sprint Plan**: `production/sprints/sprint-6.md`
**QA Plan**: `production/qa/qa-plan-sprint-6-2026-06-12.md`
**Requirement**: Sprint 6 S6-3

**GDD**: `design/gdd/systems-index.md` - M0 duel readability and combat loop.
**ADR Governing Implementation**: N/A - QA evidence story; validates control manifest rules rather than implementing architecture.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW
**Engine Notes**: Requires Unity MCP or Unity Test Runner plus manual Game View verification.

**Control Manifest Rules**:
- Required: Smoke must guard gameplay composition, presentation readability, and no S1/S2 regressions.
- Forbidden: QA evidence must not modify gameplay truth to make the test pass.
- Guardrail: Manual evidence must be specific enough for later review.

---

## Acceptance Criteria

- [ ] Full EditMode suite passes.
- [ ] Full PlayMode suite passes.
- [ ] Manual Game View smoke confirms player can identify parry success.
- [ ] Manual Game View smoke confirms player can identify when a counter is available.
- [ ] Manual Game View smoke confirms player can identify the counter result.
- [ ] No S1/S2 regressions are observed in startup, duel loop, dodge, health/combat contract, lock-on policy, or debug overlay readability.
- [ ] Evidence is captured before `/team-qa sprint`.

---

## Implementation Notes

- Run after S6-2 implementation lands.
- Use existing Sprint 5 smoke structure as the reference format.
- Capture Unity test job IDs/results if Unity MCP is used.
- Manual Game View evidence can be written notes, screenshots, or video references.

---

## Out of Scope

- Fixing defects discovered by the smoke run unless they are trivial documentation corrections.
- Changing S6-2 feedback implementation.
- Broad performance profiling beyond smoke-level observations.

---

## QA Test Cases

- **AC-1**: Full EditMode suite passes.
  - Setup: Run full EditMode tests through Unity MCP or Unity Test Runner.
  - Verify: Test result reports 0 failures.
  - Pass condition: Job/result ID or captured output is recorded in evidence.

- **AC-2**: Full PlayMode suite passes.
  - Setup: Run full PlayMode tests through Unity MCP or Unity Test Runner.
  - Verify: Test result reports 0 failures.
  - Pass condition: Job/result ID or captured output is recorded in evidence.

- **AC-3**: Manual Game View confirms feedback readability.
  - Setup: Play the M0 duel and perform repeated defensive attempts.
  - Verify: Parry success, counter availability, and counter result can each be identified.
  - Pass condition: Evidence notes identify all three moments and any ambiguity.

- **AC-4**: No S1/S2 regressions.
  - Setup: Review console and smoke notes after automated/manual runs.
  - Verify: No startup, composition, null reference, or critical gameplay regressions appear.
  - Pass condition: Evidence states no S1/S2 regressions or lists blockers.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- `production/qa/smoke-YYYY-MM-DD.md` or `production/qa/evidence/s6-3-parry-counter-feedback-smoke-evidence.md`
- Unity EditMode and PlayMode results.
- Manual Game View readability notes.

**Status**: [x] Created at `production/qa/evidence/s6-3-parry-counter-feedback-smoke-evidence.md`; manual Game View smoke pending reviewer confirmation.

---

## Dependencies

- Depends on: S6-2 complete or ready for QA.
- Unlocks: Sprint 6 QA hand-off.
