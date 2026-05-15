## Why

Stories 1-1 through 1-4 are complete. Foundation scene, camera-relative movement, lock-on wiring, and player attack resolution are all established. Combat Core now owns combat validity and result truth; Target Context owns lock-on target truth; Locomotion owns movement truth. The remaining missing layer before the first duel loop is readable is enemy-side intent communication.

The M0 duel prototype cannot prove `read → evade/parry → counter → reveal` without a readable enemy. The enemy must communicate intent before impact — through telegraph, commit, active threat, recovery, and a visible punish window — so that player defensive choices feel informed and Combat Core's validation has something to validate against. Without this layer, the duel loop has no meaningful enemy-side pressure and the prototype cannot be evaluated.

`M0EnemyIntentModel` is already a compiled Pure C# FSM skeleton with `EnterTelegraph`, `EnterCommit`, `EnterActive`, `EnterRecovery`, `ClosePunishWindow`, and `Tick()` implemented. Contract types (`EnemyIntentState`, `EnemyIntentSnapshot`, `TelegraphStateSnapshot`, `EnemyAttackIntentContext`, `EnemyAttackTagSet`, `EnemyPunishWindowContext`) are defined in `M0Contracts.cs`. `M0EnemyIntentModel` is registered in `GameplayLifetimeScope`. The Debug Overlay already has an `EnemyIntent` channel. What is missing is the tick driver wiring and a minimal loop driver that runs the FSM through its authored duel rhythm.

## What Changes

- `M0GameplayTickHandler` gains an injected `M0EnemyIntentModel` reference and calls `model.Tick(dt)` each frame
- A new `M0EnemyIntentLoopDriver` MonoBehaviour implements the scripted single-enemy duel loop (idle → telegraph → commit → active → recovery → idle) with authored timing constants
- `M0EnemyIntentLoopDriver` is wired into the scene alongside `Enemy_M0TargetablePlaceholder`
- The enemy intent snapshot is already routed through the Debug Overlay aggregator; this change confirms the live data path is connected and readable
- No damage, no health mutation, no combat result truth mutation, no AI navigation, no animation authority, no VFX, no Memory VFX trigger

## Capabilities

### New Capabilities

- `enemy-intent-fsm`: `M0EnemyIntentModel` is ticked each frame and advances through authored intent states; snapshot is live and observable
- `enemy-intent-tick-wiring`: `M0GameplayTickHandler` injects and ticks `M0EnemyIntentModel`; `M0EnemyIntentLoopDriver` drives the scripted duel sequence

### Modified Capabilities

None — no existing spec-level requirement changes; no existing system ownership changed.

## Impact

- **Code**: `M0GameplayTickHandler` extended with enemy intent tick injection; new `M0EnemyIntentLoopDriver` MonoBehaviour added to Bootstrap or Enemy layer; scene wired with loop driver component on `Enemy_M0TargetablePlaceholder` or sibling GameObject
- **APIs**: No new contract types required — all types already exist in `M0Contracts.cs`
- **Dependencies**: Depends on Stories 1-1 through 1-4 (all Complete); depends on `M0EnemyIntentModel` skeleton (already compiled); depends on `GlassRefrain.Enemy` asmdef (already present)
- **Systems**: Enemy Intent becomes a live observable truth layer; Combat Core remains unchanged as combat validity/result owner; Target Context remains unchanged as lock-on target owner
