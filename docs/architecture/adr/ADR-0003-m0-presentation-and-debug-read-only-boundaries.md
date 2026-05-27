# ADR-0003: M0 Presentation and Debug Read-Only Boundaries

## Status
Accepted

## Date
2026-05-15

## Last Verified
2026-05-15 — when this ADR was written

## Decision Makers
User + Codex

## Summary
Records the M0 presentation and debug read-only boundaries for the Glass Refrain prototype. Establishes that presentation systems (Animator, Camera, Memory VFX Response, Debug Overlay, UI/UX foundation) are downstream observers only and do not own gameplay truth, maintaining clear separation between gameplay authority and presentation concerns.

## Engine Compatibility
| Field | Value |
|-------|-------|
| **Engine** | Unity 6000.3.x |
| **Domain** | Presentation / Debug |
| **Knowledge Risk** | LOW — in training data |
| **References Consulted** | docs/engine-reference/unity/VERSION.md |
| **Post-Cutoff APIs Used** | None |
| **Verification Required** | None |

## ADR Dependencies
| Field | Value |
|-------|-------|
| **Depends On** | ADR-0001, ADR-0002 |
| **Enables** | ADR-0004, ADR-0005 |
| **Blocks** | None |
| **Ordering Note** | None |

## Context
### Problem Statement
M0 needed clear presentation and debug read-only boundaries documented to prevent presentation systems from becoming hidden authorities and to support traceability without expanding scope.

### Current State
These presentation and debug boundaries were implemented in the project but not captured in a single traceable record.

### Constraints
- Documentation-only change
- No runtime code modifications
- Must record existing decisions only

### Requirements
- Document Animator as presentation-only
- Establish Camera owns framing/readability only
- Define Memory VFX Response as downstream presentation only
- Establish Debug Overlay as read-only snapshot aggregation
- Define UI/UX foundation as documentation only for M0

## Decision
Record the following M0 presentation and debug read-only boundary decisions:

### Animator Presentation Only
- Animator system owns visual presentation only (animation blending, state transitions based on parameters)
- Animator does not own combat, movement, or recovery truth
- Animator parameters are driven by gameplay systems (Locomotion, Combat Core, etc.)
- Animator does not affect gameplay state through animation events or clip lengths
- Animation events are used for visual/audio feedback only, never to change gameplay truth

### Camera Ownership
- Lock-On & Combat Camera owns framing and readability only (camera positioning, targeting, composition)
- Camera owns Cinemachine Brain host assumptions and virtual camera objects
- Camera owns camera coordinators that adjust framing based on gameplay context
- Camera does not own target truth, movement truth, or combat validity
- Camera provides CameraMovementBasisSnapshot as read-only reference data
- Camera never interprets movement direction or makes movement decisions

### Memory VFX Response Presentation
- Memory VFX Response is downstream presentation only (visual effects triggered by memory reveals)
- Memory VFX Response receives accepted memory context from Memory State
- Memory VFX Response plays restrained VFX responses based on memory context
- Memory VFX Response does not own memory truth or reveal acceptance decisions
- Memory VFX Response does not trigger gameplay effects or state changes

### Debug Overlay Read-Only
- Debug Overlay owns grouping and presentation of debug snapshots only
- Debug Overlay displays read-only snapshot data from gameplay systems
- Debug Overlay does not own debug truth for any system domain
- Debug Overlay does not mutate gameplay state or influence gameplay decisions
- Debug Overlay acts as a composite view of snapshot assemblers/presenters

### UI/UX Foundation Documentation Only
- UI/UX foundation for M0 is documentation only (no implementation in M0 scope)
- No UI Toolkit implementation or UXML/USS files created for M0
- UI/UX concerns are documented for future implementation beyond M0
- Any UI elements in M0 are strictly for debug purposes only
- UI systems do not own gameplay truth or influence gameplay decisions

## Implementation Guidelines
- Ensure Animator parameters are set exclusively by gameplay systems
- Validate Camera systems only consume read-only gameplay data (snapshots, contexts)
- Confirm Memory VFX Response only reacts to memory state contexts
- Verify Debug Overlay only displays data, never modifies it
- Keep UI/UX foundation as documentation until post-M0 implementation
- Use code reviews to prevent presentation systems from gaining gameplay authority

## Alternatives Considered
### Alternative 1: Animator-Driven Gameplay
- **Description**: Use animation events or animation-driven systems to control gameplay
- **Pros**: Tight visual/gameplay integration, animator as single source of truth
- **Cons**: Creates hidden dependencies, makes gameplay difficult to test, violates Pure C# truth requirement
- **Rejection Reason**: Directly conflicts with Animator presentation-only requirement and Pure C# gameplay truth

### Alternative 2: Camera-Controlled Movement
- **Description**: Have camera system directly influence or determine movement direction
- **Pros**: Automatic target-relative movement, simplified locomotion logic
- **Cons**: Violates camera framing-only ownership, creates circular dependency, removes player agency
- **Rejection Reason**: Conflicts with Camera owns framing/readability only requirement and Locomotion truth ownership

### Alternative 3: Interactive Debug Overlay
- **Description**: Allow debug overlay to modify gameplay state through UI interactions
- **Pros**: Powerful debugging and tuning capabilities
- **Cons**: Violates read-only debug boundary, creates potential for accidental gameplay changes
- **Rejection Reason**: Conflicts with Debug Overlay read-only snapshot aggregation requirement

### Alternative 4: Foundation-Scoped UI Implementation
- **Description**: Implement basic UI systems in M0 foundation scope
- **Pros**: Early UI integration, foundation for future UI work
- **Cons**: Expands M0 scope, creates UI gameplay dependencies, distracts from core combat feel goal
- **Rejection Reason**: Violates UI/UX foundation documentation only requirement and M0 scope limits

## Consequences
### Positive
- Clear documentation of existing presentation and debug boundary decisions
- Prevents presentation systems from becoming hidden authorities
- Maintains clear separation of gameplay truth and presentation concerns
- Supports traceability for architecture reviews
- Enables future consistency and gate checks on presentation boundaries

### Negative
- Documentation overhead for maintenance
- Requires discipline to maintain presentation boundaries in implementation

### Neutral
- No immediate changes to runtime behavior
- Architecture patterns remain as implemented

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Animator becoming gameplay truth source | Medium | Medium | Parameter validation, animation event review |
| Camera influencing movement/truth | Low | Medium | Camera system audits, basis snapshot validation |
| Debug overlay mutating gameplay state | Low | High | Debug system validation, read-only enforcement |
| UI implementation scope creep | Medium | Low | Scope reviews, M0 boundary enforcement |

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
| Foundational — no GDD requirement. Enables: All M0 GDD systems by documenting presentation and debug read-only boundaries. |

## Related
- Links to related ADRs will be added as they are created
- Link to relevant code files: Architecture documentation only
