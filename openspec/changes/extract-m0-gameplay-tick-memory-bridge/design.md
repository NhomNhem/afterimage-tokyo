## Context

ADR-0001 establishes that `M0GameplayTickHandler` must remain orchestration-only and be decomposed in thin, behavior-preserving slices. Slice 1 targets memory-related orchestration only, because S3-2 Memory Fragment Interaction is active and already verified in current flow.

Current orchestration concerns in scope:
- Passing interact-trigger context from tick flow into memory interaction path.
- Routing reveal-related context between combat/memory-facing observers without changing truth ownership.
- Preserving debug/evidence surface currently used for S3-2 and M0 regression checks.

Constraints:
- Proposal-only in this change.
- No Unity submodule modifications.
- No runtime implementation yet.

## Goals / Non-Goals

**Goals:**
- Define a safe extraction boundary for memory-related orchestration from `M0GameplayTickHandler`.
- Preserve behavior for M0 and S3-2, especially Interact accepted flow and existing duplicate interaction behavior.
- Keep ownership boundaries explicit and unchanged.
- Define focused evidence expectations before implementation starts.

**Non-Goals:**
- No CombatCore state-machine refactor.
- No combat timing/result changes.
- No input architecture refactor.
- No `MemoryRaycastProProbe` alignment work.
- No R3/MessagePipe migration.
- No broad Nhem DI migration.
- No scene/prefab changes.
- No UI/VFX/Animancer gameplay authority changes.

## Decisions

### Decision 1: Extract memory orchestration as a narrow bridge owned by bootstrap orchestration flow
`M0GameplayTickHandler` remains orchestration owner. The extracted collaborator handles only memory interaction/reveal orchestration concerns that are currently embedded in the tick handler.

Rationale:
- Reduces orchestration class size and coupling with low gameplay risk.
- Keeps orchestration order explicit and reviewable.

Alternatives considered:
- Keep logic inline and only reorder methods: rejected (does not reduce coupling).
- Refactor CombatCore or Input first: rejected (higher risk, outside slice scope).

### Decision 2: Preserve existing ownership truth lines with hard constraints
- `MemoryState` remains reveal/collect truth owner.
- `MemoryInteractionService` remains interaction orchestration owner for S3-2.
- Bridge does not own gameplay truth and does not perform acceptance/rejection logic.

Rationale:
- Prevents ownership drift and hidden behavior changes.

### Decision 3: Require parity evidence gate before and after implementation
Implementation phase (separate change apply) must include:
- Focused memory interaction path tests.
- M0 regression check.
- Manual PlayMode checklist for `Interact -> MemoryInteractionService -> MemoryState`.
- Console classification.
- PASS/PARTIAL/FAIL table.

Rationale:
- Keeps extraction verifiable and aligned with evidence-driven workflow.

## Risks / Trade-offs

- **Risk:** Event/tick ordering shifts during extraction.
  **Mitigation:** Keep orchestration order explicitly documented and unchanged in implementation tasks.

- **Risk:** Bridge accidentally absorbs memory truth decisions.
  **Mitigation:** Define bridge as routing-only in spec requirements and test acceptance/rejection ownership.

- **Risk:** Debug/evidence signal quality regresses.
  **Mitigation:** Require equivalent-or-better debug/evidence outputs as acceptance criteria.

- **Trade-off:** Additional collaborator type increases file count.
  **Mitigation:** Accept this to gain clearer boundaries and lower blast radius.

## Migration Plan

1. Approve this OpenSpec proposal set (no code changes yet).
2. Apply change in a separate implementation phase:
   - Introduce bridge contract/class in bootstrap boundary.
   - Move only memory-related orchestration lines from tick handler.
   - Keep external behavior and ownership unchanged.
3. Run focused + regression evidence and classify PASS/PARTIAL/FAIL.
4. If parity fails, rollback to pre-extraction wiring and fix before re-attempt.

Rollback strategy:
- Revert extracted bridge wiring only; do not alter CombatCore/Input/MemoryState behavior.

## Open Questions

- Final implementation naming: `MemoryInteractionTickBridge` vs `MemoryRevealBridge` or split two collaborators.
- Whether debug publishing for memory path remains in tick handler or is partially routed via the bridge while still read-only.
- Whether duplicate interaction behavior should be documented as intentional legacy parity or explicitly marked as deferred cleanup in a later change.
