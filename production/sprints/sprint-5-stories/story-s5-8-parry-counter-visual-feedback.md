# Story S5-8: [Visual Polish] Parry/Counter Visual Feedback

> **Sprint**: Sprint 5
> **Status**: Not Started
> **Layer**: Presentation / Combat Feel
> **Type**: Visual/Feel
> **Estimate**: 1.0d
> **Priority**: Nice to Have
> **Owner**: technical-artist
> **Dependencies**: None
> **Manifest Version**: 2026-05-15
> **Last Updated**:

## Context

M0 combat evidence kept Parry/Counter visual feedback as a non-blocking follow-up. Sprint 5 may upgrade that evidence from PARTIAL to COMPLETE if must-have work is stable.

Relevant trace:
- `docs/tech-debt-register.md`
- `production/sprints/sprint-5.md`
- `production/qa/qa-plan-sprint-5-2026-06-09.md`
- `production/qa/evidence/complete-m0-playable-combat-prototype-verification-evidence.md`
- `design/gdd/combat-core.md`
- `design/gdd/player-locomotion.md`

## Goal

Make Parry and Counter visual feedback clear and distinct enough that a tester can read the timing beat without presentation owning combat truth.

## Acceptance Criteria

- [ ] Parry visual feedback is clear and distinct from attack, dodge, hit, and counter.
- [ ] Counter visual feedback is clear and distinct from parry and normal attack.
- [ ] Visual feedback timing aligns with Combat Core parry and counter windows.
- [ ] Feedback is presentation-only and does not mutate combat, target, health, locomotion, or memory truth.
- [ ] No visual noise or clutter harms enemy telegraph readability.
- [ ] Evidence upgrades the previous PARTIAL visual feedback item to COMPLETE or documents why it remains PARTIAL.

## Out of Scope

- Combat timing changes
- CounterWindow duration changes
- Damage or health changes
- Enemy telegraph changes
- Full animation polish pass
- New cinematic camera system

## Implementation Notes

- Presentation should observe confirmed combat snapshots or events only.
- Keep the effect restrained and readable for one M0 duel.
- Do not let VFX/Animator decide parry success, counter validity, or damage.
- Screenshot or short capture evidence is expected.

## QA Test Cases

- **Manual check AC-1**: Parry feedback is distinct.
  - Setup: Enter M0 duel, trigger a valid parry sequence.
  - Verify: parry feedback appears at the confirmed parry beat and is not confused with attack/dodge/hit.
  - Pass condition: tester can identify parry success from visual feedback without reading logs.

- **Manual check AC-2**: Counter feedback is distinct.
  - Setup: Open CounterWindow through valid parry or supported flow, then perform Counter.
  - Verify: counter feedback is visually distinct from parry and normal attack.
  - Pass condition: tester can identify Counter activation and completion from the presentation.

- **Manual check AC-3**: Presentation boundaries hold.
  - Setup: Review implementation and run focused combat path.
  - Verify: VFX/Animator/UI do not mutate Combat Core, TargetContext, Health, Locomotion, or MemoryState truth.
  - Pass condition: focused regression tests and code review show presentation-only behavior.

- **Manual check AC-4**: Readability is not cluttered.
  - Setup: Run enemy telegraph -> defensive response -> counter sequence.
  - Verify: enemy telegraph remains readable while feedback plays.
  - Pass condition: no effect blocks the player/enemy relationship or timing read.

## Test Evidence

**Story Type**: Visual/Feel

Required evidence:
- Manual evidence at `production/qa/evidence/s5-8-parry-counter-visual-feedback-evidence.md`
- Screenshot, short capture, or lead sign-off
- Focused M0 combat regression notes

**Status**: [ ] Not yet created

## Dependencies

- Depends on: None
- Unlocks: M0 feel/readability polish evidence
