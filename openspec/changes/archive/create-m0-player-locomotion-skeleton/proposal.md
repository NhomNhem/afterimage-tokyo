## Why

M0 needs a minimal locomotion skeleton now so movement truth has a dedicated owner before combat, camera, and animation work layer on top of it. This creates a stable C# contract for raw movement intent, state snapshots, and recovery/restriction seams without turning input or animation into gameplay authority.

## What Changes

- Introduce a minimal player locomotion capability for M0.
- Define pure C# locomotion state and read-only snapshot contracts.
- Consume raw movement intent as data from the existing input routing layer.
- Add movement restriction and recovery/action-lock context shapes.
- Expose debug-readable locomotion state for future overlay consumption.
- Keep locomotion truth in Player Locomotion, not in Input, Combat, Camera, or Animator.

## Capabilities

### New Capabilities
- `m0-player-locomotion-skeleton`: Minimal player locomotion state model, snapshot surface, input-intent consumption, and restriction/recovery seams for M0.

### Modified Capabilities
- None.

## Impact

- `Assets/_Project/Code/Core`
- `Assets/_Project/Code/PlayerLocomotion` or the project’s existing locomotion code area
- `Assets/_Project/Code/Input`
- `Assets/_Project/Tests/EditMode`
- M0 locomotion state ownership and debug visibility
