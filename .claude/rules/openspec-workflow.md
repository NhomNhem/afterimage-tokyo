# OpenSpec Workflow Rules — Glass Refrain

## Purpose

These rules govern how OpenSpec change proposals, story files, and archived work
must be treated during implementation. They prevent rework, scope creep, and
unauthorized reopening of completed work.

## Change Scope Rule

Every OpenSpec change defines a bounded scope in its proposal and task files.

Do not add features, refactors, or fixes that are outside the approved change scope
during implementation. If a need is discovered, file it as a separate issue or
proposal — do not expand the current change.

## Story Boundary Rule

Story files define implementable units of work. Each story has its own task file
with specific acceptance criteria.

Do not implement work from another story within the current story's implementation.
If a dependency or gap is discovered, surface it to the orchestrating agent rather
than silently expanding scope.

## Archived Change Rule

Once an OpenSpec change is archived (COMPLETE WITH NOTES), it is final.

An archived change must not be:
- reopened for additional work
- modified with new commits
- used as a base for extension without a new proposal

If follow-up work is needed after archiving, create a new OpenSpec proposal or
story that explicitly references the archived change as context.

## Archived Follow-Up Rule

Follow-ups discovered during the archive process must be tracked in the follow-up
tracker, not by keeping the archived change open.

Acceptable follow-up patterns:
```txt
m0-visual-polish-followups
m0-lockon-second-press-behavior-decision
```

An archived change whose follow-ups are still pending is still complete. Do not
reopen it.

## Implementation Discipline

When implementing from OpenSpec tasks:

- Implement exactly what the task describes, nothing more.
- If a task references a GDD requirement or ADR, follow it — do not reinterpret.
- If a task is ambiguous, ask rather than guessing.
- Do not "fix" unrelated code while in scope unless it's a blocking defect.
- When the task list is done, the change is ready for archive review.

## Defect Discovery Rule

If a genuine defect is discovered during implementation that is outside scope:
1. Note it in the implementation summary.
2. Do not fix it within the current change unless it blocks the task.
3. File a bug report or separate proposal for follow-up resolution.
