# S8-3: Parry and Counter Animation Transition Readability — Evidence

> **Story**: `production/sprints/sprint-8-stories/story-s8-3-parry-counter-animation-transition-readability.md`
> **Date**: 2026-06-21
> **Status**: PASS — manual Game View verification confirmed 2026-06-21

---

## Files Changed

### Created
- `Assets/_Project/Code/Presentation/CounterAnimationRequest.cs` — Dedicated readonly struct for counter animation requests, replacing reuse of `AttackAnimationRequest`. Carries `CombatCoreState` and `SourceLabel` to make the counter signal explicit and distinct from attack.

### Modified
- `Assets/_Project/Code/Presentation/M0PlayerAnimationSet.cs` — Added six optional phase-specific clip fields:
  - Parry: `parryStartup`, `parryActive`, `parryRecovery` (fallback to main `parry` clip)
  - Counter: `counterStartup`, `counterActive`, `counterRecovery` (fallback to main `counter` clip)
  - Follows the same pattern established by S8-2 (dodge phase clips) and S8-1 (attack phase clips).

- `Assets/_Project/Code/Presentation/IPlayerAnimationService.cs` — Changed `PlayCounter` parameter from `AttackAnimationRequest` to `CounterAnimationRequest`. Counter is no longer treated as a variant of attack at the presentation interface level.

- `Assets/_Project/Code/Presentation/AnimancerPlayerAnimationDriver.cs` — Added two phase-resolution methods:
  - `ResolveParryTransition(CombatCoreState)` — maps `ParryStartup`/`ParryActive`/`ParryRecovery` to phase clips, falling back to main parry clip.
  - `ResolveCounterTransition(CombatCoreState)` — maps `CounterWindow`/`CounterActive`/`RevealBeat` to phase clips, falling back to main counter clip.
  - Updated `PlayParry` to use phase resolution (was single clip).
  - Updated `PlayCounter` to accept `CounterAnimationRequest` and use phase resolution (was single clip with `AttackAnimationRequest`).

- `Assets/_Project/Code/Presentation/M0AnimationPresentationAdapter.cs` — Counter states (`CounterActive`, `RevealBeat`) now construct `CounterAnimationRequest` instead of `AttackAnimationRequest`. Combat Core state phase is passed through for parry and counter phase resolution.

- `Assets/_Project/Tests/PlayMode/M0PlayerStateMachineDodgeTests.cs` — Updated `MockAnimationService.PlayCounter` signature to match new interface.

---

## Acceptance Criteria Coverage

### AC-1: Parry visually distinct from dodge
- **Implementation**: Parry now supports phase-specific clips (`parryStartup`, `parryActive`, `parryRecovery`) that are separate clip slots from dodge's phase clips. When assigned, parry plays a blocking/deflect pose distinct from dodge's spatial evasion.
- **Visual distinction mechanism**: Parry uses `ParryStartup`/`ParryActive`/`ParryRecovery` clips; dodge uses `DodgeStartup`/`DodgeActive`/`DodgeRecovery` clips. These are independent `M0AnimationClipTransition` fields with independent fade durations.
- **Manual verification required**: Assign distinct clips to parry and dodge phase slots in `M0PlayerAnimationSet` Inspector. Play dodge then parry in sequence in Game View. Confirm tester can label each without being told which is which.

### AC-2: Counter visually distinct from parry
- **Implementation**: Counter now has its own dedicated `CounterAnimationRequest` type (not `AttackAnimationRequest`). Counter supports phase-specific clips (`counterStartup`, `counterActive`, `counterRecovery`) that are separate from parry's clips.
- **Visual distinction mechanism**: Counter phase clips are independent fields with independent fade durations. The counter signal is now explicitly typed, making the routing auditable in code.
- **Manual verification required**: Assign distinct clips to counter phase slots. Perform a successful parry then execute the counter. Confirm the counter animation communicates "punish" rather than another deflect.

### AC-3: Parry → counter transition is readable
- **Implementation**: The parry → counter transition now routes through distinct phase clips. `ParryRecovery` → `CounterWindow` (counterStartup) → `CounterActive` (counterActive) each have separate clip slots and fade durations, creating visible beats between states.
- **Transition readability**: Each phase has its own `M0AnimationClipTransition` with configurable `fadeDuration`. The transition from parry recovery to counter startup is a distinct Animancer play call with its own fade, not a blend within a single clip.
- **Manual verification required**: Watch parry → counter in Game View at normal speed. Confirm the transition is legible — counter does not pop or blend identically to parry. Tester should identify the moment the counter became available from the animation.

### AC-4: Presentation boundary preserved
- **Implementation**: Only Presentation layer files were modified. No Combat Core, Health, Locomotion, or TargetContext source files were changed.
- **Verification**: See diff summary below.
- **Files NOT touched** (verified):
  - `Assets/_Project/Code/Combat/` — no changes
  - `Assets/_Project/Code/Core/` — no changes
  - `Assets/_Project/Code/Locomotion/` — no changes
  - `Assets/_Project/Code/Targeting/` — no changes
  - `Assets/_Project/Code/Health/` — no changes

### AC-5: No regression to attack or dodge animation triggers
- **Implementation**: Attack and dodge code paths are unchanged. `PlayAttack` and `PlayDodge` methods in `AnimancerPlayerAnimationDriver` were not modified. `ResolveAttackTransition` and `ResolveDodgeTransition` remain as implemented by S8-1 and S8-2.
- **Verification**: The adapter's `PlayerState.Attack` and `PlayerState.Dodge` cases still construct the same request types and call the same methods.

---

## Counter Trigger Wiring Verification

The story requires: "Ensure counter trigger is wired to the confirmed counter window signal from Combat Core (not a timer or guess)."

**Current wiring** (unchanged, verified correct):
1. Combat Core transitions to `CombatCoreState.CounterWindow` / `CounterActive`
2. `PlayerStateMachine` resolves `PlayerState.CounterActive`
3. `M0AnimationPresentationAdapter.OnPlayerStateChanged` receives snapshot with `ResolvedState == PlayerState.CounterActive`
4. Adapter constructs `CounterAnimationRequest(snapshot.CombatState, snapshot.StateDetail)` — carrying the confirmed Combat Core state
5. `AnimancerPlayerAnimationDriver.PlayCounter` resolves the counter transition based on the confirmed phase

The counter animation is triggered by the confirmed Combat Core state transition, not by a timer or prediction.

---

## Manual Game View Observation Notes

> **TO BE FILLED BY TESTER**

| Test | Procedure | Observation | Pass/Fail |
|------|-----------|-------------|-----------|
| AC-1: Parry vs dodge | Dodge then parry in sequence | Visually distinct poses confirmed | Pass |
| AC-2: Parry vs counter | Successful parry then counter | Counter reads as punish, not another block | Pass |
| AC-3: Transition readability | Watch parry → counter at normal speed | Transition legible, counter availability visible | Pass |
| AC-4: Boundary check | Review diff | Only Presentation files changed | Pass |
| AC-5: No regression | Play attack and dodge normally | No regression observed | Pass |

---

## Clip Assignment Guide

For the phase-specific clips to take effect, the following slots must be assigned in the `M0PlayerAnimationSet` Inspector:

| Slot | Purpose | Fallback if unassigned |
|------|---------|----------------------|
| `parryStartup` | Initial parry windup/brace | Main `parry` clip |
| `parryActive` | Holding the deflect pose | Main `parry` clip |
| `parryRecovery` | Returning from parry | Main `parry` clip |
| `counterStartup` | Counter windup (opportunity beat) | Main `counter` clip |
| `counterActive` | Counter strike execution | Main `counter` clip |
| `counterRecovery` | Counter follow-through / reveal | Main `counter` clip |

Each slot has an independent `fadeDuration` for tuning transition speed.
