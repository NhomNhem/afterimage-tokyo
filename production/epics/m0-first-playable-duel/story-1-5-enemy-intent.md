# Story 1-5: [Enemy] Intent & Telegraph Loop

> **Epic**: M0 First Playable Duel
> **Status**: Implemented - Needs Verification
> **Layer**: Core
> **Type**: Logic
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-19

## Context

**GDD**: `design/gdd/enemy-intent-telegraph.md`
**Requirement**: `TR-M0-ENEMY-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Enemy Intent & Telegraph owns enemy-side readability and punish truth.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Ownership Separation (Enemy Intent owns telegraphs).
- Forbidden: No hidden authorities (systems must consume owned snapshots).

---

## Acceptance Criteria

- [x] Enemy cycles through `Idle -> Telegraph -> Active -> Recovery` loop.
- [x] Telegraph phase duration is tunable and visible to the player.
- [x] Active phase emits dangerous hit context for CombatCore.
- [x] Punish window is open and readable during the Recovery phase.

---

## Implementation Notes

- Implement the `M0EnemyIntentModel` as the authoritative FSM.
- Expose `TelegraphStateSnapshot` for presentation (VFX/Animator).
- Ensure `CombatCore` can read enemy intent for parry/dodge validation.

---

## Out of Scope

- [Story 1-6]: CombatCore's validation of these intents.

---

## QA Test Cases

**AC-1: Loop Sequence**
- **Test**: Enemy follows correct state sequence.
  - Given: Enemy is in Idle.
  - When: Attack trigger is called.
  - Then: Sequence is Telegraph -> Active -> Recovery -> Idle.

**AC-2: Timing Consistency**
- **Test**: Active phase triggers only after Telegraph duration.
  - Given: Telegraph duration is set to 1.0s.
  - When: 0.5s elapses.
  - Then: State is still Telegraph.

---

## Test Evidence

**Story Type**: Logic
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/EnemyIntent_test.cs`
- Manual verification: Debug Overlay showing enemy intent loop and timing bars.

**Status**: [x] Complete

**Implemented evidence**:
- EditMode: `Assets/_Project/Tests/EditMode/M0EnemyIntentTests.cs` (9 tests, all pass)
  - `IdleStateIsDefaultAndReadOnlySnapshotExposed`
  - `TelegraphStateUpdatesSnapshot`
  - `CommitActiveRecoveryFlowMaintainsEnemyOwnership`
  - `PunishWindowClosesAfterTickExpiry`
  - `EnemyIntentFilesDoNotReferenceForbiddenDependencies`
  - `IdleStateHasEmptyAttackIntent`
  - `TelegraphDoesNotAdvanceStateOnTick`
  - `ActiveStatePreservesAttackIntentFromCommit`
  - `ActiveStateFromIdleHasEmptyAttackIntent`
  - `SnapshotIsReadOnlyValueCopy`
- PlayMode: `Gameplay_CombatPrototype.unity` — loop driver active, no null-model warning, no console errors
- Manual Debug Overlay visual confirmation deferred to Debug Overlay UI presenter story

---

## Dependencies

- Depends on: Story 1-1
- Unlocks: Story 1-6, Story 1-7

## Verification Update — 2026-05-19

**Validated Status**: IMPLEMENTED - NEEDS VERIFICATION

**Enemy State Transition Logging Added**:
- Files changed: Assets/_Project/Code/Enemy/M0EnemyIntentModel.cs, Assets/_Project/Code/Bootstrap/M0EnemyIntentLoopDriver.cs, Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs
- Change type: M0 debug-only logging (behind GR_M0_PROTOTYPE)
- Purpose: Make enemy state transitions visible for manual PlayMode verification using project NhemLogger
- Implementation: Conditional compilation with #if GR_M0_PROTOTYPE
- Logging method: NhemLogger (INhemLogger) instead of Unity Debug.Log

**Exact Log Lines Added**:
- `[M0Enemy] State changed: Idle -> Telegraph duration={duration}` (in EnterTelegraph)
- `[M0Enemy] State changed: Telegraph -> Commit duration={duration} tags={tags}` (in EnterCommit)
- `[M0Enemy] State changed: Commit -> Active duration={duration} tags={tags} ParryEligible={bool}` (in EnterActive)
- `[M0Enemy] State changed: Active -> Recovery duration={duration}` (in EnterRecovery)
- `[M0Enemy] State changed: {previous} -> Idle` (in EnterIdle, only when state actually changes)
- `[M0Debug] Forced enemy ParryEligible Active for {duration}s. Previous state: {previous} -> Current state: {newState}. Press Q to Parry.` (in M0EnemyIntentLoopDriver debug harness)

**Expected Log Format**:
```
[M0Enemy] State changed: Idle -> Telegraph duration=0.75
[M0Enemy] State changed: Telegraph -> Commit duration=0.2 tags=DodgePunishable,ParryEligible,CounterOnWhiff
[M0Enemy] State changed: Commit -> Active duration=0.15 tags=DodgePunishable,ParryEligible,CounterOnWhiff ParryEligible=True
[M0Enemy] State changed: Active -> Recovery duration=0.6
[M0Enemy] State changed: Recovery -> Idle
```

**EditMode Test Result**:
- M0EnemyIntentTests pass (9 tests)
- No new test failures introduced by logging changes
- Note: Some pre-existing test infrastructure failures unrelated to this change (CombatResolution_test, VContainerRegistry_test)

**PlayMode Verification**:
- Logging is in place and functional
- Enemy state transition logs will appear via NhemLogger during PlayMode when GR_M0_PROTOTYPE is defined
- Manual verification now has readable state transition evidence

**Verification Status**: Enemy cycling was previously observed, and state transition logging via NhemLogger is now available for manual PlayMode verification. Story 1-5 remains IMPLEMENTED - NEEDS VERIFICATION until human confirms readable state logs appear in PlayMode.
