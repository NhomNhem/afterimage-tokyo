# S5-4 Wire M0 Dodge Displacement Verification

**Date**: 2026-06-11
**Updated**: 2026-06-12
**Story**: `production/sprints/sprint-5-stories/story-s5-4-wire-m0-dodge-displacement.md`
**Engine**: Unity 6000.3.x

## Implementation Summary

S5-4 adds `M0DodgeDisplacementBridge`, a narrow orchestration collaborator that observes Combat Core snapshot transitions and requests `IM0PlayerLocomotion.TryBeginDodgeDisplacement()` only after `DodgeStartup` has armed the bridge and a later transition reaches `DodgeActive`.

`M0GameplayTickHandler` now routes dodge displacement through this bridge outside the visual feedback adapter path, so gameplay displacement no longer depends on presentation adapter availability.

## Automated Test Coverage Added

Test file:

- `afterimage-tokyo/Assets/_Project/Tests/PlayMode/M0DodgeDisplacementIntegrationTests.cs`

Test cases:

1. `CombatCoreDodgeActive_WhenBridgeIsArmed_ShouldMoveLocomotion`
2. `NonDodgeCombatStates_WhenObservedByBridge_ShouldNotMoveLocomotion`
3. `DodgeActive_WhenStartupWasNotObserved_ShouldNotStartDisplacement`
4. `DuplicateDodgeActiveObservation_WhenAlreadyStarted_ShouldNotStartSecondDisplacement`
5. `DodgeDisplacement_WhenStartedThroughBridge_ShouldPreserveAuthorityBoundaries`

## Verification Status

| Check | Result | Notes |
|---|---|---|
| `git diff --check` | PASS | No whitespace errors reported. |
| Unity refresh / compile | PASS | Unity MCP refresh completed with no compile errors. |
| Unity PlayMode smoke | PASS | Entered Play Mode with no `M0RuntimeServiceCompositionRegistrar` config exception and no `M0GameplayTickHandler` `Update` / `OnDestroy` NRE. |
| Focused Unity PlayMode test execution | PASS | Unity MCP PlayMode job `5cc0123e9f2b477797a3051a3475e157`: 7/7 passing, including all 5 `M0DodgeDisplacementIntegrationTests`. |
| Manual dodge-lunge smoke | PASS | `Dodge pressed` drove `Neutral -> DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral`; `[M0Locomotion] Dodge displacement started` observed; player movement applied. |
| Console classification | PASS WITH WARNINGS | No new S5-scope blocker. Missing M0 animation set warnings are optional presentation-content warnings. |
| `dotnet build afterimage-tokyo.sln --no-restore` | INCONCLUSIVE | Timed out twice without compiler output; leftover build processes from this run were stopped. |
| Generated `.csproj` freshness | STALE | Unity-generated project files have not regenerated to include the new source/test files. |
| Accidental full EditMode run | FAILURES OUT OF SCOPE | First Unity MCP `run_tests` call used the wrong mode/filter and ran full EditMode. Failures were pre-existing/stale expectations outside S5-4 closure and were not counted as S5 blockers. |

## Manual PlayMode Checklist

- [x] Enter the M0 combat prototype scene.
- [x] Press Dodge from Neutral with movement input.
- [x] Confirm player transform visibly lunges in the intended direction.
- [x] Confirm Dodge does not become a perfect-dodge/i-frame reward.
- [x] Confirm attack, parry, counter, target context, health, memory interaction, reveal feedback, and runtime memory log still operate.
- [x] Confirm console has no new S5-scope blocker.

## Manual Evidence Extract

- `[M0Input] Dodge pressed`
- `[M0Combat] State changed: Neutral -> DodgeStartup`
- `[M0Combat] State changed: DodgeStartup -> DodgeActive`
- `[M0Locomotion] Dodge displacement started: before=(0.23,0.00,-0.68)`
- `[M0Combat] State changed: DodgeActive -> DodgeRecovery`
- `[M0Combat] State changed: DodgeRecovery -> Neutral`
- Additional run observed displacement start at `before=(-1.28,0.00,-1.44)` and `M0PlayerLocomotionAdapter` applying movement.

## Current Verdict

**PASS**

Implementation, focused PlayMode tests, manual dodge-lunge smoke, and console classification are complete. S5-4 is ready for `/story-done` closure.
