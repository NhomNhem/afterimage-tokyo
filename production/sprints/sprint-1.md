# Sprint 1 — 2026-05-15 to 2026-05-29

## Sprint Goal
Wire the M0 technical skeletons into a functional one-player / one-enemy Tokyo Street duel loop.

## Capacity
- Total days: 10
- Buffer (20%): 2 days reserved for unplanned work
- Available: 8 days

## Tasks

### Must Have (Critical Path)
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S1-1 ✅ | [Foundation] Scene & VContainer Wiring | lead-programmer | 1.0 | None | Bootstrap loads all 6 scenes; VContainer resolves Core/Infrastructure/Domain. |
| S1-2 | [Locomotion] Camera-Relative Movement | gameplay-programmer | 1.0 | S1-1 | Player moves relative to Camera basis; facing supports move/target directions. |
| S1-3 | [Targeting] Lock-On Wiring | gameplay-programmer | 0.5 | S1-1 | Toggle Lock-On acquires/releases target; TargetContext is source of truth. |
| S1-4 ✅ | [Combat] Player Attack Resolution | gameplay-programmer | 1.0 | S1-1, S1-2 | Light/Heavy attacks resolve in M0CombatCore; locks/recovery apply to Locomotion. |
| S1-5 | [Enemy] Intent & Telegraph Loop | ai-programmer | 1.0 | S1-1 | Enemy cycles Telegraph -> Active -> Recovery; Punish window is readable. |
| S1-6 | [Combat] Parry & Dodge Integration | gameplay-programmer | 1.0 | S1-4, S1-5 | Parry/Dodge resolve in Core; successful Parry opens CounterWindow. |
| S1-7 | [Consequence] Health & Hit Reactions | gameplay-programmer | 1.0 | S1-4, S1-5 | Damage applies to Health; Hit Reactions suppression applies to Locomotion. |
| S1-8 | [Encounter] Reset & Duel Lifecycle | lead-programmer | 0.5 | S1-1, S1-7 | Encounter Start/End/Reset resets system states and participant positions. |

### Should Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S1-9 | [Presentation] Debug Overlay Snapshots | lead-programmer | 0.5 | S1-1, S1-8 | Debug Overlay displays snapshots for all Core systems (M0Contracts). |
| S1-10 | [Memory] Reveal & VFX Placeholder | vfx-programmer | 0.5 | S1-4, S1-6 | Successful counter triggers Reveal; MemoryVFXResponse plays placeholder VFX. |

### Nice to Have
| ID | Task | Agent/Owner | Est. Days | Dependencies | Acceptance Criteria |
|----|------|-------------|-----------|-------------|-------------------|
| S1-11 | [Presentation] Animator Observer Adapters | lead-programmer | 1.0 | S1-4, S1-5 | Animator observes states/resolutions to trigger clips; no authority in Animator. |

## Current Validated Status — 2026-05-26

Sprint status is based on verified M0 Combat EditMode and PlayMode evidence, not earlier progress summaries.

| Story / Task | Validated Status | Evidence / Remaining Verification |
|---|---|---|
| S1-1 [Foundation] Scene & VContainer Wiring | VERIFIED | Strict manual DI restored; PlayMode startup/composition clean. |
| S1-2 [Locomotion] Camera-Relative Movement | VERIFIED | Latest PlayMode evidence confirms WASD movement and locomotion displacement behavior. |
| S1-3 [Targeting] Lock-On Wiring | VERIFIED | LockOn acquire/release/reacquire verified in archived LockOn evidence set. |
| S1-4 [Combat] Player Attack Resolution | VERIFIED | M0CombatCoreTests pass 13/13; LightAttack and HeavyAttack PlayMode cycles verified with Mouse Left and Mouse Right. |
| S1-5 [Enemy] Intent & Telegraph Loop | VERIFIED | Enemy intent cycle Telegraph/Commit/Active/Recovery/Idle confirmed in latest smoke evidence. |
| S1-6 [Combat] Parry & Dodge Integration | VERIFIED WITH NOTES | Dodge displacement wiring verified; closure includes notes with LockOn smoke accepted by prior reference. |
| S1-7 [Consequence] Health & Hit Reactions | VERIFIED | Story complete with evidence; follow-up remains tracked as tech debt. |
| S1-8 [Encounter] Reset & Duel Lifecycle | VERIFIED WITH NOTES (ARCHIVED) | Implemented, corrected, verified, approved-with-notes, archived at `openspec/changes/archive/2026-05-26-wire-m0-encounter-reset-duel-lifecycle`. |
| S1-9 [Presentation] Debug Overlay Snapshots | PARTIAL / IN PROGRESS | Combat/enemy labels update; last input, lock-on, and counter-window visibility still need confirmation. |
| S1-10 [Memory] Reveal & VFX Placeholder | BACKLOG | RevealBeat path not verified. |
| S1-11 [Presentation] Animator Observer Adapters | BACKLOG | No verification evidence. |

### Verification Corrections

The previous K/J/Space/L/C manual-test sequence was invalid. Manual PlayMode verification now uses actual bindings from M0InputActions.inputactions and M0DirectPlayerInput.

Actual M0 bindings: Move=WASD, LightAttack=Mouse Left, HeavyAttack=Mouse Right, Dodge=Left Shift, Parry=Q, Counter=E, LockOn=Tab, ResetEncounter=R, ToggleDebugOverlay=F3.

Player Attack Resolution is VERIFIED. LightAttack and HeavyAttack were manually verified in PlayMode using actual bindings Mouse Left and Mouse Right. Both actions were accepted from Neutral and progressed through AttackStartup -> AttackActive -> AttackRecovery -> Neutral.

Dodge displacement wiring is now verified as PASS WITH NOTES (2026-05-25), including visible displacement and transform delta.

LockOn second-press toggle-release behavior is verified in the archived LockOn change and accepted by reference in the Dodge displacement closure artifact.

Encounter reset lifecycle (Story 1-8) is now archived as completed-with-notes after corrective baseline patch verification and focused reset test pass (48/48).

## Carryover from Previous Sprint
| Task | Reason | New Estimate |
|------|--------|-------------|
| None | Phase Start | N/A |

## Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Circular dependencies in VContainer | Medium | High | Strict adherence to ADR-0004 and ADR-0005 (M0Contracts). |
| Unity 6.3 Input System quirks | Low | Medium | Use established patterns from InputFoundation. |
| CLI test unreliability | High | Low | Manual verification in Unity Editor after each task. |

## Dependencies on External Factors
- Unity 6000.3.x Environment stability.

## Definition of Done for this Sprint
- [ ] All Must Have tasks completed
- [ ] All tasks pass acceptance criteria
- [ ] QA plan exists (`production/qa/qa-plan-sprint-1.md`)
- [ ] All Logic/Integration stories have passing unit/integration tests
- [ ] Manual verification in Unity Editor successful for all wired systems
- [ ] No S1 or S2 bugs in wired duel loop
- [ ] Design documents updated for any implementation deviations
- [ ] Code reviewed and merged into M0 branch
