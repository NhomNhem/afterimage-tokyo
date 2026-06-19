# Story S6-5: Standardize Retrospective Debt Marker Baseline

> **Sprint**: Sprint 6
> **Status**: Complete
> **Layer**: Production / Tools
> **Type**: Config/Data
> **Estimate**: 0.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

**Sprint Plan**: `production/sprints/sprint-6.md`
**QA Plan**: `production/qa/qa-plan-sprint-6-2026-06-12.md`
**Requirement**: Sprint 6 S6-5

**GDD**: N/A - retrospective process hygiene.
**ADR Governing Implementation**: N/A - process/documentation story.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW
**Engine Notes**: No Unity runtime or asset changes expected.

**Control Manifest Rules**:
- Required: Process evidence must be repeatable and auditable.
- Forbidden: Do not count generated/vendor/build output as project debt.
- Guardrail: Keep command simple enough to rerun during future retrospectives.

---

## Acceptance Criteria

- [x] TODO/FIXME/HACK marker command is documented.
- [x] Included paths are explicit.
- [x] Excluded paths are explicit.
- [x] Generated/vendor/build folders are excluded.
- [x] Resulting counts are captured as evidence.
- [x] Future retros can rerun the same command and compare counts reliably.

---

## Implementation Notes

- Prefer `rg` for repeatable counting.
- Document the command in a production process note, retrospective template note, or Sprint 6 evidence file.
- Include enough path/exclusion detail that another agent can rerun it without guessing.

---

## Out of Scope

- Fixing all TODO/FIXME/HACK markers.
- Introducing a new debt tracking system.
- Editing gameplay code solely to reduce marker counts.

---

## QA Test Cases

- **AC-1**: Debt marker command is repeatable.
  - Setup: Run the documented command from repository root.
  - Verify: It completes and reports marker counts.
  - Pass condition: Evidence includes command, included paths, excluded paths, and counts.

- **AC-2**: Exclusions avoid generated/vendor/build noise.
  - Setup: Review command exclusions.
  - Verify: Library, Temp, Obj, build output, and third-party/vendor paths are excluded where appropriate.
  - Pass condition: Future retros are not dominated by generated or vendor content.

---

## Test Evidence

**Story Type**: Config/Data
**Required evidence**:
- `production/qa/evidence/s6-5-retro-debt-marker-baseline.md` or an updated retrospective/process note.

**Status**: [x] Created — `production/qa/evidence/s6-5-retro-debt-marker-baseline.md`

---

## Completion Notes
**Completed**: 2026-06-16
**Criteria**: 6/6 passing
**Deviations**: None
**Test Evidence**: Config/Data — evidence doc at `production/qa/evidence/s6-5-retro-debt-marker-baseline.md`
**Code Review**: N/A — Production/Tools story

---

## Dependencies

- Depends on: Sprint 5 retrospective action item.
- Unlocks: Cleaner Sprint 6 and future retrospective comparisons.
