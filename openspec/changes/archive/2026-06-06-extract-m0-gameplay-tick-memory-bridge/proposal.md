## Why

`M0GameplayTickHandler` currently carries mixed orchestration responsibilities, including memory interaction/reveal routing, prompt updates, reveal feedback routing, and runtime memory log fan-out. This increases change risk in the active M0/Sprint 4 memory path. We need a narrow extraction slice from ADR-0001 that reduces orchestration coupling while preserving verified behavior.

## What Changes

- Define a behavior-preserving extraction plan for memory-related orchestration from `M0GameplayTickHandler` into a narrow collaborator (`MemoryInteractionTickBridge` as the preferred implementation name unless apply-time evidence suggests a clearer name).
- Preserve current ownership boundaries:
  - `MemoryState` remains reveal/collect truth authority.
  - `MemoryInteractionService` remains interaction orchestration authority for S3-2.
  - `M0GameplayTickHandler` remains the top-level orchestration owner.
- Require parity evidence for:
  - Interact accepted path (`Interact -> MemoryInteractionService -> MemoryState`)
  - S3-3 interaction prompt placeholder behavior
  - S3-4 memory reveal VFX/audio placeholder behavior
  - S4-2 runtime memory log placeholder behavior
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
  - Prompt/reveal feedback/runtime memory log parity checks
  - M0 regression smoke
  - Console classification and PASS/PARTIAL/FAIL evidence output.
- No intended impact to:
  - CombatCore timing/result behavior
  - Input architecture boundaries
  - MemoryRaycastProProbe alignment
  - Scene/prefab composition
  - Broad Nhem DI migration
  - Animancer/VFX gameplay authority.
