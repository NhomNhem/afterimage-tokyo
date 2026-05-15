# Tasks: Wire M0 Defensive Dodge & Parry

> **Story**: production/epics/m0-first-playable-duel/story-1-6-defensive-wiring.md
> **Change**: wire-m0-defensive-dodge-parry
> **Design**: openspec/changes/wire-m0-defensive-dodge-parry/design.md

---

## 1. Combat Core — `ConsumeDefensiveIntent` Method (GlassRefrain.Combat Assembly)

- [x] 1.1 Add `public CombatActionRequestResult ConsumeDefensiveIntent(CombatActionType actionType, EnemyIntentSnapshot enemySnapshot)` to `M0CombatCore`
- [x] 1.2 For `CombatActionType.Parry`: evaluate parry success condition — `enemySnapshot.State == EnemyIntentState.Active` AND (`AttackIntent.AttackTags.Tags` is empty OR contains `"ParryEligible"`)
- [x] 1.3 If parry condition is true: call existing `RequestAction(Parry)` and mark result as parry-eligible; `OpenCounterWindow` will be called by `AdvanceState(ParryActive)` only when eligible flag is set
- [x] 1.4 If parry condition is false: call `RequestAction(Parry)` to allow state transition (player committed), but do NOT open `CounterWindow`; set a `parryWasEligible` internal flag to false before advancing
- [x] 1.5 Modify `AdvanceState(ParryActive → ParryRecovery)`: open `CounterWindow` only if `parryWasEligible == true`; reset flag after check
- [x] 1.6 For `CombatActionType.Dodge`: call existing `RequestAction(Dodge)` — enemy snapshot advisory only; no validation gate for dodge
- [x] 1.7 For `CombatActionType.Counter`: guard — reject with `CombatActionResult.Rejected` if `CounterWindow.IsOpen == false`; accept and transition to `CounterActive` if open (resolves OQ-2 from design.md)
- [x] 1.8 Verify `GlassRefrain.Combat.asmdef` does NOT gain a reference to `GlassRefrain.Enemy` — `EnemyIntentSnapshot` arrives via `GlassRefrain.Core` (M0Contracts.cs) which Combat already references
- [x] 1.9 Verify existing `ConsumeAttackIntent(LightAttack/HeavyAttack)` is unchanged
- [x] 1.10 Verify no `NavMesh`, `Animator`, `ApplyDamage`, `Health`, `Memory`, `FindObjectOfType`, `Resources.Load`, `RegisterGeneratedFor`, legacy `UnityEngine.Input` references introduced

## 2. Input Routing — `M0DirectPlayerInput` (GlassRefrain.Input Assembly)

- [x] 2.1 Add `private InputAction parryAction;` field to `M0DirectPlayerInput`
- [x] 2.2 Add `private InputAction dodgeAction;` field
- [x] 2.3 Add `private InputAction counterAction;` field
- [x] 2.4 In `OnEnable()`: resolve `parryAction = gameplayMap.FindAction("Parry");`
- [x] 2.5 In `OnEnable()`: resolve `dodgeAction = gameplayMap.FindAction("Dodge");`
- [x] 2.6 In `OnEnable()`: resolve `counterAction = gameplayMap.FindAction("Counter");`
- [x] 2.7 In `OnDestroy()`: null-assign `parryAction`, `dodgeAction`, `counterAction`
- [x] 2.8 `M0DirectPlayerInput` does NOT route parry/dodge/counter to Combat Core directly — it only reads `WasPressedThisFrame()` and stores result in a per-frame state readable by the tick handler (see task 3)
- [x] 2.9 Add `public bool ParryPressedThisFrame => parryAction != null && parryAction.WasPressedThisFrame();`
- [x] 2.10 Add `public bool DodgePressedThisFrame => dodgeAction != null && dodgeAction.WasPressedThisFrame();`
- [x] 2.11 Add `public bool CounterPressedThisFrame => counterAction != null && counterAction.WasPressedThisFrame();`
- [x] 2.12 Verify no `Keyboard.current`, `Mouse.current`, `Gamepad.current`, or `Input.GetKey` references
- [x] 2.13 Verify `GlassRefrain.Input.asmdef` does NOT gain a reference to `GlassRefrain.Enemy`
- [x] 2.14 Add comment: `// Story 1-6: Defensive intent reads — routing to CombatCore handled by M0GameplayTickHandler`

## 3. Tick Handler — Defensive Routing & Recovery Forwarding (GlassRefrain.Bootstrap Assembly)

- [x] 3.1 In `M0GameplayTickHandler.Update()`, after `enemyIntentModel?.Tick(dt)` and before end of frame: add defensive intent forwarding block
- [x] 3.2 If `directInput != null && combatCore != null && enemyIntentModel != null`:
       - If `directInput.ParryPressedThisFrame`: call `combatCore.ConsumeDefensiveIntent(CombatActionType.Parry, enemyIntentModel.Snapshot)`
       - If `directInput.DodgePressedThisFrame`: call `combatCore.ConsumeDefensiveIntent(CombatActionType.Dodge, enemyIntentModel.Snapshot)`
       - If `directInput.CounterPressedThisFrame`: call `combatCore.ConsumeDefensiveIntent(CombatActionType.Counter, enemyIntentModel.Snapshot)`
- [x] 3.3 After defensive intent forwarding: add recovery context forwarding — if `combatCore != null && locomotion != null`: `locomotion.SetRecoveryContext(combatCore.Snapshot.Recovery)`
- [x] 3.4 Verify call order in `Update()`:
       1. `locomotion.SetCameraMovementBasis(...)` (existing)
       2. `locomotion.ProcessMovementInput(dt)` (existing)
       3. `locomotion.UpdatePosition(dt)` (existing)
       4. `enemyIntentModel?.Tick(dt)` (Story 1-5)
       5. Defensive intent forwarding (new — Story 1-6)
       6. Recovery context forwarding (new — Story 1-6)
- [x] 3.5 Verify `M0GameplayTickHandler` does not call `OpenCounterWindow`, `CloseCounterWindow`, or any state-entry method directly — it only forwards intents and recovery context
- [x] 3.6 Verify `M0GameplayTickHandler` does not mutate `M0EnemyIntentModel`, `M0TargetContext`, or `M0PlayerLocomotion` truth beyond recovery forwarding

## 4. TR Registry Fix

- [x] 4.1 In `docs/architecture/tr-registry.yaml`: update `TR-M0-COMBAT-001` `gdd` field from `design/gdd/m0-combat-core-ownership.md` to `design/gdd/combat-core.md`
- [x] 4.2 Update `source_gdds` array entry for `TR-M0-COMBAT-001` to match corrected path

## 5. EditMode Tests (GlassRefrain.Tests.EditMode Assembly)

- [x] 5.1 Create `Assets/_Project/Tests/EditMode/M0DefensiveResolutionTests.cs`
       (Existing `M0CombatCoreTests.cs` updated for Counter guard + parry conditionality; new file created as primary target)

**Input routing tests (Pure C# — no MonoBehaviour required):**
- [x] 5.2 `ParryIntentRoutesToCombatCoreAsParryAction` — calling `ConsumeDefensiveIntent(Parry, activeEligibleSnapshot)` accepted by `M0CombatCore`
- [x] 5.3 `DodgeIntentRoutesToCombatCoreAsDodgeAction` — calling `ConsumeDefensiveIntent(Dodge, anySnapshot)` accepted by `M0CombatCore` when neutral
- [x] 5.4 `CounterIntentRoutesToCombatCoreAsCounterAction` — calling `ConsumeDefensiveIntent(Counter, anySnapshot)` accepted when `CounterWindow.IsOpen`
- [x] 5.5 `InputDoesNotDecideParryValidity` — `ConsumeDefensiveIntent` returns accepted/rejected based on snapshot state, not based on caller; test with two calls, same input, different snapshots

**Parry validation tests:**
- [x] 5.6 `ParrySucceedsAndOpensCounterWindowWhenEnemyActiveAndParryEligible` — enemy snapshot `State == Active`, tags contain `"ParryEligible"` → `CounterWindow.IsOpen == true` after `ParryActive` advances
- [x] 5.7 `ParryDoesNotOpenCounterWindowWhenEnemyInTelegraph` — enemy snapshot `State == Telegraph` → `CounterWindow.IsOpen == false` after full parry cycle
- [x] 5.8 `ParryDoesNotOpenCounterWindowWhenEnemyInCommit` — enemy snapshot `State == Commit` → `CounterWindow.IsOpen == false`
- [x] 5.9 `ParryDoesNotOpenCounterWindowWhenEnemyInRecovery` — enemy snapshot `State == Recovery` → `CounterWindow.IsOpen == false`
- [x] 5.10 `ParryDoesNotOpenCounterWindowWhenEnemyInIdle` — enemy snapshot `State == Idle` → `CounterWindow.IsOpen == false`
- [x] 5.11 `ParryAgainstActiveButNonParryEligibleTagsDoesNotOpenCounterWindow` — enemy snapshot `State == Active`, tags contain only `"DodgePunishable"` (no `"ParryEligible"`) → `CounterWindow.IsOpen == false`
- [x] 5.12 `ParryAgainstActiveWithEmptyTagsOpensCounterWindow` — enemy snapshot `State == Active`, tags array is empty → `CounterWindow.IsOpen == true` (all attacks parryable if no tags specified)

**Dodge tests:**
- [x] 5.13 `DodgeTransitionsThroughExpectedStatesViaConsumeDefensiveIntent` — verify `DodgeStartup → DodgeActive → DodgeRecovery → Neutral` via `AdvanceState` after `ConsumeDefensiveIntent(Dodge)`
- [x] 5.14 `DodgeRecoveryContextIsActiveWhenInDodgeRecoveryState` — `combatCore.Snapshot.Recovery.IsRecovering == true` when state is `DodgeRecovery`
- [x] 5.15 `DodgeRecoveryContextIsFalseWhenNeutral` — `combatCore.Snapshot.Recovery.IsRecovering == false` when state is `Neutral`
- [x] 5.16 `DodgeDoesNotMutateEnemyIntentSnapshot` — after `ConsumeDefensiveIntent(Dodge, snapshot)`, enemy snapshot `State` is unchanged

**Counter tests:**
- [x] 5.17 `CounterRejectedWhenCounterWindowIsClosed` — `ConsumeDefensiveIntent(Counter, anySnapshot)` returns `CombatActionResult.Rejected` when `CounterWindow.IsOpen == false`
- [x] 5.18 `CounterAcceptedWhenCounterWindowIsOpen` — after `OpenCounterWindow(...)`, `ConsumeDefensiveIntent(Counter, anySnapshot)` returns accepted and transitions to `CounterActive`

**Scope exclusion test:**
- [x] 5.19 `DefensiveWiringFilesDoNotReferenceForbiddenDependencies` — file-scan test verifying changed files contain none of: `NavMesh`, `Animator`, `AnimationEvent`, `ApplyDamage`, `AudioSource`, `ParticleSystem`, `Cinemachine`, `FindObjectOfType`, `FindFirstObjectByType`, `GameObject.Find`, `Resources.Load`, `RegisterGeneratedFor`, `UnityEngine.Input;`, `Keyboard.current`, `Mouse.current`, `Gamepad.current`

## 6. Manual Verification (PlayMode)

- [ ] 6.1 Enter PlayMode — confirm no new console errors or null-model warnings
- [ ] 6.2 Press Parry (`Q`) when enemy is in Telegraph phase — confirm `CounterWindow.IsOpen` remains false (via Debug Overlay or console log if available)
- [ ] 6.3 Press Parry (`Q`) when enemy is in Active phase — confirm `CounterWindow.IsOpen` becomes true
- [ ] 6.4 Press Dodge (`LShift`) — confirm locomotion enters `Recovering` state during `DodgeRecovery` (player translation restricted)
- [ ] 6.5 Press Counter (`E`) when `CounterWindow.IsOpen` — confirm `CombatCoreState` transitions to `CounterActive` then `RevealBeat`
- [ ] 6.6 Press Counter (`E`) when `CounterWindow.IsOpen == false` — confirm action is rejected (no state change)
- [ ] 6.7 Confirm existing light/heavy attack resolution still works (no regression from Story 1-4)
- [ ] 6.8 Confirm lock-on still works (no regression from Story 1-3)
- [ ] 6.9 Confirm enemy intent loop still cycles cleanly (no regression from Story 1-5)
- [ ] 6.10 Confirm no damage applied, no health mutated, no Memory VFX triggered

## 7. Scope Exclusion Verification (Code Review)

- [x] 7.1 `M0CombatCore.cs`: no damage/health mutation
- [x] 7.2 `M0CombatCore.cs`: no hit reaction logic
- [x] 7.3 `M0CombatCore.cs`: no Memory VFX trigger
- [x] 7.4 `M0CombatCore.cs`: no NavMesh, Animator, KCC reference
- [x] 7.5 `M0CombatCore.cs`: does not reference `GlassRefrain.Enemy` assembly
- [x] 7.6 `M0DirectPlayerInput.cs`: no `Keyboard.current`, `Mouse.current`, `Gamepad.current`, `Input.GetKey`
- [x] 7.7 `M0DirectPlayerInput.cs`: no `GlassRefrain.Enemy` reference
- [x] 7.8 `M0GameplayTickHandler.cs`: changes limited to defensive forwarding block + recovery forwarding; no state-entry calls
- [x] 7.9 `M0GameplayTickHandler.cs`: no direct mutation of Enemy Intent, Target Context, or health
- [x] 7.10 All changed files: no `FindObjectOfType`, `FindFirstObjectByType`, `GameObject.Find`, `Resources.Load`, `RegisterGeneratedFor`

## 8. Acceptance Criteria Sign-off

- [ ] 8.1 AC-1: Parry intent from Input resolves against enemy Active timing — `ConsumeDefensiveIntent(Parry, snapshot)` routes correctly; `CounterWindow.IsOpen` depends on enemy state
- [ ] 8.2 AC-2: Dodge intent from Input triggers `DodgeRequestContext` and resolves success/fail in Core — `DodgeStartup/Active/Recovery` cycle confirmed; `DodgeResultContext` or `RecoveryContext` forwarded to locomotion
- [ ] 8.3 AC-3: Successful Parry opens `CounterWindow` in `CombatCore` — `CounterWindow.IsOpen == true` when parry was against Active + ParryEligible
- [ ] 8.4 AC-4: Dodge displacement and recovery are expressed in `M0PlayerLocomotion` — `locomotion.Snapshot.State == Recovering` during `DodgeRecovery`

## 9. Documentation & Housekeeping

- [x] 9.1 Fix `TR-M0-COMBAT-001` GDD pointer in `docs/architecture/tr-registry.yaml` (task 4.1–4.2)
- [x] 9.2 Add Story 1-6 comment header to `M0DirectPlayerInput.cs` new input action fields: `// Story 1-6: Defensive intent reads`
- [x] 9.3 Add Story 1-6 comment to new `M0GameplayTickHandler.Update()` block: `// Story 1-6: Defensive intent forwarding + recovery context`

> **Note:** Story 1-6 acceptance criteria sign-off, status update (`Ready → Complete`), and sprint task status update are reserved for `/story-done` after all ACs and manual verification pass. Do not mark story or sprint status during `/opsx-apply`.
