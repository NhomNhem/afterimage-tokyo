## Why

Story 1-10 is the remaining Sprint 1 visual-feel slice for proving the last step of the M0 loop (`counter -> reveal`). We need a minimal, testable reveal pipeline that confirms successful counter outcomes can drive memory response state and restrained placeholder VFX without moving gameplay truth into presentation.

## What Changes

- Wire successful counter result from `M0CombatCore` to emit `RevealRequestContext` on the existing combat truth path.
- Ensure `MemoryState` accepts valid reveal requests and enters `Responding`, then returns to neutral rhythm through existing state flow.
- Trigger `M0MemoryVFXResponse` placeholder playback only when `MemoryState` accepts reveal.
- Add focused tests for memory acceptance/rejection and responding transition.
- Add evidence-first verification checklist and artifacts for PlayMode counter->reveal readability.
- Keep VFX downstream and non-authoritative; no combat/input/camera/AI behavior changes.

## Capabilities

### New Capabilities
- `memory-reveal-vfx-placeholder`: Minimum counter-to-memory reveal signal path with restrained placeholder VFX evidence for M0.

### Modified Capabilities
- None.

## Impact

- Affected systems:
  - Combat truth output (`RevealRequestContext` emission on successful counter)
  - Memory domain state transition (`Accept -> Responding -> return`)
  - Memory presentation observer (`M0MemoryVFXResponse` placeholder trigger)
  - Debug/evidence surface for readable verification
- Affected code areas (expected):
  - Combat / Memory / Bootstrap integration files
  - Focused EditMode tests around `MemoryState`
  - Evidence docs under `production/qa/evidence`
- M0 loop impact:
  - Completes a minimum verifiable `counter -> reveal` leg without adding full reveal cinematics/polish systems.

## Non-goals

- No animator-driven reveal reactions.
- No cinematic camera, timeline, cutscene, slow-motion, or polished VFX pass.
- No memory lore UI, progression/rewards, save/load, or checkpoint behavior.
- No enemy AI behavior rework beyond existing flow needed to produce counter evidence.

## Completion Note — 2026-05-26

Status: completed-with-notes

Story 1-10 minimum pipeline is verified for M0 placeholder scope:
- Counter path to reveal request is wired and tested.
- MemoryState acceptance path is wired and tested.
- Define-gated evidence helper confirms reveal route invocation and memory acceptance in PlayMode.

Notes:
- Manual CounterWindow timing is now proven but remains harder to reproduce consistently than helper route.
- Explicit logs for memory phase completion (`Responding -> Cooldown -> Dormant`) and VFX playback completion were not captured in final manual log set.
- These remain non-blocking evidence notes for placeholder slice closure.
