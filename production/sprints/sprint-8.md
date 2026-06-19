# Sprint 8 — 2026-08-04 to 2026-08-15

## Sprint Goal
Polish player animation readability across the M0 duel loop — attack windup/recovery, dodge phase distinction, parry/counter transition clarity, and hit reaction blending — so a tester can read their own state without the debug overlay.

## Capacity
- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days
- Planned scope: 7.0 days
- Review mode: lean

## QA Plan
QA Plan: `production/qa/qa-plan-sprint-8-2026-06-16.md`

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S8-7 | Wire School_Katana_Girl into M0 Duel Scene | Presentation / Technical Artist | 1.5 | Story 1-11 | Character visible in duel scene with owned AnimatorController; no Magica Cloth; URP materials clean. |
| S8-1 | Attack Animation Windup and Recovery Clarity | Presentation / Technical Artist | 1.0 | S8-7 | Windup and recovery phases are visually distinct; no Combat Core timing changes. |
| S8-2 | Dodge Animation Phase Distinction | Presentation / Technical Artist | 1.0 | S8-7 | Startup → active → end phases readable in Game View without debug overlay. |
| S8-3 | Parry and Counter Animation Transition Readability | Presentation / Technical Artist | 1.0 | S8-7 | Parry and counter visually distinct; transition readable without debug overlay. |
| S8-4 | Hit Reaction Animation Blending | Presentation / Technical Artist | 0.5 | S8-7 | Hit reaction blends cleanly; communicates damage taken; no Health truth changes. |
| S8-5 | Player Animation Polish Smoke | QA | 0.5 | S8-1, S8-2, S8-3, S8-4 | All four animation areas read in a live duel; no S1/S2 regressions; evidence captured. |

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S8-6 | M1 Epic Closure Review | QA / Docs | 0.5 | S7-1 (Complete) | All M1 stories reviewed for status; closure decision documented; remaining gaps surfaced. |
| S8-8 | Decompose PlayerStateMachine into Layer State Machines | Code / Architecture | 1.0 | None | Single PlayerStateMachine split into CombatStateMachine + LocomotionStateMachine (GroundState) + PlayerStateResolver; IPlayerStateMachine API unchanged; EditMode tests pass. |

### Nice to Have
*(none planned — sprint is already at the readability milestone boundary)*

## Carryover from Previous Sprint
| Task | Reason | New Estimate |
|------|--------|-------------|
| S7-7 → S8-6 M1 Epic Closure Review | Nice-to-have not started in Sprint 7; promoted to Should Have to formally close the M1 epic. | 0.5 days |

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Animation transitions require new clip assets | Low | High | Scope explicitly forbids new assets; use timing/transition tuning only. If new clips are essential, surface as a blocker before implementation. |
| Animator changes accidentally influence gameplay timing | Medium | High | All changes presentation-only; smoke (S8-5) verifies no Combat Core/Health regressions. |
| Animation polish reveals missing animation states | Medium | Medium | Missing states are evidence gaps, not scope expansion; surface them in S8-5 evidence and plan a follow-up story. |
| PlayMode smoke cannot run from CLI | High | Low | S8-5 uses manual Game View observation; document limitation as per established fallback pattern. |
| S8-8 PlayerStateMachine refactor breaks upstream consumers | Low | High | IPlayerStateMachine API is invariant; full EditMode suite + M0PlayerStateMachineDodgeTests as regression gate. |

## Dependencies on External Factors
- Unity 6000.3.x project environment remains available.
- Existing player animation clips are sufficient for transition tuning (no new asset pipeline work required).
- M0 duel scene and combat runtime remain stable after Sprint 7.
- Story 1-11 (Animator Observer Adapters) is in "Verified with notes" state — infrastructure exists, polish is the remaining gap.

## Definition of Done for this Sprint
- [ ] All Must Have tasks completed
- [ ] All tasks pass acceptance criteria
- [ ] QA plan exists (`production/qa/qa-plan-sprint-8.md`)
- [ ] Visual/Feel stories have manual Game View evidence
- [ ] Smoke check passed (`/smoke-check sprint`)
- [ ] QA sign-off report: APPROVED or APPROVED WITH CONDITIONS (`/team-qa sprint`)
- [ ] No S1 or S2 bugs in delivered features
- [ ] Animator changes do not alter Combat Core, Health, Locomotion, or TargetContext truth
- [ ] Code reviewed and merged

## Scope Check
Animation polish is scoped to the four areas identified in S7-1: attack, dodge, parry/counter, hit reaction. S8-8 (PlayerStateMachine decompose) is a parallel architecture story — independent of and a prerequisite for clean animation integration. Any work outside these areas requires explicit approval and a new story before starting.
