## Context

M0 foundations are verified with notes, and Sprint 3 shifts toward a small player-facing M1 slice.
This change introduces a narrow interaction loop around Memory Fragments while preserving established ownership boundaries:
- Input only emits raw intent.
- Use-case orchestration stays in application/service boundary.
- Memory truth stays in MemoryState.
- UI/VFX/Audio/Animancer remain presentation-only.

Key constraints:
- Use Nhem DI/VContainer for new service-level systems only.
- Do not migrate or refactor existing M0 systems unless strictly required.
- No service locator/FindObjectOfType/Resources.Load.
- ScriptableObject stores static fragment definition only, never runtime collected state.

## Goals / Non-Goals

**Goals:**
- Provide a minimal interaction flow: near fragment -> press Interact -> request reveal/collect -> accepted/rejected outcome.
- Add explicit boundaries for:
  - `MemoryFragment`
  - `InteractionSensor`
  - `MemoryInteractionService`
  - runtime memory log read-model boundary
- Produce evidence-friendly state signals for verification.

**Non-Goals:**
- Full inventory, save/profile persistence, quest/dialogue systems, lore database, RPG progression.
- Combat timing/results changes or enemy lifecycle changes.
- Camera refactor or Animancer-owned interaction truth.
- Broad system migrations.

## Decisions

1. Interaction orchestration SHALL be owned by `MemoryInteractionService`.
   - Rationale: keeps input/raw scene detection decoupled from memory truth rules.
   - Alternative considered: direct component-to-MemoryState call from fragment; rejected to avoid ownership leakage and hard coupling.

2. `MemoryFragmentDefinition` ScriptableObject SHALL hold static authored metadata only.
   - Includes: stable id, title, short text, icon, reveal clip/sfx refs, presentation config refs.
   - Excludes: runtime revealed/collected state.
   - Rationale: maintain deterministic data ownership and avoid persistence leakage.

3. Duplicate interaction SHALL be handled safely via MemoryState-backed decision path.
   - Rationale: state truth remains centralized and testable.
   - Alternative considered: fragment-local duplicate cache; rejected because runtime truth would split.

4. Nhem DI/VContainer registration for new M1 services SHALL be explicit/manual in scene LifetimeScope.
   - Primitive constructor params SHALL use explicit factory/config injection.
   - Rationale: consistent with current M0 DI guardrails.

5. Animancer usage in S3-2 is optional and presentation-only.
   - Rationale: keep S3-2 focused on interaction truth.
   - Defer richer presentation behavior to S3-4.

## Risks / Trade-offs

- [Risk] Interaction scope creeps into inventory/save/progression.
  → Mitigation: enforce non-goals in spec/tasks; reject out-of-scope fields and flows.

- [Risk] Runtime truth drifts into UI/VFX/Animancer.
  → Mitigation: require evidence hooks that show MemoryState acceptance/rejection as authority.

- [Risk] Scene wiring becomes hidden dependency.
  → Mitigation: explicitly list and justify any scene/prefab changes in evidence/tasks.

- [Risk] Interact action path ambiguity in input mapping.
  → Mitigation: treat Interact intent as explicit, verifiable input route in requirements/tests.

## Migration Plan

1. Add spec + task contract for M1 interaction slice.
2. Implement S3-2 with minimal runtime changes and focused tests.
3. Capture evidence table + console classification + scene dirtiness classification.
4. Rollback strategy:
   - Revert new interaction service/fragment wiring and ScriptableObject definitions.
   - Do not revert unrelated M0 systems.

## Open Questions

- Should runtime memory log read-model start in S3-2 as a thin store contract or wait fully for S3-5 UI story?
- Is a define-gated debug trigger needed for deterministic evidence of duplicate interaction, or can manual flow reliably cover it?
