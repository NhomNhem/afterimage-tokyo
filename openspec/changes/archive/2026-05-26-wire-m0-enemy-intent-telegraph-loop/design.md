## Context

Stories 1-1 through 1-4 are complete, establishing:
- Foundation scene and VContainer wiring (Story 1-1)
- Camera-relative movement; Locomotion owns movement truth (Story 1-2)
- Lock-On wiring; Target Context owns target truth (Story 1-3)
- Player attack resolution; Combat Core owns combat validity and result truth (Story 1-4)

`M0EnemyIntentModel` (Pure C# FSM) is compiled, registered in `GameplayLifetimeScope`, and has all state-entry methods and `Tick(dt)` implemented. All enemy intent contract types exist in `M0Contracts.cs` (lines 619–702). The Debug Overlay aggregator already accepts and routes `EnemyIntentSnapshot`. What is missing is the tick driver wiring and a minimal scripted loop driver that exercises the FSM.

**Constraints:**
- ADR-0002: Enemy Intent owns telegraph/commit/recovery truth only; Combat Core owns combat validity/results; Health owns damage/reaction; Target Context owns target truth
- ADR-0003: Enemy intent snapshot is read-only for presentation systems; no mutation from Debug Overlay or camera
- ADR-0004: Manual VContainer registration only; no generated DI
- ADR-0005: `M0Contracts.cs` must remain contracts-only; no new types are needed for this change
- Control Manifest, Core Layer: Pure C# authority; no combat truth in MonoBehaviours; no hidden authorities
- One enemy only (M0 duel scope)
- No damage application, no health mutation, no hit reaction, no parry/dodge integration
- No AI navigation, no NavMesh, no full enemy movement beyond authored position/rotation placeholder
- No animation root motion authority, no VFX, no camera polish, no Memory VFX trigger
- No KCC, no generated DI, no legacy Input Manager, no forbidden Unity object-finding APIs

**Stakeholders:**
- Enemy Intent system owner
- Combat Core system owner (read-only consumer of enemy snapshot)
- Debug Overlay system owner (read-only observer)
- Bootstrap / composition owner

## Goals / Non-Goals

**Goals:**
- Wire `M0GameplayTickHandler` to inject and tick `M0EnemyIntentModel` each frame
- Implement `M0EnemyIntentLoopDriver` as a minimal scripted MonoBehaviour that drives the enemy FSM through its authored duel sequence
- Confirm the Debug Overlay `EnemyIntent` channel receives live snapshot data
- Pass all four Story 1-5 acceptance criteria with EditMode and manual test evidence

**Non-Goals:**
- AI decision-making, utility scoring, behavior trees
- NavMesh, pathfinding, spatial navigation
- Full enemy movement system (enemy stays at authored position or with minimal placeholder movement only)
- Animation system integration or root motion authority
- VFX (particle systems, VFX Graph, shader effects)
- Memory VFX trigger or any Memory State interaction
- Combat Core changes — Combat Core reads the snapshot; this change does not modify Combat Core
- Health/damage/hit reaction (deferred to Story 1-7)
- Parry/dodge integration (deferred to Story 1-6)
- Counter window expansion (deferred to Story 1-6)
- Enemy archetype variety or pattern library
- Boss framework or phase logic
- Generated DI or Nhem attribute usage
- Legacy Input Manager
- FindObjectOfType, FindFirstObjectByType, GameObject.Find, Resources.Load

## Decisions

### Decision 1: Tick driver location — extend `M0GameplayTickHandler`

**Choice:** Inject `M0EnemyIntentModel` into `M0GameplayTickHandler.Construct()` and call `model.Tick(dt)` in `Update()`.

**Rationale:**
- `M0GameplayTickHandler` is already the authoritative frame-tick driver for gameplay systems (locomotion is ticked there today)
- Consistent with established pattern — no new tick orchestrator needed for M0 scope
- `M0EnemyIntentModel` is already registered in `GameplayLifetimeScope`; injection requires one field and one line in `Construct()`
- Alternative: New dedicated `M0EnemyTickDriver` MonoBehaviour — rejected as unnecessary overhead for one new field

### Decision 2: Loop driver as a separate `M0EnemyIntentLoopDriver` MonoBehaviour

**Choice:** Create `M0EnemyIntentLoopDriver` as a dedicated MonoBehaviour that holds authored timing constants and drives state transitions via a coroutine or `Update()` timer sequence.

**Rationale:**
- Separation of concerns: tick driver (timing infrastructure) vs. loop driver (authored duel behavior)
- Loop driver can be replaced, tuned, or extended without touching the tick infrastructure
- Makes authored timing constants Inspector-configurable via `[SerializeField]`
- Alternative: Inline the loop in `M0GameplayTickHandler` — rejected because it conflates infrastructure with authored behavior
- Alternative: Scriptable Object-driven sequence — rejected as over-engineering for M0

**Loop driver sequencing:**
```
Idle (idleDuration) →
Telegraph (telegraphDuration, telegraphId) →
Commit (attackIntentContext, commitDuration) →
Active (activeDuration) →
Recovery (recoveryDuration, openPunishWindow: true, punishWindowSeconds) →
[Idle, repeat]
```
This is a deterministic authored loop — no branching, no decision logic, no AI.

### Decision 3: `EnemyAttackIntentContext` authored inline in loop driver

**Choice:** Loop driver constructs one `EnemyAttackIntentContext` with one `EnemyAttackTagSet` (tags: `DodgePunishable`, `ParryEligible`, `CounterOnWhiff`) at composition time and passes it to `EnterCommit()` each cycle.

**Rationale:**
- M0 needs one enemy with one or two basic attacks (GDD §8)
- Tags exist to communicate defensive option context to Combat Core via read-only snapshot
- Inline construction avoids a separate data file for one prototype enemy
- Alternative: ScriptableObject attack data asset — deferred to post-M0 enemy roster work

### Decision 4: Loop driver wired via scene, injected via VContainer

**Choice:** `M0EnemyIntentLoopDriver` receives `M0EnemyIntentModel` via VContainer `[Inject]`, registered as `RegisterComponent` in `GameplayLifetimeScope`.

**Rationale:**
- Consistent with how `M0TargetableSceneAdapter` is wired (RegisterComponent pattern, Story 1-1)
- Manual DI only per ADR-0004
- Loop driver must be a scene component to run coroutines and reference the `Enemy_M0TargetablePlaceholder` GameObject
- Alternative: Constructor injection in a pure C# class — rejected because the loop driver needs MonoBehaviour lifetime and coroutine support

### Decision 5: No new contract types required

**Choice:** Use existing `M0Contracts.cs` types exclusively. No additions to contracts file.

**Rationale:**
- All six enemy intent types exist: `EnemyIntentState`, `EnemyIntentSnapshot`, `TelegraphStateSnapshot`, `EnemyAttackIntentContext`, `EnemyAttackTagSet`, `EnemyPunishWindowContext`
- This change is wiring, not new type definition
- ADR-0005: contracts hub must not grow without new cross-system contract need
- Alternative: Add `IEnemyIntentLoop` interface — deferred; unnecessary for M0 single-enemy scope

### Decision 6: `EnemyIntentState` enum scope is correct for Story 1-5

**Choice:** Keep the 5-state enum (`Idle`, `Telegraph`, `Commit`, `Active`, `Recovery`) as-is. Do not add `Stagger`, `RevealBeat`, `Defeated` yet.

**Rationale:**
- Story 1-5 scope covers only the core duel rhythm states (GDD §7.2–7.6)
- `Stagger`, `RevealBeat`, `Defeated` require parry/counter/reveal integration (Stories 1-6, 1-7, 1-8)
- Adding states before they are driven would create dead code and scope drift
- Alternative: Add all GDD states now — rejected as premature; state must be reachable and testable

## Risks / Trade-offs

**Risk:** Loop driver timing constants may produce unreadable enemy rhythm on first playtest
**Mitigation:** All timing values are `[SerializeField]` Inspector-configurable; tuning does not require code changes

**Risk:** `M0GameplayTickHandler.Construct()` grows in parameter count as more systems are added
**Mitigation:** Acceptable for M0 scope; post-M0 refactor can introduce a tick registry pattern if needed

**Risk:** Punish window closing from `Tick()` before the player can read it
**Mitigation:** `punishWindowSeconds` is a configurable authored constant, defaulting to a readable duration (≥0.3s); default is longer than test frames

**Risk:** Debug Overlay `EnemyIntent` channel may not show correct data if `M0DebugOverlaySnapshotAggregator.Capture()` is not called with the live snapshot
**Mitigation:** Verify that the aggregator is called with `enemyIntentModel.Snapshot` in the same tick handler that calls `Tick(dt)`; document the call order

**Trade-off:** Scripted deterministic loop vs. authored randomness
**Decision:** Deterministic loop — M0 is proving readability and fairness, not variety; random timing reduces testability and readability

## Migration Plan

No migration required — this wires existing compiled code. No existing system ownership changes.

**Rollback Strategy:**
- Remove `M0EnemyIntentModel` injection from `M0GameplayTickHandler`
- Delete `M0EnemyIntentLoopDriver.cs`
- Remove `RegisterComponent` call for loop driver from `GameplayLifetimeScope`
- Restore `tr-registry.yaml` GDD pointer if needed

## Open Questions

None — scope is narrow and well-defined by Story 1-5 acceptance criteria, readiness report, and GDD §4 M0 scope.
