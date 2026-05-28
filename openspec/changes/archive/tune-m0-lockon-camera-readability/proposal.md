# S2-4 — Lock-On Combat Camera Readability Pass

## Change

- Name: `tune-m0-lockon-camera-readability`
- Type: Planning only (no implementation in this change)
- Status: Proposed

## Why

Sprint 2 is focused on M0 feel/readability stabilization.
After S2-2 (combat readability) and S2-3 (enemy telegraph readability), camera framing is the next bottleneck for readable duel decision-making.

## Goal

Improve M0 lock-on camera readability so the player can consistently read both player and enemy during the duel, without moving gameplay truth into the camera.

## Scope In

- Define M0 lock-on readability expectations and measurable checks.
- Define safe camera/framing tuning surface (parameter-level only).
- Define verification and evidence requirements (EditMode/PlayMode/manual).
- Define rollback/migration strategy if tuning degrades readability.

## Scope Out

- No runtime implementation.
- No Unity submodule code edits.
- No scene/prefab/material/asset edits.
- No Cinemachine value changes yet.
- No camera system rewrite.
- No cinematic/boss/multi-enemy camera work.
- No combat/input/target/intent architecture changes.
- No targeting refactor.
- No combat timing changes.
- No combat result changes.
- No EnemyIntent lifecycle changes.
- No enemy AI behavior tree/GOAP/boss/roster expansion.
- No input architecture changes.
- No TargetContext ownership changes.
- No gameplay truth in camera.
- No camera-driven combat, target, input, enemy intent, memory, or debug overlay state.
- No root motion authority.

## Source Of Truth

- `production/sprints/sprint-2.md`
- `production/qa/qa-plan-sprint-2-2026-05-26.md`
- `production/epics/m0-first-playable-duel/story-s2-1-m0-sprint-1-playable-duel-closure-review.md`
- `production/qa/evidence/s2-2-combat-feel-readability-verification-2026-05-26.md`
- `production/qa/evidence/s2-3-enemy-telegraph-readability-verification-2026-05-27.md`

## Guardrails

- Camera is readability/framing only.
- Target truth remains in `TargetContext`.
- Combat truth remains in `CombatCore`.
- Enemy phase truth remains in `EnemyIntent`.
- Movement truth remains in `PlayerLocomotion`.
- Debug Overlay remains read-only.
- No gameplay truth in camera scripts.

## Acceptance Criteria

1. Planning artifacts clearly define what lock-on readability means for M0 duel.
2. Safe-tunable parameters are listed and bounded.
3. Non-change list is explicit and enforceable.
4. Evidence expectations include PASS/PARTIAL/FAIL and console classification.
5. Rollback plan exists for readability regressions.
6. `TargetContext` SHALL remain the sole owner of lock-on target truth.
7. Camera SHALL only consume target/camera-relevant snapshots or references needed for framing.
8. S2-4 SHALL NOT change combat timing or combat result logic.
9. S2-4 SHALL NOT change `EnemyIntent` Telegraph/Commit/Active/Recovery lifecycle logic.
10. Debug Overlay SHALL remain read-only and usable to verify camera-independent gameplay truth.
