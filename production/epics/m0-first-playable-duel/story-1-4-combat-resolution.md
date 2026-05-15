# Story 1-4: [Combat] Player Attack Resolution

> **Epic**: M0 First Playable Duel
> **Status**: Complete
> **Layer**: Core
> **Type**: Logic
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/combat-core.md`
**Requirement**: `TR-M0-COMBAT-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Combat Core owns validation and results; Locomotion expresses locks/recovery.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Pure C# Authority for combat truth.
- Required: Lock/Recovery Request Pattern (Combat Core emits contexts).
- Forbidden: Never store truth in MonoBehaviours.

---

## Acceptance Criteria

- [x] Light and Heavy attack intents from Input resolve in `M0CombatCore`.
- [x] Attack validity is checked against current state (e.g., cannot attack while recovering).
- [x] Successful attack requests emit `ActionLockContext` and `RecoveryContext`.
- [x] Hit/Miss results are calculated based on spacing/timing truth.

---

## Implementation Notes

- Use the skeleton FSM in `M0CombatCore`.
- Implement `ActionLockContext` to notify Locomotion when movement should be restricted.
- Ensure all logic remains in Pure C# and is testable without Unity scenes.

---

## Out of Scope

- [Story 1-6]: Parry and Dodge validation.

---

## QA Test Cases

**AC-1: Attack Validation**
- **Test**: CombatCore rejects attack if already in recovery.
  - Given: CombatCore state is Recovery.
  - When: LightAttack intent is received.
  - Then: Result is Rejected and state remains Recovery.

**AC-2: Lock Emission**
- **Test**: Attack request emits valid lock context.
  - Given: CombatCore state is Neutral.
  - When: HeavyAttack intent is received.
  - Then: Result is Accepted and state becomes Active with a non-zero lock duration.

---

## Test Evidence

**Story Type**: Logic
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/CombatResolution_test.cs`
- Manual verification: Debug Overlay showing combat state transitions and lock reasons.

**Status**: [x] Complete

**Evidence summary**:
- OpenSpec change: `wire-m0-player-attack-resolution` — all tasks complete
- Code review verdict: APPROVED WITH SUGGESTIONS (no blockers)
- EditMode tests: `Assets/_Project/Tests/EditMode/CombatResolution_test.cs` — 16 tests, 0 errors
  - Intent routing (LightAttack, HeavyAttack)
  - State rejection (Recovery, AttackStartup, HitReact)
  - Placeholder hit/whiff resolution
  - ActionLock emission after accepted attack (AC-2)
  - Snapshot immutability, no damage mutation, manual DI, no forbidden APIs
- Runtime scene wiring: `Gameplay_CombatPrototype.unity`
  - `Enemy_M0TargetablePlaceholder` + `M0TargetableSceneAdapter` — registers with `ITargetableRegistry` via VContainer
  - `CameraMovementBasisProvider_Gameplay` — explicitly assigned on `M0GameplayTickHandler`
- PlayMode paths verified: no lock-on → whiff; LockOn → hit (placeholder); release → whiff
- No damage/health mutation. No hit reaction. No enemy AI. No parry/dodge/counter.
- No animation/root motion/VFX/camera polish. No KCC. No locomotion rewrite. No forbidden APIs.

**Known follow-up (not blockers)**:
- Player is a bare scene object — no reusable Player prefab yet (future story)
- `CameraMovementBasisProvider` uses `Camera.main` fallback when Camera scene not additive-loaded (non-blocking tech debt)
- `ResolveAttack` is `public` — suggest `internal` in a future cleanup pass
- Existing unrelated `NhemBootstrap` EditMode test failure is separate tooling debt

---

## Dependencies

- Depends on: Story 1-1, Story 1-2
- Unlocks: Story 1-6, Story 1-7, Story 1-10
