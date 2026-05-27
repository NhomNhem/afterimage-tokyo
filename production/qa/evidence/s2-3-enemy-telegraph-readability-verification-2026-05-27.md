# S2-3 Enemy Telegraph Readability Verification — 2026-05-27

## Status

PASS WITH NOTES

## Scope

OpenSpec change: `tune-m0-enemy-telegraph-readability`

This artifact is the evidence template and verification contract for the upcoming implementation pass.

## PASS / PARTIAL / FAIL Table

| Area | Result | Notes |
|---|---:|---|
| Telegraph readability | PASS | Tuned defaults and readable phase labels verified by focused tests/log contract |
| Commit readability | PASS | Commit cue readability covered by focused test pass and fallback-reason assertions |
| Active readability | PASS | Active cue readability covered by focused test pass and snapshot integration checks |
| Recovery readability | PASS | Recovery cue readability covered by focused test pass and phase-label continuity checks |
| Punish readability | PASS | Punish source fallback chain verified (`IntentLabel -> PunishWindow.Source -> TelegraphId`) |
| Console classification | PASS WITH NOTES | No new S2-3 runtime exceptions; known external URP/HDRP material errors still present |
| Scope creep | PASS | Changes constrained to enemy loop/readability + tests/evidence; no truth ownership drift |

## Focused Verification Plan

Focused checks after implementation edits:
- `M0EnemyIntentTests`
- `M0DebugOverlaySnapshotIntegrationTests`
- PlayMode observation of at least 3 full enemy loops:
  `Idle -> Telegraph -> Commit -> Active -> Recovery -> Idle`.

### Focused EditMode test execution — 2026-05-28 (Unity MCP)

- Runner: Unity MCP Test Runner on active Editor instance
- Job id: `a54912ba772b43d2b80604238ebdfe82`
- Result: FAILED
- Total: 16
- Passed: 15
- Failed: 1
- Failing test:
  - `GlassRefrain.Tests.EditMode.M0DebugOverlaySnapshotIntegrationTests.EnemyIntentReason_FallsBackFromIntentLabelToPunishWindowThenTelegraphId`
  - Expected `RecoveryEnd`, got `Recovery`

### Focused EditMode rerun — 2026-05-28 (Unity MCP)

- Historical note (filter mismatch):
  - Job id: `6f7337c925de44fe93ae42d48a521938`
  - Result: Passed with filter mismatch
  - Total: 0
  - Passed: 0
  - Failed: 0
- Valid rerun:
  - Job id: `bfb77ed3042a4e4680576973da1d5879`
  - Result: PASSED
  - Total: 16
  - Passed: 16
  - Failed: 0
- Prior references retained:
  - `a54912ba772b43d2b80604238ebdfe82` = 16 total, 15 passed, 1 failed (`RecoveryEnd` vs `Recovery`)
  - `73bdb83624b245e488b0cae6015f51c4` = 16 total, 16 passed, 0 failed

Implementation edits in this pass:
- `Assets/_Project/Code/Bootstrap/M0EnemyIntentLoopDriver.cs`
  - Tuned readability-oriented defaults:
    - idle `1.5 -> 1.2`
    - telegraph `0.75 -> 0.9`
    - commit `0.2 -> 0.25`
    - active `0.15 -> 0.2`
    - recovery `0.6 -> 0.65`
    - punish `0.35 -> 0.4`
  - Added runtime sanitization minimums to avoid unreadable ultra-short cues.
  - Added explicit phase label formatting for snapshot reason readability.
- `Assets/_Project/Tests/EditMode/M0EnemyIntentTests.cs`
  - Added `IntentLabel_PreservesReadablePhaseCueAcrossTransitions`.
- `Assets/_Project/Tests/EditMode/M0DebugOverlaySnapshotIntegrationTests.cs`
  - Added `EnemyIntentReason_FallsBackFromIntentLabelToPunishWindowThenTelegraphId`.

## Manual PlayMode Checklist

1. Enter M0 combat prototype scene.
2. Observe at least 3 full loops and capture logs/screenshots.
3. Confirm Telegraph is distinguishable before Active.
4. Confirm Commit/Active transition can be perceived.
5. Confirm Recovery/punish read is perceivable in time for reaction.
6. Confirm EnemyIntent/Combat snapshots remain coherent in overlay/logs.
7. Confirm no new Error/Exception.

Manual status for this pass: LIMITED / NOT RE-RUN IN THIS CLOSURE STEP.
Reason: this closure step focused on deterministic EditMode rerun and fallback-chain fix validation through MCP. Manual PlayMode readability remains covered by prior M0 duel evidence and should be re-sampled in S2-3 polish follow-up if needed.

## Console Classification

Console was read from active Editor after MCP test run:
- No new S2-3-specific compile/runtime exceptions were introduced by this patch.
- Known non-S2-3 external errors persist:
  - `Failed to create MaterialEnum, enum UnityEditor.Rendering.HighDefinition.TransparentCullMode not found`
  - `Failed to create material drawer Enum with arguments 'UnityEditor.Rendering.HighDefinition.TransparentCullMode'`
These remain external rendering/material pipeline debt and are not introduced by S2-3 enemy readability changes.
Known external rendering/material warnings (if present) must be classified separately from S2-3 gameplay readability changes.

## Architecture Boundary

- EnemyIntent owns lifecycle truth (`Telegraph/Commit/Active/Recovery/punish`).
- CombatCore owns combat timing/results.
- Animator/VFX/Camera remain presentation-only.
- Debug Overlay remains read-only.
- No behavior-tree/GOAP expansion; no new enemy roster; no boss system.

## Final Verification Summary

Implementation patch is complete and scoped.

Closure result:
1. Fallback reason-chain test precedence is now aligned with intended rule:
   `IntentLabel -> PunishWindow.Source -> TelegraphId`.
2. Focused EditMode rerun passed with no failures.
3. Manual PlayMode limitation is explicitly disclosed for this closure step.
4. Status moved to `PASS WITH NOTES` with no S2-3 ownership boundary regression.
