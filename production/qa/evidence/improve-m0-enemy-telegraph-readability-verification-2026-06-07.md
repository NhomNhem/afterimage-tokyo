# Improve M0 Enemy Telegraph Readability Verification

Date: 2026-06-07

Status: PASS WITH NOTES

## Scope

OpenSpec change: `improve-m0-enemy-telegraph-readability`

Implemented scope:

- Added an `EnemyTelegraphReadabilitySnapshot` contract in Core.
- Enemy Intent now derives readability phase, progress, attack tags, defensive answer, punish availability, and reason from Enemy Intent truth.
- Debug Overlay now reads the enemy readability reason as an observer-only value.
- Added focused EditMode coverage for readability shape, tag continuity, punish availability, and Debug Overlay read-only guardrails.

Out of scope and unchanged:

- No new enemies, boss logic, behavior tree, GOAP, or multi-enemy systems.
- No CombatCore result authority changes.
- No camera, lock-on, VFX, or audio refactor.
- No direct Unity logging added.

## Automated Verification

### Unity Compile

Result: PASS

Evidence:

- Unity refresh/compile completed after code and test changes.
- Console hard errors after final compile: `0`.

### Focused EditMode Tests

Result: PASS

MCP test job:

```txt
c87930c49b3e42239e7afb31e84d0425
```

Focused fixtures:

```txt
GlassRefrain.Tests.EditMode.M0EnemyIntentTests
GlassRefrain.Tests.EditMode.M0DebugOverlaySnapshotIntegrationTests
GlassRefrain.Tests.EditMode.SceneComposition_test
GlassRefrain.Tests.EditMode.VContainerRegistry_test
```

Summary:

```txt
total: 42
passed: 42
failed: 0
skipped: 0
```

## Readability Checklist

| Check | Result | Notes |
| --- | --- | --- |
| Telegraph distinguishable from Commit/Active | PASS | `Readability.Phase`, `PhaseLabel`, `RemainingSeconds`, and `PhaseProgress01` are exposed from Enemy Intent. |
| Commit/Active attack tags preserved | PASS | Tests verify tags persist into Active and are copied defensively. |
| Recovery/punish availability visible | PASS | Tests verify `PunishAvailable`, `PunishSource`, and `DefensiveAnswer = Counter`. |
| Debug Overlay remains observer-only | PASS | Tests verify pass-through behavior and source guardrails. |
| Scene composition/registry health | PASS | Focused composition and VContainer registry tests passed. |
| Manual PlayMode visual sampling | PARTIAL | PlayMode smoke entered the M0 scene and logged driver initialization. Tool-side reflection sampling failed with an editor tooling error: `The filename or extension is too long`; no verified 3-loop visual sample was captured in this run. |

## Console Classification

Hard errors:

```txt
0
```

Known/non-blocking warnings observed during the session:

- Nhem analyzer warnings on existing M0 registration/health constructor patterns.
- UDR warnings from vendor/plugin/sample assets.
- Toon/HDRP material drawer/editor warnings seen previously.

None of the recorded warnings were introduced as hard compile or test failures by this change.

## Ownership Boundary Review

Result: PASS

- Enemy Intent owns phase truth, timing-derived readability, attack tags, and punish availability.
- Combat Core remains the authority for defensive action validity, combat result, counter window, hit resolution, and reveal request context.
- Debug Overlay consumes snapshots only and does not call Enemy Intent transition APIs.
- Presentation/camera/VFX/audio authority was not expanded.

## Manual Follow-Up Recommendation

Run a human PlayMode pass in `Gameplay_CombatPrototype` and observe at least three full enemy loops, capturing whether the Telegraph, Commit/Active, Recovery, and punish beats are readable under actual player control.
