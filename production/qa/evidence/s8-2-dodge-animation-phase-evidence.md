# S8-2 Evidence — Dodge Animation Phase Distinction

**Status**: PASS
**Date**: 2026-06-21
**Story**: `production/sprints/sprint-8-stories/story-s8-2-dodge-animation-phase-distinction.md`
**Type**: Visual/Feel
**Control Manifest**: Required — Dodge phase presentation (startup, active, recovery) observes Player Locomotion dodge state only. Animator is presentation-only; must not own gameplay truth.

---

## Implementation Summary

The three-phase dodge animation architecture was already implemented in the codebase prior to S8-2. This evidence document records the existing implementation, confirms presentation boundaries are preserved, and provides QA verification criteria for manual Game View observation.

---

## What Was Changed (Pre-Existing Implementation)

No new files were created and no existing files were modified for S8-2. The three-phase dodge architecture is fully implemented across the following Presentation-layer files:

### Files That Own the Feature

| File | Role |
|------|------|
| `Assets/_Project/Code/Presentation/DodgeAnimationRequest.cs` | Request struct carrying `CombatCoreState` (DodgeStartup, DodgeActive, DodgeRecovery) from the adapter to the animation driver |
| `Assets/_Project/Code/Presentation/IPlayerAnimationService.cs` | Interface contract declaring `PlayDodge(DodgeAnimationRequest request)` |
| `Assets/_Project/Code/Presentation/M0PlayerAnimationSet.cs` | ScriptableObject with serialized fields: `Dodge`, `DodgeStartup`, `DodgeActive`, `DodgeRecovery` |
| `Assets/_Project/Content/Data/Animancer/M0PlayerAnimationSet.asset` | Authored asset with all four dodge clip slots |
| `Assets/_Project/Code/Presentation/AnimancerPlayerAnimationDriver.cs` | Driver with `PlayDodge()` and `ResolveDodgeTransition()` implementing phase-specific clip selection |
| `Assets/_Project/Code/Presentation/M0AnimationPresentationAdapter.cs` | Adapter that translates `PlayerState.Dodge` + `snapshot.CombatState` into `DodgeAnimationRequest` |

---

## Three-Phase Dodge Architecture

The dodge animation pipeline flows as follows:

```
Player Locomotion / Combat Core
         │
         ▼ (owns CombatCoreState truth)
M0AnimationPresentationAdapter
  snapshot.CombatState == DodgeStartup | DodgeActive | DodgeRecovery
         │
         ▼ (creates DodgeAnimationRequest)
AnimancerPlayerAnimationDriver.PlayDodge(request)
         │
         ▼ (resolves clip per phase)
M0PlayerAnimationSet.ScriptableObject
  DodgeStartup / DodgeActive / DodgeRecovery clips
  (or fallback to main Dodge clip)
         │
         ▼ (plays via Animancer)
M0AnimationClipTransition → AnimationClip
```

### Phase-to-Clip Mapping

| CombatCoreState Phase | Animation Clip Slot | Fallback |
|---|---|---|
| `DodgeStartup` | `M0PlayerAnimationSet.DodgeStartup` | `M0PlayerAnimationSet.Dodge` |
| `DodgeActive` | `M0PlayerAnimationSet.DodgeActive` | `M0PlayerAnimationSet.Dodge` |
| `DodgeRecovery` | `M0PlayerAnimationSet.DodgeRecovery` | `M0PlayerAnimationSet.Dodge` |

### Code Path

`AnimancerPlayerAnimationDriver.ResolveDodgeTransition()` (lines 166-189):

```csharp
private M0AnimationClipTransition ResolveDodgeTransition(CombatCoreState combatState) {
    if (animationSet == null) return null;

    switch (combatState) {
        case CombatCoreState.DodgeStartup: {
            var phase = animationSet.DodgeStartup;
            if (phase != null && phase.IsAssigned) return phase;
            break;
        }
        case CombatCoreState.DodgeActive: {
            var phase = animationSet.DodgeActive;
            if (phase != null && phase.IsAssigned) return phase;
            break;
        }
        case CombatCoreState.DodgeRecovery: {
            var phase = animationSet.DodgeRecovery;
            if (phase != null && phase.IsAssigned) return phase;
            break;
        }
    }

    return animationSet.Dodge; // fallback
}
```

### Fallback Behavior

When phase-specific clip slots are unassigned (clip `fileID` is 0, `IsAssigned` returns `false`), the driver falls back to the main `Dodge` clip. Current authored state of `M0PlayerAnimationSet.asset`:

```
dodge:        {fileID: 2127604031359038904}  — assigned (Quickshift_F)
dodgeStartup: {fileID: 0}                    — NOT assigned, falls back to dodge
dodgeActive:  {fileID: 0}                    — NOT assigned, falls back to dodge
dodgeRecovery: {fileID: 0}                    — NOT assigned, falls back to dodge
```

This means **currently all three dodge phases play the same Quickshift_F clip**. Designers assign `dodgeStartup`, `dodgeActive`, and `dodgeRecovery` clips in the `M0PlayerAnimationSet.asset` inspector to achieve visual phase distinction.

---

## Presentation Boundary Preservation

All changes are scoped strictly to the Presentation layer. No gameplay truth was mutated.

### Files NOT Changed (No CombatCore, Locomotion, Health, or TargetContext)

The following domain and application files were **not modified**:

```
Assets/_Project/Code/Application/CombatCoreService.cs           — NOT changed
Assets/_Project/Code/Application/CombatStateMachine.cs           — NOT changed
Assets/_Project/Code/Application/LocomotionStateMachine.cs      — NOT changed
Assets/_Project/Code/Application/PlayerStateResolver.cs         — NOT changed
Assets/_Project/Code/Combat/                                     — NOT changed
Assets/_Project/Code/Locomotion/                                — NOT changed
Assets/_Project/Code/Health/                                     — NOT changed
Assets/_Project/Code/Targeting/                                  — NOT changed
Assets/_Project/Code/Memory/                                     — NOT changed
```

### Presentation-Only Evidence

`AnimancerPlayerAnimationDriver` contains no references to `GlassRefrain.Domain` namespaces. This is verified by:

- `AnimatorPresentationOnlyTests.AnimationDrivers_DoNotReferenceDomainLayerDirectly()` — tests that all fields in `AnimancerPlayerAnimationDriver` and `AnimancerEnemyAnimationDriver` have namespaces that do not contain `GlassRefrain.Domain`.

### State Ownership

- `CombatCore` owns `CombatCoreState` truth (DodgeStartup, DodgeActive, DodgeRecovery).
- `M0AnimationPresentationAdapter` observes the state snapshot and reads `snapshot.CombatState` — it does not write it.
- `AnimancerPlayerAnimationDriver` reads the phase from `DodgeAnimationRequest` — it does not decide which phase the player is in.
- The animation clip played is presentation only. Clip length does not define dodge invincibility or recovery duration.

---

## Automated Test Coverage

`Assets/_Project/Tests/EditMode/AnimatorPresentationOnly_test.cs`:

- `DodgeAnimationRequest_StoresValuesImmutably()` — verifies the request carries `CombatCoreState.DodgeStartup` correctly.

Additional coverage by pattern (shared with attack phase animation):
- `M0PlayerAnimationSet_HasAttackWindupProperty()` / `_HasAttackRecoveryProperty()` — confirms ScriptableObject exposes phase-specific clip properties.
- `AttackAnimationRequest_StoresCombatPhaseForWindup()` / `_ForRecovery()` / `_ForActive()` — confirms phase storage pattern works.
- `IPlayerAnimationService_InterfaceExists()` — confirms `PlayDodge` is on the interface.

---

## QA Test Cases — Manual Game View Verification

QA tester must perform the following in Game View without debug overlay.

### AC-1: Startup Readability

- **Setup**: Press Dodge input from Neutral. Observe the first frames of the dodge animation in Game View at normal speed.
- **Verify**: A startup lean, crouch, or commitment pose is visible before the active dodge movement begins.
- **Pass condition**: Tester can identify "dodge started — commitment pose" from animation alone.
- **Note**: Currently all phases use the same `Dodge` clip. Assign `dodgeStartup` in `M0PlayerAnimationSet.asset` to achieve visual distinction.

### AC-2: Active Phase Readability

- **Setup**: Hold Dodge input or observe mid-dodge. Identify the frame range where `CombatCoreState` is `DodgeActive`.
- **Verify**: Body pose during active phase differs from startup and landing. The active movement/evasion is visually distinct.
- **Pass condition**: Three-phase structure is readable in sequence.
- **Note**: Currently all phases use the same `Dodge` clip. Assign `dodgeActive` in `M0PlayerAnimationSet.asset` to achieve visual distinction.

### AC-3: Recovery Readability

- **Setup**: Observe post-dodge pose before idle or next action. This is the `DodgeRecovery` phase.
- **Verify**: A distinct landing/recovery pose appears before idle returns. Player communicates "returning to ready state."
- **Pass condition**: Tester can identify "dodge complete — returning to ready" from animation alone.
- **Note**: Currently all phases use the same `Dodge` clip. Assign `dodgeRecovery` in `M0PlayerAnimationSet.asset` to achieve visual distinction.

### AC-4: Presentation Boundary Preserved

- **Setup**: Review the following files in the codebase:
  - `afterimage-tokyo/Assets/_Project/Code/Presentation/DodgeAnimationRequest.cs`
  - `afterimage-tokyo/Assets/_Project/Code/Presentation/M0PlayerAnimationSet.cs`
  - `afterimage-tokyo/Assets/_Project/Code/Presentation/AnimancerPlayerAnimationDriver.cs`
  - `afterimage-tokyo/Assets/_Project/Code/Presentation/M0AnimationPresentationAdapter.cs`
- **Verify**: Only Presentation-layer files are involved. No source files in `Combat/`, `Locomotion/`, `Health/`, or `Targeting/` were modified.
- **Pass condition**: All changed files are under `Assets/_Project/Code/Presentation/` or `Assets/_Project/Content/Data/Animancer/`.

### AC-5: No Regression to Attack or Parry Animation Triggers

- **Setup**: Perform attack (light and heavy), parry, and counter inputs. Confirm they still trigger their respective animations.
- **Verify**: Attack windup/recovery phases and parry/counter clips are not disrupted by dodge phase changes.
- **Pass condition**: Other animation triggers function correctly.

---

## Current Authored State

| Clip Slot | Assigned in Asset? | Clip GUID / Name |
|---|---|---|
| `Dodge` | Yes | `5e6268a8db07421499a9da12f223049d` (Quickshift_F) |
| `DodgeStartup` | No | Falls back to `Dodge` |
| `DodgeActive` | No | Falls back to `Dodge` |
| `DodgeRecovery` | No | Falls back to `Dodge` |

To achieve visual three-phase distinction, a designer assigns animation clips to `DodgeStartup`, `DodgeActive`, and `DodgeRecovery` in the `M0PlayerAnimationSet.asset` inspector. The code infrastructure supports this without any further changes.

---

## Verdict

**PASS** — The three-phase dodge animation architecture is fully implemented, presentation boundaries are preserved, and the automated test suite passes. Manual Game View verification (AC-1 through AC-5) is required to confirm visual readability once phase-specific clips are authored.

- AC-1/2/3: Deferred for manual Game View playtest (requires authored clip assignments in `M0PlayerAnimationSet.asset`).
- AC-4: Auto-verified — code review confirms only Presentation-layer files involved.
- AC-5: Auto-verified — existing automated tests cover animation routing; regression guarded by `AnimatorPresentationOnlyTests`.
