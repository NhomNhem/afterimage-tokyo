## 1. Foundation Review

- [x] 1.1 Inspect architecture and GDD boundaries for Health, Combat Core, Locomotion, Enemy Intent, Memory, and Debug ownership
- [x] 1.2 Confirm M0 scope constraints for consequence skeleton only (no hitbox/animation/physics/stat systems)
- [x] 1.3 Confirm `M0Contracts.cs` additions remain contract-only and introduce no behavior logic

## 2. Health Contract Setup

- [x] 2.1 Define/refine health state model (living/damaged/recovering/defeated or disabled)
- [x] 2.2 Define damage application request shape (source, target, amount/context placeholders)
- [x] 2.3 Define damage application result shape (accepted/rejected/ignored + reason)
- [x] 2.4 Define hit reaction context placeholder shape
- [x] 2.5 Define defeat/disabled context placeholder shape
- [x] 2.6 Define read-only health/reaction snapshot shape for Debug Overlay observers

## 3. Health Skeleton

- [x] 3.1 Implement lightweight pure C# health/damage/hit reaction FSM/service skeleton in Health module
- [x] 3.2 Implement damage request intake and consequence result emission (validation shape only)
- [x] 3.3 Implement health value update path for accepted damage requests
- [x] 3.4 Implement hit reaction placeholder context emission after accepted damage
- [x] 3.5 Implement defeated/disabled placeholder transition when health threshold is reached
- [x] 3.6 Expose read-only health/reaction snapshot and optional change event for observer systems
- [x] 3.7 Keep Combat Core integration context-only (Combat Core does not apply damage)
- [x] 3.8 Keep Locomotion integration context-only (Locomotion owns movement-side expression)

## 4. Verification

- [x] 4.1 Add edit-mode tests for damage request/result behavior
- [x] 4.2 Add edit-mode tests for health snapshot consistency with accepted/rejected damage
- [x] 4.3 Add edit-mode tests for hit reaction placeholder behavior
- [x] 4.4 Add edit-mode tests for defeated/disabled state behavior
- [x] 4.5 Add read-only snapshot immutability/consumer-safety checks
- [x] 4.6 Run no-legacy-input and no-generated-DI checks for new health files
- [x] 4.7 Validate no hitbox/animation/ragdoll/physics/UI/enemy-AI/combat-validation/memory-acceptance/scene-wiring dependencies were introduced
- [x] 4.8 Validate Combat Core `CounterWindow` and Enemy `EnemyPunishWindow` ownership remain unaffected
- [x] 4.9 Update this task checklist only after each item is complete and verified
