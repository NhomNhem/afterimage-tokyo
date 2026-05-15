# Story 1-5: [Enemy] Intent & Telegraph Loop

> **Epic**: M0 First Playable Duel
> **Status**: Complete
> **Layer**: Core
> **Type**: Logic
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-16

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
