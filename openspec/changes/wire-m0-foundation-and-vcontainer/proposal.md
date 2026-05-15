## Why

This change implements Story 1-1 [Foundation] Scene & VContainer Wiring for the M0 First Playable Duel. It establishes the authoritative runtime foundation, additive scene composition, and dependency injection boundaries required to wire the technical skeletons into a playable duel loop. Without this foundation, systems cannot communicate or resolve dependencies according to the project's architectural standards.

## What Changes

- **Bootstrap Flow**: Implements the initial entry point in the `Bootstrap` scene to orchestrate the loading of the full M0 scene set.
- **Additive Scene Composition**: Configures the loading of 6 core scenes in a strict sequence: Bootstrap → Systems → Level → Gameplay → Camera → UI.
- **VContainer Scope Wiring**:
    - `ProjectRootLifetimeScope`: Configured to resolve global/application-level services only (e.g., scene management or configuration services if present).
    - `GameplayScope`: Configured to resolve M0 core gameplay skeleton services (Combat, Locomotion, Targeting, etc.).
- **Manual Registration**: Enforces manual VContainer registrations in composition roots, strictly avoiding automatic scanning or generated DI for M0.
- **Integration Testing**: Adds EditMode tests in `Assets/_Project/Tests/EditMode` to verify hierarchy composition and scope resolution.

## Capabilities

### New Capabilities
- `m0-runtime-foundation`: Defines the additive scene composition order, scene responsibility boundaries, and VContainer lifetime scope mappings for the M0 prototype.

### Modified Capabilities
None.

## Impact

- **Affected Code**: `Assets/_Project/Code/Bootstrap`, `Assets/_Project/Code/Infrastructure`, `Assets/_Project/Code/Core`.
- **Affected Scenes**: `Assets/_Project/Content/Scenes/Bootstrap`, `Systems`, `Gameplay_CombatPrototype`, `Camera_CombatPrototype`, `UI_DebugOverlay`, `Level_TokyoStreet_Blockout`.
- **Tests**: New EditMode tests in `Assets/_Project/Tests/EditMode/SceneComposition_test.cs`.
- **Architecture**: Enforces ADR-0001 and ADR-0004 boundaries.
