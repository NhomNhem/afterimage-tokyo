# Tasks: Wire M0 Health & Hit Reactions

> **Story**: production/epics/m0-first-playable-duel/story-1-7-health-consequence.md
> **Change**: wire-m0-health-hit-reactions
> **Design**: openspec/changes/wire-m0-health-hit-reactions/design.md

---

## 1. Health Model Enhancement

- [ ] 1.1 Verify `Assets/_Project/Code/Health/M0HealthDamageReactionModel.cs` exists
- [ ] 1.2 Review skeleton structure for required fields:
  - maxHealth (float)
  - currentHealth (float)
  - state (HealthState enum: Living, Damaged, Recovering, Disabled)
  - lastDamageResult (DamageApplicationResult)
  - hitReaction (HitReactionContext)
  - defeat (DefeatStateContext)
  - latestSnapshot (HealthStateSnapshot)
- [ ] 1.3 If skeleton is incomplete, add missing fields and RefreshSnapshot() logic
- [ ] 1.4 Verify SnapshotChanged event exists for observation
- [ ] 1.5 Verify ApplyDamage() method exists with signature: `DamageApplicationResult ApplyDamage(DamageApplicationContext request)`
- [ ] 1.6 If ApplyDamage() needs enhancement:
  - Validate target not defeated
  - Validate damage amount > 0
  - Apply damage: currentHealth -= amount
  - Clamp currentHealth to >= 0
  - Update state: currentHealth <= 0 ? Disabled : Damaged
  - Set hitReaction context with source and duration
  - Set defeat context if health <= 0
  - Call RefreshSnapshot()
- [ ] 1.7 Verify no forbidden dependencies: no FindObjectOfType, GameObject.Find, Resources.Load, legacy Input polling

## 2. Damage Amount Configuration

- [ ] 2.1 Create damage configuration constants or ScriptableObject:
  - LightAttackDamage: 10
  - HeavyAttackDamage: 20
  - CounterDamage: 25 (if counter applies damage, or use HeavyAttackDamage)
- [ ] 2.2 Create simple damage mapping function in Health assembly:
  - Map CombatActionType (LightAttack, HeavyAttack, Counter) to damage amount
  - Return damage amount based on action type
- [ ] 2.3 Ensure configuration is accessible to Health system (constant, static field, or ScriptableObject reference)

## 3. CombatCore Result Event Emission

- [ ] 3.1 Verify CombatCore already emits CombatResolutionResult with HitConfirmed flag
- [ ] 3.2 If result event does not exist, add event to CombatCore:
  - `public event Action<CombatResolutionResult> ResultChanged;`
  - Emit event in RequestAction() after result is determined
- [ ] 3.3 Verify result includes:
  - ActionType (LightAttack, HeavyAttack, Counter)
  - HitConfirmed (bool)
  - Target (player or enemy identifier)
- [ ] 3.4 Ensure event emission is thread-safe (Unity main thread only)
- [ ] 3.5 Do NOT modify CombatCore combat validity logic

## 4. Health System Wiring to CombatCore

- [ ] 4.1 Create health result processor adapter or integrate into existing Bootstrap:
  - Subscribe to CombatCore.ResultChanged event
  - On result: determine target (player or enemy)
  - On confirmed hit (HitConfirmed == true): call ApplyDamage() on target health model
- [ ] 4.2 Create separate health model instances:
  - playerHealthModel = new M0HealthDamageReactionModel(100f)
  - enemyHealthModel = new M0HealthDamageReactionModel(100f)
- [ ] 4.3 Wire player health model to CombatCore results where target is player
- [ ] 4.4 Wire enemy health model to CombatCore results where target is enemy
- [ ] 4.5 Map CombatActionType to damage amount using configuration from task 2.2
- [ ] 4.6 Verify damage is NOT applied when HitConfirmed == false
- [ ] 4.7 Verify EnemyIntent does NOT call ApplyDamage directly
- [ ] 4.8 Verify Input does NOT call ApplyDamage directly
- [ ] 4.9 Verify TargetContext does NOT call ApplyDamage directly

## 5. Player Hit Reaction and Control Suppression

- [ ] 5.1 Verify M0PlayerLocomotion already has RecoveryContext consumption (from Story 1-6)
- [ ] 5.2 If recovery/reaction context pattern exists, extend for hit reaction:
  - On player hit: emit HitReactionContext with suppression duration
  - Pass context to locomotion via SetRecoveryContext() or similar
- [ ] 5.3 If pattern does not exist, create simple suppression mechanism:
  - Add IsSuppressed flag to locomotion snapshot
  - Add SuppressionSource to locomotion snapshot
  - Health system emits HitReactionContext with SuppressionDuration
  - Locomotion observes context and suppresses movement/control for duration
- [ ] 5.4 Configure suppression duration: 0.2-0.5 seconds (tunable)
- [ ] 5.5 Test in PlayMode: confirm player movement suppressed during hit reaction
- [ ] 5.6 Test in PlayMode: confirm suppression expires after duration
- [ ] 5.7 Ensure hit reaction does NOT decide combat validity
- [ ] 5.8 Ensure no animation/root motion authority (reaction is gameplay state, not clip-driven)

## 6. Enemy Hit Reaction / Stagger

- [ ] 6.1 Verify enemy health model exists (task 4.2)
- [ ] 6.2 On enemy hit (ApplyDamage on enemy health): emit EnemyStaggerContext
- [ ] 6.3 EnemyStaggerContext includes:
  - SourceId: player identifier
  - StaggerCategory: "Stagger" or "CounterStagger"
  - StaggerDuration: 0.3-0.5 seconds
- [ ] 6.4 If Enemy Intent system can observe stagger state:
  - Wire EnemyStaggerContext to Enemy Intent
  - Pause telegraph/commit cycles during stagger (optional, if already supported)
- [ ] 6.5 If Enemy Intent cannot observe stagger, ensure stagger is visible in debug overlay only
- [ ] 6.6 Test in PlayMode: LightAttack hit on enemy triggers stagger
- [ ] 6.7 Test in PlayMode: Counter success on enemy triggers stronger stagger
- [ ] 6.8 Ensure enemy stagger does NOT open CounterWindow
- [ ] 6.9 Ensure enemy stagger does NOT decide reveal validity

## 7. VContainer Registration

- [ ] 7.1 Open Bootstrap composition root (likely in Assets/_Project/Code/Bootstrap/)
- [ ] 7.2 Register playerHealthModel:
  - `container.RegisterInstance(playerHealthModel)` or scoped registration
- [ ] 7.3 Register enemyHealthModel:
  - `container.RegisterInstance(enemyHealthModel)` or scoped registration
- [ ] 7.4 If health result processor adapter requires DI, register manually
- [ ] 7.5 Verify registration follows existing pattern from Story 1-1
- [ ] 7.6 Verify no automatic scanning or code generation
- [ ] 7.7 Verify no generated DI

## 8. Debug Overlay - Health State Visibility

- [ ] 8.1 If create-m0-playable-combat-prototype-scene is complete, extend M0CombatDebugOverlayAdapter
- [ ] 8.2 If not complete, create M0HealthDebugOverlayAdapter in GlassRefrain.Presentation
- [ ] 8.3 Subscribe to playerHealthModel.SnapshotChanged event
- [ ] 8.4 Subscribe to enemyHealthModel.SnapshotChanged event
- [ ] 8.5 Add UI Text labels for health state:
  - Player Health: "Health: 90/100"
  - Enemy Health: "Health: 80/100"
  - Player Reaction: "Reaction: HitReact (0.2s)" or "Reaction: None"
  - Suppression: "Suppressed: Yes (HitReact)" or "Suppressed: No"
  - Enemy Stagger: "Stagger: Yes (0.3s)" or "Stagger: No"
  - Player Defeated: "Defeated: No" or "Defeated: Yes"
  - Enemy Defeated: "Defeated: No" or "Defeated: Yes"
- [ ] 8.6 Update labels on snapshot change events
- [ ] 8.7 Ensure debug overlay is read-only (does not mutate health state)
- [ ] 8.8 Test in PlayMode: confirm health labels update correctly
- [ ] 8.9 Test in PlayMode: confirm reaction/stagger labels update correctly

## 9. Scene Wiring

- [ ] 9.1 Open `Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`
- [ ] 9.2 If health result processor adapter requires MonoBehaviour component:
  - Add component to scene GameObject (e.g., HealthResultProcessor on Bootstrap or separate GameObject)
  - Wire references to CombatCore, playerHealthModel, enemyHealthModel in Inspector
- [ ] 9.3 If debug overlay adapter requires MonoBehaviour component:
  - Add component to scene GameObject (e.g., on existing Canvas or separate GameObject)
  - Wire references to playerHealthModel, enemyHealthModel in Inspector
- [ ] 9.4 Save scene
- [ ] 9.5 Backup scene before changes

## 10. EditMode Tests

- [ ] 10.1 Create `Assets/_Project/Tests/EditMode/HealthConsequence_test.cs`
- [ ] 10.2 Test: Damage is not applied without confirmed CombatCore hit result
- [ ] 10.3 Test: Damage is applied after confirmed LightAttack hit
- [ ] 10.4 Test: Damage is applied after confirmed HeavyAttack hit
- [ ] 10.5 Test: Damage is applied after confirmed Counter success
- [ ] 10.6 Test: Health decreases by expected simple amount
- [ ] 10.7 Test: Health never goes below zero
- [ ] 10.8 Test: Defeated/disabled state is set when health reaches zero
- [ ] 10.9 Test: Player hit reaction creates movement/control suppression context
- [ ] 10.10 Test: Suppression expires after configured duration
- [ ] 10.11 Test: Enemy stagger is triggered by player hit
- [ ] 10.12 Test: Enemy stagger is triggered by counter success
- [ ] 10.13 Test: EnemyIntent does not directly mutate health
- [ ] 10.14 Test: Input does not directly mutate health
- [ ] 10.15 Test: TargetContext does not directly mutate health
- [ ] 10.16 Test: Debug snapshot exposes current/max health and reaction state
- [ ] 10.17 Test: Debug/UI access is read-only
- [ ] 10.18 Test: No MemoryState or MemoryVFX trigger occurs
- [ ] 10.19 Test: No animation/root motion authority
- [ ] 10.20 Test: No KCC/NavMesh usage
- [ ] 10.21 Test: No forbidden APIs (FindObjectOfType, GameObject.Find, Resources.Load, legacy Input polling)
- [ ] 10.22 Run all EditMode tests - confirm PASS

## 11. Manual PlayMode Verification

- [ ] 11.1 Enter PlayMode
- [ ] 11.2 Confirm Player and Enemy visible in Game View
- [ ] 11.3 LightAttack hit on enemy: confirm enemy health decreases (check debug overlay)
- [ ] 11.4 HeavyAttack hit on enemy: confirm enemy health decreases
- [ ] 11.5 Counter success on enemy: confirm enemy health decreases or stagger triggers
- [ ] 11.6 Enemy hit on player: confirm player health decreases
- [ ] 11.7 Player hit reaction: confirm movement/control suppression visible or debug-visible
- [ ] 11.8 Enemy stagger: confirm stagger visible or debug-visible
- [ ] 11.9 Health current/max visible in debug overlay
- [ ] 11.10 No memory reveal/VFX trigger
- [ ] 11.11 No Console errors
- [ ] 11.12 Verify existing Story 1-6 behavior still works:
  - WASD movement
  - LockOn
  - LightAttack/HeavyAttack resolution
  - Parry/Dodge/Counter resolution
  - CounterWindow expiry/consume
  - Enemy intent loop
- [ ] 11.13 Exit PlayMode

## 12. Scope Exclusion Verification

- [ ] 12.1 Verify no RPG stat system code added
- [ ] 12.2 Verify no armor/resistance code added
- [ ] 12.3 Verify no status effects code added
- [ ] 12.4 Verify no loot/XP code added
- [ ] 12.5 Verify no Memory Reveal code added
- [ ] 12.6 Verify no Memory VFX code added
- [ ] 12.7 Verify no camera shake/VFX polish code added
- [ ] 12.8 Verify no animation/root motion authority added
- [ ] 12.9 Verify no Animancer integration added
- [ ] 12.10 Verify no KCC code added
- [ ] 12.11 Verify no NavMesh code added
- [ ] 12.12 Verify no enemy AI navigation code added
- [ ] 12.13 Verify no multi-enemy damage system added
- [ ] 12.14 Verify no full damage formula framework added
- [ ] 12.15 Verify no UI polish code added
- [ ] 12.16 Verify no Asset Store package modifications
- [ ] 12.17 Verify no generated DI used
- [ ] 12.18 Verify no forbidden APIs used

## 13. Regression Tests

- [ ] 13.1 Run existing EditMode tests: M0DefensiveResolutionTests - confirm 15/15 PASS
- [ ] 13.2 Run existing EditMode tests: M0CombatCoreTests - confirm PASS
- [ ] 13.3 Verify no CombatCore logic changes (combat validity, timing windows unchanged)
- [ ] 13.4 Verify no Locomotion logic changes (movement truth unchanged)
- [ ] 13.5 Verify no EnemyIntentModel logic changes (telegraph/commit/recovery unchanged)

---

> **Note:** Story 1-7 acceptance criteria sign-off, status update (Ready → Complete), and sprint task status update are reserved for `/story-done` after all ACs and manual verification pass. Do not mark story or sprint status during `/opsx-apply`.
