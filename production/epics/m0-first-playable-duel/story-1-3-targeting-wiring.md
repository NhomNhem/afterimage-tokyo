# Story 1-3: [Targeting] Lock-On Wiring

> **Epic**: M0 First Playable Duel
> **Status**: Implemented - Needs Verification
> **Layer**: Core
> **Type**: Logic/Integration
> **Estimate**: 0.5d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-19

## Context

**GDD**: `design/gdd/lock-on-target-context.md`
**Requirement**: `TR-M0-TARGET-001`

**Supporting GDD References**:
- `design/gdd/input-mapping.md` — Input emits `LockOn` intent only
- `design/gdd/lock-on-combat-camera.md` — Camera may read target truth but must not own it
- `design/gdd/player-locomotion.md` — Locomotion may read target direction later; this story does not modify locomotion behavior

**ADR Governing Implementation**:
- [ADR-0002: M0 Gameplay Truth Ownership Boundaries] — Target Context owns target truth and resolves acquire/release requests
- [ADR-0003: M0 Presentation and Debug Read-Only Boundaries] — Camera/debug are read-only; they do not own target truth
- [ADR-0004: M0 DI and Assembly Boundary Strategy] — Manual VContainer registration only; no generated DI
- [ADR-0005: M0 Shared Contracts Strategy] — M0Contracts.cs changes must remain contracts-only

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Ownership Separation (Target Context owns focus truth).
- Forbidden: Camera does NOT drive targets.

---

## Acceptance Criteria

- [ ] **AC-1**: LockOn intent is raw input only
  - Given the New Input System `LockOn` action is triggered,
  - When input emits gameplay intent,
  - Then it emits only raw `LockOn` intent/request and does not select, store, validate, or clear targets.

- [ ] **AC-2**: Target Context acquires the single M0 enemy
  - Given one player and one registered targetable M0 enemy exist,
  - When `M0TargetContext` receives `LockOn` acquire intent with no active target,
  - Then `TargetContext.Active` becomes true and `CurrentTarget` is the registered M0 enemy.

- [ ] **AC-3**: Target Context releases active target
  - Given `M0TargetContext` has an active target,
  - When release intent is received,
  - Then active target truth is cleared, `Active` becomes false, and a release reason is exposed for debug/read-only consumers.

- [ ] **AC-4**: Target invalidation clears focus
  - Given the M0 enemy is the active target,
  - When the enemy is unregistered, disabled, defeated, or no longer targetable for the current duel,
  - Then `M0TargetContext` invalidates and clears focus with an invalidation reason.

- [ ] **AC-5**: Target direction/context is read-only
  - Given an active target exists,
  - When locomotion, camera, combat, or debug systems request target context,
  - Then they receive read-only target state/direction/snapshot data and cannot mutate target truth.

- [ ] **AC-6**: Scope exclusions are enforced
  - The implementation does not add:
    - multi-target cycling
    - boss-part targeting
    - aim assist
    - combat validity
    - attack/hit/parry/dodge/counter behavior
    - animation/root motion
    - locomotion rewrites
    - camera-owned targeting
    - generated DI
    - legacy Input Manager calls
    - Hardcoded gameplay input via `Keyboard.current`, `Mouse.current`, `Gamepad.current`, or direct device polling
    - Gameplay input not routed through project `InputActionAsset` / `M0InputActions` action maps
    - Input Mapping deciding target acquire/release or storing target truth
    - `FindObjectOfType`
    - `FindFirstObjectByType`
    - `GameObject.Find`
    - `Resources.Load`

---

## Implementation Notes

- Connect `M0InputRouter` Lock-On intent to `M0TargetContext`.
- Register the M0 Enemy as a targetable participant in the encounter.
- Ensure `TargetContext` is the single source of truth for the active target.

### Exact M0 Validity Rules

Target is valid when:
- Registered current duel enemy exists
- Enemy is targetable/active
- Enemy is still the current one-on-one duel target

Target invalidates and releases when:
- Enemy is unregistered
- Enemy is disabled
- Enemy is defeated
- Explicit release is requested
- Enemy is no longer targetable for the current duel

Explicitly excluded:
- No range scoring
- No visibility scoring
- No target priority scoring
- No combat validity checks
- No boss-part rules

### Toggle Behavior Definition

- `LockOn` input emits intent only.
- If no active target exists, Target Context interprets intent as acquire.
- If active target exists, Target Context interprets intent as release.
- Input Mapping must not decide acquire/release or store target truth.

---

## Out of Scope

- [Story 1-2]: Free movement camera basis.

Explicitly out of scope for this story:
- Multi-target cycling
- Boss-part targeting
- Aim assist
- Combat validity (attack/hit/parry/dodge/counter logic)
- Animation/root motion systems
- Locomotion behavior rewrites
- Camera ownership of target truth
- Generated DI / VContainer.SourceGenerator
- Legacy Unity Input Manager
- `FindObjectOfType` / `FindFirstObjectByType` / `GameObject.Find` / `Resources.Load`
- Hardcoded gameplay input via `Keyboard.current`, `Mouse.current`, `Gamepad.current`, or direct device polling
- Gameplay input not routed through project `InputActionAsset` / `M0InputActions` action maps
- Input Mapping deciding target acquire/release or storing target truth
- Range scoring, visibility scoring, or target priority frameworks

---

## QA Test Cases

**AC-1: Target Acquisition**
- **Test**: Lock-On intent selects the correct enemy.
  - Given: An enemy is registered in the arena.
  - When: Lock-On intent is emitted.
  - Then: TargetContext.Active is true and CurrentTarget matches the enemy.

**AC-2: Target Release**
- **Test**: Target is released on invalidation.
  - Given: Player is locked-on to an enemy.
  - When: The enemy is disabled or unregistered.
  - Then: TargetContext.Active becomes false.

---

## Test Evidence

**Story Type**: Logic/Integration
**Required evidence**:

### EditMode Logic Tests
- `Assets/_Project/Tests/EditMode/TestTargetContextOwnership.cs` — Target context acquire/release/invalidation
- `Assets/_Project/Tests/EditMode/TestLockOnIntentRouting.cs` — Input emits intent only; no legacy Input Manager
- `Assets/_Project/Tests/EditMode/TestManualTargetingDIRegistration.cs` — Manual VContainer registration

**Expected coverage**:
- [ ] Acquire succeeds with one registered valid enemy
- [ ] Release clears active target
- [ ] Invalidation clears active target (unregistered/disabled/defeated)
- [ ] No target exists results in inactive state with rejection reason
- [ ] Read-only snapshot cannot mutate target truth
- [ ] LockOn input emits raw intent only
- [ ] No legacy Input Manager / `Keyboard.current` hardcoded gameplay path
- [ ] `M0TargetContext` resolves from `GameplayScope` through manual VContainer

### Manual Verification
- Debug Overlay showing target focus state and direction
- Unity Editor play mode: one player, one enemy, toggle lock-on/release

**Status**: [ ] Not yet created

---

## Performance Note

No measurable performance impact expected. Story 1-3 supports one player, one enemy, and one active target max. Acquire/release and snapshot reads are O(1). No scanning, scoring, multi-target search, or priority framework is introduced.

---

## Dependencies

- Depends on: Story 1-1
- Unlocks: Story 1-4, Story 1-6

## Verification Update — 2026-05-19

**Validated Status**: IMPLEMENTED - NEEDS VERIFICATION

LockOn input route was observed with the actual binding Tab. Target acquisition and TargetContext state change have not yet been cleanly verified in PlayMode.
