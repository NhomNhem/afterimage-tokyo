# Story S4-2: [UI] Runtime Memory Log Placeholder

> **Epic**: M1 Memory Fragment Exploration Slice
> **Status**: Complete
> **Layer**: UI / Presentation
> **Type**: UI
> **Estimate**: 1.0d
> **Sprint**: Sprint 4
> **Dependencies**: S3-2, S3-3, S3-4, S4-1
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-06

## Context

Sprint 3 proved the first M1 exploration-memory loop:

`approach Memory Fragment -> prompt appears -> press Interact -> MemoryInteractionService -> MemoryState accepted -> reveal feedback appears once`

S4-1 captured fresh baseline test evidence before adding new runtime UI. This story carries forward the Sprint 3 S3-5 placeholder scope into Sprint 4: add a minimal runtime memory log entry after an accepted Memory Fragment reveal/collect outcome.

The runtime memory log is a read-only placeholder. It should help testers see that a fragment was revealed or collected, but it must not become a full journal, inventory, quest log, save/profile system, lore database, progression tracker, or gameplay authority.

Design trace:
- `design/gdd/systems-index.md`: HUD / Player-Facing UI is downstream presentation and depends on combat, targeting, and progression systems; presentation systems may observe gameplay state but must not own gameplay truth.
- `design/gdd/memory-state.md`: `Memory State` owns reveal request acceptance/rejection, memory response state, and memory debug truth.
- `production/qa/evidence/s3-2-memory-fragment-interaction-verification-2026-05-28.md`: verifies the S3-2 interaction route and MemoryState ownership that this story must observe.
- `production/qa/evidence/s3-3-interaction-prompt-placeholder-verification-2026-06-04.md`: verifies the prompt remains separate from Interact execution and MemoryState truth.
- `production/qa/evidence/s3-4-memory-reveal-vfx-audio-placeholder-verification-2026-06-05.md`: verifies accepted reveal feedback appears once and duplicate/spam interaction does not replay feedback.
- `production/qa/evidence/s4-1-fresh-unity-test-runner-evidence-2026-06-05.md`: records the fresh Sprint 4 baseline before this runtime UI work.

Technical requirement trace:
- `TR-M0-MEMORY-001`: Memory State owns reveal acceptance and memory-side consequence truth.
- `TR-M0-INPUT-001`: Input Mapping owns raw input truth and emits intent only.
- `TR-M0-DEBUG-001`: Debug Overlay owns grouping and presentation only; it does not own gameplay truth.

ADR note:
- No ADR applies directly to this placeholder UI story.
- ADR-0003 presentation-boundary rules apply through the control manifest: UI observes read-only snapshots/context and must not mutate gameplay state.
- ADR-0001 is related future context for orchestration decomposition only; this story does not implement refactor work.

OpenSpec:
- Required before implementation.
- Suggested change name: `add-m1-runtime-memory-log-placeholder`

## Goal

Show a minimal runtime memory log entry after an accepted Memory Fragment reveal/collect outcome, while keeping the log read-only, placeholder-scoped, and downstream of `MemoryInteractionService`, `MemoryState`, and existing reveal feedback.

## Acceptance Criteria

- [x] Accepted Memory Fragment reveal/collect appends exactly one visible runtime memory log entry.
- [x] Runtime memory log entry does not appear when there is no eligible fragment.
- [x] Runtime memory log entry does not appear for MemoryState rejected reveal outcomes.
- [x] Duplicate or spam Interact after reveal/collection does not create duplicate log entries.
- [x] Log entry content is minimal and placeholder-scoped, such as a fragment label plus a short revealed/collected state.
- [x] Runtime log observes accepted interaction/reveal context or an approved read-only memory snapshot; it does not call MemoryState mutation APIs.
- [x] Runtime log does not call `MemoryInteractionService` command paths, fragment mutation paths, Unity InputAction callbacks, or Interact execution paths.
- [x] Runtime log remains presentation/read-model state only and does not create inventory, quest, journal progression, save/profile, dialogue, lore database, or narrative branching behavior.
- [x] S3-2 interaction behavior, S3-3 prompt behavior, and S3-4 reveal feedback behavior remain preserved.
- [x] UI/VFX/audio/Animancer remain downstream presentation only and do not own memory truth.
- [x] No service locator, `FindObjectOfType`, `Resources.Load`, or direct Unity debug logging is introduced.
- [x] Focused EditMode tests cover read-only log behavior, duplicate prevention, and ownership guardrails.
- [x] Manual PlayMode evidence confirms prompt -> Interact -> reveal feedback -> runtime log entry appears once.
- [x] Console output has no new S4-scope errors/exceptions; warnings are classified.

## Out of Scope

- Full journal, inventory, quest, lore, codex, save/profile, or progression UI
- Narrative memory database, clue tracking, contradiction tracking, district reinterpretation, or truth restoration framework
- Changing MemoryState reveal/collect truth
- Changing MemoryInteractionService interaction semantics
- Changing InputAction callback ownership or raw input routing
- Changing S3-3 interaction prompt behavior
- Changing S3-4 reveal feedback playback behavior
- Changing CombatCore, EnemyIntent, TargetContext, Camera, PlayerLocomotion, Health, or Encounter behavior
- MemoryInteractionTickBridge extraction
- MemoryRaycastProProbe alignment
- R3/MessagePipe migration
- Broad Nhem DI migration
- Scene/prefab/content edits unless separately approved for minimal UI wiring

## Implementation Notes

- Prefer a narrow presentation/read-model component for runtime memory log state.
- The log may observe an accepted interaction snapshot, `M0MemoryVFXResponse`/memory response snapshot, or another approved read-only bridge produced by the implementation OpenSpec.
- The log must deduplicate by fragment identity or accepted reveal identity so repeated Interact after collection does not append again.
- If display data is missing, use a placeholder-safe fallback label and do not crash.
- Keep the visible UI small and development-placeholder quality. This is not final HUD or journal design.
- Do not use service locator, `FindObjectOfType`, `Resources.Load`, direct Unity debug logging, or presentation-driven gameplay mutation.

## Control Manifest Notes

- Presentation systems must observe gameplay truth as read-only snapshots or context.
- UI must not mutate gameplay state.
- Input remains raw intent only.
- MemoryState owns reveal/collect truth.
- MemoryInteractionService owns interaction orchestration for the M1 fragment path.
- Debug/UI readouts remain presentation-only and must not infer or repair gameplay truth.

## Engine Notes

- Unity 6000.3.x project conventions apply.
- UI implementation should follow the existing project UI Toolkit/debug overlay/runtime UI path unless the OpenSpec explicitly approves a different placeholder surface.
- Verify UI Toolkit or overlay APIs against existing project usage before implementation.

## Performance Budget

No meaningful runtime performance impact expected. The runtime log should append only on accepted reveal/collect events or equivalent read-only snapshot changes. It must not introduce broad scene scans, heavy per-frame allocations, or expensive UI rebuilds in the hot gameplay loop.

## QA Test Cases

*Written from `production/qa/qa-plan-sprint-4-2026-06-05.md`. The implementer verifies against these cases; do not invent new closure criteria during execution.*

- **AC-1**: Accepted memory reveal appends a visible runtime memory log entry.
  - Given: the player is near an eligible Memory Fragment and Interact is routed through the existing S3-2 path.
  - When: MemoryInteractionService produces an accepted reveal/collect outcome.
  - Then: one visible runtime memory log entry appears.
  - Edge cases: missing fragment display name, delayed reveal feedback, UI disabled in authoring.

- **AC-2**: Runtime log is read-only presentation/read-model state and does not mutate MemoryState.
  - Given: the runtime log component observes memory interaction or response context.
  - When: the log updates after an accepted reveal.
  - Then: source checks/tests show the log does not call MemoryState mutation APIs or decide reveal acceptance.
  - Edge cases: null snapshot, no prior accepted reveal, missing MemoryState reference.

- **AC-3**: Duplicate or spam Interact after reveal does not create duplicate entries.
  - Given: a Memory Fragment has already produced an accepted reveal/log entry.
  - When: Interact is pressed repeatedly afterward.
  - Then: no additional entry is appended for the same accepted fragment outcome.
  - Edge cases: repeated frames, duplicate snapshots, already collected fragment.

- **AC-4**: Log entry content is minimal and placeholder-scoped.
  - Given: a log entry is rendered.
  - When: the player or tester reads the runtime log.
  - Then: the entry shows only a concise fragment label/state and does not expose journal/progression/lore systems.
  - Edge cases: long fragment IDs, missing display label, multiple entries if later authored.

- **AC-5**: UI/VFX/audio/Animancer remain downstream presentation only.
  - Given: the runtime log is implemented alongside S3-4 reveal feedback.
  - When: ownership guardrails are checked.
  - Then: no presentation code owns Interact execution, MemoryState truth, or MemoryInteractionService command behavior.
  - Edge cases: tempting reuse of existing overlay adapter, direct InputAction callback, direct fragment mutation.

- **AC-6**: Forbidden APIs are not introduced.
  - Given: changed runtime files are scanned.
  - When: pre-commit or focused source checks run.
  - Then: no `FindObjectOfType`, `Resources.Load`, service locator, or direct Unity debug logging appears in owned runtime code.
  - Edge cases: test-only code, vendor/package code, comments in docs.

- **Manual PlayMode Check**: Prompt -> Interact -> Reveal feedback -> Runtime log.
  - Setup: load the M1 memory fragment scene/path, approach the fragment, and confirm the S3-3 prompt appears.
  - Verify: press Interact, confirm accepted reveal feedback appears once, and confirm one runtime memory log entry appears.
  - Pass condition: duplicate/spam Interact after reveal does not replay the banner or duplicate the log entry.

## Test Evidence

**Story Type**: UI

Required evidence:
- Focused EditMode test file: `afterimage-tokyo/Assets/_Project/Tests/EditMode/M1RuntimeMemoryLogPlaceholderTests.cs`
- Manual evidence file: `production/qa/evidence/s4-2-runtime-memory-log-placeholder-verification-2026-06-05.md`
- Console classification.
- PASS/PARTIAL/FAIL table covering accepted log append, duplicate suppression, ownership boundaries, and dirty asset classification.

Expected automated coverage:
- Accepted reveal appends one entry.
- No eligible/rejected reveal appends no entry.
- Duplicate/spam accepted context does not duplicate entries.
- Null or missing display data does not crash.
- Source/ownership guardrails prevent MemoryState mutation, Interact ownership, and forbidden APIs.

**Status**: [x] Created and passing

## Dependencies

- Depends on: S3-2 Complete, S3-3 Complete, S3-4 Complete, S4-1 Complete
- Unlocks: S4-3 Runtime Memory Log Smoke, S4-4 Decide S3-5 Carryover Closure, S4-7 MemoryRaycastProProbe Alignment Spike

## Completion Notes

**Completed**: 2026-06-06
**Criteria**: 14/14 passing
**Deviations**: None
**Test Evidence**: `production/qa/evidence/s4-2-runtime-memory-log-placeholder-verification-2026-06-05.md`
**Automated Verification**:
- Compile smoke: `dotnet build afterimage-tokyo.sln --no-restore` PASS with 0 compile errors.
- Focused S4-2 EditMode: Unity MCP job `fe5c24fa20aa48f5962d157bcfbf5f09`, 6/6 PASS.
- S3-3/S3-4 regression EditMode: Unity MCP job `a78b89164baf440a8ef415795ab2786d`, 9/9 PASS.
- OpenSpec `add-m1-runtime-memory-log-placeholder`: 31/31 tasks complete and strict validation PASS.
**Manual Verification**:
- Prompt -> Interact -> reveal feedback -> runtime log entry: PASS.
- Duplicate/spam Interact does not replay banner or duplicate runtime log entry: PASS.
**Console Classification**: No S4-scope compile/test blocker. External/non-scope Unity/package/Test Runner console entries are classified in the evidence file.
**Code Review**: Skipped in lean mode; focused tests, source guardrails, manual PlayMode confirmation, and evidence review recorded.
**Next Recommended**: `production/epics/m1-memory-fragment-exploration/story-s4-3-runtime-memory-log-smoke.md`
