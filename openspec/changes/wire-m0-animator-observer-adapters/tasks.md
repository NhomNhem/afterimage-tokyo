## 1. Scene Wiring — Player Animation Components

- [x] 1.1 Add `Animator` component to Player GameObject (instance 97846)
- [x] 1.2 Add `AnimancerComponent` to Player GameObject
- [x] 1.3 Add `AnimancerPlayerAnimationDriver` to Player GameObject
- [x] 1.4 Verify `AnimancerPlayerAnimationDriver.animancer` field references the AnimancerComponent
- [x] 1.5 Verify `disableRootMotion` is `true` on the driver

## 2. Scene Wiring — Enemy Animation Components

- [x] 2.1 Add `Animator` component to Enemy GameObject (instance 97812)
- [x] 2.2 Add `AnimancerComponent` to Enemy GameObject
- [x] 2.3 Add `AnimancerEnemyAnimationDriver` to Enemy GameObject
- [x] 2.4 Verify `AnimancerEnemyAnimationDriver.animancer` field references the AnimancerComponent
- [x] 2.5 Verify `disableRootMotion` is `true` on the driver

## 3. Scene Wiring — Adapter & DI Verification

- [x] 3.1 Verify `M0AnimationPresentationAdapter` is on the M0GameplayTickHandler GameObject
- [x] 3.2 Verify `GameplayLifetimeScope.animationPresentationAdapter` field references the adapter
- [x] 3.3 Verify `GameplayLifetimeScope.playerAnimationDriver` field references the player driver
- [x] 3.4 Verify `GameplayLifetimeScope.enemyAnimationDriver` field references the enemy driver

## 4. EditMode Tests — Presentation-Only Boundary

- [x] 4.1 Create `Assets/_Project/Tests/EditMode/AnimatorPresentationOnly_test.cs`
- [x] 4.2 Test: `M0AnimationPresentationAdapter` routes combat states to correct animation methods without modifying snapshot data
- [x] 4.3 Test: `M0AnimationPresentationAdapter` routes locomotion states to correct animation methods, gated by combat state
- [x] 4.4 Test: `M0AnimationPresentationAdapter` routes enemy intent states to correct animation methods
- [x] 4.5 Test: Duplicate state observations are skipped (no redundant Play calls)
- [x] 4.6 Test: `AnimancerPlayerAnimationDriver` handles null clips without throwing
- [x] 4.7 Test: `AnimancerEnemyAnimationDriver` handles null clips without throwing
- [x] 4.8 Test: `M0AnimationClipTransition.IsAssigned` returns false for null clips
- [x] 4.9 Test: Animation drivers do not reference gameplay types from Domain layer directly

## 5. PlayMode Verification

- [x] 5.1 Enter PlayMode and verify no `VContainerException` or `NullReferenceException` on startup
- [x] 5.2 Verify console has no error-level logs from animation components
- [x] 5.3 Perform LightAttack (Mouse Left) — verify animation driver logs missing clip warning, combat continues
- [x] 5.4 Perform Dodge (Left Shift) — verify animation driver logs missing clip warning, displacement still occurs
- [x] 5.5 Perform Parry (Q) then Counter (E) — verify counter path still works
- [x] 5.6 Verify debug overlay still displays combat/locomotion/enemy state correctly
- [x] 5.7 Disable Animator component on Player — verify WASD movement still works

## 6. Evidence Documentation

- [x] 6.1 Create `production/qa/evidence/story-1-11-animator-observer-adapters-verification-2026-05-26.md`
- [x] 6.2 Document EditMode test results (pass/fail counts)
- [x] 6.3 Document PlayMode verification results
- [x] 6.4 Document null clip tolerance evidence
- [x] 6.5 Document authority boundary evidence (movement without Animator)
