# Tasks: S2-3 Enemy Telegraph Readability Pass

## 1. Planning Finalization

- [x] 1.1 Confirm S2-3 scope remains readability-only (no AI architecture expansion).
- [x] 1.2 Confirm ownership guardrails are copied into implementation checklist.
- [x] 1.3 Confirm allowed/forbidden file boundaries are accepted before `/opsx:apply`.

## 2. Readability Targets

- [x] 2.1 Define target readability statements for Telegraph/Commit/Active/Recovery.
- [x] 2.2 Define which timing/presentation cues are safe to tune.
- [x] 2.3 Define explicit "cannot change" list (ownership, truth sources, major systems).

## 3. Verification Plan

- [x] 3.1 Define focused test requirements if timing/config logic is changed.
- [x] 3.2 Define manual PlayMode checklist and minimum sample size (>= 3 loops).
- [x] 3.3 Define console classification requirements (new hard errors vs known external warnings).
- [x] 3.4 Define PASS/PARTIAL/FAIL rubric for closure decision.

## 4. Evidence Plan

- [x] 4.1 Prepare evidence template path:
      `production/qa/evidence/s2-3-enemy-telegraph-readability-verification-YYYY-MM-DD.md`
- [x] 4.2 Require evidence table rows for:
      Telegraph, Commit, Active, Recovery, Punish readability, Console classification, Scope creep.
- [x] 4.3 Require architecture-boundary section confirming no ownership drift.

## 5. Ready-for-Apply Gate

- [x] 5.1 Proposal/design/spec reviewed for scope tightness.
- [x] 5.2 No implementation or tuning value changes done in planning phase.
- [x] 5.3 Change is marked ready for `/opsx:apply tune-m0-enemy-telegraph-readability`.

## 6. Implementation Pass (S2-3)

- [x] 6.1 Apply readability timing tuning in `M0EnemyIntentLoopDriver` defaults (Telegraph/Commit/Active/Recovery/Punish).
- [x] 6.2 Add safe duration sanitization guard for authored timing values.
- [x] 6.3 Add readable phase-label reason formatting for debug/overlay traceability.
- [x] 6.4 Add focused tests for phase-label continuity (`M0EnemyIntentTests`).
- [x] 6.5 Add focused tests for enemy reason fallback chain (`M0DebugOverlaySnapshotIntegrationTests`).
- [x] 6.6 Update evidence doc with implementation deltas and verification requirements.

## 7. Verification Pass (S2-3)

- [x] 7.1 Run focused EditMode tests:
      - `M0EnemyIntentTests`
      - `M0DebugOverlaySnapshotIntegrationTests`
- [x] 7.2 Record MCP test-run details and job id.
- [x] 7.3 Record successful run totals (`total/passed/failed`) after failing test is resolved and rerun is green.
- [ ] 7.4 Complete manual PlayMode readability checklist.
- [x] 7.5 Keep evidence status as `IN PROGRESS` until focused tests actually pass.
- [x] 7.6 Promote evidence to `PASS WITH NOTES` after focused pass + explicit manual limitation disclosure.

## Implementation Snapshot — 2026-05-28

Status: IMPLEMENTED / VERIFIED WITH NOTES

Summary:
- S2-3 runtime/test changes are implemented and scoped.
- Focused EditMode MCP initial run failed once (job: `a54912ba772b43d2b80604238ebdfe82`, 16 total / 15 passed / 1 failed).
- Fallback-chain test was corrected to assert intended precedence deterministically.
- Focused EditMode MCP rerun passed (job: `bfb77ed3042a4e4680576973da1d5879`, 16 total / 16 passed / 0 failed).
- Evidence status promoted to `PASS WITH NOTES` with explicit manual PlayMode limitation disclosure.

Next action:
- Optional: rerun manual PlayMode readability sampling for additional qualitative footage in a follow-up evidence pass.
