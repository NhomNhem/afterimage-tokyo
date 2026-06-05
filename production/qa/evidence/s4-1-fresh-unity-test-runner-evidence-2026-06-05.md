# S4-1 Fresh Unity Test Runner Evidence

**Date**: 2026-06-05
**Story**: `production/epics/m1-memory-fragment-exploration/story-s4-1-fresh-unity-test-runner-evidence.md`
**Sprint**: Sprint 4
**Verdict**: PASS WITH WARNINGS

---

## Summary

S4-1 captured fresh compile and Unity Test Runner evidence for the Sprint 3/Sprint 4 baseline.

Compile smoke passed with 0 errors. EditMode and PlayMode Unity Test Runner passes are now clean after fixing/classifying the two initial EditMode failures.

---

## Evidence Commands

### Compile Smoke

Command:

```powershell
dotnet build .\afterimage-tokyo\afterimage-tokyo.sln --no-restore -v:q /clp:ErrorsOnly
```

Result:

```text
Build succeeded.
720 Warning(s)
0 Error(s)
Time Elapsed 00:00:28.89
```

Classification:
- PASS for compile gate.
- Warnings are non-blocking for S4-1 because there are 0 compile errors.
- Warning count changed after Unity Editor/Test Runner activity; no compile errors were introduced.

### Unity Test Runner - EditMode Full Suite

Initial runner:
- Unity MCP `run_tests`
- Mode: `EditMode`
- Job ID: `6c173ed33c214e4dbcb31fd5baafe2d7`

Result:

| Metric | Count |
|--------|------:|
| Total | 219 |
| Completed | 219 |
| Failed | 2 |

Failures:

| Test | Failure |
|------|---------|
| `NhemBootstrap.Tests.Editor.BootstrapPropertyTests.ExampleTest_VersionMismatch_LogsWarningWhenVersionsDiffer` | Expected exactly one warning, observed 0. |
| `GlassRefrain.Tests.EditMode.M1MemoryRevealFeedbackBridgeTests.CombatDebugOverlayContainsMemoryRevealPlaceholderOnly` | Expected `False`, observed `True`. |

Classification:
- Initial failure was fixed/classified and re-run cleanly.
- `NhemBootstrap.Tests.Editor.BootstrapPropertyTests.ExampleTest_VersionMismatch_LogsWarningWhenVersionsDiffer` failed because `BootstrapContext.Log()` no longer appended to its in-memory `Logs` list. Fixed by restoring `Logs.Add(message)` without enabling direct Unity `Debug.Log`.
- `GlassRefrain.Tests.EditMode.M1MemoryRevealFeedbackBridgeTests.CombatDebugOverlayContainsMemoryRevealPlaceholderOnly` failed because the guardrail used a broad `InputAction` substring and matched the benign method name `UpdateLastInputAction`. Fixed by checking specific forbidden Input System usage patterns instead.

Re-run:
- Unity MCP `run_tests`
- Mode: `EditMode`
- Job ID: `683bdd423e0044cfb78d8882513ba872`

Re-run result:

| Metric | Count |
|--------|------:|
| Total | 219 |
| Passed | 219 |
| Failed | 0 |
| Skipped | 0 |
| Duration | 2.2631197s |

Re-run classification:
- PASS.

### Unity Test Runner - Focused M1 EditMode Set

Initial runner:
- Unity MCP `run_tests`
- Mode: `EditMode`
- Job ID: `7f0c209d6f134ef0b5701747d1682576`
- Requested tests:
  - `GlassRefrain.Tests.EditMode.MemoryInteractionServiceTests`
  - `GlassRefrain.Tests.EditMode.M1InteractionPromptPlaceholderTests`
  - `GlassRefrain.Tests.EditMode.M1MemoryRevealFeedbackBridgeTests`

Result:

| Metric | Count |
|--------|------:|
| Total | 12 |
| Completed | 12 |
| Failed | 1 |

Failure:

| Test | Failure |
|------|---------|
| `GlassRefrain.Tests.EditMode.M1MemoryRevealFeedbackBridgeTests.CombatDebugOverlayContainsMemoryRevealPlaceholderOnly` | Expected `False`, observed `True`. |

Classification:
- Initial failure was fixed by narrowing the guardrail test to forbidden Input System usage patterns instead of any `InputAction` substring.

Re-run:
- Unity MCP `run_tests`
- Mode: `EditMode`
- Job ID: `109cbca193dd4f359f042b6029ec4190`

Re-run result:

| Metric | Count |
|--------|------:|
| Total | 12 |
| Passed | 12 |
| Failed | 0 |
| Skipped | 0 |
| Duration | 0.4463103s |

Re-run classification:
- PASS.

### Unity Test Runner - PlayMode

Initial runner:
- Unity MCP `run_tests`
- Mode: `PlayMode`
- Job ID: `bc28e2e0002d4f349cec151c6e118d0e`

Result:

| Metric | Count |
|--------|------:|
| Total | 2 |
| Passed | 2 |
| Failed | 0 |
| Skipped | 0 |
| Duration | 0.0593417s |

Classification:
- PASS for PlayMode runner evidence.

Re-run:
- Unity MCP `run_tests`
- Mode: `PlayMode`
- Job ID: `4b1bb21e7f584f98be125ba1916ec84c`

Re-run result:

| Metric | Count |
|--------|------:|
| Total | 2 |
| Passed | 2 |
| Failed | 0 |
| Skipped | 0 |
| Duration | 0.0714772s |

Re-run classification:
- PASS.

---

## Console / Environment Classification

| Source | Classification | Notes |
|--------|----------------|-------|
| `dotnet build` | PASS | 0 compile errors, 720 warnings. |
| Unity MCP EditMode runner | PASS | Re-run 219/219 passed after fixing initial failures. |
| Unity MCP focused M1 runner | PASS | Re-run 12/12 passed after fixing guardrail false positive. |
| Unity MCP PlayMode runner | PASS | 2/2 tests passed. |
| Unity MCP console query | TOOLING WARNING | Earlier `execute_code` console query failed with `The filename or extension is too long`; not classified as Unity compile/test failure. |
| Unity submodule status | LOCAL DIRTY WARNING | `Assets/_Recovery/0 (4).unity` and `.meta` are untracked recovery artifacts. They were not modified, staged, or removed by this story. |

---

## Acceptance Criteria Check

| AC | Result | Evidence |
|----|--------|----------|
| Fresh EditMode evidence captured or blocker classified | PASS | Full EditMode re-run 219/219 PASS; focused M1 re-run 12/12 PASS. |
| Fresh PlayMode evidence captured or blocker classified | PASS | PlayMode job `bc28e2e0002d4f349cec151c6e118d0e`, 2/2 PASS. |
| Test command, timestamp, counts, artifact paths recorded | PASS WITH WARNING | Commands/job IDs/counts recorded. Unity MCP did not emit XML/log artifact files; job IDs are recorded as tool evidence. |
| Build/compile state has 0 errors | PASS | `dotnet build` passed with 0 errors. |
| M1 memory interaction focused coverage included | PASS | Focused M1 run included `MemoryInteractionServiceTests`. |
| M1 prompt and reveal feedback focused coverage included | PASS | Focused M1 re-run 12/12 PASS. |
| Existing M0 regression coverage touched by M1 loop included | PASS | Full EditMode re-run 219/219 PASS. |
| Console warnings classified | PASS WITH WARNING | Compile/test/tooling/local dirty classifications recorded. Direct Unity console log extraction was blocked by MCP tooling error. |
| Unity Test Runner blocker includes fallback path | PASS | Blockers listed with next recommended actions. |
| No runtime feature, scene, prefab, or gameplay behavior changed | PASS | Fixes were limited to test guardrail precision and NhemBootstrap in-memory test logging. |
| Evidence written and linked from story completion notes | PASS WITH WARNING | Evidence file exists; story completion notes should be updated by `/story-done`. |

---

## Fix / Classification Notes

Initial EditMode failures were addressed:

1. `M1MemoryRevealFeedbackBridgeTests.CombatDebugOverlayContainsMemoryRevealPlaceholderOnly`
   - Classification: test false positive.
   - Fix: guardrail now checks `UnityEngine.InputSystem`, `InputAction.`, `InputAction `, and `CallbackContext` instead of broad `InputAction`.
2. `NhemBootstrap.Tests.Editor.BootstrapPropertyTests.ExampleTest_VersionMismatch_LogsWarningWhenVersionsDiffer`
   - Classification: in-memory test logging regression.
   - Fix: restored `BootstrapContext.Log()` to append to `Logs` while keeping direct `Debug.Log` disabled.

Recommended next step:

```text
Run `/story-done production/epics/m1-memory-fragment-exploration/story-s4-1-fresh-unity-test-runner-evidence.md`.
```

Remaining warning:
- Unity submodule has untracked recovery files under `Assets/_Recovery/`; not touched by this story.
