# Story 1-9: [Presentation] Debug Overlay Snapshots

> **Epic**: M0 First Playable Duel
> **Status**: Ready
> **Layer**: Presentation
> **Type**: UI/Logic
> **Estimate**: 0.5d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/debug-overlay.md`
**Requirement**: `TR-M0-DEBUG-001`

**ADR Governing Implementation**: [ADR-0003: M0 Presentation and Debug Read-Only Boundaries]
**ADR Decision Summary**: Debug Overlay owns presentation only; it aggregates read-only snapshots.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Debug Snapshot Aggregation (read-only grouping).
- Forbidden: No Inference in Debug (cannot repair/override truth).

---

## Acceptance Criteria

- [ ] Debug Overlay displays read-only snapshots for all Core systems (Combat, Locomotion, Enemy, Health, Memory, Target).
- [ ] Labels match GDD state and window names exactly.
- [ ] Snapshot assembly uses the `M0Contracts` hub for data shape.
- [ ] Overlay can be toggled via debug input without affecting gameplay.

---

## Implementation Notes

- Use UI Toolkit for the overlay presentation.
- Aggregator service must read snapshots only; mutation is forbidden.
- Follow the aggregate-and-group pattern from the debug GDD.

---

## Out of Scope

- [Story 1-11]: Animator state visibility.

---

## QA Test Cases

**AC-1: Data Accuracy**
- **Test**: Overlay reflects current Core state.
  - Given: CombatCore is in CounterWindow.
  - When: Snapshot is refreshed.
  - Then: Overlay label `CounterWindow` is Active/True.

**AC-2: Read-Only Check**
- **Manual check**: Overlay does not own any state fields.
  - Setup: Inspect debug overlay code.
  - Verify: No public setters or mutators on gameplay truth.
  - Pass condition: Code review pass for read-only constraint.

---

## Test Evidence

**Story Type**: UI/Logic
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/DebugOverlay_test.cs`
- Manual verification: Screenshot of the Tokyo Street duel with the full overlay active.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-1, Story 1-8
- Unlocks: None
