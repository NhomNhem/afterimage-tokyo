## Why

`Glass Refrain` now has a complete M0 design package and an approved M0 architecture, but it does not yet have the Unity-side technical foundation that those documents assume. A focused foundation change is needed now so implementation can begin on stable folder, assembly, scene, DI, input, and contract boundaries instead of improvising them during gameplay work.

## What Changes

- Establish the authored Unity project structure for M0 under `Assets/_Project`.
- Define and scaffold the minimal M0 assembly-definition boundaries and dependency direction.
- Establish the additive scene architecture for the M0 duel prototype:
  - `Bootstrap`
  - `Systems`
  - `Gameplay_CombatPrototype`
  - `Camera_CombatPrototype`
  - `UI_DebugOverlay`
  - `Level_TokyoStreet_Blockout`
- Establish `VContainer` root and scene-scope composition boundaries.
- Establish the Unity New Input System foundation for M0 input actions and generated input code flow.
- Create the initial core contract / DTO layer used by gameplay, targeting, camera, encounter, memory, and debug systems.
- Establish the shared read-only debug snapshot and debug-event approach for M0.
- Add the initial test structure and architecture-boundary verification path for M0 foundation work.
- Add architecture guardrails that prevent gameplay truth from drifting into `Animator`, camera, UI, or VFX layers.

## Capabilities

### New Capabilities
- `unity-project-foundation`: Establishes the Unity-side technical foundation for the M0 prototype, including folder structure, minimal asmdefs, additive scenes, DI scopes, input foundation, shared contracts, debug snapshot shape, and architecture guardrails.

### Modified Capabilities

None.

## Impact

- Affected code and content roots under `Assets/_Project`
- Assembly-definition structure and compile boundaries
- Additive scene composition and scene ownership
- `VContainer` composition plan
- Unity New Input System asset/setup path
- Shared contract/DTO layer for gameplay systems
- Debug snapshot/event structure used by `Debug Overlay`
- Initial test layout and architecture-boundary tests
- Foundation for later implementation of:
  - `Combat Core`
  - `Player Locomotion`
  - `Enemy Intent & Telegraph`
  - `Lock-On / Target Context`
  - `Lock-On & Combat Camera`
  - `Health / Damage / Hit Reaction`
  - `Memory State`
  - `Memory VFX Response`
  - `Encounter Framework`
  - `Debug Overlay`
