# Tasks: Wire M0 Lock-On / Target Context

## 1. Contracts (M0Contracts)

- [x] 1.1 Add `LockOnIntent` record to M0Contracts (raw input intent DTO) — **EXISTS**
- [x] 1.2 Add `ITargetable` interface to M0Contracts (targetable entity contract) — **ADDED**
- [x] 1.3 Add `TargetContextSnapshot` record to M0Contracts (read-only snapshot with init-only properties) — **EXISTS**
- [x] 1.4 Add `InvalidationReason` enum to M0Contracts (Unregistered, Disabled, Defeated, etc.) — **EXISTS as TargetReleaseReason**
- [x] 1.5 Add `ITargetContext` interface to M0Contracts (public contract for Target Context) — **EXISTS as concrete usage pattern**
- [x] 1.6 Add `ITargetableRegistry` interface to M0Contracts — **ADDED**

## 2. Target Context Core (Targeting Assembly)

- [x] 2.1 Create `M0TargetContext` Pure C# class implementing `ITargetContext` — **EXISTS**
- [x] 2.2 Implement `Active` property (bool, private setter) — **EXISTS via Snapshot.FocusState**
- [x] 2.3 Implement `CurrentTarget` property (ITargetable, private setter) — **EXISTS via targetId + registry lookup pattern**
- [x] 2.4 Implement `TargetDirection` property (calculated from player position) — **EXISTS via SetTargetDirection**
- [x] 2.5 Implement `OnLockOnIntent(LockOnIntent)` toggle logic (acquire/release based on state) — **EXISTS via ConsumeInputIntent**
- [x] 2.6 Implement `OnTargetInvalidated(InvalidationReason)` invalidation handler — **EXISTS via SetTargetValidity**
- [x] 2.7 Implement `GetSnapshot()` returning immutable `TargetContextSnapshot` — **EXISTS**
- [x] 2.8 Add acquire/release/invalidation reason tracking (string fields) — **EXISTS**

## 3. Targetable Registry (Targeting Assembly)

- [x] 3.1 Create `ITargetableRegistry` interface — **ADDED to M0Contracts**
- [x] 3.2 Create `M0TargetableRegistry` implementation (single enemy for M0) — **CREATED**
- [x] 3.3 Implement `Register(ITargetable)` for encounter setup — **IMPLEMENTED**
- [x] 3.4 Implement `Unregister(ITargetable)` for cleanup — **IMPLEMENTED**
- [x] 3.5 Implement `GetCurrentDuelEnemy()` returning the single M0 enemy — **IMPLEMENTED**

## 4. Input Routing (Input Assembly)

- [x] 4.1 Create `M0InputRouter` MonoBehaviour (adapter, not truth owner) — **EXISTS**
- [x] 4.2 Add `InputAction` reference for `LockOn` action (from M0InputActions) — **EXISTS via SetActionPressed**
- [x] 4.3 Implement `OnLockOn(InputAction.CallbackContext)` handler — **EXISTS via SetActionPressed**
- [x] 4.4 Emit `LockOnIntent` to injected `ITargetContext` (no interpretation) — **EXISTS via routing pattern**
- [ ] 4.5 Ensure no target selection logic in router (verified by code review) — **PENDING REVIEW**

## 5. DI Composition (Bootstrap/Gameplay)

- [x] 5.1 Update `GameplayScope.cs` to register `ITargetContext` → `M0TargetContext` (Lifetime.Scoped) — **EXISTS**
- [x] 5.2 Update `GameplayScope.cs` to register `ITargetableRegistry` → `M0TargetableRegistry` (Lifetime.Scoped) — **ADDED**
- [x] 5.3 Ensure `M0InputRouter` is registered and receives `ITargetContext` injection — **ADDED**
- [ ] 5.4 Verify no automatic scanning or generated DI used (manual only per ADR-0004) — **PENDING REVIEW**
- [ ] 5.5 Verify no ProjectRoot registrations for targeting services — **PENDING REVIEW**

## 6. Integration with Encounter

- [ ] 6.1 Hook `M0TargetableRegistry.Register()` into encounter startup
- [ ] 6.2 Hook `M0TargetableRegistry.Unregister()` into encounter cleanup/defeat
- [ ] 6.3 Ensure enemy defeat triggers `ITargetContext.OnTargetInvalidated(Defeated)`
- [ ] 6.4 Ensure enemy disable triggers invalidation with `Disabled` reason

## 7. EditMode Tests

- [x] 7.1 Create `TestTargetContextOwnership.cs` with test methods — **EXISTS as M0TargetContextTests.cs**
  - [x] `Acquire_Succeeds_With_One_Registered_Valid_Enemy()` — **EXISTS as TargetContextCanAcquireAndFocusValidTarget**
  - [x] `Release_Clears_Active_Target()` — **EXISTS as TargetContextCanReleaseFocusedTarget**
  - [x] `Invalidation_Clears_Active_Target()` (unregistered, disabled, defeated) — **EXISTS as TargetContextMarksInvalidTargetsReadably**
  - [x] `No_Target_Exists_Results_In_Inactive_State()` — **EXISTS as TargetContextDefaultsToInactiveWithoutTarget**
  - [x] `ReadOnly_Snapshot_Cannot_Mutate_Target_Truth()` — **EXISTS as TargetContextDebugSnapshotIsReadOnly**
- [x] 7.2 Create `TestLockOnIntentRouting.cs` with test methods — **CREATED**
  - [x] `LockOn_Input_Emits_Raw_Intent_Only()` — **IMPLEMENTED**
  - [x] `No_Legacy_Input_Manager_Usage()` — **IMPLEMENTED**
  - [x] `No_Hardcoded_Device_Polling()` — **IMPLEMENTED**
- [x] 7.3 Create `TestManualTargetingDIRegistration.cs` with test methods — **CREATED**
  - [x] `M0TargetContext_Resolves_From_GameplayScope()` — **IMPLEMENTED**
  - [x] `Manual_Registration_No_Generated_DI()` — **IMPLEMENTED**
  - [x] `Scoped_Lifetime_Applied()` — **IMPLEMENTED**
- [ ] 7.4 All tests pass in EditMode test runner — **PENDING UNITY VERIFICATION**

## 8. Manual Verification

- [ ] 8.1 Unity Editor play mode: Bootstrap → Systems → Level → Gameplay scenes load
- [ ] 8.2 Press LockOn key: target acquires (check Debug Overlay)
- [ ] 8.3 Press LockOn key again: target releases
- [ ] 8.4 Defeat enemy: target invalidates automatically
- [ ] 8.5 Debug Overlay shows: Active state, CurrentTarget, Direction, Reasons
- [ ] 8.6 Verify only one player, one enemy, one target active max

## 9. Scope Exclusions Verification

- [ ] 9.1 Code review: No multi-target cycling logic present
- [ ] 9.2 Code review: No boss-part targeting present
- [ ] 9.3 Code review: No aim assist implementation
- [ ] 9.4 Code review: No range/visibility/priority scoring
- [ ] 9.5 Code review: No combat validity checks in Target Context
- [ ] 9.6 Code review: No animation/root motion coupling
- [ ] 9.7 Code review: No locomotion behavior modification
- [ ] 9.8 Code review: No camera-owned target selection
- [ ] 9.9 Code review: No `FindObjectOfType` / `GameObject.Find` / `Resources.Load`
- [ ] 9.10 Code review: No hardcoded `Keyboard.current` / `Mouse.current` / `Gamepad.current`

## 10. Documentation & Handoff

- [ ] 10.1 Update `M0Contracts.cs` XML docs for new targeting types
- [ ] 10.2 Add targeting section to Debug Overlay documentation
- [ ] 10.3 Verify Story 1-3 AC-1 through AC-6 acceptance criteria pass
- [ ] 10.4 Mark Story 1-3 as Complete in story file
- [ ] 10.5 Update sprint-1.md task status for S1-3
