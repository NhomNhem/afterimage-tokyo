## Why

Stories 1-1 through 1-5 are complete. Foundation scene, camera-relative movement, lock-on wiring, player attack resolution, and enemy intent telegraph loop are all established. The enemy now cycles through `Idle → Telegraph → Commit → Active → Recovery` with a readable punish window. Combat Core owns combat validity and result truth; Enemy Intent owns telegraph/commit/recovery truth.

The M0 duel loop `read → evade/parry → counter → reveal` cannot be evaluated without player defensive options. Input already has Parry (`Q`/LB), Dodge (`LShift`/A), and Counter (`E`/B) bindings defined in `M0InputActions.inputactions`. `M0InputRouter` already tracks `parryPressed`, `dodgePressed`, and `counterPressed` in its snapshot. `M0CombatCore` already has FSM states for `DodgeStartup`, `DodgeActive`, `DodgeRecovery`, `ParryStartup`, `ParryActive`, `ParryRecovery`, `CounterWindow`, and `CounterActive`. `M0PlayerLocomotion` already exposes `SetRecoveryContext()`. All contract types exist in `M0Contracts.cs` (`DodgeRequestContext`, `DodgeResultContext`, `DodgePhaseContext`, `CounterWindowState`).

What is missing is the routing: `M0DirectPlayerInput` only wires `LightAttack` and `HeavyAttack`; Parry, Dodge, and Counter presses never reach `M0CombatCore`. Parry in `M0CombatCore` unconditionally opens `CounterWindow` without checking whether the enemy is in Active phase with a `ParryEligible` attack. Dodge state transitions in Combat Core never push `RecoveryContext` to `M0PlayerLocomotion`. Without these three wiring steps, the duel loop has no defensive layer, Parry feels arbitrary, Dodge has no locomotion consequence, and the CounterWindow is unreachable through skill.

## What Changes

- `M0DirectPlayerInput` gains `parryAction`, `dodgeAction`, and `counterAction` `InputAction` fields resolved from the `M0InputActions` action map; exposes `ParryPressedThisFrame`, `DodgePressedThisFrame`, `CounterPressedThisFrame` bool accessors — routing to Combat Core is handled by `M0GameplayTickHandler`, not `M0DirectPlayerInput`
- `M0CombatCore` gains a new `ConsumeDefensiveIntent(CombatActionType, EnemyIntentSnapshot)` method; `EnemyIntentSnapshot` is passed as a value struct by the tick handler at the moment of press — no model reference, no `GlassRefrain.Enemy` assembly dependency
- Parry succeeds (opens `CounterWindow`) only when `EnemyIntentSnapshot.State == Active` and `AttackIntent.AttackTags` contains `"ParryEligible"` (or tags list is empty, meaning any attack is parryable)
- Failed Parry does not open `CounterWindow`; `M0CombatCore` still transitions through `ParryStartup → ParryActive → ParryRecovery → Neutral`
- `M0GameplayTickHandler` (or a minimal coordinator) pushes `RecoveryContext` from `M0CombatCore.Snapshot` to `M0PlayerLocomotion.SetRecoveryContext()` each tick when Combat Core is in a dodge/parry recovery state
- `TR-M0-COMBAT-001` GDD pointer in `tr-registry.yaml` corrected from `design/gdd/m0-combat-core-ownership.md` to `design/gdd/combat-core.md`
- No damage, no health mutation, no hit reaction, no Memory VFX trigger, no animation authority, no VFX, no KCC, no NavMesh, no locomotion rewrite

## Capabilities

### New Capabilities

- `defensive-input-routing`: Parry, Dodge, and Counter input presses route to `M0CombatCore` as raw intents via `M0DirectPlayerInput`
- `parry-validation-against-enemy-intent`: `M0CombatCore` validates parry success against read-only `EnemyIntentSnapshot`; `CounterWindow` opens only on a valid parry against an Active + ParryEligible enemy attack
- `dodge-recovery-request`: Dodge state transitions in Combat Core emit `RecoveryContext` to `M0PlayerLocomotion`; locomotion enters recovery state during `DodgeRecovery`

### Modified Capabilities

- `m0-combat-core`: Extended with `ConsumeDefensiveIntent(CombatActionType, EnemyIntentSnapshot)` API; parry validation logic conditional on enemy state; Counter guard added; no ownership change
- `m0-direct-player-input`: Extended with three new input action fields and routing calls; no existing wiring changed

## Impact

- **Code**: `M0DirectPlayerInput` extended with 3 input action fields and `WasPressedThisFrame` accessors; `M0CombatCore` extended with `ConsumeDefensiveIntent(CombatActionType, EnemyIntentSnapshot)` and conditional parry/counter logic; `M0GameplayTickHandler` extended to forward defensive presses (with live enemy snapshot) to Combat Core and to push `combatCore.Snapshot.Recovery` to locomotion each frame
- **APIs**: No new contract types required — `DodgeRequestContext`, `DodgeResultContext`, `CounterWindowState`, `RecoveryContext` all exist in `M0Contracts.cs`
- **Assembly boundaries**: `GlassRefrain.Combat` gains no new assembly reference — `EnemyIntentSnapshot` is a value struct in `GlassRefrain.Core` passed as a parameter; `Combat → Enemy` dependency is explicitly avoided (design.md Decision 1)
- **Dependencies**: Depends on Stories 1-1 through 1-5 (all Complete); depends on `M0CombatCore` FSM (already compiled); depends on `M0EnemyIntentModel` live loop (Story 1-5 complete)
- **Systems**: Enemy Intent remains truth owner (read-only from Combat); Combat Core gains parry validation authority; Locomotion gains dodge recovery expression; Input emits raw intents only
