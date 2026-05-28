# S2-5 M0 Playable Duel Smoke Test Verification — 2026-05-28

## Status

PASS WITH NOTES

## Scope

Smoke verification evidence for Sprint 2 Story S2-5:
- checklist-driven QA pass for M0 duel stability and readability
- no gameplay code changes
- no Unity submodule/runtime modifications

Checklist source:
- `production/qa/smoke/m0-playable-duel-smoke-checklist-2026-05-28.md`

## Environment

- Unity version: 6000.3.x (project baseline)
- Scene: M0 combat prototype scene
- Tester: Local manual run (user-provided PlayMode log capture)
- Date/time: 2026-05-28

## Console/Domain Classification

- S2-scope errors/exceptions: NOT OBSERVED in provided run log
- Known external warnings:
  - HDRP material enum/drawer warnings (`TransparentCullMode`) — external/non-S2 scope
- Other warnings observed:
  - Missing optional animation presentation/animation set warnings (`M0Animation ... missing ... tolerable`)
  - Targetable adapter construct-time inactive registration warning before successful OnEnable registration

## PASS / PARTIAL / FAIL Table

| Area | Result | Notes / Evidence |
|---|---:|---|
| Runtime + domain reload | PASS | No S2-scope startup crash/exception observed in capture |
| Scene/bootstrap load | PASS | Bootstrap systems initialized; target registration completed on enable |
| VContainer wiring | PASS WITH NOTES | No VContainerException observed; expected optional animation warnings present |
| Input actions | PASS | InputActionAsset loaded/enabled; required actions found |
| Player movement | PASS | Move start/stop and locomotion application logs observed |
| Lock-on acquire/release | PASS | `LockOn acquired` and `LockOn released` captured |
| Camera readability during lock-on | PASS WITH NOTES | Lock-on loop remained readable in capture; no direct camera metric tooling used |
| LightAttack / Dodge / Parry | PARTIAL | LightAttack and Dodge observed; explicit Parry press not captured in this run |
| CounterWindow / Counter path | PARTIAL | Not observed in this specific run log |
| EnemyIntent loop readability | PASS | Idle -> Telegraph -> Commit -> Active -> Recovery -> Idle observed |
| Health / hit consequence | PARTIAL | No explicit health consequence evidence in this run |
| Memory reveal / VFX placeholder | PARTIAL | Not exercised in this run |
| Animator/Animancer presentation-only boundary | PASS WITH NOTES | Missing animation-set warnings indicate presentation-only fallback, no truth ownership drift observed |
| Debug Overlay fields usefulness | PARTIAL | Overlay field evidence not captured in provided log sample |
| Console classification | PASS WITH NOTES | No S2-scope hard error; non-scope and placeholder warnings present |
| Known external material/HDRP classification | PASS | Classified external/non-S2 blocker |
| Dirty scene/prefab check | PASS | Post-run submodule `git status --short` clean |
| Overall smoke verdict | PASS WITH NOTES | Core loop/readability stable; some optional/manual evidence items not exercised this pass |

## Manual Checklist Record

| Check | Result | Notes |
|---|---:|---|
| Enter PlayMode on M0 scene | PASS | Bootstrap/input/enemy loop logs confirm runtime entry |
| Observe 3+ enemy intent loops | PASS | Full enemy loop transitions observed |
| Perform attack/dodge/parry checks | PARTIAL | Attack + Dodge observed; Parry not captured in this sample |
| Verify lock-on + camera readability | PASS WITH NOTES | Acquire/release observed; readability acceptable in capture |
| Verify debug overlay readability | PARTIAL | Not explicitly logged/captured |
| Review console and classify warnings/errors | PASS WITH NOTES | Classified non-scope warnings and external HDRP material warnings |
| Verify scene/prefab not unintentionally dirty | PASS | No dirty files in Unity submodule after run |

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

Unity MCP live PlayMode control/evidence extraction was limited in this pass (console query returned no live entries), so this record is based on the manually captured PlayMode run log provided in-thread and explicit post-run workspace checks.

No S2-5 blockers found. Items marked PARTIAL are follow-up evidence opportunities, not release blockers for this smoke checklist story.
