# Story S4-6: [Refactor] Implement MemoryInteractionTickBridge Thin Slice

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: Bootstrap / Orchestration
> **Type**: Integration
> **Estimate**: 1.0d
> **Sprint**: Sprint 4
> **Dependencies**: S4-1, S4-2, ADR-0001, `extract-m0-gameplay-tick-memory-bridge`
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-06

## Context

Sprint 4 includes the first ADR-guided orchestration cleanup slice after the M1 memory loop was verified. `M0GameplayTickHandler` had accumulated memory interaction, reveal feedback, runtime memory log, and memory phase handoff routing alongside its top-level gameplay tick order.

This story implements the approved OpenSpec change:

- `openspec/changes/archive/2026-06-06-extract-m0-gameplay-tick-memory-bridge`
- Main synced spec: `openspec/specs/m0-gameplay-tick-memory-bridge/spec.md`
- Evidence: `production/qa/evidence/extract-m0-gameplay-tick-memory-bridge-verification-2026-06-06.md`

The slice is behavior-preserving. It reduces `M0GameplayTickHandler` orchestration mass without changing combat truth, input architecture, MemoryState truth, MemoryInteractionService behavior, scene/prefab wiring, or broad DI strategy.

## Goal

Extract memory-related tick orchestration from `M0GameplayTickHandler` into a narrow `M0MemoryInteractionTickBridge` collaborator while preserving the current M0/M1 memory path:

`Interact -> MemoryInteractionService -> MemoryState -> prompt/reveal feedback/runtime log`

## Acceptance Criteria

- [x] `M0GameplayTickHandler` remains the owner of top-level update order.
- [x] Memory interaction tick routing is moved behind a narrow bridge/collaborator.
- [x] S3-2 `Interact -> MemoryInteractionService -> MemoryState` accepted path remains behavior-equivalent.
- [x] S3-3 interaction prompt placeholder behavior remains behavior-equivalent.
- [x] S3-4 memory reveal feedback placeholder behavior remains behavior-equivalent.
- [x] S4-2 runtime memory log placeholder behavior remains behavior-equivalent.
- [x] Duplicate/spam Interact behavior remains unchanged; no deduplication policy change is introduced.
- [x] `MemoryState` remains reveal/collect truth authority.
- [x] `MemoryInteractionService` remains memory interaction orchestration authority.
- [x] Bridge does not own combat validity, input callbacks, MemoryState acceptance policy, or presentation authority.
- [x] No CombatCore timing/result changes are introduced.
- [x] No input architecture refactor is introduced.
- [x] No `MemoryRaycastProProbe` alignment work is included.
- [x] No scene/prefab changes or broad Nhem DI migration are introduced.
- [x] Focused memory and M0 regression evidence pass.
- [x] Manual PlayMode confirms prompt, Interact accepted, one reveal feedback, one runtime log entry, and no duplicate/spam replay.

## Out of Scope

- CombatCore state-machine refactor
- Combat timing/result changes
- Input architecture refactor
- MemoryState behavior changes
- MemoryInteractionService behavior changes
- MemoryRaycastProProbe alignment
- UI/VFX/Animancer gameplay authority changes
- R3/MessagePipe migration
- Broad Nhem DI migration
- Scene/prefab edits
- Cleanup of duplicate interaction policy

## Implementation Files

- `afterimage-tokyo/Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs`
- `afterimage-tokyo/Assets/_Project/Code/Bootstrap/M0MemoryInteractionTickBridge.cs`
- `afterimage-tokyo/Assets/_Project/Code/Bootstrap/M0MemoryInteractionTickBridge.cs.meta`
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/M1InteractionPromptPlaceholderTests.cs`
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/M1RuntimeMemoryLogPlaceholderTests.cs`

## Verification

Automated evidence:

- `dotnet build afterimage-tokyo/afterimage-tokyo.sln --no-restore`: PASS, exit code 0.
- Unity EditMode focused memory suite: PASS, 18/18.
- Unity EditMode M0 defensive regression: PASS, 23/23.
- `openspec validate extract-m0-gameplay-tick-memory-bridge --strict`: PASS before archive.
- `git diff --check`: PASS.

Manual evidence:

- Eligible fragment shows prompt: PASS.
- Interact accepted path still reaches memory flow: PASS.
- Reveal feedback appears once: PASS.
- Runtime memory log appends one entry: PASS.
- Spam Interact does not add/replay incorrectly: PASS.

Evidence file:

- `production/qa/evidence/extract-m0-gameplay-tick-memory-bridge-verification-2026-06-06.md`

## Completion Notes

**Completed**: 2026-06-06
**Criteria**: 16/16 passing
**Deviations**: None
**Test Evidence**: `production/qa/evidence/extract-m0-gameplay-tick-memory-bridge-verification-2026-06-06.md`
**OpenSpec**: `openspec/changes/archive/2026-06-06-extract-m0-gameplay-tick-memory-bridge`
**Code Review**: Skipped in lean mode; focused tests, source guardrails, OpenSpec validation, and manual PlayMode confirmation recorded.
**Next Recommended**: `production/epics/m1-memory-fragment-exploration/story-s4-3-runtime-memory-log-smoke.md`
