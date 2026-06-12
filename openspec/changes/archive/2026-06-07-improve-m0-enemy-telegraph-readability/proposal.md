## Why

M0 is now back on gameplay feel after the runtime composition cleanup. The enemy telegraph loop exists, but the next risk is player readability under duel pressure: a tester must be able to understand what the enemy intends, what defensive answer is available, when commitment has happened, and why the counter/reveal opportunity did or did not appear.

This change proposes a narrow improvement pass for the existing M0 enemy telegraph readability surface.

## What Changes

- Define a follow-up readability target for the existing enemy intent loop.
- Specify how Telegraph, Commit, Active, Recovery, and punish readability should be surfaced to the player and debug overlay.
- Require focused tests/evidence that phase truth remains owned by Enemy Intent and Telegraph.
- Keep presentation cues observer-only and anchored to enemy intent snapshots.

## Scope

### In Scope

- Existing simple M0 enemy only.
- Existing duel loop `read -> evade/parry -> counter -> reveal`.
- Enemy intent phase clarity for Telegraph, Commit, Active, Recovery, and punish window.
- Debug/readout labels that explain phase, timing, attack tags, and punish availability.
- Tests for phase transition/readability data shape and ownership guardrails.
- Manual PlayMode evidence for at least three repeated enemy intent loops.

### Out of Scope

- New enemy types, boss phases, combo trees, or multi-enemy behavior.
- Behavior tree, GOAP, or broad AI architecture.
- CombatCore result authority changes.
- Health/damage/hit reaction rework.
- Camera/lock-on refactor beyond read-only cue consumption.
- Full animation, VFX, or audio pipeline rebuild.

## Guardrails

- Enemy Intent and Telegraph owns telegraph, commitment, active/recovery timing, attack tags, and punish windows.
- Combat Core owns combat action validity, counter window truth, hit resolution, and reveal request context.
- Presentation, camera, VFX, audio, and Debug Overlay may only observe confirmed enemy intent/combat snapshots.
- Debug Overlay must remain read-only and must not become gameplay truth.
- No direct Unity logging in project code; use `NhemLogger` / `NhemLogging` if logs are required.
- No broad lookup, global singleton manager, or service locator.
- The existing Odin asmdef dependency fix is treated as a compile-health prerequisite, not as enemy telegraph runtime scope.

## Acceptance Criteria

- A tester can distinguish Telegraph from Commit/Active before being hit.
- Recovery and punish availability are visible enough to support a counter decision.
- Debug/evidence can explain current phase, next expected phase, attack tags, and punish/counter relevance.
- Focused tests prove phase readability data is derived from Enemy Intent truth and remains immutable/read-only to observers.
- Scene composition and VContainer registry tests remain green after the compile-health fix.
- Evidence records automated results, console classification, and manual PlayMode readability notes.
