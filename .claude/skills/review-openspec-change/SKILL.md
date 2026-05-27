---
name: review-openspec-change
description: Review an applied OpenSpec change before commit to ensure architectural integrity.
---

# review-openspec-change

Review an applied OpenSpec change before commit.

## Purpose

Use this skill after an OpenSpec change has been applied and before committing.

The review checks whether the implementation stayed inside the approved proposal scope, preserved architecture ownership, avoided deferred systems, and kept Unity project guardrails intact.

## When to use

Use after commands like:

- `/opsx:apply <change-name>`
- manual implementation of an OpenSpec change
- Claude Code reports "ready for review"

Do not use this skill to implement new behavior.

## Inputs

Required:

- Change name
- Relevant OpenSpec change folder
- Source GDDs / architecture docs if known
- Specific guardrails for the change

Example:

```txt
Review the applied change:
create-m0-player-locomotion-skeleton
