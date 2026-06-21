# Story S8-3: [Presentation] Parry and Counter Animation Transition Readability

> **Sprint**: Sprint 8
> **Status**: Complete
> **Layer**: Presentation
> **Type**: Visual/Feel
> **Estimate**: 1.0 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-21

## Context

**Sprint Plan**: `production/sprints/sprint-8.md`
**Epic**: M0 First Playable Duel — player animation polish pass
**GDD**: `design/gdd/combat-core.md`
**Requirement**: Section 10.5 Defensive Answer Philosophy — "dodge = spatial answer, parry = timing answer, counter = reward answer... If dodge, parry, and attack blur into one generic answer space, the system loses its interpretive clarity." Also Section 10.3: "parry feedback must be readable in animation, sound, VFX, and debug overlay."
**ADR Governing Implementation**: ADR-0003 — Animator is presentation-only.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW-MEDIUM
**Engine Notes**: Animator Controller transition tuning only. No Combat Core changes.

**Performance Budget**: No performance impact expected — Animator Controller transition tuning only, no new runtime systems or per-frame allocations.

**Control Manifest Rules**:
- Required: Parry and counter animations observe confirmed Combat Core state only.
- Forbidden: Parry animation must not define parry window timing. Combat Core owns counter window truth.
- Guardrail: Parry and counter must read as visually distinct from each other and from dodge.

---

## Acceptance Criteria

- [ ] Parry animation is visually distinct from dodge — blocking/deflect pose communicates defensive intent.
- [ ] Counter animation is visually distinct from parry — counter strike communicates an active punish, not another block.
- [ ] Parry → counter transition is readable: tester can see the state change without the debug overlay.
- [ ] Presentation changes do not alter Combat Core parry or counter window truth.
- [ ] No regression to attack or dodge animation triggers.

---

## Implementation Notes

- Tune `AnimatorController` transitions between parry and counter states.
- Ensure counter trigger is wired to the confirmed counter window signal from Combat Core, not a timer or guess.
- Use existing clips — do not import new animation assets.
- Verify side-by-side: play parry then counter in Game View and confirm visual difference without debug overlay assistance.

---

## Out of Scope

- New animation assets.
- Combat Core parry/counter window timing changes.
- Attack or dodge animation (separate stories).
- Enemy animation, camera, or VFX changes.

---

## QA Test Cases

- **AC-1**: Parry vs dodge distinction.
  - Setup: Perform dodge then parry in sequence.
  - Verify: The two animations are clearly different poses.
  - Pass condition: Tester can label each without being told which is which.

- **AC-2**: Parry vs counter distinction.
  - Setup: Perform a successful parry then execute the counter.
  - Verify: The counter animation communicates "punish" rather than another deflect.
  - Pass condition: Tester can distinguish parry from counter by animation alone.

- **AC-3**: Transition readability.
  - Setup: Watch parry → counter in Game View at normal speed.
  - Verify: The transition is legible — counter does not pop or blend identically to parry.
  - Pass condition: Tester identifies the moment the counter became available from the animation.

- **AC-4**: Presentation boundary preserved.
  - Setup: Review diff.
  - Verify: Only Animator/transition files changed.
  - Pass condition: No CombatCore, Health, Locomotion, or TargetContext source files modified.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- `production/qa/evidence/s8-3-parry-counter-animation-transition-evidence.md`
- Manual Game View observation note.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-11, Story 1-6 (Defensive Wiring), `production/sprints/sprint-6-stories/story-s6-2-parry-counter-visual-feedback-polish.md` (Complete)
- Unlocks: Sprint 8 animation polish smoke

---

## Completion Notes
**Completed**: 2026-06-21
**Criteria**: 5/5 passing (AC-1/2/3/5 confirmed via Game View playtest; AC-4 auto-verified via code review)
**Deviations**: None
**Test Evidence**: Visual/Feel — evidence doc at `production/qa/evidence/s8-3-parry-counter-animation-transition-evidence.md`
**Code Review**: APPROVED WITH SUGGESTIONS (lean mode)
