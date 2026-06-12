# Sprint 5 — 2026-06-23 to 2026-07-04

**Status**: Planned
**Review Mode**: lean
**QA Plan**: TBD — run `/qa-plan sprint` before implementation begins
**Producer Gate**: skipped — Lean mode

## Sprint Goal

Close out Sprint 4 with QA sign-off, address high-priority M0 tech debt (dodge displacement wiring), and prepare M1 exploration-memory loop for polish phase.

## Capacity

- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days

## Tasks

### Must Have (Critical Path)

| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|----------:|--------------|-------------------|
| S5-1 | [QA] Sprint 4 Smoke Check | qa-lead | 0.5 | S4 Must-Have Complete | Critical path verified end-to-end; PASS/PARTIAL/FAIL report produced |
| S5-2 | [QA] Sprint 4 QA Sign-Off | qa-team | 1.0 | S5-1 | Full QA cycle executed; sign-off report: APPROVED or APPROVED WITH CONDITIONS |
| S5-3 | [Retrospective] Sprint 4 Retrospective | producer | 0.5 | S5-2 | What went well, what didn't, action items for Sprint 5 documented |
| S5-4 | [Feature] Wire M0 Dodge Displacement | gameplay-programmer | 2.0 | None | Combat Core Dodge state triggers Player Locomotion dodge displacement; manual PlayMode verification confirms dodge lunge |

### Should Have

| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|----------:|--------------|-------------------|
| S5-5 | [Architecture] Harden Health-Combat Contract | gameplay-programmer | 1.0 | None | Replace string-based resolved-combat gating with typed contract in `M0HealthDamageReactionModel` |
| S5-6 | [Design Decision] LockOn Toggle Policy | game-designer | 0.5 | None | Explicit decision: acquire-only/maintain focus vs toggle acquire/release; documented in GDD or decision log |
| S5-7 | [Debug] MemoryRaycastProbe Alignment or Deprecation | gameplay/debug | 0.5 | S4-2 | Debug probe aligns with `MemoryInteractionService` eligibility or is formally deprecated |

### Nice to Have

| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|----------:|--------------|-------------------|
| S5-8 | [Visual Polish] Parry/Counter Visual Feedback | technical-artist | 1.0 | None | Capture/polish direct visual feedback for Parry and Counter (PARTIAL → COMPLETE) |
| S5-9 | [Dependency] Resolve HDRP Material Enum Error | engine-programmer | 0.5 | None | Migrate HDRP TransparentCullMode to URP-compatible drawer/dependency |

## Carryover from Previous Sprint

| Task | Reason | New Estimate |
|------|--------|-------------:|
| S4-5 Architecture Review | Should-have; remained backlog | 0.5d |
| S4-7 MemoryRaycastProbe Alignment | Nice-to-have; remained backlog | 0.5d |

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Dodge displacement wiring changes locomotion contract | Medium | High | Keep change behavior-preserving; regression test M0 combat flow |
| QA sign-off finds S1/S2 bugs | Medium | High | Run smoke check first; triage before sign-off begins |
| Tech debt stories expand scope | Medium | Medium | Keep stories narrow; defer follow-ups to backlog |
| Sprint 4 close-out takes longer than estimated | Low | Medium | Prioritize S5-1/S5-2/S5-3 as must-have; defer tech debt if needed |

## Dependencies on External Factors

- Unity 6000.3.x editor/runtime stability
- Sprint 4 must-have stories completed (4/4 done, S4-3 manually confirmed)
- No blocking S1/S2 bugs discovered during Sprint 4 smoke/QA

## Architecture Constraints

- Dodge displacement must not change Combat Core Dodge state authority
- Player Locomotion remains movement truth owner
- No service locator, `FindObjectOfType`, `Resources.Load`, or direct Unity debug logging
- Tech debt fixes must not introduce new scope or expand gameplay systems

## Definition of Done for This Sprint

- [ ] All Must Have tasks completed
- [ ] QA plan exists for Sprint 5
- [ ] Sprint 4 smoke check: PASS
- [ ] Sprint 4 QA sign-off: APPROVED or APPROVED WITH CONDITIONS
- [ ] Sprint 4 retrospective completed
- [ ] Dodge displacement wiring verified via manual PlayMode
- [ ] All Logic/Integration stories have passing unit/integration tests
- [ ] Smoke report exists for Sprint 5 (`/smoke-check sprint`)
- [ ] QA sign-off report for Sprint 5: APPROVED or APPROVED WITH CONDITIONS
- [ ] No S1/S2 bugs in delivered features
- [ ] Design documents updated for any deviations
- [ ] Code reviewed and merged

## Recommended First Story

`S5-1 — [QA] Sprint 4 Smoke Check`

Reason: Sprint 4 must-have closure requires smoke check before QA sign-off can begin.
