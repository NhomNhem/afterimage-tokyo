# Story S4-3: [QA] Runtime Memory Log Smoke

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: QA / Integration
> **Type**: Integration
> **Estimate**: 0.5d
> **Sprint**: Sprint 4
> **Dependencies**: S4-2
> **Manifest Version**: 2026-05-15
> **Last Updated**:

## Context

S4-2 implemented the runtime memory log placeholder after the accepted M1 Memory Fragment interaction path. This story performs the smoke pass that confirms the whole tester-facing path still reads correctly:

`Prompt -> Interact -> Reveal feedback -> Runtime memory log`

Design trace:
- `production/sprints/sprint-4.md`: S4-3 verifies the runtime memory log smoke path after S4-2.
- `production/qa/qa-plan-sprint-4-2026-06-05.md`: defines S4-3 as Integration / QA with no new unit tests required unless a blocker is found.
- `production/qa/evidence/s4-2-runtime-memory-log-placeholder-verification-2026-06-05.md`: confirms S4-2 implementation and manual baseline.
- `openspec/specs/runtime-memory-log-placeholder/spec.md`: runtime memory log remains read-only, placeholder-scoped, and downstream of memory truth.

Technical requirement trace:
- `TR-M0-MEMORY-001`: Memory State owns reveal acceptance and memory-side consequence truth.
- `TR-M0-INPUT-001`: Input Mapping owns raw input truth and emits intent only.
- `TR-M0-DEBUG-001`: Debug Overlay owns grouping and presentation only; it does not own gameplay truth.

ADR note:
- No ADR applies directly to this QA smoke story.
- ADR-0003 presentation-boundary rules apply through the control manifest: UI observes read-only snapshots/context and must not mutate gameplay state.

## Goal

Capture smoke evidence that the accepted M1 memory interaction path still presents prompt, reveal feedback, and exactly one runtime memory log entry, with duplicate/spam behavior and console output classified.

## Acceptance Criteria

- [x] Prompt -> Interact -> Reveal feedback -> runtime log path is verified with PASS/PARTIAL/FAIL evidence.
- [x] Duplicate/spam Interact after accepted reveal does not replay the banner or duplicate the runtime log entry.
- [x] S4-2 focused automated checks are reused or explicitly linked; no new automated tests are required unless smoke finds a regression.
- [x] Console output is classified as blocking, acceptable, known external, or unrelated.
- [x] Dirty scene/prefab/assets status is checked and any unrelated dirt is explicitly classified.
- [x] Evidence records setup, command/tooling used, timestamp, pass/fail status, and any manual limitations.
- [x] Runtime memory log remains read-only presentation/read-model state and does not own memory truth.
- [x] No runtime feature, scene, prefab, or gameplay behavior is changed by this story unless a smoke blocker is found and separately approved.

## Out of Scope

- Runtime memory log implementation changes
- New UI, journal, inventory, quest, lore, save/profile, progression, dialogue, or codex behavior
- MemoryState acceptance/rejection policy changes
- MemoryInteractionService interaction semantics changes
- Prompt or reveal feedback feature expansion
- CombatCore, EnemyIntent, TargetContext, Camera, PlayerLocomotion, Health, or Encounter behavior changes
- MemoryInteractionTickBridge extraction
- MemoryRaycastProProbe alignment
- Broad Nhem DI migration

## Implementation Notes

- Prefer a lean smoke report only.
- Reuse S4-2 automated evidence where it already proves read-only log behavior and duplicate prevention.
- If PlayMode cannot be sampled because of Unity tooling, record the blocker and fallback evidence instead of silently passing.
- Keep all smoke observations evidence-only unless a blocking regression is found and separately triaged.

## Control Manifest Notes

- QA evidence must not change gameplay truth ownership.
- Presentation and Debug Overlay remain read-only observers.
- MemoryState owns reveal/collect truth.
- MemoryInteractionService owns memory interaction orchestration.
- No direct Unity debug logging, service locator, `FindObjectOfType`, or `Resources.Load` should be introduced.

## Engine Notes

- Unity 6000.3.x project conventions apply.
- Use Unity Test Runner or Unity MCP where available.
- Separate PowerShell/profile noise and package/editor warnings from Unity compile/test failures.

## Performance Budget

No runtime performance impact expected. This is a smoke/evidence story and should not add runtime behavior.

## QA Test Cases

*Written from `production/qa/qa-plan-sprint-4-2026-06-05.md`. The implementer verifies against these cases; do not invent new closure criteria during execution.*

- **AC-1**: Prompt -> Interact -> Reveal feedback -> Runtime log.
  - Given: the M1 memory fragment scene/path is loaded and the player can approach an eligible fragment.
  - When: the player approaches the fragment and presses Interact.
  - Then: the prompt appears, interaction is accepted, reveal feedback appears once, and one runtime memory log entry appears.
  - Edge cases: missing scene path, prompt unavailable, accepted interaction not routed, runtime log UI hidden.

- **AC-2**: Duplicate/spam behavior remains safe.
  - Given: an accepted reveal already created a runtime memory log entry.
  - When: Interact is pressed repeatedly afterward.
  - Then: the reveal banner does not replay and no duplicate runtime memory log entry is appended for the same outcome.
  - Edge cases: repeated frames, duplicate snapshots, already collected fragment.

- **AC-3**: Console output is classified.
  - Given: smoke execution produces console output.
  - When: evidence is written.
  - Then: blocking errors, acceptable warnings, known external warnings, and unrelated editor/package messages are separated.
  - Edge cases: NDF analyzer warnings, material drawer warnings, PowerShell profile noise.

- **AC-4**: Dirty asset status is classified.
  - Given: the working tree may contain pre-existing unrelated Unity/vendor dirt.
  - When: smoke evidence is captured.
  - Then: scene/prefab/runtime files touched by smoke are identified, and unrelated dirt is explicitly left out of scope.
  - Edge cases: Unity auto-refresh meta changes, vendor package churn, generated test artifacts.

## Test Evidence

**Story Type**: Integration / QA

Required evidence:
- Smoke evidence file: `production/qa/evidence/s4-3-runtime-memory-log-smoke-verification-2026-06-07.md`
- Link to S4-2 automated/manual evidence.
- PASS/PARTIAL/FAIL table for prompt, Interact, reveal feedback, runtime log, duplicate/spam behavior, console classification, and dirty asset classification.

**Status**: [x] Created — `production/qa/evidence/s4-3-runtime-memory-log-smoke-verification-2026-06-07.md`

## Dependencies

- Depends on: S4-2 Complete
- Unlocks: S4-4 Decide S3-5 Carryover Closure
