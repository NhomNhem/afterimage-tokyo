# Technical Preferences

<!-- Updated by /setup-engine. All agents reference this file for project-specific standards and conventions. -->

## Engine & Language

- **Engine**: Unity 6000.3.x
- **Language**: C#
- **Rendering**: URP
- **Physics**: Unity PhysX (default 3D physics)

## Input & Platform

- **Target Platforms**: PC
- **Input Methods**: Keyboard/Mouse, Gamepad
- **Primary Input**: Gamepad
- **Gamepad Support**: Full
- **Touch Support**: None
- **Platform Notes**: Combat readability, lock-on behavior, and dodge/parry timing must be strong on both gamepad and keyboard/mouse. No critical hover-only interactions.

## Naming Conventions

- **Classes**: PascalCase
- **Variables**: Public PascalCase, private `_camelCase`
- **Signals/Events**: PascalCase for C# events, descriptive past-tense or state-change names
- **Files**: PascalCase matching class or primary type
- **Scenes/Prefabs**: PascalCase with role prefix where useful, e.g. `Gameplay_CombatPrototype`, `UI_DebugOverlay`
- **Constants**: PascalCase or `UPPER_SNAKE_CASE` when clearly constant-like

## Project Structure

- All authored Glass Refrain work lives under `Assets/_Project`.
- Third-party imports live under `Assets/ThirdParty` and are read-only unless explicitly approved.
- Authored art and audio live under `Assets/_Project/Content`, not top-level `Assets/Art` or `Assets/Audio`.

### Preferred Unity Roots

- `Assets/_Project`
- `Assets/ThirdParty/AssetStore`
- `Assets/ThirdParty/Plugins`
- `Assets/Settings`

### `_Project` Layout

- `Code/Core`
- `Code/Infrastructure`
- `Code/Bootstrap`
- `Code/Gameplay`
- `Code/Combat`
- `Code/AI`
- `Code/Camera`
- `Code/Memory`
- `Code/District`
- `Code/Interaction`
- `Code/VFX`
- `Code/UI`
- `Code/Editor`
- `Content/Scenes`
- `Content/Prefabs`
- `Content/Data`
- `Content/Animation`
- `Content/Materials`
- `Content/VFX`
- `Content/Audio`
- `Content/UI`
- `Content/Art`
- `Prototypes`
- `Tests`

## Scene Architecture

Glass Refrain uses additive scene loading from day one.

### Scene Roles

- `Bootstrap`: startup only; initializes flow and loads additive scene sets
- `Systems`: persistent cross-scene systems only
- `Gameplay`: player, enemy, encounter roots, and gameplay-scoped LifetimeScopes
- `Camera`: Cinemachine cameras and camera coordinators
- `UI`: HUD, UI Toolkit roots, and debug overlays
- `Levels`: environment, colliders, authored placements, lighting, and set dressing

### Recommended Scene Folders

- `Assets/_Project/Content/Scenes/Bootstrap/Bootstrap.unity`
- `Assets/_Project/Content/Scenes/Systems/Systems_Persistent.unity`
- `Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`
- `Assets/_Project/Content/Scenes/Camera/Camera_CombatPrototype.unity`
- `Assets/_Project/Content/Scenes/UI/UI_CombatHUD.unity`
- `Assets/_Project/Content/Scenes/UI/UI_DebugOverlay.unity`
- `Assets/_Project/Content/Scenes/Levels/TokyoAct1/Level_TokyoStreet_Blockout.unity`
- `Assets/_Project/Content/Scenes/Levels/TokyoAct1/Level_TokyoStreet_Lighting.unity`
- `Assets/_Project/Content/Scenes/Levels/TokyoAct1/Level_TokyoStreet_SetDress.unity`
- `Assets/_Project/Content/Scenes/Prototypes/M0_KatanaCombat/M0_Composition.unity`
- `Assets/_Project/Content/Scenes/Prototypes/M0_KatanaCombat/Sandbox_Camera.unity`
- `Assets/_Project/Content/Scenes/Prototypes/M0_KatanaCombat/Sandbox_CombatTiming.unity`
- `Assets/_Project/Content/Scenes/Prototypes/M0_KatanaCombat/Sandbox_VFX_MemoryState.unity`

### M0 Minimal Additive Scene Set

- `Bootstrap.unity`
- `Systems_Persistent.unity`
- `Level_TokyoStreet_Blockout.unity`
- `Gameplay_CombatPrototype.unity`
- `Camera_CombatPrototype.unity`
- `UI_DebugOverlay.unity`

### Scene Ownership Rules

- Bootstrap should only initialize and load scene sets.
- Persistent systems stay separated from gameplay content.
- Level scenes contain environment, colliders, placement, and authored map content.
- Gameplay scenes contain player, enemy, encounter roots, and gameplay LifetimeScopes.
- Camera scenes contain Cinemachine cameras and camera coordinators.
- UI scenes contain HUD, UI Toolkit roots, and debug overlays.
- Avoid a god `SceneManager` scene.
- Level scenes must not own gameplay rules.
- Presentation scenes may observe gameplay state, but must not own gameplay truth.

## Assembly Definition Architecture

Do not create asmdefs speculatively. Start small, then split only when compile boundaries and ownership are proven useful.

### M0 Minimal Asmdef Folder Map

- `Assets/_Project/Code/Core/GlassRefrain.Core.asmdef`
- `Assets/_Project/Code/Infrastructure/GlassRefrain.Infrastructure.asmdef`
- `Assets/_Project/Code/Bootstrap/GlassRefrain.Bootstrap.asmdef`
- `Assets/_Project/Code/Combat/GlassRefrain.Combat.asmdef`
- `Assets/_Project/Code/Memory/GlassRefrain.Memory.asmdef`
- `Assets/_Project/Code/Camera/GlassRefrain.Camera.asmdef`
- `Assets/_Project/Code/UI/GlassRefrain.UI.asmdef`
- `Assets/_Project/Code/VFX/GlassRefrain.VFX.asmdef`
- `Assets/_Project/Tests/GlassRefrain.Tests.asmdef`

### M0 Minimal Asmdef Roles

#### `GlassRefrain.Core`

- shared primitives, IDs, result types, math helpers, and interfaces that are safe for all layers
- should avoid `UnityEngine` dependencies unless absolutely necessary
- must not reference `VContainer`, `R3`, `Cinemachine`, `DOTween`, UI Toolkit, or gameplay implementation assemblies

#### `GlassRefrain.Infrastructure`

- scene loading, logging, config, save paths, and adapters to engine/package services
- references: `GlassRefrain.Core`
- may reference: `VContainer`, `UnityEngine`, and `Addressables` later if needed
- must not own combat truth

#### `GlassRefrain.Bootstrap`

- `ProjectRootLifetimeScope`, bootstrap entry, and startup scene loading
- references: `GlassRefrain.Core`, `GlassRefrain.Infrastructure`
- may reference: `VContainer`
- must remain thin

#### `GlassRefrain.Combat`

- player combat FSM, attack flow, parry/dodge/counter logic, hit resolution contracts, and lock-on logic
- references: `GlassRefrain.Core`
- may reference: `R3` only for observation and debug-facing streams if needed
- should avoid referencing `VContainer` directly except composition-specific files if unavoidable
- must not reference `UI`, `Camera`, `VFX`, or `Bootstrap`
- combat truth must remain explicit and frame-readable

#### `GlassRefrain.Memory`

- memory states, memory fragments, distortion state rules, and truth restoration logic
- references: `GlassRefrain.Core`
- may reference: `R3` for state observation
- must not reference `VFX`, `Camera`, `UI`, or `Bootstrap`

#### `GlassRefrain.Camera`

- camera state coordination, Cinemachine adapters, and camera presentation logic
- references: `GlassRefrain.Core`
- should prefer interfaces and contracts from `Core` or presentation-safe read models
- direct references to `Combat` or `Memory` require manual review
- may reference: `Cinemachine`, `UnityEngine`
- must not own combat truth or memory truth

#### `GlassRefrain.UI`

- UI Toolkit presenters, HUD/debug overlays, and state presentation
- references: `GlassRefrain.Core`
- should prefer read-only interfaces, event streams, or presentation DTOs
- direct dependency on domain implementation assemblies requires manual review
- may reference: `R3`, UI Toolkit
- must not own gameplay truth

#### `GlassRefrain.VFX`

- memory-state visual presenters, shader parameter adapters, and VFX triggers
- references: `GlassRefrain.Core`
- should prefer read-only memory-state interfaces or presentation adapters
- direct dependency on `Memory` implementation assemblies requires manual review
- may reference: `UnityEngine`, URP-related APIs, `DOTween` for presentation only
- must not own gameplay truth

#### `GlassRefrain.Tests`

- M0 EditMode and PlayMode test entry
- references: `Core`, `Combat`, `Memory`, `Camera` as needed
- may reference: Unity Test Framework

### Long-Term Candidate Asmdefs

- `GlassRefrain.Core`
- `GlassRefrain.Infrastructure`
- `GlassRefrain.Bootstrap`
- `GlassRefrain.Gameplay`
- `GlassRefrain.Combat`
- `GlassRefrain.AI`
- `GlassRefrain.Camera`
- `GlassRefrain.Memory`
- `GlassRefrain.District`
- `GlassRefrain.Interaction`
- `GlassRefrain.VFX`
- `GlassRefrain.UI`
- `GlassRefrain.Editor`
- `GlassRefrain.Tests.EditMode`
- `GlassRefrain.Tests.PlayMode`

### Dependency Graph

Preferred high-level shape:

`Core`
↑
`Combat / Memory / District / Interaction / AI / Gameplay`
↑
`Camera / UI / VFX` presentation adapters
↑
`Bootstrap / scene composition` where needed

Prefer interfaces and read models over direct coupling. Presentation assemblies may observe gameplay state, but must not own gameplay truth.

### Forbidden Dependencies

- `Core -> anything`
- `Combat -> Camera`
- `Combat -> UI`
- `Combat -> VFX`
- `Combat -> Bootstrap`
- `Memory -> VFX`
- `Memory -> UI`
- `Memory -> Camera`
- `Gameplay/domain -> Bootstrap`
- `Any domain assembly -> Editor`
- `Runtime assemblies -> Tests`

### Package Reference Policy

- `VContainer` should live mostly in Bootstrap, Infrastructure, and composition assemblies
- `R3` is allowed for observation, not hot combat truth
- `Cinemachine` should be isolated to the Camera assembly
- `DOTween` should be isolated to UI, VFX, and camera polish, not Combat
- Shader Graph and HLSL are content assets, not asmdef dependencies
- Official `VContainer.SourceGenerator` is an optional later optimization
- `NhemDangFugBixs.VContainer.SourceGenerator` is the planned architecture guardrail, but generated DI remains for pure C# services

### Composition Rule

If a domain service needs DI attributes from `NhemDangFugBixs` tooling, verify whether that creates an asmdef or package dependency. If yes, keep the dependency lightweight and limited to runtime attributes only. Do not allow domain assemblies to reference composition assemblies.

### When To Split More Assemblies Later

- when compile times or editor reload times materially improve
- when ownership boundaries are stable
- when a subsystem has a meaningfully different dependency surface
- when tests benefit from narrower references

### When Not To Create An Asmdef Yet

- when a subsystem is still in heavy prototype churn
- when the split only mirrors folders aesthetically
- when the result would force awkward circular references
- when the combat loop is not yet proven

### Manual Review Before Implementation

Validate package references, source-generator attribute requirements, and whether any domain-layer attribute usage would accidentally pull composition concerns inward.

## Dependency Injection Architecture

Glass Refrain uses VContainer as the runtime DI container.

### Root Scope

Glass Refrain uses a `ProjectRootLifetimeScope` configured through `VContainerSettings`.

- `ProjectRootLifetimeScope` is a prefab assigned in `VContainerSettings`
- it is the parent of all scene LifetimeScopes
- `Bootstrap.unity` starts the game and loads additive scene sets

### Scope Ownership

- root scope owns application lifetime only
- scene scopes own gameplay lifetime
- combat truth must never be registered globally

### Project Root Allowed Services

- logger
- scene flow/loading service
- game settings/config service
- save path/config service
- build info service
- global audio root if needed

### Project Root Forbidden Services

- player combat services
- lock-on service
- enemy intent service
- encounter state
- boss state
- current district memory state
- HUD state
- camera state for a specific scene

### Scene Scope Mapping

- `ProjectRootLifetimeScope` -> `IProjectScope`
- `SystemsLifetimeScope` -> long-lived cross-scene systems if needed
- `GameplayLifetimeScope` -> `IGameplayScope`
- `CombatLifetimeScope` -> `ICombatScope`
- `MemoryLifetimeScope` / `DistrictLifetimeScope` -> `IMemoryScope` / `IDistrictScope`
- `CameraLifetimeScope` -> `ICameraScope`
- `UILifetimeScope` -> `IUIScope`

### Composition Rule

Generated DI is for pure C# services. Unity scene objects remain explicitly composed in their scene LifetimeScopes. Do not use `IObjectResolver` as a service locator.

## VContainer Source Generation Policy

### Official VContainer Source Generator

This is the source generator provided by VContainer itself.

- purpose: injection and resolve acceleration
- integration form: `VContainer.SourceGenerator.dll` placed under `Assets/` and marked as `RoslynAnalyzer`
- usage timing: only after DI architecture is stable and profiling or iteration justify it
- not a substitute for explicit registration architecture

### `NhemDangFugBixs.VContainer.SourceGenerator`

This is planned project or team-authored DI architecture tooling.

- purpose: compile-time DI workflow, marker-based scope registration, generated installers, analyzer guardrails, duplicate and invalid registration checks, and future `di-smoke` validation
- status: planned architecture safety layer for Glass Refrain
- generated DI remains limited to pure C# services
- Unity scene objects remain explicitly composed

### Glass Refrain M0 Decision

- use `VContainer` as the runtime DI container
- create a minimal manual `LifetimeScope` baseline first
- configure `ProjectRootLifetimeScope` through `VContainerSettings`
- add `NhemDangFugBixs.VContainer.SourceGenerator` in a separate OpenSpec change
- consider official VContainer source generation only later as optional optimization

### Rules

- do not confuse generated registration with VContainer injection acceleration
- do not use official VContainer source generation as a substitute for registration architecture
- do not use `NhemDangFugBixs` tooling as a reason to auto-register MonoBehaviours
- generated DI is for pure C# services only
- Unity scene objects remain explicitly composed

## Performance Budgets

- **Target Framerate**: 60 fps
- **Frame Budget**: 16.6 ms
- **Draw Calls**: Set during prototype profiling; do not optimize speculatively
- **Memory Ceiling**: Set when target hardware budget is locked

## Testing

- **Framework**: Unity Test Framework
- **Minimum Coverage**: Focus on combat state transitions, memory-state rules, and scene-composition smoke tests first
- **Required Tests**: Combat timing windows, lock-on stability, memory-state rule changes, PlayMode smoke path for M0

## Combat Coding Standards

- combat execution must be explicit and frame-readable
- use pure C# FSMs for combat and intent logic
- separate intent, commitment, active frames, and recovery in code and data
- animation events notify timing windows; they do not own combat truth
- use R3 for visibility and observation, not hot combat truth
- presentation systems may observe gameplay state, but must not own gameplay truth

## Package Usage Guidelines

- `Input System`: hot-path reads should stay local and cached; do not route every combat input through inspector events
- `Cinemachine`: use authored camera states and blends, not a giant custom camera monolith
- `VContainer`: keep most usage in root, infrastructure, and scene composition
- `R3`: state visibility, UI binding, and debug overlays
- `DOTween`: UI, camera polish, reveal beats, subtle environmental motion, and memory presentation
- `Awaitable`: first choice for simple Unity async flows
- `UniTask`: only when cancellation or orchestration complexity justifies it
- `Shader Graph`: default for artist-facing visual effects
- `Custom HLSL`: only when Shader Graph is insufficient, unreadable, or performance-sensitive
- `URP Renderer Features`: only for limited screen-space memory effects that preserve combat readability
- avoid DOTS/ECS in M0
- avoid large generic RPG frameworks

## Allowed Libraries / Addons

- `VContainer` — approved runtime DI container
- `NhemDangFugBixs.VContainer.SourceGenerator` — planned compile-time DI architecture guardrail
- `R3` — approved for state observation and presentation binding
- `ObservableCollections` — approved for UI/debug-facing collections
- `ZLinq` — approved only where profiling justifies it
- `DOTween` — approved for presentation and polish only

## Forbidden Patterns

- registering combat truth in the project root scope
- using `IObjectResolver` as a service locator
- auto-registering MonoBehaviours, ScriptableObjects, hitboxes, animation event receivers, camera components, or VFX presenters via generated DI
- using DOTween for authoritative combat motion, locomotion, or gameplay-affecting position
- using presentation scenes or assemblies to own gameplay truth

## Architecture Decisions Log

- Unity 6000.3.x + URP locked for engine setup phase
- additive scene loading from day one
- `Bootstrap` / `Systems` / `Gameplay` / `Camera` / `UI` / `Level` scene separation
- M0 minimal additive scene set approved
- `ProjectRootLifetimeScope` via `VContainerSettings`
- root scope owns app lifetime only
- scene scopes own gameplay lifetime
- official VContainer source generator is an optional later optimization
- `NhemDangFugBixs.VContainer.SourceGenerator` is the planned DI architecture guardrail

## Engine Specialists

- **Primary**: unity-specialist
- **Language/Code Specialist**: unity-specialist
- **Shader Specialist**: unity-shader-specialist
- **UI Specialist**: unity-ui-specialist
- **Additional Specialists**: unity-addressables-specialist, unity-dots-specialist
- **Routing Notes**: Use `unity-specialist` for architecture and general gameplay code. Use `unity-shader-specialist` for Shader Graph, HLSL, and URP material or renderer-feature work. Use `unity-ui-specialist` for UI Toolkit runtime UI. Use `unity-addressables-specialist` only when asset streaming and catalogs are actively being integrated. DOTS specialist is not part of M0.

### File Extension Routing

| File Extension / Type | Specialist to Spawn |
|-----------------------|---------------------|
| Game code (.cs) | unity-specialist |
| Shader / material files (.shader, .shadergraph, .mat) | unity-shader-specialist |
| UI / screen files (.uxml, .uss, UI prefabs) | unity-ui-specialist |
| Scene / prefab / level files (.unity, .prefab) | unity-specialist |
| Native extension / plugin files | unity-specialist |
| General architecture review | unity-specialist |
