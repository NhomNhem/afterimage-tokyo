# Sprint 4 — 2026-06-27 to 2026-07-10

**Status**: Planned
**Review Mode**: lean
**QA Plan**: `production/qa/qa-plan-sprint-4-2026-06-05.md`
**Producer Gate**: skipped — Lean mode

> **QA Ready**: Sprint 4 now has a QA plan. Create the S4 story docs before `/story-readiness` or implementation so story-level QA cases can be back-filled cleanly.

## Sprint Goal

Harden the M1 exploration-memory loop by adding the runtime memory log placeholder, producing fresh Unity test evidence, and cleaning the first ADR-guided orchestration slice without expanding gameplay truth ownership.

## Capacity

- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days

## Tasks

### Must Have (Critical Path)

| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|----------:|--------------|-------------------|
| S4-1 | [QA] Fresh Sprint 3/Sprint 4 Unity Test Runner Evidence | qa-lead | 0.5 | S3-6 | Fresh EditMode/PlayMode artifact is captured or the tooling blocker is classified with a fallback verification path. |
| S4-2 | [UI] Runtime Memory Log Placeholder | ui-programmer | 1.0 | S3-2, S3-3 | Revealed/collected fragment entry appears in a minimal read-only runtime log without owning memory truth. |
| S4-3 | [QA] Runtime Memory Log Smoke | qa-lead | 0.5 | S4-2 | Prompt -> Interact -> Reveal feedback -> Runtime log is verified with PASS/PARTIAL/FAIL evidence. |
| S4-4 | [Producer] Decide S3-5 Carryover Closure | producer/lead | 0.25 | S4-2, S4-3 | Sprint 3 carryover is closed, absorbed into Sprint 4, or explicitly descoped before Sprint 4 close-out. |

### Should Have

| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|----------:|--------------|-------------------|
| S4-5 | [Architecture] Extract M0 Gameplay Tick Memory Bridge Proposal Review | lead-programmer | 0.5 | ADR-0001 | OpenSpec `extract-m0-gameplay-tick-memory-bridge` is reviewed and either approved for implementation or deferred. |
| S4-6 | [Refactor] Implement MemoryInteractionTickBridge Thin Slice | gameplay-programmer | 1.0 | S4-5 | Behavior-preserving extraction only; no CombatCore, Input, or MemoryState truth changes. |

### Nice to Have

| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|----------:|--------------|-------------------|
| S4-7 | [Debug] MemoryRaycastProProbe Alignment Spike | gameplay/debug | 0.5 | S4-2 | Debug probe aligns with `MemoryInteractionService` eligibility or is formally deprecated as non-truth debug evidence. |

## Carryover from Previous Sprint

| Task | Reason | New Estimate |
|------|--------|-------------:|
| S3-5 Runtime Memory Log Placeholder | Should-have story was outside Sprint 3 must-have smoke gate and remained not started. | 1.0d |
| Fresh Unity Test Runner artifact | Sprint 3 QA sign-off condition retained this as close-out hygiene. | 0.5d |

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Runtime log drifts into full journal/progression UI | Medium | High | Keep S4-2 placeholder-only and read-only; no save/profile/progression behavior. |
| Memory bridge extraction changes orchestration order | Medium | High | Require focused regression tests and keep extraction behavior-preserving. |
| Unity Test Runner blocked by open Editor or tooling | Medium | Medium | Capture blocker explicitly and use compile smoke/manual fallback only with clear warning. |
| S4 scope becomes mixed implementation plus architecture cleanup | Medium | Medium | Treat S4-5/S4-6 as should-have after runtime log and QA evidence are stable. |

## Dependencies on External Factors

- Unity 6000.3.x editor/runtime stability
- Unity Test Runner availability
- Existing M1 fragment scene/bootstrap wiring
- Existing UI Toolkit debug overlay/runtime UI path

## Architecture Constraints

- Input owns raw Interact intent only.
- `MemoryInteractionService` owns interaction orchestration.
- `MemoryState` owns reveal/collect truth.
- Runtime memory log must remain read-only presentation/read-model.
- UI/VFX/Audio/Animancer remain downstream presentation-only.
- CombatCore, EnemyIntent, TargetContext, Camera, and PlayerLocomotion gameplay truth remain unchanged.
- No service locator, `FindObjectOfType`, `Resources.Load`, or direct Unity debug logging.
- No broad Nhem DI migration.

## Definition of Done for This Sprint

- [ ] All Must Have tasks completed
- [ ] QA plan exists for Sprint 4
- [ ] Fresh Unity Test Runner artifact captured or blocker classified
- [ ] Runtime memory log remains read-only and placeholder-scoped
- [ ] Smoke report exists
- [ ] QA sign-off report is APPROVED or APPROVED WITH CONDITIONS
- [ ] No S1/S2 bugs in delivered features
- [ ] Design/evidence documents updated for deviations and deferred optional work

## Recommended First Story

`S4-1 — [QA] Fresh Sprint 3/Sprint 4 Unity Test Runner Evidence`

Reason: it clears the main Sprint 3 QA condition before new implementation adds noise.
