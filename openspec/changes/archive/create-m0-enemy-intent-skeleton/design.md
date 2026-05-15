## Context

M0 already has input, locomotion, target context, and combat core skeletons, but enemy-side readability truth still needs a dedicated owner. `Enemy Intent & Telegraph` must own telegraph, commitment, active/recovery timing, attack tags, and `EnemyPunishWindow` context without leaking into Combat Core truth, movement truth, or damage truth.

This change is a skeleton only: enemy intent state model, telegraph snapshot placeholder, basic attack intent placeholder, enemy attack tags, punish-window placeholder, read-only enemy intent snapshot, and tests. It intentionally defers real AI, navigation, hitbox, animation, and damage behavior.

## Goals / Non-Goals

**Goals:**
- Establish Enemy Intent & Telegraph as authority for enemy telegraph and commitment truth.
- Define a pure C# enemy intent state model for M0 duel readability.
- Define enemy telegraph snapshot placeholder for read-phase observation.
- Define basic attack intent placeholder and enemy attack tag representation.
- Define `EnemyPunishWindow` context placeholder owned by Enemy Intent.
- Expose read-only enemy intent snapshot for Debug Overlay and downstream observers.
- Add edit-mode tests for idle/telegraph/commit/active/recovery/punish-window snapshot behavior.
- Keep `M0Contracts.cs` as contracts-only, no behavior logic.

**Non-Goals:**
- Real enemy AI movement or behavior trees.
- NavMesh pathing.
- Animation controller or animation-event dependency.
- Hitbox logic.
- Damage application or health mutation.
- Player tracking behavior.
- Scene/prefab wiring.
- Boss behavior.
- Multi-enemy behavior.
- Final telegraph VFX/audio.
- Legacy Input Manager support or generated DI APIs.

## Decisions

### 1. Keep enemy readability truth in a pure C# state owner

**Decision:** Model Enemy Intent as a small pure C# FSM/service that owns enemy-side intent phases and publishes read-only snapshots.

**Why:** M0 needs enemy-side truth that is inspectable and decoupled from animation/presentation systems.

**Alternatives considered:**
- Fold telegraph truth into Combat Core
  - rejected because Combat Core owns player combat request/result truth, not enemy telegraph truth
- Fold intent truth into Animator states
  - rejected because Animator remains presentation-only and non-authoritative

### 2. Treat enemy telegraph and attack intent as contract-first placeholders

**Decision:** Represent telegraph and basic attack intent using contract placeholders and snapshot fields without full AI behavior.

**Why:** Downstream systems need stable shape ownership before behavior complexity is introduced.

**Alternatives considered:**
- Implement full enemy attack decision logic now
  - rejected because it violates M0 skeleton scope
- Omit telegraph/intent contracts until later
  - rejected because Debug and Combat integration boundaries need explicit contract ownership now

### 3. Keep `EnemyPunishWindow` owned by Enemy Intent, not Combat Core

**Decision:** Define and emit a placeholder punish-window context in Enemy Intent state transitions.

**Why:** Enemy punishability is enemy-side readability/consequence of enemy commitment and recovery phases.

**Alternatives considered:**
- Let Combat Core own punish window
  - rejected because Combat Core should not own enemy telegraph/commit/recovery truth

### 4. Keep ownership boundaries explicit across systems

**Decision:** Enemy Intent publishes read-only snapshot/context only; it does not mutate Combat Core, Health, Target, or Locomotion authorities.

**Why:** Prevents god-system creep and protects architecture ownership split.

**Alternatives considered:**
- Couple enemy state transitions directly to damage and movement systems
  - rejected because Health owns damage/hit reaction consequence and Locomotion owns movement truth

### 5. Keep debug consumption read-only

**Decision:** Enemy intent snapshot is immutable data for Debug Overlay.

**Why:** Debug Overlay is observer-only and must not mutate gameplay authority.

**Alternatives considered:**
- Expose mutable debug control surface from enemy model
  - rejected for authority leakage risk

## Risks / Trade-offs

- [Enemy intent scope creeps into full AI] → Keep state machine limited to M0 duel readability phases.
- [Combat Core starts owning enemy readability truth] → Keep enemy telegraph/punish contracts in Enemy domain.
- [Contracts file becomes behavior host] → Keep all logic in Enemy module; contracts remain data-only.
- [Debug snapshot becomes secondary authority] → Derive snapshot strictly from Enemy Intent current state.
- [Hidden coupling to animation/hitbox/nav systems] → Explicitly forbid these dependencies in this change.

## Migration Plan

1. Review architecture and GDD boundaries for Enemy Intent, Combat Core, Health, Debug, Target, and Locomotion ownership.
2. Define or refine enemy intent contract shapes in `M0Contracts.cs` (state enum/snapshot/attack intent/tag/punish window placeholders only).
3. Implement pure C# `M0EnemyIntent` skeleton in Enemy module with idle/telegraph/commit/active/recovery flow.
4. Implement placeholder state-transition methods that emit read-only snapshots.
5. Wire `EnemyPunishWindow` placeholder open/close through enemy-side transitions.
6. Add edit-mode tests for state and snapshot behavior (idle/telegraph/commit/active/recovery/punish-window).
7. Run checks for forbidden dependencies (legacy input, generated DI, animation/nav/hitbox/damage coupling).
8. Update OpenSpec tasks checklist after verification.

Rollback strategy:
- Remove Enemy Intent skeleton and revert added enemy-intent contract surface if ownership boundaries are violated.

## Open Questions

- Should M0 enemy tags include only `DodgePunishable` and `ParryEligible`, or also optional placeholders like `CounterOnWhiff` now?
- Should punish-window source labels distinguish telegraph-break vs whiff vs parry-response in this skeleton pass?
- Should enemy snapshot include last transition reason string now or defer to a later debug refinement change?
