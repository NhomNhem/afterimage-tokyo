# Story S2-5: [QA] M0 Playable Duel Smoke Test Checklist

> **Epic**: M0 First Playable Duel
> **Status**: Complete
> **Layer**: Integration
> **Type**: Integration
> **Estimate**: 0.5d
> **Last Updated**: 2026-06-04

## Context

Sprint 2 readability passes have been delivered with notes:
- S2-2 Combat Feel Readability
- S2-3 Enemy Telegraph Readability
- S2-4 Lock-On Camera Readability

This story creates a repeatable smoke checklist and evidence template so QA/dev can quickly classify stability and readability without changing runtime code.

## Goal

Create a repeatable M0 duel smoke verification package that:
- can be executed by QA or developer in one session,
- cleanly separates scope blockers from known external/non-scope noise,
- produces a PASS/PARTIAL/FAIL outcome with follow-up rules.

## Acceptance Criteria

- [x] Story file exists and defines scope, non-goals, and execution constraints.
- [x] Smoke checklist exists at `production/qa/smoke/m0-playable-duel-smoke-checklist-2026-05-28.md`.
- [x] Evidence template exists at `production/qa/evidence/s2-5-m0-playable-duel-smoke-test-verification-2026-05-28.md`.
- [x] Checklist includes all required smoke areas:
  - project open/domain reload classification
  - scene/bootstrap load
  - VContainer wiring
  - input actions
  - player movement
  - lock-on acquire/release
  - camera readability during lock-on
  - light attack / dodge / parry
  - counter window/counter path when available
  - enemy intent loop (Idle -> Telegraph -> Commit -> Active -> Recovery)
  - health/hit consequence
  - memory reveal/VFX placeholder
  - animator/animancer observer remains presentation-only
  - debug overlay fields
  - console error/warning classification
  - known external material/HDRP issue classification
  - dirty scene/prefab check
  - PASS/PARTIAL/FAIL result table
- [x] Each checklist item has concrete PASS/PARTIAL/FAIL criteria.
- [x] Known external/non-scope issues are explicitly separated from S2 story blockers.
- [x] Template does not claim evidence as executed; it is execution-ready only.
- [x] Follow-up action rules are explicit for PASS/PARTIAL/FAIL outcomes.

## Out Of Scope

- Gameplay code changes
- Unity submodule/runtime behavior changes
- Combat/camera/enemy/animation/VFX tuning
- OpenSpec implementation work

## Execution Notes

- This is docs-only and can be maintained independently from gameplay patches.
- If running the checklist reveals tooling/runtime gaps requiring implementation, open a small OpenSpec change before coding.

## Deliverables

1. `production/epics/m0-first-playable-duel/story-s2-5-m0-playable-duel-smoke-test-checklist.md`
2. `production/qa/smoke/m0-playable-duel-smoke-checklist-2026-05-28.md`
3. `production/qa/evidence/s2-5-m0-playable-duel-smoke-test-verification-2026-05-28.md`
4. `production/qa/smoke-2026-06-04.md`

## Completion Notes

**Completed**: 2026-06-04
**Verdict**: COMPLETE

Evidence:
- Smoke checklist: `production/qa/smoke/m0-playable-duel-smoke-checklist-2026-05-28.md`
- Initial evidence template/execution notes: `production/qa/evidence/s2-5-m0-playable-duel-smoke-test-verification-2026-05-28.md`
- Fresh smoke report: `production/qa/smoke-2026-06-04.md`

Fresh smoke result:
- EditMode project assembly: 197/197 PASS
- PlayMode project assembly: 2/2 PASS
- Manual smoke: PASS all
- Console classification: no gameplay compile/runtime blockers
