## Why

Sprint 1 proved M0 duel wiring and ownership boundaries, but S2-1 closure review shows readability remains partial for Attack, Dodge, and Parry beats.
Sprint 2 needs a constrained tuning plan that improves readability/feel without moving gameplay truth out of CombatCore and PlayerLocomotion.

## What Changes

- Define S2-2 readability tuning scope for Attack, Dodge, and Parry in M0 duel.
- Define safe tuning surface (timing/config/presentation coupling constraints) and forbidden changes.
- Define evidence-first verification requirements before/after tuning.
- Define manual PlayMode checklist and PASS/PARTIAL/FAIL acceptance classification.
- Define test expectations if any combat timing logic or validation behavior changes.

## Capabilities

### New Capabilities
- `m0-combat-feel-readability`: A constrained combat readability tuning contract for Attack/Dodge/Parry that preserves domain ownership boundaries and enforces evidence-driven verification.

### Modified Capabilities
- None.

## Impact

- Affected planning/docs:
  - `production/sprints/sprint-2.md`
  - `production/qa/qa-plan-sprint-2-2026-05-26.md`
  - `production/epics/m0-first-playable-duel/story-s2-1-m0-sprint-1-playable-duel-closure-review.md`
  - `production/qa/evidence/s2-1-m0-playable-duel-closure-review-2026-05-26.md`
- Expected future implementation surfaces (for apply phase only): CombatCore timing/config boundaries, PlayerLocomotion dodge readability expression, and presentation-layer readability signals.
- No new system ownership transfer; CombatCore and PlayerLocomotion remain authority for gameplay truth.

## Non-goals

- No gameplay implementation in this change proposal phase.
- No Unity submodule edits in this planning step.
- No camera behavior rewrite, enemy AI redesign, memory system redesign, or full animation/VFX polish.
- No RPG expansion (inventory/lore/map/progression/boss/multi-enemy systems).
