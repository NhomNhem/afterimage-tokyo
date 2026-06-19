# Story S8-7: [Presentation] Wire School_Katana_Girl into M0 Duel Scene

> **Sprint**: Sprint 8
> **Status**: Complete
> **Layer**: Presentation
> **Type**: Visual/Feel
> **Estimate**: 1.5 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-17

## Context

**Sprint Plan**: `production/sprints/sprint-8.md`
**Epic**: M0 First Playable Duel — player animation polish pass
**Asset source**: `Assets/Resources/Models/CombatGirlsCharacterPack/School_Katana_Girl/`
**Project model copy**: `Assets/_Project/Content/Art/Model/Characters/School_Katana_FullBody-Magica cloth2.fbx`
**Project materials**: `Assets/_Project/Content/Materials/Characters/Player/` (already exist, URP-ready)
**Animation system**: **Animancer** (not a plain AnimatorController)
**GDD**: `design/gdd/player-locomotion.md`, `design/gdd/combat-core.md`
**ADR Governing Implementation**: ADR-0003 — Animator is presentation-only.

**Engine**: Unity 6000.3.x + URP | **Risk**: MEDIUM
**Engine Notes**: Project model copy uses the Magica cloth2 FBX. For M0 the
`AnimancerComponent.Animator.applyRootMotion` is already disabled by
`AnimancerPlayerAnimationDriver`. No Magica Cloth physics runtime needed for
animation-only clip playback.

## What already exists

| Asset | Location | Status |
|-------|----------|--------|
| `AnimancerPlayerAnimationDriver` | `Assets/_Project/Code/Presentation/` | ✅ Complete |
| `M0PlayerAnimationSet` ScriptableObject | `Assets/_Project/Content/Data/Animancer/` | ✅ Exists — clips empty |
| `M0AnimationPresentationAdapter` | `Assets/_Project/Code/Presentation/` | ✅ Wired in TickHandler |
| Project URP materials | `Assets/_Project/Content/Materials/Characters/Player/` | ✅ All mat groups present |
| Project model copy | `Assets/_Project/Content/Art/Model/Characters/` | ✅ FBX present |
| Project prefab copy | `Assets/_Project/Content/Prefabs/Characters/` | ✅ Magica cloth2 prefab present |

**Dependency note for S8-1–S8-4**: Those stories tune animation clip transitions
and timing. They require clips assigned to `M0PlayerAnimationSet` and a visible
character in the scene. This story provides that baseline.

## Available animation clips (vendor pack)

**Normal** (primary combat clips):
- `Idle.fbx` → `M0PlayerAnimationSet.idle`
- `Run.fbx` or `Walk.fbx` → `M0PlayerAnimationSet.locomotion`
- `Attack1.fbx` → `M0PlayerAnimationSet.lightAttack`
- `Attack2.fbx` or `Attack3.fbx` → `M0PlayerAnimationSet.heavyAttack`
- `Evade.fbx` → `M0PlayerAnimationSet.dodge`
- `Hit1.fbx` → hit reaction (assign to lightAttack slot as placeholder per existing driver code)
- `Stun.fbx` — available as fallback

**Special** (directional dodge / counter candidates):
- `Quickshift_B.fbx` — backstep dodge candidate
- `Sp_Skill1.fbx` or `Sp_Skill2.fbx` → `M0PlayerAnimationSet.counter` or `parry`

**Control Manifest Rules**:
- Required: `AnimancerPlayerAnimationDriver` observes `IPlayerStateMachine` — do not own gameplay truth.
- Forbidden: Do not re-enable root motion. `AnimancerPlayerAnimationDriver.disableRootMotion` must remain true.
- Guardrail: Do not use the vendor `School_Katana_Controller.controller`.

---

## Acceptance Criteria

- [ ] Player character renders with School_Katana_Girl mesh in the M0 duel scene Game View.
- [ ] `AnimancerComponent` is present on the player character object and assigned to `AnimancerPlayerAnimationDriver`.
- [ ] `M0PlayerAnimationSet` has clips assigned for: idle, locomotion, lightAttack, heavyAttack, dodge, parry, counter.
- [ ] Character transitions between Idle ↔ Moving animations when player moves.
- [ ] Attack1 clip plays when a light attack is triggered.
- [ ] Evade clip plays when dodge is triggered.
- [ ] Root motion remains disabled (`applyRootMotion = false`).
- [ ] No S1/S2 console errors from character wiring.
- [ ] No Magica Cloth 2 runtime physics errors (cloth simulation not required).
- [ ] No gameplay truth files (Combat Core, Health, Locomotion, TargetContext) modified.

---

## Implementation Notes

This is a Unity Editor authoring task — no new C# code required.

**Step 1 — Verify model import**
- Open `Assets/_Project/Content/Art/Model/Characters/School_Katana_FullBody-Magica cloth2.fbx` in Inspector.
- Confirm Rig is set to Humanoid or Generic as needed by Animancer.
- Confirm animation clips are embedded or confirm vendor FBX clips are accessible from `Animations/Normal/` and `Animations/Special/`.

**Step 2 — Set up player character in scene**
- Open `Gameplay_CombatPrototype.unity`.
- Locate the existing player GameObject (the one with `M0PlayerLocomotionAdapter`).
- Add (or confirm) `AnimancerComponent` on the character mesh child.
- Add `AnimancerPlayerAnimationDriver` to the character object and wire `animancer` and `animationSet` fields in the Inspector.
- Assign `M0PlayerAnimationSet` asset to `animationSet`.

**Step 3 — Assign clips to M0PlayerAnimationSet**
- Open `Assets/_Project/Content/Data/Animancer/M0PlayerAnimationSet.asset`.
- Assign vendor clips to each slot:
  - `idle` ← `Normal/Idle.fbx` clip
  - `locomotion` ← `Normal/Run.fbx` clip
  - `lightAttack` ← `Normal/Attack1.fbx` clip
  - `heavyAttack` ← `Normal/Attack2.fbx` clip
  - `dodge` ← `Normal/Evade.fbx` clip
  - `parry` ← `Special/Sp_Skill1.fbx` clip (placeholder)
  - `counter` ← `Special/Sp_Skill2.fbx` clip (placeholder)

**Step 4 — Wire AnimationPresentationAdapter**
- Confirm `M0AnimationPresentationAdapter` on the scene has `AnimancerPlayerAnimationDriver` as its injected `IPlayerAnimationService` (via VContainer LifetimeScope).
- If not registered, add `AnimancerPlayerAnimationDriver` to the LifetimeScope `RegisterComponentInHierarchy` or equivalent.

**Step 5 — Verify in Play mode**
- Enter Play mode. Move player — should see Idle → Run transition.
- Trigger light attack — should see Attack1 clip.
- Trigger dodge — should see Evade clip.
- Check Console for new S1/S2 errors.

**Performance**: No performance impact expected — wiring only, no new runtime systems added. AnimancerComponent was already ticking with empty clips; replacing with authored clips adds no measurable overhead.

---

## Out of Scope

- Magica Cloth 2 cloth physics simulation.
- Vendor `School_Katana_Controller.controller` as active controller.
- Avatar Mask / upper-body layering.
- HitReaction clip slot (not in `M0PlayerAnimationSet` — use existing fallback in driver).
- New C# code.

---

## QA Test Cases

- **AC-1**: Character visible.
  - Enter Play mode. Verify School_Katana_Girl mesh renders. No pink/missing materials.

- **AC-2**: Idle/Move animation plays.
  - Move player with input. Verify Idle → Run clip transition occurs.

- **AC-3**: Attack clip plays.
  - Trigger light attack. Verify Attack1 clip plays on the Animancer component.

- **AC-4**: Dodge clip plays.
  - Trigger dodge. Verify Evade clip plays.

- **AC-5**: Console clean.
  - No new S1/S2 errors in Console after entering and exiting Play mode.

- **AC-6**: Presentation boundary.
  - Diff review: only scene, prefab, ScriptableObject, and FBX import settings changed.
  - No Combat Core, Health, Locomotion, or TargetContext `.cs` files modified.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- `production/qa/evidence/s8-7-school-katana-girl-wiring-evidence.md`
- Game View screenshot: character rendered in duel scene with animation playing.
- Console clean note.

**Status**: [x] Created

---

## Dependencies

- Depends on: Story 1-11 (Animator Observer Adapters — Verified with notes), `AnimancerPlayerAnimationDriver` (exists)
- Blocks: S8-1, S8-2, S8-3, S8-4 (require visible character and assigned clips)
- Unlocks: Sprint 8 animation polish stories

---

## Completion Notes

**Completed**: 2026-06-17
**Criteria**: 10/10 passing
**Deviations**: None
**Test Evidence**: Visual/Feel — evidence doc at `production/qa/evidence/s8-7-school-katana-girl-wiring-evidence.md`, screenshot at `Assets/_Project/Screenshots/s8-7-play-mode-test.png`
**Code Review**: Skipped (Visual/Feel — no C# code; scene authoring only)
