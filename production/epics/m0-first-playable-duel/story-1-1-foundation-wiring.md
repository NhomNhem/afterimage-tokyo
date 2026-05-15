# Story 1-1: [Foundation] Scene & VContainer Wiring

> **Epic**: M0 First Playable Duel
> **Status**: Complete
> **Layer**: Foundation
> **Type**: Integration
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/systems-index.md`
**Requirement**: `TR-M0-FOUNDATION-001`, `TR-M0-FOUNDATION-002`, `TR-M0-DI-001`

**ADR Governing Implementation**: [ADR-0001: M0 Runtime Foundation and Scene Composition]
**ADR Decision Summary**: Establishes additive scene loading for 6 core scenes and manual VContainer scope separation.

**Engine**: Unity 6000.3.x | **Risk**: LOW
**Engine Notes**: All ADRs have Engine Compatibility sections stamped.

**Control Manifest Rules (this layer)**:
- Required: Additive Scene Composition (Bootstrap -> Systems -> Level -> Gameplay -> Camera -> UI).
- Required: Manual VContainer Registration (no automatic scanning).
- Forbidden: Never use Generated DI for M0.

---

## Acceptance Criteria

- [x] Bootstrap scene loads all 6 required scenes in the correct order.
- [x] `ProjectRootLifetimeScope` resolves global services (SceneLoader).
- [x] `GameplayScope` resolves Core gameplay systems from skeletons.
- [x] No circular dependencies exist in the manual registration.

---

## Implementation Notes

- Use `VContainer.Unity.LifetimeScope` for manual registrations.
- `Bootstrap` scene MUST be the entry point.
- Wiring MUST follow the additive order defined in ADR-0001.

---

## Out of Scope

- [Story 1-2]: Camera-Relative Movement wiring.

---

## QA Test Cases

**AC-1: Scene Loading order**
- **Test**: Hierarchy contains all 6 scenes after Bootstrap load.
  - Given: Bootstrap scene is loaded and play is pressed.
  - When: SceneLoader completes its task.
  - Then: Scenes are present in order: Bootstrap, Systems, Level, Gameplay, Camera, UI.

**AC-2: VContainer Resolution**
- **Test**: Core systems are resolvable in GameplayScope.
  - Given: VContainer is initialized.
  - When: Resolving `ICombatCore` or `ILocomotion`.
  - Then: The skeleton implementation is returned without error.

---

## Test Evidence

**Story Type**: Integration
**Required evidence**:
- Integration: `Assets/_Project/Tests/EditMode/SceneComposition_test.cs` — must exist and pass
- Manual verification: Hierarchy screenshot showing all scenes and VContainer diagnostics.

**Status**: [x] Complete

---

## Dependencies

- Depends on: None
- Unlocks: Story 1-2, Story 1-3, Story 1-4

## Completion Notes
**Completed**: 2026-05-15
**Criteria**: 4/4 passing
**Deviations**: None
**Test Evidence**: Integration tests at `Assets/_Project/Tests/EditMode/SceneComposition_test.cs` and `VContainerRegistry_test.cs`. Manual Unity Editor verification confirmed.
**Code Review**: Skipped (Lean mode verification only)
**OpenSpec Change**: `wire-m0-foundation-and-vcontainer`
