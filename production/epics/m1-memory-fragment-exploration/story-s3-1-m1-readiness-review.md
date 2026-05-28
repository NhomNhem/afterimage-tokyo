# Story S3-1: [Review] M1 Readiness / Scope Review

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Planned
> **Layer**: QA / Documentation
> **Type**: Review
> **Estimate**: 0.5d
> **Sprint**: Sprint 3
> **Last Updated**: 2026-05-28

## Context

M0 First Playable Duel is complete with notes and Sprint 2 Must-Have path is closed with notes.
Before implementing S3-2, this story validates whether the current M0 foundation is ready for a small M1 exploration-memory slice.

**Hard Scope Boundary**:
- Docs/review only.
- No gameplay code changes.
- No Unity submodule changes.
- No OpenSpec unless required by discovered behavior/system contract changes.

## Goal

Review M1 readiness across existing systems, ownership boundaries, and scope risk so Sprint 3 can start implementation with minimal ambiguity.

## Review Questions

1. Which M0 systems can be reused for M1?
2. Which new systems are needed?
3. What ownership boundaries apply?
4. What must remain out of scope?
5. What risks exist before S3-2?
6. Does S3-2 require OpenSpec?
7. Should Nhem DI V1 be used for new M1 services?
8. Which data belongs in ScriptableObject definitions?
9. Should Animancer be deferred to S3-4?

## Must-Evaluate Areas

- Player Locomotion readiness for exploration movement
- Input Mapping readiness for Interact action
- Memory State readiness for reveal/collect
- Memory VFX Response readiness for presentation response
- Debug Overlay usefulness for evidence
- Scene/map readiness
- UI readiness for interaction prompt and memory log
- Nhem DI/VContainer registration readiness
- ScriptableObject definition/config readiness
- Animancer presentation-only boundary
- Save/Profile out of scope unless explicitly required

## Expected New M1 Boundaries

- `MemoryFragment` (data + interaction target concept)
- `MemoryInteractionService` (use-case orchestration)
- `InteractionSensor` (proximity/candidate detection)
- `RuntimeMemoryLogStore` (runtime log read model)

## Deliverables

1. Story file (this file):
   `production/epics/m1-memory-fragment-exploration/story-s3-1-m1-readiness-review.md`
2. Evidence file:
   `production/qa/evidence/m1-readiness-review-2026-05-28.md`

## Acceptance Criteria

- [ ] Review identifies reusable M0 systems.
- [ ] Review identifies new M1 boundaries:
  - `MemoryFragment`
  - `MemoryInteractionService`
  - `InteractionSensor`
  - `RuntimeMemoryLogStore`
- [ ] Review lists non-goals clearly.
- [ ] Review recommends whether S3-2 requires OpenSpec.
- [ ] Review states Nhem DI adoption level.
- [ ] Review does not claim implementation work.

## Out of Scope

- S3-2 implementation
- New gameplay runtime code
- Scene/prefab/tooling implementation changes
- Save/Profile system design
- Broad RPG expansion

## Notes

If this review discovers required contract changes across ownership boundaries, open a small OpenSpec for S3-2 before coding.
