# Story 1-6: [Combat] Parry & Dodge Integration

> **Epic**: M0 First Playable Duel
> **Status**: Implemented - Needs Human PlayMode Verification
> **Layer**: Core
> **Type**: Logic/Integration
> **Estimate**: 1.0d
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-05-19

## Context

**GDD**: `design/gdd/combat-core.md`
**Requirement**: `TR-M0-COMBAT-001`

**ADR Governing Implementation**: [ADR-0002: M0 Gameplay Truth Ownership Boundaries]
**ADR Decision Summary**: Combat Core owns parry/dodge validation; Locomotion expresses dodge movement.

**Engine**: Unity 6000.3.x | **Risk**: LOW

**Control Manifest Rules (this layer)**:
- Required: Lock/Recovery Request Pattern (Dodge recovery emitted by Core).
- Forbidden: Presentation (VFX/Animator) does not decide results.

---

## Acceptance Criteria

- [ ] Parry intent from Input resolves against enemy Active timing.
- [ ] Dodge intent from Input triggers `DodgeRequestContext` and resolves success/fail in Core.
- [ ] Successful Parry opens `CounterWindow` in `CombatCore`.
- [ ] Dodge displacement and recovery are expressed in `M0PlayerLocomotion`.

---

## Implementation Notes

- Connect `M0InputRouter` Parry/Dodge intents to `M0CombatCore`.
- Use the `CombatCore` FSM to manage defensive timing windows.
- Coordinate with `M0PlayerLocomotion` to apply movement phase for dodge.

---

## Out of Scope

- [Story 1-10]: Memory reveal response.

---

## QA Test Cases

**AC-1: Parry Window**
- **Test**: Parry succeeds within valid window.
  - Given: Enemy is in Active state.
  - When: Parry intent is received during the parry window.
  - Then: Result is Success and CounterWindow.IsOpen is true.

**AC-2: Dodge Resolution**
- **Test**: Dodge fails if timing is completely off.
  - Given: Enemy hit is already resolving.
  - When: Dodge intent is received too late.
  - Then: CombatCore result is Fail/Hit.

---

## Test Evidence

**Story Type**: Logic/Integration
**Required evidence**:
- Logic: `Assets/_Project/Tests/EditMode/M0DefensiveResolutionTests.cs`
- Manual verification: Debug Overlay showing parry windows and dodge results.

**Status**: [ ] Not yet created

---

## Dependencies

- Depends on: Story 1-3, Story 1-4, Story 1-5
- Unlocks: Story 1-7, Story 1-10

---

## Completion Notes
**Completed**: Not fully complete as of 2026-05-19 validation
**Criteria**: Basic Dodge and Parry action cycles verified; CounterWindow open/accepted counter path remains unverified
**Deviations**: Previous completion claim was too broad for current verified evidence
**Test Evidence**: Dodge input routed and progressed Neutral -> DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral. Parry input routed and progressed Neutral -> ParryStartup -> ParryActive -> ParryRecovery -> Neutral. Parry failure was correct because enemy intent was not parry-eligible. CounterWindow open/accepted counter path and RevealBeat path not verified.
**Code Review**: APPROVED WITH SUGGESTIONS
**Scene Wiring**: Gameplay_CombatPrototype.unity fixed and saved (M0GameplayTickHandler references corrected to GameObject instanceIDs)

## Verification Update — 2026-05-19

**Validated Status**: IMPLEMENTED - NEEDS HUMAN PLAYMODE VERIFICATION

**What Was Verified (EditMode)**:
- All M0DefensiveResolutionTests passed.
- New test CounterAcceptedTransitionsToCounterActiveAndEmitsRevealRequest added and passed.
- CounterWindow opens on successful parry with ParryEligible enemy.
- Counter can be accepted from Neutral while CounterWindow is open.
- Counter acceptance transitions to CounterActive and emits RevealRequestContext.

**CounterWindow Duration Tuning Change**:
- Files changed: Assets/_Project/Code/Combat/M0CombatCore.cs
- Change type: M0 tuning (debug-only under GR_M0_PROTOTYPE)
- New CounterWindow duration: 3.0s (GR_M0_PROTOTYPE), 0.5s (production default)
- Purpose: Make manual PlayMode verification easier without changing final gameplay design
- Implementation: Conditional compilation with #if GR_M0_PROTOTYPE

**Deterministic Verification Harness Added**:
- Files changed: Assets/_Project/Code/Bootstrap/M0EnemyIntentLoopDriver.cs
- Change type: M0 debug-only verification helper (behind GR_M0_PROTOTYPE)
- Debug method: DebugForceParryEligibleActive()
- Debug trigger: Context menu item "Debug: Force ParryEligible Active (CounterWindow Verification)"
- Debug serialized field: debugParryEligibleActiveDuration = 3.0s
- Purpose: Force enemy into ParryEligible Active state for reliable manual PlayMode verification
- Implementation: Conditional compilation with #if GR_M0_PROTOTYPE
- No production behavior impact when GR_M0_PROTOTYPE is removed

**Manual PlayMode Verification Steps**:
1. Open Gameplay_CombatPrototype scene in Unity Editor
2. Enter PlayMode
3. Select Enemy_M0TargetablePlaceholder GameObject
4. In Inspector, right-click M0EnemyIntentLoopDriver component
5. Click "Debug: Force ParryEligible Active (CounterWindow Verification)"
6. Observe Console: [M0Debug] Forced enemy ParryEligible Active for 3.0s. Press Q to Parry.
7. Press Q once (Parry)
8. Observe Console logs:
   - [M0Combat] Parry success: CounterWindow opening
   - [M0Combat] CounterWindow opened duration=3
9. Wait for Combat state to return to Neutral (ParryRecovery completes)
10. Press E once (Counter)
11. Observe Console logs:
    - [M0Combat] Counter accepted
    - [M0Combat] RevealRequestContext emitted
12. Confirm Combat state transitions: Neutral → CounterActive → RevealBeat → Neutral
13. Confirm 0 gameplay errors in Console

**Required Log Evidence for Verification**:
Story 1-6 cannot be marked Verified until human PlayMode logs confirm:
- Q Parry success
- CounterWindow opens
- Combat returns to Neutral
- E Counter accepted
- CounterActive / RevealRequestContext occurs

**Verification Status**: EditMode verification complete. Human manual PlayMode verification required using deterministic debug harness. Follow manual steps above. Story 1-6 must remain IMPLEMENTED - NEEDS HUMAN PLAYMODE VERIFICATION until logs confirm all required evidence.
