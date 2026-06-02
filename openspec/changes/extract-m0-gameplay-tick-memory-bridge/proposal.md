## Why

`M0GameplayTickHandler` currently carries mixed orchestration responsibilities, including memory interaction/reveal routing, which increases change risk in the active M0/S3-2 path. We need a narrow extraction slice from ADR-0001 that reduces orchestration coupling while preserving verified behavior.

## What Changes

- Define a behavior-preserving extraction plan for memory-related orchestration from `M0GameplayTickHandler` into a narrow collaborator (`MemoryInteractionTickBridge` / `MemoryRevealBridge` naming to be finalized in implementation).
- Preserve current ownership boundaries:
  - `MemoryState` remains reveal/collect truth authority.
  - `MemoryInteractionService` remains interaction orchestration authority for S3-2.
  - `M0GameplayTickHandler` remains the top-level orchestration owner.
- Require parity evidence for:
  - Interact accepted path (`Interact -> MemoryInteractionService -> MemoryState`)
  - Existing duplicate interaction behavior
  - Existing debug/evidence output quality.

## Capabilities

### New Capabilities
- `m0-gameplay-tick-memory-bridge`: Extract memory-related tick orchestration behind a narrow bridge contract while keeping runtime behavior unchanged.

### Modified Capabilities
- None.

## Impact

- Affected runtime area:
  - `Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs`
  - New bootstrap collaborator(s) for memory orchestration.
- Affected verification area:
  - Focused memory interaction tests
  - M0 regression smoke
  - Console classification and PASS/PARTIAL/FAIL evidence output.
- No intended impact to:
  - CombatCore timing/result behavior
  - Input architecture boundaries
  - MemoryRaycastProProbe alignment
  - Scene/prefab composition
  - Animancer/VFX gameplay authority.
