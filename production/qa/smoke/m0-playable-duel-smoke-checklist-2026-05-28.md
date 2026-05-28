# M0 Playable Duel Smoke Checklist — 2026-05-28

## Scope

Sprint 2 smoke verification for the current M0 playable duel after readability passes.

This checklist is docs-only guidance and does not require code changes.

## Execution Constraints

- Do not modify gameplay code during smoke execution.
- Do not modify Unity scene/prefab/assets while running checklist.
- If scene/prefab becomes dirty during run, classify explicitly.
- Separate known external issues from S2 story blockers.

## PASS/PARTIAL/FAIL Rubric

Use these meanings consistently:
- `PASS`: expected behavior observed, no S2-scope blocker.
- `PARTIAL`: behavior observed with limitations/noise; still usable but follow-up needed.
- `FAIL`: behavior missing/broken or blocked by S2-scope issue.

## Smoke Items

| ID | Item | Steps | PASS Criteria | PARTIAL Criteria | FAIL Criteria |
|---|---|---|---|---|---|
| 1 | Project opens / domain reload | Open project, wait for compilation/domain reload | No S2-scope compile/domain failure | External/non-scope warnings only | S2-scope compile/domain failure blocks run |
| 2 | Scene/bootstrap load | Load M0 combat prototype scene and enter PlayMode | Scene enters PlayMode; bootstrap runs | PlayMode runs with non-blocking warnings | Cannot enter/keep PlayMode due to S2-scope issue |
| 3 | VContainer wiring | Observe startup for DI failures | No VContainerException in S2-scope flow | Non-S2 DI warnings only | S2-scope DI failure blocks gameplay loop |
| 4 | Input actions | Verify required gameplay actions are found/active | Move/Attack/Dodge/Parry/Counter/LockOn inputs respond | Intermittent input delay but usable | Inputs not wired or unusable |
| 5 | Player movement | Move in multiple directions | Movement/facing readable and functional | Minor readability issue, still controllable | Movement control broken |
| 6 | Lock-on acquire/release | Toggle lock-on on/off while enemy is valid | Acquire and release both work; logs/overlay reflect state | One transition less readable but functional | Cannot acquire/release reliably |
| 7 | Camera readability during lock-on | Move/attack/dodge under lock-on over enemy loops | Player + enemy remain readable most of the time | Occasional occlusion, duel still readable | Frequent occlusion/loss blocks readability |
| 8 | LightAttack / Dodge / Parry | Execute each action at least once | State transitions and feel readable for all three | One beat unclear but still operable | Any core beat consistently unreadable/broken |
| 9 | CounterWindow / Counter path | Attempt parry-timed counter flow | CounterWindow and/or counter path observed when available | Hard to reproduce but some evidence exists | No counter path evidence when flow should be available |
| 10 | EnemyIntent loop | Observe 3+ cycles | Idle -> Telegraph -> Commit -> Active -> Recovery visible/repeatable | One phase less clear but loop still understandable | Intent lifecycle unreadable/broken |
| 11 | Health / hit consequence | Trigger hit/consequence interactions | Health/hit consequence responds as expected | Minor clarity issue only | Consequence path broken |
| 12 | Memory reveal / VFX placeholder | Trigger reveal path (manual or approved helper path) | Reveal path evidence present and bounded | Evidence partial but non-blocking with notes | Reveal path broken in-scope |
| 13 | Animator/Animancer ownership | Observe runtime behavior/logs for presentation layer | Presentation remains downstream; no gameplay truth ownership drift | Placeholder animation warnings only | Animator/Animancer drives gameplay truth |
| 14 | Debug Overlay fields | Verify overlay readable fields during loop | Core fields readable and camera-independent truth visible | Some fields noisy but still usable | Overlay unusable for smoke validation |
| 15 | Console classification | Review Error/Warning/Log after run | No new S2-scope hard errors | Only known external/non-scope warnings | New S2-scope hard errors/exceptions |
| 16 | Known external material/HDRP issue | Check for known material enum warnings | Known issue present and correctly classified external | Same warnings plus noise, still classifiable | Misclassified as S2 blocker without evidence |
| 17 | Dirty scene/prefab check | Exit PlayMode, inspect dirty assets | No unintended scene/prefab dirtiness | Dirty but clearly intentional and documented | Unintended dirty scene/prefab without classification |

## Result Table Template

| Area | Result | Notes / Evidence Reference |
|---|---:|---|
| Runtime + domain reload | PENDING |  |
| Bootstrap + DI | PENDING |  |
| Input + movement | PENDING |  |
| Lock-on + camera readability | PENDING |  |
| Attack / Dodge / Parry | PENDING |  |
| Counter path | PENDING |  |
| Enemy intent readability | PENDING |  |
| Health consequence | PENDING |  |
| Memory reveal / VFX placeholder | PENDING |  |
| Presentation ownership boundary | PENDING |  |
| Debug overlay usefulness | PENDING |  |
| Console classification | PENDING |  |
| External material/HDRP classification | PENDING |  |
| Dirty scene/prefab check | PENDING |  |
| Overall smoke verdict | PENDING |  |

## Follow-Up Rules

- If `Overall = PASS`:
  - Mark smoke check complete and proceed with next Sprint 2 priority.
- If `Overall = PASS WITH NOTES`:
  - Log notes in evidence; open targeted follow-up tasks/tech debt without blocking unrelated stories.
- If `Overall = PARTIAL`:
  - Open a scoped follow-up story or OpenSpec change before tuning/coding.
- If `Overall = FAIL`:
  - Stop progression for affected scope, create blocker record, and resolve critical issue first.

## Non-Scope Error Policy

Known external/non-scope issues (example: HDRP material enum warnings) must be tracked separately and must not be treated as S2 smoke blockers unless they directly block execution of checklist items.
