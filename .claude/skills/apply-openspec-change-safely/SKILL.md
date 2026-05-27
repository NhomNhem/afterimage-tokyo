---
name: apply-openspec-change-safely
description: Apply an approved OpenSpec change while adhering to strict architectural guardrails and scope.
---

# apply-openspec-change-safely

Apply an OpenSpec change with strict scope and architecture guardrails.

## Purpose

Use this skill when applying an approved and validated OpenSpec change.

The goal is to implement only the approved scope, avoid adjacent systems, and keep the project architecture clean.

## When to use

Use after:

- proposal.md exists
- design.md exists
- tasks.md exists
- spec delta exists if required
- validation has passed

Do not use this before validation.

## Inputs

Required:

- Change name
- Change folder
- Approved scope
- Non-goals
- Relevant GDDs
- Relevant architecture docs
- Guardrails

Example:

```txt
Apply create-m0-player-locomotion-skeleton.
