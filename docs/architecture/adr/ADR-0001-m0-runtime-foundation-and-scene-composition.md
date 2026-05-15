# ADR-0001: M0 Runtime Foundation and Scene Composition

## Status
Accepted

## Date
2026-05-15

## Last Verified
2026-05-15 — when this ADR was written

## Decision Makers
User + Codex

## Summary
Records the M0 runtime foundation and scene composition decisions for the Glass Refrain prototype. Establishes Unity 6000.3.x with URP, additive scene composition, and clear separation of concerns across Bootstrap, Systems, Gameplay, Camera, UI, and Level scenes.

## Engine Compatibility
| Field | Value |
|-------|-------|
| **Engine** | Unity 6000.3.x |
| **Domain** | Core / Infrastructure |
| **Knowledge Risk** | LOW — in training data |
| **References Consulted** | docs/engine-reference/unity/VERSION.md |
| **Post-Cutoff APIs Used** | None |
| **Verification Required** | None |

## ADR Dependencies
| Field | Value |
|-------|-------|
| **Depends On** | None |
| **Enables** | ADR-0002, ADR-0003, ADR-0004, ADR-0005 |
| **Blocks** | None |
| **Ordering Note** | None |

## Context
### Problem Statement
M0 needed clear runtime foundation and scene composition boundaries documented to support traceability and future architecture reviews without expanding scope.

### Current State
These decisions were implemented in the project but not captured in a single traceable record.

### Constraints
- Documentation-only change
- No runtime code modifications
- Must record existing decisions only

### Requirements
- Document Unity version and render pipeline
- Define additive scene composition approach
- Establish scene responsibility boundaries
- Define VContainer lifetime scopes

## Decision
Record the following M0 runtime foundation and scene composition decisions:

### Unity Engine and Pipeline
- Unity 6000.3.x LTS with Universal Render Pipeline (URP)
- No dependency on DOTS/ECS or experimental packages

### Additive Scene Composition
M0 uses additive scene loading with six required scenes loaded in specific order:
1. Bootstrap - startup entry, root configuration, initial scene-set load
2. Systems - persistent app-level services, service adapters, shared configuration
3. Level_TokyoStreet_Blockout - duel arena geometry, blockout colliders, spawn markers
4. Gameplay_CombatPrototype - player/enemy/encounter roots, gameplay-scoped lifetime, authoritative M0 runtime state
5. Camera_CombatPrototype - Cinemachine Brain host, virtual cameras, camera coordinators
6. UI_DebugOverlay - debug UI Toolkit overlay root, read-only debug presentation

### Scene Responsibility Boundaries
Each scene has clearly defined ownership:
- **Bootstrap**: Owns startup and initial scene loading; does not own combat/locomotion/truth
- **Systems**: Owns persistent services and configuration; does not own active duel state
- **Gameplay_CombatPrototype**: Owns player/enemy/encounter roots and gameplay lifetime scope; does not own persistent app lifetime
- **Camera_CombatPrototype**: Owns Cinemachine setup and camera coordination; does not own target/movement truth
- **UI_DebugOverlay**: Owns debug presentation only; does not own gameplay state
- **Level_TokyoStreet_Blockout**: Owns arena geometry and spawn points; does not own gameplay truth

### VContainer Lifetime Scopes
- **ProjectRootLifetimeScope**: Bootstrap services, scene loader, global config, logging, package adapters
- **GameplayScope**: Input Mapping runtime, Locomotion FSM, Combat Core FSM, Enemy Intent FSM, Health service, Target Context FSM, Memory State FSM, Encounter Micro-scope
- **CameraScope**: Camera coordinator, Cinemachine adapters, camera feedback services
- **UI/DebugScope**: Debug overlay presenters, snapshot assemblers, visibility toggles

## Implementation Guidelines
- Maintain additive scene loading order strictly
- Enforce scene responsibility boundaries via code reviews
- Validate VContainer scopes prevent accidental cross-scope registrations
- Keep all decisions as documentation; no runtime enforcement mechanisms required

## Alternatives Considered
### Alternative 1: Single Scene Approach
- **Description**: All systems in one scene with runtime enable/disable
- **Pros**: Simpler scene management
- **Cons**: Violates scene responsibility boundaries, harder to isolate systems, conflicts with additive loading requirement
- **Rejection Reason**: Does not meet M0 requirement for clear scene separation and additive loading from day one

### Alternative 2: Addressables-Based Loading
- **Description**: Load scenes via Addressables asset system
- **Pros**: Better memory management, asynchronous loading
- **Cons**: Adds complexity unnecessary for M0 scope, requires additional setup not justified for prototype
- **Rejection Reason**: Out of scope for M0; additive scene loading with standard Unity approach sufficient

## Consequences
### Positive
- Clear documentation of existing runtime foundation decisions
- Enables traceability for architecture reviews
- Supports future consistency and gate checks
- Maintains M0 scope boundaries

### Negative
- Documentation overhead for maintenance
- Requires discipline to maintain scene separation in implementation

### Neutral
- No immediate changes to runtime behavior
- Architecture patterns remain as implemented

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Scene responsibility drift | Medium | Medium | Code reviews, architecture documentation |
| VContainer scope violations | Low | Medium | Dependency injection testing, scope validation |
| Additive loading order mistakes | Low | High | Automated scene loading validation |

## Performance Implications
| Metric | Before | Expected After | Budget |
|--------|--------|---------------|--------|
| CPU (frame time) | [Current]ms | [Same]ms | [Budget]ms |
| Memory | [Current]MB | [Same]MB | [Budget]MB |
| Load Time | [Current]s | [Same]s | [Budget]s |

## Migration Plan
1. No migration needed - recording existing decisions
2. Verify documentation accuracy against current implementation
3. Update if implementation diverges from documented decisions

**Rollback plan**: Revert documentation changes if needed; no runtime impact

## Validation Criteria
- [ ] All five ADR files created with correct scope
- [ ] Each ADR records only already-made decisions
- [ ] No runtime code, scene, prefab, UI/VFX, or gameplay behavior changes introduced
- [ ] Unresolved decisions marked as Open where applicable
- [ ] Outputs are evaluable by future /consistency-check and /gate-check

## GDD Requirements Addressed
| GDD Document | System | Requirement | How This ADR Satisfies It |
|--------------|--------|-------------|--------------------------|
| Foundational — no GDD requirement. Enables: All M0 GDD systems by documenting runtime foundation boundaries. |

## Related
- Links to related ADRs will be added as they are created
- Link to relevant code files: Architecture documentation only