# Story S5-1: [QA] Sprint 4 Smoke Check

> **Sprint**: Sprint 5
> **Status**: Complete
> **Layer**: QA / Integration
> **Type**: Integration
> **Estimate**: 0.5d
> **Priority**: Must Have
> **Owner**: qa-lead
> **Dependencies**: Sprint 4 must-have complete
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-09

## Context

Sprint 5 begins by closing Sprint 4 with an explicit smoke check. The smoke covers the M1 exploration-memory loop and the M0 combat regression path before Sprint 5 starts higher-risk dodge displacement work.

Reference plan:
- `production/sprints/sprint-5.md`
- `production/qa/qa-plan-sprint-5-2026-06-09.md`
- `production/qa/smoke-2026-06-09.md`

## Goal

Verify that Sprint 4 must-have work is stable enough to hand off to QA sign-off.

## Acceptance Criteria

- [x] M1 exploration-memory loop is checked: approach fragment -> prompt appears -> Interact -> reveal feedback -> runtime log entry.
- [x] Sprint 4 must-have stories S4-1, S4-2, S4-3, and S4-4 are verified Complete or explicitly classified.
- [x] M0 combat duel regression is checked: attack, dodge, parry, counter, and health.
- [x] Compile smoke is classified with no new Sprint 4 blocking errors.
- [x] Console output is classified with no new Sprint 4-scope blocker.
- [x] A smoke report is written with PASS, PARTIAL, or FAIL verdict.

## Out of Scope

- New runtime code
- New Unity scene or prefab changes
- Sprint 5 gameplay implementation
- Fixing unrelated material, package, or editor warnings

## Implementation Notes

- This is a QA execution story.
- Evidence may be evidence-based when Unity Test Runner output is not available through CLI.
- Existing Sprint 4 evidence files may be cited instead of rerunning every focused test manually.

## QA Test Cases

- **AC-1**: M1 loop smoke path is verified.
  - Given: Sprint 4 memory features are present.
  - When: the tester approaches a memory fragment, sees the prompt, presses Interact, and observes reveal feedback.
  - Then: a runtime memory log entry is present and no duplicate/spam replay regression is reported.
  - Edge cases: missing fragment setup, prompt appears but Interact is rejected, runtime log does not append.

- **AC-2**: M0 combat regression is verified.
  - Given: the M0 duel scene or equivalent smoke path is available.
  - When: the tester runs attack, dodge, parry, counter, and health interactions.
  - Then: the duel loop remains operable and no Sprint 4 change blocks combat.
  - Edge cases: existing non-blocking visual debt, external material warnings.

- **AC-3**: Smoke verdict is documented.
  - Given: automated and manual evidence has been reviewed.
  - When: the smoke report is written.
  - Then: it includes PASS, PARTIAL, or FAIL and classifies any warnings.
  - Edge cases: Unity Test Runner unavailable via CLI, evidence-based fallback required.

## Test Evidence

**Story Type**: Integration

Required evidence:
- Smoke report at `production/qa/smoke-2026-06-09.md`
- Classification of automated/manual evidence
- No runtime file changes for this story

**Status**: [x] Created

## Completion Notes

**Completed**: 2026-06-09
**Evidence**: `production/qa/smoke-2026-06-09.md`
**Verdict**: PASS WITH WARNINGS
**Warnings**: Unity Test Runner not run via CLI; no `tests/` directory detected by smoke skill; performance not checked this session.
