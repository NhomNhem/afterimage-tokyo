# Story S8-5: [QA] Player Animation Polish Smoke

> **Sprint**: Sprint 8
> **Status**: Not Started
> **Layer**: QA / Integration
> **Type**: Visual/Feel
> **Estimate**: 0.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-16

## Context

**Sprint Plan**: `production/sprints/sprint-8.md`
**Epic**: M0 First Playable Duel — player animation polish pass
**QA Plan**: `production/qa/qa-plan-sprint-8.md`
**Requirement**: Sprint 8 QA gate for animation polish stories S8-1 through S8-4.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW
**Engine Notes**: Manual PlayMode smoke only. No runtime code changes.

---

## Goal

Confirm that all four animation polish areas (attack, dodge, parry/counter, hit reaction) read clearly in Game View together, with no S1/S2 regressions and no presentation-boundary violations.

---

## Acceptance Criteria

- [ ] Attack windup and recovery phases are readable in a live duel.
- [ ] Dodge start → active → end phases are readable in a live duel.
- [ ] Parry and counter animations are visually distinct from each other and from dodge.
- [ ] Hit reaction blends cleanly from any interrupted state.
- [ ] No S1/S2 regressions in startup, duel loop, health/combat contract, lock-on, or debug overlay readability.
- [ ] Console output classified — no new blocking errors from animation changes.
- [ ] Evidence records PASS/PARTIAL/FAIL table for all four animation areas.

---

## Out of Scope

- New animation feature work.
- Combat Core, Health, Locomotion, or TargetContext truth changes.
- Enemy animation changes.

---

## QA Test Cases

- **AC-1 through AC-4**: Manual duel smoke.
  - Setup: Load M0 duel scene, play through attack, dodge, parry, counter, take damage.
  - Verify: All four animation areas read as described in S8-1 through S8-4 evidence.
  - Pass condition: Tester can describe all four animation states without prompting.

- **AC-5**: No regressions.
  - Setup: Run full EditMode suite.
  - Verify: All tests pass.
  - Pass condition: EditMode PASS, no new failures.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- `production/qa/evidence/s8-5-animation-polish-smoke.md`
- PASS/PARTIAL/FAIL table for all four animation areas.
- EditMode test suite run result.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: S8-1, S8-2, S8-3, S8-4 all complete
- Unlocks: Sprint 8 QA sign-off
