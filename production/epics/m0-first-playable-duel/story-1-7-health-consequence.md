# Story 1-7: [Consequence] Health & Hit Reactions

> **Epic**: M0 First Playable Duel
> **Status**: Complete
> **Layer**: Core
> **Type**: Logic/Integration
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-21

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

- [x] Damage is applied to Health only after a confirmed `CombatCore` hit result.
- [x] Hit Reaction state triggers movement/control suppression in `M0PlayerLocomotion`.
- [x] Hit-reaction intent placeholder is emitted after valid player hit/counter consequence.
- [x] Health snapshot/state change event is observable for debug integration (full Debug Overlay rendering is out of scope in this story).

---

## Requirement Trace

**TR-M0-HEALTH-001**: Health / Damage / Hit Reaction owns damage/application and consequence truth.

- AC1 maps to TR-M0-HEALTH-001 consequence gating: Health applies damage only from resolved `CombatCore` outcomes.
- AC2 maps to TR-M0-HEALTH-001 reaction consequence: Hit Reaction emits suppression context consumed by `M0PlayerLocomotion`.
- AC3 maps to TR-M0-HEALTH-001 reaction consequence: Successful resolved hits/counters emit health-owned hit-reaction intent placeholder.
- AC4 maps to TR-M0-HEALTH-001 debug visibility: Health consequence snapshot/event is exposed for read-only debug integration.

Boundary note: Health/Hit Reaction observes resolved combat outcomes and applies consequence truth; it must not replace or bypass `CombatCore` action validity/result authority.

---

## Implementation Notes

- Use the `M0HealthDamageReactionModel` skeleton.
- Ensure hit reactions are short and return control to the player predictably.
- Coordinate with `M0PlayerLocomotion` via `MovementRestrictionContext`.

---

## Out of Scope

- [Story 1-8]: Encounter reset on defeat.
- Full enemy stagger gameplay implementation.
- Full Debug Overlay UI rendering/wiring for health channels.

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

## Performance Budget

- Scope impact: Consequence-only processing for resolved hit outcomes (no authority changes to `CombatCore`).
- CPU budget target: no measurable frame spike from health/reaction consequence handling in 1v1 M0 duel.
- Allocation budget target: no per-frame GC allocation in hot consequence paths.
- If any regression is observed, capture evidence in story test notes before completion.

---

## Test Evidence

**Story Type**: Logic/Integration
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/M0HealthConsequenceTests.cs`
- Manual verification: Debug Overlay showing health bars and suppression reason.

**Status**: [x] Automated and debug-integration evidence complete (see `production/qa/evidence/story-1-7-health-consequence-evidence.md`)

---

## Dependencies

- Depends on: Story 1-4, Story 1-5
- Unlocks: Story 1-8

---

## Completion Notes
**Completed**: 2026-05-21
**Criteria**: 4/4 passing
**Deviations**: None blocking. Follow-up recorded: `harden-m0-health-combat-confirmation-contract` (replace string-based resolved-combat gating with typed resolved-combat outcome contract).
**Test Evidence**: Logic + integration evidence at `production/qa/evidence/story-1-7-health-consequence-evidence.md` (Unity MCP EditMode PASS 6/6).
**Code Review**: Complete — APPROVED WITH SUGGESTIONS.
