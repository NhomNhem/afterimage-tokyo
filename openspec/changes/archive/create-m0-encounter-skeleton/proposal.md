## Why

M0 needs a minimal encounter shell so the first duel can be prepared, started, observed, ended, and reset without turning Encounter Framework into a mission, spawn, or progression system. This gives the prototype a clear lifecycle around the existing combat, enemy, health, target, and memory authorities.

## What Changes

- Add a pure C# encounter lifecycle state model for M0
- Add one-player / one-enemy participant registration and readiness blocker tracking
- Add start, end, fail, abort, and reset request/result shapes
- Add a read-only encounter snapshot for debug and observer use
- Add observe-only completion, fail, and reveal-context surfaces
- Add tests for prepare/ready/start/active/complete/fail/abort/reset behavior

## Capabilities

### New Capabilities
- `encounter-framework`: Minimal M0 encounter lifecycle shell with participant registration, readiness, start/end/reset, and read-only snapshot support.

### Modified Capabilities
- None

## Impact

- New encounter lifecycle contracts and state model in `Assets/_Project/Code/Core/M0Contracts.cs`
- New encounter runtime model under `Assets/_Project/Code/Encounter`
- Test coverage for lifecycle transitions and readiness/debug visibility
- Read-only observation of combat, enemy, health, target, and memory state without taking ownership from those systems
