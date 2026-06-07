# S4-7 MemoryRaycastProProbe Alignment Verification

Date: 2026-06-07
Story: `production/epics/m1-memory-fragment-exploration/story-s4-7-memory-raycast-probe-alignment-spike.md`
Change: `align-memory-raycast-probe-with-interaction-service`
Scope: Align memory debug probe evidence with `MemoryInteractionService` read-only eligibility while preserving memory gameplay behavior.

## Summary

Result: PASS WITH NOTES

`MemoryRaycastProProbe` now logs service-owned eligibility from `MemoryInteractionService.Snapshot` and keeps RaycastPro detector/collider output as supplemental `collider*` evidence. The probe remains debug-only and does not execute interaction, mutate memory truth, or route prompt/reveal/log behavior.

## Baseline And Scope

| Check | Result | Notes |
| --- | --- | --- |
| Working tree state | PARTIAL | Parent/submodule had pre-existing unrelated dirty files before implementation. This change did not touch those files. |
| Baseline service tests | PASS | Unity EditMode `MemoryInteractionServiceTests`: 3/3 passed before implementation. |
| Existing mismatch | PASS | Previous evidence recorded `MemoryRaycastProProbe` collider-only `hitName=None` as debug mismatch while service interaction passed. |

## Implementation Evidence

| Area | Result | Notes |
| --- | --- | --- |
| Service-owned eligibility in probe | PASS | Probe logs `serviceEligible`, `serviceFragmentId`, `serviceOutcome`, and `serviceReason` from `MemoryInteractionService.Snapshot`. |
| RaycastPro data remains supplemental | PASS | Probe logs `colliderAvailable`, `colliderHitName`, `colliderDistance`, `colliderLayer`, `colliderWithinRadius`, and `colliderReason`. |
| Missing detector does not block interaction | PASS | Missing `RangeDetector` logs a warning and still reports service snapshot availability; gameplay remains owned by `MemoryInteractionService`. |
| Logger usage | PASS | Probe uses `INhemLogger`; no direct Unity debug logging added. |

## Ownership Guardrails

| Guardrail | Result | Notes |
| --- | --- | --- |
| Probe does not execute Interact | PASS | Source guardrail forbids calling service `Tick` from probe. |
| Probe does not mutate MemoryState | PASS | Source guardrail forbids `IntakeRevealRequest`, `EvaluateRequestedReveal`, and `AdvancePhase`. |
| Probe does not own prompt/reveal/log | PASS | Source guardrail forbids prompt/log presentation update calls from probe. |
| No broad lookup/resource/service locator | PASS | Source guardrail forbids `FindObject*`, `Resources.Load`, and `ServiceLocator`. |

## Automated Checks

| Check | Result | Notes |
| --- | --- | --- |
| Unity EditMode baseline memory tests | PASS | 3/3 passed: `MemoryInteractionServiceTests`. |
| Unity EditMode focused memory suite | PASS | 22/22 passed: `MemoryInteractionServiceTests`, `MemoryRaycastProProbeAlignmentTests`, interaction prompt, reveal feedback, and runtime memory log tests. |
| Unity EditMode scene composition suite | PASS | 19/19 passed: `SceneComposition_test`. |
| OpenSpec strict validation | PASS | `openspec validate align-memory-raycast-probe-with-interaction-service --strict`. |

## Console Classification

| Console Entry | Classification | Action |
| --- | --- | --- |
| `KinematicCharacterController` UDR warnings | Existing vendor/package warnings | Out of scope. |
| `BroAudio` sample UDR warning | Existing vendor/sample warning | Out of scope. |
| `IdaFaber` demo UDR warnings | Existing vendor/demo warning | Out of scope. |
| `Odin Validator` UDR warning | Existing package warning | Out of scope. |
| `ParticleDropdownController.audio hides inherited member` | Existing resource script warning | Out of scope. |
| `SampleTest` nullable annotations warning | Existing test warning | Out of scope. |
| `PrefabStage.prefabAssetPath is obsolete` | Existing resource script warning | Out of scope. |
| `Unity Toon Shader` / `Dark UI` warnings | Existing package/resource warnings | Out of scope. |

## Manual PlayMode Checklist

Tester confirmed all five manual PlayMode smoke steps PASS:

| Step | Result | Expected |
| --- | --- | --- |
| Eligible fragment shows prompt | PASS | Prompt appears from service-owned eligibility. |
| Interact accepted | PASS | `Interact -> MemoryInteractionService -> MemoryState` remains accepted path. |
| Reveal feedback appears once | PASS | Reveal feedback still triggers once after accepted interaction. |
| Runtime memory log appends one entry | PASS | Accepted interaction adds one placeholder entry. |
| Spam Interact does not replay incorrectly | PASS | Duplicate/spam behavior remains equivalent to baseline. |

## PASS/PARTIAL/FAIL Table

| Area | Result | Notes |
| --- | --- | --- |
| Compile/test runner | PASS | Focused EditMode tests passed. |
| Service/probe evidence alignment | PASS | Probe now reports service truth and collider supplemental data separately. |
| Ownership boundaries | PASS | Source guardrails cover command/mutation/lookup/logging restrictions. |
| Console | PASS WITH NOTES | Existing vendor/package warnings only. |
| Manual PlayMode | PASS | Tester confirmed all five checklist items passed. |
