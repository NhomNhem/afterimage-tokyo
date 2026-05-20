# Tasks Reconciliation: Wire M0 Health & Hit Reactions

> **Story**: production/epics/m0-first-playable-duel/story-1-7-health-consequence.md  
> **Change**: wire-m0-health-hit-reactions  
> **Design**: openspec/changes/wire-m0-health-hit-reactions/design.md  
> **Evidence**: production/qa/evidence/story-1-7-health-consequence-evidence.md

---

## Corrected Story 1-7 Outcome (Truth Source)

- [x] AC1 PASS: damage applies only after resolved valid combat outcome
- [x] AC2 PASS: hit-reaction suppression intent is emitted
- [x] AC3 PASS: hit-reaction placeholder intent is emitted
- [x] AC4 PASS: health Current/Max observable through read-only debug aggregate path
- [x] Evidence verdict: ADEQUATE
- [x] Unity MCP EditMode Test Runner: PASS 6/6
- [x] Code review: APPROVED WITH SUGGESTIONS (no blockers)

---

## Completed (Evidence-Backed)

### 1. Health Model Enhancement
- [x] 1.1 Verify `Assets/_Project/Code/Health/M0HealthDamageReactionModel.cs` exists
- [x] 1.2 Required skeleton fields present (`maxHealth`, `currentHealth`, `state`, `lastDamageResult`, `hitReaction`, `defeat`, `latestSnapshot`)
- [x] 1.3 Skeleton completeness verified (no missing fields required for corrected Story 1-7 scope)
- [x] 1.4 `SnapshotChanged` event exists for observation
- [x] 1.5 `ApplyDamage(DamageApplicationContext request)` exists
- [x] 1.6 `ApplyDamage` behavior verified for corrected scope (validation, clamp, state update, hitReaction/defeat, snapshot refresh)
- [x] 1.7 Forbidden dependency scan evidence present for health-scope files

### 10. EditMode Tests (Corrected Story 1-7 Scope)
- [x] 10.2 Damage is not applied without resolved valid combat outcome (covered by rejection-path tests)
- [x] 10.6 Health decreases by expected amount after accepted damage
- [x] 10.13 EnemyIntent does not directly mutate health (forbidden dependency scan evidence)
- [x] 10.14 Input does not directly mutate health (forbidden dependency scan evidence)
- [x] 10.15 TargetContext does not directly mutate health (forbidden dependency scan evidence)
- [x] 10.16 Debug snapshot exposes current/max health and reaction state (AC4 explicit proof test)
- [x] 10.17 Debug access path is read-only (debug aggregate consumption proof)
- [x] 10.21 Forbidden API scan PASS for scoped files
- [x] 10.22 Unity EditMode test run PASS (6/6)

---

## Deferred / Out of Corrected Story 1-7 Scope

- [ ] 2.1-2.3 Damage constants/mapping framework (Light/Heavy/Counter mapping) not proven in corrected scope
- [ ] 3.1-3.5 Typed CombatCore result event contract (`ResultChanged`, `HitConfirmed` payload contract) not proven in corrected scope
- [ ] 4.1-4.9 Full runtime wiring from CombatCore result stream to player/enemy health models not proven in corrected scope
- [ ] 5.5-5.6 PlayMode suppression timing verification not performed for health consequence path
- [ ] 6.1-6.9 Enemy stagger context implementation/verification out of corrected Story 1-7 scope
- [ ] 7.1-7.7 Explicit VContainer registration path verification for health models not proven in this evidence pass
- [ ] 8.1-8.9 Debug overlay UI label wiring for health/reaction/stagger not proven (only read-only aggregate path proven)
- [ ] 9.1-9.5 Scene wiring/manual inspector setup not proven for corrected scope
- [ ] 10.1, 10.3-10.5, 10.7-10.12, 10.18-10.20 not proven in corrected Story 1-7 scope
- [ ] 11.1-11.13 Full manual PlayMode health consequence verification not performed
- [ ] 12.1-12.18 Full broad scope-exclusion sweep not fully proven beyond current evidence checks
- [ ] 13.1-13.5 Full regression suite rerun/proof not part of corrected Story 1-7 evidence pass

---

## Follow-Up Candidates

- [ ] harden-m0-health-combat-confirmation-contract  
  Reason: `M0HealthDamageReactionModel` currently gates resolved combat outcome via string `ContextLabel` parsing.
- [ ] add-playmode-health-consequence-verification
- [ ] wire-health-debug-overlay-labels
- [ ] verify-health-vcontainer-registration-path
- [ ] add-typed-combat-outcome-event-contract
- [ ] implement-enemy-stagger-context-if-still-required-by-future-corrected-story
- [ ] add-full-regression-suite-for-health-consequence

---

## Sign-Off Status

- [x] Developer: PASS
- [ ] Designer: PENDING
- [ ] QA Lead: PENDING

---

> **Note:** This reconciliation is documentation-only and reflects corrected Story 1-7 scope truth. It does not claim unperformed PlayMode verification, scene UI label wiring, or enemy stagger implementation.
