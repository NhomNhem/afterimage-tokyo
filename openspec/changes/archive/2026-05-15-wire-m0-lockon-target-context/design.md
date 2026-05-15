# Design: Wire M0 Lock-On / Target Context

## Context

Story 1-3 requires wiring the Lock-On / Target Context system for the M0 First Playable Duel. The system must:

- Accept raw `LockOn` input intent from the New Input System
- Interpret intent as acquire/release toggle in Target Context
- Manage target truth (active target, validity, direction) as the single source of truth
- Expose read-only context to Camera, Locomotion, Combat Core, and Debug Overlay
- Support exactly one player, one enemy, one active target maximum

The architecture follows ADR-0002 (gameplay truth ownership), ADR-0003 (presentation read-only), ADR-0004 (manual DI), and ADR-0005 (contracts-only).

## Goals / Non-Goals

**Goals:**
- Input Mapping emits raw `LockOn` intent without interpretation
- Target Context acquires/releases the single M0 enemy via toggle behavior
- Target Context validates/invalidates target based on enemy state changes
- Target Context exposes read-only target state/direction/context
- Manual VContainer composition for Target Context services
- EditMode tests verify ownership, intent routing, and DI registration

**Non-Goals:**
- Multi-target selection, cycling, or priority scoring
- Boss-part targeting or ranged targeting
- Aim assist or soft-targeting
- Combat validity (target focus does not decide attack/hit/dodge/parry/counter)
- Animation-driven targeting or root motion integration
- Locomotion behavior modification (Story 1-2 scope)
- Camera-owned target selection or framing decisions
- Generated DI or automatic VContainer scanning
- Direct device polling (all input via `InputActionAsset`)

## Decisions

### Decision: Target Context owns all target truth
**Rationale**: Per ADR-0002, gameplay truth must have a single owner. Target Context owns:
- `Active` (bool): Whether target focus is currently active
- `CurrentTarget` (ITargetable): The single active target reference
- `TargetDirection` (Vector3): Direction to target for consumers
- Acquire/release/invalidation logic and state transitions

**Alternative considered**: Splitting ownership between Input (acquire), Camera (framing target), and Encounter (targetable registry). **Rejected**: Creates hidden authority and circular dependencies.

### Decision: Toggle behavior implemented in Target Context, not Input
**Rationale**: Input Mapping MUST emit intent only (ADR-0002). Target Context interprets the raw intent based on current state (no active target → acquire; has active target → release). This keeps input decoupled from target state.

**Alternative considered**: Input Mapping tracks toggle state. **Rejected**: Violates "input emits intent only" rule; leaks target truth into input layer.

### Decision: Read-only snapshots for cross-system communication
**Rationale**: Per ADR-0003, presentation systems must observe read-only data. Camera, Locomotion, and Debug Overlay receive `TargetContextSnapshot` (DTO) containing active state, target reference, direction, and last acquire/release/invalidation reasons.

**Alternative considered**: Direct mutable access to Target Context. **Rejected**: Violates read-only boundary; creates risk of mutation from presentation.

### Decision: Manual VContainer registration in GameplayScope
**Rationale**: Per ADR-0004, M0 uses manual DI only. Target Context services register in `GameplayScope` (not ProjectRoot) to maintain scene-scoped lifetimes and prevent accidental global state.

**Alternative considered**: Automatic scanning or generated DI. **Rejected**: Explicitly deferred for M0 to prevent accidental global registrations and ensure clear ownership.

### Decision: Target invalidation on enemy state change, not distance/visibility
**Rationale**: M0 scope excludes range/visibility scoring. Target invalidates when enemy is explicitly unregistered, disabled, defeated, or no longer targetable. This keeps validity deterministic and debuggable.

**Alternative considered**: Range-based invalidation with tunable distance threshold. **Rejected**: Adds unnecessary complexity for M0 single-enemy duel.

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Target truth leaks into Camera/Locomotion | Enforce read-only snapshot pattern; code review DI registrations |
| Input decides acquire/release logic | AC-1 explicitly forbids; test asserts Input Mapping returns raw intent only |
| Toggle behavior ambiguity | Document state machine: Inactive→AcquireRequest→Active→ReleaseRequest→Inactive |
| Enemy registration race condition | Ensure Encounter Framework registers enemy before Target Context can acquire |
| Read-only snapshot mutation | Snapshot DTO uses init-only properties or records; tests verify immutability |

## Migration Plan

N/A for M0 wiring. This is foundational wiring for the first playable duel, not a migration of existing functionality.

## Open Questions

None. All design decisions resolved per GDD and ADR constraints.

## Architecture Overview

```
Input Mapping (New Input System)
    ↓ emits LockOnIntent
M0InputRouter
    ↓ routes to
M0TargetContext (Pure C#)
    ├── Acquire (if no active target)
    ├── Release (if active target)
    ├── Validate/Invalidate (on enemy state change)
    └── Exposes TargetContextSnapshot (read-only)
        ↓
Camera ── Locomotion ── Combat Core ── Debug Overlay
(consumes read-only snapshot)
```

## Key Interfaces

```csharp
// Input layer (M0Contracts)
public record LockOnIntent(bool Requested);

// Target Context (Targeting assembly)
public interface ITargetContext
{
    bool Active { get; }
    ITargetable CurrentTarget { get; }
    Vector3 TargetDirection { get; }
    TargetContextSnapshot GetSnapshot();
    void OnLockOnIntent(LockOnIntent intent);
    void OnTargetInvalidated(InvalidationReason reason);
}

// Read-only snapshot (M0Contracts)
public record TargetContextSnapshot(
    bool Active,
    ITargetable CurrentTarget,
    Vector3 TargetDirection,
    string LastAcquireReason,
    string LastReleaseReason,
    string LastInvalidationReason
);
```

## DI Registration

```csharp
// GameplayScope.cs
builder.Register<ITargetContext, M0TargetContext>(Lifetime.Scoped);
builder.Register<ITargetableRegistry, M0TargetableRegistry>(Lifetime.Scoped);
// M0InputRouter injected with ITargetContext
```
