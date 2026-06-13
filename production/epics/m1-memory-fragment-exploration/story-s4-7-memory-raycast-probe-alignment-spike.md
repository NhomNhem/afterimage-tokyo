# Story S4-7: [Debug] MemoryRaycastProProbe Alignment Spike

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: Debug / Memory Evidence
> **Type**: Integration
> **Estimate**: 0.5d
> **Sprint**: Sprint 4
> **Dependencies**: S4-2, `align-memory-raycast-probe-with-interaction-service`
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

S3-2 and later Sprint 4 evidence proved the memory interaction path through `MemoryInteractionService`, but `MemoryRaycastProProbe` could still log collider-only output such as `hitName=None`. That made debug evidence look contradictory even when gameplay interaction succeeded.

This story implements the approved OpenSpec change:

- `openspec/changes/align-memory-raycast-probe-with-interaction-service`
- Evidence: `production/qa/evidence/s4-7-memory-raycast-probe-alignment-verification-2026-06-07.md`

The probe remains debug-only. It now reports service-owned eligibility from `MemoryInteractionService.Snapshot` and labels RaycastPro collider data as supplemental evidence.

## Goal

Align memory debug probe output with the service-owned interaction snapshot so smoke evidence can distinguish gameplay truth from supplemental RaycastPro collider data.

## Acceptance Criteria

- [x] Probe debug output reports service-owned eligibility.
- [x] Probe debug output includes the service-owned nearby fragment id when available.
- [x] Probe output labels RaycastPro detector/collider data as supplemental.
- [x] Missing RaycastPro detector setup does not block gameplay interaction.
- [x] Probe does not execute Interact.
- [x] Probe does not mutate `MemoryState`.
- [x] Probe does not call `MemoryInteractionService` command paths.
- [x] Prompt, reveal feedback, and runtime memory log remain downstream of service/memory truth.
- [x] No broad scene lookup, service locator, resource fallback, or direct Unity debug logging is introduced.
- [x] Focused EditMode memory and guardrail tests pass.
- [x] Manual PlayMode smoke confirms eligible prompt, accepted Interact, one reveal feedback, one runtime log entry, and duplicate/spam safety.

## Out of Scope

- MemoryInteractionService behavior changes
- MemoryState acceptance/rejection policy changes
- Input architecture refactor
- Prompt, reveal feedback, or runtime memory log feature expansion
- CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, or camera changes
- R3 or MessagePipe migration
- Scene or prefab changes

## Implementation Files

- `afterimage-tokyo/Assets/_Project/Code/Memory/MemoryRaycastProProbe.cs`
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/MemoryRaycastProProbeAlignmentTests.cs`
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/MemoryRaycastProProbeAlignmentTests.cs.meta`

## Verification

Automated evidence:

- Unity EditMode baseline: `MemoryInteractionServiceTests` PASS, 3/3.
- Unity EditMode focused memory suite: PASS, 22/22.
- Unity EditMode scene composition suite: PASS, 19/19.
- `openspec validate align-memory-raycast-probe-with-interaction-service --strict`: PASS.

Manual evidence:

- Tester confirmed all five PlayMode smoke steps PASS.

Evidence file:

- `production/qa/evidence/s4-7-memory-raycast-probe-alignment-verification-2026-06-07.md`

## Completion Notes

**Completed**: 2026-06-07
**Criteria**: 11/11 passing
**Deviations**: Working tree had pre-existing unrelated dirty submodule files before this implementation.
**Test Evidence**: `production/qa/evidence/s4-7-memory-raycast-probe-alignment-verification-2026-06-07.md`
**OpenSpec**: `openspec/changes/align-memory-raycast-probe-with-interaction-service`
**Next Recommended**: Archive the OpenSpec change after approval.
**Sprint 5 Carryover Sync**: 2026-06-12 `/story-done` confirmed the story was already complete and reconciled the Sprint 5 carryover row. Focused Unity MCP EditMode job `dab8fcb2c85643348dcb3045c47d0308` passed 4/4 `MemoryRaycastProProbeAlignmentTests`.
