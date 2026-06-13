# Story S6-7: Select Next M0/M1 Feel Slice

> **Sprint**: Sprint 6
> **Status**: Not Started
> **Layer**: Design / Production
> **Type**: Config/Data
> **Estimate**: 0.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

**Sprint Plan**: `production/sprints/sprint-6.md`
**QA Plan**: `production/qa/qa-plan-sprint-6-2026-06-12.md`
**Requirement**: Sprint 6 S6-7

**GDD**: `design/gdd/systems-index.md` - M0 combat feel and M1 memory fragment exploration priorities.
**ADR Governing Implementation**: N/A - decision/story planning only.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW
**Engine Notes**: No Unity runtime or asset changes expected.

**Control Manifest Rules**:
- Required: Decisions must support the M0 loop: read -> evade/parry -> counter -> reveal.
- Forbidden: Do not introduce broad RPG, open-world, save, equipment, or progression scope.
- Guardrail: Pick one next slice and explicitly defer alternatives.

---

## Acceptance Criteria

- [ ] One primary next slice is selected.
- [ ] Alternatives are named and deferred with reasons.
- [ ] Decision ties back to M0 combat feel or M1 memory fragment exploration.
- [ ] Decision cites current evidence from Sprint 5/Sprint 6 smoke or QA notes.
- [ ] Decision does not introduce broad RPG, open-world, save, equipment, or progression scope.

---

## Implementation Notes

- Candidate next slices: lock-on readability, enemy telegraph clarity, counter/reveal feedback, or M1 memory feedback polish.
- Prefer the slice with the strongest evidence gap after Sprint 6 smoke.
- Keep output as a short decision note, not a new design epic.

---

## Out of Scope

- Implementing the selected slice.
- Creating a full roadmap.
- Reopening Sprint 6 scope unless the selected slice is already planned.

---

## QA Test Cases

- **AC-1**: One primary next slice is selected.
  - Setup: Review decision note.
  - Verify: Exactly one next slice is marked primary.
  - Pass condition: `/story-readiness` or `/sprint-plan` can use the decision without asking what to do next.

- **AC-2**: Alternatives are deferred with reasons.
  - Setup: Review decision note alternatives.
  - Verify: Each non-selected candidate has a short defer reason.
  - Pass condition: Deferred options are not silently lost.

- **AC-3**: Decision stays within M0/M1 scope.
  - Setup: Compare decision against project current priority.
  - Verify: It supports read -> evade/parry -> counter -> reveal or M1 memory fragment exploration.
  - Pass condition: No broad RPG/open-world/progression scope is introduced.

---

## Test Evidence

**Story Type**: Config/Data
**Required evidence**:
- `production/qa/evidence/s6-7-next-m0-m1-feel-slice-decision.md` or an equivalent design decision note.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Sprint 6 smoke context or current Sprint 5/Sprint 6 QA evidence.
- Unlocks: Sprint 7 planning or the next OpenSpec proposal.
