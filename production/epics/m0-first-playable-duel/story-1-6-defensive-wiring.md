# Story 1-6: [Combat] Parry & Dodge Integration

> **Epic**: M0 First Playable Duel
> **Status**: Complete
> **Layer**: Core
> **Type**: Logic/Integration
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-16

## Context

**GDD**: `design/gdd/combat-core.md`
**Requirement**: `TR-M0-COMBAT-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Combat Core owns parry/dodge validation; Locomotion expresses dodge movement.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Lock/Recovery Request Pattern (Dodge recovery emitted by Core).
- Forbidden: Presentation (VFX/Animator) does not decide results.

---

## Acceptance Criteria

- [ ] Parry intent from Input resolves against enemy Active timing.
- [ ] Dodge intent from Input triggers `DodgeRequestContext` and resolves success/fail in Core.
- [ ] Successful Parry opens `CounterWindow` in `CombatCore`.
- [ ] Dodge displacement and recovery are expressed in `M0PlayerLocomotion`.

---

## Implementation Notes

- Connect `M0InputRouter` Parry/Dodge intents to `M0CombatCore`.
- Use the `CombatCore` FSM to manage defensive timing windows.
- Coordinate with `M0PlayerLocomotion` to apply movement phase for dodge.

---

## Out of Scope

- [Story 1-10]: Memory reveal response.

---

## QA Test Cases

**AC-1: Parry Window**
- **Test**: Parry succeeds within valid window.
  - Given: Enemy is in Active state.
  - When: Parry intent is received during the parry window.
  - Then: Result is Success and CounterWindow.IsOpen is true.

**AC-2: Dodge Resolution**
- **Test**: Dodge fails if timing is completely off.
  - Given: Enemy hit is already resolving.
  - When: Dodge intent is received too late.
  - Then: CombatCore result is Fail/Hit.

---

## Test Evidence

**Story Type**: Logic/Integration
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/DefensiveResolution_test.cs`
- Manual verification: Debug Overlay showing parry windows and dodge results.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-3, Story 1-4, Story 1-5
- Unlocks: Story 1-7, Story 1-10

---

## Completion Notes
**Completed**: 2026-05-16
**Criteria**: 4/4 passing (all verified via EditMode tests and runtime input verification)
**Deviations**: None
**Test Evidence**: Logic test file at Assets/_Project/Tests/EditMode/M0DefensiveResolutionTests.cs (15/15 PASS), runtime input verification PASS, PlayMode gameplay verification PASS
**Code Review**: APPROVED WITH SUGGESTIONS
**Scene Wiring**: Gameplay_CombatPrototype.unity fixed and saved (M0GameplayTickHandler references corrected to GameObject instanceIDs)
