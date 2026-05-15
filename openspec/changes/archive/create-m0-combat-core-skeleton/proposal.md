## Why

M0's `read → evade/parry → counter → reveal` loop needs a combat authority layer. Combat Core must own combat validation and result truth — not Input, Locomotion, Animation, or Enemy systems. This skeleton establishes the minimum Combat Core state model, action request/result contracts, action lock/recovery context, CounterWindow placeholder, reveal request context placeholder, and a read-only combat snapshot for Debug Overlay before downstream systems start depending on it.

## What Changes

- Introduce a minimal M0 Combat Core capability.
- Define pure C# combat state model (Neutral, AttackStartup/Active/Recovery, DodgeStartup/Active/Recovery, ParryStartup/Active/Recovery, CounterWindow, CounterActive, HitReact, RevealBeat, Disabled).
- Define combat action request model (CombatActionType, CombatActionRequest).
- Define combat action result model (CombatActionResult, CombatResolutionResult).
- Define ActionLockContext and RecoveryContext for cross-system lock/recovery handoff.
- Define CounterWindow placeholder state (open/closed, source, remaining duration).
- Define RevealRequestContext placeholder (source context type, combat result source).
- Expose read-only M0CombatSnapshot for Debug Overlay and downstream observers.
- Keep Combat Core's authority boundary explicit: validation shape without full validation behavior.
- Add edit-mode tests for basic request/result/snapshot behavior.

## Capabilities

### New Capabilities
- `m0-combat-core-skeleton`: Minimal combat truth state model, action request/result contracts, action lock/recovery request context, CounterWindow placeholder, reveal request context placeholder, read-only combat snapshot for Debug Overlay.

### Modified Capabilities
- None. (Existing Input, Locomotion, and Target context capabilities are unchanged.)

## Impact

- `Assets/_Project/Code/Core` (new or refined contracts — CombatActionRequest, CombatActionResult, ActionLockContext, RecoveryContext, RevealRequestContext, M0CombatSnapshot)
- `Assets/_Project/Code/Combat` (new Combat Core state model FSM skeleton)
- `Assets/_Project/Tests/EditMode` (new Combat Core test coverage)
- M0 combat-truth ownership and downstream observation boundaries
