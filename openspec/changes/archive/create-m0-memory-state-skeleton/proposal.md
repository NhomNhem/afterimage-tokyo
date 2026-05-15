## Why

M0 needs a dedicated Memory State owner so reveal acceptance and rejection decisions are authoritative, testable, and separated from Combat Core and Health consequence processing. This skeleton is needed now to prevent reveal logic from leaking into adjacent systems as more combat consequences are added.

## What Changes

- Introduce a minimal M0 Memory State skeleton capability.
- Define a pure C# memory state model that covers dormant, requested, accepted, rejected, responding, and cooldown phases.
- Define reveal request acceptance/rejection request-result shapes with readable reason/context placeholders.
- Define reveal response and cooldown state shapes.
- Expose a read-only memory snapshot for Debug Overlay and downstream consumers.
- Add edit-mode tests covering dormant/requested/accepted/rejected/responding/cooldown behavior.
- Preserve ownership boundaries so Combat Core can create reveal request context but cannot accept reveal itself.

## Capabilities

### New Capabilities
- `m0-memory-state-skeleton`: Minimal memory reveal state authority including reveal acceptance/rejection result shaping, response/cooldown state shaping, and read-only snapshot behavior for M0.

### Modified Capabilities
- None. (Combat Core, Health/Damage/Hit Reaction, Player Locomotion, Enemy Intent & Telegraph, and Debug Overlay ownership boundaries remain unchanged.)

## Impact

- `Assets/_Project/Code/Core` (contract shape additions/refinements for memory reveal request/result and snapshot data only)
- `Assets/_Project/Code/Memory` (new pure C# memory state skeleton owner)
- `Assets/_Project/Tests/EditMode` (new memory skeleton behavior coverage)
- M0 boundary enforcement for reveal acceptance ownership vs Combat Core and Health consequence context
