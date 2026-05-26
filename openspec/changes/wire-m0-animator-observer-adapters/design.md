## Context

The M0 animation observer adapter stack is already fully implemented in C# code:

- `M0AnimationPresentationAdapter` — MonoBehaviour that receives `M0CombatSnapshot`, `LocomotionStateSnapshot`, and `EnemyIntentSnapshot` and routes them to `IPlayerAnimationService` / `IEnemyAnimationService`
- `IPlayerAnimationService` / `IEnemyAnimationService` — interfaces defining animation playback methods
- `AnimancerPlayerAnimationDriver` / `AnimancerEnemyAnimationDriver` — Animancer-based MonoBehaviour implementations
- `M0PlayerAnimationSet` / `M0EnemyAnimationSet` — ScriptableObject assets holding `M0AnimationClipTransition` references
- `M0AnimationClipTransition` — serializable wrapper for `AnimationClip` + `fadeDuration`
- `GameplayLifetimeScope` — already registers all components and wires them via `SetAnimationPresentationAdapter`
- `M0GameplayTickHandler` — already routes `OnCombatSnapshotChanged`, `OnLocomotionSnapshotChanged`, `OnEnemyIntentSnapshotChanged` to the adapter

The gap is purely scene-level: neither the Player nor Enemy GameObject has Animator, AnimancerComponent, or animation driver components attached.

## Goals / Non-Goals

**Goals:**
- Attach Animator + AnimancerComponent + animation driver components to Player and Enemy GameObjects
- Verify `M0AnimationPresentationAdapter` is on the tick handler GameObject
- Prove the observer pattern works: adapters observe snapshots, drivers play clips, no gameplay truth leaks into presentation
- Prove missing animation clips do not break gameplay (null clip tolerance)
- Create focused EditMode tests for the presentation-only boundary
- Create PlayMode evidence of clean runtime startup and combat loop continuity

**Non-Goals:**
- Do not author or polish final animation clips
- Do not require clips for M0 pass
- Do not change CombatCore timing, CounterWindow, MemoryState, Locomotion, EnemyIntent, TargetContext, Camera, or Encounter lifecycle
- Do not add root motion authority
- Do not let Animator/Animancer own gameplay truth
- Do not use Animator parameters as source of truth

## Decisions

1. **Use Animancer (not raw AnimatorController)**: Already chosen by existing code. Animancer provides programmatic clip playback without requiring Mecanim state machines. This keeps the adapter simple — just call `animancer.Play(clip)`.

2. **Null clip tolerance**: `AnimancerPlayerAnimationDriver.Play()` and `AnimancerEnemyAnimationDriver.Play()` already check `transition.IsAssigned` and log an error without crashing. No animation clips are required for M0 pass.

3. **Root motion disabled by default**: Both drivers set `animancer.Animator.applyRootMotion = false` in `Awake()` and before every `Play()`. Locomotion owns movement truth.

4. **State deduplication**: `M0AnimationPresentationAdapter` tracks `_lastCombatState`, `_lastLocomotionState`, `_lastEnemyIntentState` and skips duplicate calls. This avoids redundant clip restarts.

5. **Locomotion gated by combat state**: `ObserveLocomotionSnapshot` returns early if combat is not Neutral/Disabled. This prevents locomotion animations from interrupting combat animations.

6. **Scene wiring via Unity Editor**: Components are added directly to GameObjects in the scene using Unity MCP tools. No code changes needed.

## Risks / Trade-offs

- **Risk**: Animancer package may not be installed. **Mitigation**: Verify Animancer is in Packages before wiring.
- **Risk**: Adding Animator component could interfere with existing transform hierarchy. **Mitigation**: Animator is added as a leaf component; root motion is disabled.
- **Trade-off**: Using Animancer instead of raw Mecanim adds a package dependency, but the existing code already depends on it and Animancer provides cleaner programmatic control for M0.
