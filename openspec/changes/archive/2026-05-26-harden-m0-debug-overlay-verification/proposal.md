## Why

Story 1-9 is currently partial, and Sprint 1 verification needs a reliable, repeatable way to prove duel-loop state visibility in PlayMode without relying on ambiguous logs alone.
We need a narrow hardening pass so Debug Overlay evidence can be trusted while preserving ownership boundaries.

## What Changes

- Harden M0 Debug Overlay verification for the existing duel-loop read model:
  - Overlay visibility in PlayMode
  - CombatState field from CombatCore snapshot
  - EnemyIntent field from EnemyIntent snapshot
  - LastInput field from Input snapshot/router
  - CounterWindow field from CombatCore snapshot (if present in snapshot)
  - LockOnTarget field from TargetContext snapshot
- Keep Debug Overlay read-only and non-authoritative.
- Allow minimal display binding fixes only when data already exists in domain snapshots.
- Add focused verification checklist and evidence artifact requirements (screenshot/log/manual proof).
- Do not alter gameplay behavior, timings, targeting rules, or encounter lifecycle behavior.

## Capabilities

### New Capabilities
- `debug-overlay-verification`: Defines M0 verification requirements for read-only Debug Overlay state visibility and evidence capture.

### Modified Capabilities
- None.

## Impact

- Affected systems:
  - Presentation debug overlay adapter/read model wiring
  - Gameplay tick snapshot forwarding to overlay (read-only pathway)
  - QA evidence workflow for Story 1-9
- M0 loop impact:
  - Improves verification clarity for `read -> evade/parry -> counter -> reveal` without changing gameplay truth.
- Ownership boundary affected:
  - Debug Overlay remains Presentation-only observer; gameplay truth stays in CombatCore / EnemyIntent / TargetContext / InputRouter domain owners.

## Non-goals

- Gameplay behavior changes
- Combat timing/state machine changes
- Target acquisition policy changes
- Enemy AI behavior changes
- Encounter lifecycle behavior changes
- New debug command console
- Save/load/checkpoint work
- UI visual polish
- Animation/camera/VFX changes
- Full HUD system
