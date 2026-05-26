Status: completed-with-notes

## Why

Sprint 1 is currently at risk, and Story 1-8 is the final Must Have needed to close the M0 duel loop with a reliable reset flow. We need a minimal, testable encounter lifecycle so one-player/one-enemy combat can return to a clean playable state without scene reload hacks.

## What Changes

- Add a minimal M0 encounter reset lifecycle covering: duel start, active duel, reset request, reset complete.
- Define reset behavior across existing ownership boundaries:
  - Combat Core reset to `Neutral` and clear transient combat/action windows.
  - Player Locomotion reset to known start transform/state suitable for replay.
  - Enemy Intent loop/model reset to known initial idle/start state.
  - LockOn/TargetContext reset to `None` (or explicit valid initial target if configured by design).
  - Input/runtime transient state cleared so stale intents do not leak post-reset.
- Add one minimal reset trigger path for M0 testing/evidence (debug/smoke trigger only; no full restart UI).
- Require debug overlay to remain read-only and reflect post-reset state accurately.
- Add explicit evidence checklist for before/after reset snapshots and console validation.

## Capabilities

### New Capabilities
- `encounter-reset-duel-lifecycle`: Defines minimal encounter lifecycle and reset contract for M0 one-player/one-enemy duel replayability.

### Modified Capabilities
- `target-context-release`: Clarify reset-driven release behavior so target truth returns to `None` (or defined initial target) during encounter reset.

## Impact

- Affected systems:
  - Encounter framework bootstrap/runtime orchestration
  - Combat state reset hooks
  - Player locomotion reset hooks (transform/state)
  - Enemy intent loop/model reset hooks
  - Target context release/reset integration
  - Debug overlay read model (display only)
- No new save/load, checkpoint, multi-enemy, boss lifecycle, or restart menu systems.
- M0 loop impact: increases repeatability and debuggability of `read -> evade/parry -> counter -> reveal` by guaranteeing clean reruns after each duel/reset.

## Non-goals

- Save/load or checkpoint persistence
- Scene transitions or full encounter manager framework
- Multi-enemy orchestration or boss lifecycle
- Restart UI/menu, cutscenes, progression, loot/reward plumbing
- Animation-authoritative reset logic, camera-authoritative gameplay reset, or debug overlay-owned truth

## Completion Note — 2026-05-25

M0 Encounter Reset & Duel Lifecycle is verified as completed-with-notes.

Verified:
- Dirty duel state can be created.
- Encounter reset can be triggered.
- Combat, locomotion, enemy intent, and target context return to clean playable state.
- Overlay remains read-only.
- Compile/domain reload passed.
- Focused EditMode reset tests passed.
- Manual PlayMode before/after reset evidence passed.
- Console classification found no new hard gameplay errors.

Known notes:
- Existing animation presentation warnings remain non-blocking for M0.
