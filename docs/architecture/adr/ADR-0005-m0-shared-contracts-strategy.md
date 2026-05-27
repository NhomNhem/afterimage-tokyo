# ADR-0005: M0 Shared Contracts Strategy

## Status
Accepted

## Date
2026-05-15

## Last Verified
2026-05-15 — when this ADR was written

## Decision Makers
User + Codex

## Summary
Records the M0 shared contracts strategy for the Glass Refrain prototype. Establishes M0Contracts.cs as a temporary shared contract hub, defines its contracts-only nature, and establishes split trigger conditions for when contracts become too broad or after First Playable.

## Engine Compatibility
| Field | Value |
|-------|-------|
| **Engine** | Unity 6000.3.x |
| **Domain** | Core / Contracts |
| **Knowledge Risk** | LOW — in training data |
| **References Consulted** | docs/engine-reference/unity/VERSION.md |
| **Post-Cutoff APIs Used** | None |
| **Verification Required** | None |

## ADR Dependencies
| Field | Value |
|-------|-------|
| **Depends On** | ADR-0001, ADR-0002, ADR-0003, ADR-0004 |
| **Enables** | None |
| **Blocks** | None |
| **Ordering Note** | None |

## Context
### Problem Statement
M0 needed a clear shared contracts strategy documented to prevent contracts from accumulating behavior logic, to establish when to split contracts by domain, and to support traceability without expanding scope.

### Current State
This shared contracts strategy was implemented in the project but not captured in a single traceable record.

### Constraints
- Documentation-only change
- No runtime code modifications
- Must record existing decisions only

### Requirements
- Document M0Contracts.cs as temporary shared contract hub allowed for M0
- Establish M0Contracts.cs remains contracts-only (no behavior logic)
- Define split trigger after First Playable or when contracts become too broad
- Document possible future change: split-m0-contracts-by-domain

## Decision
Record the following M0 shared contracts strategy decisions:

### Temporary Shared Contract Hub
- M0Contracts.cs is allowed as a temporary shared contract hub for M0 scope only
- Contracts file contains only data structures, interfaces, and enums shared across systems
- No behavior logic, state machines, or gameplay systems are implemented in M0Contracts.cs
- M0Contracts.cs serves as a centralized location for shared DTOs, requests, results, and snapshots
- The file is explicitly temporary and intended to be refactored post-M0

### Contracts-Only Nature
- M0Contracts.cs contains exclusively:
  - Data Transfer Objects (DTOs) for cross-system communication
  - Request/result contexts (e.g., CombatActionRequest, RevealRequestContext)
  - Snapshot structures (e.g., HealthStateSnapshot, LocomotionStateSnapshot)
  - Enums defining action types, states, or categories
  - Interface definitions for pure contracts (no implementation)
- M0Contracts.cs explicitly excludes:
  - MonoBehaviour implementations
  - Pure C# FSMs or state machines
  - Service classes or managers
  - Any behavior logic, algorithms, or stateful operations
  - UnityEngine dependencies except for basic serializable types (Vector3, etc.) when absolutely necessary for data transfer

### Split Trigger Conditions
- Split trigger occurs after First Playable is achieved and validated
- Split trigger occurs when M0Contracts.cs becomes too broad (exceeds reasonable shared contract size)
- Split trigger occurs when contract ownership becomes unclear or systems develop domain-specific contract needs
- The specific change to split contracts is: split-m0-contracts-by-domain
- Post-split, contracts will reside in their respective domain assemblies (e.g., combat contracts in Combat assembly)

### Future Evolution
- After split, each domain owns its contracts in its respective assembly
- Cross-domain communication uses explicitly defined interface contracts
- No global contracts hub remains after splitting
- Contracts remain pure data/interfaces without behavior

## Implementation Guidelines
- Keep M0Contracts.cs strictly limited to contracts only
- Review any additions to M0Contracts.cs for behavioral content
- Monitor file size and scope to detect when splitting is needed
- Prepare for post-M0 refactoring to distribute contracts to domain assemblies
- Ensure all contracts remain serializable and usable across scope boundaries
- Avoid putting Unity-specific types in contracts when possible (prefer plain C# types)

## Alternatives Considered
### Alternative 1: No Shared Contracts
- **Description**: Each system defines its own contracts with no sharing
- **Pros**: Zero risk of inappropriate sharing, maximum domain isolation
- **Cons**: Duplication of similar contracts, inconsistent data structures, difficult cross-system communication
- **Rejection Reason**: Creates unnecessary duplication and hinders system integration needed for M0 prototype

### Alternative 2: Permanent Global Contracts Hub
- **Description**: Keep M0Contracts.cs as permanent shared location for all contracts
- **Pros**: Single source of truth for shared data structures, consistent contracts
- **Cons**: Becomes dumping ground for unrelated contracts, violates domain ownership principles, grows uncontrollably
- **Rejection Reason**: Violates temporary nature requirement and creates long-term maintenance burden

### Alternative 3: Contracts in Individual Systems with Duplication
- **Description**: Define similar contracts in each system with slight variations as needed
- **Pros**: Maximum domain ownership, no sharing concerns
- **Cons**: Contract duplication, inconsistency in shared concepts, difficult to evolve shared patterns
- **Rejection Reason**: Creates maintenance burden and inconsistency in shared concepts like snapshots or requests

### Alternative 4: Contracts in Infrastructure Assembly
- **Description**: Place all shared contracts in GlassRefrain.Infrastructure assembly
- **Proper**: Centralized location, follows dependency direction (Core <- Infrastructure)
- **Cons**: Still creates global contracts hub, mixes infrastructure concerns with pure data contracts
- **Rejection Reason**: Still creates a global hub (just in different location) and doesn't solve core issue

## Consequences
### Positive
- Clear documentation of existing shared contracts strategy
- Prevents accumulation of behavior logic in contracts file
- Establishes clear trigger conditions for contract splitting
- Supports traceability for architecture reviews
- Enables future consistency and gate checks on contracts strategy

### Negative
- Documentation overhead for maintenance
- Requires discipline to maintain contracts-only nature
- Temporary hub will require future refactoring effort

### Neutral
- No immediate changes to runtime behavior
- Architecture patterns remain as implemented

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Behavior logic accumulating in M0Contracts.cs | Medium | High | Code reviews, contracts-only validation, automated checks |
| Missing split trigger leading to bloated contracts file | Medium | Medium | Regular contract file reviews, size/threshhold monitoring |
| Unclear contract ownership after split | Low | Medium | Domain ownership documentation, interface definition standards |
| Contracts becoming too granular or fragmented | Low | Low | Contract cohesion guidelines, domain-specific contract grouping |

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
| Foundational — no GDD requirement. Enables: All M0 GDD systems by documenting shared contracts strategy. |

## Related
- Links to related ADRs will be added as they are created
- Link to relevant code files: Architecture documentation only
