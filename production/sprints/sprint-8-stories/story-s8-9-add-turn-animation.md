# Story S8-9: [Presentation] Fix Animation Clip Mappings — Peace/Combat Mode Split

> **Sprint**: Sprint 8
> **Status**: In Progress
> **Layer**: Presentation
> **Type**: Visual/Feel
> **Estimate**: 1.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-18

## Context

**Sprint Plan**: `production/sprints/sprint-8.md`
**Epic**: M0 First Playable Duel — player animation polish pass

Manual testing revealed multiple animation clip mapping errors, missing slots, and a missing peace/combat distinction:

1. **Parry** maps to Sp_Skill1 (96f special attack) — WRONG, should be Quickshift_B (backstep parry)
2. **Counter** maps to Sp_Skill2 (233f special attack) — WAY too long, should be FS Melee counter_
3. **HitReaction** piggybacks on PlayAttack — WRONG, plays Attack1 instead of hit reaction
4. **Dash (Shift key)** uses Evade (step-back) — WRONG for forward dash, needs Quickshift_F
5. **No peace/combat mode split** — character is always in combat stance (Sp_Idle/Sp_Run) even when not fighting
6. **Sp_TurnL/R are combat turn-slash attacks**, NOT locomotion pivots — removed
7. **No directional walk clips** — causes "forward then backward" visual when turning
8. **M0DirectPlayerInput uses FindAction** — should use auto-generated M0InputActions wrapper class

**ADR-0003**: Animator is presentation-only — this story must not touch domain/application facing logic.

**Engine**: Unity 6000.3.x + URP | Animancer
**Risk**: MEDIUM — reassigns multiple animation clips, adds dual clip sets, and refactors input wiring.

## Corrected Animation Mapping

### Peace Locomotion (Normal clips — when NOT in combat)

| Slot | Clip | Source |
|---|---|---|
| idle | Idle | Katana Normal |
| locomotion | Run | Katana Normal |
| walk | Walk | Katana Normal |

### Combat Locomotion (Special clips — when HasTargetFocus OR CombatState != Neutral)

| Slot | Clip | Source |
|---|---|---|
| combatIdle | Sp_Idle | Katana Special |
| combatLocomotion | Sp_Run | Katana Special |
| combatWalk | Sp_Walk | Katana Special |

### Combat Actions

| Slot | Clip | Source | Change |
|---|---|---|---|
| lightAttack | Attack1 | Katana Normal | unchanged |
| heavyAttack | Attack2 | Katana Normal | unchanged |
| dodge | Evade | Katana Normal | unchanged |
| dash | Quickshift_F | Katana Special | NEW |
| dashBack | Quickshift_B | Katana Special | NEW |
| dashLeft | Quickshift_L | Katana Special | NEW |
| dashRight | Quickshift_R | Katana Special | NEW |
| parry | Quickshift_B | Katana Special | FIX (was Sp_Skill1) |
| counter | counter_ | FS Melee Sword | FIX (was Sp_Skill2) |
| hitReaction | Hit1 | Katana Normal | NEW (was piggybacked on Attack1) |
| hitReaction2 | (unassigned) | FS Melee Sword | NEW (reserved for future variant) |
| stun | Stun | Katana Normal | NEW |

### Directional Walks (FS Melee — for future blend tree)

| Slot | Clip | Source |
|---|---|---|
| walkBack | sword_walk_back | FS Melee Sword |
| walkLeft | sword_walk_left | FS Melee Sword |
| walkRight | sword_walk_right | FS Melee Sword |

### Removed

| Slot | Reason |
|---|---|
| ~~turnLeft~~ | Sp_TurnL is a combat attack clip, not a locomotion pivot |
| ~~turnRight~~ | Sp_TurnR is a combat attack clip, not a locomotion pivot |

## Acceptance Criteria

- [x] `M0PlayerAnimationSet` has 21 slots: 3 peace locomotion + 3 combat locomotion + 11 combat actions (including 4 directional dashes + hitReaction2) + 3 directional walks + 1 dodge.
- [x] `turnLeft` and `turnRight` slots REMOVED from M0PlayerAnimationSet.
- [x] `IPlayerAnimationService` has `SetCombatMode(bool)`, `PlayDash(DashDirection)`, `PlayHitReaction`, `PlayStun` — `PlayTurn` removed. `PlayLocomotion` accepts `Vector2 relativeMovementDirection`.
- [x] `AnimancerPlayerAnimationDriver.SetCombatMode` switches between peace (Normal) and combat (Special) clip sets for idle/locomotion/walk.
- [x] `AnimancerPlayerAnimationDriver` uses Animancer `MixerState<Vector2>` for combat locomotion blending (forward/back/left/right).
- [x] `M0AnimationPresentationAdapter` detects combat mode from `snapshot.HasTargetFocus || CombatState != Neutral` and calls `SetCombatMode` before routing.
- [x] `M0AnimationPresentationAdapter` computes relative movement direction (strafe, forward) from `PlayerStateSnapshot.MovementDirection` and `FacingDirection`.
- [x] `PlayerStateSnapshot` carries `Axis2 MovementDirection` and `Axis2 FacingDirection` for animation use.
- [x] `LocomotionStateMachine` exposes `CurrentMoveIntent` and `CurrentFacingDirection` for the resolver.
- [x] `DashDirection` enum (Forward/Back/Left/Right) routes to correct Quickshift clip per direction.
- [x] Parry clip: Quickshift_B (not Sp_Skill1). Counter clip: counter_ (not Sp_Skill2). HitReaction: Hit1 (not Attack1).
- [x] Peace idle: Normal Idle. Peace locomotion: Normal Run. Combat idle: Sp_Idle. Combat locomotion: Sp_Run.
- [x] `M0DirectPlayerInput` uses M0InputActions generated wrapper — no FindAction calls.
- [x] All existing tests updated to match new interface.
- [x] No gameplay truth files (Combat Core, Health, Locomotion, TargetContext) modified.
- [ ] M0PlayerAnimationSet.asset updated with new dash/dashBack/dashLeft/dashRight/hitReaction2 clip references in Unity Editor.
- [ ] No new S1/S2 console errors (requires Unity Editor verification).

## Implementation Notes

**Combat mode detection**:
- `M0AnimationPresentationAdapter.OnPlayerStateChanged` checks `snapshot.HasTargetFocus || snapshot.CombatState != CombatCoreState.Neutral`
- Calls `_playerAnimationService.SetCombatMode(isCombatMode)` before routing any animation

**Movement direction pipeline**:
- `LocomotionStateMachine` exposes `CurrentMoveIntent` (Axis2 from input) and `CurrentFacingDirection` (Axis2 from locomotion facing)
- `PlayerStateResolver` reads both and passes them into `PlayerStateSnapshot` as `MovementDirection` and `FacingDirection`
- `M0AnimationPresentationAdapter.ComputeRelativeDirection()` projects world-space movement onto character facing: `forward = dot(move, facing)`, `right = cross(move, facing)` → returns `Vector2(right, forward)`
- Relative direction is passed to `PlayLocomotion` for MixerState blending

**MixerState directional blending (combat mode)**:
- `AnimancerPlayerAnimationDriver` creates `MixerState<Vector2>` with 4 child states:
  - CombatLocomotion (Sp_Run) at `(0, 1)` — forward
  - WalkBack (sword_walk_back) at `(0, -1)` — backward
  - WalkLeft (sword_walk_left) at `(-1, 0)` — left strafe
  - WalkRight (sword_walk_right) at `(1, 0)` — right strafe
- Mixer parameter is updated each frame with the relative direction Vector2
- Peace mode uses simple single-clip playback (no mixer)

**Dash direction routing**:
- `DashDirection` enum: Forward, Back, Left, Right
- `ResolveDashDirection()` picks dominant axis from relative direction: |forward| >= |strafe| → Forward/Back, else → Left/Right
- `PlayDash(DashDirection)` selects: Dash (Quickshift_F), DashBack (Quickshift_B), DashLeft (Quickshift_L), DashRight (Quickshift_R)

**Input refactor**:
- `M0DirectPlayerInput` replaced `[SerializeField] InputActionAsset` + `FindAction` with `M0InputActions` generated wrapper
- Typed access: `_inputActions.Gameplay.Move`, `.Dodge`, etc.
- Disposes `_inputActions` in OnDestroy

## Out of Scope

- PlayerState.Dash or PlayerState.Stun (requires domain/application changes — future story)
- Root motion from any clips (must remain disabled)
- Upper-body mask / layered animation
- Camera or jump fixes (separate concerns)
- Smooth turn animation (>90° turns currently snap via root rotation — future story for Quickshift snap animation)

## QA Test Cases

- **AC-1**: Peace idle — Stand still with no target lock. Normal Idle plays (not Sp_Idle).
- **AC-2**: Peace locomotion — Move with no target lock. Normal Run plays (not Sp_Run).
- **AC-3**: Combat idle — Lock on target, stand still. Sp_Idle plays.
- **AC-4**: Combat locomotion — Lock on target, move forward. Sp_Run plays.
- **AC-5**: Combat strafe left — Lock on target, move left. sword_walk_left blends in via MixerState.
- **AC-6**: Combat strafe right — Lock on target, move right. sword_walk_right blends in via MixerState.
- **AC-7**: Combat walk backward — Lock on target, move backward. sword_walk_back blends in via MixerState.
- **AC-8**: Parry plays Quickshift_B — Trigger parry. Backstep parry animation (not Sp_Skill1).
- **AC-9**: Counter plays FS counter_ — Trigger counter. Short counter slash (not 233f Sp_Skill2).
- **AC-10**: HitReaction plays Hit1 — Take damage. Hit reaction clip (not Attack1).
- **AC-11**: Dash forward — Dodge while pressing forward. Quickshift_F plays.
- **AC-12**: Dash backward — Dodge while pressing backward. Quickshift_B plays.
- **AC-13**: Dash left — Dodge while pressing left. Quickshift_L plays.
- **AC-14**: Dash right — Dodge while pressing right. Quickshift_R plays.
- **AC-15**: Turn slots removed — No turnLeft/turnRight in M0PlayerAnimationSet.
- **AC-16**: No FindAction in M0DirectPlayerInput — Source uses M0InputActions.Gameplay.X pattern.
- **AC-17**: Console clean — No new S1/S2 errors.

## Dependencies

- Depends on: S8-7 (visible character + clips assigned), S8-8 (decomposed state machine)
- Blocks: nothing
