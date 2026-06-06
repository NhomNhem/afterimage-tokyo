# harden-m0-runtime-composition-nhemdi Verification — 2026-06-06

## Verdict

PASS — automated verification passed and manual PlayMode checklist was confirmed by tester.

## Scope

OpenSpec change: `harden-m0-runtime-composition-nhemdi`

Implementation hardens M0/M1 runtime composition by replacing broad `GameplayLifetimeScope` scene discovery fallback with explicit serialized scene references for:

- `MemoryRaycastProProbe`
- `MemoryFragment[]`

The slice preserves NhemDI-generated registration for pure/runtime services and keeps scene object injection as an explicit Unity scene instance special case.

## Changed Runtime Surface

- `afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
  - Added explicit `memoryProbe` and `memoryFragments` serialized references.
  - Removed `FindFirstObjectByType<MemoryRaycastProProbe>()`.
  - Removed broad `FindObjectsByType<MemoryFragment>()`.
  - Kept diagnostics through `INhemLogger`.
- `afterimage-tokyo/Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`
  - Assigned existing scene `MemoryRaycastProProbe` and `MemoryFragment` references to `GameplayLifetimeScope`.
- `afterimage-tokyo/Assets/_Project/Tests/EditMode/SceneComposition_test.cs`
  - Added guardrails for explicit memory scene composition and scene reference assignment.

## Ownership Classification

| Area | Result | Notes |
|---|---:|---|
| Bootstrap/DI | PASS | `GameplayLifetimeScope` composes explicit scene references; no broad memory scene search remains. |
| NhemDI services | PASS | Existing pure/runtime services remain NhemDI/generated or existing explicit registration where already scoped. |
| MemoryInteractionService | PASS | No behavior or truth ownership changes. |
| MemoryState | PASS | No reveal/collect truth changes. |
| Presentation/UI/VFX | PASS | No authority changes. |
| CombatCore/Input/Locomotion/TargetContext | PASS | No runtime behavior changes in this slice. |

## Automated Evidence

| Check | Result | Evidence |
|---|---:|---|
| Compile smoke | PASS | `dotnet build afterimage-tokyo/afterimage-tokyo.sln --no-restore` exited 0. Existing vendor/package warnings only. |
| OpenSpec strict validation | PASS | `openspec validate harden-m0-runtime-composition-nhemdi --strict` passed. |
| Diff whitespace check | PASS | `git -C afterimage-tokyo diff --check` passed after line-ending cleanup. |
| Owned runtime search fallback scan | PASS | `rg "FindObject|FindFirstObject|FindAnyObject|FindObjectsByType|Resources\\.Load|ServiceLocator" afterimage-tokyo/Assets/_Project/Code -g "*.cs"` returned no matches. |
| Direct Debug scan | PASS WITH NOTES | Matches only in generated `M0InputActions.cs`; no new owned runtime direct `Debug.Log*` calls. |
| Focused EditMode composition + memory suite | PASS | Unity MCP EditMode: 20/20 passed. Included `SceneComposition_test`, S3/S4 memory prompt/reveal/log tests, and `MemoryInteractionServiceTests`. |
| M0 defensive regression | PASS | Unity MCP EditMode: `M0DefensiveResolutionTests` 23/23 passed. |
| PlayMode suite | PASS | Unity MCP PlayMode: 2/2 passed. |

## Console Classification

| Console Class | Result | Notes |
|---|---:|---|
| Errors | PASS | No project compile/runtime errors reported by Unity MCP during focused checks. |
| Warnings | PASS WITH NOTES | Console includes pre-existing vendor/analyzer warnings (`UDR0001`, `UDR0005`, obsolete API warnings) and one pre-existing project warning on `M0EnemyIntentLoopDriver._initialized`. No new blocker from this slice was identified. |

## Manual PlayMode Checklist

Manual tester console evidence was provided after the explicit scene reference wiring. The log confirms the new composition path injected the explicit memory scene references and that Interact reached the accepted memory path. Tester then confirmed the remaining visual/log/spam checklist items passed in PlayMode.

| Step | Result | Notes |
|---|---:|---|
| Explicit memory scene composition injected | PASS | Console evidence: `[M0Bootstrap] Memory DI injected: probe=True fragments=1`. |
| Eligible fragment prompt visible | PASS | Tester confirmed PlayMode pass. |
| Interact accepted | PASS | Console evidence: `[M1Memory] Interaction result: fragmentId=memory-fragment outcome=Accepted reason=Reveal accepted by MemoryState`. |
| Reveal feedback appears once | PASS | Tester confirmed PlayMode pass. |
| Runtime memory log appends one entry | PASS | Tester confirmed PlayMode pass. |
| Spam/duplicate Interact does not replay or append incorrectly | PASS | Tester confirmed repeat-interaction parity. |

## PASS / PARTIAL / FAIL Summary

| Category | Result |
|---|---:|
| Compile | PASS |
| OpenSpec | PASS |
| Source guardrails | PASS |
| Focused EditMode | PASS |
| M0 regression | PASS |
| PlayMode tests | PASS |
| Manual PlayMode checklist | PASS |

## Follow-Up

No follow-up is required for this change. The OpenSpec change is ready for review, archive, and commit when approved.
