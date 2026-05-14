## Why

M0 needs a clean input-routing layer that turns Unity New Input System actions into raw, read-only intent snapshots without letting input code become gameplay authority. This is needed now so downstream combat, locomotion, targeting, camera, and debug work can consume a stable contract instead of improvising input interpretation later.

## What Changes

- Define the M0 input intent contract for raw input snapshots and downstream events.
- Confirm the M0 gameplay action set and routing boundaries for Unity New Input System only.
- Add a lightweight input router/facade if needed to centralize source-to-intent translation.
- Preserve input enable/disable state and downstream rejection reporting without moving validation into Input Mapping.
- Expose raw input snapshot data for future Debug Overlay consumption.
- Keep all input-source code under `Assets/_Project/Code/Input`.
- Keep shared input contracts under `Assets/_Project/Code/Core`.

## Capabilities

### New Capabilities
- `m0-input-intent-routing`: Routes Unity New Input System actions into read-only/raw M0 input intent snapshots and events, preserving enable/disable state and downstream routing outcomes.

### Modified Capabilities

- None.

## Impact

- `Assets/_Project/Code/Input`
- `Assets/_Project/Code/Core`
- `Assets/_Project/Content/Data/Input/M0InputActions.inputactions`
- M0 input routing contracts, snapshots, and events
- Future Debug Overlay input visibility
- Downstream consumer boundaries for locomotion, combat, targeting, and camera systems
