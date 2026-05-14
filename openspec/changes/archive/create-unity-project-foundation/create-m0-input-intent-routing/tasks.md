## 1. Foundation Review

- [x] 1.1 Inspect the existing M0 input foundation, `M0Contracts.cs`, and `M0InputActions.inputactions`
- [x] 1.2 Confirm the architecture and GDD constraints for input intent, debug visibility, and downstream ownership

## 2. Contract Refinement

- [x] 2.1 Define or refine input intent DTOs and routing result shapes in shared core contracts if needed
- [x] 2.2 Define the read-only input snapshot shape, including enabled/disabled state and latest raw action values
- [x] 2.3 Define downstream rejection reporting so input can record ignored/routed/rejected outcomes without owning validation

## 3. Input Routing Surface

- [x] 3.1 Implement a lightweight input router/facade under `Assets/_Project/Code/Input`
- [x] 3.2 Wire the router to Unity New Input System action callbacks and raw intent emission
- [x] 3.3 Expose the debug-readable input snapshot/event surface without adding gameplay behavior

## 4. Verification

- [x] 4.1 Add tests for snapshot shape, routing outcome distinctions, and read-only access
- [x] 4.2 Add checks that verify no legacy Unity Input Manager references are introduced
- [x] 4.3 Update the task checklist only after each task is complete and verified
