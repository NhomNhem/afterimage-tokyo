## Context

Stories 1-1 through 1-5 are complete, establishing:
- Foundation scene and VContainer wiring (Story 1-1)
- Camera-relative movement; Locomotion owns movement truth (Story 1-2)
- Lock-On wiring; Target Context owns target truth (Story 1-3)
- Player attack resolution; Combat Core owns combat validity and result truth (Story 1-4)
- Enemy Intent telegraph loop; Enemy Intent owns telegraph/commit/recovery truth (Story 1-5)

**What exists today:**
- `M0CombatCore` (Pure C#, `GlassRefrain.Combat`): FSM with `DodgeStartup/Active/Recovery`, `ParryStartup/Active/Recovery`, `CounterWindow`, `CounterActive`. `ConsumeAttackIntent(CombatActionType)` accepts Dodge, Parry, Counter. `OpenCounterWindow()` unconditionally called when `ParryActive` advances — no enemy intent check yet.
- `M0DirectPlayerInput` (MonoBehaviour, `GlassRefrain.Input`): wires `LightAttack` and `HeavyAttack` only. `parryAction`, `dodgeAction`, `counterAction` are absent.
- `M0InputActions.inputactions`: Parry (`Q`/LB), Dodge (`LShift`/A), Counter (`E`/B) bindings exist and are bound.
- `M0PlayerLocomotion` (Pure C#, `GlassRefrain.Locomotion`): exposes `SetRecoveryContext(RecoveryContext)`. Not yet called from Combat Core state changes.
- `M0EnemyIntentModel` (Pure C#, `GlassRefrain.Enemy`): live, ticked each frame, cycles through intent states. `Snapshot` exposes read-only `EnemyIntentSnapshot`.
- `M0Contracts.cs`: all required types exist — `DodgeRequestContext`, `DodgeResultContext`, `DodgePhaseContext`, `CounterWindowState`, `RecoveryContext`, `EnemyIntentSnapshot`, `EnemyIntentState`, `EnemyAttackTagSet`.
- `tr-registry.yaml`: `TR-M0-COMBAT-001` points to non-existent `design/gdd/m0-combat-core-ownership.md`.

**Constraints:**
- ADR-0002: Input emits intent only. Combat Core owns validity/results. Enemy Intent read-only from Combat. Locomotion owns movement expression.
- ADR-0003: Presentation systems must not mutate gameplay state. Debug Overlay is read-only.
- ADR-0004: Manual VContainer registration only. No generated DI.
- ADR-0005: `M0Contracts.cs` is contracts-only. No new types unless a new cross-system contract need arises.
- Control Manifest: No forbidden APIs (`Input.GetKey`, `Keyboard.current`, `FindObjectOfType`, etc.). Pure C# authority. No combat truth in MonoBehaviours.
- One player, one enemy only.
- No health mutation, no damage, no hit reaction, no Memory VFX, no animation authority, no KCC, no NavMesh, no locomotion rewrite.

**Stakeholders:**
- Input system owner (reads intent, emits raw press only)
- Combat Core system owner (owns validity/result truth)
- Enemy Intent system owner (read-only snapshot consumer)
- Locomotion system owner (expresses recovery from Combat Core)
- Bootstrap / composition owner (manual DI wiring)

## Goals / Non-Goals

**Goals:**
- Wire Parry, Dodge, Counter input presses from `M0InputActions` to `M0CombatCore` via `M0DirectPlayerInput`
- Add enemy intent snapshot validation to `M0CombatCore` parry path: `CounterWindow` opens only when `EnemyIntentSnapshot.State == Active` and attack is `ParryEligible`
- Wire `M0CombatCore` dodge/parry recovery state transitions to push `RecoveryContext` to `M0PlayerLocomotion`
- Fix `TR-M0-COMBAT-001` GDD pointer in `tr-registry.yaml`
- Pass all four Story 1-6 acceptance criteria with EditMode and manual test evidence

**Non-Goals:**
- Health mutation, damage application, or hit reaction (Story 1-7)
- Memory reveal runtime trigger (Story 1-10)
- Animation, root motion, or Animator state authority
- VFX, camera polish, or post-processing
- KCC, NavMesh, or full enemy AI
- Locomotion positional dodge impulse (may be added if explicitly in GDD AC-4; see Decision 4)
- Full combat damage result or stat-based resolution
- Enemy AI navigation or pattern switching
- Multiple enemy types
- Generated DI, legacy Input Manager, hardcoded device polling

## Decisions

### Decision 1: Assembly coupling strategy for parry validation

**Problem:** `M0CombatCore` lives in `GlassRefrain.Combat`. `M0EnemyIntentModel` lives in `GlassRefrain.Enemy`. Parry validation needs to read `EnemyIntentSnapshot`. Two options:

**Option A — Snapshot parameter at call-time:**
Add `ConsumeParyIntent(EnemyIntentSnapshot enemySnapshot)` method to `M0CombatCore`. Caller (`M0GameplayTickHandler` or `M0DirectPlayerInput`) passes the current snapshot at the moment of parry. `M0CombatCore` receives only the struct — no reference to `M0EnemyIntentModel` or `GlassRefrain.Enemy`. No new assembly reference required.

**Option B — Model injection:**
Add `SetEnemyIntentModel(M0EnemyIntentModel model)` to `M0CombatCore`. Reads `model.Snapshot` internally at parry validation time. Requires `GlassRefrain.Combat` to reference `GlassRefrain.Enemy`.

**Choice: Option A — snapshot parameter at call-time.**

**Rationale:**
- `GlassRefrain.Combat` currently references only `GlassRefrain.Core` and `GlassRefrain.Targeting`. Adding a reference to `GlassRefrain.Enemy` would create a `Combat → Enemy` dependency that conflicts with ADR-0002's ownership boundary model (Combat Core consumes enemy snapshots, not enemy models).
- `EnemyIntentSnapshot` is already in `GlassRefrain.Core` (via `M0Contracts.cs`). Passing it as a parameter keeps Combat Core's API clean and independently testable.
- The coordinator (`M0DirectPlayerInput` or `M0GameplayTickHandler`) already has access to both `M0CombatCore` and `M0EnemyIntentModel` via injection — passing `enemyIntentModel.Snapshot` at parry-press time is a one-line change.
- Tests can inject arbitrary `EnemyIntentSnapshot` values without needing a live model.

**New method signature:**
```csharp
public CombatActionRequestResult ConsumeDefensiveIntent(
    CombatActionType actionType,
    EnemyIntentSnapshot enemySnapshot)
```
`ConsumeAttackIntent` continues to serve light/heavy attacks (no snapshot needed for attacks). Counter uses same signature but snapshot is advisory (counter is a player-initiated action against an open window, not validated against a new enemy intent frame).

### Decision 2: Where parry validation lives

**Choice:** Parry validation logic lives entirely inside `M0CombatCore.ConsumeDefensiveIntent()`.

**Rationale:**
- ADR-0002: Combat Core owns combat validity and result truth. Moving validation to `M0DirectPlayerInput` would place result truth in an input bridge MonoBehaviour — a violation.
- Coordinator passes snapshot; Core decides. Clean ownership.

**Validation rule:**
```
parry succeeds if:
    enemySnapshot.State == EnemyIntentState.Active
    AND (enemySnapshot.AttackIntent.AttackTags.Tags is empty
         OR enemySnapshot.AttackIntent.AttackTags.Tags contains "ParryEligible")
```
If either condition fails, `CounterWindow` is NOT opened. Combat Core still transitions `ParryStartup → ParryActive → ParryRecovery → Neutral` (the player committed to a parry action), but with no counter opening.

### Decision 3: Where dodge-to-locomotion recovery push lives

**Problem:** `M0CombatCore` transitions to `DodgeRecovery` but never calls `locomotion.SetRecoveryContext()`. `M0PlayerLocomotion` does not know about Combat Core state.

**Choice:** Extend `M0GameplayTickHandler.Update()` to check `combatCore.Snapshot.Recovery` each frame and forward it to `locomotion.SetRecoveryContext()`.

**Rationale:**
- `M0GameplayTickHandler` already holds references to both `M0CombatCore` and `M0PlayerLocomotion` via injection. Adding one forwarding call is minimal.
- Alternative: `M0CombatCore` holds a reference to `M0PlayerLocomotion` and calls `SetRecoveryContext()` directly — rejected because Combat Core should not own locomotion. ADR-0002: "Combat Core does not own movement expression or locomotion truth."
- Alternative: Event subscription (`CombatCore.SnapshotChanged`) — viable but adds event plumbing for one field forward; tick-based forwarding is simpler and consistent with existing tick pattern.

**Forwarding logic (each frame in `M0GameplayTickHandler.Update()`):**
```csharp
if (combatCore != null && locomotion != null)
    locomotion.SetRecoveryContext(combatCore.Snapshot.Recovery);
```
This replaces no existing locomotion recovery logic — `M0PlayerLocomotion.SetRecoveryContext()` already exists and is the intended consumer.

### Decision 4: Dodge displacement — recovery lock only for Story 1-6

**Choice:** Story 1-6 implements recovery lock only (locomotion enters `Recovering` state during `DodgeRecovery`). No positional dodge impulse or directional dash is added in this change.

**Rationale:**
- Story 1-6 AC-4: "Dodge displacement and recovery are expressed in `M0PlayerLocomotion`." The minimum expression is that locomotion acknowledges the recovery phase and restricts translation.
- Positional dodge impulse requires a `DodgeMovementRequest` shape, a direction vector from input, and locomotion impulse logic — this is a locomotion extension beyond the scope of wiring defensive intent.
- Decision deferred to a follow-up story or as an increment within Story 1-6 only if explicitly time-boxed. Not in this OpenSpec.

### Decision 5: Counter input routing scope

**Choice:** Counter input press (`E`/B) routes to `combatCore.ConsumeAttackIntent(CombatActionType.Counter)` (not the new `ConsumeDefensiveIntent`) — Counter does not require enemy snapshot validation at this phase.

**Rationale:**
- Counter is the player's offensive response during an open `CounterWindow`. The window's validity is already tracked inside `M0CombatCore`. Counter input only needs to be accepted/rejected based on whether `CounterWindow.IsOpen` — no external snapshot query required.
- Using `ConsumeAttackIntent` keeps Counter consistent with how attacks are routed. Story 1-6 only needs to wire the input; the FSM handles acceptance.

### Decision 6: No new contract types

**Choice:** Use existing `M0Contracts.cs` types exclusively. No additions.

**Rationale:**
- `DodgeRequestContext`, `DodgeResultContext`, `DodgePhaseContext`, `CounterWindowState`, `RecoveryContext`, `EnemyIntentSnapshot`, `EnemyAttackTagSet` all exist.
- ADR-0005: contracts hub must not grow without a new cross-system contract need. This change is wiring, not new type definition.

### Decision 7: `ConsumeDefensiveIntent` used by `M0DirectPlayerInput`

**Choice:** `M0DirectPlayerInput` calls `combatCore.ConsumeDefensiveIntent(CombatActionType.Parry, enemyIntentModel.Snapshot)` on parry press, `combatCore.ConsumeDefensiveIntent(CombatActionType.Dodge, enemyIntentModel.Snapshot)` on dodge press (snapshot advisory for dodge), and `combatCore.ConsumeAttackIntent(CombatActionType.Counter)` on counter press.

**Consequence:** `M0DirectPlayerInput` must hold a reference to `M0EnemyIntentModel`. This requires adding `SetEnemyIntentModel(M0EnemyIntentModel)` to `M0DirectPlayerInput` and wiring it in `M0GameplayTickHandler.Construct()`. `GlassRefrain.Input` already references `GlassRefrain.Combat` and `GlassRefrain.Core` — must verify it also allows `GlassRefrain.Enemy` reference, or pass snapshot differently.

**Alternative resolution:** `M0GameplayTickHandler.Update()` handles parry press detection itself (checking `directInput.Snapshot.ParryPressed`) and calls `combatCore.ConsumeDefensiveIntent(Parry, enemyIntentModel.Snapshot)`. This keeps enemy model reference in the tick handler only, not in `M0DirectPlayerInput`.

**Final choice: Tick handler handles parry/dodge/counter forwarding.** `M0DirectPlayerInput` gains only the three new `InputAction` field reads (returning `WasPressedThisFrame()` as bools via the existing snapshot approach), and `M0GameplayTickHandler` routes snapshot presses to Combat Core with the enemy snapshot. This avoids adding `GlassRefrain.Enemy` as a reference to `GlassRefrain.Input`.

**Flow:**
```
M0InputActions (Parry/Dodge/Counter bindings)
  → M0DirectPlayerInput (reads WasPressedThisFrame, stores in InputIntentSnapshot)
  → M0GameplayTickHandler.Update() (reads snapshot.ParryPressed etc., passes to combatCore.ConsumeDefensiveIntent with enemyIntentModel.Snapshot)
  → M0CombatCore (validates, transitions state, conditionally opens CounterWindow)
```

## Risks / Trade-offs

**Risk 1 — Combat Core growing in surface area (LOW)**
Adding `ConsumeDefensiveIntent()` to the existing `ConsumeAttackIntent()` adds one public method. The FSM states already exist. Risk of surface area bloat is low for M0 scope.

**Risk 2 — Snapshot staleness at parry-press time (LOW)**
`M0GameplayTickHandler.Update()` reads `enemyIntentModel.Snapshot` at parry-press detection time. The snapshot is refreshed each frame by `enemyIntentModel.Tick(dt)` earlier in the same `Update()` call. Ordering must be: `(1) Tick enemy model → (2) Check defensive input → (3) Forward recovery`. This is the correct call order and is deterministic.

**Risk 3 — Parry window feel (MEDIUM)**
Parry window is currently the entire `ParryActive` state duration. Enemy `Active` state duration is 0.15s (authored in `M0EnemyIntentLoopDriver`). If parry startup is too long, the player will always miss. These are `[SerializeField]` tunable. Final timing requires PlayMode tuning — outside this OpenSpec.

**Risk 4 — Recovery forwarding every frame (LOW)**
Forwarding `combatCore.Snapshot.Recovery` to locomotion every frame even when no dodge/parry is happening is safe — `Recovery.IsRecovering` is false when not in a recovery state, which `M0PlayerLocomotion.ResolveState()` already handles.

**Risk 5 — `GlassRefrain.Input` assembly reference scope (LOW)**
`M0DirectPlayerInput` currently references `GlassRefrain.Combat`, `GlassRefrain.Core`, `GlassRefrain.Locomotion`, `GlassRefrain.Targeting`. Under Decision 7, no new assembly reference is added to Input — snapshot forwarding happens in the tick handler.

## Migration Plan

No migration required — this wires existing compiled code and FSM states. No existing system ownership changes.

**Rollback strategy:**
- Remove parry/dodge/counter input action fields from `M0DirectPlayerInput`
- Remove `ConsumeDefensiveIntent()` from `M0CombatCore` (or guard it)
- Remove recovery forwarding call from `M0GameplayTickHandler`
- Restore unconditional `OpenCounterWindow` in `M0CombatCore.AdvanceState(ParryActive)` if needed

## Open Questions

**OQ-1:** Should dodge acceptance check Combat Core state (i.e., reject if already in `DodgeActive` or `AttackActive`)? Current `RequestAction` already rejects actions in locked states — likely already handled. Verify during implementation.

**OQ-2:** Should Counter input be blocked when `CounterWindow.IsOpen == false`? Current `RequestAction` transitions to `CounterActive` unconditionally when Counter is requested. Story 1-6 may add a guard: reject Counter if `CounterWindow.IsOpen == false`. Mark this as a task item to verify and decide.
