# Story S8-8: [Architecture] Decompose PlayerStateMachine into Layer State Machines

> **Sprint**: Sprint 8
> **Status**: Complete
> **Layer**: Application / Architecture
> **Type**: Logic
> **Estimate**: 1.0 days
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-17
> **Completed**: 2026-06-17

## Context

**Sprint Plan**: `production/sprints/sprint-8.md`
**Epic**: M0 First Playable Duel — architecture hardening
**GDD**: `design/gdd/combat-core.md`, `design/gdd/player-locomotion.md`
**ADR Governing Implementation**: Control Manifest (Application layer) + `.claude/docs/technical-preferences.md` Clean Architecture boundaries — Domain pure, Application orchestrates, Infra implements, Presentation observes.

**Engine**: Unity 6000.3.x + URP | **Risk**: LOW
**Engine Notes**: Pure C# class decomposition. No Unity lifecycle, no scene/prefab changes.

**Control Manifest Rules**:
- Required: Prefer composition over inheritance. Prefer small interfaces. Split read and command interfaces when it improves dependency direction.
- Forbidden: No global singleton managers. No gameplay truth in Presentation.
- Guardrail: IPlayerStateMachine API must remain unchanged — upstream consumers (M0GameplayTickHandler, M0AnimationPresentationAdapter) are unchanged.

---

## Current Architecture

`PlayerStateMachine` (284 lines) currently handles:
- CombatCoreState observation → PlayerState mapping (`CombatPriorityToPlayerState`)
- LocomotionState observation → PlayerState mapping (`LocomotionPriorityToPlayerState`)
- Priority-based resolution between combat and locomotion
- Action lock aggregation
- Recovery context aggregation
- Debug snapshot production
- VContainer registration via `PlayerStateMachineFactory`

## Target Architecture

```
M0CombatCore ──→ CombatStateMachine ──┐
                                      ├── PlayerStateResolver ──→ IPlayerStateMachine
IM0PlayerLocomotion ──→ LocomotionStateMachine ─┘
                            ↑
                        GroundState (Idle/Moving/Restricted/Recovering)
```

### New Classes

1. **CombatStateMachine** (`Application` layer)
   - Wraps `M0CombatCore`, subscribes to `SnapshotChanged`
   - Contains `CombatPriorityTable` and `CombatPriorityToPlayerState`
   - Emits combat `PlayerState` via `Observable<PlayerState>`

2. **LocomotionStateMachine** (`Application` layer)
   - Wraps `IM0PlayerLocomotion`, subscribes to `SnapshotChanged`
   - Defines `GroundState` enum: `Idle`, `Moving`, `Restricted`, `Recovering`
   - Maps `LocomotionState → GroundState`
   - Emits GroundState + movement context via dedicated snapshot

3. **PlayerStateResolver** (`Application` layer)
   - Takes both state machines
   - Implements priority resolution (same logic as current `ResolvePlayerState`)
   - Aggregates action lock + recovery context
   - Emits `PlayerStateSnapshot` — identical to current shape
   - Implements `IPlayerStateMachine` — same API

### Deletions

- `PlayerStateMachine` (the current class) — logic split into 3
- `PlayerStateMachineFactory` — inline into resolver or `M0SceneCompositionRegistrar`

---

## Acceptance Criteria

- [ ] CombatStateMachine compiles, observes CombatCore, maps state correctly.
- [ ] LocomotionStateMachine compiles with GroundState enum, observes Locomotion, maps correctly.
- [ ] PlayerStateResolver merges combat + ground priority correctly (same logic as current ResolvePlayerState).
- [ ] IPlayerStateMachine interface unchanged — no upstream consumer changes.
- [ ] M0SceneCompositionRegistrar updated — resolves via new 3-class chain.
- [ ] Action lock + recovery context preserved in PlayerStateSnapshot.
- [ ] CreateDebugSnapshot output format preserved (debug overlay unchanged).
- [ ] All EditMode tests pass (current baseline: 251/251).
- [ ] Existing M0PlayerStateMachineDodgeTests pass (PlayMode) or updated for new constructor.
- [ ] No new warnings in compile output.

---

## Out of Scope

- Changes to IPlayerStateMachine interface or PlayerStateSnapshot shape.
- Scene, prefab, or GameObject changes.
- Combat Core, Locomotion, or Health truth changes.
- VContainer DI migration beyond updated registration.
- New test coverage beyond what's needed for regression — this is a behavior-preserving refactor.

---

## QA Test Cases

- **AC-1**: Resolved state for combat-with-attack yields PlayerState.Attack — same as before.
- **AC-2**: Resolved state for locomotion-moving yields PlayerState.Moving when combat is Neutral.
- **AC-3**: Resolved state for combat-with-priority (e.g., HitReact) overrides locomotion.
- **AC-4**: Null combat or null locomotion degrades correctly (locomotion-only or combat-only).
- **AC-5**: Debug snapshot format matches existing CreateDebugSnapshot output.
- **AC-6**: Full EditMode suite regression — no existing tests broken.

---

## Test Evidence

**Story Type**: Logic
**Required evidence**:
- `production/qa/evidence/s8-8-decompose-player-state-machine.md`
- Full EditMode suite PASS result
- Targeted EditMode tests for each new class's mapping logic

**Status**: [x] Created at `production/qa/evidence/s8-8-decompose-player-state-machine.md` + `Assets/_Project/Tests/EditMode/M0StateMachineDecompositionTests.cs` (8 tests)

---

## Dependencies

- Depends on: None.
- Unlocks: Cleaner separation before animation slice (S8-1 through S8-5) — architecture stable before presentation changes.

## Completion Notes
**Completed**: 2026-06-17
**Criteria**: 10/10 passing
**Deviations**: ADVISORY — PlayerStateResolver::Dispose() does not explicitly dispose child machines (DI container handles); HasCore/HasLocomotion properties exposed beyond old API (intentional degraded-mode detection)
**Test Evidence**: Logic — Assets/_Project/Tests/EditMode/M0StateMachineDecompositionTests.cs (8 tests, all PASS); production/qa/evidence/s8-8-decompose-player-state-machine.md
**Code Review**: Complete — passed with suggestions
