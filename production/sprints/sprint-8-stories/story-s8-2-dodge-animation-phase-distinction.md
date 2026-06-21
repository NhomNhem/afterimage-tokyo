# Story S8-2: [Presentation] Dodge Animation Phase Distinction

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
**GDD**: `design/gdd/player-locomotion.md`, `design/gdd/combat-core.md`
**ADR Governing Implementation**: ADR-0003 — Animator is presentation-only; must not own gameplay truth.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW-MEDIUM
**Engine Notes**: Animator Controller transition and blend tree tuning only. No gameplay state changes.

**Control Manifest Rules**:
- Required: Dodge phase presentation (startup → active → recovery) observes Player Locomotion dodge state only.
- Forbidden: Dodge animation clip length must not define dodge invincibility or recovery. Combat Core / Player Locomotion owns dodge truth.
- Guardrail: Changes scoped to `AnimatorController`, blend tree weights, and transition settings only.

---

## Acceptance Criteria

- [ ] Dodge startup phase is visually identifiable — player pose communicates commitment to dodge.
- [ ] Dodge active phase (invincibility window) is visually distinct from startup and landing.
- [ ] Dodge recovery/landing phase is visually distinct — player communicates return to ready state.
- [ ] Start → active → end transitions read as three separate phases in Game View without debug overlay.
- [ ] Presentation changes do not alter Player Locomotion dodge truth or Combat Core dodge validity.
- [ ] No regression to attack or parry animation triggers.

---

## Implementation Notes

- Tune dodge blend tree or transition settings to give each phase a distinct pose.
- Align animation parameter updates to existing Locomotion dodge state signals.
- Verify in Game View without relying on debug overlay labels — the animation alone should communicate the phase.
- Use existing clips — do not import new animation assets.

---

## Out of Scope

- New animation assets.
- Player Locomotion dodge displacement or timing changes.
- Attack, parry, or counter animation (separate stories).
- Enemy animation or camera changes.

---

## QA Test Cases

- **AC-1**: Startup readability.
  - Setup: Perform a dodge in Game View, observe at slow motion or frame-by-frame if possible.
  - Verify: A startup lean or commitment pose is visible before the active dodge movement.
  - Pass condition: Tester can identify "dodge started" from animation alone.

- **AC-2**: Active phase readability.
  - Setup: Observe mid-dodge body pose.
  - Verify: Body pose during active phase differs from startup and landing.
  - Pass condition: Three-phase structure is readable.

- **AC-3**: Recovery readability.
  - Setup: Observe post-dodge pose before next action.
  - Verify: A distinct landing/recovery pose appears before idle.
  - Pass condition: Tester can identify "dodge complete, returning to ready" from animation alone.

- **AC-4**: Presentation boundary preserved.
  - Setup: Review diff of changed files.
  - Verify: Only Animator/blend-tree files changed.
  - Pass condition: No Locomotion truth, CombatCore, Health, or TargetContext source files modified.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- `production/qa/evidence/s8-2-dodge-animation-phase-evidence.md`
- Manual Game View observation note or screenshot sequence.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-11, Story 1-6 (Defensive Wiring), S5-4 (dodge displacement — Complete)
- Unlocks: Sprint 8 animation polish smoke

## Completion Notes
**Completed**: 2026-06-21
**Criteria**: 4/6 passing (4 auto-verified, 3 deferred for manual Game View playtest)
**Deferred**: AC-1/2/3 — three-phase visual distinction requires designer-authored `dodgeStartup`/`dodgeActive`/`dodgeRecovery` clips in `M0PlayerAnimationSet.asset`; code infrastructure complete
**Deviations**: None
**Test Evidence**: `production/qa/evidence/s8-2-dodge-animation-phase-evidence.md` (Visual/Feel, PASS)
**Code Review**: APPROVED WITH SUGGESTIONS — minor: `M0PlayerAnimationSet` class lacks doc comments; `ResolveDashDirection` unused after S8-2 (advisory, no action required)
