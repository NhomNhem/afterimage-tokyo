# Story 1-6 Defensive Wiring — Evidence

> Date: 2026-05-20  
> Scope: create-m0-playable-combat-prototype-scene  
> Story: story-1-6-defensive-wiring.md  
> Verdict: PASS

## Automated Test Evidence

Test file:

`Assets/_Project/Tests/EditMode/M0DefensiveResolutionTests.cs`

Coverage summary:

- Parry success when enemy intent is ParryEligible.
- Parry fail when enemy intent is not ParryEligible.
- CounterWindow opens on successful parry.
- Counter is rejected before Neutral.
- Counter is accepted after ParryRecovery -> Neutral.
- CounterWindow expires correctly.
- Counter consumes CounterWindow and enters CounterActive.

## Manual PlayMode Evidence

Manual sequence:

```txt
F6 -> Q -> wait CombatState Neutral -> E
```

Required log checkpoints observed:

```txt
[M0InputDiag] performed action=DebugForceParryEligibleActive control=/Keyboard/f6
[M0Debug] DebugForceParryEligibleActive input pressed
[M0Debug] Forced enemy ParryEligible Active for 3s...
[M0Input] Parry pressed
[M0Combat] State changed: Neutral -> ParryStartup
[M0DebugOverlay] Snapshot update received combatState=ParryStartup enemyState=Active
[M0Combat] State changed: ParryStartup -> ParryActive
[M0DebugOverlay] Snapshot update received combatState=ParryActive enemyState=Active
[M0Combat] Parry success: CounterWindow opening
[M0Combat] CounterWindow opened duration=3
[M0Combat] State changed: ParryRecovery -> Neutral
[M0Input] Counter pressed
[M0Combat] CounterWindow Counter consumed
[M0Combat] State changed: Neutral -> CounterActive
```

## Verification Notes

Confirmed:

- Bootstrap passes.
- Enemy intent loop transitions.
- Debug Overlay receives enemy/combat snapshots.
- F6 real harness invokes `M0EnemyIntentLoopDriver`.
- Forced Active remains stable long enough for Q.
- Q succeeds while enemyState is Active.
- CounterWindow opens.
- E consumes CounterWindow after combat returns Neutral.
- Combat enters CounterActive.

## Code Review Constraints

Confirmed:

- No CombatCore rule change.
- No fallback lookup added.
- No direct `UnityEngine.Debug.Log/Warning/Error` added.
- Animation refs remain runtime-optional/deferred.
- OnDestroy null guards added.
- Dead diagnostic preprocessor comments cleaned.

## Sign-off

Developer: PASS  
Designer: PASS  
QA: PASS  
Archive recommendation: PASS after gate re-run
