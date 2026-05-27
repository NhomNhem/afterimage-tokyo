# Sprint 2 — 2026-05-30 to 2026-06-12

**Status**: Planned
**Review Mode**: lean
**QA Plan**: `production/qa/qa-plan-sprint-2-2026-05-26.md`
**Producer Gate**: skipped — Lean mode

## Sprint Goal

Turn the verified M0 technical duel skeleton into a more readable and playable first playable duel prototype without expanding scope into full RPG systems.

## Capacity

- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days

## Story Classification Summary

| ID | Story | Type | Priority | Est. Days | Owner | Dependencies |
|----|-------|------|----------|-----------|-------|--------------|
| S2-1 | [Review] M0 Sprint 1 Playable Duel Closure Review | Integration | must-have | 0.5 | qa-lead | None |
| S2-2 | [Combat Feel] Attack / Dodge / Parry Readability Tuning | Visual/Feel | must-have | 1.5 | gameplay-programmer | S1-4, S1-5, S1-6, S1-11 |
| S2-3 | [Enemy] Telegraph Readability Pass | Visual/Feel | must-have | 1.0 | ai-programmer | S1-5, S1-11 |
| S2-4 | [Camera] Lock-On Combat Camera Readability Pass | Visual/Feel | must-have | 1.0 | lead-programmer | S1-1, S1-3, S1-11 |
| S2-5 | [QA] M0 Playable Duel Smoke Test Checklist | Integration | must-have | 0.5 | qa-lead | S2-1 |
| S2-6 | [Animation] Placeholder Clip Assignment and Timing Readability | Visual/Feel | should-have | 0.5 | art-director | S1-11 |
| S2-7 | [Memory] Reveal VFX Readability Pass | Visual/Feel | should-have | 0.5 | vfx-programmer | S1-10 |
| S2-8 | [Audio/VFX] Combat Feedback Placeholder Pass | Visual/Feel | should-have | 0.5 | sound-designer | S1-4, S1-6, S1-10 |
| S2-9 | [Tech Debt] External Material/HDRP Enum Error Classification or Fix | Config/Data | could-have | 0.5 | technical-artist | None |
| S2-10 | [Presentation] Debug Overlay Polish | UI | could-have | 0.5 | ui-programmer | S1-9 |

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S2-1 | [Review] M0 Sprint 1 Playable Duel Closure Review | qa-lead | 0.5 | None | Sprint 1 closure is summarized, verified-with-notes items are explicit, and Sprint 2 follow-ups are de-risked. |
| S2-2 | [Combat Feel] Attack / Dodge / Parry Readability Tuning | gameplay-programmer | 1.5 | S1-4, S1-5, S1-6, S1-11 | Attack, dodge, and parry beats are easier to read without moving gameplay truth into Animator/VFX. |
| S2-3 | [Enemy] Telegraph Readability Pass | ai-programmer | 1.0 | S1-5, S1-11 | Enemy intent cues are visibly distinct before commit/active/recovery. |
| S2-4 | [Camera] Lock-On Combat Camera Readability Pass | lead-programmer | 1.0 | S1-1, S1-3, S1-11 | Lock-on camera keeps both combatants readable and does not own combat truth. |
| S2-5 | [QA] M0 Playable Duel Smoke Test Checklist | qa-lead | 0.5 | S2-1 | Smoke checklist covers launch, duel loop, warning-only missing clips, and animator-disabled movement. |

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S2-6 | [Animation] Placeholder Clip Assignment and Timing Readability | art-director | 0.5 | S1-11 | Placeholder clips improve timing readability while remaining presentation-only. |
| S2-7 | [Memory] Reveal VFX Readability Pass | vfx-programmer | 0.5 | S1-10 | Reveal beat stays restrained and readable without obscuring enemy intent. |
| S2-8 | [Audio/VFX] Combat Feedback Placeholder Pass | sound-designer | 0.5 | S1-4, S1-6, S1-10 | Placeholder audio/VFX cues reinforce combat outcomes without adding authority. |

### Nice to Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S2-9 | [Tech Debt] External Material/HDRP Enum Error Classification or Fix | technical-artist | 0.5 | None | External editor/material error is classified or fixed without touching M0 gameplay truth. |
| S2-10 | [Presentation] Debug Overlay Polish | ui-programmer | 0.5 | S1-9 | Debug overlay remains read-only and becomes easier to scan during PlayMode. |

## Carryover from Previous Sprint

| Task | Reason | New Estimate |
|------|--------|-------------|
| `m0-visual-polish-followups` | Sprint 1 passed with notes, but full clip visual alignment and readability still need work. | 0.5d |
| `m0-dodge-displacement-wiring` | Dodge feel/readability still needs refinement even though core wiring is verified. | folded into S2-2 |
| `rendering-material-hdrp-enum-error` | External editor/material issue remains tracked separately. | 0.5d |

## Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Readability tuning drifts into gameplay truth changes | Medium | High | Keep CombatCore, PlayerLocomotion, EnemyIntent, and MemoryState as the only truth owners. |
| Animation polish expands into production clip work | Medium | Medium | Limit to placeholder clip assignment and timing readability. |
| Camera polish starts driving combat outcomes | Low | High | Camera remains framing/readability only; no state ownership. |
| External material/HDRP issue distracts from sprint goal | Medium | Low | Treat as contained tech debt unless it blocks editor/runtime stability. |
| Manual QA scope becomes vague | Medium | Medium | Use the Sprint 2 QA plan and smoke checklist before implementation. |

## Dependencies on External Factors

- Unity 6000.3.x editor/runtime stability
- Existing M0 placeholder assets and scene wiring
- QA plan sign-off before implementation begins

## Explicit Non-Goals

- Full RPG systems
- Inventory / loot / equipment
- Save / load / progression
- Full narrative / lore implementation
- Full map system
- Boss system
- New enemy roster
- Production animation polish
- Full audio pipeline
- Gameplay truth in Animator, VFX, Camera, UI, Input, or Debug Overlay

## Definition of Done for This Sprint

- [ ] All Must Have tasks completed
- [ ] All tasks pass acceptance criteria
- [ ] QA plan exists (`production/qa/qa-plan-sprint-2-2026-05-26.md`)
- [ ] All Logic/Integration stories have passing unit/integration tests
- [ ] Smoke check passed (`/smoke-check sprint`)
- [ ] QA sign-off report: APPROVED or APPROVED WITH CONDITIONS (`/team-qa sprint`)
- [ ] No S1 or S2 bugs in delivered features
- [ ] Design documents updated for any deviations
- [ ] Code reviewed and merged

## Recommended First Story

`[Review] M0 Sprint 1 Playable Duel Closure Review`

It de-risks Sprint 2 by turning verified-with-notes work into a concrete gap list before tuning begins.

## Suggested OpenSpec Changes

- No new OpenSpec change is required to start Sprint 2.
- If the closure review exposes a gap in camera, readability, or asset classification ownership, open a small follow-up change rather than widening Sprint 2.
