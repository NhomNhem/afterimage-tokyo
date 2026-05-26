## 1. Scope Guardrails

- [x] 1.1 Confirm Story 1-9 scope-in/scope-out and preserve read-only overlay ownership boundary in implementation notes.
- [x] 1.2 Confirm allowed/forbidden file list before code edits; block gameplay behavior changes in this change.

## 2. Overlay Binding Verification

- [x] 2.1 Verify PlayMode overlay visibility path is active and can be toggled/observed in current M0 scene.
- [x] 2.2 Verify CombatState display binding reads CombatCore snapshot only.
- [x] 2.3 Verify EnemyIntent display binding reads EnemyIntent snapshot only.
- [x] 2.4 Verify LastInput display binding reads input snapshot/router only.
- [x] 2.5 Verify CounterWindow display binding reads CombatCore snapshot only (if snapshot field exists).
- [x] 2.6 Verify LockOnTarget display binding reads TargetContext snapshot only.
- [x] 2.7 Add minimal missing display binding only where snapshot data already exists; do not add new gameplay truth paths.

## 3. Test and Evidence Hardening

- [x] 3.1 Add/update focused tests for Debug Overlay snapshot integration if current coverage is insufficient.
- [x] 3.2 Run focused verification (compile + relevant tests + manual PlayMode overlay checks).
- [x] 3.3 Capture evidence artifact with required proof:
  - overlay visible
  - CombatState
  - EnemyIntent
  - LastInput
  - CounterWindow
  - LockOnTarget
  - PASS/PARTIAL/FAIL table for:
    - Overlay Visible
    - CombatState
    - EnemyIntent
    - LastInput
    - CounterWindow
    - LockOnTarget
    - Read-only Boundary
    - Console Classification
- [x] 3.4 Record any non-blocking external console errors separately from scoped overlay verification outcome.

## 4. Documentation and Closure

- [x] 4.1 Create/update evidence file under `production/qa/evidence/` with screenshot/log/manual proof table.
- [x] 4.2 Update OpenSpec tasks/proposal status based on actual evidence completeness (PASS/PARTIAL/FAIL).
- [x] 4.3 Prepare for `/test-evidence-review` with explicit blocker/non-blocker classification.

## Closure Snapshot — 2026-05-26

Verdict: READY FOR TEST-EVIDENCE-REVIEW

Evidence:
- `production/qa/evidence/harden-m0-debug-overlay-verification-2026-05-26.md`

Summary:
- Overlay visible/readable in PlayMode: PASS
- CombatState overlay path: PASS
- EnemyIntent overlay path: PASS
- LastInput overlay path: PASS
- CounterWindow overlay path: PASS
- LockOnTarget overlay path: PASS
- Read-only boundary: PASS
- Console classification: PASS

Scope:
- No gameplay behavior changes
- No camera/animation/VFX/save-load/encounter lifecycle changes
- No direct keyboard/mouse/gamepad polling added
