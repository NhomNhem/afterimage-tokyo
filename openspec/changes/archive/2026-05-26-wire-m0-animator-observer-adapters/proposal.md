## Why

The M0 animation observer adapter stack is already implemented in code (`M0AnimationPresentationAdapter`, `AnimancerPlayerAnimationDriver`, `AnimancerEnemyAnimationDriver`, interfaces, DI wiring, tick handler routing), but the scene GameObjects do not have the required Animator, AnimancerComponent, or animation driver components attached. Without scene wiring, the presentation layer cannot observe gameplay snapshots and the M0 duel loop has no visual animation feedback.

This is the last remaining story in Sprint 1 (10/11 verified). Closing it completes the presentation layer wiring for M0.

## What Changes

- Attach Animator, AnimancerComponent, and `AnimancerPlayerAnimationDriver` to the Player GameObject in the M0 scene
- Attach Animator, AnimancerComponent, and `AnimancerEnemyAnimationDriver` to the Enemy GameObject in the M0 scene
- Verify `M0AnimationPresentationAdapter` is on the tick handler GameObject and referenced in `GameplayLifetimeScope`
- Create focused EditMode tests proving the adapter/driver is presentation-only (no gameplay truth ownership)
- Create PlayMode evidence showing runtime starts without DI/NullReference errors and combat loop still runs after wiring

## Capabilities

### New Capabilities

- `m0-animator-observer-adapters`: Wire Animancer-based animation observer adapters into the M0 scene so Player and Enemy presentation SHALL observe CombatCore, Locomotion, and EnemyIntent snapshots without owning gameplay truth.

### Modified Capabilities

None. No existing spec-level behavior changes.

## Impact

- **Scene**: Player and Enemy GameObjects gain Animator + AnimancerComponent + animation driver components
- **DI**: No changes — `GameplayLifetimeScope` wiring already complete
- **Tick Handler**: No changes — routing already complete
- **Tests**: New `AnimatorPresentationOnly_test.cs` EditMode test file
- **Evidence**: New PlayMode evidence file
- **Ownership boundary**: Presentation only — SHALL not affect gameplay truth
