# Story S5-9: [Dependency] Resolve HDRP Material Enum Error

> **Sprint**: Sprint 5
> **Status**: Not Started
> **Layer**: Infrastructure / Asset Pipeline
> **Type**: Logic
> **Estimate**: 0.5d
> **Priority**: Nice to Have
> **Owner**: engine-programmer
> **Dependencies**: None
> **Manifest Version**: 2026-05-15
> **Last Updated**:

## Context

Several evidence files classify an external/non-scope HDRP material drawer warning:

`Failed to create MaterialEnum, enum UnityEditor.Rendering.HighDefinition.TransparentCullMode not found`

Sprint 5 may resolve or classify this dependency issue so future global console gates can become stricter.

Relevant trace:
- `docs/tech-debt-register.md`
- `production/sprints/sprint-5.md`
- `production/qa/qa-plan-sprint-5-2026-06-09.md`
- `production/qa/evidence/s4-2-runtime-memory-log-placeholder-verification-2026-06-05.md`
- `afterimage-tokyo/Assets/_Project/Content/Materials/`

## Goal

Identify and migrate or classify HDRP `TransparentCullMode` material/drawer references so Unity Editor console no longer reports the unresolved HDRP enum as an M0/M1 blocker.

## Acceptance Criteria

- [ ] Source material, shader, package, or drawer references for `TransparentCullMode` are identified.
- [ ] Owned project assets under `afterimage-tokyo/Assets/_Project/` use URP-compatible configuration or are explicitly classified.
- [ ] Unity Editor starts or reloads without unresolved HDRP `TransparentCullMode` enum errors, or the remaining warnings are outside owned scope and documented.
- [ ] Console output classification distinguishes owned asset issues from vendor/package issues.
- [ ] No gameplay, combat, memory, input, or scene behavior is changed.
- [ ] Validation evidence is captured.

## Out of Scope

- Full material art pass
- Render pipeline migration
- Third-party package source changes unless explicitly approved
- Combat, locomotion, memory, or UI behavior changes
- Shader redesign

## Implementation Notes

- Prefer identifying exact owned assets first.
- Do not bulk-edit materials without confirming they are owned and URP-compatible.
- If remaining errors are vendor/package-only, document that classification rather than forcing risky changes.
- This story is nice-to-have; do not let it block S5-4.

## QA Test Cases

- **AC-1**: HDRP enum references are identified.
  - Given: project materials and packages are searchable.
  - When: `TransparentCullMode` references are inspected.
  - Then: owned project references and external/vendor references are separated.
  - Edge cases: serialized material property remains but no drawer error occurs.

- **AC-2**: Owned assets are URP-compatible or classified.
  - Given: owned project assets under `afterimage-tokyo/Assets/_Project/` are known.
  - When: their material configuration is reviewed.
  - Then: each relevant asset is migrated, verified compatible, or documented as intentionally deferred.
  - Edge cases: generated material files, imported character materials, package cache references.

- **AC-3**: Console classification improves.
  - Given: Unity Editor reload or compile-domain validation runs.
  - When: console output is reviewed.
  - Then: unresolved HDRP enum errors are gone or explicitly non-owned/non-blocking.
  - Edge cases: Library/PackageCache warnings, fresh import warnings.

- **AC-4**: Gameplay remains untouched.
  - Given: this is an asset/dependency cleanup story.
  - When: changes are reviewed.
  - Then: no combat, locomotion, memory, input, scene, or prefab behavior changes are included.
  - Edge cases: material asset changes under character visuals only.

## Test Evidence

**Story Type**: Logic

Required evidence:
- Validation notes at `production/qa/evidence/s5-9-resolve-hdrp-material-enum-verification-2026-06-11.md`
- Console classification after reload or compile-domain check
- List of changed or classified material/shader/package references

Expected automated test path from QA plan:
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/HdrpMaterialEnumResolutionTests.cs`

**Status**: [ ] Not yet created

## Dependencies

- Depends on: None
- Unlocks: stricter console gates for later sprints
