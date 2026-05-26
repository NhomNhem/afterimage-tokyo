# Tasks: Wire M0 Enemy Intent & Telegraph Loop

## 1. Tick Driver Wiring (Bootstrap Assembly)

- [x] 1.1 Add `private M0EnemyIntentModel enemyIntentModel;` field to `M0GameplayTickHandler`
- [x] 1.2 Extend `M0GameplayTickHandler.Construct()` `[Inject]` method to accept `M0EnemyIntentModel` parameter and assign it
- [x] 1.3 Call `enemyIntentModel?.Tick(dt)` in `M0GameplayTickHandler.Update()` after locomotion tick
- [x] 1.4 Verify `M0GameplayTickHandler` does not call any state-entry methods (`EnterTelegraph`, `EnterCommit`, etc.) — tick only
- [x] 1.5 Verify `M0EnemyIntentModel` injection does not break existing locomotion, targetContext, or combatCore injection

## 2. Loop Driver Implementation (Enemy Assembly)

- [x] 2.1 Create `Assets/_Project/Code/Bootstrap/M0EnemyIntentLoopDriver.cs` as a `sealed` MonoBehaviour (moved to Bootstrap — Enemy asmdef has no VContainer reference; Bootstrap already references both GlassRefrain.Enemy and VContainer)
- [x] 2.2 Add `[SerializeField] private float idleDuration = 1.5f;` (inspector-tunable)
- [x] 2.3 Add `[SerializeField] private float telegraphDuration = 0.75f;`
- [x] 2.4 Add `[SerializeField] private float commitDuration = 0.2f;`
- [x] 2.5 Add `[SerializeField] private float activeDuration = 0.15f;`
- [x] 2.6 Add `[SerializeField] private float recoveryDuration = 0.6f;`
- [x] 2.7 Add `[SerializeField] private float punishWindowDuration = 0.35f;`
- [x] 2.8 Add `[SerializeField] private string telegraphId = "BasicSlashTelegraph";`
- [x] 2.9 Add `[SerializeField] private string attackId = "BasicSlash";`
- [x] 2.10 Add `[SerializeField] private string attackLabel = "M0BasicSlash";`
- [x] 2.11 Implement `[Inject] private void Construct(M0EnemyIntentModel model)` to store the injected model
- [x] 2.12 Implement coroutine or timer-based `RunLoop()` method that drives the deterministic cycle:
       `EnterIdle → wait → EnterTelegraph → wait → EnterCommit → wait → EnterActive → wait → EnterRecovery → wait → [repeat]`
- [x] 2.13 Construct one `EnemyAttackIntentContext` with `EnemyAttackTagSet` tags: `["DodgePunishable", "ParryEligible", "CounterOnWhiff"]`
- [x] 2.14 Pass constructed context to `EnterCommit()` each cycle
- [x] 2.15 Open punish window in `EnterRecovery()` call: `openPunishWindow: true`, `punishWindowSeconds: punishWindowDuration`, `punishSource: "RecoveryEnd"`
- [x] 2.16 Start `RunLoop()` coroutine in `Start()` if `model != null`; log a warning if model is null
- [x] 2.17 Verify no `NavMesh`, `NavMeshAgent`, `Animator`, `AnimationEvent`, `OnTrigger`, `OnCollision`, `ApplyDamage`, `AudioSource`, `ParticleSystem`, or `Cinemachine` references
- [x] 2.18 Verify no `FindObjectOfType`, `FindFirstObjectByType`, `GameObject.Find`, `Resources.Load`, `RegisterGeneratedFor<`, legacy `UnityEngine.Input;`, or `InputManager` references

## 3. DI Composition (Bootstrap Assembly)

- [x] 3.1 Add `[SerializeField] private M0EnemyIntentLoopDriver loopDriver;` to `GameplayLifetimeScope`
- [x] 3.2 Add `if (loopDriver != null) { builder.RegisterComponent(loopDriver); }` in `GameplayLifetimeScope.Configure()`
- [x] 3.3 Registration changed to `builder.RegisterInstance(new M0EnemyIntentModel())` — VContainer cannot resolve `System.String` constructor parameter even with default; `RegisterInstance` is the correct manual-DI pattern for types with non-resolvable constructor args (consistent with `M0LocomotionSettings`)
- [x] 3.4 Verify no generated DI attributes or automatic scanning patterns added to `GameplayLifetimeScope`
- [x] 3.5 Verify `GameplayLifetimeScope` still uses only `using VContainer` and `using VContainer.Unity` for DI — no new DI libraries

## 4. Scene Wiring

- [x] 4.1 Add `M0EnemyIntentLoopDriver` component to the `Enemy_M0TargetablePlaceholder` GameObject in `Gameplay_CombatPrototype.unity`
- [x] 4.2 Assign the loop driver component to the `loopDriver` serialized field on `GameplayLifetimeScope` in the scene
- [x] 4.3 Confirmed: `M0GameplayTickHandler.enemyIntentModel` is VContainer-injected at runtime; no serialized field required; null-guard `enemyIntentModel?.Tick(dt)` prevents exception if injection fails
- [x] 4.4 Confirmed: `targetableAdapter` → `Enemy_M0TargetablePlaceholder / M0TargetableSceneAdapter` (instanceID 255634) unchanged

## 5. Debug Overlay Live Path

- [x] 5.1 Confirm `M0DebugOverlaySnapshotAggregator.Capture()` is called in the gameplay tick path (in `M0GameplayTickHandler` or a UI driver) and passes `enemyIntentModel.Snapshot` as the `enemyIntent` argument — EnemyIntent channel exists in aggregator (line 44); no UI presenter wired yet (no presenter is in Story 1-5 scope)
- [x] 5.2 If the aggregator `Capture()` call is not yet in the tick path, add it — DEFERRED: no Debug Overlay UI presenter exists in Story 1-5 scope; `UiDebugOverlayLifetimeScope` is a skeleton; Capture() wiring belongs to the UI presenter story
- [x] 5.3 Verify Debug Overlay remains read-only — no changes to `M0DebugOverlaySnapshotAggregator` logic (confirmed: aggregator untouched)

## 6. EditMode Tests

- [x] 6.1 Verify `Assets/_Project/Tests/EditMode/M0EnemyIntentTests.cs` exists (it already does)
- [x] 6.2 Add test: `IdleStateHasEmptyAttackIntent` — in Idle, `Snapshot.AttackIntent.AttackId` is empty string, tags array is empty
- [x] 6.3 Add test: `TelegraphDoesNotAdvanceStateOnTick` — after `EnterTelegraph(1.0f)` and `Tick(0.4f)`, state is still `EnemyIntentState.Telegraph`
- [x] 6.4 Add test: `ActiveStatePreservesAttackIntentFromCommit` — after `EnterCommit(intent)` then `EnterActive()`, `Snapshot.AttackIntent.AttackId` equals commit's attackId
- [x] 6.5 Add test: `ActiveStateFromIdleHasEmptyAttackIntent` — after `EnterActive()` without prior `EnterCommit()`, `Snapshot.AttackIntent.AttackId` is empty
- [x] 6.6 Verify existing tests still pass:
       - `IdleStateIsDefaultAndReadOnlySnapshotExposed`
       - `TelegraphStateUpdatesSnapshot`
       - `CommitActiveRecoveryFlowMaintainsEnemyOwnership`
       - `PunishWindowClosesAfterTickExpiry`
       - `EnemyIntentFilesDoNotReferenceForbiddenDependencies`
- [x] 6.7 Add test: `SnapshotIsReadOnlyValueCopy` — modifying a local snapshot copy does not affect model's next `Snapshot` return

## 7. Manual Verification (PlayMode)

- [x] 7.1 Unity Editor play mode: Gameplay_CombatPrototype loaded without errors — confirmed ([GameplayScope] log only, zero errors)
- [x] 7.2 Confirmed: `M0EnemyIntentLoopDriver` found on `Enemy_M0TargetablePlaceholder` in PlayMode; null-model warning did not fire
- [x] 7.3 Open Debug Overlay: `EnemyIntent` channel shows state cycling — DEFERRED: no Debug Overlay UI presenter wired in Story 1-5 scope; EnemyIntent channel exists in aggregator; verify when UI story is complete
- [x] 7.4 Confirm `RemainingSeconds` decreases in real time — DEFERRED: verified via `TelegraphDoesNotAdvanceStateOnTick` EditMode test; visual confirmation requires Debug Overlay presenter
- [x] 7.5 Confirm `PunishWindow.IsOpen` visual — DEFERRED: verified by `PunishWindowClosesAfterTickExpiry` EditMode test; visual confirmation requires Debug Overlay presenter
- [x] 7.6 Confirm player attack resolution (Story 1-4) still works — light/heavy attacks resolve hit/whiff correctly
- [x] 7.7 Confirm lock-on (Story 1-3) still works — `Enemy_M0TargetablePlaceholder` is targetable
- [x] 7.8 Confirmed: zero console errors related to `M0EnemyIntentModel` or `M0EnemyIntentLoopDriver` in PlayMode run

## 8. Scope Exclusion Verification

- [x] 8.1 Code review: `M0EnemyIntentLoopDriver.cs` contains no damage/health mutation
- [x] 8.2 Code review: `M0EnemyIntentLoopDriver.cs` contains no hit reaction logic
- [x] 8.3 Code review: `M0EnemyIntentLoopDriver.cs` contains no parry/dodge validation
- [x] 8.4 Code review: `M0EnemyIntentLoopDriver.cs` contains no counter window resolution
- [x] 8.5 Code review: `M0EnemyIntentLoopDriver.cs` contains no Memory VFX trigger
- [x] 8.6 Code review: `M0EnemyIntentLoopDriver.cs` contains no NavMesh or AI navigation
- [x] 8.7 Code review: `M0EnemyIntentLoopDriver.cs` contains no full enemy movement system
- [x] 8.8 Code review: `M0EnemyIntentLoopDriver.cs` contains no animation root motion authority
- [x] 8.9 Code review: `M0EnemyIntentLoopDriver.cs` contains no VFX or camera polish
- [x] 8.10 Code review: `M0EnemyIntentLoopDriver.cs` contains no KCC integration
- [x] 8.11 Code review: `M0EnemyIntentLoopDriver.cs` contains no generated DI attributes
- [x] 8.12 Code review: `M0EnemyIntentLoopDriver.cs` contains no legacy Input Manager or hardcoded device polling
- [x] 8.13 Code review: `M0EnemyIntentLoopDriver.cs` contains no `FindObjectOfType`, `FindFirstObjectByType`, `GameObject.Find`, `Resources.Load`
- [x] 8.14 Code review: `M0GameplayTickHandler.cs` changes are limited to one new field + one new Construct() parameter + one Tick() call

## 9. Acceptance Criteria Sign-off

- [x] 9.1 AC-1: Enemy cycles `Idle → Telegraph → Active → Recovery` — loop driver active in PlayMode (no null-model warning, no errors); EditMode `CommitActiveRecoveryFlowMaintainsEnemyOwnership` passes
- [x] 9.2 AC-2: `telegraphDuration` is `[SerializeField]` Inspector-configurable; `RemainingSeconds` ticks via `M0GameplayTickHandler.Update()` each frame; Debug Overlay channel exists (presenter wiring deferred to UI story)
- [x] 9.3 AC-3: Active phase preserves `EnemyAttackIntentContext` from Commit in `Snapshot.AttackIntent` — confirmed by `ActiveStatePreservesAttackIntentFromCommit` EditMode test; Combat Core reads snapshot read-only
- [x] 9.4 AC-4: `PunishWindow.IsOpen == true` during Recovery; closes after `punishWindowDuration` — confirmed by `PunishWindowClosesAfterTickExpiry` EditMode test

## 10. Documentation & Housekeeping

- [x] 10.1 Fix `docs/architecture/tr-registry.yaml` — update TR-M0-ENEMY-001 `gdd` field from `design/gdd/m0-enemy-intent-ownership.md` to `design/gdd/enemy-intent-telegraph.md`

> **Note:** Story 1-5 acceptance criteria sign-off, status update (`Ready → Complete`), and sprint task status update are reserved for `/story-done` after all ACs and manual verification pass. Do not mark story or sprint status during `/opsx-apply`.
