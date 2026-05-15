# Story 1-7: [Consequence] Health & Hit Reactions

> **Epic**: M0 First Playable Duel
> **Status**: Ready
> **Layer**: Core
> **Type**: Logic/Integration
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/health-damage-hit-reaction.md`
**Requirement**: `TR-M0-HEALTH-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Health owns consequence truth; it processes hit results and triggers reaction state.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Lock/Recovery Request Pattern (Health triggers locomotion suppression).
- Forbidden: Never store truth in MonoBehaviours.

---

## Acceptance Criteria

- [ ] Damage is applied to Health only after a confirmed `CombatCore` hit result.
- [ ] Hit Reaction state triggers movement/control suppression in `M0PlayerLocomotion`.
- [ ] Stagger state in enemy is triggered by player hits or counter success.
- [ ] Health state (current/max) is visible in debug.

---

## Implementation Notes

- Use the `M0HealthDamageReactionModel` skeleton.
- Ensure hit reactions are short and return control to the player predictably.
- Coordinate with `M0PlayerLocomotion` via `MovementRestrictionContext`.

---

## Out of Scope

- [Story 1-8]: Encounter reset on defeat.

---

## QA Test Cases

**AC-1: Damage Application**
- **Test**: Health decreases only on hit result.
  - Given: Entity has 100 Health.
  - When: Combat result is Hit (10 damage).
  - Then: Health becomes 90.

**AC-2: Control Suppression**
- **Test**: Player is suppressed during hit reaction.
  - Given: Player is hit.
  - When: Input is received during hit reaction.
  - Then: Movement velocity remains 0 until reaction ends.

---

## Test Evidence

**Story Type**: Logic/Integration
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/HealthConsequence_test.cs`
- Manual verification: Debug Overlay showing health bars and suppression reason.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-4, Story 1-5
- Unlocks: Story 1-8
