# S8-4: Hit Reaction Animation Blending — Evidence

> **Story**: `production/sprints/sprint-8-stories/story-s8-4-hit-reaction-animation-blending.md`
> **Date**: 2026-06-21
> **Status**: PASS — implementation complete; manual Game View verification pending

---

## Files Changed

### Created
- `Assets/_Project/Code/Presentation/HitReactionAnimationRequest.cs` — Dedicated readonly struct for hit reaction animation requests, replacing reuse of `AttackAnimationRequest`. Carries `CombatCoreState` and `SourceLabel` to make the hit reaction signal explicit and distinct from attack.

### Modified
- `Assets/_Project/Code/Presentation/IPlayerAnimationService.cs` — Changed `PlayHitReaction` parameter from `AttackAnimationRequest` to `HitReactionAnimationRequest`. Hit reaction is no longer treated as a variant of attack at the presentation interface level.

- `Assets/_Project/Code/Presentation/AnimancerPlayerAnimationDriver.cs` — Implemented context-sensitive hit reaction blending:
  - Added `ResolveHitReactionTransition()` — alternates between `hitReaction` and `hitReaction2` clips for visual variety.
  - Added `ResolveHitReactionFadeDuration()` — selects blend timing based on the interrupted state:
    - From idle/locomotion: 0.15s fade (smooth entry into reaction)
    - From attack/dodge/parry/counter: 0.1s fade (responsive interrupt)
    - From another hit reaction: 0.05s fade (quick chain without squishiness)
  - Updated `PlayHitReaction` to accept `HitReactionAnimationRequest` and use context-sensitive blend timing.
  - Added debug logging under `GR_M0_PROTOTYPE` define for hit reaction clip selection and fade duration.

- `Assets/_Project/Code/Presentation/M0AnimationPresentationAdapter.cs` — `PlayerState.HitReaction` case now constructs `HitReactionAnimationRequest` instead of `AttackAnimationRequest`. Combat Core state phase is passed through for hit reaction context.

- `Assets/_Project/Tests/PlayMode/M0PlayerStateMachineDodgeTests.cs` — Updated `MockAnimationService.PlayHitReaction` signature to match new interface.

---

## Acceptance Criteria Coverage

### AC-1: Hit reaction visually distinct from idle and attack
- **Implementation**: Hit reaction uses dedicated `hitReaction` and `hitReaction2` clip slots in `M0PlayerAnimationSet`, which are independent from idle, locomotion, and attack clip slots. The clip alternation toggle ensures visual variety between consecutive hits.
- **Visual distinction mechanism**: Hit reaction clips are separate `M0AnimationClipTransition` fields with independent fade durations. The hit reaction signal is now explicitly typed via `HitReactionAnimationRequest`, making the routing auditable in code.
- **Manual verification required**: Assign distinct clips to `hitReaction` and `hitReaction2` slots in `M0PlayerAnimationSet` Inspector. Take damage in Game View. Confirm tester identifies "player took a hit" from animation alone.

### AC-2: Blend quality from interrupted states
- **Implementation**: `ResolveHitReactionFadeDuration()` selects blend timing based on the currently playing clip name:
  - From idle/locomotion (no action clip name match): 0.15s — smooth transition from relaxed state
  - From attack/dodge/parry/counter (action clip name match): 0.1s — responsive interrupt that cuts action cleanly
  - From another hit reaction (chain hit): 0.05s — minimal fade to avoid squishy feel during rapid damage
- **Transition quality**: Animancer's cross-fade with context-appropriate duration prevents jarring snaps. The fade duration is tuned per interrupted state category rather than using a single global value.
- **Manual verification required**: Take damage mid-attack in Game View. Confirm hit reaction blends without a jarring snap or pop. Transition should feel responsive, not broken.

### AC-3: Hit reaction communicates damage taken
- **Implementation**: Hit reaction uses dedicated body response clips (`hitReaction`, `hitReaction2`) that are visually distinct from combat action clips. The clip alternation provides variety for repeated hits.
- **Body response legibility**: The hit reaction clip is played from time 0 with a context-appropriate fade, ensuring the reaction pose is visible. The clip is independent from attack/dodge/parry clips, so the body language clearly signals "hit taken" rather than "action in progress."
- **Manual verification required**: Take damage from idle, from mid-attack, and from mid-dodge. Confirm each hit reaction reads as "player took damage" regardless of the interrupted state.

### AC-4: Presentation boundary preserved
- **Implementation**: Only Presentation layer files were modified. No Health, Combat Core, Locomotion, or TargetContext source files were changed.
- **Verification**: See diff summary below.
- **Files NOT touched** (verified):
  - `Assets/_Project/Code/Combat/` — no changes
  - `Assets/_Project/Code/Core/` — no changes
  - `Assets/_Project/Code/Locomotion/` — no changes
  - `Assets/_Project/Code/Targeting/` — no changes
  - `Assets/_Project/Code/Health/` — no changes

### AC-5: No regression to attack, dodge, or parry animation triggers
- **Implementation**: Attack, dodge, and parry code paths are unchanged. `PlayAttack`, `PlayDodge`, and `PlayParry` methods in `AnimancerPlayerAnimationDriver` were not modified. `ResolveAttackTransition`, `ResolveDodgeTransition`, and `ResolveParryTransition` remain as implemented by S8-1, S8-2, and S8-3.
- **Verification**: The adapter's `PlayerState.Attack`, `PlayerState.Dodge`, and `PlayerState.Parry` cases still construct the same request types and call the same methods. Only the `PlayerState.HitReaction` case was updated to use `HitReactionAnimationRequest`.

---

## Hit Reaction Trigger Wiring Verification

The story requires: "Ensure hit reaction trigger is driven by confirmed damage result, not a visual guess."

**Current wiring** (unchanged, verified correct):
1. `M0HealthDamageReactionModel.ApplyDamage()` validates the combat outcome as `ConfirmedHit` or `ConfirmedCounterHit`
2. Health snapshot fires `SnapshotChanged` event
3. Combat Core transitions to `CombatCoreState.HitReact` based on confirmed damage
4. `PlayerStateMachine` (via `CombatStateMachine`) resolves `PlayerState.HitReaction`
5. `M0AnimationPresentationAdapter.OnPlayerStateChanged` receives snapshot with `ResolvedState == PlayerState.HitReaction`
6. Adapter constructs `HitReactionAnimationRequest(snapshot.CombatState, snapshot.StateDetail)` — carrying the confirmed Combat Core state
7. `AnimancerPlayerAnimationDriver.PlayHitReaction` resolves the hit reaction transition and blend timing

The hit reaction animation is triggered by the confirmed Health damage result, propagated through Combat Core state, not by a timer or prediction.

---

## Manual Game View Observation Notes

> **TO BE FILLED BY TESTER**

| Test | Procedure | Observation | Pass/Fail |
|------|-----------|-------------|-----------|
| AC-1: Visual distinction | Take damage from idle state | Hit reaction pose is distinct from idle and attack | TBD |
| AC-2: Blend from attack | Take damage mid-attack | No pop or snap; transition feels responsive | TBD |
| AC-2: Blend from idle | Take damage while idle | Smooth blend into reaction, no jarring start | TBD |
| AC-2: Blend from dodge | Take damage during dodge recovery | Clean interrupt of dodge animation | TBD |
| AC-3: Damage communication | Take damage in Game View | Body response clearly reads as "hit taken" | TBD |
| AC-3: Repeated hits | Take damage multiple times in sequence | Alternating clips provide variety | TBD |
| AC-4: Boundary check | Review diff | Only Presentation files changed | Pass |
| AC-5: No regression | Play attack, dodge, parry normally | No regression in animation triggers | TBD |

---

## Clip Assignment Guide

For the hit reaction to be visually effective, the following slots should be assigned in the `M0PlayerAnimationSet` Inspector:

| Slot | Purpose | Fallback if unassigned |
|------|---------|----------------------|
| `hitReaction` | Primary hit reaction body response | Warning logged; no clip plays |
| `hitReaction2` | Alternate hit reaction for variety | Falls back to `hitReaction` |

Each slot has an independent `fadeDuration` configurable in the Inspector. The runtime blend timing is determined by `ResolveHitReactionFadeDuration()` based on the interrupted state, overriding the per-clip `fadeDuration` for hit reactions specifically.

---

## Blend Timing Reference

| Interrupted State Category | Fade Duration | Rationale |
|---------------------------|---------------|-----------|
| Idle / Locomotion | 0.15s | Smooth entry from relaxed state; avoids abrupt start |
| Attack / Dodge / Parry / Counter | 0.1s | Responsive interrupt; cuts action cleanly without lingering |
| Another hit reaction (chain) | 0.05s | Minimal fade; prevents squishy feel during rapid damage |
