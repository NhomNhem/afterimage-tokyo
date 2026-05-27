## Context

Sprint 2 Story S2-2 targets readability and feel stabilization for Attack/Dodge/Parry in the M0 duel loop.
S2-1 review confirms current behavior is playable but partially readable under pressure.
This design defines implementation constraints so tuning can happen safely without breaking gameplay ownership boundaries.

## Goals / Non-Goals

**Goals:**
- Define what readability tuning means in measurable terms for Attack, Dodge, and Parry.
- Define safe tuning levers for CombatCore/Locomotion/presentation timing expression.
- Keep CombatCore authoritative for combat timing/results/CounterWindow/reveal request.
- Keep PlayerLocomotion authoritative for dodge movement/facing/recovery/restrictions.
- Require evidence artifacts and PASS/PARTIAL/FAIL reporting for each tuning pass.

**Non-Goals:**
- No broad combat architecture refactor.
- No gameplay truth migration to Animator/VFX/Camera/UI/Debug Overlay.
- No root-motion authority.
- No new enemy/boss/RPG systems.
- No scope expansion into save/load, progression, lore UI, or encounter lifecycle redesign.

## Decisions

### Decision 1: Readability tuning is defined as phase clarity, not mechanic expansion

Readability for Attack/Dodge/Parry is measured by whether testers can reliably identify windup/active/recovery and success/failure outcomes in real time.

**Rationale:**
S2 is stabilization, not feature expansion.

**Alternative considered:** adding new combat mechanics to improve feel.
**Rejected because:** it changes scope and masks baseline readability issues.

### Decision 2: Safe tuning surface is constrained to existing ownership boundaries

Allowed future tuning surface:
- CombatCore timing/config values and transition readability signals (while preserving state authority).
- PlayerLocomotion dodge expression parameters and authored readability cues tied to existing state.
- Presentation timing alignment (Animator/VFX/Camera) as downstream-only response.

Forbidden future tuning surface:
- Animator events applying gameplay outcomes.
- VFX/camera deciding combat validity.
- Input polling shortcuts that bypass existing input routing.

**Rationale:**
Preserves the proven M0 architecture and keeps regressions debuggable.

**Alternative considered:** temporary mixed authority between core and presentation for faster feel iteration.
**Rejected because:** it creates hidden truth and unstable behavior.

### Decision 3: Evidence-first gate is mandatory for each tuning increment

Any implementation increment for S2-2 must produce:
- before/after evidence table,
- manual PlayMode checklist results,
- console classification,
- explicit scope creep status,
- focused tests only when timing/logic contract changes.

**Rationale:**
Prevents subjective “feels better” changes without reproducible proof.

**Alternative considered:** rely on ad-hoc playtest feedback only.
**Rejected because:** cannot reliably close acceptance criteria.

## Risks / Trade-offs

- **[Risk] Readability tuning drifts into gameplay behavior changes**
  → **Mitigation:** require ownership checklist and forbidden-change audit in each evidence report.

- **[Risk] Tuning becomes purely visual and misses core timing clarity**
  → **Mitigation:** require logs/snapshots for combat phase transitions plus manual readability notes.

- **[Risk] Overfitting to one tester’s perception**
  → **Mitigation:** use repeatable checklist with PASS/PARTIAL/FAIL per axis and sign-off roles from Sprint 2 QA plan.

- **[Risk] Regressions in counter/reveal loop while tuning parry/dodge timing**
  → **Mitigation:** rerun focused core tests and smoke path checks whenever timing logic changes.

## Migration Plan

1. Baseline capture from current M0 duel (pre-tuning evidence snapshot).
2. Apply minimal scoped tuning change set (future apply phase).
3. Run focused verification and manual checklist.
4. Classify results PASS/PARTIAL/FAIL with console classification.
5. If regression found, revert affected tuning set and retest.

Rollback strategy:
- Revert tuning commits only (no broad rollback).
- Re-run baseline checklist to confirm previous readable state.

## Open Questions

1. Should S2-2 include only config-level timing tweaks first, with presentation timing alignment split into S2-6/S2-8?
2. What minimum sample size is required for manual readability confidence (single QA session vs two sessions)?
3. If counter readability improves but dodge readability regresses, is split delivery acceptable or must S2-2 ship as one balanced bundle?
