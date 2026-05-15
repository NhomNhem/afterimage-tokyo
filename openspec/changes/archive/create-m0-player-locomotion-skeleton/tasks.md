## 1. Foundation Review

- [x] 1.1 Inspect the existing M0 contracts, input router, and locomotion assembly boundaries
- [x] 1.2 Confirm the architecture and GDD constraints for movement truth, read-only debug data, and restriction/recovery ownership

## 2. Locomotion Contract Setup

- [x] 2.1 Define or refine the locomotion state enum/model if needed
- [x] 2.2 Define the read-only locomotion snapshot shape
- [x] 2.3 Define the movement restriction and recovery/action-lock context shape

## 3. Locomotion Skeleton

- [x] 3.1 Implement a lightweight pure C# locomotion FSM/service skeleton
- [x] 3.2 Consume raw movement intent as data only from the input routing layer
- [x] 3.3 Expose a read-only debug snapshot for future Debug Overlay consumption

## 4. Verification

- [x] 4.1 Add edit mode tests for idle, moving, restricted, and recovering snapshot behavior
- [x] 4.2 Run no-legacy-input and no-generated-DI checks
- [x] 4.3 Update the task checklist only after each task is complete and verified
