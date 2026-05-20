# Design: Wire M0 Health & Hit Reactions

> **Change ID**: wire-m0-health-hit-reactions
> **Proposal**: proposal.md
> **Date**: 2026-05-16

## Design Overview

This change wires health, damage, and hit reaction consequences for M0 by integrating the existing M0HealthDamageReactionModel skeleton with CombatCore confirmed results, ensuring Health owns health mutation, HitReaction owns reaction/suppression context, enemy stagger is triggered from player hits/counter success, and debug visibility is provided for health and reaction state.

## Architecture Decisions

### 1. Health Damage Application Flow

**Decision**: CombatCore emits confirmed hit/counter result; Health system processes result to apply damage.

**Rationale**: Per ADR-0002, CombatCore owns combat validity/results, Health owns damage/application and consequence truth. Damage must only apply after confirmed result to prevent speculative damage.

**Implementation**:
- CombatCore already emits CombatResolutionResult with HitConfirmed flag
- Health system (M0HealthDamageReactionModel) subscribes to CombatCore result events
- On confirmed hit/counter: call ApplyDamage() with damage amount and source
- ApplyDamage() validates: target not defeated, damage amount > 0
- ApplyDamage() reduces currentHealth, updates state (Living → Damaged → Disabled), emits snapshot change

**Dependencies**: Story 1-4 (Player Attack Resolution) - Complete, Story 1-6 (Parry & Dodge Integration) - Complete

**Guardrails**:
- EnemyIntent must NOT call ApplyDamage directly
- Input must NOT call ApplyDamage directly
- TargetContext must NOT call ApplyDamage directly
- Damage only applied when HitConfirmed == true

### 2. Player Hit Reaction and Control Suppression

**Decision**: Player hit reaction emits movement/control suppression context for M0PlayerLocomotion.

**Rationale**: Per ADR-0002, Locomotion owns movement truth; Health provides reaction context. Control suppression is consequence of hit, not combat validity.

**Implementation**:
- On player hit (ApplyDamage on player health): emit HitReactionContext with:
  - SourceId: enemy identifier
  - ReactionCategory: "HitReact"
  - SuppressionDuration: 0.2-0.5 seconds (configurable)
- M0PlayerLocomotion already has RecoveryContext consumption (from Story 1-6)
- Extend or reuse existing recovery/reaction context pattern:
  - If HitReactionContext is active, locomotion suppresses movement/control
  - Suppression expires after configured duration
  - Return to normal locomotion after suppression ends

**Dependencies**: Story 1-2 (Camera-Relative Movement) - Complete, Story 1-6 (Parry & Dodge Integration) - Complete

**Guardrails**:
- Hit reaction does NOT decide combat validity
- Locomotion owns movement expression; Health provides context only
- No animation/root motion authority (reaction is gameplay state, not clip-driven)

### 3. Enemy Hit Reaction / Stagger

**Decision**: Enemy hit reaction or stagger is triggered by player LightAttack/HeavyAttack hit or Counter success.

**Rationale**: Per GDD, enemy reaction communicates interruption and supports counter/readability. Stagger is consequence of confirmed player hit.

**Implementation**:
- Create or enhance enemy health model (separate instance of M0HealthDamageReactionModel for enemy)
- On enemy hit (ApplyDamage on enemy health): emit EnemyStaggerContext with:
  - SourceId: player identifier
  - StaggerCategory: "Stagger" or "CounterStagger" (stronger on counter)
  - StaggerDuration: 0.3-0.5 seconds (configurable)
- Enemy Intent & Telegraph system may observe stagger state to pause telegraph/commit cycles (optional, if already supported)
- Stagger is simple state/context; does NOT open CounterWindow (CombatCore owns CounterWindow)

**Dependencies**: Story 1-5 (Enemy Intent & Telegraph Loop) - Complete

**Guardrails**:
- Enemy stagger does NOT open CounterWindow
- Enemy stagger does NOT decide reveal validity
- Enemy Intent owns telegraph/commit/recovery; stagger is consequence context only

### 4. Health State Model

**Decision**: Use existing M0HealthDamageReactionModel skeleton with simple numeric health model.

**Rationale**: Skeleton already exists with HealthState (Living, Damaged, Recovering, Disabled), DamageApplicationResult, HitReactionContext, DefeatStateContext. Enhance if needed for M0 scope.

**Implementation**:
- Verify M0HealthDamageReactionModel has required fields:
  - maxHealth (float, e.g., 100)
  - currentHealth (float)
  - state (HealthState enum)
  - lastDamageResult (DamageApplicationResult)
  - hitReaction (HitReactionContext)
  - defeat (DefeatStateContext)
  - latestSnapshot (HealthStateSnapshot)
- If skeleton is incomplete, add missing fields
- Create separate instances: playerHealthModel, enemyHealthModel
- Configure initial health values (tuning data, can be constants for M0)

**Dependencies**: None (skeleton exists)

**Guardrails**:
- Health state truth in Pure C# model, not MonoBehaviour
- No gameplay truth in Unity components

### 5. Debug Visibility

**Decision**: Debug overlay exposes current/max health, hit reaction state, suppression reason, defeated state.

**Rationale**: Per ADR-0003, presentation and debug are read-only. Debug visibility enables prototype tuning without console logs.

**Implementation**:
- Extend existing debug overlay (M0CombatDebugOverlayAdapter) or create separate health debug adapter
- Subscribe to HealthStateSnapshot events from playerHealthModel and enemyHealthModel
- Display read-only labels:
  - Player Health: "Health: 90/100"
  - Enemy Health: "Health: 80/100"
  - Player Reaction: "Reaction: HitReact (0.2s)" or "Reaction: None"
  - Suppression: "Suppressed: Yes (HitReact)" or "Suppressed: No"
  - Enemy Stagger: "Stagger: Yes (0.3s)" or "Stagger: No"
  - Player Defeated: "Defeated: No" or "Defeated: Yes"
  - Enemy Defeated: "Defeated: No" or "Defeated: Yes"

**Dependencies**: Optional: create-m0-playable-combat-prototype-scene (if complete, extend existing debug overlay)

**Guardrails**:
- Debug overlay is read-only; does not mutate health state
- No gameplay truth stored in UI components

### 6. VContainer Registration

**Decision**: Manual VContainer registration for health models and adapters.

**Rationale**: Per ADR-0004, manual VContainer composition only. No automatic scanning or code generation.

**Implementation**:
- Register playerHealthModel as singleton or scoped service in Bootstrap
- Register enemyHealthModel as singleton or scoped service
- If visual/debug adapters require DI, register manually
- Verify registration follows existing pattern from Story 1-1

**Dependencies**: Story 1-1 (Foundation Scene & VContainer Wiring) - Complete

**Guardrails**:
- No generated DI
- No automatic scanning
- Manual registration only

### 7. Damage Amount Configuration

**Decision**: Use simple constants for M0 damage amounts.

**Rationale**: M0 is prototype; exact values are tuning data. Avoid overbuilding damage formula framework.

**Implementation**:
- Define constants or ScriptableObject for tuning:
  - LightAttackDamage: 10
  - HeavyAttackDamage: 20
  - CounterDamage: 25 (if counter applies damage, or stronger reaction)
- Damage amounts are applied by Health system based on CombatCore result type
- CombatCore result includes ActionType (LightAttack, HeavyAttack, Counter); Health maps to damage amount

**Dependencies**: Story 1-4 (Player Attack Resolution) - Complete

**Guardrails**:
- No RPG stat system
- No armor/resistance
- No damage scaling formula

## Assembly Boundaries

### GlassRefrain.Health (New or Extended)
- **Purpose**: Health damage application and consequence truth
- **Dependencies**: GlassRefrain.Core (for snapshot contracts)
- **Forbidden**: Must NOT depend on GlassRefrain.Input, GlassRefrain.Enemy, GlassRefrain.Combat directly
- **Pattern**: Subscribe to CombatCore result events; apply damage; emit health snapshot

### GlassRefrain.Presentation (Extended if create-m0-playable-combat-prototype-scene complete)
- **Purpose**: Debug overlay for health state
- **Dependencies**: GlassRefrain.Core, GlassRefrain.Health (for health snapshot contracts)
- **Forbidden**: Must NOT mutate health state
- **Pattern**: Subscribe to health snapshot events; render read-only labels

### Existing Assemblies (Unchanged)
- GlassRefrain.Combat: No logic changes (may need to expose result events if not already)
- GlassRefrain.Enemy: No logic changes
- GlassRefrain.Input: No logic changes
- GlassRefrain.Bootstrap: Manual VContainer registration for health models

## Data Flow

```
CombatCore Result (HitConfirmed) → Health.ApplyDamage() → Health State Update → Health Snapshot
Health Snapshot → Debug Overlay → UI Labels
Player HitReactionContext → Locomotion Recovery Context → Movement Suppression
Enemy StaggerContext → Enemy Intent (optional) → Telegraph/Commit Pause
```

## Forbidden Patterns

- No FindObjectOfType, FindFirstObjectByType, GameObject.Find
- No Resources.Load
- No legacy Input Manager (Keyboard.current, Mouse.current, Gamepad.current polling)
- No gameplay truth storage in MonoBehaviours
- No animation/root motion authority (Animancer/Animator state as gameplay truth)
- No KCC
- No NavMesh
- No RPG stats, armor, resistance
- No status effects
- No loot/XP
- No Memory Reveal / Memory VFX
- No generated DI
- No Asset Store package modifications
- EnemyIntent must NOT call ApplyDamage
- Input must NOT call ApplyDamage
- TargetContext must NOT call ApplyDamage

## Verification Plan

### EditMode Tests
- Create `Assets/_Project/Tests/EditMode/HealthConsequence_test.cs`
- Test coverage:
  - Damage is not applied without confirmed CombatCore hit result
  - Damage is applied after confirmed LightAttack hit
  - Damage is applied after confirmed HeavyAttack hit
  - Damage is applied after confirmed Counter success
  - Health decreases by expected simple amount
  - Health never goes below zero
  - Defeated/disabled state is set when health reaches zero
  - Player hit reaction creates movement/control suppression context
  - Suppression expires after configured duration
  - Enemy stagger is triggered by player hit
  - Enemy stagger is triggered by counter success
  - EnemyIntent does not directly mutate health
  - Input does not directly mutate health
  - TargetContext does not directly mutate health
  - Debug snapshot exposes current/max health and reaction state
  - Debug/UI access is read-only
  - No MemoryState or MemoryVFX trigger occurs
  - No animation/root motion authority
  - No KCC/NavMesh usage
  - No forbidden APIs

### Manual PlayMode Verification
- Enter PlayMode
- Confirm Player and Enemy visible in Game View
- LightAttack hit on enemy: confirm enemy health decreases
- HeavyAttack hit on enemy: confirm enemy health decreases
- Counter success on enemy: confirm enemy health decreases or stagger triggers
- Enemy hit on player: confirm player health decreases
- Player hit reaction: confirm movement/control suppression visible or debug-visible
- Enemy stagger: confirm stagger visible or debug-visible
- Health current/max visible in debug overlay
- No memory reveal/VFX trigger
- No Console errors
- Verify existing Story 1-6 behavior still works (attacks, parry, dodge, counter, lockOn, enemy intent loop)

## Open Questions

None - scope is clearly defined by GDD and ADRs.

## Alternatives Considered

### Alternative 1: Full RPG Damage Framework
- **Description**: Implement full damage formula with stats, armor, resistance
- **Pros**: Production-ready
- **Cons**: Out of scope for M0; overbuilds prototype
- **Rejection Reason**: M0 is simple duel prototype; RPG stats deferred

### Alternative 2: Animation-Driven Reactions
- **Description**: Use Animancer/Animator clips for hit reaction timing
- **Pros**: Polished visuals
- **Cons**: Animation authority complexity; violates ADR-0002
- **Rejection Reason**: No animation/root motion authority in M0

### Alternative 3: Health in CombatCore
- **Description**: Store health in CombatCore
- **Pros**: Single authority
- **Cons**: Violates ADR-0002 ownership boundaries
- **Rejection Reason**: Health owns consequence truth per ADR-0002

## Impact Assessment

### Positive Impact
- Health/damage consequences are visible and verifiable
- Hit reactions communicate consequence without animation authority
- Debug visibility enables prototype tuning
- Foundation for future Story 1-8 (Encounter reset)

### Negative Impact
- Adds health system complexity (minimal scope for M0)
- Requires manual VContainer registration

### Neutral Impact
- No performance impact (simple numeric operations)
- No gameplay logic changes to existing systems (Health is new layer)

## Rollback Plan

If health system causes issues:
- Remove or disable health model registrations in VContainer
- Remove or disable result event subscriptions
- Scene changes can be reverted by restoring scene backup

No gameplay logic changes to existing systems, so rollback is safe.
