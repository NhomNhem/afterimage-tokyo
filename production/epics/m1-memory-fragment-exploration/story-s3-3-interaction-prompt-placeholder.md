# Story S3-3: [UI] Interaction Prompt Placeholder

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: UI / Presentation
> **Type**: UI
> **Estimate**: 1.0d
> **Sprint**: Sprint 3
> **Dependencies**: S3-2
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-05

## Context

S3-2 completed the core Memory Fragment interaction path with notes:

`approach Memory Fragment -> press Interact -> MemoryInteractionService -> MemoryState accepted/rejected outcome`

This story adds a minimal interaction prompt placeholder so the player can understand when an eligible Memory Fragment can be interacted with. The prompt is presentation-only. It observes interaction eligibility or read-only interaction context and must not decide whether a fragment is valid, collected, revealed, accepted, or rejected.

Design trace:
- `design/gdd/systems-index.md`: UI and presentation systems support memory-state readability but do not own gameplay truth.
- `design/gdd/memory-state.md`: `Memory State` owns reveal acceptance/rejection and memory-facing truth.
- `production/qa/evidence/m1-readiness-review-2026-05-28.md`: UI readiness is partial and placeholder prompt/log stories are required.
- `production/qa/evidence/s3-2-memory-fragment-interaction-verification-2026-05-28.md`: S3-2 verifies the interaction service route and MemoryState ownership that this UI prompt must observe.

Technical requirement trace:
- `TR-M0-MEMORY-001`: Memory State owns reveal acceptance and memory-side consequence truth.
- `TR-M0-INPUT-001`: Input Mapping owns raw input truth and emits intent only.

ADR note:
- No ADR applies directly to this S3-3 UI placeholder story.
- The applicable authority is Sprint 3 scope, the approved S3-1 readiness evidence, and the S3-2 interaction OpenSpec/evidence.

OpenSpec:
- Required before implementation.
- Suggested change name: `add-m1-interaction-prompt-placeholder`

## Goal

Show a clear, minimal placeholder prompt when a Memory Fragment is eligible for interaction, hide it when no eligible fragment is available, and keep UI strictly downstream of gameplay truth.

## Acceptance Criteria

- [x] Prompt appears when the player is within the eligible interaction context for a Memory Fragment.
- [x] Prompt disappears when the player leaves eligibility range or no eligible fragment is available.
- [x] Prompt text is concise and placeholder-safe, such as `Interact` or `Press F to Interact`.
- [x] Prompt does not call `MemoryState`, `MemoryInteractionService`, input callbacks, or fragment mutation methods to decide truth.
- [x] Prompt observes read-only interaction eligibility/context produced by S3-2 systems or an approved UI-facing read model.
- [x] Pressing Interact remains owned by the existing raw input route and S3-2 interaction orchestration.
- [x] Prompt does not change reveal/collect acceptance, duplicate handling, or MemoryState state.
- [x] Prompt remains presentation-only and does not create inventory, journal, quest, save/profile, or progression behavior.
- [x] Prompt state is evidence-visible in manual capture or debug output.
- [x] Console output has no new S3-scope errors/exceptions; warnings are classified.

## Out of Scope

- Full HUD design
- Runtime memory log UI (S3-5)
- Memory reveal VFX/audio feedback (S3-4)
- Dialogue, lore database, quest, inventory, save/profile, or progression systems
- Changing S3-2 interaction validity rules
- Changing InputAction callback ownership
- Changing MemoryState reveal/collect truth
- Changing CombatCore, EnemyIntent, Camera, or TargetContext behavior
- Polished typography, animation, localization, accessibility pass, or final UI art
- Broad UI Toolkit architecture refactor

## Implementation Notes

- Prefer a small UI/presentation adapter that observes an existing read-only context.
- If a new UI-facing read model is needed, define it in the OpenSpec and keep it downstream of `MemoryInteractionService`/fragment eligibility.
- Do not use service locator, `FindObjectOfType`, `Resources.Load`, or direct Unity debug logging.
- Do not make the prompt the source of truth for eligibility, collection, reveal, or duplicate handling.

## Control Manifest Notes

- Presentation must observe gameplay truth as read-only context.
- UI must not mutate gameplay state.
- Input remains raw intent only.
- Runtime memory truth remains in MemoryState and S3-2 interaction service boundaries.

## Engine Notes

- Unity 6000.3.x project conventions apply.
- UI implementation details must be verified against existing project UI patterns before coding.
- If UI Toolkit is used, keep this story to placeholder prompt behavior only.

## Performance Budget

No meaningful performance impact expected. Prompt visibility should update from an existing interaction context/read model and should not introduce broad scene scans, heavy per-frame allocations, or rendering-heavy UI effects.

## Test Evidence

Required evidence file:
- `production/qa/evidence/s3-3-interaction-prompt-placeholder-verification-2026-06-04.md`

Manual verification required by Sprint 3 QA plan:
- Prompt visibility/behavior capture.
- PASS/PARTIAL/FAIL table for appear, disappear, no-truth-ownership, console classification, and dirty asset classification.

Suggested OpenSpec evidence:
- Proposal/design/tasks/spec under `openspec/changes/add-m1-interaction-prompt-placeholder`.
- Manual capture showing prompt appears near eligible fragment and disappears when not eligible.

## Readiness Notes

S3-2 dependency is complete with notes and is sufficient to start this prompt story. Remaining S3-2 notes are not blockers for S3-3 because:
- `MemoryRaycastProProbe` mismatch is debug-only and not gameplay truth.
- Duplicate manual PlayMode capture is a follow-up; duplicate handling already has focused test coverage.

This story has an OpenSpec proposal, implementation, automated verification, and tester-confirmed manual PlayMode evidence for prompt appear/disappear behavior and Interact routing.

## Completion Notes

**Completed**: 2026-06-05
**Criteria**: 10/10 passing
**Deviations**: None
**Test Evidence**:
- `production/qa/evidence/s3-3-interaction-prompt-placeholder-verification-2026-06-04.md`
- Unity EditMode `GlassRefrain.Tests.EditMode.M1InteractionPromptPlaceholderTests` PASS 3/3
- OpenSpec `add-m1-interaction-prompt-placeholder` PASS 19/19 tasks
**Code Review**: Skipped in lean mode; automated guardrails and manual tester confirmation recorded.
