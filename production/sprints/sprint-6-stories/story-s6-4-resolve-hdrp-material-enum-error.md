# Story S6-4: Resolve HDRP Material Enum Error

> **Sprint**: Sprint 6
> **Status**: Not Started
> **Layer**: Engine / Tools
> **Type**: Config/Data
> **Estimate**: 0.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

**Sprint Plan**: `production/sprints/sprint-6.md`
**QA Plan**: `production/qa/qa-plan-sprint-6-2026-06-12.md`
**Requirement**: Sprint 6 S6-4

**GDD**: N/A - dependency/console hygiene.
**ADR Governing Implementation**: Control Manifest ADR-0001 / Unity 6000.3.x + URP project constraint.

**Engine**: Unity 6000.3.x + URP | **Risk**: MEDIUM
**Engine Notes**: Avoid broad render pipeline migration. Fix only owned references or classify the source as vendor/package noise.

**Control Manifest Rules**:
- Required: Strictly adhere to Unity 6 LTS and URP.
- Forbidden: Do not mutate vendor/package assets unless explicitly approved.
- Guardrail: No gameplay behavior changes for console hygiene.

---

## Acceptance Criteria

- [ ] The known HDRP material enum error no longer appears for owned assets, or is classified as external/vendor and documented.
- [ ] Any changed material or pipeline reference is under owned project content.
- [ ] URP project rendering remains intact.
- [ ] M0 duel scene still loads without material-related S1/S2 errors.
- [ ] No gameplay behavior changes are introduced.
- [ ] Evidence captures console status after domain reload and asset import.

---

## Implementation Notes

- Search for owned HDRP material/shader references before editing.
- Prefer migrating/removing invalid owned references over adding compatibility hacks.
- If the issue is vendor/package-only, record classification and defer rather than patching package content.
- If tooling code changes are required, add a small targeted EditMode test.

---

## Out of Scope

- Full HDRP to URP migration.
- Vendor package edits.
- Visual redesign of materials.
- Gameplay, combat, camera, or scene composition changes.

---

## QA Test Cases

- **AC-1**: HDRP material enum issue is resolved or classified.
  - Setup: Open Unity, allow domain reload/import, and inspect console.
  - Verify: The known error is absent for owned assets or documented as external.
  - Pass condition: Evidence includes console status and classification.

- **AC-2**: URP/M0 rendering remains intact.
  - Setup: Open or run the M0 duel scene after cleanup.
  - Verify: Scene loads without material-related S1/S2 errors.
  - Pass condition: No material cleanup causes broken M0 scene loading.

- **AC-3**: No gameplay behavior changes are introduced.
  - Setup: Review diff.
  - Verify: Changes are limited to owned asset/config/tooling areas.
  - Pass condition: No gameplay code or combat state behavior changes appear in diff.

---

## Test Evidence

**Story Type**: Config/Data
**Required evidence**:
- `production/qa/evidence/s6-4-resolve-hdrp-material-enum-error.md`
- Console screenshot/log excerpt after domain reload/import.
- Targeted EditMode result if tooling code changes.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: None.
- Unlocks: Cleaner Sprint 6 smoke and QA signoff.
