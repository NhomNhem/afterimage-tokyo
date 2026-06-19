# Story S6-2: Parry/Counter Visual Feedback Polish

> **Sprint**: Sprint 6
> **Status**: Complete
> **Layer**: Presentation
> **Type**: Visual/Feel
> **Estimate**: 1.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-16

## Context

**Sprint Plan**: `production/sprints/sprint-6.md`
**QA Plan**: `production/qa/qa-plan-sprint-6-2026-06-12.md`
**Requirement**: Sprint 6 S6-2

**GDD**: `design/gdd/systems-index.md` - Combat Core, Lock-On / Combat Camera, and M0 read -> evade/parry -> counter -> reveal loop.
**Requirement Detail**: M0 tester must understand which defensive answer was available, when the counter window appeared, and why the parry/counter attempt succeeded or failed.
**ADR Governing Implementation**: Control Manifest ADR-0003 / Presentation rules, with ADR-0002 / Core ownership as a secondary constraint.

**Engine**: Unity 6000.3.x + URP | **Risk**: MEDIUM
**Engine Notes**: Presentation must observe confirmed gameplay state and must not own combat truth.

**Control Manifest Rules**:
- Required: Presentation systems observe gameplay truth as read-only snapshots or context.
- Required: Animator/VFX/camera feedback are presentation only.
- Forbidden: Presentation systems must not mutate Combat Core, Target Context, Health, or Locomotion truth.

---

## Acceptance Criteria

- [ ] Parry feedback is visually distinct from dodge, hit reaction, and counter feedback.
- [ ] Counter availability feedback appears only after confirmed combat state opens the counter opportunity.
- [ ] Counter result feedback appears only after confirmed counter execution or resolution.
- [ ] Feedback timing is readable but restrained; it does not obscure enemy telegraph, target, or player pose.
- [ ] Presentation observes gameplay state and does not own combat truth.
- [ ] No new console errors occur during repeated parry/counter attempts.
- [ ] Evidence is captured for parry success, counter availability, and counter result.

---

## Implementation Notes

- Prefer small presentation adapters over changing combat authority.
- Use existing confirmed combat/counter state where available.
- Keep effects restrained and readable in the M0 duel arena.
- Do not add broad HUD, progression, or full VFX systems.
- If a new presentation hook is needed, keep it read-only and scoped to M0.
- Performance/readability budget: feedback must introduce no visible hitch, log spam, or readability regression during repeated parry/counter attempts; if code is added to hot gameplay paths, avoid per-frame allocations.

---

## Out of Scope

- Changing parry/counter combat rules.
- Adding new enemy attacks or multi-enemy behavior.
- Implementing full combat HUD.
- Changing lock-on policy decided in Sprint 5.

---

## QA Test Cases

- **AC-1**: Parry success feedback is distinct.
  - Setup: Enter M0 duel Game View and perform a successful parry.
  - Verify: The feedback can be distinguished from dodge, hit reaction, and counter feedback.
  - Pass condition: A reviewer can name the parry success moment from the capture without explanation.

- **AC-2**: Counter availability is tied to confirmed combat state.
  - Setup: Trigger a parry or state that opens a counter opportunity.
  - Verify: Availability feedback appears only when the counter opportunity is open.
  - Pass condition: No availability cue appears during normal movement, failed defensive timing, or recovery without an open counter window.

- **AC-3**: Counter result feedback is tied to confirmed resolution.
  - Setup: Execute a counter from an available counter window.
  - Verify: Result feedback appears only after confirmed counter execution or resolution.
  - Pass condition: Feedback does not fire on a mere input press that combat rejects.

- **AC-4**: Feedback remains readable and restrained.
  - Setup: Capture repeated parry/counter attempts in the M0 arena.
  - Verify: Enemy telegraph, player pose, target, and camera framing remain readable.
  - Pass condition: Feedback supports the duel read and does not dominate the screen.

- **AC-5**: Presentation does not own gameplay truth.
  - Setup: Review code diff and relevant components.
  - Verify: Presentation reads snapshots/events/context and does not mutate combat, health, target, or locomotion authority.
  - Pass condition: Code review finds no presentation-side gameplay truth ownership.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- `production/qa/evidence/s6-2-parry-counter-visual-feedback-polish.md`
- Game View screenshot sequence or video clip covering parry success, counter availability, and counter result.
- Automated regression results if any code changes affect routing or gameplay state.
- Manual evidence must note whether repeated parry/counter attempts produced visible hitching, log spam, or any readability regression.

**Status**: [x] Created at `production/qa/evidence/s6-2-parry-counter-visual-feedback-polish.md`
**Manual verification**: [x] Parry/counter feedback confirmed readable with no console errors

---

## Completion Notes
**Completed**: 2026-06-16
**Criteria**: 7/7 passing
**Deviations**: None
**Test Evidence**: Visual/Feel — evidence doc at `production/qa/evidence/s6-2-parry-counter-visual-feedback-polish.md`
**Code Review**: APPROVED WITH SUGGESTIONS (2 required fixes applied: enemy material reset removed from ResetFeedback(), private runtime fields renamed to _camelCase per AGENTS.md)

## Dependencies

- Depends on: S5-4, S5-5, S5-6 complete.
- Unlocks: S6-3 Parry/Counter Feedback Smoke Evidence.
