# Story S4-5: [Architecture] Extract M0 Gameplay Tick Memory Bridge Proposal Review

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: Architecture / Review
> **Type**: Integration
> **Estimate**: 0.5d
> **Sprint**: Sprint 4
> **Dependencies**: ADR-0001
> **Manifest Version**: 2026-05-15
> **Last Updated**:

## Context

Sprint 4 includes an ADR-guided cleanup lane for `M0GameplayTickHandler`. Before implementation, the proposal review story verifies that the OpenSpec change for extracting memory-related tick orchestration is narrow, behavior-preserving, and aligned with ADR-0001.

Design trace:
- `production/sprints/sprint-4.md`: S4-5 reviews OpenSpec `extract-m0-gameplay-tick-memory-bridge`.
- `production/qa/qa-plan-sprint-4-2026-06-05.md`: S4-5 requires strict OpenSpec validation and proposal/design/tasks review.
- `docs/architecture/adr-0001-m0-scene-composition-and-runtime-boundaries.md`: governs scene/bootstrap/runtime boundary cleanup.
- `docs/architecture/control-manifest.md`: Bootstrap owns orchestration and global config only; gameplay truth must remain scoped and explicit.

Technical requirement trace:
- `openspec/specs/m0-gameplay-tick-memory-bridge/spec.md`: memory interaction/reveal orchestration extraction must preserve prompt, reveal feedback, runtime memory log, and M0/M1 memory path parity.

ADR note:
- Governing ADR: ADR-0001.
- Related guardrails: ADR-0002 for gameplay truth ownership, ADR-0003 for presentation-only observers, ADR-0004 for manual VContainer registration.

## Goal

Review and approve or defer the `extract-m0-gameplay-tick-memory-bridge` OpenSpec proposal before any implementation begins.

## Acceptance Criteria

- [x] OpenSpec `extract-m0-gameplay-tick-memory-bridge` validates with `--strict`, or the validation blocker is recorded.
- [x] Proposal, design, tasks, and spec delta are reviewed for ADR-0001 alignment.
- [x] Scope remains memory interaction/reveal orchestration only.
- [x] No CombatCore, Input architecture, MemoryState truth, scene/prefab, R3/MessagePipe, or broad Nhem DI migration is included.
- [x] Behavior-preserving verification requirements are present for S3-2 interaction, S3-3 prompt, S3-4 reveal feedback, and S4-2 runtime memory log.
- [x] Decision is recorded: approved for implementation, deferred, or needs revision.
- [x] No runtime implementation is performed in this review story.

## Out of Scope

- Implementing `M0MemoryInteractionTickBridge`
- Runtime code changes
- Scene or prefab changes
- CombatCore/Input/MemoryState behavior changes
- Prompt, reveal feedback, or runtime memory log feature changes
- MemoryRaycastProProbe alignment
- Broad Nhem DI migration
- R3 or MessagePipe migration

## Implementation Notes

- This story is proposal review only.
- If the OpenSpec change is already implemented or archived, record that fact in completion notes rather than reimplementing anything.
- If the proposal has drifted from ADR-0001, update or defer the proposal before implementation.

## Control Manifest Notes

- Bootstrap owns scene orchestration and global config only.
- Gameplay truth must remain in pure services and scoped runtime composition.
- Manual VContainer registration remains the M0 strategy.
- No global singleton truth, service locator, generated DI migration, or broad lookup.

## Engine Notes

N/A - no Unity API implementation should occur in this review story.

## Performance Budget

No runtime performance impact expected. This story is architecture review only.

## QA Test Cases

*Written from `production/qa/qa-plan-sprint-4-2026-06-05.md`. The implementer verifies against these cases; do not invent new closure criteria during execution.*

- **AC-1**: OpenSpec validates strict.
  - Given: the OpenSpec change exists.
  - When: `openspec validate extract-m0-gameplay-tick-memory-bridge --strict` is run.
  - Then: validation passes or a blocker is recorded with next action.
  - Edge cases: change already archived, missing active change, stale main spec.

- **AC-2**: ADR-0001 alignment is reviewed.
  - Given: proposal/design/tasks/spec are available.
  - When: the reviewer checks scope.
  - Then: the change remains behavior-preserving and limited to memory tick orchestration.
  - Edge cases: accidental CombatCore/Input scope, DI migration creep, scene/prefab work.

- **AC-3**: Implementation decision is recorded.
  - Given: review is complete.
  - When: the story closes.
  - Then: the decision says approved, deferred, needs revision, or already implemented/archived with evidence.
  - Edge cases: proposal superseded by a later archived OpenSpec change.

## Test Evidence

**Story Type**: Integration / Architecture Review

Required evidence:
- OpenSpec validation output or archived-change validation note.
- Review decision note.
- Confirmation that no runtime implementation occurred in this story.

Expected evidence:
- Link to `openspec/changes/archive/2026-06-06-extract-m0-gameplay-tick-memory-bridge` if already archived.
- Link to `production/qa/evidence/extract-m0-gameplay-tick-memory-bridge-verification-2026-06-06.md` if implementation has already occurred.

**Status**: [x] Created — `production/qa/evidence/s4-5-m0-gameplay-tick-memory-bridge-review-2026-06-16.md`

Archived change: `openspec/changes/archive/2026-06-06-extract-m0-gameplay-tick-memory-bridge/`
Implementation evidence: `production/qa/evidence/extract-m0-gameplay-tick-memory-bridge-verification-2026-06-06.md`

## Dependencies

- Depends on: ADR-0001 Accepted
- Unlocks: S4-6 Implement MemoryInteractionTickBridge Thin Slice
