## Context

This change plans S2-3 only. It does not implement tuning yet.

M0 ownership is already established:
- EnemyIntent: telegraph lifecycle truth.
- CombatCore: combat result/timing truth.
- Presentation systems (Animator/VFX/Camera/UI/Debug): read-only or visual-only.

S2-3 must improve readability while preserving those boundaries.

## What "Enemy Telegraph Readability" Means in M0

Readability is successful when a tester can reliably answer:
1. "What is the enemy about to do?" during Telegraph.
2. "When is commitment locked?" at Commit/Active.
3. "When is my punish/defense timing available?" across Active/Recovery and punish window.
4. "Why did I succeed/fail?" from visible cues plus snapshot/log evidence.

## Safe Tuning Surface (Allowed)

- Phase durations in enemy telegraph loop settings/data.
- Non-authoritative cue timing alignment (animation/VFX/camera readouts that follow EnemyIntent snapshot).
- Debug overlay presentation labels/ordering for readability (read-only display only).
- Threshold/label readability notes in evidence artifacts.

## Forbidden Changes (Not Allowed in S2-3)

- Moving authority out of EnemyIntent or CombatCore.
- Changing combat resolution ownership or CounterWindow truth.
- Behavior-tree/GOAP architecture expansion.
- Adding enemy classes/roster/boss logic.
- Root motion as gameplay authority.
- Input binding redesign for this story.

## Required Verification Evidence

1. Focused EditMode test result (if timing/config logic changes are proposed in apply phase).
2. Manual PlayMode capture for phase readability:
   - Telegraph distinct from Commit
   - Commit distinct from Active
   - Recovery/punish readability
3. Console classification:
   - No new hard gameplay errors
   - Known external warnings explicitly classified
4. Scope classification:
   - No ownership drift
   - No out-of-scope systems changed

## Manual PlayMode Checklist (for apply/verify phase)

1. Enter M0 combat prototype scene.
2. Observe at least 3 full enemy intent loops.
3. Record whether Telegraph cues are distinguishable before Active.
4. Record whether Commit/Active transition is perceivable.
5. Record whether Recovery/punish read is perceivable in time for player decision.
6. Confirm CombatCore and EnemyIntent state traces remain coherent in overlay/log.
7. Confirm no new Error/Exception in console.

## PASS / PARTIAL / FAIL Criteria

- PASS:
  - Telegraph/Commit/Active/Recovery cues are consistently distinguishable in repeated runs.
  - No authority drift and no hard gameplay errors.
- PARTIAL:
  - Some phases readable but one or more transitions remain ambiguous or inconsistent.
  - No authority drift, but further tuning needed.
- FAIL:
  - Readability not improved or regressed; or ownership boundaries are violated; or new hard gameplay errors introduced.

## Allowed / Forbidden Implementation Files (for future apply)

Allowed (expected):
- `Assets/_Project/Code/Enemy/*`
- `Assets/_Project/Code/Bootstrap/M0EnemyIntentLoopDriver.cs`
- `Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs` (only if required for read-path orchestration, not truth migration)
- `Assets/_Project/Tests/EditMode/M0EnemyIntentTests.cs`
- `production/qa/evidence/s2-3-enemy-telegraph-readability-verification-YYYY-MM-DD.md`

Forbidden (without explicit separate approval):
- Combat authority files that change result ownership:
  - `Assets/_Project/Code/Combat/M0CombatCore.cs` (except strictly read-only integration if explicitly approved later)
- Save/load, progression, roster, boss, large AI framework files
- Scene/prefab/material churn unrelated to telegraph readability proof
