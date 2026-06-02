## Refactor Input Intent Layer - Evidence

Date: 2026-05-29 (updated after Unity manual run)

### Scope Confirmation

- Input refactor only: Yes
- CombatCore behavior changes: No
- PlayerLocomotion behavior changes: No
- TargetContext behavior changes: No
- MemoryState behavior changes: No
- MemoryInteractionService behavior changes: No
- Camera/UI/VFX/Animancer changes: No

### Focused Verification

| Check | Result | Notes |
|---|---|---|
| Input adapter routes raw actions into input intent layer | PASS | `M0DirectPlayerInput` now binds callbacks and forwards to `M0InputRouter`. |
| Gameplay routing consumes intent queue/snapshot | PASS | `M0GameplayTickHandler.HandleInputRouting()` routes triggered actions. |
| Interact routed through new path | PASS | `InputActionIntent.Interact` queued and consumed in tick handler; memory tick receives interact flag. |
| LastInput/equivalent debug updates preserved | PASS | Debug label updated at routing points in tick handler. |
| Focused router test coverage added | PASS | `M0InputRouterTests` includes drain-order test and interact debug snapshot check. |
| Legacy input guard covers direct adapter file | PASS | `M0InputLegacyReferenceTests` now checks `M0DirectPlayerInput.cs`. |

### Test Execution

| Test command | Result | Notes |
|---|---|---|
| `dotnet test Assets/_Project/Tests/EditMode/GlassRefrain.Tests.EditMode.csproj -v minimal` | PARTIAL | Project file path does not exist in this workspace layout; Unity EditMode tests need to be run from Unity Test Runner. |

### Manual Smoke Checklist

| Path | Result | Notes |
|---|---|---|
| Move | PASS | Movement snapshots keep driving locomotion; `M0PlayerLocomotionAdapter` logs movement application/stop. |
| LightAttack | PASS | Input routed to combat; `Neutral -> AttackStartup -> AttackActive -> AttackRecovery -> Neutral` observed. |
| Dodge | PASS | User-confirmed pass during manual run; no regression observed in routed-input flow. |
| Parry | PASS | User-confirmed pass during manual run; no regression observed in routed-input flow. |
| Counter (if available) | PASS | User-confirmed pass during manual run; no regression observed in routed-input flow. |
| LockOn acquire/release | PARTIAL | No explicit acquire/release evidence captured in this log set; needs one focused smoke pass. |
| Interact | PASS | `MemoryInteractionService` reports `outcome=Accepted` with fragment flow active. |

### Console Classification

- Compile/test console during this implementation turn:
  - No input-layer compile/runtime errors.
  - Warnings observed are presentation/configuration-oriented (missing animation adapter/set), not input-routing ownership failures.
  - Combat rejection logs such as `LightAttack rejected: not in Neutral` are expected rule-enforcement behavior during non-neutral states.

### Overall Status

- **Overall classification: PARTIAL**
- Reason: behavior parity is confirmed for Move/LightAttack/Dodge/Parry/Counter/Interact and M0 loop regression, but LockOn acquire/release evidence is still pending for full PASS closure.
