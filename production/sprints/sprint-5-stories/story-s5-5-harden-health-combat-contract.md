# Story S5-5: [Architecture] Harden Health-Combat Contract

> **Sprint**: Sprint 5
> **Status**: Complete
> **Layer**: Core / Health
> **Type**: Logic
> **Estimate**: 1.0d
> **Priority**: Should Have
> **Owner**: gameplay-programmer
> **Dependencies**: None
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

The tracked tech debt item `harden-m0-health-combat-confirmation-contract` asks to replace string-based resolved-combat gating in `M0HealthDamageReactionModel.IsResolvedCombatOutcome` with a typed contract.

Relevant trace:
- `TR-M0-HEALTH-001` — Health / Damage / Hit Reaction owns damage/application and consequence truth.
- `TR-M0-COMBAT-001` — Combat Core owns combat validation and result truth.
- `TR-M0-CONTRACTS-001` — `M0Contracts.cs` remains contracts-only shared DTO/enum/interface hub.
- `design/gdd/m0-health-damage-ownership.md`
- `design/gdd/combat-core.md`
- `docs/architecture/adr/ADR-0002-m0-gameplay-truth-ownership-boundaries.md`
- `docs/architecture/adr/ADR-0005-m0-shared-contracts-strategy.md`
- `docs/architecture/control-manifest.md`
- `docs/tech-debt-register.md`
- `production/sprints/sprint-5.md`
- `production/qa/qa-plan-sprint-5-2026-06-09.md`
- `afterimage-tokyo/Assets/_Project/Code/Health/M0HealthDamageReactionModel.cs`
- `afterimage-tokyo/Assets/_Project/Code/Core/M0Contracts.cs`

## Architecture Notes

- Governed by ADR-0002: Health owns damage/consequence/reaction after a confirmed combat result; Combat Core owns combat validity and hit resolution context.
- Governed by ADR-0005: the typed contract can live in `M0Contracts.cs` only as DTO/enum data, with no behavior or service logic.
- Control manifest version 2026-05-15 applies: Core remains pure C#, contracts-only, and free of hidden authority or Unity object ownership.

## Engine Notes

- Unity 6000.3.x APIs are not required for the implementation.
- This is a Pure C# Core/Health contract change and should be verified through EditMode tests.

## Performance Budget

- Expected runtime impact: O(1) enum/property check replacing string trim/comparison.
- No per-frame allocation, scene mutation, physics, animation, memory, locomotion, or VFX work is in scope.

## Goal

Remove fragile string matching from health/damage reaction gating and replace it with a typed combat outcome contract while preserving existing M0 health consequence behavior.

## Acceptance Criteria

- [x] A typed resolved-combat outcome contract exists or an existing typed contract is reused.
- [x] `M0HealthDamageReactionModel` no longer relies on string comparison to decide resolved combat outcomes.
- [x] Invalid, null, or unrecognized combat outcomes are rejected safely.
- [x] Existing resolved-combat scenarios still produce the same health/damage reaction behavior.
- [x] Health remains the owner of health values and hit reaction classification after confirmed combat result.
- [x] Combat Core remains the owner of combat action validity and hit resolution context.
- [x] No broad combat, memory, or locomotion behavior changes are introduced.
- [x] Unit tests cover the typed contract and previous string-based scenarios.

## Out of Scope

- Full damage formula redesign
- New stats, armor, equipment, or RPG scaling
- Enemy health redesign
- CombatCore state-machine rewrite
- Presentation or VFX changes

## Implementation Notes

- Prefer adding small typed fields/enums to existing contracts over adding a broad service.
- Keep Domain/Core contracts free of Unity object ownership.
- Do not infer health consequences from presentation strings or debug labels.
- If source guardrail tests exist that scan for string comparisons, update them to assert the new typed path.

## QA Test Cases

- **AC-1**: Typed resolved-combat outcome identifies resolved states.
  - Given: a resolved combat outcome is represented by typed data.
  - When: `M0HealthDamageReactionModel` evaluates it.
  - Then: health/damage reaction logic accepts the resolved outcome.
  - Edge cases: blocked hit, whiff, parry, counter, rejected action.

- **AC-2**: String-based gating is removed.
  - Given: the health model source is inspected.
  - When: the resolved-combat gate is reviewed.
  - Then: it does not rely on string comparisons for combat outcome truth.
  - Edge cases: string constants used only for debug display or evidence labels.

- **AC-3**: Invalid outcomes reject safely.
  - Given: null, default, or unrecognized typed outcomes.
  - When: the health model evaluates them.
  - Then: they do not apply damage as resolved combat.
  - Edge cases: default enum value, missing actor id, uninitialized result.

- **AC-4**: Existing behavior is preserved.
  - Given: current health consequence tests.
  - When: they run after the contract hardening.
  - Then: previously passing behavior still passes.
  - Edge cases: death/defeat threshold, zero/negative damage, repeated damage.

## Test Evidence

**Story Type**: Logic

Required evidence:
- Automated test path from QA plan: `afterimage-tokyo/Assets/_Project/Tests/EditMode/M0HealthCombatContractTests.cs`
- Existing M0 health/damage tests still pass
- Source guardrail or review confirming string-based gating is gone

Expected evidence location:
- `production/qa/evidence/s5-5-harden-health-combat-contract-verification-2026-06-12.md`

**Status**: [x] Created at `production/qa/evidence/s5-5-harden-health-combat-contract-verification-2026-06-12.md`

## Dependencies

- Depends on: None
- Unlocks: safer health/combat consequence work

## Completion Notes

**Completed**: 2026-06-12
**Criteria**: 8/8 passing
**Deviations**: None
**Test Evidence**: Logic story verified by `afterimage-tokyo/Assets/_Project/Tests/EditMode/M0HealthCombatContractTests.cs` and existing M0 health/debug regression suites.
**Verification**: Unity MCP EditMode job `b767f4e90916465080ce6b2ec4f9f489` — 28/28 PASS.
**Code Review**: Complete with fixes applied. Review findings about implicit confirmed outcomes and missing source-id coverage were fixed before closure.
