# Sprint 9 — Combat Camera & Final M0 Polish

## Sprint Goal
Wire Genshin-style combat camera, add enemy hit reactions, close M1 carryover — so M0 duel feels frame-ready from any camera angle.

## Capacity
- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days
- Planned scope: 6.5 days
- Review mode: lean

## QA Plan
QA Plan: `production/qa/qa-plan-sprint-9-2026-06-21.md`

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S9-1 | Commit & Stabilize Sprint 8 Work | Dev | 0.5 | — | Uncommitted fixes committed; EditMode 281/281; smoke re-run PASS. |
| S9-2 | Combat Camera Integration | Dev | 2.0 | S9-1 | Orbit camera follows lock-on target; spring arm smooths transitions; FOV adjusts during dodge/sprint; no camera snap between states; IM0CameraTargetProvider already wired. |
| S9-3 | Enemy Hit Reaction Animation | Dev | 1.0 | S9-1 | Enemy visibly reacts to ConfirmedHit via Hit1/Hit2 clips; reaction distinct from idle and telegraph; no EnemyIntent truth changes. |
| S8-6 | M1 Epic Closure | Docs | 0.5 | — | All M1 stories reviewed for status; closure decision documented; remaining gaps surfaced. |

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S9-4 | EditMode Tests: HasTargetFocus + SetStrafeMode | Dev | 1.0 | S9-1 | Tests cover lock-on → HasTargetFocus=true → isCombatMode; SetStrafeMode toggles facing target; dodge facing unchanged during displacement. |
| S9-5 | Enemy Telegraph Readability Polish | Dev | 1.0 | S9-3 | Telegraph color/shape visually distinct from idle; active phase distinct from recovery; no Combat Core timing changes; debug overlay shows intent state. |

### Nice to Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S9-6 | Assign Turn Clips | Dev | 0.5 | S9-1 | Sp_TurnL, Sp_TurnR, Turn180 assigned in M0PlayerAnimationSet.asset; 130°+ pivot plays turn animation; movement lock releases cleanly. |

## Carryover from Previous Sprint
| Task | Reason | New Estimate |
|------|--------|-------------|
| S8-6 M1 Epic Closure | Should-have not started in Sprints 7 and 8; M1 memory epic remains formally open. Formally close or descope. | 0.5 days |

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Camera refactor breaks existing framing | Medium | High | Camera DI already set up (`IM0CameraTargetProvider`, `M0CombatCameraService`); S9-2 wires existing service, not rebuild. |
| Enemy hit reaction needs new clips | Low | Medium | School_Katana_Girl has Hit1/Hit2 in Normal folder; reuse player HitReactionAnimationRequest pattern. |
| S8-6 deferred a third time | Medium | Low | Should-have; formally descope if not started by mid-sprint. |
| Camera feels wrong at first try | Medium | Medium | Iterate spring arm / FOV values as tuning knobs; manual Game View verification per story. |

## Dependencies on External Factors
- Unity 6000.3.x + URP project environment remains available.
- `IM0CameraTargetProvider` + `M0CombatCameraService` already exist from prior camera refactor work.
- School_Katana_Girl Hit1/Hit2 clips are available in `Animations/Normal/`.
- M0 duel scene and combat runtime stable after Sprint 8.

## Action Items from Sprint 8 Retro
| # | Action | Sprint 9 Story |
|---|--------|---------------|
| 1 | Commit all uncommitted Sprint 8 work | S9-1 |
| 2 | Close S8-6 M1 Epic Closure or formally descope | S8-6 |
| 3 | Assign turn clips (Sp_TurnL/R, Turn180) | S9-6 |
| 4 | Add EditMode tests for HasTargetFocus and SetStrafeMode | S9-4 |

## Definition of Done for this Sprint
- [ ] All Must Have tasks completed
- [ ] All tasks pass acceptance criteria
- [ ] QA plan exists (`production/qa/qa-plan-sprint-9.md`)
- [ ] Smoke check passed (`/smoke-check sprint`)
- [ ] QA sign-off report: APPROVED or APPROVED WITH CONDITIONS (`/team-qa sprint`)
- [ ] No S1 or S2 bugs in delivered features
- [ ] M0 duel readable with combat camera active — tester can explain enemy intent, defense, counter, reveal from Game View
- [ ] Code reviewed and merged

## Scope Check
Sprint 9 completes the remaining M0 readability gaps after Sprint 8's animation polish: camera framing (S9-2) and enemy feedback (S9-3/5). S8-6 (M1 closure) and S9-4/6 (tests/turn clips) close technical debt. No new systems introduced beyond what M0 needs to prove the duel loop.
