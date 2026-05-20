# Tasks: Create M0 Playable Combat Prototype Scene

> **Change**: create-m0-playable-combat-prototype-scene
> **Design**: openspec/changes/create-m0-playable-combat-prototype-scene/design.md

---

## 1. Runtime Camera Setup

- [x] 1.1 Open `Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity` in Unity Editor
- [x] 1.2 Verify Main Camera GameObject exists in scene
- [x] 1.3 If Main Camera is missing, add Main Camera GameObject (GameObject > Camera)
- [x] 1.4 Configure Main Camera:
  - Clear Flags: Skybox
  - Culling Mask: Everything (or appropriate layers)
  - Projection: Perspective
  - Field of View: 60
  - Clipping Planes: Near 0.3, Far 1000
- [ ] 1.5 If Cinemachine is already in project, verify CinemachineBrain component on Main Camera (add only if needed for existing camera system)
- [x] 1.6 Ensure Main Camera is active (GameObject active in hierarchy)
- [x] 1.7 Verify Scene Camera is NOT being used as runtime camera (Scene Camera is Editor-only)
- [x] 1.8 Save scene

## 2. CameraMovementBasisProvider Integration

- [ ] 2.1 Locate CameraMovementBasisProvider component in scene (likely on Player_M0Prototype or separate GameObject)
- [ ] 2.2 Verify CameraMovementBasisProvider.camera field references Main Camera
- [ ] 2.3 If field is null, assign Main Camera to CameraMovementBasisProvider.camera
- [ ] 2.4 If field references Scene Camera, reassign to Main Camera
- [ ] 2.5 Enter PlayMode and test WASD movement - confirm player moves relative to camera basis
- [ ] 2.6 Exit PlayMode and save scene

## 3. Player/Enemy Visibility

- [x] 3.1 Verify Player_M0Prototype scene object or prefab instance exists in scene
- [x] 3.2 Verify Enemy_M0Prototype / Enemy_M0TargetablePrototype scene object or prefab instance exists in scene
- [x] 3.3 For Player_M0Prototype:
  - Verify Renderer component exists (MeshRenderer, SkinnedMeshRenderer, or SpriteRenderer)
  - If missing, add placeholder MeshRenderer with primitive mesh (Cube or Sphere)
  - Ensure material is assigned
  - Ensure object is within Main Camera frustum (adjust position if needed)
- [x] 3.4 For Enemy_M0Prototype / Enemy_M0TargetablePrototype:
  - Verify Renderer component exists
  - If missing, add placeholder MeshRenderer with primitive mesh
  - Ensure material is assigned (different color from player for distinction)
  - Ensure object is within Main Camera frustum (adjust position if needed)
- [x] 3.5 Save scene

## 4. Visual Feedback Adapter - Core Structure

- [x] 4.1 Create or verify `Assets/_Project/Code/Presentation` folder
- [x] 4.2 Create or verify `GlassRefrain.Presentation.asmdef` with reference to `GlassRefrain.Core`
- [x] 4.3 Verify `GlassRefrain.Presentation.asmdef` does NOT reference `GlassRefrain.Combat`, `GlassRefrain.Enemy`, `GlassRefrain.Input`
- [x] 4.4 Create `M0CombatVisualFeedbackAdapter.cs` in `Assets/_Project/Code/Presentation/`
- [x] 4.5 Implement MonoBehaviour structure with:
  - References to Combat Core snapshot provider (via event subscription)
  - References to Enemy Intent snapshot provider (via event subscription)
  - Renderer references for player and enemy (assigned in Inspector)
  - Placeholder materials for feedback states (assigned in Inspector)
- [x] 4.6 Add `M0CombatVisualFeedbackAdapter` component to scene GameObject (e.g., PresentationAdapter or separate GameObject)
- [ ] 4.7 Assign Player Renderer, Enemy Renderer, and placeholder materials in Inspector
- [ ] 4.8 Wire Combat Core snapshot event subscription (if Combat Core exposes SnapshotChanged event)
- [ ] 4.9 Wire Enemy Intent snapshot event subscription (if Enemy Intent exposes SnapshotChanged event)
- [x] 4.10 Verify no forbidden dependencies: no FindObjectOfType, no GameObject.Find, no Resources.Load, no legacy Input polling

## 5. Visual Feedback - Player Actions

- [x] 5.1 In `M0CombatVisualFeedbackAdapter`, implement LightAttack feedback:
  - Detect LightAttack trigger from Combat Core snapshot (state transition or action result)
  - Change player material color temporarily (e.g., flash white or red)
  - Duration: 0.2 seconds
  - Restore original material after duration
- [x] 5.2 Implement HeavyAttack feedback:
  - Detect HeavyAttack trigger from Combat Core snapshot
  - Change player material color with different color (e.g., flash yellow or orange)
  - Duration: 0.3 seconds
  - Restore original material after duration
- [x] 5.3 Implement Parry feedback:
  - Detect Parry trigger from Combat Core snapshot
  - Change player material color briefly (e.g., flash blue)
  - Duration: 0.2 seconds
  - Restore original material after duration
- [x] 5.4 Implement Dodge feedback:
  - Detect Dodge trigger from Combat Core snapshot
  - Briefly scale player (e.g., scale to 0.9 then back to 1.0)
  - Duration: 0.3 seconds
  - Restore original scale after duration
- [x] 5.5 Implement Counter feedback:
  - Detect Counter trigger from Combat Core snapshot
  - Stronger visual feedback (e.g., color + scale: flash green + scale to 1.2)
  - Duration: 0.5 seconds
  - Restore original material and scale after duration
- [ ] 5.6 Enter PlayMode and test each action - confirm visual feedback triggers for LightAttack, HeavyAttack, Parry, Dodge, Counter
- [ ] 5.7 Exit PlayMode and save scene

## 6. Visual Feedback - Enemy Intent Phases

- [x] 6.1 In `M0CombatVisualFeedbackAdapter`, implement Enemy Telegraph feedback:
  - Detect Telegraph state from Enemy Intent snapshot
  - Change enemy material color (e.g., yellow)
  - Maintain color while in Telegraph state
- [x] 6.2 Implement Enemy Active feedback:
  - Detect Active state from Enemy Intent snapshot
  - Change enemy material color (e.g., red)
  - Maintain color while in Active state
- [x] 6.3 Implement Enemy Recovery feedback:
  - Detect Recovery state from Enemy Intent snapshot
  - Change enemy material color (e.g., gray)
  - Maintain color while in Recovery state
- [ ] 6.4 Enter PlayMode and test - confirm enemy color changes through Telegraph → Commit → Active → Recovery cycle
- [ ] 6.5 Exit PlayMode and save scene

## 7. Debug Overlay Adapter - Core Structure

- [x] 7.1 Create `M0CombatDebugOverlayAdapter.cs` in `Assets/_Project/Code/Presentation/`
- [x] 7.2 Implement MonoBehaviour structure with:
  - Canvas reference (assigned in Inspector or created at runtime)
  - Text component references for labels (assigned in Inspector)
  - Combat Core snapshot event subscription
  - Enemy Intent snapshot event subscription
  - Input snapshot event subscription (if available)
- [x] 7.3 Create Canvas in scene (GameObject > UI > Canvas)
  - Render Mode: Screen Space - Overlay
  - Canvas Scaler: Scale with Screen Size (1920x1080 reference)
- [x] 7.4 Create Text GameObjects under Canvas for debug labels:
  - Combat State Label (top-left)
  - Enemy Intent State Label (below Combat State)
  - CounterWindow Label (below Enemy Intent State)
  - Last Input Action Label (below CounterWindow)
  - LockOn Target Label (below Last Input)
- [x] 7.5 Add `M0CombatDebugOverlayAdapter` component to Canvas or separate GameObject
- [ ] 7.6 Assign Text component references in Inspector
- [ ] 7.7 Wire snapshot event subscriptions
- [x] 7.8 Implement toggle key (F1) to show/hide Canvas
- [x] 7.9 Verify no forbidden dependencies

## 8. Debug Overlay - State Display

- [x] 8.1 Implement Combat State display:
  - Read Combat Core snapshot state
  - Update Combat State Label text (e.g., "Combat: Neutral", "Combat: LightAttackActive")
  - Update every frame or on snapshot change
- [x] 8.2 Implement Enemy Intent State display:
  - Read Enemy Intent snapshot state
  - Update Enemy Intent State Label text (e.g., "Enemy: Telegraph", "Enemy: Active")
  - Update every frame or on snapshot change
- [x] 8.3 Implement CounterWindow display:
  - Read Combat Core snapshot CounterWindow state
  - Update CounterWindow Label text (e.g., "CounterWindow: Open 0.5s/2.0s" or "CounterWindow: Closed")
  - Update every frame or on snapshot change
- [x] 8.4 Implement Last Input Action display:
  - Read Input snapshot or track last pressed action
  - Update Last Input Action Label text (e.g., "Last Input: LightAttack", "Last Input: Parry")
  - Update on input change
- [x] 8.5 Implement LockOn Target display:
  - Read Target Context snapshot
  - Update LockOn Target Label text (e.g., "LockOn: None" or "LockOn: Enemy_M0Prototype")
  - Update on target change
- [ ] 8.6 Enter PlayMode and test:
  - Press F1 - confirm overlay toggles
  - Perform actions - confirm labels update correctly
  - Observe enemy cycle - confirm enemy state label updates
- [ ] 8.7 Exit PlayMode and save scene

## 9. VContainer Registration (if needed)

- [x] 9.1 If `M0CombatVisualFeedbackAdapter` requires dependency injection, register in VContainer:
  - Add manual registration in Bootstrap composition root
  - Do NOT use automatic scanning or code generation
  - Verify registration follows ADR-0004 (manual VContainer only)
- [x] 9.2 If `M0CombatDebugOverlayAdapter` requires dependency injection, register in VContainer:
  - Add manual registration in Bootstrap composition root
  - Do NOT use automatic scanning or code generation
  - Verify registration follows ADR-0004
- [x] 9.3 If no DI needed (MonoBehaviour with Inspector-assigned references), skip this section

## 10. Verification - Gameplay Preservation

- [ ] 10.1 Enter PlayMode
- [ ] 10.2 Confirm Game View renders (no "No cameras rendering")
- [ ] 10.3 Confirm WASD movement works
- [ ] 10.4 Confirm F (LockOn) works or debug label shows target
- [ ] 10.5 Confirm Left Click (LightAttack) works and visual feedback triggers
- [ ] 10.6 Confirm Right Click (HeavyAttack) works and visual feedback triggers
- [ ] 10.7 Confirm Q (Parry) works and visual feedback triggers
- [ ] 10.8 Confirm LShift (Dodge) works and visual feedback triggers
- [ ] 10.9 Confirm E (Counter) works when valid and visual feedback triggers
- [ ] 10.10 Confirm enemy cycles through Telegraph → Commit → Active → Recovery
- [ ] 10.11 Confirm CounterWindow opens on successful parry and closes on expiry/consume
- [ ] 10.12 Confirm no Console errors
- [ ] 10.13 Exit PlayMode
- [ ] 10.14 Run EditMode tests: `M0DefensiveResolutionTests` - confirm 15/15 PASS
- [ ] 10.15 Verify no gameplay logic changes (Combat Core, Locomotion, Enemy Intent, Input unchanged)

## 11. Scope Exclusion Verification

- [ ] 11.1 Verify no health mutation code added
- [ ] 11.2 Verify no damage application code added
- [ ] 11.3 Verify no hit reaction implementation (beyond visual feedback)
- [ ] 11.4 Verify no stagger implementation (beyond visual feedback)
- [ ] 11.5 Verify no Memory Reveal code added
- [ ] 11.6 Verify no Memory VFX code added
- [ ] 11.7 Verify no KCC code added
- [ ] 11.8 Verify no Animancer/Animator authority added
- [ ] 11.9 Verify no root motion added
- [ ] 11.10 Verify no NavMesh code added
- [ ] 11.11 Verify no input architecture refactor
- [ ] 11.12 Verify no CombatCore logic changes
- [ ] 11.13 Verify no Locomotion logic changes
- [ ] 11.14 Verify no EnemyIntentModel logic changes
- [ ] 11.15 Verify no generated DI used
- [ ] 11.16 Verify no Asset Store package modifications

## 12. Scene Backup and Cleanup

- [ ] 12.1 Backup current `Gameplay_CombatPrototype.unity` before changes (copy to .backup)
- [ ] 12.2 After implementation, verify scene file size is reasonable
- [ ] 12.3 Verify no unintended GameObjects added to scene
- [ ] 12.4 Verify scene hierarchy is clean
- [ ] 12.5 Save final scene

---

> **Note:** This change is for prototype visibility only. Do not implement health/damage/hit reaction (Story 1-7). Do not update story or sprint status during implementation.
