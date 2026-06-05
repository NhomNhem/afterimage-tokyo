# Story S3-6: [QA] M1 Exploration-Memory Smoke Test

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: QA / Integration
> **Type**: Integration
> **Estimate**: 0.5d
> **Sprint**: Sprint 3
> **Dependencies**: S3-2, S3-3, S3-4
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-05

## Context

Sprint 3 builds the first M1 exploration-memory loop on top of the M0 gameplay foundation:

`approach Memory Fragment -> prompt appears -> press Interact -> MemoryInteractionService -> MemoryState accepted -> placeholder reveal feedback`

This story verifies the loop end-to-end after the required Sprint 3 implementation stories:
- S3-2 Memory Fragment interaction prototype
- S3-3 Interaction prompt placeholder
- S3-4 Memory reveal VFX/audio placeholder

S3-5 Runtime Memory Log Placeholder remains a should-have story and is not required for the must-have smoke gate.

Design trace:
- `design/gdd/systems-index.md`: UI/VFX/Audio support memory-state readability but do not own gameplay truth.
- `design/gdd/memory-state.md`: `Memory State` owns reveal acceptance/rejection and memory-facing truth.
- `production/qa/qa-plan-sprint-3-2026-05-28.md`: defines the Sprint 3 smoke test scope.
- `production/qa/evidence/m1-readiness-review-2026-05-28.md`: approves M1 readiness with strict ownership boundaries.
- `production/qa/evidence/s3-2-memory-fragment-interaction-verification-2026-05-28.md`: verifies the interaction service route and MemoryState ownership.
- `production/qa/evidence/s3-3-interaction-prompt-placeholder-verification-2026-06-04.md`: verifies prompt behavior and UI ownership boundaries.
- `production/qa/evidence/s3-4-memory-reveal-vfx-audio-placeholder-verification-2026-06-05.md`: verifies reveal feedback playback and duplicate/spam non-replay.

Technical requirement trace:
- `TR-M0-MEMORY-001`: Memory State owns reveal acceptance and memory-side consequence truth.
- `TR-M0-INPUT-001`: Input Mapping owns raw input truth and emits intent only.

ADR note:
- No ADR applies directly to this QA story.
- The applicable authority is Sprint 3 scope, the approved S3-1 readiness evidence, and completed S3-2/S3-3/S3-4 evidence.

OpenSpec:
- None required. This is a QA closure story.

## Goal

Verify that the Sprint 3 M1 exploration-memory loop is stable enough for QA hand-off, with blockers separated from known external/non-scope warnings.

## Acceptance Criteria

- [x] Project open/domain reload has no S3-scope blocker.
- [x] M1 scene/bootstrap loads without crash.
- [x] VContainer/Nhem DI wiring does not block runtime memory interaction.
- [x] Interact input route reaches the memory interaction path.
- [x] Fragment proximity exposes the S3-3 interaction prompt.
- [x] Pressing Interact triggers the accepted reveal/collect response.
- [x] S3-4 reveal banner appears once after accepted interaction.
- [x] Repeated/spam Interact after collection does not replay the accepted reveal banner.
- [x] UI/VFX/Audio/Animancer remain presentation-only and do not own gameplay truth.
- [x] MemoryInteractionService remains interaction orchestration truth.
- [x] MemoryState remains reveal/collect truth.
- [x] Console has no new S3-scope Error/Exception.
- [x] Known external/non-scope warnings are classified separately.
- [x] No unintended dirty scene/prefab/asset state was reported for this smoke pass.
- [x] Smoke report records PASS/PARTIAL/FAIL-style evidence and final QA gate verdict.

## Out of Scope

- Implementing S3-5 Runtime Memory Log Placeholder
- New gameplay behavior
- CombatCore, EnemyIntent, TargetContext, Camera, Input, or MemoryState behavior changes
- MemoryRaycastProProbe alignment
- Final VFX/audio production
- Inventory, quest, dialogue, save/profile, progression, cinematic, or full narrative memory systems
- Broad Nhem DI migration
- R3/MessagePipe migration
- Scene/prefab/content edits

## Implementation Notes

- This story is evidence-only and does not require code changes.
- The smoke report uses existing S3-2/S3-3/S3-4 evidence plus developer-confirmed manual PlayMode smoke results.
- The final smoke verdict is `PASS WITH WARNINGS` because no fresh full Unity Test Runner XML artifact was available for the current Sprint 3 state.
- The warning does not block QA hand-off because compile smoke passed with 0 errors and manual M1 loop smoke was confirmed PASS all.

## Control Manifest Notes

- Input remains raw Interact intent only.
- `MemoryInteractionService` remains interaction orchestration owner.
- `MemoryState` remains reveal/collect truth owner.
- ScriptableObject data remains static/config only.
- UI/VFX/Audio/Animancer remain downstream presentation.
- Debug overlay remains read-only.
- Camera and CombatCore do not own interaction truth.

## Engine Notes

- Unity 6000.3.x project conventions apply.
- Unity tests live under `afterimage-tokyo/Assets/_Project/Tests`.
- A fresh full Unity Test Runner artifact is still recommended before final sprint closure, but absence of that artifact is recorded as a warning rather than a blocker.

## Performance Budget

No new runtime feature work was introduced by this story. Smoke verification did not report hitches or S3-scope performance blockers.

## Test Evidence

Smoke report:
- `production/qa/smoke-2026-06-05.md`

Supporting evidence:
- `production/qa/evidence/m1-readiness-review-2026-05-28.md`
- `production/qa/evidence/s3-2-memory-fragment-interaction-verification-2026-05-28.md`
- `production/qa/evidence/s3-3-interaction-prompt-placeholder-verification-2026-06-04.md`
- `production/qa/evidence/s3-4-memory-reveal-vfx-audio-placeholder-verification-2026-06-05.md`

Automated/source verification:
- `dotnet build .\afterimage-tokyo\afterimage-tokyo.sln --no-restore -v:q /clp:ErrorsOnly` PASS, 0 errors.
- S3-2 focused Unity evidence: `MemoryInteractionServiceTests` 3/3 PASS, MemoryState accept/reject path 7/7 PASS, DI/manual wiring guardrail 1/1 PASS.
- S3-3 focused Unity evidence: `M1InteractionPromptPlaceholderTests` 3/3 PASS.
- S3-4 source/guardrail coverage: `M1MemoryRevealFeedbackBridgeTests` cover accepted feedback, no eligible, duplicate ignored, rejected reveal, cooldown non-replay, and ownership guardrails.

Manual PlayMode evidence:
- Developer confirmed Sprint 3 M1 smoke checks all pass.
- Accepted Memory Fragment interaction shows the placeholder banner once.
- Repeated/spam Interact after collection does not replay the banner.
- Console warnings are classified as expected/non-scope or baseline; no S3-scope blocker is recorded.

## Completion Notes

**Completed**: 2026-06-05
**Criteria**: 15/15 passing
**Deviations**:
- Fresh full Unity Test Runner XML artifact was not available for the current Sprint 3 state; recorded as warning, not blocker.
**Test Evidence**:
- `production/qa/smoke-2026-06-05.md`
- Supporting S3-1/S3-2/S3-3/S3-4 evidence files listed above.
**Code Review**: Not applicable; QA/docs-only story.
