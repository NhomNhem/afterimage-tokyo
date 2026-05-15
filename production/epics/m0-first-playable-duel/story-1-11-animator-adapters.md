# Story 1-11: [Presentation] Animator Observer Adapters

> **Epic**: M0 First Playable Duel
> **Status**: Ready
> **Layer**: Presentation
> **Type**: Visual/Feel
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/combat-core.md`, `design/gdd/player-locomotion.md`
**Requirement**: `TR-M0-ANIMATION-001`

**ADR Governing Implementation**: [ADR-0003: M0 Presentation and Debug Read-Only Boundaries]
**ADR Decision Summary**: Animator system owns presentation only; it does not affect gameplay truth.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Animator Presentation-Only (observer pattern).
- Forbidden: No hidden authorities (animation clip length does not define recovery).

---

## Acceptance Criteria

- [ ] Animator observers states and results to trigger animation clips (Attack, Dodge, Parry).
- [ ] No combat or locomotion truth is stored in or decided by the Animator.
- [ ] Animation events do not apply gameplay results directly.
- [ ] Character facing and movement expression match the authoritative Locomotion state.

---

## Implementation Notes

- Use Pure C# adapters to translate Core snapshots into Animator parameters.
- Ensure the character moves based on Pure C# position truth, not root motion.
- Keep the Animator Controller simple for M0 (placeholder quality).

---

## Out of Scope

- [Story 1-10]: Memory reveal VFX response.

---

## QA Test Cases

**AC-1: Authority Boundary**
- **Manual check**: Character moves without animation clips.
  - Setup: Disable the Animator component.
  - Verify: Character still repositioned in the duel arena.
  - Pass condition: Movement truth is preserved without presentation.

**AC-2: Trigger Alignment**
- **Manual check**: Clips trigger on correct state transitions.
  - Setup: Perform a Parry in the duel.
  - Verify: Parry animation plays in sync with the parry window.
  - Pass condition: Visual feedback matches internal state.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/AnimatorPresentationOnly_test.cs`
- Manual verification: Video clip of the duel demonstrating visual alignment with debug overlay.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-4, Story 1-5
- Unlocks: None
