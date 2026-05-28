## Context

The M0 technical skeletons for `Combat`, `Locomotion`, `Targeting`, `Health`, `Enemy`, and `Memory` exist as individual assemblies (`asmdef`) but are currently not integrated into a runtime loop. This design defines how to wire these systems using VContainer lifetime scopes and Unity's additive scene loading system to prove the M0 duel foundation.

## Goals / Non-Goals

**Goals:**
- **Synchronized Entry**: Ensure the `Bootstrap` scene is the single entry point for the application.
- **Additive Composition**: Load the 6 core M0 scenes in the sequence: Bootstrap → Systems → Level → Gameplay → Camera → UI.
- **Dependency Boundaries**: Enforce the separation between application-level services (`ProjectRootLifetimeScope`) and gameplay-level services (`GameplayScope`).
- **Manual Wiring**: Register all M0 technical skeletons manually to maintain complete visibility and avoid premature complexity from generated DI.
- **Validation**: Provide EditMode tests to verify the VContainer registry integrity and scene loading sequence.

**Non-Goals:**
- **No Gameplay Implementation**: This change does NOT implement FSM logic, movement, or combat resolution. It only wires the existing skeletons.
- **No Generated DI**: Nhem-generated DI or reflection-based scanning is explicitly forbidden for M0.
- **No HUD/UI Implementation**: Only the `UI_DebugOverlay` scene is loaded; no player-facing HUD is created.
- **No Persistence**: Save/Load and persistent state are deferred.

## Decisions

### 1. Manual VContainer Registration
- **Decision**: Register all M0 services manually in `ProjectRootLifetimeScope` and `GameplayLifetimeScope`.
- **Rationale**: ADR-0004 defers generated DI to keep the M0 footprint small and highly traceable. Manual registration ensures that every dependency is explicit and verifiable during the skeleton wiring phase.
- **Alternatives**: Reflection scanning (rejected for performance and "magic" behavior), Source Generators (deferred until production scaling).

### 2. Strict Additive Scene Order
- **Decision**: Orchestrate scene loading in a hard-coded sequence: Bootstrap → Systems → Level → Gameplay → Camera → UI.
- **Rationale**: ADR-0001 requires this order to ensure that presentation systems (Camera/UI) always load after the systems they observe (Gameplay/Systems). This prevents race conditions where a UI element tries to bind to a missing gameplay service.
- **Alternatives**: Parallel loading (rejected for complexity), single-scene loading (rejected for ownership boundary violations).

### 3. M0Contracts as the DI Interface Hub
- **Decision**: Use `M0Contracts.cs` (interfaces and DTOs) as the primary registration targets in VContainer.
- **Rationale**: ADR-0005 establishes `M0Contracts` as the temporary contracts-only hub. This allows systems to reference each other via interfaces without creating assembly dependency cycles.

## Risks / Trade-offs

- **Circular Dependencies** → *Mitigation*: Strictly follow the dependency direction (Core references nothing; Presentation references Core). Use the `M0Contracts` hub to break cycles between systems.
- **Scene Loading Timing** → *Mitigation*: Implement a simple synchronous or basic async `M0BootstrapOrchestrator` to ensure each scene is loaded before the next begins initialization if required by VContainer parent-child scopes.
- **Manual Registry Maintenance** → *Mitigation*: Add an EditMode test that attempts to resolve all mandatory M0 interfaces from the `GameplayScope` to catch missing registrations early.
