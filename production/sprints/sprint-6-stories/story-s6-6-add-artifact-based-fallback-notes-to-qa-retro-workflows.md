# Story S6-6: Add Artifact-Based Fallback Notes to QA/Retro Workflows

> **Sprint**: Sprint 6
> **Status**: Complete
> **Layer**: Production / Process
> **Type**: Config/Data
> **Estimate**: 0.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

**Sprint Plan**: `production/sprints/sprint-6.md`
**QA Plan**: `production/qa/qa-plan-sprint-6-2026-06-12.md`
**Requirement**: Sprint 6 S6-6

**GDD**: N/A - workflow resilience.
**ADR Governing Implementation**: N/A - process/documentation story.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW
**Engine Notes**: No Unity runtime or asset changes expected.

**Control Manifest Rules**:
- Required: QA and retrospective outputs must be auditable through files and session markers.
- Forbidden: Fallback paths must not weaken QA signoff or retro accountability.
- Guardrail: Keep workflow notes concise and actionable.

---

## Acceptance Criteria

- [x] QA workflow explains artifact-based fallback when interactive helpers are unavailable.
- [x] Retro workflow explains artifact-based fallback when interactive helpers are unavailable.
- [x] Fallback still requires explicit evidence files, verdicts, and session markers.
- [x] Fallback does not weaken QA signoff or retrospective accountability.
- [x] Changed workflow files are listed in evidence.

---

## Implementation Notes

- Prefer updating local skill/workflow docs or production process docs already used by the project.
- State when fallback is allowed: helper unavailable, but source artifacts are present and auditable.
- State required output shape: report file, verdict, evidence links, and `production/session-state/active.md` marker.

---

## Out of Scope

- Rewriting the entire skill system.
- Adding new automation tooling.
- Changing QA/retro verdict criteria.

---

## QA Test Cases

- **AC-1**: QA fallback is explicit.
  - Setup: Review changed QA workflow note.
  - Verify: It states how to proceed from artifacts when helpers are unavailable.
  - Pass condition: A reviewer can identify required inputs, output report, verdict, and marker.

- **AC-2**: Retro fallback is explicit.
  - Setup: Review changed retrospective workflow note.
  - Verify: It states how to proceed from artifacts when helpers are unavailable.
  - Pass condition: A reviewer can run a retro without hidden interactive dependencies.

- **AC-3**: Accountability is preserved.
  - Setup: Review fallback language.
  - Verify: Evidence files, verdicts, and session markers remain required.
  - Pass condition: Fallback does not permit silent or evidence-free close-out.

---

## Test Evidence

**Story Type**: Config/Data
**Required evidence**:
- `production/qa/evidence/s6-6-artifact-fallback-workflow-notes.md` or story-done summary listing changed workflow files.

**Status**: [x] Created — `production/qa/evidence/s6-6-artifact-fallback-workflow-notes.md`

---

## Completion Notes
**Completed**: 2026-06-16
**Criteria**: 5/5 passing
**Deviations**: None
**Test Evidence**: Config/Data — evidence doc at `production/qa/evidence/s6-6-artifact-fallback-workflow-notes.md`
**Code Review**: N/A — Production/Process story

---

## Dependencies

- Depends on: Sprint 5 retrospective action item.
- Unlocks: More reliable future QA/retro workflow runs.
