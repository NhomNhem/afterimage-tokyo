# Story S3-2: [Feature] Memory Fragment Interaction Prototype

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete with Notes
> **Layer**: Gameplay / Integration
> **Type**: Integration
> **Estimate**: 2.0d
> **Sprint**: Sprint 3
> **Dependencies**: S3-1
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-04

## Context

S3-1 approved the M1 exploration-memory slice with notes and recommended a small OpenSpec before implementation.
This story implements the first narrow player-facing M1 loop:

`approach Memory Fragment -> press Interact -> MemoryInteractionService -> MemoryState accepted/rejected outcome`

Design trace:
- `design/gdd/memory-state.md`: `Memory State` owns reveal request acceptance or rejection, provisional memory state value, and memory-facing debug truth.
- `design/gdd/systems-index.md`: `Memory State` owns reveal acceptance/rejection and provisional memory consequence for M0.
- `production/qa/evidence/m1-readiness-review-2026-05-28.md`: S3-2 should focus on `MemoryFragment`, `MemoryInteractionService`, interaction detection, and runtime read-model boundaries without expanding into full RPG systems.

Technical requirement trace:
- `TR-M0-MEMORY-001`: Memory State owns reveal acceptance and memory-side consequence truth.
- `TR-M0-INPUT-001`: Input Mapping owns raw input truth and emits intent only.

ADR note:
- No ADR applies directly to this S3-2 implementation story; the applicable authority is the approved S3-1 readiness evidence plus the S3-2 OpenSpec change.
- Future orchestration decomposition records are related follow-up work only and are not prerequisites for this story.

OpenSpec:
- `openspec/changes/implement-m1-memory-fragment-interaction`

## Goal

Allow the player to interact with an eligible Memory Fragment and trigger a safe reveal/collect request through approved ownership boundaries while preserving the M0 combat loop and avoiding scope expansion.

## Acceptance Criteria

- [x] A `MemoryFragmentDefinition` ScriptableObject holds static fragment metadata/config only and stores no runtime collected/revealed truth.
- [x] A runtime `MemoryFragment`/eligibility boundary identifies whether a fragment is interactable.
- [x] Interact input remains raw intent and does not own reveal/collect truth.
- [x] `MemoryInteractionService` owns interaction use-case orchestration.
- [x] `MemoryState` remains authoritative for accepted/rejected reveal/collect outcomes.
- [x] Pressing Interact without an eligible fragment is safe and does not accept reveal/collect.
- [x] Duplicate interaction is handled safely through the MemoryState-backed path without duplicate truth mutation.
- [x] UI/VFX/Audio/Animancer remain downstream presentation-only consumers.
- [x] CombatCore, EnemyIntent, TargetContext, and Camera gameplay truth remain unchanged.
- [x] Debug/evidence output can show fragment presence, Interact route, service result, MemoryState outcome, and known limitations.
- [x] Scene/prefab changes, if required for the fragment path, are explicitly classified in evidence.

## Out of Scope

- Full inventory system
- Save/load/profile persistence
- Quest/dialogue/lore database systems
- RPG progression or long-term narrative memory graph
- CombatCore timing/result changes
- Enemy lifecycle changes
- Camera ownership changes
- UI prompt polish beyond downstream placeholders
- MemoryRaycastProProbe alignment follow-up
- Broad Nhem DI migration
- R3/MessagePipe migration

## Implementation Notes

- The implementation uses the existing Input System path for `Interact`.
- Runtime truth remains in `MemoryState`.
- `MemoryInteractionService` is the use-case bridge between eligible fragment context and MemoryState.
- ScriptableObject data is static authoring/config only.
- The accepted interaction path has manual PlayMode evidence.
- Duplicate behavior has focused test evidence; explicit second-interact manual capture remains a follow-up note.

## Control Manifest Notes

- Input follows the Control Manifest rule that Input emits raw intents only.
- Runtime memory truth stays in pure/application memory state/service boundaries.
- Presentation systems remain read-only/downstream and do not mutate gameplay truth.
- No `FindObjectOfType`, `Resources.Load`, service locator, or direct Unity debug logging is introduced by this story.

## Engine Notes

- Unity 6000.3.x project conventions are preserved.
- Unity New Input System remains the input source; this story only routes the existing `Interact` intent path.
- ScriptableObject usage is static authored data only and excludes runtime collected/revealed state.

## Performance Budget

No meaningful performance impact is expected. The story adds a narrow interaction eligibility/service route and does not introduce broad scans, allocations-heavy hot paths, rendering work, physics-heavy loops, or combat timing changes.

## Test Evidence

Evidence file:
- `production/qa/evidence/s3-2-memory-fragment-interaction-verification-2026-05-28.md`

Focused EditMode tests:
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/MemoryInteractionServiceTests.cs`
  - `Tick_WithEligibleFragmentAndInteract_AcceptsThroughMemoryState`
  - `Tick_WithoutEligibleFragmentAndInteract_IsSafe`
  - `Tick_DuplicateInteraction_IsIgnoredSafely`

Recorded evidence summary:
- Focused interaction tests: 3/3 PASS
- MemoryState accept/reject path tests: 7/7 PASS
- DI/manual wiring guardrail test: 1/1 PASS
- Manual PlayMode accepted path: PASS WITH NOTES

## Completion Notes

**Completed**: 2026-05-29
**Closure synced**: 2026-06-04
**Verdict**: COMPLETE WITH NOTES

What is complete:
- Core S3-2 interaction path is functional.
- `Interact -> MemoryInteractionService -> MemoryState accepted` is verified.
- M0 gameplay loop continues running during the capture.
- Ownership boundaries remain intact.

Known notes/follow-ups:
- `MemoryRaycastProProbe` debug raycast mismatch is follow-up only and not gameplay truth.
- Explicit duplicate second-interact manual capture remains pending, though duplicate handling is covered by focused EditMode tests.
- S3-3/S3-4/S3-5 remain separate downstream UI/presentation/read-model stories.
