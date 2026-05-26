## Why

Memory reveals are core combat mechanics that must provide clear visual feedback to the player about enemy state and actions. To build a complete M0 reveal system, we need a dedicated VFX response subsystem that reacts to Memory State decisions (accept/reject/ignore) and manages the visual timeline of reveals without interfering with combat feedback, enemy readability, or player agency.

## What Changes

- New M0Contracts abstraction layer for VFX response that enforces ownership boundaries
- Memory VFX Response state machine with five distinct states: idle, requested, playing, cooldown, rejected/ignored
- Read-only snapshot API for debug overlay and observer-friendly consumption patterns
- Full unit test coverage for state transitions, lifecycle, and snapshot consistency
- Clear separation of concerns: Memory State owns acceptance, VFX Response owns timing and presentation

## Capabilities

### New Capabilities
- `memory-vfx-response`: State model for Memory reveals VFX response. Manages state lifecycle (idle → requested → playing → cooldown), snapshot reads, and state transition validation. Enforces that VFX only plays after accepted Memory State context.
- `memory-vfx-response-observer`: Observer-friendly read-only API for Memory VFX Response state, enabling safe consumption by Debug Overlay and other systems without mutation risk.

### Modified Capabilities
<!-- No existing capabilities have requirement changes for this phase -->

## Impact

- **Code**: New `Assets/_Project/Code/Memory/M0MemoryVFXResponse.cs` subsystem
- **Contracts**: Extends `Assets/_Project/Code/Core/M0Contracts.cs` with VFX response contract definitions
- **Dependencies**: Reads from `M0MemoryState` context (owned by Memory State); owned by M0 bootstrap composition
- **Tests**: Full spec coverage in `Assets/_Project/Tests/Core/Memory/M0MemoryVFXResponseTests.cs`
- **APIs**: Read-only snapshot observer pattern for safe external access
