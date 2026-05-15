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
| S1-1 | [Foundation] Scene & VContainer Wiring | lead-programmer | 1.0 | None | Bootstrap loads all 6 scenes; VContainer resolves Core/Infrastructure/Domain. |
| S1-2 | [Locomotion] Camera-Relative Movement | gameplay-programmer | 1.0 | S1-1 | Player moves relative to Camera basis; facing supports move/target directions. |
| S1-3 | [Targeting] Lock-On Wiring | gameplay-programmer | 0.5 | S1-1 | Toggle Lock-On acquires/releases target; TargetContext is source of truth. |
| S1-4 | [Combat] Player Attack Resolution | gameplay-programmer | 1.0 | S1-1, S1-2 | Light/Heavy attacks resolve in M0CombatCore; locks/recovery apply to Locomotion. |
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
