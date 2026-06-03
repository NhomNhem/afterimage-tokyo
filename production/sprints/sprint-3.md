# Sprint 3 — 2026-06-13 to 2026-06-26

**Status**: In Progress with Notes
**Review Mode**: lean
**QA Plan**: `production/qa/qa-plan-sprint-3-2026-05-28.md`
**Producer Gate**: skipped — Lean mode

## Sprint Name

Sprint 3 — M1 Memory Fragment Exploration Slice

## Sprint Goal

Deliver a small playable exploration-memory loop where the player explores a Tokyo street area, approaches a Memory Fragment, presses Interact, triggers reveal/collect response, receives placeholder feedback, and sees runtime memory log confirmation.

## Capacity

- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days

## Story Classification Summary

| ID | Story | Type | Priority | Est. Days | Owner | Dependencies | OpenSpec Likely |
|----|-------|------|----------|-----------|-------|--------------|-----------------|
| S3-1 | [Review] M1 Readiness / Scope Review | Integration | must-have | 0.5 | lead-programmer | None | No |
| S3-2 | [Feature] Memory Fragment Interaction Prototype | Integration | must-have | 2.0 | gameplay-programmer | S3-1 | Yes |
| S3-3 | [UI] Interaction Prompt Placeholder | UI | must-have | 1.0 | ui-programmer | S3-2 | Yes |
| S3-4 | [Presentation] Memory Reveal VFX/Audio Placeholder | Visual/Feel | must-have | 1.0 | vfx-programmer | S3-2 | Yes |
| S3-5 | [UI] Runtime Memory Log Placeholder | UI | should-have | 1.0 | ui-programmer | S3-2 | Yes |
| S3-6 | [QA] M1 Exploration-Memory Smoke Test | Integration | must-have | 0.5 | qa-lead | S3-2, S3-3, S3-4 | No |

## Current Progress

**Last Updated**: 2026-06-04

| ID | Status | Evidence / Notes |
|----|--------|------------------|
| S3-1 | Complete | `production/qa/evidence/m1-readiness-review-2026-05-28.md` approved M1 readiness with notes and required a small S3-2 OpenSpec. |
| S3-2 | Complete with Notes | `production/qa/evidence/s3-2-memory-fragment-interaction-verification-2026-05-28.md` records core interaction path PASS WITH NOTES; duplicate second-interact manual capture and `MemoryRaycastProProbe` alignment remain follow-ups. |
| S3-3 | Not Started | Downstream UI prompt placeholder; depends on S3-2. |
| S3-4 | Not Started | Downstream presentation placeholder; depends on S3-2. |
| S3-5 | Not Started | Optional runtime memory log placeholder; depends on S3-2. |
| S3-6 | Not Started | Sprint 3 smoke test remains pending until S3-3/S3-4 are complete. |

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S3-1 | [Review] M1 Readiness / Scope Review | lead-programmer | 0.5 | None | M1 slice scope and boundaries are explicit; non-goals and ownership map are approved for implementation planning. |
| S3-2 | [Feature] Memory Fragment Interaction Prototype | gameplay-programmer | 2.0 | S3-1 | Player can approach fragment, press Interact, and trigger reveal/collect flow through approved ownership boundaries. |
| S3-3 | [UI] Interaction Prompt Placeholder | ui-programmer | 1.0 | S3-2 | Interaction prompt appears/disappears readably based on interaction context without owning interaction truth. |
| S3-4 | [Presentation] Memory Reveal VFX/Audio Placeholder | vfx-programmer | 1.0 | S3-2 | Placeholder reveal feedback plays clearly and remains presentation-only. |
| S3-6 | [QA] M1 Exploration-Memory Smoke Test | qa-lead | 0.5 | S3-2, S3-3, S3-4 | Repeatable smoke checklist verifies the exploration-memory loop and classifies blockers vs external noise. |

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S3-5 | [UI] Runtime Memory Log Placeholder | ui-programmer | 1.0 | S3-2 | Runtime memory log shows collected/revealed fragment entries in a readable placeholder format. |

### Nice to Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| — | — | — | — | — | Keep Sprint 3 focused; no extra Nice-to-Have planned initially. |

## Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Interaction flow drifts into broad systems (inventory/save/quest/dialogue) | Medium | High | Enforce M1 slice boundaries; route expansions to backlog via separate scope decision. |
| Ownership drift into UI/VFX/camera | Medium | High | Keep interaction truth in orchestration/state services; presentation remains downstream only. |
| Placeholder feedback feels unclear | Medium | Medium | Require smoke evidence for readability before closure. |
| Runtime log grows into full journal/progression UI | Medium | Medium | Keep runtime log as minimal placeholder in Sprint 3. |

## Dependencies on External Factors

- Unity 6000.3.x editor/runtime stability
- Existing M0 scene/bootstrap foundations
- Availability of placeholder assets/audio cues

## Architecture Constraints

- Input owns raw Interact intent only.
- MemoryInteractionService owns interaction use-case orchestration.
- MemoryState owns reveal/collect truth.
- ScriptableObject owns static fragment definition/config only.
- UI/VFX/Audio/Animancer are presentation-only.
- Debug Overlay remains read-only.
- Camera does not own interaction truth.
- CombatCore is not changed.

## Explicit Non-Goals

- Full inventory system
- Save/load system
- Quest system
- Dialogue system
- RPG progression
- Boss/multi-enemy systems
- Large map system
- Cinematic system
- CombatCore behavior expansion

## OpenSpec Guidance

Likely OpenSpec-required stories:
- S3-2 Memory Fragment Interaction Prototype
- S3-3 Interaction Prompt Placeholder
- S3-4 Memory Reveal VFX/Audio Placeholder
- S3-5 Runtime Memory Log Placeholder

Docs/review stories usually do not require new OpenSpec:
- S3-1
- S3-6

## Definition of Done for This Sprint

- [ ] All Must Have stories completed
- [ ] M1 exploration-memory loop is playable end-to-end
- [ ] QA plan and smoke evidence exist for Sprint 3
- [ ] Ownership boundaries are preserved (no truth drift into presentation)
- [ ] No prohibited scope systems introduced

## Recommended First Implementation Story

`S3-2 — [Feature] Memory Fragment Interaction Prototype`

Reason: It is the core interaction backbone that S3-3, S3-4, and S3-5 depend on.
