# Retrospective: Sprint 5

Period: 2026-06-23 -- 2026-07-04
Generated: 2026-06-12

## Metrics

| Metric | Planned | Actual | Delta |
|--------|--------:|-------:|------:|
| Stories | 9 | 7 delivered, 2 deferred | -2 nice-to-have |
| Must-have stories | 4 | 4 | 0 |
| Should-have stories | 3 | 3 | 0 |
| Completion Rate | 100% must/should, 78% total | 100% must/should, 78% total | Stable core scope |
| Story Points / Effort Days | 7.5 planned | 6.0 delivered | -1.5 deferred |
| Bugs Found | -- | 0 S1/S2 | -- |
| Bugs Fixed | -- | 0 | -- |
| Unplanned Tasks Added | -- | 1 smoke assertion drift fix | +1 |
| Commits | -- | 1 committed in sprint window; multiple local artifacts pending | -- |

## Velocity Trend

| Sprint | Planned | Completed | Rate |
|--------|--------:|----------:|-----:|
| Sprint 3 | 6 stories | 5 complete, 1 optional not started | 100% must-have / 83% total |
| Sprint 4 | 7 stories | 6 complete, 1 backlog | 100% must-have / 86% total |
| Sprint 5 | 9 stories | 7 complete, 2 nice-to-have deferred | 100% must/should / 78% total |

**Trend**: Stable for committed scope. The team continues to finish must-have and should-have work, while nice-to-have items are intentionally deferred instead of being partially implemented.

## What Went Well

- **Core Sprint 5 scope closed cleanly**: S5-1 through S5-7 are complete, including Sprint 4 close-out, dodge displacement, health/combat contract hardening, lock-on policy, and MemoryRaycastProbe carryover sync.
- **Smoke gate moved from warning to PASS**: Full Unity MCP EditMode passed 262/262 and full PlayMode passed 7/7. Manual Game View and performance smoke were also confirmed PASS.
- **QA sign-off was decisive**: `production/qa/qa-signoff-sprint-5-2026-06-12.md` approved the delivered scope with no S1/S2 bugs and no approval conditions.
- **High-priority tech debt was reduced**: S5-4 addressed dodge displacement wiring and S5-5 replaced fragile health/combat string gating with a typed contract.
- **Carryover ambiguity got cleaned up**: S5-7 was recognized as already complete from Sprint 4 evidence, verified again with a focused Unity MCP job, and reconciled in `production/sprint-status.yaml`.
- **Ownership boundaries held**: Combat Core kept dodge authority, Player Locomotion kept movement truth, Health kept reaction/consequence truth, and debug/presentation surfaces stayed observational.

## What Went Poorly

- **Sprint metadata drifted**: S5-7 was complete in its story/evidence but still listed as backlog in `sprint-status.yaml`, which made the next-step flow temporarily misleading.
- **Smoke assertion drift cost time**: `SceneComposition_test` had stale assumptions about Odin serialization and VContainer `UseComponents` registration style. The fix was test-only, but it blocked the smoke gate until corrected.
- **Tooling workflow was uneven**: `team-qa` and retrospective workflows expected `AskUserQuestion`/subagents, which were not available in this turn. Reports had to be produced directly from artifacts.
- **Sprint plan file lagged behind reality**: `production/sprints/sprint-5.md` still says QA plan is TBD and checklist items are unchecked, while actual QA artifacts and `sprint-status.yaml` show completion.
- **Nice-to-have work stayed deferred**: S5-8 Parry/Counter Visual Feedback and S5-9 HDRP material enum cleanup remain unresolved, so polish/console hygiene debt still exists.

## Blockers Encountered

| Blocker | Duration | Resolution | Prevention |
|---------|----------|------------|------------|
| SceneComposition assertion drift | During smoke gate | Updated assertions to match Odin `serializationData` and `UseComponents(... AddInstance(...))`; reran full EditMode/PlayMode | Prefer helper methods for scene serialized-field assertions and update smoke tests alongside composition refactors |
| S5-7 sprint-status mismatch | During Sprint 5 close-out | `/story-done` sync marked S5-7 done, cleared blocker, and added fresh focused test evidence | Add a status reconciliation check before `/help` and QA sign-off |
| Team QA subagent flow unavailable | QA sign-off turn | Produced sign-off directly from sprint files, smoke report, QA evidence, and Unity MCP results | Keep direct artifact-based fallback in QA skills documented |

## Estimation Accuracy

| Task | Estimated | Actual | Variance | Likely Cause |
|------|----------:|-------:|---------:|--------------|
| S5-1 Sprint 4 Smoke Check | 0.5d | Complete | On track | Evidence-based QA story with existing Sprint 4 artifacts. |
| S5-2 Sprint 4 QA Sign-Off | 1.0d | Complete | On track | Documentation-only sign-off. |
| S5-3 Sprint 4 Retrospective | 0.5d | Complete | On track | Documentation-only retrospective. |
| S5-4 Wire M0 Dodge Displacement | 2.0d | Complete | Slightly higher complexity | Runtime config serialization and tick-handler NRE follow-ups emerged during review. |
| S5-5 Harden Health-Combat Contract | 1.0d | Complete | On track | Narrow typed-contract hardening with focused EditMode coverage. |
| S5-6 LockOn Toggle Policy | 0.5d | Complete | On track | Config/Data decision, no runtime changes. |
| S5-7 MemoryRaycastProbe Alignment | 0.5d | Complete via carryover sync | Lower than planned implementation | Story was already implemented in Sprint 4; Sprint 5 work was reconciliation and focused verification. |
| S5-8 Parry/Counter Visual Feedback | 1.0d | Deferred | -1.0d | Nice-to-have polish intentionally not pulled into delivered scope. |
| S5-9 Resolve HDRP Material Enum Error | 0.5d | Deferred | -0.5d | Nice-to-have cleanup intentionally left for later. |

**Overall estimation accuracy**: Good for must-have and should-have scope. Sprint 5 delivered 6.0 of 7.5 planned effort days; the remaining 1.5 days were explicitly deferred nice-to-have work.

## Carryover Analysis

| Task | Original Sprint | Times Carried | Reason | Action |
|------|----------------|--------------:|--------|--------|
| S4-7 / S5-7 MemoryRaycastProbe Alignment | Sprint 4 | 1 | Story was complete but Sprint 5 status metadata was stale | Completed and reconciled in Sprint 5 |
| S5-8 Parry/Counter Visual Feedback | Sprint 5 | 1 | Nice-to-have polish; not required for QA approval | Replan only if next sprint focuses on M0 feel/readability polish |
| S5-9 Resolve HDRP Material Enum Error | Sprint 5 | 1 | Nice-to-have cleanup; non-blocking for delivered scope | Replan as console hygiene / asset pipeline cleanup if stricter gates are desired |

## Technical Debt Status

- Current authored-scope TODO count: 9
- Current authored-scope FIXME count: 5
- Current authored-scope HACK count: 5
- Previous retro baseline: ~5 owned project/docs combined markers
- Trend: Needs normalization. The current scan uses broader authored paths than Sprint 4, so the count should not be treated as a direct apples-to-apples increase.
- High-value debt reduced: dodge displacement wiring and health/combat contract hardening are complete.
- Remaining notable debt: Parry/Counter visual feedback polish, HDRP material enum/editor warning cleanup, and test/status tooling consistency.

## Previous Action Items Follow-Up

| Action Item (from Sprint 4) | Status | Notes |
|-----------------------------|--------|-------|
| Implement S5-4 Wire M0 Dodge Displacement | Done | S5-4 completed with PlayMode evidence and smoke PASS. |
| Run `/test-setup` to scaffold test directory structure | Not Started | Unity tests exist under `Assets/_Project/Tests`, but root `tests/` is still absent for generic smoke tooling. |
| Complete S4-5 architecture review or formally close it | Not Confirmed | Sprint 5 focused on S5-4 through S5-7 closure; S4-5 was not surfaced in current sprint status. |
| Keep tech debt focused on dodge displacement and health contract first | Done | S5-4 and S5-5 directly addressed those items. |

## Action Items for Next Iteration

| # | Action | Owner | Priority | Deadline |
|---|--------|-------|----------|----------|
| 1 | Reconcile sprint plan markdown with `sprint-status.yaml` and QA artifacts before final archive/commit | producer | High | Before Sprint 6 planning |
| 2 | Decide whether Sprint 6 pulls S5-8 visual feedback polish or defers it to a later M0 feel pass | lead-programmer / technical-artist | Medium | Sprint 6 planning |
| 3 | Decide whether S5-9 HDRP enum cleanup is worth a dedicated console-hygiene slice | engine-programmer | Medium | Sprint 6 planning |
| 4 | Standardize TODO/FIXME/HACK counting paths so retrospectives compare the same baseline each sprint | dev | Low | Sprint 6 close-out |
| 5 | Add an artifact-based fallback note to QA/retro workflows when subagents or AskUserQuestion are unavailable | process owner | Low | Before next QA cycle |

## Process Improvements

- **Run a status reconciliation before close-out**: Compare story files, `sprint-status.yaml`, smoke reports, and QA sign-off before asking "what next?".
- **Keep smoke tests aligned with composition style**: When scene composition changes from direct serialized fields to Odin `serializationData` or VContainer `UseComponents`, update scene assertion helpers in the same slice.
- **Treat nice-to-have deferral as a decision, not residue**: S5-8 and S5-9 were correctly deferred, but they should enter the next sprint as explicit candidates or be archived out of scope.

## Summary

Sprint 5 was successful. The delivered scope closed with smoke PASS, QA APPROVED, no S1/S2 bugs, and the highest-priority M0 tech debt reduced. The single most important process fix is to reconcile sprint metadata before close-out so completed work does not masquerade as backlog and confuse the next-step flow.
