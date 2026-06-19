# Sprint 7 — 2026-07-21 to 2026-08-01

## Sprint Goal
Close M1 memory exploration and clear process debt while deciding the next feel slice for afterimage-tokyo.

## Capacity
- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days
- Estimated scope: 3 days
- Review mode: lean

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S7-1 | Select Next M0/M1 Feel Slice | Design / Tech Lead | 0.5 | Sprint 6 smoke context | Decision recorded for the next slice among lock-on readability, enemy telegraph clarity, counter/reveal feedback, or M1 memory feedback polish. |
| S7-2 | M1 Runtime Memory Log Smoke | QA | 0.5 | S4-2 (Complete) | Smoke pass confirms the tester-facing path (Prompt → Interact → Reveal feedback → Runtime memory log) reads correctly with no S1/S2 regressions. Evidence captured. Story file: `production/epics/m1-memory-fragment-exploration/story-s4-3-runtime-memory-log-smoke.md` (Ready). |
| S7-3 | Resolve HDRP Material Enum Error | Engine / Tools | 0.5 | None | Owned references are classified or migrated, console noise is reduced, and no gameplay or material authoring behavior regresses. |

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S7-4 | M0 Gameplay Tick Memory Bridge Review | Architecture / Review | 0.5 | ADR-0001 | OpenSpec change for extracting memory-related tick orchestration is narrow, behavior-preserving, and aligned with ADR-0001. Story file: `production/epics/m1-memory-fragment-exploration/story-s4-5-extract-m0-gameplay-tick-memory-bridge-proposal-review.md` (Not Started). |
| S7-5 | Standardize Retrospective Debt Marker Baseline | Production / Tools | 0.5 | None | TODO/FIXME/HACK counting paths and exclusions are documented with a repeatable command so future retros compare the same baseline. |
| S7-6 | Add Artifact-Based Fallback Notes to QA/Retro Workflows | Production / Process | 0.5 | None | Workflow docs or skill notes state the fallback path when Task/AskUserQuestion style helpers are unavailable; QA/retro outputs remain auditable. |

### Nice to Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S7-7 | M1 Epic Closure Review | QA / Docs | 0.5 | S7-1, S7-2 | All M1 epic stories reviewed for completion status; closure decision documented in epic; remaining gaps surfaced. |

## Carryover from Previous Sprint
| Task | Reason | New Estimate |
|------|--------|-------------|
| S6-4 → S7-3 Resolve HDRP Material Enum Error | Not started — deferred from Sprint 6 should-have. | 0.5 days |
| S6-5 → S7-5 Debt Marker Baseline | Not started — deferred from Sprint 6 should-have. | 0.5 days |
| S6-6 → S7-6 Fallback Notes | Not started — deferred from Sprint 6 should-have. | 0.5 days |
| S6-7 → S7-1 Select Next Feel Slice | Not started — deferred from Sprint 6 nice-to-have; promoted to must-have for Sprint 7. | 0.5 days |
| S4-3 → S7-2 M1 Runtime Memory Log Smoke | Ready but never pulled into Sprint 6. | 0.5 days |
| S4-5 → S7-4 M0 Gameplay Tick Memory Bridge Review | Not started — architecture review deferred. | 0.5 days |

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| S7-1 decision delays rest of sprint | Low | High | Keep 0.5d hard cap; defer to separate design session if decision needs more time. |
| HDRP enum cleanup expands into broad render pipeline migration | Low | Medium | Limit S7-3 to owned references and evidence; defer vendor/package or broad migration work. |
| Process cleanup competes with finishing M1 | Medium | Low | Keep S7-5 and S7-6 as Should Have; cut them before touching S7-1/S7-2. |
| M1 epic has hidden gaps after closure review | Low | Medium | S7-7 surfaces gaps as data, not as a blocker; gaps inform the next feel slice decision. |

## Dependencies on External Factors
- Unity 6000.3.x project environment remains available.
- Unity MCP remains available for EditMode/PlayMode validation.
- Current M0 duel scene and combat runtime composition remain stable after Sprint 6.
- M1 memory interaction prototype is already implemented and smoke-ready (S4-3 is Ready).
- `production/epics/m1-memory-fragment-exploration/story-s4-3-runtime-memory-log-smoke.md` is the Ready story targeting S7-2.
- `production/epics/m1-memory-fragment-exploration/story-s4-5-extract-m0-gameplay-tick-memory-bridge-proposal-review.md` is the Not Started story targeting S7-4.

## Definition of Done for this Sprint
- [ ] All Must Have tasks completed
- [ ] All tasks pass acceptance criteria
- [ ] QA plan exists (`production/qa/qa-plan-sprint-7.md`)
- [ ] All Logic/Integration stories have passing unit/integration tests where applicable
- [ ] Smoke check passed (`/smoke-check sprint`)
- [ ] QA sign-off report: APPROVED or APPROVED WITH CONDITIONS (`/team-qa sprint`)
- [ ] No S1 or S2 bugs in delivered features
- [ ] Design documents updated for any deviations
- [ ] Code reviewed and merged

## Scope Check
If this sprint includes stories added beyond the original epic scope, run `/scope-check [epic]` before implementation begins.
