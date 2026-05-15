## Why

M0 needs a dedicated target-truth owner now so lock-on, locomotion, camera, combat, and debug can all observe one readable source of target state instead of inferring it differently. This skeleton establishes the minimum target context contract before the first duel systems start depending on it.

## What Changes

- Introduce a minimal M0 target context capability.
- Define pure C# target context state and read-only snapshot contracts.
- Represent focus active/inactive state, acquire/release requests, validity, and direction/context data.
- Consume raw `LockOn` input intent as a request source without letting Input own target truth.
- Expose read-only target snapshot data for future locomotion, camera, combat, and debug consumers.
- Keep target truth in Lock-On / Target Context, not in Input, Camera, Locomotion, Combat, or Animator.

## Capabilities

### New Capabilities
- `m0-target-context-skeleton`: Minimal target-truth state model, focus state, acquire/release request handling, validity, direction/context snapshot, and debug-facing read-only exposure for M0.

### Modified Capabilities
- None.

## Impact

- `Assets/_Project/Code/Core`
- `Assets/_Project/Code/TargetContext` or the project’s existing target-context code area
- `Assets/_Project/Code/Input`
- `Assets/_Project/Tests/EditMode`
- M0 target-truth ownership and downstream observation boundaries
