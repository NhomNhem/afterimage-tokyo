## 1. Foundation Review

- [x] 1.1 Inspect the existing M0 contracts, input router, and adjacent target-facing GDD constraints
- [x] 1.2 Confirm the architecture and GDD constraints for target truth ownership, read-only snapshots, and downstream observation

## 2. Target Contract Setup

- [x] 2.1 Define or refine the target state/focus model if needed
- [x] 2.2 Define the read-only target snapshot shape
- [x] 2.3 Define acquire/release request and validity context shapes

## 3. Target Skeleton

- [x] 3.1 Implement a lightweight pure C# target context FSM/service skeleton
- [x] 3.2 Consume raw LockOn intent as request data only
- [x] 3.3 Expose a read-only target snapshot for future locomotion, camera, combat, and debug consumption

## 4. Verification

- [x] 4.1 Add edit mode tests for acquire, focus, release, and invalid target behavior
- [x] 4.2 Run no-legacy-input and no-generated-DI checks
- [x] 4.3 Update the task checklist only after each task is complete and verified
