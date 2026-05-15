# ADR-0002: M0 Gameplay Truth Ownership Boundaries

## Status
Accepted

## Date
2026-05-15

## Last Verified
2026-05-15 — when this ADR was written

## Decision Makers
User + Codex

## Summary
Records the M0 gameplay truth ownership boundaries for the Glass Refrain prototype. Establishes clear ownership of gameplay truth across core systems: Pure C# gameplay truth, Input emits intent only, Locomotion owns movement truth, Target Context owns target truth, Combat Core owns combat validity/results, Enemy Intent owns telegraph/commit/recovery, Health owns damage/consequence/reaction, Memory State owns reveal acceptance/rejection, and Encounter owns lifecycle only.

## Engine Compatibility
| Field | Value |
|-------|-------|
| **Engine** | Unity 6000.3.x |
| **Domain** | Core / Gameplay |
| **Knowledge Risk** | LOW — in training data |
| **References Consulted** | docs/engine-reference/unity/VERSION.md |
| **Post-Cutoff APIs Used** | None |
| **Verification Required** | None |

## ADR Dependencies
| Field | Value |
|-------|-------|
| **Depends On** | ADR-0001 |
| **Enables** | ADR-0003, ADR-0004, ADR-0005 |
| **Blocks** | None |
| **Ordering Note** | None |

## Context
### Problem Statement
M0 needed clear gameplay truth ownership boundaries documented to prevent ownership drift and support traceability without expanding scope.

### Current State
These ownership decisions were implemented in the project but not captured in a single traceable record.

### Constraints
- Documentation-only change
- No runtime code modifications
- Must record existing decisions only

### Requirements
- Document Pure C# gameplay truth ownership
- Define Input system responsibilities (intent only)
- Establish Locomotion ownership of movement truth
- Define Target Context ownership of target truth
- Establish Combat Core ownership of combat validity/results
- Document Enemy Intent ownership of telegraph/commit/recovery
- Establish Health ownership of damage/consequence/reaction
- Define Memory State ownership of reveal acceptance/rejection
- Establish Encounter ownership of lifecycle only

## Decision
Record the following M0 gameplay truth ownership boundary decisions:

### Pure C# Gameplay Truth
- All authoritative gameplay state exists in Pure C# classes/structs
- Unity components act as adapters, composition roots, or presentation surfaces only
- No gameplay truth stored in MonoBehaviour fields or ProjectRoot singletons

### Input System Ownership
- Input Mapping owns raw input truth only
- Input emits intent only (movement, look, action intents)
- Input does not own movement, targeting, or combat truth
- Input enabled/disabled context is owned by Input Mapping

### Locomotion Truth Ownership
- Player Locomotion owns movement truth (position, rotation, velocity, facing)
- Locomotion processes input intents to produce movement
- Locomotion owns movement expression and current locomotion recovery truth
- Locomotion does not own combat validity or target acquisition

### Target Context Ownership
- Lock-On / Target Context owns target truth (current target, target validity, lock-on state)
- Target Context resolves acquire/release requests from Input
- Target Context does not own targeting decisions or combat validity
- Target Context provides read-only target data to other systems

### Combat Core Ownership
- Combat Core owns combat validation and result truth (action acceptance/rejection, hit/miss, block/parry/counter)
- Combat Core validates action requests against current combat state
- Combat Core emits combat action request results plus action lock/recovery request context
- Combat Core does not own movement expression or locomotion truth

### Enemy Intent Ownership
- Enemy Intent & Telegraph owns enemy-side readability and punish truth
- Enemy Intent exposes telegraph state, active timing, and attack tags
- Enemy Intent owns telegraph/commit/recovery timing and vulnerability windows
- Enemy Intent does not own enemy movement or combat validity

### Health Ownership
- Health / Damage / Hit Reaction owns damage/application and consequence truth
- Health processes hit results to apply damage and consequence
- Health owns damage/consequence/reaction state and hit reaction categories
- Health does not own damage application decisions or hit reaction expression

### Memory State Ownership
- Memory State owns reveal acceptance and memory-side consequence truth
- Memory State accepts, rejects, or ignores reveal requests from Combat Core
- Memory State owns reveal acceptance tuning and memory cooldown/reset state
- Memory State does not own VFX playback or memory-triggered gameplay effects

### Encounter Ownership
- Encounter Framework owns encounter lifecycle only (start, active, end, reset states)
- Encounter Framework manages participant registration and readiness validation
- Encounter Framework observes end/fail/abort/reset conditions and emits contexts
- Encounter Framework does not own combat, health, memory, or gameplay truth

## Implementation Guidelines
- Maintain Pure C# gameplay truth in dedicated code folders
- Use input intents as the sole communication from Input to gameplay systems
- Ensure systems only consume truth they own or request via defined interfaces
- Prevent gameplay truth from leaking into Unity components or presentation systems
- Validate ownership boundaries through code reviews and architecture documentation

## Alternatives Considered
### Alternative 1: Unity Component-Based Truth
- **Description**: Store gameplay truth in MonoBehaviour fields on GameObjects
- **Pros**: Direct access in Unity editor, familiar Unity pattern
- **Cons**: Makes truth difficult to test, violates separation of concerns, creates hidden dependencies
- **Rejection Reason**: Conflicts with Pure C# gameplay truth requirement and testability goals

### Alternative 2: Centralized Gameplay Singleton
- **Description**: Store all gameplay truth in a root-scoped singleton service
- **Pros**: Simple global access to all gameplay state
- **Cons**: Creates tight coupling, violates scene scope boundaries, makes testing difficult
- **Rejection Reason**: Violates VContainer scoping principles and creates ownership ambiguity

### Alternative 3: Physics Component-Based Truth
- **Description**: Store movement/truth in Unity physics components (Rigidbody, Collider)
- **Pros**: Integrated with Unity physics system
- **Cons**: Mixes gameplay truth with physics representation, difficult to serialize/test
- **Rejection Reason**: Conflicts with Pure C# gameplay truth and creates physics/gameplay coupling

## Consequences
### Positive
- Clear documentation of existing gameplay truth ownership decisions
- Prevents ownership drift and hidden authority issues
- Supports traceability for architecture reviews
- Enables future consistency and gate checks on ownership boundaries

### Negative
- Documentation overhead for maintenance
- Requires discipline to maintain ownership boundaries in implementation

### Neutral
- No immediate changes to runtime behavior
- Architecture patterns remain as implemented

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Ownership drift (multiple systems owning same truth) | Medium | Medium | Code reviews, clear interface definitions |
| Input emitting more than intent | Low | Medium | Input system validation, code reviews |
| Systems consuming unowned truth | Medium | Medium | Dependency direction checks, architecture validation |

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
| Foundational — no GDD requirement. Enables: All M0 GDD systems by documenting gameplay truth ownership boundaries. |

## Related
- Links to related ADRs will be added as they are created
- Link to relevant code files: Architecture documentation only