# Story 1-2: [Locomotion] Camera-Relative Movement

> **Epic**: M0 First Playable Duel
> **Status**: Complete
> **Layer**: Core
> **Type**: Logic/Integration
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-15

## Context

**GDD**: `design/gdd/player-locomotion.md`
**Requirement**: `TR-M0-LOCOMOTION-001`, `TR-M0-CAMERA-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Locomotion owns movement truth; Camera provides read-only movement basis.

**Engine**: Unity 6000.3.x | **Risk**: LOW
**Engine Notes**: Pure C# truth authority established.

**Control Manifest Rules (this layer)**:
- Required: Camera Movement Basis (forward/right projected on ground plane).
- Required: Pure C# Authority for movement truth.
- Forbidden: Camera must NOT mutate movement truth.

---

## Acceptance Criteria

- [ ] Player moves in world-projected direction relative to camera forward.
- [ ] Movement basis (forward/right) is provided by `CameraScope`.
- [ ] Locomotion FSM handles basic move/idle transitions.
- [ ] Facing supports movement direction when not locked-on.

---

## Implementation Notes

- Implement `CameraMovementBasisSnapshot` provider in the Camera system.
- Wire movement basis into `M0PlayerLocomotion`.
- Use Pure C# for position/facing calculation.

---

## Out of Scope

- [Story 1-3]: Lock-On facing/orientation.

---

## QA Test Cases

**AC-1: Basis Projection**
- **Test**: Movement basis is projected correctly on the ground plane.
  - Given: Camera is tilted at a 45-degree angle.
  - When: Fetching movement basis.
  - Then: Forward vector has Y = 0 and is normalized.

**AC-2: Movement Feel**
- **Manual check**: Movement feels grounded and responsive in Tokyo Street.
  - Setup: Load M0 arena.
  - Verify: Character moves in sync with input relative to camera view.
  - Pass condition: 100% directional accuracy.

---

## Test Evidence

**Story Type**: Logic/Integration
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/LocomotionBasis_test.cs`
- Manual verification: Video clip or screenshot showing movement basis debug rays.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-1
- Unlocks: Story 1-4

## Completion Notes
**Completed**: 2026-05-15
**Criteria**: 4/4 passing
**Tests**: EditMode 15/15 passing
**Code Review**: APPROVED WITH SUGGESTIONS — adapter guard fix applied, build validation PASS, PlayMode zero errors
**Result**: COMPLETE WITH NOTES
**Advisory notes**:
- Manual screenshot/video evidence not provided; PlayMode verification reported clean.
- M0LocomotionSettings remains inline/hardcoded for M0 prototype.
- CameraMovementBasisProvider cross-scene serialized reference may be unassigned at edit time and is gracefully handled with warning.
