# Proposal: Create M0 Playable Combat Prototype Scene

> **Change ID**: create-m0-playable-combat-prototype-scene
> **Schema**: spec-driven
> **Status**: Proposed
> **Date**: 2026-05-16
> **Author**: User + Codex

## Problem Statement

The current M0 logic-only combat prototype is not visible in PlayMode. Game View previously showed "No cameras rendering", and prototype feedback is mostly console logs and EditMode tests. Before adding health and hit reactions (Story 1-7), we need a stable visible combat prototype scene so damage, stagger, and control suppression can be verified visually.

## Proposed Solution

Turn the current M0 logic-only combat prototype into a visible playable prototype scene by:
- Ensuring Gameplay_CombatPrototype.unity has an active runtime camera that renders Game View
- Adding or restoring Main Camera if missing
- Ensuring CameraMovementBasisProvider uses the runtime camera transform
- Ensuring Player and Enemy are visible in Game View
- Adding minimal presentation-only visual feedback for combat actions
- Adding debug overlay or temporary read-only labels for combat state visibility

## Success Criteria

- Game View no longer says "No cameras rendering"
- Runtime Main Camera renders the scene
- Player is visible and moves with WASD
- Enemy is visible
- LightAttack, HeavyAttack, Parry, Dodge, Counter have minimal visual feedback
- Enemy intent phases are visible without console logs
- Debug overlay shows combat state, enemy intent state, CounterWindow state
- No Console errors
- All Story 1-6 gameplay behavior preserved

## Out of Scope

- Health/damage/hit reaction implementation (Story 1-7)
- Memory Reveal / Memory VFX
- KCC
- Animancer/Animator authority
- Root motion
- Camera polish beyond basic runtime camera visibility
- Input architecture refactor
- CombatCore logic modification
- Locomotion logic modification
- EnemyIntentModel logic modification
- Asset Store package modifications
- Generated DI
- Story/sprint status updates

## Risks

- **Risk**: Adding visual components might inadvertently store gameplay truth
  - **Mitigation**: Enforce read-only observation pattern; visual components observe snapshots only

- **Risk**: Camera setup might conflict with existing CameraMovementBasisProvider
  - **Mitigation**: Verify CameraMovementBasisProvider uses runtime camera transform

- **Risk**: Visual feedback timing might desync from combat state
  - **Mitigation**: Visual components observe snapshots directly; no timing logic in visual layer

## Dependencies

- Story 1-1: Foundation Scene & VContainer Wiring (Complete)
- Story 1-2: Camera-Relative Movement (Complete)
- Story 1-3: Lock-On Wiring (Complete)
- Story 1-4: Player Attack Resolution (Complete)
- Story 1-5: Enemy Intent & Telegraph Loop (Complete)
- Story 1-6: Parry & Dodge Integration (Complete)

## Timeline Estimate

0.5d (half day) - This is a technical visibility fix, not a new gameplay feature.
