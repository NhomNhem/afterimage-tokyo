# S3-2 Memory Fragment Interaction Verification — 2026-05-28

## Status

IN PROGRESS

## Scope

OpenSpec change: `implement-m1-memory-fragment-interaction`

Implemented scope:
- `MemoryFragmentDefinition` ScriptableObject (static metadata/config only)
- `MemoryFragment` runtime component with interaction radius eligibility
- `MemoryInteractionService` orchestration service via VContainer registration
- Interact input action wiring (`M0InputActions.inputactions` + `M0DirectPlayerInput`)
- Tick orchestration route (`M0GameplayTickHandler` -> `MemoryInteractionService.Tick`)
- Focused EditMode tests for interaction route and duplicate handling safety

Out of scope and unchanged:
- CombatCore timing/results
- EnemyIntent lifecycle
- TargetContext ownership
- Camera ownership
- Inventory/save/quest/dialogue/lore/progression systems

## PASS / PARTIAL / FAIL

| Item | Result | Notes |
|---|---:|---|
| Interact intent route exists | PASS | `M0DirectPlayerInput` now reads `Interact` action and tick handler forwards to service |
| Eligible fragment detection | PASS | `MemoryFragment` radius-based eligibility consumed by service |
| Service-owned orchestration | PASS | `MemoryInteractionService` owns use-case flow and requests MemoryState |
| MemoryState truth ownership | PASS | `M0MemoryState` still performs accept/reject via `IntakeRevealRequest` + `EvaluateRequestedReveal` |
| Duplicate interaction safety | PASS | Duplicate fragment interaction returns `DuplicateIgnored` outcome |
| ScriptableObject static boundary | PASS | `MemoryFragmentDefinition` stores static fields only |
| Presentation-only truth boundary | PASS | No UI/VFX/Animancer ownership shift introduced |
| Manual PlayMode run | PARTIAL | Manual scene verification not executed in this patch pass |
| Scene/prefab change classification | PARTIAL | No intentional scene/prefab edit recorded in this patch |

## Focused EditMode Tests

Added:
- `Assets/_Project/Tests/EditMode/MemoryInteractionServiceTests.cs`
  - `Tick_WithEligibleFragmentAndInteract_AcceptsThroughMemoryState`
  - `Tick_WithoutEligibleFragmentAndInteract_IsSafe`
  - `Tick_DuplicateInteraction_IsIgnoredSafely`

Run status:
- Unity MCP EditMode focused run completed (2026-05-29):
  - Job `e4ed31cafccc43a6814ccde61f435f27`
  - total=3, passed=3, failed=0, skipped=0
  - Targeted tests:
    - `MemoryInteractionServiceTests.Tick_WithEligibleFragmentAndInteract_AcceptsThroughMemoryState`
    - `MemoryInteractionServiceTests.Tick_WithoutEligibleFragmentAndInteract_IsSafe`
    - `MemoryInteractionServiceTests.Tick_DuplicateInteraction_IsIgnoredSafely`
- Unity MCP MemoryState accept/reject path run completed:
  - Job `25b923982db44e6abde625fc031462e0`
  - total=7, passed=7, failed=0, skipped=0
- Unity MCP DI/manual wiring guardrail run completed:
  - Job `e2694e453ef141ea9785ffeef27da88c`
  - total=1, passed=1, failed=0, skipped=0
  - Test: `M0MemoryStateTests.VContainerScopeRemainsManualWiring`

## Console / Domain Classification

Unity MCP console snapshot (Error/Warning) after focused runs:
- Warning: Unity Test Framework `IPrebuildSetup` and `IPostBuildCleanup` logs (non-blocking test infrastructure warnings).
- Exception log entry: `Saving results to ... TestResults.xml` (test framework reporting output, non-S3-2 blocker in this context).
- Error (external/non-scope): HDRP material enum drawer mismatch:
  - `Failed to create MaterialEnum, enum UnityEditor.Rendering.HighDefinition.TransparentCullMode not found`
  - `Failed to create material drawer Enum with arguments 'UnityEditor.Rendering.HighDefinition.TransparentCullMode'`
  - Classified as known external render/material tooling issue, not introduced by S3-2 Memory Fragment interaction code.

No new S3-2-scope compile/runtime exception was observed in the focused test runs.
No new direct `UnityEngine.Debug.*` calls were introduced by this patch.

## Manual PlayMode Checklist

Pending:
- Load gameplay scene with at least one `MemoryFragment`.
- Approach fragment and verify eligibility behavior.
- Press Interact and verify accepted flow.
- Press Interact again and verify duplicate-safe behavior.
- Classify console warnings/errors as S3-2 scope vs external warnings.
- Tooling limitation (2026-05-29): Unity MCP `execute_code` failed in this session with `mono.exe: The filename or extension is too long`, so automated/manual-assist PlayMode capture could not be completed from MCP.

### Manual PlayMode Evidence Snapshot — 2026-05-29

Verdict: `IN PROGRESS`

What this capture proves:
- Runtime/bootstrap stability is present.
- Gameplay input map includes `Interact`.
- Core M0 loop still runs.
- No S3-2-scope crash/error was observed in the captured logs.

What this capture does not yet prove:
- Nearby/eligible `MemoryFragment` state.
- `Interact` pressed while fragment is eligible.
- `MemoryInteractionService` request/result log.
- `MemoryState` accept/reject result tied to fragment interaction.
- Duplicate second-interact handling (`already collected` / safe ignore / reject).

Second focused capture attempt status:
- Attempted to run another focused manual-assist capture via Unity MCP on 2026-05-29.
- MCP `execute_code` is currently blocked in this environment with:
  - `Error running ... mono.exe: The filename or extension is too long.`
- Because of this tooling blocker, end-to-end fragment interaction evidence could not be captured directly by MCP in this run.

## Architecture Boundary Check

- Input remains raw intent source (`Interact` only).
- `MemoryInteractionService` owns orchestration.
- `MemoryState` remains reveal/collect truth source.
- ScriptableObject remains static definition/config only.
- Camera/CombatCore/EnemyIntent ownership boundaries unchanged.

## Known Limitations

- Manual PlayMode evidence is not captured yet in this update.
- Scene placement/authoring for a concrete playable fragment still requires Unity editor verification.

## Follow-up Rules

- If manual PlayMode confirms the route and no S3-2 errors: keep `PASS WITH NOTES` or upgrade to `PASS`.
- If interaction fails in-scene due to wiring/placement: downgrade to `PARTIAL` and open focused fix story.

---

## Pre-Commit Re-Review Snapshot — 2026-05-29

Verdict: `APPROVED WITH NOTES (NOT READY TO COMMIT)`

Pre-commit scope/boundary review results:
- PASS: S3-2 runtime scope remains Memory Fragment interaction only.
- PASS: `MemoryState` remains reveal/collect truth owner.
- PASS: `MemoryInteractionService` remains use-case orchestration owner.
- PASS: no `FindObjectOfType`, `Resources.Load`, or service locator introduced in S3-2 files.
- PASS: no direct `UnityEngine.Debug.Log/Warning/Error` introduced in S3-2 files.
- PASS: `MemoryFragmentDefinition` remains static data/config only.
- PASS: no CombatCore timing/result logic changes.
- PASS: no EnemyIntent lifecycle changes.
- PASS: no TargetContext/camera ownership rewrite.

Outstanding blockers before commit:
1. Manual PlayMode checklist remains pending.
2. Working tree currently contains unrelated dirty files in submodule:
   - `Packages/manifest.json`
   - `Packages/packages-lock.json`
   - `qodana.yaml` (untracked/staged in submodule at review time)
   These must be excluded from S3-2 staging.

Commit readiness:
- Not ready until focused tests run + manual checklist classification is recorded + staging is scope-clean.

## Manual PlayMode Interaction Capture — 2026-05-29

### Verdict

`PASS WITH NOTES`

This capture proves the core S3-2 interaction path for the first interaction attempt.

| Item | Result | Evidence / Notes |
|---|---:|---|
| Memory DI wiring | PASS | `[M0Bootstrap] Memory DI injected: probe=True fragments=1` confirms the runtime memory dependencies were injected and one fragment was registered. |
| Interact input path | PASS | `F` / Interact triggered the memory interaction flow during PlayMode. |
| MemoryInteractionService request/result | PASS | `MemoryInteractionService` logged `outcome=Accepted reason=Reveal accepted by MemoryState`. |
| MemoryState acceptance | PASS | The accepted outcome confirms the interaction request was accepted by MemoryState. |
| No VContainerException crash | PASS | Runtime continued without DI crash. |
| M0 gameplay loop regression | PASS | Movement/combat/enemy intent continued running during the capture. |
| MemoryRaycastProProbe debug raycast | PARTIAL / FOLLOW-UP | Probe repeatedly logged `hitName=None`; classified as debug-probe mismatch because gameplay interaction succeeds through MemoryInteractionService fragment registry/distance criteria. |
| Duplicate interaction handling | PENDING / PARTIAL | Needs explicit second-interact capture showing rejected/ignored/already-collected behavior, unless captured in a later log. |

### Classification

The core S3-2 gameplay path is functional:

`Interact → MemoryInteractionService → MemoryState accepted`

`MemoryRaycastProProbe` is not treated as gameplay truth and is not a blocker for S3-2. It should be aligned in a follow-up so debug evidence uses the same eligibility criteria as `MemoryInteractionService`.
