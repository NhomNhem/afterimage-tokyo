# Story S5-6: [Design Decision] LockOn Toggle Policy

> **Sprint**: Sprint 5
> **Status**: Complete
> **Layer**: Design / Target Context
> **Type**: Config/Data
> **Estimate**: 0.5d
> **Priority**: Should Have
> **Owner**: game-designer
> **Dependencies**: None
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

M0 has evidence for LockOn acquire/focus behavior and prior evidence for acquire/release/reacquire. Sprint 5 needs an explicit policy decision so future implementation and QA do not treat second-press behavior ambiguously.

Relevant trace:
- `TR-M0-TARGET-001` — Lock-On / Target Context owns target truth and state.
- `docs/architecture/adr/ADR-0002-m0-gameplay-truth-ownership-boundaries.md`
- `docs/architecture/control-manifest.md`
- `docs/tech-debt-register.md`
- `production/sprints/sprint-5.md`
- `production/qa/qa-plan-sprint-5-2026-06-09.md`
- `production/qa/evidence/complete-m0-playable-combat-prototype-verification-evidence.md`
- `production/qa/evidence/lockon-toggle-release-2026-05-24.md`
- `design/gdd/lock-on-target-context.md`

## Architecture Notes

- Governed by ADR-0002: Lock-On / Target Context owns target truth and resolves acquire/release requests from Input intent.
- Control manifest version 2026-05-15 applies: this Config/Data story must not change runtime code, scene objects, prefabs, input bindings, camera behavior, or gameplay truth.

## Engine Notes

- N/A — no Unity API or runtime implementation is involved.
- This story updates design/evidence documentation only.

## Performance Budget

- No performance impact expected because no runtime code, scene, prefab, gameplay loop, rendering, or physics changes are in scope.

## Goal

Record the M0 LockOn second-press policy: acquire-only/maintain focus or toggle acquire/release.

## Acceptance Criteria

- [x] The chosen policy is explicitly recorded: acquire-only/maintain focus or toggle acquire/release.
- [x] Rationale explains why this policy is better for M0 duel readability.
- [x] Existing evidence is cited, including acquire/focus and toggle-release observations.
- [x] The affected design document or decision log is updated.
- [x] Follow-up implementation work is created only if the chosen policy differs from current runtime behavior.
- [x] No runtime code, scene, prefab, gameplay, or UI behavior is changed by this story.

## Out of Scope

- Implementing LockOn behavior changes
- Target acquisition algorithm changes
- Camera framing changes
- Multi-target support
- Input binding changes

## Implementation Notes

- This story is a design decision, not an implementation story.
- Favor the policy that best supports one readable M0 duel.
- If current runtime behavior is accepted, document it as intentional rather than accidental.
- If policy and runtime differ, create a separate implementation story/change instead of modifying code here.

## QA Test Cases

- **AC-1**: Policy decision is recorded.
  - Given: prior LockOn evidence and target-context design docs exist.
  - When: the decision is written.
  - Then: it clearly names one policy and does not leave second-press behavior ambiguous.
  - Edge cases: evidence documents disagree, runtime behavior differs by scene.

- **AC-2**: Rationale is M0-readable.
  - Given: M0 is focused on one readable duel.
  - When: the rationale is reviewed.
  - Then: it explains readability/feel tradeoffs without expanding into multi-enemy systems.
  - Edge cases: future features such as multi-target lock-on are deferred.

- **AC-3**: No runtime scope is introduced.
  - Given: this is a Config/Data story.
  - When: it closes.
  - Then: only design/decision/evidence docs changed.
  - Edge cases: follow-up implementation story is created but not implemented here.

## Test Evidence

**Story Type**: Config/Data

Required evidence:
- Decision documented in `design/gdd/lock-on-target-context.md` or a decision log
- Evidence references to previous LockOn observations
- No runtime file changes

Expected evidence location:
- `production/qa/evidence/s5-6-lockon-toggle-policy-decision-2026-06-12.md`

**Status**: [x] Created at `production/qa/evidence/s5-6-lockon-toggle-policy-decision-2026-06-12.md`

## Dependencies

- Depends on: None
- Unlocks: future LockOn implementation/readability polish

## Completion Notes

**Completed**: 2026-06-12
**Criteria**: 6/6 passing
**Deviations**: None
**Test Evidence**: Config/Data decision evidence at `production/qa/evidence/s5-6-lockon-toggle-policy-decision-2026-06-12.md`
**Code Review**: Complete — APPROVED
