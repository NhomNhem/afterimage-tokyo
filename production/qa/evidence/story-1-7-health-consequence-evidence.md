# Story 1-7 Health Consequence — Evidence

> Date: 2026-05-20
> Scope: story-1-7-health-consequence
> Story: production/epics/m0-first-playable-duel/story-1-7-health-consequence.md
> Current verdict: ADEQUATE (AC1-AC4 explicitly traced)

## Unity Test Runner Result

- Runner: Unity Editor Test Runner via MCP
- Fixture: `GlassRefrain.Tests.EditMode.M0HealthConsequenceTests`
- Summary: **PASS 6/6**, Failed 0, Skipped 0
- XML artifact: `C:\Users\truon\AppData\LocalLow\DefaultCompany\afterimage-tokyo\TestResults.xml`

Passed test names:

1. `DamageConsequence_DoesNotMutateCombatCoreDefensiveOwnership`
2. `DamageConsequence_ReducesHealth_AfterResolvedValidCombatOutcome`
3. `HealthConsequenceFiles_DoNotReferenceForbiddenDependencies`
4. `HitReaction_IsEmitted_AfterAcceptedDamageConsequence`
5. `InvalidOrRejectedCombatOutcome_DoesNotReduceHealth`
6. `HealthSnapshot_IsObservable_ThroughDebugReadOnlyAggregate_AfterDamage`

## Acceptance Criteria Trace

### AC1
Damage is applied to Health only after a confirmed resolved combat outcome.
Status: **PASS**

Evidence:
- `DamageConsequence_ReducesHealth_AfterResolvedValidCombatOutcome`
- `InvalidOrRejectedCombatOutcome_DoesNotReduceHealth`

### AC2
Hit Reaction state triggers suppression intent after accepted damage consequence.
Status: **PASS**

Evidence:
- `HitReaction_IsEmitted_AfterAcceptedDamageConsequence`

### AC3
Hit-reaction intent placeholder is emitted after valid player hit/counter consequence.
Status: **PASS**

Note:
- Placeholder emission from health consequence is explicitly covered by passed tests:
  - `HitReaction_IsEmitted_AfterAcceptedDamageConsequence`
  - `DamageConsequence_ReducesHealth_AfterResolvedValidCombatOutcome`
- Full enemy stagger behavior is explicitly out of scope for Story 1-7 and remains pending in later story scope.

### AC4
Health snapshot/state change is observable for debug integration.
Status: **PASS**

Note:
- Explicit debug integration observation is covered by:
  - `HealthSnapshot_IsObservable_ThroughDebugReadOnlyAggregate_AfterDamage`
- This test proves the read-only debug aggregate path carries health `Current` and `Max` after accepted damage.
- Full Debug Overlay UI rendering/wiring is out of scope for Story 1-7 and remains pending.

## Constraints Confirmation

- No CombatCore authority replacement in Health.
- No Story 1-6/F6 harness scope changes required by this evidence cleanup.
- No Animancer implementation.
- No fallback lookup APIs introduced for this evidence update.
- No direct `UnityEngine.Debug.Log/Warning/Error` added by this evidence update.

## Sign-off

- Developer: PASS
- Designer: PENDING
- QA Lead: PENDING
