# LockOn Toggle Release Evidence — 2026-05-24

## Change

`openspec/changes/archive/2026-05-25-decide-m0-lockon-second-press-toggle-release`

## Scope

Manual PlayMode evidence update only.

No gameplay code, scene, prefab, material, camera, combat, memory, or input-binding changes.

## Goal

Prove LockOn second press releases the current target and third press reacquires it.

Expected transition:

`None -> Enemy -> None -> Enemy`

## Environment

- Project: Glass Refrain / afterimage-tokyo
- Sprint: Sprint 1
- Scene: M0 playable combat prototype scene
- Date: 2026-05-24
- Evidence type: Manual PlayMode observation

## Test Steps

1. Entered PlayMode.
2. Enabled/observed Debug Overlay.
3. Confirmed initial LockOn target state.
4. Pressed `Tab` once.
5. Observed target acquire.
6. Pressed `Tab` second time.
7. Observed target release.
8. Pressed `Tab` third time.
9. Observed target reacquire.
10. Checked for new gameplay console errors during the run.

## Overlay Observations

| Step | Input | Expected | Observed | Result |
| --- | --- | --- | --- | --- |
| 0 | None | `LockOn Target: None` | `LockOn Target: None` | PASS |
| 1 | Tab | `LockOn Target: Enemy` | `LockOn Target: Enemy` | PASS |
| 2 | Tab | `LockOn Target: None` | `LockOn Target: None` | PASS |
| 3 | Tab | `LockOn Target: Enemy` | `LockOn Target: Enemy` | PASS |

## Behavior Result

Observed transition:

`None -> Enemy -> None -> Enemy`

Result: PASS

## Console / Smoke Result

| Check | Result | Notes |
| --- | --- | --- |
| No new gameplay console errors during this LockOn run | PASS | Manual observation |
| LockOn acquire worked | PASS | First Tab acquired target |
| LockOn release worked | PASS | Second Tab released target |
| LockOn reacquire worked | PASS | Third Tab acquired target again |

## Required Acceptance Coverage

| Requirement | Result | Evidence |
| --- | --- | --- |
| Second press releases active LockOn target | PASS | Overlay showed `Enemy -> None` |
| Third press reacquires valid target | PASS | Overlay showed `None -> Enemy` |
| Full transition sequence proven | PASS | `None -> Enemy -> None -> Enemy` |
| No new gameplay console errors | PASS | Manual smoke observation |

## Verdict

PASS

## Artifact References — 6.1 / 6.2

### 6.1 Acquire -> Release -> Acquire log excerpt

Artifact file:
`production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md`

Referenced excerpt:

```txt
[M0Input] LockOn pressed
[M0Target] LockOn acquired
[M0Input] LockOn pressed
[M0Target] LockOn released
[M0Input] LockOn pressed
[M0Target] LockOn acquired
```

### 6.2 Overlay transition artifact

Artifact file:
`production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md`

Referenced excerpt:

```txt
Overlay LockOn Target: None
Tab press #1 -> Overlay LockOn Target: Enemy
Tab press #2 -> Overlay LockOn Target: None
Tab press #3 -> Overlay LockOn Target: Enemy
```

## Notes

- Evidence is based on manual PlayMode observation from 2026-05-24.
- No gameplay code was changed during this evidence update.
- No scene, prefab, material, camera, combat, memory, or input-binding changes were made.
- Debug Overlay was used as read-only proof.
- `Lock-On / Target Context` remains target truth owner.
- Explicit log/overlay artifacts for tasks 6.1/6.2 are recorded in:
  `production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md`.

## Dodge Displacement Triage Note

Result: PARTIAL / External Follow-up

During regression smoke, Dodge input and Combat Core state chain passed:

- `DodgePressedThisFrame` was received.
- Combat state transitioned:
  `Neutral -> DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral`.

However, player dodge displacement / lunge movement was not observed.

Read-only triage found this is not caused by LockOn toggle-release. The current M0 locomotion path only applies movement from Move input and does not yet implement a dedicated dodge impulse/displacement profile. `M0GameplayTickHandler` forwards Dodge input to Combat Core, but does not bridge Combat Core Dodge state into a locomotion displacement request.

Conclusion:
- LockOn behavior evidence remains PASS.
- 5.6 remains PARTIAL as a broader M0 locomotion/combat integration follow-up.
- Follow-up required: Dodge displacement wiring from Combat Core state to Player Locomotion.
