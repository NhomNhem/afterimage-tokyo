## 1. Scope and Baseline Alignment

- [ ] 1.1 Confirm S2-2 scope against `production/sprints/sprint-2.md` and S2-1 closure review evidence.
- [ ] 1.2 Record explicit safe-tuning surface (CombatCore/Locomotion authority preserved, presentation downstream-only).
- [ ] 1.3 Record explicit forbidden changes list for S2-2 (no root motion authority, no gameplay truth in Animator/VFX/Camera/UI, no broad refactor).

## 2. Readability Criteria Definition

- [ ] 2.1 Define Attack readability criteria (windup/active/recovery clarity + success/failure interpretation).
- [ ] 2.2 Define Dodge readability criteria (start/commit/recovery clarity + spatial readability).
- [ ] 2.3 Define Parry readability criteria (timing clarity + success/failure + CounterWindow readability).
- [ ] 2.4 Define PASS/PARTIAL/FAIL thresholds for each axis and overall S2-2 verdict.

## 3. Verification and Evidence Plan

- [ ] 3.1 Define before/after evidence requirements (captures/logs/notes) for each readability axis.
- [ ] 3.2 Define mandatory console classification format (blocking vs non-blocking vs unrelated external issues).
- [ ] 3.3 Define evidence table schema for S2-2 closure report.
- [ ] 3.4 Define sign-off roles and minimum manual verification expectations per Sprint 2 QA plan.

## 4. Manual PlayMode Checklist

- [ ] 4.1 Define Attack checklist steps in PlayMode.
- [ ] 4.2 Define Dodge checklist steps in PlayMode.
- [ ] 4.3 Define Parry checklist steps in PlayMode.
- [ ] 4.4 Define regression checks for core loop continuity (`read -> evade/parry -> counter -> reveal`).

## 5. Test Policy for Timing/Logic Changes

- [ ] 5.1 Define rule: if no timing/logic contract changes, rerun focused existing tests only.
- [ ] 5.2 Define rule: if timing/logic contract changes, add/update focused EditMode tests before closure.
- [ ] 5.3 Define required test evidence output format (suite list, pass/fail count, failure classification).

## 6. OpenSpec and Execution Readiness

- [ ] 6.1 Mark which follow-up items need separate OpenSpec changes if scope expands beyond S2-2.
- [ ] 6.2 Run planning review to confirm no gameplay implementation is included in this change.
- [ ] 6.3 Confirm apply-readiness for S2-2 implementation phase without committing planning artifacts yet.
