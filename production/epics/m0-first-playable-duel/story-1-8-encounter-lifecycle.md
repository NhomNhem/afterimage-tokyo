# Story 1-8: [Encounter] Reset & Duel Lifecycle

> **Epic**: M0 First Playable Duel
> **Status**: Ready
> **Layer**: Core
> **Type**: Logic/Integration
> **Estimate**: 0.5d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/encounter-framework.md`
**Requirement**: `TR-M0-ENCOUNTER-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Encounter Framework owns encounter lifecycle only (start, end, reset).

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Ownership Separation (Encounter owns lifecycle only).
- Forbidden: No hidden authorities (Encounter doesn't decide combat truth).

---

## Acceptance Criteria

- [ ] Encounter cycles through `Ready -> Starting -> Active -> Ending -> Resetting`.
- [ ] Duel starts only after player and enemy participants are registered and ready.
- [ ] Reset trigger returns participants to their initial duel positions and resets system state.
- [ ] Reset is repeatable without reloading the scene.

---

## Implementation Notes

- Use the `M0EncounterFramework` skeleton.
- Implement `EncounterResetContext` to coordinate state clearing across systems.
- Ensure reset logic is simple and fast for M0 iteration.

---

## Out of Scope

- [Story 1-11]: Final animation reset.

---

## QA Test Cases

**AC-1: Lifecycle Transition**
- **Test**: Encounter transition follows GDD flow.
  - Given: Encounter is Ready.
  - When: Start trigger is received.
  - Then: State is Active.

**AC-2: Participant Reset**
- **Manual check**: Participants return to start markers on reset.
  - Setup: Finish or abort a duel.
  - Verify: Player and Enemy snap back to initial positions.
  - Pass condition: 100% position accuracy on reset.

---

## Test Evidence

**Story Type**: Logic/Integration
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/EncounterLifecycle_test.cs`
- Manual verification: Debug Overlay showing encounter phase and reset trigger.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-1, Story 1-7
- Unlocks: Story 1-9
