# Design: Create M0 Playable Combat Prototype Scene

> **Change ID**: create-m0-playable-combat-prototype-scene
> **Proposal**: proposal.md
> **Date**: 2026-05-16

## Design Overview

This change transforms the current M0 logic-only combat prototype into a visible playable prototype scene by stabilizing the runtime camera, ensuring player/enemy visibility, adding minimal visual feedback for combat actions, and providing debug overlay visibility for combat state.

## Architecture Decisions

### 1. Runtime Camera Setup

**Decision**: Ensure Gameplay_CombatPrototype.unity has an active Main Camera that renders Game View.

**Rationale**: Current Game View shows "No cameras rendering". A runtime Main Camera is required for PlayMode visibility.

**Implementation**:
- Add or restore Main Camera GameObject to scene if missing
- Configure Main Camera with standard settings (clear flags, culling mask, projection)
- If Cinemachine is already in project, add CinemachineBrain to Main Camera only if needed for existing camera system
- Do NOT use Scene Camera as runtime camera (Scene Camera is for Editor only)

**Dependencies**: None (independent change)

**Guardrails**:
- Camera must not mutate combat, target, input, enemy intent, health, or locomotion truth
- Camera is presentation-only; observes but does not own gameplay state

### 2. CameraMovementBasisProvider Integration

**Decision**: Ensure CameraMovementBasisProvider uses the runtime camera transform.

**Rationale**: Camera-relative movement (Story 1-2) depends on CameraMovementBasisProvider having a valid camera transform.

**Implementation**:
- Verify CameraMovementBasisProvider.camera field references Main Camera
- If field is null or references Scene Camera, reassign to Main Camera
- Test that WASD movement works relative to camera basis

**Dependencies**: Story 1-2 (Camera-Relative Movement) - Complete

**Guardrails**:
- CameraMovementBasisProvider observes camera transform only
- No gameplay truth stored in camera component

### 3. Player/Enemy Visibility

**Decision**: Ensure Player and Enemy scene objects are visible in Game View.

**Rationale**: Prototype feedback requires visual confirmation of participant positions and actions.

**Implementation**:
- Verify Player_M0Prototype scene object or prefab instance exists in scene
- Verify Enemy_M0Prototype / Enemy_M0TargetablePrototype scene object or prefab instance exists in scene
- Ensure both objects have Renderer components (MeshRenderer, SkinnedMeshRenderer, or SpriteRenderer)
- Ensure both objects are within Main Camera frustum
- If objects are missing or invisible, restore/adjust positions or add placeholder meshes

**Dependencies**: Story 1-1 (Foundation Scene & VContainer Wiring) - Complete

**Guardrails**:
- Player/Enemy GameObjects are composition roots; gameplay truth in Pure C# models
- No gameplay truth stored in MonoBehaviour fields

### 4. Minimal Visual Feedback for Combat Actions

**Decision**: Add minimal presentation-only visual feedback for LightAttack, HeavyAttack, Parry, Dodge, Counter, and Enemy intent phases.

**Rationale**: Prototype feedback requires visual confirmation of action triggers without relying on console logs.

**Implementation**:
- Create simple visual feedback adapter: `M0CombatVisualFeedbackAdapter` (GlassRefrain.Presentation assembly)
- Adapter observes Combat Core snapshot and Enemy Intent snapshot via event subscriptions
- On LightAttack trigger: Change player material color temporarily or scale briefly
- On HeavyAttack trigger: Different material color or scale change
- On Parry trigger: Brief player color flash or scale
- On Dodge trigger: Brief player scale or position offset (visual only)
- On Counter trigger: Stronger visual feedback (e.g., color + scale)
- On Enemy Telegraph: Change enemy material color or add simple label
- On Enemy Active: Different enemy color or label
- On Enemy Recovery: Different enemy color or label
- Visual feedback duration: 0.2-0.5 seconds (short and readable)
- Use placeholder materials/colors/scale (no final art)

**Dependencies**: Story 1-4 (Player Attack Resolution) - Complete, Story 1-5 (Enemy Intent & Telegraph Loop) - Complete, Story 1-6 (Parry & Dodge Integration) - Complete

**Guardrails**:
- Visual adapter observes snapshots only; does not mutate gameplay state
- No gameplay truth in visual components
- Visual feedback is presentation-only; does not affect combat validity

### 5. Debug Overlay for Combat State

**Decision**: Add debug overlay or temporary read-only labels showing combat state, enemy intent state, CounterWindow state, and last input action.

**Rationale**: Prototype tuning requires inspectable state without console logs.

**Implementation**:
- Create debug overlay adapter: `M0CombatDebugOverlayAdapter` (GlassRefrain.Presentation assembly)
- Adapter subscribes to snapshot events from Combat Core, Enemy Intent, and Input
- Display read-only text labels in UI:
  - Combat State: e.g., "Neutral", "LightAttackActive", "ParryActive"
  - Enemy Intent State: e.g., "Telegraph", "Commit", "Active", "Recovery"
  - CounterWindow: "Open: 0.5s / 2.0s" or "Closed"
  - Last Input Action: e.g., "LightAttack", "HeavyAttack", "Parry", "Dodge", "Counter"
  - LockOn Target: "None" or "Enemy_M0Prototype"
- Use Unity UI Text components in a Canvas (Screen Space - Overlay)
- Position overlay in corner (e.g., top-left or bottom-left)
- Add toggle key (e.g., F1) to show/hide overlay

**Dependencies**: Story 1-4, Story 1-5, Story 1-6 - All Complete

**Guardrails**:
- Debug overlay is read-only; does not mutate gameplay state
- No gameplay truth stored in UI components
- Debug overlay observes snapshots only

### 6. Preservation of Existing Gameplay Behavior

**Decision**: All Story 1-6 gameplay behavior must be preserved.

**Rationale**: This is a visibility fix, not a gameplay change.

**Implementation**:
- Do not modify CombatCore logic
- Do not modify Locomotion logic
- Do not modify EnemyIntentModel logic
- Do not modify Input architecture
- Verify after changes:
  - WASD movement still works
  - LockOn still works
  - LightAttack/HeavyAttack resolution still works
  - Parry/Dodge/Counter resolution still works
  - CounterWindow expiry/consume still works
  - Enemy intent loop still cycles
  - EditMode tests still pass (15/15 defensive tests)

**Dependencies**: All Stories 1-1 through 1-6 - Complete

**Guardrails**:
- No gameplay logic changes
- Visual layer is strictly observational

## Assembly Boundaries

### GlassRefrain.Presentation (New or Extended)
- **Purpose**: Presentation-only adapters for visual feedback and debug overlay
- **Dependencies**: GlassRefrain.Core (for snapshot contracts)
- **Forbidden**: Must NOT depend on GlassRefrain.Combat, GlassRefrain.Enemy, GlassRefrain.Input directly
- **Pattern**: Subscribe to snapshot events; render presentation; no gameplay state mutation

### Existing Assemblies (Unchanged)
- GlassRefrain.Combat: No changes
- GlassRefrain.Enemy: No changes
- GlassRefrain.Input: No changes
- GlassRefrain.Bootstrap: No changes (except potential scene wiring for visual adapters)

## Data Flow

```
Combat Core Snapshot → CombatVisualFeedbackAdapter → Material/Scale Changes
Combat Core Snapshot → CombatDebugOverlayAdapter → UI Text Labels
Enemy Intent Snapshot → CombatVisualFeedbackAdapter → Enemy Material/Label
Enemy Intent Snapshot → CombatDebugOverlayAdapter → Enemy State Label
Input Snapshot → CombatDebugOverlayAdapter → Last Input Label
```

## Forbidden Patterns

- No FindObjectOfType, FindFirstObjectByType, GameObject.Find
- No Resources.Load
- No legacy Input Manager (Keyboard.current, Mouse.current, Gamepad.current polling)
- No gameplay truth storage in MonoBehaviours
- No animation/root motion authority (Animancer/Animator state as gameplay truth)
- No KCC
- No NavMesh
- No health/damage/hit reaction in this change
- No Memory Reveal / Memory VFX in this change
- No generated DI
- No Asset Store package modifications

## Verification Plan

### Manual Verification (PlayMode)
- Enter PlayMode - confirm Game View renders (no "No cameras rendering")
- Confirm Main Camera is active and rendering
- Confirm Player is visible
- Confirm Enemy is visible
- Press WASD - confirm player moves visibly
- Press F (LockOn) - confirm target acquisition or debug label shows current target
- Press Left Click (LightAttack) - confirm visual feedback triggers
- Press Right Click (HeavyAttack) - confirm visual feedback triggers
- Press Q (Parry) - confirm visual feedback triggers
- Press LShift (Dodge) - confirm visual feedback triggers
- Press E (Counter) - confirm visual feedback triggers when valid
- Observe Enemy - confirm Telegraph/Active/Recovery phases are visible via color/label
- Press F1 - confirm debug overlay toggles
- Read debug overlay - confirm combat state, enemy intent state, CounterWindow state, last input are displayed
- Verify no Console errors
- Verify existing Story 1-6 behavior still works (movement, attacks, parry, dodge, counter, lockOn, enemy intent loop)

### EditMode Tests
- Run existing EditMode tests (M0DefensiveResolutionTests) - confirm 15/15 PASS
- No new EditMode tests required for this change (presentation-only)

## Open Questions

None - this is a straightforward visibility fix with clear scope boundaries.

## Alternatives Considered

### Alternative 1: Use Console Logs Only
- **Description**: Continue using console logs for prototype feedback
- **Pros**: No new code
- **Cons**: Not visible in Game View; requires Console window split; less intuitive for visual feedback
- **Rejection Reason**: Goal is visible playable prototype; console logs insufficient for visual verification

### Alternative 2: Full Animation System
- **Description**: Implement full Animancer/Animator setup for combat actions
- **Pros**: More polished visual feedback
- **Cons**: Out of scope for M0; introduces animation authority complexity; requires animation assets
- **Rejection Reason**: Out of scope; this change is for visibility only, not animation polish

### Alternative 3: Skip Debug Overlay
- **Description**: Add visual feedback but no debug overlay
- **Pros**: Simpler implementation
- **Cons**: Cannot inspect combat state without console logs; harder to tune
- **Rejection Reason**: Debug overlay is essential for prototype tuning before Story 1-7

## Impact Assessment

### Positive Impact
- Visible playable prototype enables visual verification of combat behavior
- Debug overlay provides inspectable state without console logs
- Foundation for Story 1-7 health/damage/hit reaction visual verification

### Negative Impact
- Adds presentation code (minimal scope)
- Requires scene modifications

### Neutral Impact
- No gameplay logic changes
- No performance impact (simple material/label changes)

## Rollback Plan

If visual feedback causes issues:
- Disable or remove CombatVisualFeedbackAdapter
- Disable or remove CombatDebugOverlayAdapter
- Scene changes can be reverted by restoring scene backup

No gameplay logic changes, so rollback is safe.
