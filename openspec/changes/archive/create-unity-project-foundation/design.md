## Context

`Glass Refrain` has completed the M0 GDD package and an approved M0 architecture document. The next implementation step is not combat behavior itself, but the Unity project foundation that enforces the architecture at the folder, assembly, scene, dependency injection, input, contract, and debug-boundary level.

The project is pinned to Unity 6000.3.x + URP and explicitly chooses:

- Unity New Input System only
- `Cinemachine`
- `VContainer`
- `R3`
- `ObservableCollections`
- `ZLinq`
- `DOTween`
- Shader Graph
- Pure C# FSMs for gameplay truth

The architecture already defines the most important ownership seams:

- `Combat Core` owns combat validation/results
- `Player Locomotion` owns movement truth
- `Input Mapping` owns raw input truth
- `Lock-On / Target Context` owns target truth
- `Lock-On & Combat Camera` owns framing/readability only
- `Debug Overlay` is read-only

This change must create the technical scaffolding for those seams without prematurely implementing combat behavior, AI behavior, camera polish, final animation pipelines, or long-term RPG systems.

## Goals / Non-Goals

**Goals:**

- Create the Unity project structure under `Assets/_Project` that matches the approved architecture.
- Create the minimal assembly-definition layout and dependency direction for M0.
- Represent the additive M0 scene architecture and scene ownership boundaries.
- Represent `VContainer` root and scene-scope composition structure.
- Represent the Unity New Input System foundation and action-map setup path.
- Define the initial core contract/DTO layer for cross-system communication.
- Represent the shared read-only debug snapshot/event shape.
- Create initial test structure and architecture-boundary verification entry points.
- Enforce guardrails that keep gameplay truth out of `Animator`, camera, VFX, and UI.

**Non-Goals:**

- Implement combat attacks, parry timing, dodge resolution, or enemy AI behavior
- Implement final camera behavior
- Implement memory VFX polish
- Implement final HUD or presentation systems
- Implement save/persistence or progression systems
- Implement boss/multi-enemy frameworks
- Build a giant generic RPG or ability framework

## Decisions

### 1. Use `Assets/_Project` as the single authored root

**Decision:** All authored game code, content, data, tests, and prototype scene content will live under `Assets/_Project`, while third-party content remains under `Assets/ThirdParty`.

**Why:** This matches the project technical preferences and makes architecture boundaries inspectable from day one.

**Alternatives considered:**

- Scatter authored code across top-level Unity defaults
  - rejected because it weakens ownership clarity
- Build by feature only with no layer roots
  - rejected because the M0 architecture needs explicit cross-system boundaries early

### 2. Start with a minimal but real asmdef split

**Decision:** Create a small set of M0 assemblies rather than one monolithic runtime assembly or a fully exploded long-term graph.

Target M0 set:

- `GlassRefrain.Core`
- `GlassRefrain.Infrastructure`
- `GlassRefrain.Bootstrap`
- `GlassRefrain.Input`
- `GlassRefrain.Locomotion`
- `GlassRefrain.Combat`
- `GlassRefrain.Enemy`
- `GlassRefrain.Targeting`
- `GlassRefrain.Camera`
- `GlassRefrain.Health`
- `GlassRefrain.Memory`
- `GlassRefrain.Encounter`
- `GlassRefrain.VFX`
- `GlassRefrain.UI`
- `GlassRefrain.Tests.EditMode`
- `GlassRefrain.Tests.PlayMode`

**Why:** One big runtime assembly would make ownership drift too easy. A highly granular full-production split would be premature.

**Alternatives considered:**

- One runtime asmdef for all M0 code
  - rejected because it invites forbidden dependencies
- Large future-proof assembly graph now
  - rejected because it overbuilds before M0 feel is proven

### 3. Use additive scene composition from day one

**Decision:** Represent M0 with these additive scene roles:

- `Bootstrap`
- `Systems`
- `Gameplay_CombatPrototype`
- `Camera_CombatPrototype`
- `UI_DebugOverlay`
- `Level_TokyoStreet_Blockout`

**Why:** The approved architecture and technical preferences already assume scene-role separation. Representing this early prevents level, camera, and gameplay truth from collapsing together.

**Alternatives considered:**

- Single all-in-one prototype scene
  - rejected because it undermines later composition and ownership clarity

### 4. Keep gameplay truth in Pure C# services/FSMs with Unity adapters

**Decision:** Domain truth will be represented by Pure C# state models and services, while `MonoBehaviour` components act as adapters, presenters, or composition hosts.

**Why:** This preserves testability and keeps `Animator` and scene objects from becoming hidden authorities.

**Alternatives considered:**

- `MonoBehaviour`-driven gameplay truth everywhere
  - rejected because it weakens testability and contract clarity

### 5. Split combat lock/recovery ownership between request and expression

**Decision:** `Combat Core` will own combat-side lock/recovery requests, while `Player Locomotion` will own movement-side restriction and recovery expression.

**Why:** This resolves the main architecture concern from the gate review without giving both systems overlapping truth ownership.

**Alternatives considered:**

- `Combat Core` owns all recovery truth
  - rejected because locomotion must still own movement truth
- `Player Locomotion` derives all recovery independently
  - rejected because combat commitment would lose explicit authority

### 6. Represent camera-relative movement as a read-only basis contract

**Decision:** `Lock-On & Combat Camera` may expose a `CameraMovementBasisSnapshot`, but `Player Locomotion` interprets it.

**Why:** This preserves the camera/locomotion boundary while still allowing camera-relative movement assumptions for M0.

**Alternatives considered:**

- camera directly computes final movement direction
  - rejected because that would let camera own locomotion behavior

### 7. Use Unity New Input System only

**Decision:** The foundation change will establish Unity New Input System assets and generated input-code expectations only. No legacy Input Manager path will be introduced.

**Why:** Unity 6 deprecates the legacy path, the GDD explicitly rejects it, and the architecture depends on explicit raw input intent contracts.

**Alternatives considered:**

- support `Both` or legacy input for convenience
  - rejected because it muddies ownership and introduces deprecated paths

### 8. Use read-only per-system debug snapshots plus optional debug events

**Decision:** Each authoritative system owns a debug snapshot DTO. `Debug Overlay` consumes snapshots and optional transition/rejection events, but never becomes a hidden event bus for gameplay truth.

**Why:** This satisfies the design package without creating a noisy god-debug system.

**Alternatives considered:**

- one giant mutable debug model
  - rejected because it would blur ownership
- no shared snapshot shape until later
  - rejected because the gate concern explicitly asked to tighten this now

## Risks / Trade-offs

- **Too many asmdefs too early** → Keep the split minimal and tied to real ownership seams only
- **One-runtime-assembly convenience pressure** → Enforce forbidden dependencies from the beginning
- **Camera or animator drift back into gameplay authority** → Keep adapters and contracts explicit; do not allow presentation code in domain assemblies
- **Input system overbuild** → Limit this change to action maps, routing, and contracts only
- **Debug DTO sprawl** → Start with per-system snapshots and only add fields required by M0 GDDs
- **Foundation work turns into gameplay implementation** → Keep tasks focused on folders, scenes, scopes, contracts, and test scaffolding only

## Migration Plan

1. Establish folders and asset roots under `Assets/_Project`
2. Create minimal asmdefs and compile boundaries
3. Represent additive scenes and their ownership roles
4. Establish root and scene-scope `VContainer` composition shells
5. Create Unity New Input System assets and generated-code path
6. Add shared core contracts / DTOs
7. Add debug snapshot/event contracts
8. Add test assembly scaffolding and first architecture smoke checks

Rollback strategy:

- because this is a foundation-first change, rollback means reverting the created folder, scene, assembly, and contract scaffolding before gameplay code depends on it

## Open Questions

- Should first playable M0 ship keyboard/mouse only or include gamepad immediately?
- Should `Counter` be a separate input action in the first implementation pass or remain contextual?
- Which contracts belong in `GlassRefrain.Core` versus a thin infrastructure-facing shared layer if some DTOs later require Unity types?
- Should the first additive scene composition include separate prototype-only composition scenes, or only the minimal M0 combat set?
