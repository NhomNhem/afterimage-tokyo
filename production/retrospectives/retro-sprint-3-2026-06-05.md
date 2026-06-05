# Retrospective: Sprint 3

Period: 2026-06-13 -- 2026-06-26
Generated: 2026-06-05

## Metrics

| Metric | Planned | Actual | Delta |
|--------|--------:|-------:|------:|
| Stories | 6 | 5 complete | -1 optional |
| Must-have stories | 5 | 5 | 0 |
| Completion Rate | 100% must-have / 83% total | 100% must-have / 83% total | Stable |
| Story Points / Effort Days | 6.0 | 5.0 completed | -1.0 optional |
| Bugs Found | -- | 0 | -- |
| Bugs Fixed | -- | 0 | -- |
| Unplanned Tasks Added | -- | 0 | -- |
| Commits | -- | 23 | -- |

## Velocity Trend

| Sprint | Planned | Completed | Rate |
|--------|--------:|----------:|-----:|
| Sprint 2 | 10 | 5 must-have complete, optional classified/deferred | 100% must-have |
| Sprint 3 | 6 | 5 complete, 1 optional not started | 100% must-have / 83% total |

**Trend**: Stable. The team continues to complete the must-have path while treating optional polish as explicit carryover or deferral.

## What Went Well

- Sprint 3 stayed narrow: approach Memory Fragment, show prompt, press Interact, accept through MemoryState, and show restrained feedback.
- Ownership boundaries held: Input remained raw intent, `MemoryInteractionService` remained orchestration, `MemoryState` remained reveal/collect truth, and UI/VFX stayed presentation-only.
- S3-3 and S3-4 shipped with focused evidence and manual PlayMode confirmation.
- Duplicate/spam Interact behavior was verified for reveal feedback non-replay.
- No S3-scope bugs were filed during the smoke/QA pass.

## What Went Poorly

- A fresh full Unity Test Runner XML artifact was not produced for the final Sprint 3 state, so the smoke verdict stayed `PASS WITH WARNINGS`.
- QA sign-off was drafted in conversation but not yet written as a formal report at the time of this retrospective.
- S3-5 Runtime Memory Log Placeholder remained not started. This is acceptable as a should-have, but it should be explicitly carried over or descoped before the next sprint plan.

## Blockers Encountered

| Blocker | Duration | Resolution | Prevention |
|---------|----------|------------|------------|
| No fresh full Unity Test Runner artifact | Final close-out window | Compile smoke passed with 0 errors and manual M1 loop smoke passed all; warning recorded instead of blocking QA hand-off | Run Unity Test Runner before final sprint closure |
| S3-5 not started | Sprint scope | Kept outside must-have gate | Decide early whether should-have stories are pull-in work or planned carryover |
| QA sign-off not written | Close-out flow | Strategy/sign-off draft produced in conversation | Write sign-off report before `/gate-check` |

## Estimation Accuracy

| Task | Estimated | Actual | Variance | Likely Cause |
|------|----------:|-------:|---------:|--------------|
| S3-1 Readiness Review | 0.5d | Complete | On track | Review-only scope was clear. |
| S3-2 Memory Fragment Interaction | 2.0d | Complete with notes | Slightly higher evidence overhead | Interaction crossed input, service, state, and scene/runtime evidence. |
| S3-3 Interaction Prompt | 1.0d | Complete | On track | UI remained read-only and narrow. |
| S3-4 Reveal Feedback Placeholder | 1.0d | Complete | On track | Reused existing `M0MemoryVFXResponse` snapshot path. |
| S3-6 Smoke Test | 0.5d | Complete with notes | Slight evidence warning | Unity Test Runner artifact gap required explicit classification. |
| S3-5 Runtime Memory Log | 1.0d | Not started | Carryover | Should-have item was not needed for must-have loop proof. |

**Overall estimation accuracy**: Good for must-have scope. Optional scope should be planned as pull-in work unless the team explicitly wants total-sprint completion.

## Carryover Analysis

| Task | Original Sprint | Times Carried | Reason | Action |
|------|----------------|--------------:|--------|--------|
| S3-5 Runtime Memory Log Placeholder | Sprint 3 | 1 | Should-have, outside must-have smoke gate | Decide: carry into next sprint, descope, or replace with a smaller debug/read-model story |
| Fresh Unity Test Runner artifact | Sprint 3 close-out | 1 | Final smoke used compile + manual evidence, not full fresh XML artifact | Run before final gate if clean PASS is required |

## Technical Debt Status

- Current TODO/FIXME/HACK count across broad repo scan: 377, likely includes docs/vendor/package noise.
- Current TODO/FIXME/HACK count in owned gameplay C# under `afterimage-tokyo/Assets/_Project`: 0.
- Current TODO/FIXME/HACK count across owned project/docs scan: 5.
- Trend: Stable for owned gameplay code.
- Area of concern: workflow evidence is strong, but close-out still depends on remembering QA sign-off and fresh test artifacts.

## Previous Action Items Follow-Up

| Action Item | Status | Notes |
|-------------|--------|-------|
| Keep M1 scope narrow after M0 closure | Done | Sprint 3 avoided inventory, save/load, quest, dialogue, and broad progression systems. |
| Preserve ownership boundaries during presentation work | Done | S3-3/S3-4 kept UI/VFX downstream and snapshot-driven. |
| Classify external/non-scope console warnings separately | Done | Smoke and S3-4 evidence classify animation/targeting/baseline logs separately from S3-scope blockers. |
| Formal QA sign-off before gate | In Progress | Draft exists in conversation; report still needs to be written. |

## Action Items for Next Iteration

| # | Action | Owner | Priority | Deadline |
|---|--------|-------|----------|----------|
| 1 | Write Sprint 3 QA sign-off report | qa-lead | High | Before `/gate-check` |
| 2 | Decide S3-5 carryover vs descope | product/lead | High | Before next sprint plan |
| 3 | Run fresh Unity Test Runner and attach artifact | qa-lead/dev | Medium | Before final Sprint 3 closure or next phase gate |
| 4 | Keep future presentation slices snapshot-driven | all implementers | Medium | Ongoing |

## Process Improvements

- Add a close-out checklist item: QA sign-off report must be written before retrospective/gate-check.
- Treat should-have stories as explicit pull-in work. If they are not pulled in by mid-sprint, mark them carryover early.
- Capture Unity Test Runner artifacts before the final smoke report when the target verdict is clean PASS.

## Summary

Sprint 3 was successful: the must-have M1 exploration-memory loop is playable and verified without ownership drift. The single most important next process fix is to formalize QA sign-off and fresh Unity test artifacts before calling the sprint fully closed.
