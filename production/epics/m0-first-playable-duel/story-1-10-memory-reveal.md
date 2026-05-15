# Story 1-10: [Memory] Reveal & VFX Placeholder

> **Epic**: M0 First Playable Duel
> **Status**: Ready
> **Layer**: Feature/Presentation
> **Type**: Visual/Feel
> **Estimate**: 0.5d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/memory-state.md`
**Requirement**: `TR-M0-MEMORY-001`, `TR-M0-MEMORY-VFX-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Memory State owns reveal acceptance; Memory VFX is downstream presentation only.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Read-Only Observation (VFX observes memory state).
- Forbidden: No Mutation from Presentation.

---

## Acceptance Criteria

- [ ] Successful counter result in `CombatCore` triggers a `RevealRequestContext`.
- [ ] `MemoryState` accepts the request and enters the `Responding` state.
- [ ] `M0MemoryVFXResponse` (skeleton) triggers a placeholder VFX on acceptance.
- [ ] Reveal response is short and restrained, returning to neutral rhythm.

---

## Implementation Notes

- Connect `CombatCore` reveal trigger to `MemoryState`.
- Use the `MemoryState` FSM to manage acceptance and cooldown.
- Ensure VFX playback is decoupled from gameplay state via events or snapshots.

---

## Out of Scope

- [Story 1-11]: Animator support for reveal reactions.

---

## QA Test Cases

**AC-1: Reveal Acceptance**
- **Test**: Reveal request is accepted after counter success.
  - Given: Counter hit is confirmed.
  - When: RevealRequestContext is emitted.
  - Then: MemoryState becomes Responding.

**AC-2: VFX Restraint**
- **Manual check**: VFX does not obscure enemy intent.
  - Setup: Trigger a counter reveal.
  - Verify: VFX duration is short and player can still see the enemy during recovery.
  - Pass condition: Duel readability maintained.

---

## Test Evidence

**Story Type**: Visual/Feel
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/MemoryState_test.cs`
- Manual verification: Video clip of the counter reveal sequence.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-4, Story 1-6
- Unlocks: None
