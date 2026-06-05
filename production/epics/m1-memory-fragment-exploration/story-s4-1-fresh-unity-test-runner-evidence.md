# Story S4-1: [QA] Fresh Sprint 3/Sprint 4 Unity Test Runner Evidence

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: QA / Integration
> **Type**: Integration
> **Estimate**: 0.5d
> **Sprint**: Sprint 4
> **Dependencies**: S3-6
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-05

## Context

Sprint 3 closed the M1 exploration-memory loop with `PASS WITH WARNINGS`.
The main remaining QA condition is that no fresh full Unity Test Runner artifact
was available for the current Sprint 3/Sprint 4 baseline.

This story captures that fresh test evidence before Sprint 4 implementation adds
new runtime changes.

Sprint 4 critical path:

`fresh test evidence -> runtime memory log placeholder -> runtime memory log smoke -> S3-5 carryover closure`

Design trace:
- `design/gdd/m0-memory-state-ownership.md`: Memory State owns reveal acceptance and memory-side consequence truth.
- `design/gdd/m0-input-system.md`: Input Mapping owns raw input truth and emits intent only.
- `production/sprints/sprint-4.md`: S4-1 is the recommended first story.
- `production/qa/qa-plan-sprint-4-2026-06-05.md`: defines S4-1 test scope and artifact expectations.
- `production/qa/qa-signoff-sprint-3-2026-06-05.md`: records Sprint 3 approval with the fresh test artifact condition.
- `production/qa/smoke-2026-06-05.md`: records Sprint 3 smoke result as `PASS WITH WARNINGS`.

Technical requirement trace:
- `TR-M0-MEMORY-001`: Memory State owns reveal acceptance and memory-side consequence truth.
- `TR-M0-INPUT-001`: Input Mapping owns raw input truth and emits intent only.

ADR note:
- No ADR applies directly to this QA evidence story.
- ADR-0001 remains related future architecture context only; this story does not implement refactor work.

OpenSpec:
- None required. This is a QA/evidence story.

## Goal

Capture fresh Unity Test Runner evidence, or classify the Unity Test Runner blocker with an explicit fallback path, so Sprint 4 starts from a known test baseline.

## Acceptance Criteria

- [x] Fresh EditMode test evidence is captured under `afterimage-tokyo/test-results/` or the blocker is classified.
- [x] Fresh PlayMode test evidence is captured under `afterimage-tokyo/test-results/` or the blocker is classified.
- [x] Test command, timestamp, total/pass/fail counts, and result artifact paths are recorded.
- [x] Build/compile state has 0 errors.
- [x] M1 memory interaction focused coverage is included or explicitly listed as unavailable.
- [x] M1 prompt and reveal feedback focused coverage is included or explicitly listed as unavailable.
- [x] Existing M0 regression coverage touched by the M1 loop is included or explicitly listed as unavailable.
- [x] Console warnings are classified as known, acceptable, or blocking.
- [x] Any Unity Test Runner blocker includes a fallback verification path.
- [x] No runtime feature, scene, prefab, or gameplay behavior is changed by this story.
- [x] Evidence is written to a Sprint 4 QA evidence file and linked from story completion notes.

## Out of Scope

- Runtime memory log implementation
- S4-2 UI/read-model work
- S4-3 smoke execution
- Gameplay behavior changes
- CombatCore, Input, MemoryState, TargetContext, Camera, EnemyIntent, or PlayerLocomotion changes
- MemoryInteractionTickBridge extraction
- MemoryRaycastProProbe alignment
- Scene/prefab/content edits
- Broad Nhem DI migration
- R3/MessagePipe migration

## Implementation Notes

- This story is evidence-only and should not modify runtime code.
- Prefer Unity Test Runner artifacts for both EditMode and PlayMode.
- If Unity Test Runner cannot run because of editor/tooling constraints, capture:
  - command attempted
  - exact error/blocker
  - fallback compile/test evidence
  - manual scope that remains unverified
- The fallback path should be explicit enough for `/story-done` and QA sign-off to decide PASS, PARTIAL, or BLOCKED.

## Control Manifest Notes

- QA evidence must not change gameplay truth ownership.
- No direct Unity debug logging should be introduced.
- No service locator, `FindObjectOfType`, or `Resources.Load` should be introduced.
- UI/VFX/Audio/Animancer remain presentation-only.
- Debug evidence remains read-only and must not drive gameplay behavior.

## Engine Notes

- Unity 6000.3.x project conventions apply.
- Unity test results should be written under `afterimage-tokyo/test-results/`.
- PowerShell/profile noise should be separated from Unity compile/test failures when classifying evidence.

## Performance Budget

No runtime performance impact is expected. This story only captures evidence and does not add runtime behavior.

## QA Test Cases

*Written from `production/qa/qa-plan-sprint-4-2026-06-05.md`. The implementer verifies against these cases; do not invent new closure criteria during execution.*

- **AC-1**: Fresh EditMode evidence is captured or blocker classified.
  - Given: Sprint 4 starts from the current M1 baseline.
  - When: the QA lead runs the Unity EditMode test suite or focused M1/M0 regression set.
  - Then: result artifact paths, pass/fail counts, and blocker state are recorded.
  - Edge cases: Unity Editor already open, Test Runner unavailable, stale test artifact, partial suite only.

- **AC-2**: Fresh PlayMode evidence is captured or blocker classified.
  - Given: PlayMode scene/bootstrap tests exist or can be invoked.
  - When: the QA lead runs the PlayMode test path.
  - Then: result artifact paths are recorded, or the blocker and fallback path are documented.
  - Edge cases: scene bootstrap unavailable, PlayMode runner timeout, package/tooling failure.

- **AC-3**: Compile state has 0 errors.
  - Given: the Unity project solution is available.
  - When: compile/build smoke is run.
  - Then: the evidence records 0 compile errors or marks the story blocked.
  - Edge cases: warnings only, project profile noise, missing packages.

- **AC-4**: M1 loop focused coverage is represented.
  - Given: existing tests and evidence cover MemoryInteractionService, prompt, and reveal feedback.
  - When: fresh evidence is assembled.
  - Then: memory interaction, prompt, reveal feedback, and relevant M0 regression coverage are listed as run or explicitly unavailable.
  - Edge cases: renamed tests, skipped tests, test assembly not discovered.

- **AC-5**: Console output is classified.
  - Given: test/build/manual fallback output includes logs or warnings.
  - When: evidence is written.
  - Then: known, acceptable, and blocking warnings/errors are separated.
  - Edge cases: NDF warnings, PowerShell profile noise, unrelated package warnings.

- **AC-6**: Evidence-only boundary is preserved.
  - Given: this story is QA-only.
  - When: the story is completed.
  - Then: no runtime code, scene, prefab, or gameplay behavior changes are included.
  - Edge cases: generated test result files, generated logs, local editor artifacts.

## Test Evidence

**Story Type**: Integration / QA

Required evidence:
- Fresh EditMode result artifact or classified blocker.
- Fresh PlayMode result artifact or classified blocker.
- Compile/build smoke output with 0 errors.
- Console classification.
- PASS/PARTIAL/FAIL summary table.

Expected evidence file:
- `production/qa/evidence/s4-1-fresh-unity-test-runner-evidence-2026-06-05.md`

Supporting context:
- `production/qa/qa-signoff-sprint-3-2026-06-05.md`
- `production/qa/smoke-2026-06-05.md`
- `production/qa/qa-plan-sprint-4-2026-06-05.md`

**Status**: [x] Created and verified

## Dependencies

- Depends on: S3-6 Complete
- Unlocks: S4-2 Runtime Memory Log Placeholder

## Completion Notes

**Completed**: 2026-06-05
**Verdict**: COMPLETE WITH NOTES
**Criteria**: 11/11 passing
**Deviations**: None blocking.
**Advisory Notes**:
- Unity MCP job IDs are recorded as runner evidence; dedicated XML/log artifacts under `afterimage-tokyo/test-results/` were not emitted by the MCP runner.
- Unity MCP console query was blocked by a tooling/path-length error and is classified separately from Unity compile/test failures.
- Unity submodule has pre-existing untracked recovery files under `Assets/_Recovery/`; they were left untouched.
**Test Evidence**:
- `production/qa/evidence/s4-1-fresh-unity-test-runner-evidence-2026-06-05.md`
- Compile smoke: PASS, 0 errors / 720 warnings.
- Unity EditMode full suite: PASS, 219/219.
- Unity focused M1 EditMode set: PASS, 12/12.
- Unity PlayMode suite: PASS, 2/2.
**Code Review**: Skipped in lean mode; QA evidence story plus focused fixes verified by compile and Unity Test Runner.
**Scope**:
- Runtime gameplay truth unchanged.
- Scene/prefab/content files unchanged by this story.
- Fixes were limited to test guardrail precision and NhemBootstrap in-memory test logging needed to restore test correctness.
