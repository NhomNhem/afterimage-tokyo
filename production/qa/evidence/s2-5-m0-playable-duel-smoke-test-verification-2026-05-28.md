# S2-5 M0 Playable Duel Smoke Test Verification — 2026-05-28

## Status

IN PROGRESS

## Scope

Smoke verification evidence for Sprint 2 Story S2-5:
- checklist-driven QA pass for M0 duel stability and readability
- no gameplay code changes
- no Unity submodule/runtime modifications

Checklist source:
- `production/qa/smoke/m0-playable-duel-smoke-checklist-2026-05-28.md`

## Environment

- Unity version: PENDING
- Scene: M0 combat prototype scene
- Tester: PENDING
- Date/time: PENDING

## Console/Domain Classification

- S2-scope errors/exceptions: PENDING
- Known external warnings:
  - HDRP material enum/drawer warnings (`TransparentCullMode`) — classify as external unless proven blocking
- Other warnings: PENDING

## PASS / PARTIAL / FAIL Table

| Area | Result | Notes / Evidence |
|---|---:|---|
| Runtime + domain reload | PENDING |  |
| Scene/bootstrap load | PENDING |  |
| VContainer wiring | PENDING |  |
| Input actions | PENDING |  |
| Player movement | PENDING |  |
| Lock-on acquire/release | PENDING |  |
| Camera readability during lock-on | PENDING |  |
| LightAttack / Dodge / Parry | PENDING |  |
| CounterWindow / Counter path | PENDING |  |
| EnemyIntent loop readability | PENDING |  |
| Health / hit consequence | PENDING |  |
| Memory reveal / VFX placeholder | PENDING |  |
| Animator/Animancer presentation-only boundary | PENDING |  |
| Debug Overlay fields usefulness | PENDING |  |
| Console classification | PENDING |  |
| Known external material/HDRP classification | PENDING |  |
| Dirty scene/prefab check | PENDING |  |
| Overall smoke verdict | PENDING |  |

## Manual Checklist Record

| Check | Result | Notes |
|---|---:|---|
| Enter PlayMode on M0 scene | PENDING |  |
| Observe 3+ enemy intent loops | PENDING |  |
| Perform attack/dodge/parry checks | PENDING |  |
| Verify lock-on + camera readability | PENDING |  |
| Verify debug overlay readability | PENDING |  |
| Review console and classify warnings/errors | PENDING |  |
| Verify scene/prefab not unintentionally dirty | PENDING |  |

## Ownership Boundary Notes

During smoke review, confirm no gameplay truth drift into:
- camera
- animator/animancer
- VFX
- UI/debug overlay
- input presentation layer

Any boundary breach is a FAIL for this smoke.

## Follow-Up Actions

- If overall `PASS`: close S2-5 evidence with summary.
- If overall `PASS WITH NOTES`: log notes + open targeted follow-up story/tech debt.
- If overall `PARTIAL`: define blocking subset and open scoped OpenSpec/change request if implementation is required.
- If overall `FAIL`: stop progression on affected scope and resolve blocker first.

## Notes

This file is an execution template and does not claim manual verification has already been performed.
