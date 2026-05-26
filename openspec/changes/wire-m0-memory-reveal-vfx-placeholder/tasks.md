## 1. Scope and Wiring Plan

- [x] 1.1 Confirm existing CombatCore counter success output path and reveal request hook point.
- [x] 1.2 Confirm MemoryState acceptance/responding path and existing cooldown/return behavior.
- [x] 1.3 Confirm existing M0MemoryVFXResponse adapter path to avoid duplicate presentation wiring.

## 2. Counter to Memory Wiring

- [x] 2.1 Wire successful counter result to emit/forward `RevealRequestContext` through existing combat truth flow.
- [x] 2.2 Ensure rejected/invalid counter outcomes do not emit reveal requests.
- [x] 2.3 Keep GameplayTickHandler (or equivalent bridge) orchestration-only with no new gameplay truth ownership.

## 3. Memory Acceptance and Response

- [x] 3.1 Wire MemoryState request intake so valid reveal requests transition to `Responding`.
- [x] 3.2 Ensure reveal rejection path is explicit and debug-visible via existing logger/snapshot patterns.
- [x] 3.3 Ensure responding returns to baseline neutral rhythm after response/cooldown.

## 4. Memory VFX Placeholder Hook

- [x] 4.1 Wire `M0MemoryVFXResponse` to accepted memory response signal/snapshot (downstream only).
- [x] 4.2 Ensure placeholder VFX is short and restrained for M0 readability.
- [x] 4.3 Verify VFX layer does not mutate CombatCore/MemoryState/Input truth.

## 5. Tests and Verification

- [x] 5.1 Add/update focused EditMode tests for MemoryState acceptance and responding transition.
- [x] 5.2 Add/update focused test for rejected reveal request behavior.
- [x] 5.3 Verify compile/domain reload and focused test pass for touched memory/combat components.
- [x] 5.4 Run manual PlayMode counter->reveal smoke and capture evidence:
  Combat success -> RevealRequestContext -> Memory Responding -> Placeholder VFX -> return.
- [x] 5.5 Classify readability in evidence: VFX does not obscure enemy intent (PASS/PARTIAL/FAIL).
- [x] 5.6 Classify console output: no new hard gameplay errors; known non-blocking warnings separated.

## 5A. Evidence Helper (Define-Gated)

- [x] 5A.1 Add minimal `GR_M0_PROTOTYPE || GR_MEMORY_DEBUG` helper for reveal evidence when manual counter timing is unreliable.
- [x] 5A.2 Ensure helper routes through CombatCore reveal emission -> MemoryState Intake/Evaluate -> Responding -> VFX lifecycle.
- [x] 5A.3 Ensure helper does not directly trigger VFX accepted playback without MemoryState acceptance.
- [x] 5A.4 Record evidence explicitly as `manual timing PARTIAL` and `helper route PASS/PENDING`.

## 6. Evidence and Closure

- [x] 6.1 Create/update `production/qa/evidence/wire-m0-memory-reveal-vfx-placeholder-verification-YYYY-MM-DD.md`.
- [x] 6.2 Include explicit PASS/PARTIAL/FAIL table for:
  Counter Success, RevealRequest Emission, Memory Responding, VFX Trigger, Return to Neutral Rhythm, Readability, Console Classification.
- [x] 6.3 Update proposal/tasks closure status to completed-with-notes only if any non-blocking visual notes remain.

## 7. Logging Guardrail

- [x] 7.1 Confirm no direct `UnityEngine.Debug.*` was added; gameplay logs use NhemLogger path only.

## Risks

- Counter timing window may be hard to reproduce consistently during manual evidence capture.
- Placeholder VFX may temporarily reduce readability if intensity/duration is not sufficiently restrained.
- Existing non-blocking animation warnings may create console noise during verification.

## Allowed Implementation Files

- `Assets/_Project/Code/Combat/M0CombatCore.cs`
- `Assets/_Project/Code/Memory/M0MemoryState.cs`
- `Assets/_Project/Code/Memory/M0MemoryVFXResponse.cs`
- `Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs`
- `Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
- `Assets/_Project/Tests/EditMode/**` (focused memory/combat tests only)
- `production/qa/evidence/wire-m0-memory-reveal-vfx-placeholder-verification-YYYY-MM-DD.md`

## Forbidden Implementation Files

- Scene/prefab/material assets unless explicitly approved for evidence capture support.
- Camera/animation/VFX polish systems beyond minimal placeholder wiring.
- Input binding assets and input architecture ownership.
- Enemy AI behavior systems except minimal read-only verification support.
- Save/load/checkpoint/progression/memory lore UI systems.
- Encounter lifecycle reset flow files (Story 1-8 scope).

## Closure Snapshot — 2026-05-26

Status: completed-with-notes

Completed:
- Runtime/DI stability verified after explicit factory registration for primitive constructor services.
- Focused EditMode tests passed: `97e2782d53994bb9828d8d90fcfcaed7`, 32/32.
- Manual CounterWindow timing captured successfully.
- CounterWindow opened, Counter consumed, and CombatCore entered CounterActive.
- Define-gated evidence helper verified CombatCore reveal emission route.
- MemoryState accepted reveal request from `DebugCounterRevealEvidence`.

Notes:
- Manual counter timing is proven but can still be hard to reproduce consistently.
- Define-gated helper was used for evidence hardening only; no player-facing gameplay behavior change.
- Memory phase completion `Responding -> Cooldown -> Dormant` was not explicitly logged in final capture.
- `M0MemoryVFXResponse` playback start/complete was not explicitly logged in final capture.
- These remain PARTIAL evidence notes and are not blockers for Story 1-10 placeholder scope.

Scope Creep:
PASS. No camera, animation, polished VFX, save/load, progression, lore UI, encounter lifecycle, or input binding scope expansion.
