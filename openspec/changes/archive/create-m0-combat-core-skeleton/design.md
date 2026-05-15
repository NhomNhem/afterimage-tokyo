## Context

M0 already has the raw input contract, locomotion skeleton, and target context skeleton in place, but combat truth still needs a minimal dedicated owner so the duel can resolve actions fairly. `Combat Core` must stay narrower than a full RPG combat framework and avoid becoming a movement, camera, or memory authority layer.

This change is a skeleton only: combat state model, action request shapes, action result shapes, action lock/recovery request context, CounterWindow placeholder, reveal request context placeholder, read-only combat snapshot, and test coverage. It must remain compatible with the existing M0 contract style and keep full validation behavior deferred.

## Goals / Non-Goals

**Goals:**
- Establish Combat Core as the authority for combat validation and result truth.
- Define pure C# combat state model with the GDD-specified states.
- Define combat action request and result contract shapes.
- Define action lock/recovery request context for Player Locomotion consumption.
- Define CounterWindow placeholder state.
- Define RevealRequestContext placeholder for Memory State consumption.
- Expose read-only M0CombatSnapshot for Debug Overlay and downstream observers.
- Create edit-mode tests for basic request/result/snapshot behavior.

**Non-Goals:**
- Real attack hitbox logic.
- Animation events or Animator integration.
- Enemy AI or enemy behavior.
- Damage application or health changes.
- Parry timing tuning.
- Dodge timing tuning.
- Counter attack implementation.
- Memory State reveal acceptance/rejection.
- VFX/audio/camera feedback.
- Scene/prefab wiring.
- Legacy Input Manager support or generated DI APIs.

## Decisions

### 1. Keep combat truth as a pure C# state owner

**Decision:** Model Combat Core as a small FSM/service with explicit state, action request/result contracts, and snapshot output rather than as Animator logic or a generic ability framework.

**Why:** The architecture says combat truth belongs in `Combat Core`, and the combat layer needs to be independently inspectable by Locomotion, Camera, Debug, and Memory systems.

**Alternatives considered:**
- Fold combat truth into Animator state machine
  - rejected because Animator must remain presentation-only
- Fold combat truth into a generic ability system
  - rejected because M0 needs specific combat state, not a broad framework
- Fold combat truth into Player Locomotion
  - rejected because Locomotion owns movement truth, not combat validity

### 2. Treat combat action requests as validated contracts

**Decision:** Combat Core consumes typed action requests (LightAttack, HeavyAttack, Dodge, Parry, Counter) from Input Mapping via the contract layer, validates them against current combat state, and emits accepted/rejected results.

**Why:** Input must remain a raw intent source. Combat validity and timing are Combat Core's responsibility.

**Alternatives considered:**
- Let Input decide combat validity
  - rejected because it would move gameplay authority into input
- Let Locomotion decide action validity
  - rejected because Locomotion owns movement, not combat rules

### 3. Keep CounterWindow and RevealRequestContext as placeholders

**Decision:** Represent CounterWindow as a state with open/closed/source/duration fields and RevealRequestContext as a request shape with combat result source, but defer full validation behavior (e.g., CounterWindow eligibility rules, RevealRequest acceptance/rejection).

**Why:** Downstream systems (Enemy Intent, Memory State) need to observe these shapes, but the skeleton shouldn't implement complete validation logic yet.

**Alternatives considered:**
- Implement full CounterWindow validation rules now
  - rejected because it would blur scope and commit to tuning before the skeleton is proven
- Omit CounterWindow and RevealRequestContext entirely
  - rejected because downstream skeletons (Memory State, Enemy Intent) need the contract shape

### 4. Action lock/recovery context bridges Combat Core and Player Locomotion

**Decision:** Combat Core emits ActionLockContext and RecoveryContext as request data. Player Locomotion owns movement-side expression of those locks and recovery states.

**Why:** Combat Core knows when an action should lock movement or enter recovery. Player Locomotion owns movement truth. The contract shape prevents each system from creating its own conflicting lock interpretation.

**Alternatives considered:**
- Let Combat Core directly control movement
  - rejected because movement truth belongs to Player Locomotion
- Let Player Locomotion infer locks from combat state
  - rejected because it would create hidden ownership and timing ambiguity

### 5. Expose read-only combat snapshot for Debug Overlay

**Decision:** Represent current combat state, last action result, CounterWindow state, and active lock/recovery context as a read-only snapshot struct.

**Why:** Debug Overlay and other downstream observers need inspectable combat truth without being able to mutate Combat Core state.

**Alternatives considered:**
- Expose Combat Core internals directly
  - rejected because it breaks encapsulation and invites accidental mutation
- Omit snapshot until later
  - rejected because debug visibility is required from the skeleton stage

## Risks / Trade-offs

- [Combat scope creeps toward full action RPG framework] → Keep the state model limited to M0 states and defer broad ability/stat frameworks.
- [Animator starts owning combat truth] → Keep Animator adapters as observers only; Pure C# FSM remains authoritative.
- [Action lock/recovery boundary becomes ambiguous] → Combat Core emits request context; Player Locomotion owns movement expression — enforce the split in code review.
- [CounterWindow placeholder becomes permanent] → The placeholder is explicitly temporary; a follow-up change implements full validation rules.
- [RevealRequestContext creates false expectations] → Clearly mark it as placeholder in code and docs; Memory State still owns acceptance/rejection.
- [Debug snapshot becomes a second authority] → Derive it from combat state only and keep it read-only.

## Migration Plan

1. Inspect the current M0 contracts and architecture boundaries.
2. Define or refine CombatActionType, CombatActionRequest, and CombatActionResult contracts in the Core contract layer.
3. Define ActionLockContext, RecoveryContext, CounterWindowState, and RevealRequestContext in the Core contract layer.
4. Define M0CombatSnapshot for read-only debug/observer consumption.
5. Implement the pure C# Combat Core FSM/service skeleton with all M0 states.
6. Wire action request intake and result emission (validation shape only — no full validation logic).
7. Expose read-only combat snapshot for downstream observers.
8. Add edit-mode tests for basic request/result/snapshot behavior.
9. Validate that no legacy input, no Animator-as-authority patterns, and no generated DI references were introduced.

Rollback strategy:
- Remove the Combat Core skeleton and restore prior contract surface if the state model proves too broad for M0 or conflicts with downstream skeletons.

## Open Questions

- Should CounterWindow source distinguish dodge-opened vs parry-opened vs enemy-punish-opened at the skeleton stage, or only after full validation rules are added?
- Should ActionLockContext include a generic lock reason enum now, or remain a simple boolean lock request with source label?
- Should RecoveryContext distinguish action-specific recovery durations or use a generic recovery duration placeholder?
- Should the combat snapshot include a full transition history or only the latest state and last result?
- Should HitReact include a hit-source category placeholder now, or only after Health/Damage/Hit Reaction defines its contract?
