## 1. Foundation Review

- [x] 1.1 Review architecture and GDD boundaries for Memory State, Combat Core, Health, and Debug ownership
- [x] 1.2 Confirm M0 skeleton-only scope and explicitly exclude VFX/narrative/content/persistence/cutscene subsystems
- [x] 1.3 Confirm `M0Contracts.cs` updates remain contracts-only with no behavior logic

## 2. Memory Contract Setup

- [x] 2.1 Define/refine reveal request context shape in `M0Contracts.cs`
- [x] 2.2 Define/refine reveal acceptance/rejection result shape with readable reason/context placeholders
- [x] 2.3 Define/refine memory response and cooldown state shapes
- [x] 2.4 Define/refine read-only memory snapshot shape for Debug Overlay and observers
- [x] 2.5 Define/refine request classification markers needed to reject generic-hit/failed-defense/presentation-only reveal triggers

## 3. Memory State Skeleton

- [x] 3.1 Implement pure C# `M0MemoryState` skeleton model under Memory module
- [x] 3.2 Implement dormant -> requested transition behavior for reveal request intake
- [x] 3.3 Implement requested -> accepted and requested -> rejected result behavior
- [x] 3.4 Implement accepted -> responding -> cooldown phase progression behavior
- [x] 3.5 Implement rejected path behavior returning to stable state with explicit result context
- [x] 3.6 Enforce that generic hit, failed dodge, failed parry, invalid counter, and presentation-only requests cannot be accepted
- [x] 3.7 Expose read-only snapshot and optional change notification for observer systems
- [x] 3.8 Keep Combat Core as reveal request context producer only (no reveal acceptance authority)
- [x] 3.9 Keep Health as consequence context provider only (no reveal acceptance authority)

## 4. Verification

- [x] 4.1 Add edit-mode tests for dormant/requested/accepted/rejected/responding/cooldown behavior
- [x] 4.2 Add edit-mode tests confirming rejected generic-hit/failed-defense/presentation-only triggers
- [x] 4.3 Add edit-mode tests confirming snapshot read-only behavior and phase/result consistency
- [x] 4.4 Add edit-mode tests confirming Combat Core/Health are not reveal acceptance authorities
- [x] 4.5 Run static checks for no legacy Input Manager and no Nhem generated DI usage
- [x] 4.6 Validate no non-goal systems slipped in (VFX, narrative graph, clue DB, branching memory, district reinterpretation, save/persistence, cutscene, combat validation, damage application, scene/prefab wiring)
- [x] 4.7 Validate VContainer usage remains manual scope wiring
- [x] 4.8 Update this task checklist only after each item is implemented and verified
