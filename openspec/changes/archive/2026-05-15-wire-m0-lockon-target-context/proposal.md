# Proposal: Wire M0 Lock-On / Target Context

## Why

Story 1-3 ([Targeting] Lock-On Wiring) requires wiring the Lock-On / Target Context system for the M0 First Playable Duel. The player must be able to intentionally focus the one M0 duel enemy through raw input intent, while maintaining clear architectural boundaries: Target Context owns target truth, Input Mapping emits intent only, and Camera/Locomotion remain read-only consumers.

This change enables the first readable katana duel by providing stable target focus without creating hidden ownership or over-engineered targeting frameworks. It supports the core combat loop (`read → evade/parry → counter → reveal`) by ensuring the player can stay oriented to the duel enemy without the system automating combat outcomes.

## What Changes

- **Input Mapping**: Emits raw `LockOn` intent only; does not select, store, validate, or clear targets.
- **Target Context**: Interprets `LockOn` intent as acquire/release, owns target truth, manages validity/invalidation, and exposes read-only context.
- **Toggle Behavior**: Target Context toggles focus on the single registered M0 enemy (one player, one enemy, one active target max).
- **Invalidation**: Target automatically releases when enemy is unregistered, disabled, defeated, or explicitly released.
- **Read-Only Contracts**: Camera, Locomotion, Combat Core, and Debug Overlay receive read-only target snapshots/context.
- **DI Wiring**: Manual VContainer registration for Target Context services in `GameplayScope` only.

## Capabilities

### New Capabilities

- `lockon-input-routing`: Input Mapping emits raw `LockOn` intent without target selection or validation
- `target-context-acquisition`: Target Context acquires the single M0 enemy when no active target exists
- `target-context-release`: Target Context releases active target on toggle or invalidation
- `target-context-validation`: Target Context invalidates target when enemy becomes untargetable
- `target-readonly-context`: Target Context exposes read-only target state/direction to consumers
- `target-manual-di`: Manual VContainer wiring for Target Context services

### Modified Capabilities

None. This change introduces new targeting capabilities without modifying existing spec-level requirements.

## Impact

- **Code**: New `Assets/_Project/Code/Targeting/` assembly with Target Context implementation
- **DI**: `GameplayScope` composition root registers Target Context services
- **Tests**: Three EditMode test files for ownership, intent routing, and DI registration
- **Dependencies**: Consumes Input Mapping intent; provides read-only context to Camera/Locomotion
- **M0Contracts**: May add targeting contracts (DTOs, interfaces) if needed for cross-system communication

## Hard Exclusions (Enforced)

- No multi-target cycling
- No boss-part targeting
- No aim assist
- No range/visibility/priority scoring
- No combat validity (attack/hit/parry/dodge/counter)
- No animation/root motion
- No locomotion rewrite
- No camera-owned targeting
- No generated DI (VContainer.SourceGenerator)
- No legacy Input Manager
- No hardcoded device polling (`Keyboard.current`, `Mouse.current`, `Gamepad.current`)
- No `FindObjectOfType`, `FindFirstObjectByType`, `GameObject.Find`, `Resources.Load`
