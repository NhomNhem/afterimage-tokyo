## Why

Story 1-3 established that Target Context now owns lock-on target truth, Input emits raw intents only, and Locomotion owns movement truth. Story 1-4 must now wire player light/heavy attack resolution so that Combat Core owns combat validity and result truth, completing the foundational combat authority layer before parry/dodge integration.

## What Changes

- Input emits raw `LightAttack` and `HeavyAttack` intents only (no combat decisions in Input layer)
- Combat Core consumes attack intents and validates whether attack requests can start based on current combat state
- Combat Core distinguishes light attack vs heavy attack requests
- Combat Core resolves placeholder hit/whiff results against read-only Target Context data
- Combat Core exposes read-only combat state/result snapshot for debug and presentation systems
- Combat Core may emit movement restriction/recovery request shapes if supported by skeleton
- Manual VContainer composition for Combat Core registration (ADR-0004 compliance)
- No damage/health mutation in this story (deferred to later stories)
- No parry/dodge integration (deferred to Story 1-6)

## Capabilities

### New Capabilities

- `player-attack-intent-routing`: Input Mapping emits raw LightAttack and HeavyAttack intents without combat decisions
- `combat-attack-validation`: Combat Core validates attack requests against current combat state (e.g., cannot attack while recovering)
- `combat-attack-resolution`: Combat Core resolves placeholder hit/whiff results using read-only Target Context spacing/timing truth
- `combat-state-snapshot`: Combat Core exposes read-only combat state and result snapshot for debug/presentation
- `combat-manual-di`: Manual VContainer registration for Combat Core wiring

### Modified Capabilities

None (no existing spec-level requirement changes)

## Impact

- **Code**: `M0InputRouter` extension for LightAttack/HeavyAttack intent emission, `M0CombatCore` implementation for validation and resolution, `M0Contracts.cs` additions for combat intent/result contracts
- **APIs**: New combat intent contracts (LightAttackIntent, HeavyAttackIntent, CombatResultSnapshot), read-only combat state snapshot interface
- **Dependencies**: Depends on Input Mapping (Story 1-1), Locomotion (Story 1-2), Target Context (Story 1-3) — all Complete
- **Systems**: Combat Core becomes the authoritative combat validity and result truth owner per ADR-0002
