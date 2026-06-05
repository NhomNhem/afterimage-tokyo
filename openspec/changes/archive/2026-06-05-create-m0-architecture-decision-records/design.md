## Context

The M0 skeleton already established working boundaries for runtime foundation, gameplay truth ownership, presentation read-only behavior, manual DI scoping, and temporary shared contracts. These decisions exist across prior implementation and discussions but are not yet normalized into a lightweight ADR set and a stable technical requirement registry for traceability.

First Playable Duel readiness now depends on a minimal architecture traceability layer that can be evaluated by consistency and gate checks. The requested scope is documentation only and must not introduce runtime behavior changes, scene/prefab edits, UI/VFX implementation, generated DI enablement, or any new gameplay behavior.

## Goals / Non-Goals

**Goals:**
- Record already-made M0 architecture decisions in five ADR files under `docs/architecture/adr/`.
- Create stable M0 technical requirement IDs in `docs/architecture/tr-registry.yaml`.
- Cross-link TR entries to source GDDs, ADR references, implementation references, and test references.
- Preserve unresolved decisions as `Open` so they are trackable without speculative architecture.
- Make outputs directly evaluable for future `/consistency-check` and `/gate-check` workflows.

**Non-Goals:**
- No runtime C# implementation changes.
- No Unity scene/prefab/UI/VFX behavior work.
- No generated DI activation for M0.
- No expansion of M0 scope beyond the decisions and IDs explicitly requested.

## Decisions

1. Represent each architecture boundary cluster as one ADR document.
- Why: This keeps M0 governance lean and reviewable while preserving decision intent.
- Alternative considered: Single monolithic ADR for all decisions.
- Rejected because: It weakens traceability granularity and makes future deltas harder to review.

2. Keep ADR language strictly “recorded decision” oriented.
- Why: The request explicitly requires recording decisions already made, not proposing net-new architecture.
- Alternative considered: Enriching ADRs with speculative future architecture.
- Rejected because: Violates scope guardrails and introduces unapproved design drift.

3. Use stable TR IDs in a single YAML registry with required fields.
- Why: Consistent IDs and structured fields enable automated checks and future change propagation.
- Alternative considered: Free-form markdown list.
- Rejected because: Harder for machine evaluation and consistency tooling.

4. Mark unknowns as `Open` instead of filling assumptions.
- Why: Maintains factual integrity and allows explicit follow-up decisions.
- Alternative considered: Best-guess closure of unresolved items.
- Rejected because: Conflicts with “do not invent architecture” hard rule.

5. Keep implementation and test references as pointers, not execution tasks.
- Why: This change is documentation-only and should not imply runtime modifications.
- Alternative considered: Bundling code/test updates in the same change.
- Rejected because: Out of scope for this proposal.

## Risks / Trade-offs

- [Risk] Registry references may lag real implementation paths as code evolves.
  - Mitigation: Use explicit notes/status fields and update via follow-on OpenSpec deltas.
- [Risk] Some source GDD/test mappings may be incomplete at proposal time.
  - Mitigation: Mark unresolved mappings as `Open` instead of fabricating links.
- [Trade-off] Lean ADRs optimize speed and governance clarity over exhaustive narrative detail.
