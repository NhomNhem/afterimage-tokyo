# S8-7 Evidence: Wire School_Katana_Girl into M0 Duel Scene

**Status**: PASS
**Date**: 2026-06-17
**Implementer**: OpenCode (Terminal)

## Summary

School_Katana_Girl character wired into M0 duel scene. All 7 `M0PlayerAnimationSet` clips assigned, child Animator cleaned (vendor controller removed, root motion disabled), `AnimancerComponent` repointed to child mesh Animator. Play mode clean with zero errors.

## Acceptance Criteria

| # | Criterion | Result | Method |
|---|-----------|--------|--------|
| AC-1 | Character renders with School_Katana_Girl mesh | ✅ Pass | Play mode test + screenshot |
| AC-2 | AnimancerComponent present and assigned to driver | ✅ Pass | SerializedObject inspection |
| AC-3 | M0PlayerAnimationSet clips assigned (all 7) | ✅ Pass | SerializedProperty verification |
| AC-4 | Idle ↔ Moving transition on player input | ✅ Pass | Manual playtest confirmation |
| AC-5 | Attack1 plays on light attack trigger | ✅ Pass | Manual playtest confirmation |
| AC-6 | Evade plays on dodge trigger | ✅ Pass | Manual playtest confirmation |
| AC-7 | Root motion disabled | ✅ Pass | bool verification (driver + child Animator) |
| AC-8 | No S1/S2 console errors | ✅ Pass | Console check after play mode |
| AC-9 | No Magica Cloth errors | ✅ Pass | Console check — zero cloth errors |
| AC-10 | No gameplay truth files modified | ✅ Pass | Scope check (scene + asset only) |

## Key Actions

1. **Rig check**: `School_Katana_FullBody-Magica cloth2.fbx` — Generic (Animancer-compatible)
2. **Child Animator cleanup**: Removed vendor `School_Katana_Controller.controller`, set `applyRootMotion = false`
3. **AnimancerComponent repointed**: `_Animator` field from `Player` → `School_Katana_FullBody-Magica cloth2` (where SkinnedMeshRenderers and avatar live)
4. **Clip assignment**: All 7 `M0AnimationClipTransition.clip` sub-properties assigned via SerializedProperty

## Deviations

None.

## Comments

- AC-4/5/6 confirmed by developer via manual Play mode test
- Screenshot: `Assets/_Project/Screenshots/s8-7-play-mode-test.png` (inside Unity submodule)
- Story: `production/sprints/sprint-8-stories/story-s8-7-wire-school-katana-girl-into-m0-scene.md`
