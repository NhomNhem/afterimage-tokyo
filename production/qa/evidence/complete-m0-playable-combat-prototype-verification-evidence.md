# Complete M0 Playable Combat Prototype Verification — Evidence

Date: 2026-05-21 (final manual PlayMode capture update)  
Change: `complete-m0-playable-combat-prototype-verification`  
Scene: `Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`  
Verdict: PASS for story-done blockers (visual polish follow-ups remain PARTIAL)

## Scope Statement

Verification/testability cleanup only. No gameplay behavior expansion.

## Root Cause Resolved

- Root cause:
  - `M0LocomotionSettings` was previously resolved as default struct through DI, causing zero velocity/no visible movement.
- Fix:
  - Explicit factory/registration for `M0PlayerLocomotion` with valid `M0LocomotionSettings`.

## Build and Smoke Status

- Build status: PASS (`dotnet build afterimage-tokyo.sln`, warnings only).
- Post-cleanup PlayMode smoke: executed manually.
- Final focused PlayMode capture (LockOn/Parry/Counter/Overlay): executed manually on 2026-05-21.

## Final Focused Capture (2026-05-21)

Evidence source:
- Final manual PlayMode capture notes for this change (this section).
- Supplemental verified artifact: `production/qa/evidence/story-1-6-defensive-wiring-evidence.md` (Parry/Counter success path).

Observed evidence excerpt:

```txt
[M0Input] LockOn pressed
[M0Input] Parry pressed
[M0Input] Counter pressed
Overlay visible in Game View
Overlay LockOn Target: None -> Enemy_M0TargetablePlaceholder (after LockOn press)
Overlay LastInput updates after LockOn / Parry / Counter
Overlay CounterWindow: Closed -> Open during valid counter opportunity
```

LockOn behavior note:
- This pass validates LockOn acquire/focus behavior.
- Pressing Tab a second time kept LockOn active in this run.

## 1) Combat Input / Log Proof

- LightAttack pressed: PASS
- HeavyAttack pressed: PASS
- LockOn pressed: PASS (final focused manual capture evidence)
- Parry pressed: PASS (proven in Story 1-6 evidence)
- Dodge pressed: PASS
- Counter pressed: PASS (proven in Story 1-6 evidence)

Console excerpts:

```txt
[M0Input] LightAttack pressed
[M0Input] HeavyAttack pressed
[M0Input] Dodge pressed
[M0Combat] State changed: Neutral -> AttackStartup
[M0Combat] State changed: AttackStartup -> AttackActive
[M0Combat] State changed: AttackActive -> AttackRecovery
[M0Combat] State changed: AttackRecovery -> Neutral
[M0Combat] State changed: Neutral -> DodgeStartup
[M0Combat] State changed: DodgeStartup -> DodgeActive
[M0Combat] State changed: DodgeActive -> DodgeRecovery
[M0Combat] State changed: DodgeRecovery -> Neutral
[M0Input] Parry pressed
[M0Combat] State changed: Neutral -> ParryStartup
[M0Combat] State changed: ParryStartup -> ParryActive
[M0Combat] Parry success: CounterWindow opening
[M0Combat] CounterWindow opened duration=3
[M0Input] Counter pressed
[M0Combat] CounterWindow Counter consumed
[M0Combat] State changed: Neutral -> CounterActive
```

Provenance note:
- The Parry/Counter lines above are from `production/qa/evidence/story-1-6-defensive-wiring-evidence.md` (2026-05-20), reused here as supplemental hard evidence because no newer LockOn/Parry/Counter capture artifact exists in this pass.

## 2) Combat Visual Feedback

- LightAttack visual feedback: PARTIAL
- HeavyAttack visual feedback: PARTIAL
- Parry visual feedback: PARTIAL
- Dodge visual feedback: PARTIAL
- Counter visual feedback: PARTIAL

Observation notes:

- State transitions for attack/dodge are clearly logged and gameplay responds.
- Animation presentation is out of scope for this change; missing animation adapter warning remains non-blocking.
- Parry/counter state success is strongly proven by logs, but dedicated Game View visual captures (separate from logs) are still missing.

## 3) Enemy Intent Visual Cycle

- Telegraph visual/overlay proof: PASS (state/log proof)
- Active visual/overlay proof: PASS (state/log proof)
- Recovery visual/overlay proof: PASS (state/log proof)

Evidence:

```txt
[M0EnemyLoop] Transition Idle -> Telegraph
[M0Enemy] State changed: Idle -> Telegraph duration=0.75
[M0EnemyLoop] Transition Telegraph -> Commit
[M0Enemy] State changed: Telegraph -> Commit duration=0.2 tags=DodgePunishable,ParryEligible,CounterOnWhiff
[M0EnemyLoop] Transition Commit -> Active
[M0Enemy] State changed: Commit -> Active duration=0.15 tags=DodgePunishable,ParryEligible,CounterOnWhiff ParryEligible=True
[M0EnemyLoop] Transition Active -> Recovery
[M0Enemy] State changed: Active -> Recovery duration=0.6
[M0EnemyLoop] Transition Recovery -> Idle
[M0Enemy] State changed: Recovery -> Idle
```

## 4) Debug Overlay Field Proof

- Overlay visible: PASS (final focused manual capture confirms visible in Game View)
- Combat State updates: PASS (snapshot update logs present)
- Enemy Intent updates: PASS (snapshot update logs present + enemy loop logs)
- CounterWindow updates: PASS (final focused manual capture shows Open state)
- LastInput updates: PASS (final focused manual capture confirms updates)
- LockOn Target updates: PASS (final focused manual capture confirms target field update)

Observation:

- This pass uses focused manual PlayMode capture notes plus log evidence to confirm overlay blocker fields.
- Supplemental overlay snapshot evidence from Story 1-6:
  - `[M0DebugOverlay] Snapshot update received combatState=ParryStartup enemyState=Active`
  - `[M0DebugOverlay] Snapshot update received combatState=ParryActive enemyState=Active`
- Final focused capture closes previous overlay blockers:
  - LockOn Target field update observed.
  - LastInput field update observed.
  - CounterWindow Open observed during valid opportunity.

## 5) Locomotion / Movement Proof (Post-cleanup)

- `[M0Input] Move started: value=(...)` observed.
- `[M0Locomotion] Move applied: before=(...), after=(...)` observed.
- `[M0Input] Move stopped` observed.
- `[M0Locomotion] Move stopped` observed.
- WASD visible movement: PASS.
- Player transform changes: PASS.
- PlayerMesh follows Player: PASS.

Console excerpts:

```txt
[M0Input] Move started: value=(-1.00,0.00)
[M0Locomotion] Model move started: pos=(-0.17,0.00,0.00) vel=(-5.00,0.00,0.00)
[M0Locomotion] Move applied: before=(0.00,0.00,0.00) after=(-0.17,0.00,0.00)
[M0Input] Move stopped
[M0Locomotion] Move stopped
```

## 6) Console Status

- Gameplay errors: `0` (for verified movement smoke runs in this evidence slice)
- Warnings:
  - `[M0Animation] Animation presentation adapter missing; combat continues without animation presentation`
  - `[M0Bootstrap] Animation presentation not assigned; animation playback disabled for this M0 smoke run.`

These warnings are non-blocking for this verification change because animation presentation / Animancer / root-motion authority are out of scope.

## PASS items

1. Build status PASS.
2. DI root cause fixed (default struct resolution removed via explicit factory/registration).
3. WASD movement visible after cleanup.
4. Player transform changes and PlayerMesh follows Player.
5. Movement diagnostics kept at useful transition level (start/applied/stop).
6. Enemy intent cycle state transitions verified via logs (Telegraph/Commit/Active/Recovery/Idle).
7. Console gameplay errors reported as 0 for this smoke evidence slice.
8. Parry input + success + CounterWindow open + Counter consume path proven by prior verified evidence artifact (Story 1-6).
9. LockOn input path confirmed in focused final manual capture.
10. Debug overlay blocker fields confirmed in focused final manual capture:
   - Overlay visible
   - CounterWindow
   - LastInput
   - LockOn Target

## PARTIAL items

1. Combat visual feedback proof for Light/Heavy/Dodge remains log-backed and partial on direct visual capture.
2. Parry visual feedback remains PARTIAL (state/log proven, dedicated visual capture not attached).
3. Counter visual feedback remains PARTIAL (state/log proven, dedicated visual capture not attached).
4. LockOn toggle-release behavior remains follow-up (not required for current blocker closure).

## FAIL items

- None.

## Remaining blockers

- None for current story-done blockers.

## OBSERVED / FOLLOW-UP

### LockOn Toggle / Release Behavior

Status: OBSERVED / FOLLOW-UP

Observation:
- Pressing Tab once acquires or maintains LockOn target successfully.
- Pressing Tab a second time kept LockOn active in this capture.

Decision:
- Current M0 evidence validates LockOn acquire/focus behavior only.
- Toggle-release behavior is not validated in this evidence pass.

Follow-up:
- Decide later whether M0 LockOn should be toggle acquire/release or acquire-only/hold-focus behavior.

## Ready for story-done

YES — all previously listed blocker items now have direct evidence references in this file and/or verified referenced evidence artifact.
