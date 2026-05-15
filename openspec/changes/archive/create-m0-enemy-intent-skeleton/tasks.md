## 1. Foundation Review

- [x] 1.1 Inspect architecture and GDD ownership boundaries for Enemy Intent, Combat Core, Health, Locomotion, Target, and Debug Overlay
- [x] 1.2 Confirm scope constraints for M0 enemy intent skeleton (single-enemy readability contracts only)
- [x] 1.3 Confirm `M0Contracts.cs` additions remain contract-only and do not introduce behavior logic

## 2. Enemy Contract Setup

- [x] 2.1 Define or refine enemy intent state enum for idle/telegraph/commit/active/recovery flow
- [x] 2.2 Define enemy telegraph snapshot placeholder shape
- [x] 2.3 Define basic enemy attack intent placeholder shape
- [x] 2.4 Define enemy attack tag representation for M0
- [x] 2.5 Define `EnemyPunishWindow` context placeholder (open/closed/source/remaining)
- [x] 2.6 Define read-only enemy intent snapshot for Debug Overlay consumption

## 3. Enemy Intent Skeleton

- [x] 3.1 Implement lightweight pure C# enemy intent FSM/service skeleton in Enemy module
- [x] 3.2 Implement Idle baseline state
- [x] 3.3 Implement Telegraph state and snapshot updates
- [x] 3.4 Implement Commit/Active/Recovery placeholder path
- [x] 3.5 Implement enemy attack tag assignment in intent/result snapshot context
- [x] 3.6 Implement `EnemyPunishWindow` placeholder open/close on enemy-side transition rules
- [x] 3.7 Expose read-only enemy intent snapshot and optional change event for observer systems
- [x] 3.8 Keep Combat Core interaction observer-only (no Combat Core authority takeover)

## 4. Verification

- [x] 4.1 Add edit-mode tests for idle state snapshot behavior
- [x] 4.2 Add edit-mode tests for telegraph state snapshot behavior
- [x] 4.3 Add edit-mode tests for commit/active/recovery transition snapshot behavior
- [x] 4.4 Add edit-mode tests for `EnemyPunishWindow` placeholder open/close behavior
- [x] 4.5 Add edit-mode tests for enemy attack tag snapshot behavior
- [x] 4.6 Add read-only snapshot immutability/consumer-safety checks
- [x] 4.7 Run no-legacy-input and no-generated-DI checks for new enemy intent files
- [x] 4.8 Validate no NavMesh/Animator/hitbox/damage/scene wiring dependencies were introduced
- [x] 4.9 Update this task checklist only after each item is complete and verified
