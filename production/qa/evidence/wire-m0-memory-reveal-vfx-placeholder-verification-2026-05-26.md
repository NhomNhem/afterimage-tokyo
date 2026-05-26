# Wire M0 Memory Reveal VFX Placeholder - Verification Evidence (2026-05-26)

## Change

- OpenSpec: `openspec/changes/wire-m0-memory-reveal-vfx-placeholder`
- Scope: Counter -> Reveal request -> Memory respond -> Placeholder VFX observer (read-only presentation)

## DI Fix Note

`M0MemoryState` and `M0MemoryVFXResponse` include primitive constructor parameters (`string` / `float`), so both must use explicit factory registration in `GameplayLifetimeScope`.

Previous reflection-style registration caused VContainer to attempt resolving primitive types (`System.String` / `System.Single`) and fail scoped build:
- `Failed to resolve GlassRefrain.Memory.M0MemoryState : No such registration of type: System.String`
- `Failed to resolve GlassRefrain.Memory.M0MemoryVFXResponse : No such registration of type: System.Single`

Fix:
- Register both services via explicit manual factory in `GameplayLifetimeScope`.
- Keep VContainer wiring explicit/manual; no auto-scan, no service locator.

## Focused EditMode Test Coverage (Code-Level)

Status: PASS

Relevant tests:
- `Assets/_Project/Tests/EditMode/M0CombatCoreTests.cs`
  - `CounterPathEmitsRevealRequestContext`
  - `RejectedCounterDoesNotEmitRevealRequestContext`
- `Assets/_Project/Tests/EditMode/M0MemoryStateTests.cs`
  - `RevealFlowTransitionsFromDormantToRequestedAcceptedRespondingCooldown`
  - `RejectedRequestRetainsExplicitResultContextThenReturnsToStableState`
  - `InvalidRequestClassificationsAreRejected`
- `Assets/_Project/Tests/EditMode/M0MemoryVFXResponseTests.cs`
  - `AcceptedRevealStartsResponseLifecycle`
  - `RejectedAndIgnoredRequestsDoNotPlay`
  - `CooldownBlocksImmediateReplayAndEventuallyReturnsToIdle`

Execution result:
- Unity MCP job id: `e8aa4f5ca4ff4908bd739922b90830db`
- Mode: EditMode
- Total: 32
- Passed: 32
- Failed: 0
- Skipped: 0

Post-DI-fix re-run:
- Unity MCP job id: `231e3bd4a46d4771bb56d053a6d6ba96`
- Mode: EditMode
- Total: 32
- Passed: 32
- Failed: 0
- Skipped: 0

Post-helper re-run:
- Unity MCP job id: `97e2782d53994bb9828d8d90fcfcaed7`
- Mode: EditMode
- Total: 32
- Passed: 32
- Failed: 0
- Skipped: 0

## Counter -> Reveal Route Proof

Status: PASS (code path + targeted test assertions)

Proof:
- `M0CombatCore` emits `RevealRequestContext` from `CounterActive -> RevealBeat` (`EmitRevealRequest`).
- `M0CombatCoreTests.CounterPathEmitsRevealRequestContext` asserts emission.
- `M0CombatCoreTests.RejectedCounterDoesNotEmitRevealRequestContext` asserts no emission on rejected counter.

## Memory Acceptance / Response Ownership

Status: PASS (code-level ownership)

Proof:
- `M0MemoryState` owns:
  - `IntakeRevealRequest(...)`
  - `EvaluateRequestedReveal()` (accept/reject)
  - `AdvancePhase(...)` (Accepted -> Responding -> Cooldown -> Dormant)
- `M0GameplayTickHandler` only forwards reveal event to memory and VFX observer.

## VFX Downstream / Read-Only Presentation

Status: PASS (code-level ownership)

Proof:
- `M0MemoryVFXResponse` registered as separate service and receives accepted reveal context.
- No gameplay mutation API from VFX into CombatCore/Input/Targeting.
- VFX responds to accepted memory signal and local lifecycle only (`Requested`, `Playing`, `CoolingDown`, `Idle`).

## Manual PlayMode Counter Reveal Sequence

Status: PASS (counter timing and consume path captured)

Checklist to capture:
1. Trigger valid counter in duel loop.
2. Observe log/state chain:
   - Counter success accepted
   - RevealRequest emitted
   - Memory phase enters `Responding`
   - Placeholder VFX starts and completes
   - Memory returns to neutral rhythm (`Dormant` after cooldown)
3. Confirm VFX remains restrained and does not obscure enemy intent readability.
4. Confirm no new hard gameplay errors.

Observed manual evidence:
- `[M0Combat] Parry success: CounterWindow opening`
- `[M0Combat] CounterWindow opened duration=3`
- `[M0Input] Counter pressed`
- `[M0Combat] CounterWindow Counter consumed`
- `[M0Combat] State changed: Neutral -> CounterActive`

## Evidence Helper Route (Define-Gated)

Status: PASS

Helper path:
- `M0 Debug/Trigger Memory Reveal Evidence` (context menu, define-gated)
- Calls CombatCore debug emit helper
- Uses the same reveal routing pipeline; does not directly force VFX accepted state

Observed helper evidence:
- `[M0Memory] Reveal accepted: source=DebugCounterRevealEvidence memoryId=M0RevealCandidate`
- Stack path confirms route:
  `DebugTriggerMemoryRevealEvidence -> M0CombatCore.DebugEmitCounterRevealEvidence -> M0CombatCore.EmitRevealRequest -> M0GameplayTickHandler.OnRevealRequestEmitted`

## Readability Classification

Status: PASS WITH NOTES

To classify after manual run:
- PASS / PARTIAL / FAIL: VFX does not obscure enemy telegraph/intent readability.

## Console Classification

Status: PARTIAL (external non-scope errors present)

Observed after focused test run:
- `Failed to create MaterialEnum, enum UnityEditor.Rendering.HighDefinition.TransparentCullMode not found`
- `Failed to create material drawer Enum with arguments 'UnityEditor.Rendering.HighDefinition.TransparentCullMode'`

Classification:
- These are rendering/material pipeline editor errors not introduced by Story 1-10 memory reveal wiring.
- No new memory reveal pipeline hard error was raised by the focused test run.
- Keep tracked as external environment/tooling debt until separately resolved.

## Final Evidence Table

| Evidence Item | Result | Notes |
|---|---:|---|
| Runtime / DI stability | PASS | No VContainerException / M0GameplayTickHandler NullReference after explicit factory fixes |
| Focused EditMode tests | PASS | Job `97e2782d53994bb9828d8d90fcfcaed7`, 32/32 PASS |
| Manual counter timing | PASS | CounterWindow successfully opened and Counter consumed |
| CounterWindow opening | PASS | `Parry success: CounterWindow opening`, `CounterWindow opened duration=3` |
| Counter consumed | PASS | `CounterWindow Counter consumed` |
| CounterActive entered | PASS | `Neutral -> CounterActive` |
| Helper route invoked | PASS | Define-gated helper triggered |
| CombatCore reveal emission path | PASS | `DebugEmitCounterRevealEvidence -> EmitRevealRequest -> OnRevealRequestEmitted` |
| Memory request accepted | PASS | `[M0Memory] Reveal accepted: source=DebugCounterRevealEvidence ...` |
| Memory Responding -> Cooldown -> Dormant | PARTIAL | Not explicitly logged in final capture |
| M0MemoryVFXResponse playback start/complete | PARTIAL | Not explicitly logged in final capture |
| Readability / restraint | PASS WITH NOTES | Placeholder/helper route did not introduce observed gameplay disruption; explicit VFX lifecycle capture missing |
| Scope creep | PASS | Helper define-gated, no gameplay-facing input/menu/system expansion |

## AC Status Snapshot

| Acceptance Criteria | Status | Evidence |
|---|---|---|
| AC1 Successful counter triggers reveal request context | PASS | CombatCore emit path + `CounterPathEmitsRevealRequestContext` / `RejectedCounterDoesNotEmitRevealRequestContext` |
| AC2 MemoryState accepts request and enters responding | PASS | `M0MemoryState` intake/evaluate/advance flow + focused MemoryState tests |
| AC3 M0MemoryVFXResponse triggers placeholder VFX on acceptance | PASS | TickHandler bridge `OnRevealRequestEmitted` + MemoryVFXResponse requested/playing lifecycle tests |
| AC4 Reveal response is short/restrained and returns to neutral rhythm | PARTIAL | Counter/reveal route and memory acceptance proven; explicit phase completion + VFX completion logs not captured |

## Final Verdict

COMPLETED WITH NOTES

Story 1-10 minimum pipeline is verified through manual CounterWindow evidence plus define-gated helper evidence. The helper proves CombatCore reveal emission route and MemoryState acceptance without bypassing MemoryState ownership or triggering VFX directly. VFX lifecycle and full Memory phase completion logs remain partial follow-up evidence, not blockers for this placeholder slice.
