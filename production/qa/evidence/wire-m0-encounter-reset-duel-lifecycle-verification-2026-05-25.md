# M0 Encounter Reset Duel Lifecycle Verification — 2026-05-25

Change:
`wire-m0-encounter-reset-duel-lifecycle`

Story:
`1-8 [Encounter] Reset & Duel Lifecycle`

Status:
COMPLETED WITH NOTES

## Scope

This verification run covers:
- project path validation
- compile/domain reload health
- focused EditMode tests for reset-related owners
- manual PlayMode dirty -> reset -> clean flow
- console classification for non-blocking warnings vs hard errors

---

## 1) Project Path Verification

Result: PASS

Evidence:
- `Test-Path J:/afterimage-tokyo/afterimage-tokyo` returned `True`.

---

## 2) Compile / Domain Reload

Result: PASS

Procedure:
1. Cleared Unity Console.
2. Triggered refresh with compile request:
   - `refresh_unity(mode=force, scope=all, compile=request, wait_for_ready=true)`
3. Read console for errors:
   - `read_console(types=[error])`

Evidence:
- Unity Console error entries after compile request: **0**.

---

## 3) Focused EditMode Tests

Result: PASS

Run:
- `run_tests(mode=EditMode, include_details=true, include_failed_tests=true, init_timeout=120000, test_names=[...])`
- Job ID: `5f32ad96b2444fef82ae3c9cd50e7f06`
- Poll: `get_test_job(wait_timeout=60)`

Suite summary:
- Total: **47**
- Passed: **47**
- Failed: **0**
- Skipped: **0**
- Result: **Passed**

Target suites covered:
- `GlassRefrain.Tests.EditMode.M0CombatCoreTests` (includes `ResetForEncounter_ForcesNeutralAndClearsTransients`)
- `GlassRefrain.Tests.EditMode.M0PlayerLocomotionTests` (includes `ResetForEncounter_RestoresPositionFacingAndClearsVelocity`)
- `GlassRefrain.Tests.EditMode.M0EnemyIntentTests` (includes `ResetForEncounter_ReturnsModelToIdleAndClearsTelegraphAndPunishWindow`)
- `GlassRefrain.Tests.EditMode.M0TargetContextTests` (includes `ResetForEncounter_ClearsLockOnState`)

---

## Manual PlayMode Reset Flow — Dirty -> Reset -> Clean

Result: PASS

### Dirty state creation

Result: PASS

Evidence observed:
- Player moved away from start position.
- Combat activity occurred through LightAttack / HeavyAttack / Parry / Dodge.
- EnemyIntent left Idle and reached active lifecycle states.
- LockOn was acquired.
- Transient combat/action state was present before reset.

### Reset trigger

Result: PASS

Evidence observed:
- Encounter reset was triggered during active/dirty duel state.
- Reset sequence executed through the M0 encounter lifecycle path.

### After-reset clean state

Result: PASS

Expected clean state was restored:
- CombatState returned to `Neutral`.
- Player transform/locomotion returned to baseline.
- EnemyIntent returned to baseline/Idle.
- TargetContext/LockOn was released or returned to expected clean state.
- Debug Overlay reflected post-reset state as read-only display.
- Gameplay remained playable after reset.

### Before/After Reset Artifact Values

Result: PASS

Observed values captured in the reset validation slice:

| Field | Before Reset (Dirty) | After Reset (Clean) |
| --- | --- | --- |
| CombatState | `DodgeRecovery` | `Neutral` |
| PlayerTransform | `(-3.41, 0.00, -1.44)` | `(0.00, 0.00, 0.00)` |
| EnemyIntent | `Active` | `Idle` |
| LockOnTarget | `enemy-m0-placeholder` | `None` |

### Post-reset smoke

Result: PASS

Observed:
- WASD still works.
- LightAttack still works.
- Dodge still works.
- LockOn can be used/reacquired as expected.
- No new hard gameplay errors were observed.

---

## Console Classification

Result: PASS WITH KNOWN NON-BLOCKING WARNINGS

Observed warnings:
- `[M0Animation] Animation presentation adapter missing; combat continues without animation presentation`
- `[M0Bootstrap] Animation presentation not assigned; animation playback disabled for this M0 smoke run.`
- `[M0Target] SceneAdapter register skipped: object inactive`

Classification:
- Animation presentation warnings are known non-blocking for current M0 verification scope.
- No new hard gameplay errors were produced in this run.

---

## Task Mapping

- `5.1` Compile/domain reload: **PASS**
- `5.2` Focused EditMode tests: **PASS**
- `5.3` Manual reset flow proof: **PASS**
- `5.4` Before/after reset state artifacts: **PASS**
- `5.5` Console classification: **PASS**
- `5.6` Evidence doc update: **PASS**

---

## Notes

- Reset lifecycle is verified for minimum M0 duel loop needs.
- Existing animation presentation warnings remain non-blocking for this change.

---

## Corrective Patch Verification — 2026-05-26

Result: PASS WITH NOTES

Corrective patch commits:
- Submodule: `f308a236 fix: use authored baseline for m0 encounter reset`
- Parent: `f8f3b57a docs: tighten m0 encounter reset evidence`

Focused EditMode tests:
- Job: `58ff61bc0547430990ead51c6d4456b9`
- Result: PASS
- Total: 48
- Passed: 48
- Failed: 0

Special focus:
- `ResetForEncounter_UsesProvidedAuthoredBaselineEvenWhenNonZero`: PASS
- `ResetForEncounter_ForcesNeutralAndClearsTransients`: PASS
- `ResetForEncounter_ReturnsModelToIdleAndClearsTelegraphAndPunishWindow`: PASS
- `ResetForEncounter_ClearsLockOnState`: PASS

Compile/domain reload:
- Refresh/compile request completed.
- Console 0-error gate: NOT CLEAN.
- Observed external/editor material errors:
  - `Failed to create MaterialEnum, enum UnityEditor.Rendering.HighDefinition.TransparentCullMode not found`
  - `Failed to create material drawer Enum with arguments 'UnityEditor.Rendering.HighDefinition.TransparentCullMode'`

Classification:
- These errors are not from scoped 1-8 reset lifecycle code.
- No new gameplay reset lifecycle compile/test failure was observed.
- Focused reset tests passed 48/48.
- Treat as external rendering/material pipeline issue to track separately.

Story impact:
- Non-blocking for 1-8 reset lifecycle correctness.
- Blocking for a strict global 0-console-error gate until tracked/fixed separately.

Verdict:
APPROVED WITH NOTES for Story 1-8.
