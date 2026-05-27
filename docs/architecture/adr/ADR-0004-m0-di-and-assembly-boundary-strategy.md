# ADR-0004: M0 DI and Assembly Boundary Strategy

## Status
Accepted

## Date
2026-05-15

## Last Verified
2026-05-15 — when this ADR was written

## Decision Makers
User + Codex

## Summary
Records the M0 DI and assembly boundary strategy for the Glass Refrain prototype. Establishes manual VContainer scopes for M0, defers generated DI, defines asmdef dependency direction, and ensures no gameplay truth is registered globally by accident.

## Engine Compatibility
| Field | Value |
|-------|-------|
| **Engine** | Unity 6000.3.x |
| **Domain** | Infrastructure / Dependency Injection |
| **Knowledge Risk** | LOW — in training data |
| **References Consulted** | docs/engine-reference/unity/VERSION.md |
| **Post-Cutoff APIs Used** | None |
| **Verification Required** | None |

## ADR Dependencies
| Field | Value |
|-------|-------|
| **Depends On** | ADR-0001, ADR-0002, ADR-0003 |
| **Enables** | ADR-0005 |
| **Blocks** | None |
| **Ordering Note** | None |

## Context
### Problem Statement
M0 needed clear DI and assembly boundary strategy documented to prevent dependency violations, accidental global registrations, and to support traceability without expanding scope.

### Current State
These DI and assembly boundary decisions were implemented in the project but not captured in a single traceable record.

### Constraints
- Documentation-only change
- No runtime code modifications
- Must record existing decisions only

### Requirements
- Document Manual VContainer scopes for M0
- Establish Generated DI deferred for M0
- Ensure No gameplay truth registered globally by accident
- Define asmdef dependency direction
- Establish No domain assembly depends on UI/VFX/Camera unless explicitly presentation-facing

## Decision
Record the following M0 DI and assembly boundary strategy decisions:

### Manual VContainer Scopes for M0
- All VContainer registrations are manual (no code generation or automatic scanning)
- Scopes are clearly defined: ProjectRootLifetimeScope, GameplayScope, CameraScope, UI/DebugScope
- No automatic type registration or reflection-based discovery is used
- All service lifetimes are explicitly defined (Singleton, Scoped, Transient)
- Scopes are properly disposed when scenes are unloaded

### Generated DI Deferred
- Generated DI (via source generators or automatic binding) is explicitly deferred for M0
- All DI configuration is hand-written and explicit
- No automatic interface-to-implementation mapping is used
- DI containers are composed manually in composition roots per scope
- Generated DI may be considered for post-M0 scope when benefits outweigh complexity

### No Global Gameplay Truth Registration
- No gameplay truth types ( Pure C# state models, FSMs, etc.) are registered in ProjectRootLifetimeScope
- Gameplay-scoped services are registered only in GameplayScope or appropriate sub-scopes
- Root scope contains only bootstrap services, scene loaders, configuration access, logging, and safe package adapters
- Accidental global registration is prevented through scope validation and code reviews

### Asmdef Dependency Direction
Preferred dependency shape:
- GlassRefrain.Core references nothing (pure domain logic)
- GlassRefrain.Infrastructure references GlassRefrain.Core
- GlassRefrain.Bootstrap references GlassRefrain.Core, GlassRefrain.Infrastructure
- Domain assemblies (Input, Locomotion, Combat, Enemy, Targeting, Camera, Health, Memory, Encounter, VFX, UI) reference GlassRefrain.Core
- Presentation assemblies reference GlassRefrain.Core plus presentation-safe domain contracts only
- Tests reference the assemblies under test

### Forbidden Dependencies
- Core -> anything (Core has no dependencies)
- Combat -> Camera, UI, VFX
- Locomotion -> Camera, UI
- Memory -> Camera, UI
- Targeting -> Camera, UI
- any runtime assembly -> test assembly
- Domain assembly -> UI/VFX/Camera unless explicitly presentation-facing (camera basis, debug snapshots)

### Presentation-Facing Contracts Only
- Assemblies may depend on UI/VFX/Camera only through explicitly defined, presentation-safe contracts
- Examples: CameraMovementBasisSnapshot, DebugSnapshot DTOs, UI event contracts
- These contracts contain only data, no behavior or gameplay truth
- Contracts are defined in Core or Infrastructure assemblies to maintain dependency direction

## Implementation Guidelines
- Maintain manual VContainer registrations in composition roots per scope
- Validate asmdef dependencies regularly to prevent forbidden directions
- Ensure all gameplay truth remains scoped appropriately (never in root scope)
- Use presentation-facing contracts for any cross-domain presentation needs
- Review DI configurations to prevent accidental global registrations
- Keep all DI configuration explicit and readable

## Alternatives Considered
### Alternative 1: Automatic DI Scanning
- **Description**: Use reflection or source generators to automatically register types
- **Pros**: Reduced boilerplate, automatic dependency resolution
- **Cons**: Risk of accidental global registrations, obscured dependency relationships, harder to validate scopes
- **Rejection Reason**: Violates Manual VContainer scopes requirement and increases risk of gameplay truth in root scope

### Alternative 2: Single Root Scope for All Services
- **Description**: Register all services in ProjectRootLifetimeScope regardless of lifetime needs
- **Pros**: Simplified DI configuration, global access to all services
- **Cons**: Violates scene scope principles, creates unnecessary object retention, mixes lifetime concerns
- **Rejection Reason**: Directly conflicts with VContainer scoping requirements and creates memory/performance issues

### Alternative 3: Unrestricted Asmdef Dependencies
- **Description**: Allow assemblies to reference each other freely based on needs
- **Pros**: Maximum flexibility in code organization
- **Cons**: Creates dependency cycles, obscures architectural layers, violates dependency direction principles
- **Rejection Reason**: Conflicts with established asmdef dependency direction and layering principles

### Alternative 4: Gameplay Truth in Root Scope for Simplicity
- **Description**: Register gameplay services in root scope to avoid scope complexity
- **Pros**: Simple access to gameplay truth from any system
- **Cons**: Violates scene ownership principles, creates hidden dependencies, makes testing difficult
- **Rejection Reason**: Directly conflicts with No gameplay truth registered globally by accident requirement

## Consequences
### Positive
- Clear documentation of existing DI and assembly boundary strategy
- Prevents dependency violations and accidental global registrations
- Maintains clean architectural layers and dependency direction
- Supports traceability for architecture reviews
- Enables future consistency and gate checks on DI and assembly boundaries

### Negative
- Documentation overhead for maintenance
- Requires discipline to maintain DI configurations and asmdef dependencies
- Manual DI requires more boilerplate than automatic alternatives

### Neutral
- No immediate changes to runtime behavior
- Architecture patterns remain as implemented

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Accidental global gameplay truth registration | Medium | High | Scope validation, code reviews, DI configuration audits |
| Forbidden asmdef dependencies introduced | Medium | Medium | Dependency validation, automated asmdef checking |
| Presentation assemblies depending on gameplay truth | Low | Medium | Contract validation, interface reviews |
| Manual DI becoming burdensome | Low | Low | Template creation, DI pattern standardization |

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
| Foundational — no GDD requirement. Enables: All M0 GDD systems by documenting DI and assembly boundary strategy. |

## Related
- Links to related ADRs will be added as they are created
- Link to relevant code files: Architecture documentation only
