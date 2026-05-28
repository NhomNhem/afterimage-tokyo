## Why

Sprint 3 needs a visible player-facing loop beyond M0 duel stabilization.
The project needs a minimal, testable Memory Fragment interaction slice that proves exploration -> interact -> reveal/collect response without expanding into full RPG systems.

## What Changes

- Add a small Memory Fragment interaction capability for M1.
- Introduce static fragment definitions via ScriptableObject for authored fragment metadata.
- Route Interact intent through a clearly owned interaction use-case service (`MemoryInteractionService`) using Nhem DI/VContainer conventions.
- Reuse `MemoryState` as source of truth for accepted/rejected reveal/collect outcomes.
- Provide debug/evidence hooks for nearby fragment, interact press, acceptance, and duplicate handling.
- Allow minimal scene placement/wiring only if required to execute the loop and evidence.

## Capabilities

### New Capabilities
- `memory-fragment-interaction`: Player can interact with eligible Memory Fragments and trigger reveal/collect flow with accepted/rejected outcomes owned by MemoryState.

### Modified Capabilities
- `memory-state`: Extend/clarify requirement coverage for reveal/collect acceptance and duplicate interaction handling in M1 interaction context.

## Impact

- Affected systems:
  - Input intent routing (Interact intent only)
  - New interaction orchestration service (`MemoryInteractionService`)
  - Memory fragment runtime identity/detection boundary
  - MemoryState integration path for reveal/collect request outcome
  - Read-only debug/evidence surfaces
- Affected assets/config:
  - New `MemoryFragmentDefinition` ScriptableObject type for static data/config
  - Potential minimal scene placement/wiring for fragment presence
- Explicitly unaffected:
  - CombatCore logic
  - Enemy lifecycle logic
  - Camera ownership model
  - Save/profile/inventory/progression systems
