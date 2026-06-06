## Why

M0 runtime composition still contains bootstrap-time scene discovery fallbacks (`FindFirstObjectByType` / `FindObjectsByType`) for memory probe and fragment wiring. This keeps `GameplayLifetimeScope` responsible for both DI composition and scene inventory discovery, which weakens NhemDI ownership, makes setup failures less explicit, and increases risk as M0/M1 memory loop wiring grows.

This change proposes the first refactor-wave slice: harden runtime composition around NhemDI and explicit scene adapters while preserving the verified `read -> evade/parry -> counter -> reveal` loop.

## What Changes

- Replace M0/M1 runtime composition fallbacks with explicit, verifiable composition boundaries for scene-provided memory participants.
- Keep NhemDI as the preferred registration path for gameplay runtime services in `IGameplayLifetimeScope`.
- Keep `GameplayLifetimeScope` focused on scope composition and generated/attribute-backed registrations.
- Introduce or refine narrow scene composition adapters/providers only where scene objects must be bridged into runtime services.
- Add validation/evidence requirements proving missing scene composition is detected clearly without broad service locator behavior.
- Preserve S3-2/S3-3/S3-4/S4-2 behavior:
  - eligible fragment prompt
  - Interact accepted path
  - reveal feedback once
  - runtime memory log append
  - duplicate/spam Interact parity
- Keep this slice behavior-preserving. Any runtime behavior change requires a separate approved OpenSpec change.

## Capabilities

### New Capabilities
- `m0-runtime-composition-nhemdi`: Harden M0 runtime dependency composition by removing broad scene discovery fallback behavior and requiring explicit NhemDI/scoped composition boundaries for gameplay services and scene-provided participants.

### Modified Capabilities
- None.

## Impact

- Affected ownership boundary:
  - **Bootstrap/DI**: owns composition and setup validation only.
  - **MemoryInteraction**: remains interaction orchestration truth.
  - **MemoryState**: remains reveal/collect truth.
  - **Presentation/UI/VFX**: remain observers/adapters only.
- Likely affected files during apply:
  - `afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
  - scene adapter/provider types under `Assets/_Project/Code/Bootstrap/` or ownership-specific folders
  - focused EditMode tests for composition guardrails and memory path parity
- No intended impact to:
  - CombatCore timing/result behavior
  - Input architecture
  - PlayerLocomotion truth
  - TargetContext truth
  - MemoryState acceptance policy
  - MemoryInteractionService behavior
  - Unity scene/prefab assets in this proposal
  - broad ScriptableObject migration
  - R3/MessagePipe migration

## Non-goals

- No CombatCore state-machine refactor.
- No combat timing/result changes.
- No input architecture refactor.
- No `M0Contracts.cs` split in this change.
- No broad ScriptableObject authored-config migration.
- No R3/MessagePipe event/read-model migration.
- No MemoryRaycastProProbe behavior or alignment change unless needed only to expose an explicit dependency boundary.
- No scene/prefab edits unless a later approved implementation step explicitly scopes them.
- No Service Locator, `FindObjectOfType`, `FindFirstObjectByType`, `FindAnyObjectByType`, broad `FindObjectsByType`, or `Resources.Load` in owned runtime composition code.

## M0 Loop Impact

The change should improve setup reliability and maintainability without changing player-facing behavior. The tester should still observe the same M0/M1 memory path: eligible fragment prompt appears, Interact is accepted, reveal feedback appears once, runtime memory log records the reveal, and spam Interact does not replay or append incorrectly.
