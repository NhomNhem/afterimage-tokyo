## Context

M0 already has input, locomotion, target context, combat core, and enemy intent skeletons in place, but consequence truth still needs a dedicated owner. `Health / Damage / Hit Reaction` must own health values, damage application, hit reaction classification, and defeat/disabled consequence while remaining strictly separate from combat validity, movement truth, enemy telegraph truth, and memory reveal acceptance.

This change is a skeleton only: health state model, damage request/result contracts, hit reaction context placeholder, defeat/disabled context placeholder, read-only health/reaction snapshot, and test coverage. It must stay contract-compatible with existing M0 skeletons and defer advanced reaction/presentation systems.

## Goals / Non-Goals

**Goals:**
- Establish Health / Damage / Hit Reaction as the authority for consequence truth.
- Define pure C# health state model for M0 consequence phases.
- Define damage application request/result shape with readable outcome context.
- Define hit reaction context placeholder shape.
- Define defeat/disabled context placeholder shape.
- Expose read-only health/reaction snapshot for Debug Overlay and downstream observers.
- Add edit-mode tests for damage request/result, health snapshot, hit reaction placeholder, and defeated state behavior.
- Keep `M0Contracts.cs` as contracts-only (data shapes, no behavior logic).

**Non-Goals:**
- Actual hitbox collision.
- Animation-based hit reactions.
- Ragdoll/physics knockback.
- RPG stats/armor/resistance systems.
- Damage numbers UI.
- Enemy AI changes.
- Combat Core hit validation logic.
- Memory State reveal acceptance/rejection logic.
- Scene/prefab wiring.
- Legacy Input Manager support or generated DI APIs.

## Decisions

### 1. Keep consequence truth in a pure C# health owner

**Decision:** Model Health/Damage/Hit Reaction as a small pure C# FSM/service with explicit health state and consequence snapshots.

**Why:** M0 needs inspectable consequence truth decoupled from presentation systems and combat validation logic.

**Alternatives considered:**
- Fold damage application into Combat Core
  - rejected because Combat Core owns combat validity/result, not consequence application
- Fold reaction truth into Locomotion
  - rejected because Locomotion owns movement expression, not consequence classification

### 2. Treat damage as confirmed-result-driven request/result contracts

**Decision:** Health system consumes damage application requests derived from confirmed combat outcomes and emits accepted/rejected/ignored consequence results.

**Why:** Prevents speculative or presentation-only damage and keeps ownership explicit.

**Alternatives considered:**
- Allow animation/hitbox/presentation to apply damage directly
  - rejected because it creates hidden authority and tuning ambiguity
- Let Enemy Intent apply enemy damage directly
  - rejected because Enemy Intent owns telegraph/commit rhythm, not health truth

### 3. Keep hit reaction classification separate from movement expression

**Decision:** Health system emits hit reaction context classification only; Player Locomotion owns movement-side suppression/recovery expression.

**Why:** Preserves clear boundary between consequence classification and locomotion control behavior.

**Alternatives considered:**
- Drive movement lock/recovery directly from Health model
  - rejected because movement truth belongs to Locomotion

### 4. Keep defeat/disabled consequences explicit but minimal

**Decision:** Represent defeat/disabled as a placeholder consequence context in the health model without implementing full respawn/failure flow.

**Why:** M0 needs clear defeated-state truth without over-scoping full game-loop consequence handling.

**Alternatives considered:**
- Implement full respawn/checkpoint pipeline now
  - rejected because it is outside M0 skeleton scope

### 5. Keep debug consumption read-only

**Decision:** Health/reaction snapshot is immutable data for Debug Overlay and observers.

**Why:** Debug Overlay must remain non-authoritative and non-mutating.

**Alternatives considered:**
- Expose mutable health state through debug channels
  - rejected because it leaks authority and risks accidental behavior coupling

## Risks / Trade-offs

- [Health scope creeps into full stats framework] → Keep model minimal and duel-focused.
- [Combat Core starts applying damage] → Keep Combat Core as provider of confirmed context only.
- [Locomotion ownership blurs] → Emit reaction context only; movement expression remains in Locomotion.
- [Enemy Intent ownership blurs] → Keep enemy telegraph/commit/recovery rhythm in Enemy Intent only.
- [Contracts file becomes behavior host] → Keep behavior in Health module; contracts remain data-only.
- [Debug snapshot becomes second authority] → Derive snapshot from health state only and keep read-only.

## Migration Plan

1. Review architecture and GDD boundaries for Health, Combat Core, Locomotion, Enemy Intent, Memory, and Debug ownership.
2. Define/refine health-state, damage request/result, hit reaction context, defeat/disabled context, and read-only snapshot contracts in `M0Contracts.cs` (shape-only).
3. Implement pure C# `M0HealthDamageReaction` skeleton in Health module.
4. Wire confirmed-result-driven damage request intake and consequence result emission (placeholder validation shape only).
5. Emit hit reaction and defeat/disabled placeholder contexts.
6. Expose read-only health/reaction snapshot for observers.
7. Add edit-mode tests for request/result, snapshot behavior, hit reaction placeholder, and defeated state.
8. Run checks for forbidden dependencies (legacy input, generated DI, hitbox/animation/physics/UI wiring).
9. Update OpenSpec tasks checklist after verification.

Rollback strategy:
- Remove Health skeleton and restore prior contract surface if ownership boundaries are violated or scope expands beyond M0 skeleton intent.

## Open Questions

- Should damage request source labels distinguish player-hit vs enemy-hit at skeleton stage, or stay generic until encounter wiring?
- Should defeated/disabled context include provisional reason enums now, or remain simple string labels?
- Should hit reaction context include severity tiers now, or defer until deeper tuning pass?
