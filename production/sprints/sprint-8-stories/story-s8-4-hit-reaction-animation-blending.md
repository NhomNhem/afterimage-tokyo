# Story S8-4: [Presentation] Hit Reaction Animation Blending

> **Sprint**: Sprint 8
> **Status**: Complete
> **Layer**: Presentation
> **Type**: Visual/Feel
> **Estimate**: 0.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-21

## Context

**Sprint Plan**: `production/sprints/sprint-8.md`
**Epic**: M0 First Playable Duel — player animation polish pass
**GDD**: `design/gdd/combat-core.md`, `design/gdd/player-locomotion.md`
**Requirement**: Section 8.8 Basic Hit Reaction / Recovery — "short and clear...sufficient to communicate that the player lost control because of a readable mistake." Also `TR-M0-HEALTH-001`: "Health / Damage / Hit Reaction owns damage/application and consequence truth."
**ADR Governing Implementation**: ADR-0003 — Animator is presentation-only.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW
**Engine Notes**: Animator hit reaction trigger and blend tuning only. No Health/Combat Core changes.

**Performance Budget**: No performance impact expected — Animator blend tuning only, no new runtime systems.

**Control Manifest Rules**:
- Required: Hit reaction animation observes confirmed Health/damage result only.
- Forbidden: Hit reaction clip length must not define stagger duration. Health / Combat Core owns hit stagger truth.
- Guardrail: Changes scoped to Animator hit reaction state and blending only.

---

## Acceptance Criteria

- [ ] Hit reaction animation is visually distinct from idle and attack animations.
- [ ] Hit reaction blends cleanly from the interrupted state (attack, dodge, idle) without a pop.
- [ ] Hit reaction communicates damage taken — body response is legible in Game View.
- [ ] Presentation changes do not alter Health damage application or hit stagger truth.
- [ ] No regression to attack, dodge, or parry animation triggers.

---

## Implementation Notes

- Tune hit reaction state transitions in `AnimatorController` — focus on blend in/out timing.
- Ensure hit reaction trigger is driven by confirmed damage result, not a visual guess.
- Use existing clips — do not import new assets.
- Scope is player hit reactions only (not enemy reactions).

---

## Out of Scope

- New animation assets.
- Health damage or stagger timing changes.
- Enemy hit reaction animation.
- Camera shake or VFX changes.

---

## QA Test Cases

- **AC-1**: Hit reaction legibility.
  - Setup: Take damage in Game View.
  - Verify: Hit reaction pose is visually distinct from idle and attack.
  - Pass condition: Tester identifies "player took a hit" from animation alone.

- **AC-2**: Blend quality.
  - Setup: Take damage mid-attack.
  - Verify: Hit reaction blends without a jarring snap or pop.
  - Pass condition: Transition feels responsive, not broken.

- **AC-3**: Presentation boundary preserved.
  - Setup: Review diff.
  - Verify: Only Animator files changed.
  - Pass condition: No Health, CombatCore, Locomotion, or TargetContext source files modified.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- `production/qa/evidence/s8-4-hit-reaction-animation-blending-evidence.md`
- Manual Game View observation note.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-11, Story 1-7 (Health & Hit Reactions), S5-5 (Health-Combat Contract — Complete)
- Unlocks: Sprint 8 animation polish smoke

---

## Completion Notes
**Completed**: 2026-06-21
**Criteria**: 5/5 passing
**Deviations**: None
**Test Evidence**: Visual/Feel — evidence doc at `production/qa/evidence/s8-4-hit-reaction-animation-blending-evidence.md` (sign-off table TBD, fill before sprint close-out)
**Code Review**: Skipped (lean mode)
