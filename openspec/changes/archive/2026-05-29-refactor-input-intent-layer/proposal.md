## Why

Current M0 input wiring mixes Unity InputAction reading and gameplay-side routing inside one path, creating a SOLID bottleneck and increasing regression risk while S3-2 Memory Fragment Interaction (Interact path) is still evolving. We need a behavior-preserving refactor now to separate Unity callback concerns from gameplay-facing intent publication without moving gameplay truth into Input.

## What Changes

- Refactor input architecture into two layers:
  - Unity Input Adapter layer for InputAction callback binding/state capture only.
  - Gameplay Input Intent layer for raw intent snapshot/event publication.
- Keep Unity New Input System as the only gameplay input source.
- Preserve current routing behavior for supported actions: Move, LightAttack, HeavyAttack (if present), Dodge, Parry, Counter, LockOn, Interact.
- Keep LastInput or equivalent debug/evidence visibility for smoke and regression validation.
- Keep ownership boundaries unchanged: Combat/Locomotion/Target/Memory systems remain gameplay truth owners.

## Non-goals

- No combat timing/result changes.
- No dodge/locomotion behavior changes.
- No lock-on behavior changes.
- No memory reveal/collect behavior changes.
- No camera/enemy/animation/VFX/UI changes.
- No R3/MessagePipe migration in this change.
- No generated DI migration.
- No input rebinding UI or profile/save input settings.

## Capabilities

### New Capabilities
- `input-intent-layer`: Behavior-preserving two-layer Input architecture that keeps Input raw-intent-only and publishes gameplay-facing intent snapshots/events for existing M0/S3-2 actions.

### Modified Capabilities
- None.

## Impact

- Affected systems:
  - Input architecture and bootstrap wiring in `_Project/Code/Input` and related bootstrap composition.
  - Debug/evidence path exposing latest input.
- No new external dependencies.
- M0 loop impact: should remain behavior-equivalent for read → evade/parry → counter → reveal.
- Ownership boundary impact: Input layer responsibilities become narrower and clearer; gameplay truth ownership remains unchanged.
