# Proposal: Complete M0 Playable Combat Prototype Verification

> **Change ID**: complete-m0-playable-combat-prototype-verification  
> **Schema**: spec-driven  
> **Status**: Completed with Notes (2026-05-21 story-done closure; no blockers)  
> **Date**: 2026-05-21

## Goal

Finish missing PlayMode verification and minimal scene/reference fixes for the archived `create-m0-playable-combat-prototype-scene` change.  
This is verification/testability cleanup only, not new gameplay.

## Scope

- Verify Main Camera renders Game View.
- Verify PlayerMesh is visible and follows Player.
- Verify EnemyMesh is visible and follows Enemy.
- Verify `CameraMovementBasisProvider` uses runtime Main Camera.
- Verify WASD visibly moves Player.
- Verify LightAttack / HeavyAttack / Parry / Dodge / Counter visual feedback.
- Verify Enemy intent phase visual cycle.
- Verify Debug Overlay labels are visible and update.
- Verify existing Story 1-6 behavior still works.
- Fix only minimal scene/reference issues needed to make the above true.

## Hard Exclusions

- no health/damage/hit reaction changes
- no memory reveal/VFX
- no KCC
- no Animancer/root motion authority
- no input architecture refactor
- no CombatCore logic changes
- no Locomotion logic changes
- no EnemyIntentModel logic changes
- no generated DI
- no forbidden APIs
- no new gameplay features

## Expected Output

- Updated verification evidence for prototype scene PlayMode checks
- Reconciled task checklist with explicit pass/fail status
- Clear archive-readiness statement for prototype verification change
