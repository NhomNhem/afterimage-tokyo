# ADR-0001: Decompose M0 Gameplay Tick Handler Orchestration

## Status
Proposed

## Date
2026-05-29

## Engine Compatibility

| Field | Value |
|-------|-------|
| Engine | Unity 6000.3.x |
| Domain | Core / Bootstrap Orchestration |
| Knowledge Risk | MEDIUM |
| References Consulted | docs/engine-reference/unity/VERSION.md; docs/engine-reference/unity/breaking-changes.md; docs/engine-reference/unity/deprecated-apis.md; docs/engine-reference/unity/modules/input.md |
| Post-Cutoff APIs Used | None |
| Verification Required | Unity Play Mode smoke for M0 loop + S3-2 interact parity after each extraction slice |

## ADR Dependencies

| Field | Value |
|-------|-------|
| Depends On | None |
| Enables | Future ADR: split-m0-contracts-by-bounded-context; future ADR: modularize-m0-combat-core-state-machine |
| Blocks | None |
| Ordering Note | This ADR should land before any CombatCore deep refactor to reduce orchestration blast radius first. |

## Context

### Problem Statement
`M0GameplayTickHandler` has grown into a high-coupling orchestration hotspot (~500+ lines), mixing input routing, memory tick bridging, snapshot fan-out, debug sync, and reset flow. This increases regression risk for M0/S3-2 and obscures ownership boundaries.

### Constraints
- Preserve behavior for verified M0 duel loop and S3-2 interact flow.
- Do not move gameplay truth ownership out of existing owners.
- No CombatCore timing/result changes in this ADR.
- No broad DI migration in this ADR.
- No scene/prefab ownership changes.

### Requirements
- Tick handler remains orchestration boundary only.
- Extraction must be behavior-preserving and evidence-driven.
- Ownership stays intact:
  - Input = raw intent
  - CombatCore = combat validity/result
  - PlayerLocomotion = movement truth
  - TargetContext = lock-on truth
  - MemoryState = reveal/collect truth

## Decision

`M0GameplayTickHandler` SHALL be reduced to explicit orchestration order and lifecycle wiring only. Non-trivial responsibilities SHALL be extracted into narrow collaborators with stable contracts and no truth ownership drift.

This ADR records the decomposition decision only. Implementation requires a separate OpenSpec change before any runtime extraction.

### In Scope
- Define decomposition direction and collaborator boundaries.
- Behavior-preserving extraction plan.
- Preserve M0/S3-2 current verified behavior.

### Out of Scope
- CombatCore state machine rewrite.
- Combat timing changes.
- Input architecture rewrite in the same ADR.
- R3/MessagePipe migration.
- Animancer/VFX authority changes.
- Broad Nhem DI migration.
- No changes to S3-2 Memory Fragment interaction behavior.
- No MemoryRaycastProProbe alignment in this ADR.

### Architecture Direction (Target Shape)
- `M0GameplayTickHandler`:
  - lifecycle entry (`Construct`, `Update`, `OnDestroy`)
  - deterministic orchestration order
  - wiring of snapshots/events
- Extracted collaborators (initial):
  1. `MemoryInteractionTickBridge`
  2. `InputIntentRoutingBridge`
  3. `DebugSnapshotPublishBridge`
  4. `EncounterResetBridge` (if needed)

`InputIntentRoutingBridge` routes already-produced raw input intents and does not own Unity InputAction callbacks.

## Alternatives Considered

### Alternative 1: Keep one class and only rearrange methods
- **Description**: Keep `M0GameplayTickHandler` as a single type and improve readability with method grouping only.
- **Pros**: No new types; minimal immediate churn.
- **Cons**: Coupling remains; ownership blur persists; review surface stays large.
- **Rejection Reason**: Does not address maintainability and regression-risk hotspot.

### Alternative 2: Refactor CombatCore first
- **Description**: Split `M0CombatCore` before orchestration refactor.
- **Pros**: Targets another large file quickly.
- **Cons**: Highest gameplay-risk area; directly touches combat truth/timing.
- **Rejection Reason**: Wrong sequencing for M0 risk profile.

### Alternative 3: Split contracts first
- **Description**: Decompose `M0Contracts` before tick-handler orchestration cleanup.
- **Pros**: Strong long-term modularity gains.
- **Cons**: Broad ripple across references/assembly boundaries while S3-2 is active.
- **Rejection Reason**: Safer after orchestration boundary is clean.

## Consequences

### Positive
- Lower blast radius for future gameplay changes.
- Clearer ownership boundaries at runtime wiring point.
- Easier parity verification per thin slice.

### Negative
- More files/types in Bootstrap layer.
- Requires strict naming and contract discipline.

### Risks
- Hidden behavior drift during extraction.
- Event ordering drift in the update loop.

### Risk Mitigation
- Keep orchestration order explicit and unchanged.
- Thin-slice extraction with per-slice smoke/evidence.
- Unity console check after each code step.

## GDD Requirements Addressed

| GDD System | Requirement | How This ADR Addresses It |
|------------|-------------|---------------------------|
| input-mapping.md | Input remains raw intent, no gameplay truth | Intent routing is orchestration-only; ownership remains in input layer contracts |
| combat-core.md | CombatCore owns validity/timing/results | Tick handler coordinates calls but does not move combat truth ownership |
| memory-state.md | MemoryState owns reveal acceptance truth | Memory bridge routes context only; acceptance/rejection remains in MemoryState |
| debug-overlay.md | Debug remains read-only observer | Debug publish bridge keeps read-model/presentation role only |
| systems-index.md | Ownership boundaries remain explicit | Decomposition enforces owner-by-system boundaries in runtime orchestration |

## Performance Implications
- **CPU**: Neutral to slightly positive (smaller focused methods and collaborators).
- **Memory**: Slight increase from a few small collaborator instances.
- **Load Time**: Neutral.
- **Network**: Not applicable.

## Migration Plan

Slice 1:
- Extract `MemoryInteractionTickBridge` from current update path.
- Parity check: interact/reveal accepted path remains PASS.

Slice 2:
- Extract `InputIntentRoutingBridge`.
- Parity check: move/light/parry/dodge/counter routes unchanged.

Slice 3:
- Extract `DebugSnapshotPublishBridge`.
- Parity check: LastInput/debug channels remain observable.

Slice 4:
- Reduce `M0GameplayTickHandler` to explicit orchestration order only.
- Final parity check: M0 loop + S3-2 regression matrix.

## Validation Criteria
- No compile/runtime errors in Unity console.
- M0 loop remains readable and behavior-equivalent.
- S3-2 interact remains accepted under the same conditions.
- No ownership drift found in code review checklist.

## Related Decisions
- Future ADR candidate: split-m0-contracts-by-bounded-context
- Future ADR candidate: modularize-m0-combat-core-state-machine
- Architecture reference: docs/architecture/architecture.md
