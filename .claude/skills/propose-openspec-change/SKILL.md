---
name: propose-openspec-change
description: Create a complete OpenSpec proposal package including proposal, design, and task files.
---

# propose-openspec-change

Create a complete OpenSpec proposal package for a small, reviewable change.

## Purpose

Use this skill to create a complete proposal-only OpenSpec change.

A complete proposal package should include:

- proposal.md
- design.md
- tasks.md
- spec delta/spec.md if required by local OpenSpec workflow

## When to use

Use before implementation.

Do not modify runtime files.

## Inputs

Required:

- Change name
- Goal
- Source of truth docs
- Scope
- Non-goals
- Guardrails
- Acceptance criteria

## Rules

1. Proposal only

Do not edit `Assets/_Project` runtime files.

2. Keep scope small

Each change should be small enough to review and commit independently.

Good examples:

- `create-m0-input-intent-routing`
- `create-m0-player-locomotion-skeleton`
- `create-m0-target-context-skeleton`

Bad examples:

- `build-combat-system`
- `finish-m0`
- `make-player-controller`

3. Required artifacts

Create:

```txt
openspec/changes/<change-name>/proposal.md
openspec/changes/<change-name>/design.md
openspec/changes/<change-name>/tasks.md
openspec/changes/<change-name>/specs/<capability>/spec.md