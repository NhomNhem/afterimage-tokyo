# Sprint 6 - 2026-07-07 to 2026-07-18

## Sprint Goal
Make the stable M0 combat foundation easier to read by polishing parry/counter feedback while closing Sprint 5 metadata and console-hygiene carryover.

## Capacity
- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days
- Planned scope: 4 days
- Review mode: lean

## QA Plan
QA Plan: `production/qa/qa-plan-sprint-6-2026-06-12.md`

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|--------------|---------------------|
| S6-1 | Reconcile Sprint 5 Metadata and QA Artifacts | Producer / Codex | 0.5 | Sprint 5 QA, retro, gate check | `production/sprints/sprint-5.md` reflects final smoke, QA, retro, and deferred S5-8/S5-9 decisions; no runtime changes. |
| S6-2 | Parry/Counter Visual Feedback Polish | Gameplay / Presentation | 1.5 | S5-4, S5-5, S5-6 | Parry and counter feedback are visually distinct, timing follows confirmed Combat Core state, presentation remains non-authoritative, and evidence is captured. |
| S6-3 | Parry/Counter Feedback Smoke Evidence | QA | 0.5 | S6-2 | Focused M0 duel smoke confirms testers can identify parry success, counter availability, and counter result without new S1/S2 regressions. |

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|--------------|---------------------|
| S6-4 | Resolve HDRP Material Enum Error | Engine / Tools | 0.5 | None | Owned references are classified or migrated, console noise is reduced, and no gameplay or material authoring behavior regresses. |
| S6-5 | Standardize Retrospective Debt Marker Baseline | Production / Tools | 0.5 | Sprint 5 retro | TODO/FIXME/HACK counting paths and exclusions are documented with a repeatable command so future retros compare the same baseline. |
| S6-6 | Add Artifact-Based Fallback Notes to QA/Retro Workflows | Production / Process | 0.5 | Sprint 5 retro | Workflow docs or skill notes state the fallback path when Task/AskUserQuestion style helpers are unavailable; QA/retro outputs remain auditable. |

### Nice to Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|--------------|---------------------|
| S6-7 | Select Next M0/M1 Feel Slice | Design / Tech Lead | 0.5 | Sprint 6 smoke context | Decision recorded for the next slice among lock-on readability, enemy telegraph clarity, counter/reveal feedback, or M1 memory feedback polish. |

## Carryover from Previous Sprint
| Task | Reason | New Estimate |
|------|--------|--------------|
| S5-8 Parry/Counter Visual Feedback | Deferred as nice-to-have after Sprint 5 must/should work closed; now directly supports M0 feel/readability. | 1.5 days |
| S5-9 Resolve HDRP Material Enum Error | Deferred because it was console hygiene, not a Sprint 5 close-out blocker. | 0.5 days |
| Sprint 5 plan/status reconciliation | Gate passed with concerns because `sprint-5.md` lagged behind final QA/smoke/retro artifacts. | 0.5 days |

## Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Visual feedback becomes too noisy and hurts duel readability | Medium | High | Keep feedback restrained, tied only to confirmed combat state, and validate in manual Game View smoke. |
| HDRP enum cleanup expands into broad render pipeline migration | Low | Medium | Limit S6-4 to owned references and evidence; defer vendor/package or broad migration work. |
| Process cleanup competes with gameplay polish | Medium | Medium | Keep S6-5 and S6-6 as Should Have; cut them before touching S6-2/S6-3. |
| Starting implementation before QA plan exists weakens acceptance criteria | Medium | High | Run `/qa-plan sprint` before `/dev-story` work. |

## Dependencies on External Factors
- Unity 6000.3.x project environment remains available.
- Unity MCP remains available for EditMode/PlayMode validation.
- Current M0 duel scene and combat runtime composition remain stable after Sprint 5.
- Existing parry/counter hooks expose enough confirmed state for presentation-only feedback.

## Definition of Done for this Sprint
- [ ] All Must Have tasks completed
- [ ] All tasks pass acceptance criteria
- [ ] QA plan exists (`production/qa/qa-plan-sprint-6-2026-06-12.md`)
- [ ] All Logic/Integration stories have passing unit/integration tests where applicable
- [ ] Smoke check passed (`/smoke-check sprint`)
- [ ] QA sign-off report: APPROVED or APPROVED WITH CONDITIONS (`/team-qa sprint`)
- [ ] No S1 or S2 bugs in delivered features
- [ ] Design documents updated for any deviations
- [ ] Code reviewed and merged

## Scope Check
If this sprint includes stories added beyond the original epic scope, run `/scope-check [epic]` before implementation begins.
