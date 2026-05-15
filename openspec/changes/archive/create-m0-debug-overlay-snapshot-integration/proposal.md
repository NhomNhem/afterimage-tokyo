## Why

M0 needs a single read-only debug surface that can aggregate the duel's key system snapshots without taking ownership of any gameplay truth. This gives designers a way to inspect the first duel across input, locomotion, targeting, combat, enemy intent, health, memory, memory VFX, and encounter flow while preserving each source system's authority.

## What Changes

- Add a pure C# debug snapshot aggregation model for M0
- Add a read-only aggregate snapshot with per-channel debug groups
- Add simple channel visibility/toggle state for developer use
- Surface last accepted/rejected reason data only from source snapshots or explicit context
- Add tests for aggregation, read-only pass-through, channel toggles, and no source mutation

## Capabilities

### New Capabilities
- `debug-overlay-snapshot-integration`: Minimal M0 debug snapshot aggregation and channel grouping for read-only developer visibility.

### Modified Capabilities
- None

## Impact

- `Assets/_Project/Code/Core/M0Contracts.cs` gains debug snapshot contract shapes only
- A new pure C# debug overlay snapshot model is added under `Assets/_Project/Code/DebugOverlay`
- Edit-mode tests cover aggregation, snapshot pass-through, channel toggle state, and source immutability
- Source systems remain the owners of their own state; the overlay only observes read-only snapshots
