## Why

M0 manual evidence confirms LockOn acquire/focus works, but second-press behavior is currently unresolved as a product decision. In the latest verification pass, pressing Tab once acquires/maintains target, while pressing Tab again keeps LockOn active. This behavior is tracked as follow-up and must be explicitly decided before further targeting polish.

For M0 duel readability and control clarity, we adopt Option B:

- Press Tab when unlocked: acquire valid target
- Press Tab when locked: release current target
- Press Tab again: acquire valid target again

This change is decision + wiring only. It does not broaden system scope.

## What Changes

- Define LockOn second-press behavior as toggle acquire/release for M0.
- Wire `M0TargetContext` handling for LockOn intent:
  - `None -> Target` on first valid press
  - `Target -> None` on second press
  - `None -> Target` on next valid press
- Keep existing input binding and existing intent-routing architecture.
- Update debug/evidence expectations for `LockOn Target` field transitions.

## Capabilities

### New Capabilities

- `m0-lockon-toggle-release`: lock state toggles between acquired target and released state on repeated LockOn intent.

### Modified Capabilities

- `m0-lockon-acquire-focus`: now explicitly includes second-press release behavior for M0.

## Impact

- **Code**: `M0TargetContext`, existing LockOn input intent routing integration points, debug snapshot/overlay expectations for `LockOn Target`.
- **Tests/Evidence**: add/update tests and manual evidence for `None -> Enemy -> None -> Enemy` sequence.
- **No architecture refactor**: target truth remains in Target Context; input remains intent-only emitter.

## Story

- **Story**: `[Targeting] LockOn Second-Press Toggle Release Decision & Wiring`

## Non-goals

- No Combat Core changes.
- No Parry/Counter changes.
- No Memory State / Memory VFX changes.
- No camera feature additions.
- No input binding changes.
- No Animancer/root motion/KCC/NavMesh changes.
- No targeting architecture refactor.
