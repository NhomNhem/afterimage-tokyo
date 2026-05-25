# M0 Dodge Displacement Wiring — Verification (2026-05-25)

## Change

- `openspec/changes/archive/2026-05-25-wire-m0-dodge-displacement-combat-locomotion`

## Scope of this pass

- Verification-only pass on the correct Unity instance/worktree.
- No new gameplay implementation added in this pass.

## Unity instance / project path verification

- Unity instance: `afterimage-tokyo@aae9d45abe534984`
- Unity version: `6000.3.11f1`
- Project root reported by MCP: `J:/afterimage-tokyo/afterimage-tokyo`
- Active scene: `Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`

## Git scope verification

Changed files in Unity submodule were limited to intended implementation files:

- `Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
- `Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs`
- `Assets/_Project/Code/Locomotion/M0LocomotionSettings.cs`
- `Assets/_Project/Code/Locomotion/M0PlayerLocomotion.cs`
- `Assets/_Project/Tests/EditMode/M0PlayerLocomotionTests.cs`

## Compile / domain reload

- `refresh_unity` with script compile request completed.
- `editor/state` reported `is_compiling=false`, `ready_for_tools=true`.
- No compiler error entries were returned in console error query during this pass.

Result: PASS

## EditMode verification

### 1) `GlassRefrain.Tests.EditMode.M0PlayerLocomotionTests`

- Result: PASS
- Summary: `10 passed / 0 failed`
- Includes:
  - `DodgeDisplacementMovesPlayerWhenTriggered`
  - `DodgeDisplacementRejectsDuplicateTriggerDuringSameCycle`
  - `InvalidDodgeSettingsFailFast`

### 2) `GlassRefrain.Tests.EditMode.M0CombatCoreTests`

- Result: PASS
- Summary: `13 passed / 0 failed`
- Includes dodge state progression coverage:
  - `DodgeCycleTransitionsThroughExpectedStates`
  - `DodgeAndParryTickProgressionReturnToNeutral`

## PlayMode verification

### PlayMode test assembly run

- Assembly: `GlassRefrain.Tests.PlayMode`
- Result: PASS
- Summary: `2 passed / 0 failed`
- Covered tests:
  - `SceneFoundationTests.RequiredSceneAssetsExist`
  - `SceneFoundationTests.ScopeShellTypesExist`

### Manual PlayMode gameplay evidence (2026-05-25)

#### Dodge displacement / lunge

Result: PASS

Observed excerpt:

```text
[M0Combat] State changed: Neutral -> DodgeStartup
[M0Combat] State changed: DodgeStartup -> DodgeActive
[M0Locomotion] Dodge displacement started: before=(-1.28,0.00,0.00)
[M0Locomotion] Move applied: before=(-1.28,0.00,0.00) after=(-1.36,0.00,0.02)
[M0Combat] State changed: DodgeActive -> DodgeRecovery
[M0Combat] State changed: DodgeRecovery -> Neutral
```

Conclusion:
- Dodge request is accepted from Neutral.
- Combat chain reaches `DodgeActive`.
- Bridge triggers locomotion displacement.
- Player transform changes during dodge (`delta > 0`).

#### Repeated/invalid Dodge gating

Result: PASS

Observed excerpt:

```text
[M0Combat] Dodge rejected: not in Neutral (current=AttackActive)
```

Conclusion:
- Dodge remains CombatCore-gated.
- Invalid timing does not start a new displacement cycle.

#### WASD locomotion smoke

Result: PASS

Observed excerpt:

```text
[M0Input] Move started
[M0Locomotion] Move applied
[M0Input] Move stopped
[M0Locomotion] Move stopped
```

#### LightAttack smoke

Result: PASS

Observed excerpt:

```text
[M0Input] LightAttack pressed
[M0Combat] State changed: Neutral -> AttackStartup
[M0Combat] State changed: AttackStartup -> AttackActive
[M0Combat] State changed: AttackActive -> AttackRecovery
[M0Combat] State changed: AttackRecovery -> Neutral
```

#### Enemy intent smoke

Result: PASS

Observed:
- Enemy loop reached Telegraph, Commit, Active, Recovery, Idle.

#### LockOn smoke

Result: PARTIAL

Note:
- LockOn not explicitly captured in this specific dodge-displacement log slice.
- Keep PARTIAL here unless a direct LockOn smoke excerpt/reference is attached in this run.

## Console status

- No gameplay compile/runtime errors were observed in this verification run.
- Console warnings observed were Unity Test Framework runner warnings (`IPrebuildSetup` / `IPostBuildCleanup`), not gameplay logic errors.

## Task mapping (OpenSpec section 5.x)

- `5.1` CLOSED (manual PlayMode dodge displacement observed)
- `5.2` CLOSED (manual before/after transform delta observed)
- `5.3` CLOSED (manual + EditMode state chain evidence)
- `5.4` CLOSED (no new hard gameplay errors observed in smoke)
- `5.5` PARTIAL (LockOn smoke still needs direct capture/reference in this run)

## Current verdict

- Implementation sanity via compile + EditMode tests: PASS
- Manual PlayMode dodge displacement evidence: PASS
- Gameplay smoke closure: PARTIAL (LockOn smoke evidence still pending for this change artifact)
- Ready for code review: YES (with notes)
- Ready for story/evidence closure: NO (pending `5.5` LockOn smoke proof/reference)

## LockOn Smoke Reference

Result: PASS BY REFERENCE

This Dodge displacement change did not modify LockOn, TargetContext, input bindings, camera, or target overlay behavior.

LockOn smoke is accepted by reference to the prior completed LockOn evidence set:

- `production/qa/evidence/lockon-toggle-release-2026-05-24.md`
- `production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md`
- Archived OpenSpec change:
  `openspec/changes/archive/2026-05-25-decide-m0-lockon-second-press-toggle-release`

Prior accepted LockOn evidence proves:

- LockOn pressed
- `None -> Enemy -> None -> Enemy`
- `[M0Target] LockOn acquired`
- `[M0Target] LockOn released`
- overlay target transition proof

Current Dodge displacement change only touched locomotion/combat bridge scope and did not alter LockOn behavior.
