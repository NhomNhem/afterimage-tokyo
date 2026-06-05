# Story S3-4: [Presentation] Memory Reveal VFX/Audio Placeholder

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: Presentation / VFX / Audio
> **Type**: Visual/Feel
> **Estimate**: 1.0d
> **Sprint**: Sprint 3
> **Dependencies**: S3-2
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-05

## Context

S3-2 completed the core Memory Fragment interaction path:

`approach Memory Fragment -> press Interact -> MemoryInteractionService -> MemoryState accepted/rejected outcome`

S3-3 added a read-only interaction prompt placeholder. This story adds the next downstream readability layer: a restrained placeholder response after an accepted MemoryState-backed reveal/collect outcome.

Design trace:
- `design/gdd/systems-index.md`: UI/VFX/Audio support memory-state readability but do not own gameplay truth.
- `design/gdd/memory-state.md`: `Memory State` owns reveal acceptance/rejection and memory-facing truth.
- `production/qa/evidence/m1-readiness-review-2026-05-28.md`: Animancer/VFX behavior should remain deferred to S3-4 and presentation-only.
- `production/qa/evidence/s3-2-memory-fragment-interaction-verification-2026-05-28.md`: S3-2 verifies the interaction service route and MemoryState ownership that S3-4 must observe.
- `production/qa/evidence/s3-3-interaction-prompt-placeholder-verification-2026-06-04.md`: S3-3 prompt behavior remains separate and unchanged.

Technical requirement trace:
- `TR-M0-MEMORY-001`: Memory State owns reveal acceptance and memory-side consequence truth.
- `TR-M0-INPUT-001`: Input Mapping owns raw input truth and emits intent only.

ADR note:
- No ADR applies directly to this S3-4 placeholder story.
- The applicable authority is Sprint 3 scope, the approved S3-1 readiness evidence, and the S3-2/S3-3 downstream presentation boundary.

OpenSpec:
- `openspec/changes/archive/2026-06-05-add-m1-memory-reveal-vfx-audio-placeholder`

## Goal

Play a clear, restrained placeholder reveal feedback response after an accepted Memory Fragment interaction, while keeping VFX/audio/UI strictly downstream of gameplay truth.

## Acceptance Criteria

- [x] Placeholder reveal feedback plays after an accepted MemoryState-backed Memory Fragment reveal/collect outcome.
- [x] Placeholder feedback does not play when there is no eligible fragment.
- [x] Placeholder feedback does not replay for duplicate/ignored interaction spam after collection.
- [x] Placeholder feedback does not play for MemoryState rejected reveal outcomes.
- [x] Feedback observes accepted reveal/result context or `M0MemoryVFXResponse` snapshot as read-only data.
- [x] `M0MemoryVFXResponse` remains the response state/snapshot owner.
- [x] Presentation code does not call MemoryState mutation/acceptance APIs.
- [x] Presentation code does not call MemoryInteractionService command paths or fragment mutation paths.
- [x] Presentation code does not own Unity InputAction callbacks or Interact execution.
- [x] CombatCore, EnemyIntent, TargetContext, Camera, Input, and MemoryState gameplay truth remain unchanged.
- [x] Placeholder remains authored-asset-light and does not expand into final VFX/audio production.
- [x] Placeholder does not create runtime memory log, inventory, quest, dialogue, save/profile, progression, cinematic, or final narrative memory behavior.
- [x] S3-2 interaction behavior and S3-3 prompt behavior remain preserved.
- [x] Console output has no new S3-scope errors/exceptions; warnings are classified.
- [x] Evidence records accepted feedback playback, non-replay on duplicate/spam, ownership boundaries, and dirty asset classification.

## Out of Scope

- Runtime memory log UI (S3-5)
- Full VFX graph, particle system, authored audio clip, mix, or final production VFX/audio pass
- Cinematic, dialogue, quest, inventory, save/profile, progression, or narrative memory database
- Changing MemoryState behavior
- Changing MemoryInteractionService command-path semantics
- Changing InputAction callback ownership
- Changing CombatCore, EnemyIntent, TargetContext, Camera, or locomotion behavior
- MemoryRaycastProProbe alignment
- R3/MessagePipe migration
- Broad Nhem DI migration
- Scene/prefab changes beyond minimal placeholder wiring

## Implementation Notes

- Added a narrow `M1MemoryRevealFeedbackBridge` that converts an accepted `MemoryInteractionSnapshot` plus read-only `MemoryStateSnapshot` into a request on the existing `M0MemoryVFXResponse`.
- Added a UI Toolkit placeholder banner in `CombatDebugOverlay.uxml`/`.uss`.
- `M0CombatDebugOverlayAdapter` only reads `IMemoryVFXResponseSnapshot` to show/hide the banner.
- S3-4 intentionally ships as a visual placeholder only. Audio and final VFX production remain future polish.
- The accepted playback path is downstream of `MemoryInteractionService` and `MemoryState`; it does not decide interaction validity or memory truth.

## Control Manifest Notes

- Presentation systems observe gameplay truth as read-only snapshots or context.
- UI/VFX/Audio must not mutate gameplay state.
- Input remains raw intent only.
- Runtime memory truth remains in MemoryState and S3-2 interaction service boundaries.
- No service locator, `FindObjectOfType`, `Resources.Load`, or direct Unity debug logging is introduced.

## Engine Notes

- Unity 6000.3.x project conventions apply.
- UI implementation uses the existing `CombatDebugOverlay` UI Toolkit document.
- Unity batchmode EditMode test execution was blocked because another Unity Editor instance already had the project open; manual PlayMode verification was completed in that Editor.

## Performance Budget

No meaningful performance impact expected. The placeholder observes an existing response snapshot and updates a small UI Toolkit element. No broad scene scans, heavy allocations, particle systems, audio mixing, or new gameplay loops were introduced.

## Test Evidence

Required evidence file:
- `production/qa/evidence/s3-4-memory-reveal-vfx-audio-placeholder-verification-2026-06-05.md`

OpenSpec:
- `openspec/changes/archive/2026-06-05-add-m1-memory-reveal-vfx-audio-placeholder`
- 26/26 tasks complete.
- `openspec validate add-m1-memory-reveal-vfx-audio-placeholder --strict` PASS before archive.

Automated/source verification:
- `dotnet build .\afterimage-tokyo\afterimage-tokyo.sln --no-restore -v:q /clp:ErrorsOnly` PASS, 0 errors.
- `git -C .\afterimage-tokyo diff --check` PASS.
- Runtime forbidden API scan PASS for changed runtime files.
- `M1MemoryRevealFeedbackBridgeTests` cover accepted trigger, no-eligible non-playback, duplicate/ignored non-replay, MemoryState rejected non-playback, cooldown non-replay, and ownership guardrails.

Manual PlayMode evidence:
- Accepted Memory Fragment interaction shows the placeholder banner once.
- Repeated/spam Interact after collection does not replay the banner.
- Console includes `[M1Memory] Interaction result: fragmentId=memory-fragment outcome=Accepted reason=Reveal accepted by MemoryState`.
- Existing warnings are classified as non-scope/baseline in the evidence file.

## Completion Notes

**Completed**: 2026-06-05
**Criteria**: 15/15 passing
**Deviations**: None
**Test Evidence**:
- `production/qa/evidence/s3-4-memory-reveal-vfx-audio-placeholder-verification-2026-06-05.md`
- OpenSpec archive: `openspec/changes/archive/2026-06-05-add-m1-memory-reveal-vfx-audio-placeholder`
- `M1MemoryRevealFeedbackBridgeTests` source/guardrail coverage
- Manual PlayMode confirmation
**Code Review**: Skipped in lean mode; automated guardrails and manual tester confirmation recorded.
